import os
from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from dotenv import load_dotenv

# Load from project root
load_dotenv(os.path.join(os.path.dirname(__file__), "../../../.env"))

JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 # 24 hours

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    if not JWT_SECRET:
        raise ValueError("JWT_SECRET not found in environment")
        
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    # Ensure 'sub' is used for user ID
    if "user_id" in to_encode and "sub" not in to_encode:
        to_encode["sub"] = to_encode.pop("user_id")
        
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)
    return encoded_jwt
