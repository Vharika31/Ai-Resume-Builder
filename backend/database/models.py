from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
MONGO_URL=os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client["ai_resume_generator"]

# Users Collection
users = db["users"]
resumes = db["resumes"]

def create_user(user_id, email):
    users.insert_one({"user_id": user_id, "email": email, "resumes": []})

def save_resume(user_id, resume_text):
    resumes.insert_one({"user_id": user_id, "resume": resume_text})
