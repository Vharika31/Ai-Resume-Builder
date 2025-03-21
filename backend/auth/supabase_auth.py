import requests
from flask import request
import os
from dotenv import load_dotenv
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

def verify_token():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return {"error": "Unauthorized"}, 401

    token = auth_header.split(" ")[1]
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{SUPABASE_URL}/auth/v1/user", headers=headers)

    if response.status_code == 200:
        return response.json(), 200
    return {"error": "Invalid token"}, 401
