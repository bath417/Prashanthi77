import re
from fastapi import HTTPException
from datetime import datetime

# Simple in-memory session storage
user_sessions = {}

def validate_sector(sector: str):
    if not re.match("^[a-zA-Z ]+$", sector):
        raise HTTPException(status_code=400, detail="Invalid sector format")

def track_user_request(user: str):
    if user not in user_sessions:
        user_sessions[user] = 0

    user_sessions[user] += 1
    return user_sessions[user]

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")