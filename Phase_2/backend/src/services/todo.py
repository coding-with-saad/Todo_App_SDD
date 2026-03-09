from typing import List, Optional
from fastapi import HTTPException, status
from ..models.todo import Todo
from ..repository.todo import TodoRepository

class TaskService:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def list_tasks(self, user_id: str) -> List[Todo]:
        return self.repository.get_by_user(user_id)

    def create_task(self, title: str, user_id: str, description: Optional[str] = None) -> Todo:
        if not title or not title.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Title is mandatory"
            )
        # Create with explicit user_id
        new_todo = Todo(title=title, description=description, user_id=user_id)
        return self.repository.create(new_todo)

    def update_task(self, todo_id: int, user_id: str, title: Optional[str] = None, completed: Optional[bool] = None) -> Todo:
        todo = self.repository.get_by_id(todo_id, user_id)
        if not todo:
            print(f"Update failed: Task {todo_id} not found for user {user_id}")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task {todo_id} not found or not owned by you"
            )
        
        if title is not None:
            todo.title = title
        if completed is not None:
            todo.completed = completed
            
        return self.repository.update(todo)

    def delete_task(self, todo_id: int, user_id: str) -> None:
        todo = self.repository.get_by_id(todo_id, user_id)
        if not todo:
            print(f"Delete failed: Task {todo_id} not found for user {user_id}")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task {todo_id} not found or not owned by you"
            )
        self.repository.delete(todo)
