<!--
SYNC IMPACT REPORT
- Version change: [CONSTITUTION_VERSION] → 2.0.0
- List of modified principles:
  - [PRINCIPLE_1_NAME] → I. Three-Layer Architecture
  - [PRINCIPLE_2_NAME] → II. Repository-Only Data Access
  - [PRINCIPLE_3_NAME] → III. JWT-Based Authentication (NON-NEGOTIABLE)
  - [PRINCIPLE_4_NAME] → IV. Type-Safe Development
  - [PRINCIPLE_5_NAME] → V. Clean Code & Modular Design
  - [PRINCIPLE_6_NAME] → VI. Agentic Dev Stack Workflow
- Added sections: Technology Constraints, Security Requirements, Workflow Rules
- Removed sections: None (redefined template placeholders)
- Templates requiring updates:
  - .specify/templates/plan-template.md (✅ aligned)
  - .specify/templates/spec-template.md (✅ aligned)
  - .specify/templates/tasks-template.md (✅ aligned)
- Follow-up TODOs: None.
-->

# Phase II: Todo Full-Stack Web Application Constitution

## Core Principles

### I. Three-Layer Architecture
The system follows a three-layer architecture: Frontend (Next.js), Backend API (FastAPI), and Database (Neon PostgreSQL). Backend logic must be strictly separated into **routers → services → repository layers** to ensure modularity and maintainability.

### II. Repository-Only Data Access
All database interactions MUST go through the repository layer. Direct database access from routers or services is strictly prohibited. This ensures a single source of truth for data access patterns and simplifies database-level testing.

### III. JWT-Based Authentication (NON-NEGOTIABLE)
All API endpoints MUST require valid JWT authentication. Authentication is handled by Better Auth on the frontend, and the backend MUST verify the JWT signature on every request using a shared secret. Users can only access their own tasks, filtered by `user_id`.

### IV. Type-Safe Development
Use Python 3.13+ type hints for all parameters and return values in the backend. SQLModel must be used for ORM and request/response validation. The frontend must use TypeScript and ensure type parity with the backend API contracts.

### V. Clean Code & Modular Design
Functions should be small, single-purpose, and declarative. All public classes and functions must include descriptive docstrings. Each module must be independent and reusable, avoiding circular dependencies or tightly coupled logic.

### VI. Agentic Dev Stack Workflow
Development follows the Agentic Dev Stack workflow: Write spec → Generate plan → Break into tasks → Implement via Gemini CLI. No manual coding is allowed; all implementations must be generated through the workflow to ensure consistency and auditability.

## Technology Constraints
The project is strictly bound to the following technology stack:
- **Backend Language/Framework**: Python 3.13+, FastAPI
- **ORM & Data Validation**: SQLModel
- **Database**: Neon Serverless PostgreSQL
- **Frontend Framework**: Next.js 16+ (App Router)
- **Authentication**: Better Auth issuing JWT tokens
- **Communication**: REST API with JWT in `Authorization: Bearer <token>` header

## Security Requirements
- All API endpoints MUST require valid JWT verification.
- User data isolation is mandatory; all queries MUST filter by `user_id`.
- All secrets (DB credentials, JWT secrets) MUST be stored in `.env` files and never committed to source control.
- The API MUST return `401 Unauthorized` for failed authentication or missing tokens.
- Passwords must be securely hashed before storage (handled via Better Auth).

## Workflow Rules
- Development follows **Spec-Kit Plus** methodology.
- Every user interaction MUST generate a **Prompt History Record (PHR)**.
- Each feature must be implemented independently and verified before integration.
- Commit messages MUST follow the format: `type(scope): description`.

## Governance
This constitution supersedes all other project practices. Any architectural or security violation must be explicitly flagged and justified in the Implementation Plan's Complexity Tracking section. Amendments to this constitution require a version increment and must be propagated across all dependent templates.

**Version**: 2.0.0 | **Ratified**: 2026-03-06 | **Last Amended**: 2026-03-06
