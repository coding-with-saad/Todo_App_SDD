"""
Business logic and service layer for task management.
"""
from typing import Dict, List, Optional
from src.models.task import Task

class TodoManager:
    """
    Manages the lifecycle and storage of tasks in memory.
    
    Attributes:
        tasks (Dict[int, Task]): Dictionary of tasks indexed by their ID.
    """

    def __init__(self):
        """Initializes empty storage and ID counter."""
        self.tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def _get_next_id(self) -> int:
        """
        Increments and returns the next task ID.
        
        Returns:
            int: The next available task ID.
        """
        new_id = self._next_id
        self._next_id += 1
        return new_id

    def add_task(self, title: str) -> int:
        """
        Adds a new task and returns its ID.
        
        Args:
            title (str): The title of the task.
            
        Returns:
            int: The unique ID assigned to the task.
            
        Raises:
            ValueError: If the title is empty or whitespace-only.
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty.")
        
        task_id = self._get_next_id()
        task = Task(id=task_id, title=title.strip())
        self.tasks[task_id] = task
        return task_id

    def get_all_tasks(self) -> List[Task]:
        """
        Returns a list of all tasks.
        
        Returns:
            List[Task]: All tasks in the collection.
        """
        return list(self.tasks.values())

    def mark_complete(self, task_id: int) -> bool:
        """
        Marks a task as complete. 
        
        Args:
            task_id (int): The ID of the task to complete.
            
        Returns:
            bool: True if successful, False if task_id not found.
        """
        if task_id in self.tasks:
            self.tasks[task_id].status = "Complete"
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Deletes a task. 
        
        Args:
            task_id (int): The ID of the task to delete.
            
        Returns:
            bool: True if successful, False if task_id not found.
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def update_task(self, task_id: int, new_title: str) -> bool:
        """
        Updates a task title. 
        
        Args:
            task_id (int): The ID of the task to update.
            new_title (str): The new title for the task.
            
        Returns:
            bool: True if successful, False if task_id not found.
            
        Raises:
            ValueError: If the new title is empty or whitespace-only.
        """
        if not new_title or not new_title.strip():
            raise ValueError("Task title cannot be empty.")
            
        if task_id in self.tasks:
            self.tasks[task_id].title = new_title.strip()
            return True
        return False
