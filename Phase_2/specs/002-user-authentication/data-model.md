# Data Model: Authentication System

## Entities

### User (Auth Managed)
- **Table Name**: `user`
- **Fields**:
  - `id`: `String` (Primary Key, UUID format)
  - `email`: `String` (Unique)
  - `name`: `String`
  - `hashed_password`: `String` (Managed by Better Auth)
  - `created_at`: `DateTime`
  - `updated_at`: `DateTime`

### Task (Todo)
- **Table Name**: `todo`
- **Fields**:
  - `id`: `Int` (Primary Key, Auto-increment)
  - `title`: `String`
  - `description`: `String` (Optional)
  - `completed`: `Boolean` (Default: false)
  - `user_id`: `String` (Foreign Key to `user.id`, Non-nullable)
  - `created_at`: `DateTime`
  - `updated_at`: `DateTime`

## Relationships
- **User (1) ↔ Task (N)**: A user can have multiple tasks, but each task belongs to exactly one user.

## Validation Rules
- `user_id` must be present in every `Todo` create/update operation.
- Emails must be validated for format before registration.
- Passwords must meet complexity requirements (enforced by Better Auth).
