# Feature Specification: Todo Backend API + Database

**Feature Branch**: `003-todo-backend-db`  
**Created**: 2026-03-07  
**Status**: Draft  
**Input**: User description: "Todo Backend API + Database Specification with CRUD, SQLModel, and Neon PostgreSQL"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Create and Store Tasks (Priority: P1)

As an authenticated user, I want to create new todo tasks and have them saved in a persistent database so that I don't lose my items when I refresh or log out.

**Why this priority**: Core functionality of the application.

**Independent Test**: Can be tested by sending a POST request to `/todos` with a title and verifying the task is returned with a unique ID and exists in the database.

**Acceptance Scenarios**:

1. **Given** I am a logged-in user, **When** I provide a valid task title and description, **Then** the system saves the task and links it to my user ID.
2. **Given** I am a logged-in user, **When** I attempt to create a task without a title, **Then** the system returns a validation error.

---

### User Story 2 - Retrieve Personalized Task List (Priority: P1)

As an authenticated user, I want to view a list of only my own tasks so that I can manage my personal workload without seeing other users' data.

**Why this priority**: Essential for multi-user privacy and basic usability.

**Independent Test**: Can be verified by creating tasks for User A and User B, then logging in as User A and ensuring only User A's tasks are returned by `GET /todos`.

**Acceptance Scenarios**:

1. **Given** I have multiple tasks in the system, **When** I request my tasks, **Then** I receive a list containing only tasks where `user_id` matches my ID.
2. **Given** I have no tasks, **When** I request my tasks, **Then** I receive an empty list.

---

### User Story 3 - Update and Toggle Task Status (Priority: P2)

As an authenticated user, I want to update my tasks' details and mark them as complete so that I can track my progress.

**Why this priority**: Necessary for the full task lifecycle.

**Independent Test**: Send a PATCH or PUT request to `/todos/{id}` with updated fields or a completion toggle and verify the database record is updated.

**Acceptance Scenarios**:

1. **Given** I own an existing task, **When** I toggle its completion status, **Then** the system updates the task and returns the new state.
2. **Given** I attempt to update a task that does not belong to me, **Then** the system returns a 404 Not Found or 401 Unauthorized.

---

### User Story 4 - Delete Tasks (Priority: P2)

As an authenticated user, I want to delete tasks I no longer need so that I can keep my list clean.

**Why this priority**: Important for list management.

**Independent Test**: Send a DELETE request to `/todos/{id}` and verify that a subsequent GET request for that ID returns a 404.

**Acceptance Scenarios**:

1. **Given** I own an existing task, **When** I delete it, **Then** the system removes it permanently.
2. **Given** I attempt to delete a task that I do not own, **Then** the system returns a 404 or 401 and the task remains.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide RESTful endpoints for CRUD operations on tasks.
- **FR-002**: Every task MUST be linked to an `authenticated_user_id`.
- **FR-003**: System MUST use **SQLModel** for all database interactions.
- **FR-004**: Database MUST be **Neon Serverless PostgreSQL**.
- **FR-005**: All retrieval queries MUST filter by the current user's ID extracted from the JWT.
- **FR-006**: System MUST support toggling the `completed` status of a task.
- **FR-007**: Data access MUST be through a dedicated **repository layer**.

### Key Entities

- **Task (Todo)**:
  - `id`: Unique identifier (Integer).
  - `title`: String (Mandatory).
  - `description`: String (Optional).
  - `completed`: Boolean (Default: false).
  - `user_id`: Reference to the owner (String/UUID).
  - `created_at`: Timestamp.
  - `updated_at`: Timestamp.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All API responses for task management return in under **200ms**.
- **SC-002**: 100% of tasks created are correctly linked to the creating user in the Neon PostgreSQL database.
- **SC-003**: Zero instances of a user successfully retrieving or modifying another user's task.
- **SC-004**: CRUD endpoints return consistent JSON formats as defined in the technical plan.

## Assumptions

- **A-001**: The authentication middleware correctly populates `request.state.user_id` for all protected routes.
- **A-002**: Neon DB connection strings and secrets are available in the `.env` file.
