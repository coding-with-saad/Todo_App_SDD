from fastapi import APIRouter, Request, Depends, HTTPException, status
from typing import List, Optional
from pydantic import BaseModel
from ..models.todo import Todo
from ..repository.todo import TodoRepository
from ..services.todo import TaskService
from ..database.session import get_session
from sqlmodel import Session

router = APIRouter()

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

def get_task_service(session: Session = Depends(get_session)) -> TaskService:
    repository = TodoRepository(session)
    return TaskService(repository)

@router.get("/", response_model=List[Todo])
async def list_todos(
    request: Request, 
    service: TaskService = Depends(get_task_service)
):
    """List authenticated user's tasks."""
    user_id = getattr(request.state, "user_id", None)
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    try:
        return service.list_tasks(user_id)
    except Exception as e:
        print(f"Error in list_todos: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/", response_model=Todo, status_code=status.HTTP_201_CREATED)
async def create_todo(
    request: Request, 
    todo_in: TaskCreate,
    service: TaskService = Depends(get_task_service)
):
    """Create a new task for the authenticated user."""
    user_id = getattr(request.state, "user_id", None)
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    try:
        return service.create_task(
            title=todo_in.title, 
            user_id=user_id, 
            description=todo_in.description
        )
    except Exception as e:
        print(f"Error in create_todo: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/{id}", response_model=Todo)
async def update_todo(
    id: int,
    request: Request,
    todo_in: TaskUpdate,
    service: TaskService = Depends(get_task_service)
):
    """Update or toggle a task."""
    user_id = getattr(request.state, "user_id", None)
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    try:
        return service.update_task(
            todo_id=id,
            user_id=user_id,
            title=todo_in.title,
            completed=todo_in.completed
        )
    except Exception as e:
        print(f"Error in update_todo: {e}")
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(
    id: int,
    request: Request,
    service: TaskService = Depends(get_task_service)
):
    """Delete a task."""
    user_id = getattr(request.state, "user_id", None)
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    try:
        service.delete_task(todo_id=id, user_id=user_id)
        return None
    except Exception as e:
        print(f"Error in delete_todo: {e}")
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(status_code=500, detail=str(e))
