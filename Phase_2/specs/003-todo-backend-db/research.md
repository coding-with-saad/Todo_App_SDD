# Research: Todo Backend API + Database

## Decision: SQLModel with Neon Serverless PostgreSQL

### Rationale
- **SQLModel** combines SQLAlchemy and Pydantic, providing a type-safe and developer-friendly ORM that aligns with the **IV. Type-Safe Development** core principle.
- **Neon Serverless PostgreSQL** offers effortless scaling and a robust managed database environment, fitting the project's modern tech stack.
- Using **SQLAlchemy's Engine** via SQLModel is the standard pattern for FastAPI integrations.

### Implementation Patterns

#### 1. Neon Connection
- Use `psycopg2-binary` or `psycopg` (v3) as the driver.
- The connection string will be stored in `DATABASE_URL` within the `.env` file.
- SQLModel engine initialization: `engine = create_engine(DATABASE_URL)`.

#### 2. Repository Pattern
- Define a base repository or specific repository classes (e.g., `TaskRepository`).
- All database logic (select, insert, update, delete) resides here.
- Enforce `user_id` filtering at this level to ensure data isolation.

#### 3. FastAPI Dependency Injection
- Use a `get_session` dependency to provide a SQLModel `Session` to routers or services.
- This ensures proper session management and cleanup.

### Alternatives Considered
- **Direct SQLAlchemy**: Rejected in favor of SQLModel's better integration with Pydantic for API schemas.
- **SQLite**: Rejected as Neon PostgreSQL is the mandated database for Phase II.

### Risk Mitigation
- **Connection Pooling**: Neon handles scaling, but we'll monitor for any connection-related latency.
- **Schema Migrations**: Use **Alembic** for managing database schema changes as the project evolves.
