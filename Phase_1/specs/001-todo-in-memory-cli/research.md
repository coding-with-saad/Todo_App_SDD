# Research: Todo In-Memory Python CLI

## Decision 1: Python 3.12 Standard Library only
- **Decision**: Use only Python standard library for Phase I.
- **Rationale**: Phase I constraints strictly forbid external persistence or web frameworks. To ensure a clean and modular codebase, `unittest` will be used for testing and simple terminal I/O for the interface.
- **Alternatives considered**: `pytest` (rejected to keep dependencies zero in Phase I).

## Decision 2: In-Memory Storage Mechanism
- **Decision**: Use a dictionary within `TodoManager` for task storage.
- **Rationale**: A dictionary indexed by task ID provides O(1) access for updates, deletions, and completions, ensuring the <100ms response goal.
- **Alternatives considered**: List of objects (rejected due to O(n) lookup overhead).

## Decision 3: CLI Interface Pattern
- **Decision**: A simple command loop with a menu-driven interface.
- **Rationale**: Minimalist and effective for Phase I requirements. Each menu option maps directly to a `TodoManager` method.
- **Alternatives considered**: Positional arguments CLI (rejected as it's less user-friendly for a purely in-memory session where state is lost).
