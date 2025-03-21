from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB Connection
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")  # Default to local MongoDB if not set
client = MongoClient(MONGO_URL)
db = client["ai_resume_generator"]

# Collections
users = db["users"]
resumes = db["resumes"]

def create_user(user_id, email):
    """Creates a new user in the database if they don't already exist."""
    if not users.find_one({"user_id": user_id}):
        users.insert_one({"user_id": user_id, "email": email, "resumes": []})
        return {"status": "success", "message": "User created successfully"}
    return {"status": "exists", "message": "User already exists"}

def save_resume(user_id, resume_text):
    """Saves a generated resume for a user."""
    resume_data = {
        "user_id": user_id,
        "resume": resume_text
    }
    resumes.insert_one(resume_data)
    return {"status": "success", "message": "Resume saved successfully"}

def get_resumes_by_user(user_id):
    """Retrieves all resumes for a given user."""
    return list(resumes.find({"user_id": user_id}, {"_id": 0}))

def get_user_by_id(user_id):
    """Fetches user details by ID."""
    return users.find_one({"user_id": user_id}, {"_id": 0})

def delete_resume(user_id):
    """Deletes all resumes associated with a user."""
    result = resumes.delete_many({"user_id": user_id})
    return {"status": "success", "deleted_count": result.deleted_count}
