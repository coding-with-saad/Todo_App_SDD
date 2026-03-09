import os
from typing import Optional, Dict
from jose import jwt, JWTError
from datetime import datetime
from dotenv import load_dotenv

# Load from project root (two levels up from backend/src/auth)
load_dotenv(os.path.join(os.path.dirname(__file__), "../../../.env"))

JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"

def verify_jwt(token: str) -> Optional[Dict]:
    """Verify the JWT signature and return the payload if valid."""
    if not JWT_SECRET:
        print("CRITICAL: JWT_SECRET not found in environment!")
        return None
        
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        print(f"JWT Verification Failed: {e}")
        return None

def get_user_id_from_payload(payload: Dict) -> Optional[str]:
    """Extract user_id (sub) from JWT payload."""
    return payload.get("sub")
