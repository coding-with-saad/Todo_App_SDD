# Feature Specification: Todo In-Memory Python CLI

**Feature Branch**: `001-todo-in-memory-cli`  
**Created**: 2026-03-04  
**Status**: Draft  
**Input**: User description: "# Todo In-Memory Python Console App Specification ## Part 1: Reference Architecture - Use classes for Task and TodoManager. - Store tasks in memory (list/dict). - Keep modular: storage, logic, and console separated. - Avoid mixing storage and display logic. ## Part 2: Current Architecture - New project, no existing code. - Files: task.py, manager.py, app.py, tests/. - In-memory storage only; data lost on exit. ## Part 3: Implementation Plan 1. Define Task class. 2. Implement TodoManager methods: Add, Delete, Update, View, Mark Complete. 3. Build console interface in app.py. 4. Write unit tests. 5. Validate and cleanup. ## Part 4: Implementation Checklist - [ ] Task 1: Task class - [ ] Task 2: TodoManager.add_task() - [ ] Task 3: TodoManager.delete_task() - [ ] Task 4: TodoManager.update_task() - [ ] Task 5: TodoManager.view_tasks() - [ ] Task 6: TodoManager.mark_complete() - [ ] Task 7: Console interface - [ ] Task 8: Unit tests - [ ] Task 9: Final validation ## Constraints - No database or web UI. - Python 3.13+, console only. - Immediate in-memory operations. - Validate user input; no auth needed. - Works on Windows, macOS, Linux terminals. ## Success Criteria - All five features implemented. - Clean code and proper project structure. - Tests pass and console responds correctly. - Tasks correctly stored in memory during runtime."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add and View Tasks (Priority: P1)

As a user, I want to add tasks to my list and view them so that I can keep track of my to-dos.

**Why this priority**: Core functionality for any todo application.

**Independent Test**: Add a task via CLI and verify it appears in the task list.

**Acceptance Scenarios**:

1. **Given** an empty todo list, **When** the user adds a task "Buy milk", **Then** "Buy milk" should be visible in the list.
2. **Given** a todo list, **When** the user views the list, **Then** all previously added tasks should be displayed with their status.

---

### User Story 2 - Complete and Delete Tasks (Priority: P2)

As a user, I want to mark tasks as complete or delete them so that I can manage my progress and keep the list clean.

**Why this priority**: Essential for managing the lifecycle of a task.

**Independent Test**: Mark a task as complete and verify status change; delete a task and verify it is removed from the list.

**Acceptance Scenarios**:

1. **Given** a task "Buy milk" in the list, **When** the user marks it as complete, **Then** its status should change to "Complete".
2. **Given** a task "Buy milk" in the list, **When** the user deletes it, **Then** it should no longer appear in the list.

---

### User Story 3 - Update Tasks (Priority: P3)

As a user, I want to update the title of a task so that I can correct mistakes or change details.

**Why this priority**: Useful for correcting errors without deleting and re-adding.

**Independent Test**: Change the name of an existing task and verify the update.

**Acceptance Scenarios**:

1. **Given** a task "Buy milk", **When** the user updates it to "Buy organic milk", **Then** the list should show "Buy organic milk" instead.

---

### Edge Cases

- **Empty Input**: Attempting to add a task with an empty or whitespace-only name.
- **Duplicate Tasks**: Adding tasks with the same name.
- **Non-existent IDs**: Attempting to delete, update, or complete a task using an ID that doesn't exist.
- **Large Lists**: Handling a large number of tasks in memory (within reasonable CLI limits).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a `Task` class with attributes: ID, title, and status (e.g., Pending/Complete).
- **FR-002**: System MUST implement a `TodoManager` to manage the collection of tasks in memory.
- **FR-003**: System MUST allow adding a task with a title.
- **FR-004**: System MUST allow viewing all tasks with their IDs and completion status.
- **FR-005**: System MUST allow marking a task as complete by its ID.
- **FR-006**: System MUST allow deleting a task by its ID.
- **FR-007**: System MUST allow updating a task title by its ID.
- **FR-008**: System MUST validate user input (e.g., non-empty titles, valid numeric IDs).

### Key Entities

- **Task**: Represents a single item in the todo list. Attributes include a unique identifier (ID), a title, and a completion status.
- **TodoManager**: The service responsible for the CRUD operations and maintaining the in-memory state of tasks.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can add, view, complete, delete, and update tasks within a single CLI session.
- **SC-002**: 100% of tasks added are correctly stored and retrieved from memory during the application's runtime.
- **SC-003**: System responds to user commands in under 100ms for all in-memory operations.
- **SC-004**: System successfully handles and reports invalid user inputs (e.g., non-existent IDs) without crashing.
- **SC-005**: All core business logic is covered by unit tests.
