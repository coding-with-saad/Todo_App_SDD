# CLI Interface Patterns: Todo In-Memory Python CLI

## Menu Options
1. Add Task
2. View All Tasks
3. Update Task Title
4. Mark Task Complete
5. Delete Task
6. Exit

## Interaction Patterns

### 1. Add Task
- **Input**: `Enter task title: [Title string]`
- **Success**: `Task added with ID: [N]`
- **Failure**: `Error: Task title cannot be empty.`

### 2. View Tasks
- **Output**:
  ```text
  ID | Status   | Title
  -----------------------
  1  | Pending  | Buy groceries
  2  | Complete | Write code
  ```

### 3. Mark Task Complete
- **Input**: `Enter task ID to complete: [N]`
- **Success**: `Task [N] marked as complete.`
- **Failure**: `Error: Task ID [N] not found.`

### 4. Update Task Title
- **Input**: `Enter task ID to update: [N]`
- **Input**: `Enter new title: [New Title]`
- **Success**: `Task [N] updated to [New Title].`
- **Failure**: `Error: Task ID [N] not found.`

### 5. Delete Task
- **Input**: `Enter task ID to delete: [N]`
- **Success**: `Task [N] deleted.`
- **Failure**: `Error: Task ID [N] not found.`
