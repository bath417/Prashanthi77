import os
from fastapi import Header, HTTPException

API_KEY = os.getenv("SECRET_KEY", "test123")

async def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return "authorized-user"