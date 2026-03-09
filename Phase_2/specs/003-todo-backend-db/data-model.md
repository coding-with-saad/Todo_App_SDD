# Data Model: Todo Backend API + Database

## Entities

### User (Auth Reference)
- **Table Name**: `user`
- **Description**: Managed primarily by Better Auth on the frontend, but referenced by ID in the backend.
- **Fields**:
  - `id`: `String` (Primary Key, matches Better Auth `user_id`)
  - `email`: `String` (Unique)

### Task (Todo)
- **Table Name**: `todo`
- **Fields**:
  - `id`: `Optional[int]` (Primary Key, Auto-increment)
  - `title`: `String` (Non-nullable)
  - `description`: `Optional[str]`
  - `completed`: `bool` (Default: `False`)
  - `user_id`: `String` (Foreign Key to `user.id`, Non-nullable)
  - `created_at`: `datetime` (Auto-now-add)
  - `updated_at`: `datetime` (Auto-now)

## Relationships
- **User (1) ↔ Task (N)**: One user can have many tasks. Each task belongs to exactly one user.

## Validation Rules
- `title` must not be empty or whitespace only.
- `user_id` must be a valid ID from the authentication context.
- `completed` must be a boolean value.

## State Transitions
- **Created**: Initial state after POST `/todos`.
- **Toggled**: `completed` status flips from `True` ↔ `False` via PATCH `/todos/{id}`.
- **Deleted**: Record removed from database via DELETE `/todos/{id}`.
