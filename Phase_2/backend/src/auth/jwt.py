import os
from typing import Optional, Dict
from jose import jwt, JWTError
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: Dict) -> str:
    """Create JWT token."""
    if not JWT_SECRET:
        raise Exception("JWT_SECRET not found in environment")

    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)
    return encoded_jwt


def verify_jwt(token: str) -> Optional[Dict]:
    """Verify the JWT signature and return payload."""
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
    """Extract user id from payload."""
    return payload.get("sub")