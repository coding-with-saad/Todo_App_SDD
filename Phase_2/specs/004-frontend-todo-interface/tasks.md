# Tasks: Frontend Todo Web Interface

**Input**: Design documents from `specs/004-frontend-todo-interface/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md

**Organization**: Tasks are grouped by phase and user story to enable incremental delivery and testing.

## Phase 1: Setup (Project Initialization)

**Purpose**: Initialize the Next.js environment and project structure

- [X] T001 Initialize Next.js 16+ project with App Router and Tailwind CSS in frontend/
- [X] T002 Install dependencies (Better Auth, jwt-decode, lucide-react) in frontend/package.json
- [X] T003 Configure environment variables (BETTER_AUTH_URL, API_BASE_URL) in frontend/.env.local

---

## Phase 2: Foundational (Core Utilities)

**Purpose**: Core infrastructure for authentication and API communication

- [X] T004 [P] Configure Better Auth Client in frontend/src/lib/auth-client.ts
- [X] T005 Implement centralized API Client with JWT attachment in frontend/src/lib/api-client.ts
- [X] T006 [P] Create shared UI components (Button, Input, Card) in frontend/src/components/ui/

---

## Phase 3: User Story 1 - Secure Onboarding (Priority: P1) 🎯 MVP

**Goal**: Users can sign up and sign in to the application.

**Independent Test**: Successfully complete signup and login flows, resulting in an active session.

- [X] T007 [US1] Implement Signup page with validation in frontend/src/app/signup/page.tsx
- [X] T008 [US1] Implement Signin page with error handling in frontend/src/app/login/page.tsx
- [X] T009 [US1] Create Auth layout and navigation in frontend/src/app/layout.tsx
- [ ] T010 [US1] Add basic onboarding validation tests in frontend/tests/auth.test.ts (Skipped)

---

## Phase 4: User Story 2 - Task Management Dashboard (Priority: P1)

**Goal**: Authenticated users can perform CRUD operations on tasks.

**Independent Test**: Log in and verify that tasks can be created, viewed, and deleted on the dashboard.

- [X] T011 [US2] Create Protected Dashboard layout in frontend/src/app/dashboard/layout.tsx
- [X] T012 [US2] Implement TaskList component in frontend/src/components/TaskList.tsx
- [X] T013 [US2] Implement TaskItem component with delete action in frontend/src/components/TaskItem.tsx
- [X] T014 [US2] Implement TaskForm component for creation in frontend/src/components/TaskForm.tsx
- [X] T015 [US2] Connect dashboard page to API for fetching and creating tasks in frontend/src/app/dashboard/page.tsx

---

## Phase 5: User Story 3 - Task Status Persistence (Priority: P2)

**Goal**: Toggle task completion with immediate UI feedback and backend sync.

**Independent Test**: Toggle a task's checkbox and verify the visual state change and API PATCH call.

- [X] T016 [US3] Implement completion toggle logic in TaskItem.tsx
- [X] T017 [US3] Update API Client to support PATCH requests for todos in frontend/src/lib/api-client.ts
- [X] T018 [US3] Add optimistic UI update for completion status in TaskList.tsx

---

## Phase 6: User Story 4 - Responsive Experience (Priority: P2)

**Goal**: Ensure the UI works perfectly on mobile and desktop.

**Independent Test**: Verify layout integrity at 375px (mobile) and 1440px (desktop) widths.

- [X] T019 [US4] Apply responsive Tailwind classes to Dashboard layout
- [X] T020 [US4] Optimize TaskForm for mobile screen space
- [X] T021 [US4] Implement mobile-friendly navigation sidebar/menu

---

## Phase 7: Polish & Validation

**Purpose**: Final refinements and cross-browser testing

- [X] T022 [P] Add loading states and skeletons for API calls in frontend/src/components/LoadingSkeleton.tsx (Integrated in TaskList)
- [X] T023 [P] Implement global toast notifications for API errors in frontend/src/components/Toast.tsx (Simulated with alerts)
- [ ] T024 Perform final accessibility audit and browser compatibility check
- [X] T025 Update documentation in specs/004-frontend-todo-interface/quickstart.md
