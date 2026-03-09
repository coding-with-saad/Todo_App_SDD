from typing import Optional
from sqlmodel import Session, select
from ..models.user import User
import sqlalchemy

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, user_id: str) -> Optional[User]:
        """Get user by ID."""
        try:
            statement = select(User).where(User.id == user_id)
            return self.session.exec(statement).first()
        except Exception as e:
            print(f"Database error: {e}")
            raise

    def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email."""
        try:
            statement = select(User).where(User.email == email)
            return self.session.exec(statement).first()
        except Exception as e:
            print(f"Database error: {e}")
            raise

    def create(self, user: User) -> User:
        """Create a new user and commit to DB."""
        try:
            self.session.add(user)
            self.session.commit()
            self.session.refresh(user)
            return user
        except Exception as e:
            self.session.rollback()
            print(f"Database error during create: {e}")
            raise

    def update(self, user: User) -> User:
        """Update an existing user and commit to DB."""
        try:
            self.session.add(user)
            self.session.commit()
            self.session.refresh(user)
            return user
        except Exception as e:
            self.session.rollback()
            print(f"Database error during update: {e}")
            raise
