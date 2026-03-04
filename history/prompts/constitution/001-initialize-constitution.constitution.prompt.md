---
id: 001
title: Initialize phase-driven project constitution
stage: constitution
date: 2026-03-04
surface: agent
model: gemini-2.0-flash
feature: none
branch: main
user: User
command: /sp.constitution
labels: [constitution, architecture, phases, development]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
  - .specify/templates/tasks-template.md
  - .gemini/commands/sp.constitution.toml
tests:
  []
---

## Prompt

# /sp.constitution # Project Constitution

## 1. Architecture Principles

- The system must evolve in clearly separated phases.
- Each phase must be independently runnable before moving to the next.
- Phase I starts as a pure in-memory console application with no external persistence.
- Core business logic must remain framework-independent and reusable across all phases.
- Domain models must not be rewritten when transitioning between phases.
- Maintain strict separation of concerns:
  - Domain layer
  - Application layer
  - Infrastructure layer
  - Interface layer
- All external integrations (AI, database, messaging, Kubernetes, cloud services) must be implemented as adapters.
- Core logic must never directly depend on infrastructure tools.

---

## 2. Phase Constraints

### Phase I – In-Memory Console Application

- Language: Python 3.12
- Console-based interface only.
- No web frameworks allowed.
- Data stored strictly in memory using structured classes.
- No database.
- No external APIs.
- Modular design required.
- All logic must be testable without interactive input dependency.

---

### Phase II – Full-Stack Web Application

- Frontend: Next.js
- Backend: FastAPI
- ORM: SQLModel
- Database: Neon PostgreSQL
- RESTful API design required.
- No business logic inside route handlers.
- Database access allowed only through a repository layer.
- Configuration strictly via environment variables.

---

### Phase III – AI-Powered Todo Chatbot

- AI Integration: OpenAI ChatKit
- Agent Framework: OpenAI Agents SDK
- Tool Protocol: Official MCP SDK
- AI must interact only through defined tool interfaces.
- AI layer must not directly access the database.
- All AI actions must pass through service layer validation.
- Deterministic fallback logic required if AI response fails.

---

### Phase IV – Local Kubernetes Deployment

- Containerization: Docker
- Local cluster: Minikube
- Package management: Helm
- AI deployment assistant: kubectl-ai
- Agent orchestration: kagent
- Each service must have its own Dockerfile.
- No hardcoded ports or secrets inside containers.
- Helm charts must support environment-based overrides.

---

### Phase V – Advanced Cloud Deployment

- Messaging: Kafka
- Distributed runtime: Dapr
- Cloud provider: DigitalOcean DOKS
- All services must be stateless.
- Event-driven communication required for cross-service updates.
- Infrastructure must be fully reproducible through configuration.
- No manual production configuration changes.

---

## 3. Code Quality Standards

- Strict type hints required across all Python code.
- No function longer than 40 lines.
- All public classes and functions must include docstrings.
- No circular dependencies allowed.
- Unit tests required for all core business logic.
- Refactor before extending large files.

---

## 4. Security Requirements

- Secrets must exist only in environment variables or secret managers.
- Validate input at every system boundary.
- Never log sensitive data.
- Authentication required starting from Phase II.
- AI prompts must not expose internal system structure.

---

## 5. Workflow Rules

- If a requirement is unclear, ask exactly one clarifying question before proceeding.
- When architectural decisions arise, propose three structured options before implementation.
- After completing a phase milestone, summarize architecture decisions made.
- If any implementation violates this constitution, explicitly flag the violation.
- No phase may be skipped.
- Each phase must be stable before proceeding to the next.

## Response snapshot

Updated project constitution at `.specify/memory/constitution.md` with detailed architecture principles, phase-driven evolution (Phase I to V), code quality, security, and workflow rules. Propagated changes to `plan-template.md` and `tasks-template.md` for phase-compliance.

## Outcome

- ✅ Impact: High (Foundational)
- 🧪 Tests: n/a
- 📁 Files: constitution.md, plan-template.md, tasks-template.md, sp.constitution.toml
- 🔁 Next prompts: /sp.specify
- 🧠 Reflection: Successfully initialized the project with a robust phase-driven development model.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
