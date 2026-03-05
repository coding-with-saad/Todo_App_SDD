---
description: "Task list for Todo In-Memory Python CLI"
---

# Tasks: Todo In-Memory Python CLI

**Input**: Design documents from `/specs/001-todo-in-memory-cli/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Current Project Phase**: Phase I - In-Memory Console Application
> ⚠️ **CONSTITUTION COMPLIANCE**: All tasks MUST comply with the constraints of the current project phase (e.g., Python 3.12, no DB in Phase I, strict type hints, 40-line limit).

**Tests**: Unit tests are REQUIRED for all core business logic as per the specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths below assume single project structure

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure: src/models/, src/services/, tests/unit/
- [x] T002 Initialize project with Python 3.12 environment
- [x] T003 [P] Configure `.gitignore` for Python (excluding __pycache__, etc.)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Define `Task` class with ID, title, and status in `src/models/task.py`
- [x] T005 Initialize `TodoManager` class in `src/services/manager.py`
- [x] T006 [P] Create test discovery helper or base test class in `tests/unit/test_manager.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Allow users to add tasks to their list and view them.

**Independent Test**: Run app, add "Buy milk", view list, verify "Buy milk" appears with status "Pending".

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T007 [P] [US1] Unit test for `add_task` in `tests/unit/test_manager.py`
- [x] T008 [P] [US1] Unit test for `get_all_tasks` in `tests/unit/test_manager.py`

### Implementation for User Story 1

- [x] T009 [US1] Implement `add_task` method in `src/services/manager.py`
- [x] T010 [US1] Implement `get_all_tasks` method in `src/services/manager.py`
- [x] T011 [US1] Implement "Add Task" and "View All Tasks" menu options in `src/app.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Complete and Delete Tasks (Priority: P2)

**Goal**: Allow users to mark tasks as complete or delete them.

**Independent Test**: Mark existing task as complete and verify status; delete task and verify removal.

### Tests for User Story 2

- [x] T012 [P] [US2] Unit test for `mark_complete` in `tests/unit/test_manager.py`
- [x] T013 [P] [US2] Unit test for `delete_task` in `tests/unit/test_manager.py`

### Implementation for User Story 2

- [x] T014 [US2] Implement `mark_complete` method in `src/services/manager.py`
- [x] T015 [US2] Implement `delete_task` method in `src/services/manager.py`
- [x] T016 [US2] Implement "Mark Task Complete" and "Delete Task" menu options in `src/app.py`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Tasks (Priority: P3)

**Goal**: Allow users to update the title of an existing task.

**Independent Test**: Update task title and verify change in list view.

### Tests for User Story 3

- [x] T017 [P] [US3] Unit test for `update_task` in `tests/unit/test_manager.py`

### Implementation for User Story 3

- [x] T018 [US3] Implement `update_task` method in `src/services/manager.py`
- [x] T019 [US3] Implement "Update Task Title" menu option in `src/app.py`

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T020 [P] Add input validation for task IDs and titles in `src/app.py`
- [x] T021 [P] Ensure all docstrings follow code standards in all `.py` files
- [x] T022 [P] Run final validation against `quickstart.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Setup (T001-T003).
- **User Stories (Phase 3+)**: All depend on Foundational (T004-T006).

### Parallel Opportunities

- T003, T006, T007, T008, T012, T013, T017 can be developed in parallel as they touch different files or are independent tests.
- Once Phase 2 is done, US1, US2, and US3 implementation can theoretically start in parallel, though US2/US3 logically follow US1 for manual testing.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1 & 2.
2. Complete Phase 3 (US1).
3. **STOP and VALIDATE**: Verify core "Add/View" loop works.

### Incremental Delivery

1. Foundation ready.
2. Add US1 → MVP ready.
3. Add US2 → Management features ready.
4. Add US3 → Full CRUD ready.
