import unittest
from src.services.manager import TodoManager
from src.models.task import Task

class TestTodoManager(unittest.TestCase):
    """Unit tests for the TodoManager business logic."""

    def setUp(self):
        """Initializes a new manager before each test."""
        self.manager = TodoManager()

    def test_add_task_success(self):
        """T007: Should successfully add a task and return its ID."""
        task_id = self.manager.add_task("Buy milk")
        self.assertEqual(task_id, 1)
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[1].title, "Buy milk")

    def test_get_all_tasks_empty(self):
        """T008: Should return an empty list when no tasks exist."""
        tasks = self.manager.get_all_tasks()
        self.assertEqual(tasks, [])

    def test_get_all_tasks_populated(self):
        """T008: Should return all added tasks."""
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        tasks = self.manager.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].title, "Task 1")
        self.assertEqual(tasks[1].title, "Task 2")

    def test_mark_complete_success(self):
        """T012: Should mark an existing task as complete."""
        task_id = self.manager.add_task("Task to complete")
        success = self.manager.mark_complete(task_id)
        self.assertTrue(success)
        self.assertEqual(self.manager.tasks[task_id].status, "Complete")

    def test_mark_complete_fail_invalid_id(self):
        """T012: Should return False for non-existent ID."""
        success = self.manager.mark_complete(999)
        self.assertFalse(success)

    def test_delete_task_success(self):
        """T013: Should delete an existing task."""
        task_id = self.manager.add_task("Task to delete")
        success = self.manager.delete_task(task_id)
        self.assertTrue(success)
        self.assertNotIn(task_id, self.manager.tasks)

    def test_delete_task_fail_invalid_id(self):
        """T013: Should return False for non-existent ID."""
        success = self.manager.delete_task(999)
        self.assertFalse(success)

    def test_update_task_success(self):
        """T017: Should update an existing task title."""
        task_id = self.manager.add_task("Old Title")
        success = self.manager.update_task(task_id, "New Title")
        self.assertTrue(success)
        self.assertEqual(self.manager.tasks[task_id].title, "New Title")

    def test_update_task_fail_invalid_id(self):
        """T017: Should return False for non-existent ID."""
        success = self.manager.update_task(999, "New Title")
        self.assertFalse(success)

    def test_update_task_fail_empty_title(self):
        """T017: Should raise ValueError for empty title."""
        task_id = self.manager.add_task("Title")
        with self.assertRaises(ValueError):
            self.manager.update_task(task_id, "")

if __name__ == "__main__":
    unittest.main()
