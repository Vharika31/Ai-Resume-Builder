import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import google.genai as genai
from google.genai import types
from linkedin.linkedin_fetch import fetch_linkedin  # Ensure correct import

# Load environment variables
load_dotenv()

# Configure Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini Client
client = genai.Client(api_key=GEMINI_API_KEY)

app = Flask(__name__)

@app.route("/api/resume/generate", methods=["POST"])
def resume_generator():
    """
    Generates a professional resume using LinkedIn data.
    """
    data = request.json
    linkedin_id = data.get("linkedin_id")

    # Fetch user data from LinkedIn
    user_data = fetch_linkedin(linkedin_id)
    if not user_data:
        return jsonify({"error": "Failed to fetch LinkedIn data"}), 400

    name = user_data.get("name", "User")
    experience = user_data.get("experience", "No experience available")
    skills = user_data.get("skills", [])

    # Construct prompt for AI resume generator
    input_text = f"""
    Generate a professional resume for {name}.
    Experience: {experience}
    Skills: {', '.join(skills)}.
    Include a strong summary, work experience, skills, and education sections.
    Format the response as a well-structured resume.
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

    # Generate resume using Gemini API
    model = "gemini-2.0-flash"
    response_text = ""

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        response_text += chunk.text

    return jsonify({"resume": response_text})

if __name__ == "__main__":
    app.run(debug=True)
