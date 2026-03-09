from typing import List, Optional
from sqlmodel import Session, select
from ..models.todo import Todo

class TodoRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_user(self, user_id: str) -> List[Todo]:
        """List authenticated user's tasks."""
        statement = select(Todo).where(Todo.user_id == user_id)
        return self.session.exec(statement).all()

    def get_by_id(self, todo_id: int, user_id: str) -> Optional[Todo]:
        """Get a specific task by ID and user ID."""
        statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == user_id)
        return self.session.exec(statement).first()

    def create(self, todo: Todo) -> Todo:
        """Create a new task."""
        self.session.add(todo)
        self.session.commit()
        self.session.refresh(todo)
        return todo

    def update(self, todo: Todo) -> Todo:
        """Update an existing task."""
        self.session.add(todo)
        self.session.commit()
        self.session.refresh(todo)
        return todo

    def delete(self, todo: Todo) -> None:
        """Delete a task."""
        self.session.delete(todo)
        self.session.commit()
