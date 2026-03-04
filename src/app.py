import sys
from src.services.manager import TodoManager

def main():
    """Main entry point for the Todo CLI application."""
    manager = TodoManager()
    
    print("=== Todo In-Memory CLI (Phase I) ===")
    
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task Title (P3)")
        print("4. Mark Task Complete (P2)")
        print("5. Delete Task (P2)")
        print("6. Exit")
        
        choice = input("\nSelect an option: ").strip()
        
        if choice == "1":
            title = input("Enter task title: ").strip()
            try:
                task_id = manager.add_task(title)
                print(f"Task added with ID: {task_id}")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == "2":
            tasks = manager.get_all_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                print("\nID | Status   | Title")
                print("-" * 30)
                for task in tasks:
                    status_padded = task.status.ljust(8)
                    print(f"{task.id:<2} | {status_padded} | {task.title}")
                    
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to complete: ").strip())
                if manager.mark_complete(task_id):
                    print(f"Task {task_id} marked as complete.")
                else:
                    print(f"Error: Task ID {task_id} not found.")
            except ValueError:
                print("Error: Please enter a valid numeric ID.")

        elif choice == "5":
            try:
                task_id = int(input("Enter task ID to delete: ").strip())
                if manager.delete_task(task_id):
                    print(f"Task {task_id} deleted.")
                else:
                    print(f"Error: Task ID {task_id} not found.")
            except ValueError:
                print("Error: Please enter a valid numeric ID.")

        elif choice == "6":
            print("Exiting. Goodbye!")
            sys.exit(0)
            
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to update: ").strip())
                new_title = input("Enter new title: ").strip()
                if manager.update_task(task_id, new_title):
                    print(f"Task {task_id} updated to: {new_title}")
                else:
                    print(f"Error: Task ID {task_id} not found.")
            except ValueError as e:
                if str(e).startswith("invalid literal for int()"):
                    print("Error: Please enter a valid numeric ID.")
                else:
                    print(f"Error: {e}")
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
