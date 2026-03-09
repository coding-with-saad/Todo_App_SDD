from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr
from sqlmodel import Session
import uuid
import bcrypt
from ..database.session import get_session
from ..repository.user import UserRepository
from ..models.user import User
from ..auth.jwt_utils import create_access_token

router = APIRouter()

def hash_password(password: str) -> str:
    # bcrypt expects bytes
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd_bytes, salt)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_byte_enc = plain_password.encode('utf-8')
    hashed_password_byte_enc = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_byte_enc, hashed_password_byte_enc)

class RegisterUser(BaseModel):
    email: EmailStr
    password: str
    name: str

class LoginUser(BaseModel):
    email: EmailStr
    password: str

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user_in: RegisterUser, session: Session = Depends(get_session)):
    """Register a new user and store in Neon DB."""
    repository = UserRepository(session)
    
    # Check if user already exists
    try:
        existing_user = repository.get_by_email(user_in.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exists"
            )
        
        # Create new user
        hashed_pwd = hash_password(user_in.password)
        new_user = User(
            id=str(uuid.uuid4()),
            email=user_in.email,
            name=user_in.name,
            hashed_password=hashed_pwd
        )
        
        repository.create(new_user)
        return {"message": "User registered successfully", "user_id": new_user.id}
    except Exception as e:
        print(f"Error in register: {e}")
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login")
async def login(user_in: LoginUser, session: Session = Depends(get_session)):
    """Authenticate user and return JWT."""
    repository = UserRepository(session)
    user = repository.get_by_email(user_in.email)
    
    if not user or not user.hashed_password or not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    # Generate token
    access_token = create_access_token(data={"sub": user.id})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "name": user.name
        }
    }
