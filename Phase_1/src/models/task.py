"""
Task model for the Todo In-Memory CLI.
"""
from dataclasses import dataclass

@dataclass
class Task:
    """Represents a single todo item in the system."""
    id: int
    title: str
    status: str = "Pending"

    def to_dict(self) -> dict:
        """
        Returns task as a dictionary for easier display/serialization.
        
        Returns:
            dict: The task data as a dictionary.
        """
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status
        }
