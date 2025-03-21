from flask import Flask, request, jsonify
from auth.supabase_auth import verify_token
from linkedin.linkedin_fetch import fetch_linkedin
from ai.gemini import generate_recommendations
from resume.resume_generator import resume_generator

 # Updated function name

app = Flask(__name__)

# Authentication Route (Verify Supabase Token)
@app.route("/api/auth/verify", methods=["GET"])
def auth_verify():
    return verify_token()

# Fetch LinkedIn Data using RapidAPI
@app.route("/api/linkedin", methods=["POST"])
def linkedin_fetch():
    return fetch_linkedin()

# AI-Based Job & Skill Recommendations
@app.route("/api/recommendations", methods=["POST"])
def ai_recommend():
    return generate_recommendations()

# AI-Powered Resume Generation
@app.route("/api/resume/generate", methods=["POST"])
def resume_generate():
    return resume_generator()

# Send Resume via Email


if __name__ == "__main__":
    app.run(debug=True)
