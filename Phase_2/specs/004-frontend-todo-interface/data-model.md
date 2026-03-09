# Data Model: Frontend Todo Web Interface

## Entities (Frontend State)

### Auth Session
- **Properties**:
  - `user`: `UserObject` (id, email, name)
  - `token`: `String` (JWT for API authentication)
  - `isLoggedIn`: `Boolean`
- **Source**: Managed by Better Auth Client.

### Task (UI Component State)
- **Properties**:
  - `id`: `Int`
  - `title`: `String`
  - `description`: `String` (Optional)
  - `completed`: `Boolean`
  - `user_id`: `String`
  - `created_at`: `String` (ISO Date)
  - `updated_at`: `String` (ISO Date)
- **Source**: Fetched from FastAPI backend via `/todos`.

## UI State Transitions
- **Auth Flow**: `Unauthenticated` → `Sign Up/In` → `Authenticated` → `Dashboard`.
- **Task Flow**: `Loading` → `Displayed` → `Adding/Updating` → `Syncing` → `Updated`.
- **Error States**: `Unauthorized` (Redirect to login), `Network Error` (Toast notification).

## Validation Rules (Client-Side)
- **Signup**: Email must be valid format; Password must meet length requirements.
- **Task Creation**: Title must be at least 1 character.
