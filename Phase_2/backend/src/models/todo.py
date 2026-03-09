from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(min_length=1)
    description: Optional[str] = None
    completed: bool = Field(default=False)
    user_id: str = Field(index=True, nullable=False)  # Foreign key to User.id
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
