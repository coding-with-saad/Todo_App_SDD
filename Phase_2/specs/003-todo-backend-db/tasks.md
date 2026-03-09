# Tasks: Todo Backend API + Database

**Input**: Design documents from `specs/003-todo-backend-db/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md, contracts/

**Tests**: API tests are included for each user story to ensure correctness and security.

**Organization**: Tasks are grouped by phase and user story to enable incremental delivery and testing.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Database connection and session management setup

- [X] T001 Configure Neon PostgreSQL `DATABASE_URL` in `.env`
- [X] T002 Implement database engine and session management in `backend/src/database/session.py`
- [X] T003 Initialize Alembic for database migrations in `backend/alembic/`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure required for all task operations

- [X] T004 Define `User` and `Task` SQLModel classes in `backend/src/models/todo.py`
- [X] T005 Implement CRUD operations in `TaskRepository` with `user_id` filtering in `backend/src/repository/todo.py`
- [X] T006 Implement `TaskService` for business logic and ownership validation in `backend/src/services/todo.py`
- [ ] T007 Create initial database migration and upgrade schema in `backend/alembic/` (Skipped: Environment connection issue)

---

## Phase 3: User Story 1 - Create and Store Tasks (Priority: P1) 🎯 MVP

**Goal**: Authenticated users can create and persist tasks.

**Independent Test**: Send POST `/todos` with title and verify 201 Created and DB record exists.

- [X] T008 [US1] Implement POST `/todos` endpoint in `backend/src/api/todos.py`
- [X] T009 [US1] Add input validation for mandatory `title` field in `backend/src/models/todo.py`
- [X] T010 [US1] Add integration test for task creation in `backend/tests/integration/test_tasks.py`

---

## Phase 4: User Story 2 - Retrieve Personalized Task List (Priority: P1)

**Goal**: Users only see their own tasks.

**Independent Test**: Create tasks for User A and B; verify User A's GET `/todos` only returns A's tasks.

- [X] T011 [US2] Implement GET `/todos` endpoint in `backend/src/api/todos.py`
- [X] T012 [US2] Ensure repository filters by `request.state.user_id` in `backend/src/repository/todo.py`
- [X] T013 [US2] Add integration test for user data isolation in `backend/tests/integration/test_isolation.py`

---

## Phase 5: User Story 3 - Update and Toggle Task Status (Priority: P2)

**Goal**: Users can update details and toggle completion status.

**Independent Test**: PATCH `/todos/{id}` with `completed: true` and verify state change.

- [X] T014 [US3] Implement PATCH `/todos/{id}` endpoint in `backend/src/api/todos.py`
- [X] T015 [US3] Add completion toggle logic in `TaskService` in `backend/src/services/todo.py`
- [X] T016 [US3] Enforce user ownership check before update in `backend/src/services/todo.py`
- [X] T017 [US3] Add integration test for task status toggle in `backend/tests/integration/test_tasks.py`

---

## Phase 6: User Story 4 - Delete Tasks (Priority: P2)

**Goal**: Users can permanently remove their tasks.

**Independent Test**: DELETE `/todos/{id}` and verify 204 No Content and 404 on GET.

- [X] T018 [US4] Implement DELETE `/todos/{id}` endpoint in `backend/src/api/todos.py`
- [X] T019 [US4] Enforce user ownership check before deletion in `backend/src/services/todo.py`
- [X] T020 [US4] Add integration test for task deletion in `backend/tests/integration/test_tasks.py`

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final refinements and performance verification

- [X] T021 [P] Verify API response times are under 200ms
- [X] T022 [P] Standardize JSON response formats across all endpoints
- [X] T023 Final code cleanup and documentation update in `specs/003-todo-backend-db/quickstart.md`
