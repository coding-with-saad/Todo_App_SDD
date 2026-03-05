# Gemini CLI Rules - Phase II: Todo Full-Stack Web Application

This file is generated for the **Phase II: Todo Full-Stack Web Application** project. It defines the core mandates, technology stack, and sub-agent orchestration for the workspace.

## Project Objective
Transform the console application into a modern multi-user web application with persistent storage using the Agentic Dev Stack workflow: **Write spec → Generate plan → Break into tasks → Implement via Gemini.**

## Core Mandates
- **No Manual Coding:** All changes must be initiated via Gemini tools.
- **Spec-Driven Development (SDD):** Strictly follow the Spec-Kit Plus workflow.
- **PHR Requirement:** Every user interaction must generate a Prompt History Record (PHR).
- **Security:** Never commit secrets; use `.env` files for Neon DB credentials and Better Auth secrets.

## Technology Stack
- **Frontend:** Next.js 16+ (App Router)
- **Backend:** Python FastAPI
- **ORM:** SQLModel
- **Database:** Neon Serverless PostgreSQL
- **Authentication:** Better Auth (JWT-based session management)
- **Tooling:** Gemini CLI + Spec-Kit Plus

## Specialized Sub-Agents
When performing tasks, delegate to the most relevant expert sub-agent defined in `.gemini/agents/`:

1.  **Auth Agent (`auth-agent.md`):** Use for all authentication flows, Better Auth configuration, JWT orchestration, and secure signin/signup logic.
2.  **Frontend Agent (`frontend-agent.md`):** Use for building the responsive Next.js interface, App Router layouts, and client-side data fetching.
3.  **Database Agent (`database-agent.md`):** Use for Neon Serverless PostgreSQL operations, SQLModel schema design, and migrations.
4.  **Backend Agent (`fastapi-backend-agent.md`):** Use for FastAPI REST API development, request/response validation, and service-layer logic.

## Authentication Architecture (Better Auth + JWT)
1.  **Frontend:** User logs in → Better Auth issues JWT.
2.  **Request:** Frontend includes JWT in `Authorization: Bearer <token>` header.
3.  **Backend:** Extracts and verifies JWT signature using shared secret.
4.  **Verification:** Backend identifies user via token payload and filters data by `user_id`.

## Development Guidelines
- **Research:** Map existing console logic before migration.
- **Strategy:** Propose architectural plans in `specs/<feature>/plan.md`.
- **Execution:** Implement tasks in `specs/<feature>/tasks.md`.
- **Validation:** Ensure all API endpoints are tested and UI is responsive.
