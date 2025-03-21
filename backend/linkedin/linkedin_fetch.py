import requests
import os
from dotenv import load_dotenv
from flask import Blueprint, request, jsonify

# Load environment variables
load_dotenv()

# Fetch LinkedIn API credentials from .env
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_URL = os.getenv("RAPIDAPI_URL")

# Create a Flask Blueprint for LinkedIn Fetching
linkedin_bp = Blueprint("linkedin", __name__)

@linkedin_bp.route("/api/linkedin", methods=["POST"])
def fetch_linkedin(linkedin_id="harika31"):
    """
    Fetch user data from LinkedIn API using RapidAPI.
    """
    data = request.json
    linkedin_id = data.get("linkedin_id")

    headers = {"X-RapidAPI-Key": RAPIDAPI_KEY}
    params = {"id": linkedin_id}

    response = requests.get(RAPIDAPI_URL, headers=headers, params=params)

    if response.status_code == 200:
        return jsonify(response.json())

    return jsonify({"error": "Failed to fetch LinkedIn data"}), 400
