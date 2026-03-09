from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: str = Field(primary_key=True)  # UUID from Better Auth
    email: str = Field(index=True, unique=True)
    name: Optional[str] = None
    hashed_password: Optional[str] = None  # Managed by Better Auth, but stored for reference if needed
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
