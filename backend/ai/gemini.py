import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import google.genai as genai
from google.genai import types
from linkedin.linkedin_fetch import fetch_linkedin

# Load environment variables
load_dotenv()

# Configure Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Ensure API key is available
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set. Please check your .env file.")

app = Flask(__name__)
client = genai.Client(api_key=GEMINI_API_KEY)

@app.route("/api/resume/generate", methods=["POST"])
def generate_recommendations():
    """
    Generates job recommendations based on LinkedIn profile data.
    """
    data = request.json
    linkedin_id = data.get("linkedin_id")

    # Fetch data from LinkedIn
    user_data = fetch_linkedin(linkedin_id)
    if not user_data:
        return jsonify({"error": "Failed to fetch LinkedIn data"}), 400

    name = user_data.get("name", "User")
    experience = user_data.get("experience", "No experience available")
    skills = user_data.get("skills", [])

    # Construct prompt for AI model
    input_text = f"""
    Based on the LinkedIn profile of {name}, analyze their experience and skills.
    Experience: {experience}
    Skills: {', '.join(skills)}

    Suggest:
    1. Best job roles they are suitable for.
    2. Skills they should improve for better opportunities.
    """

    # Prepare content for Gemini API
    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=input_text)],
        ),
    ]

    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        top_k=40,
        max_output_tokens=8192,
        response_mime_type="text/plain",
    )

    # Generate response using Gemini API
    client = genai.Client(api_key=GEMINI_API_KEY)
    model = "gemini-2.0-flash"
    response_text = ""

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        response_text += chunk.text

    return jsonify({"recommendations": response_text})

if __name__ == "__main__":
    app.run(debug=True)
