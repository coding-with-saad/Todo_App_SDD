# Tasks: Authentication System

**Input**: Design documents from `specs/002-user-authentication/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are included as standard validation tasks for each user story.

**Organization**: Tasks are grouped by phase and user story to enable incremental delivery.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and environment configuration

- [X] T001 Create project structure per implementation plan
- [X] T002 Initialize [language] project with [framework] dependencies
- [X] T003 [P] Configure linting and formatting tools
- [X] T004 Initialize Next.js project and install dependencies (Better Auth, jwt-decode) in frontend/
- [X] T005 [P] Configure shared environment variables (JWT_SECRET, DATABASE_URL) in .env files

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before user story implementation

- [X] T006 Implement User model in backend/src/models/user.py
- [X] T007 Update Todo model to include user_id in backend/src/models/todo.py
- [ ] T008 Setup database migrations for User and updated Todo tables
- [X] T009 [P] Implement base TodoRepository with user_id support in backend/src/repository/todo.py
- [X] T010 [P] Implement base UserRepository in backend/src/repository/user.py

---

## Phase 3: User Story 1 - Secure Sign Up & Sign In (Priority: P1) 🎯 MVP

**Goal**: Enable users to create accounts and receive a JWT upon login via Better Auth.

**Independent Test**: Successfully register a user and login via frontend, receiving a valid JWT.

- [X] T011 [US1] Configure Better Auth with JWT plugin in frontend/src/lib/auth.ts
- [X] T012 [US1] Implement Sign Up page UI in frontend/src/pages/signup.tsx
- [X] T013 [US1] Implement Login page UI in frontend/src/pages/login.tsx
- [ ] T014 [US1] Create Auth router for backend registration/login (if needed for Better Auth sync) in backend/src/api/auth.py
- [ ] T015 [US1] Add integration test for user registration and login in backend/tests/integration/test_auth.py

---

## Phase 4: User Story 2 - Authenticated API Access (Priority: P1)

**Goal**: Secure the backend API using JWT and include tokens in frontend requests.

**Independent Test**: Call a protected endpoint with a valid JWT and get a 200 OK.

- [X] T016 [US2] Implement JWT verification utility in backend/src/auth/jwt.py
- [X] T017 [US2] Implement FastAPI authentication middleware in backend/src/auth/middleware.py
- [ ] T018 [US2] Protect Todo API routes using auth middleware in backend/src/api/todos.py
- [X] T019 [US2] Create API client with automatic Bearer token inclusion in frontend/src/lib/api-client.ts
- [ ] T020 [P] [US2] Contract test for protected /todos endpoint in backend/tests/contract/test_auth_todos.py

---

## Phase 5: User Story 3 - Data Isolation & Ownership (Priority: P2)

**Goal**: Ensure users can only see and manage their own tasks.

**Independent Test**: Authenticate as User A and attempt to access User B's task; verify failure.

- [ ] T021 [US3] Update TodoRepository to filter all queries by request.state.user_id in backend/src/repository/todo.py
- [ ] T022 [US3] Implement ownership check in TodoService for update/delete operations in backend/src/services/todo.py
- [ ] T023 [US3] Add integration test for cross-user data isolation in backend/tests/integration/test_isolation.py

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final refinements and security hardening

- [ ] T024 [P] Implement Logout functionality and token clearing in frontend/src/components/Logout.tsx
- [ ] T025 [P] Add global 401 Unauthorized error handling in frontend/src/lib/api-client.ts
- [ ] T026 Update quickstart.md with final environment setup details in specs/002-user-authentication/quickstart.md
- [ ] T027 Run final security validation and performance check for JWT verification

---

## Dependencies & Execution Order

1. **Phase 1 & 2**: Must be completed first as they provide the platform and data structure.
2. **Phase 3 (US1)**: First functional increment. Enables authentication.
3. **Phase 4 (US2)**: Depends on US1 (for token) and Phase 2 (for routes). Enables security.
4. **Phase 5 (US3)**: Depends on US2 (for user_id context). Enables privacy.
5. **Phase 6**: Final cleanup.

## Parallel Opportunities

- T003 (Backend Setup) and T004 (Frontend Setup) can run in parallel.
- T009 and T010 (Repositories) can run in parallel.
- T024 and T025 (Polish) can run in parallel.

## Implementation Strategy

### MVP First (User Story 1 & 2)
Focus on getting the user authenticated and the API protected. This delivers the core security value.

### Incremental Delivery
- **Step 1**: Basic auth (US1) - Register/Login works.
- **Step 2**: Protected API (US2) - Todos are secured.
- **Step 3**: Privacy (US3) - Multi-user isolation is enforced.
