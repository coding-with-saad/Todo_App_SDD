<!--
# Sync Impact Report
- Version change: null → 1.0.0 (Initial version)
- List of modified principles:
  - Library-First → Evolutionary Phases
  - CLI Interface → Independent Runnable Phases
  - Test-First → Core Business Logic Independence
  - Integration Testing → Domain Model Stability
  - Observability/Versioning → Strict Separation of Concerns
  - [Added] Adapter-Based Integrations
  - [Added] Core Logic Dependency Isolation
- Added sections:
  - Phase Constraints (Phase I to V)
  - Code Quality Standards
  - Security Requirements
  - Workflow Rules
- Removed sections: None (repurposed placeholders)
- Templates requiring updates:
  - .specify/templates/tasks-template.md (✅ updated)
  - .specify/templates/plan-template.md (✅ updated)
- Follow-up TODOs: None.
-->

# AI-Powered Todo Chatbot Constitution

## 1. Architecture Principles

### I. Evolutionary Phases
The system MUST evolve in clearly separated phases. No phase may be skipped, and each phase must be stable before proceeding to the next.

### II. Independent Runnable Phases
Each phase MUST be independently runnable and deliver a functional subset of features before moving to the next evolutionary stage.

### III. Core Business Logic Independence
Core business logic MUST remain framework-independent and reusable across all phases. It must never directly depend on infrastructure tools or external frameworks.

### IV. Domain Model Stability
Domain models MUST NOT be rewritten when transitioning between phases. They represent the core truth of the system and must remain stable as infrastructure evolves.

### V. Strict Separation of Concerns
Maintain strict separation between the following layers:
- **Domain layer**: Core entities and business rules.
- **Application layer**: Use cases and orchestration.
- **Infrastructure layer**: External tools, databases, and frameworks.
- **Interface layer**: CLI, Web, or AI agent interfaces.

### VI. Adapter-Based Integrations
All external integrations (AI, database, messaging, Kubernetes, cloud services) MUST be implemented as adapters following the Ports and Adapters pattern.

### VII. Core Logic Dependency Isolation
Core logic MUST NOT directly depend on infrastructure tools. Interaction with the outside world must happen through defined interfaces (Ports).

## 2. Phase Constraints

### Phase I – In-Memory Console Application
- **Language**: Python 3.12
- **Interface**: Console-based only. No web frameworks allowed.
- **Storage**: Strictly in-memory using structured classes. No database.
- **External Dependencies**: No external APIs.
- **Design**: Modular design required; all logic must be testable without interactive input.

### Phase II – Full-Stack Web Application
- **Frontend**: Next.js
- **Backend**: FastAPI
- **ORM**: SQLModel
- **Database**: Neon PostgreSQL
- **Design**: RESTful API; no business logic in route handlers.
- **Access**: Database access allowed only through a repository layer.
- **Configuration**: Strictly via environment variables.

### Phase III – AI-Powered Todo Chatbot
- **AI Integration**: OpenAI ChatKit
- **Agent Framework**: OpenAI Agents SDK
- **Tool Protocol**: Official MCP SDK
- **Security**: AI interacts only through defined tool interfaces; no direct database access.
- **Validation**: All AI actions must pass through service layer validation.
- **Reliability**: Deterministic fallback logic required if AI response fails.

### Phase IV – Local Kubernetes Deployment
- **Containerization**: Docker (one Dockerfile per service).
- **Local Cluster**: Minikube.
- **Package Management**: Helm (support environment-based overrides).
- **AI Assistance**: AI deployment assistant (kubectl-ai) and agent orchestration (kagent).
- **Security**: No hardcoded ports or secrets inside containers.

### Phase V – Advanced Cloud Deployment
- **Messaging**: Kafka (event-driven communication for cross-service updates).
- **Distributed Runtime**: Dapr.
- **Cloud Provider**: DigitalOcean DOKS.
- **Architecture**: All services must be stateless.
- **Operations**: Infrastructure fully reproducible through configuration; no manual production changes.

## 3. Code Quality Standards
- **Typing**: Strict type hints required across all Python code.
- **Complexity**: No function longer than 40 lines.
- **Documentation**: All public classes and functions must include docstrings.
- **Architecture**: No circular dependencies allowed.
- **Testing**: Unit tests required for all core business logic.
- **Refactoring**: Refactor before extending large files.

## 4. Security Requirements
- **Secrets**: Must exist only in environment variables or secret managers.
- **Validation**: Validate input at every system boundary.
- **Privacy**: Never log sensitive data.
- **Auth**: Authentication required starting from Phase II.
- **AI Safety**: AI prompts must not expose internal system structure.

## 5. Workflow Rules
- **Clarification**: If a requirement is unclear, ask exactly one clarifying question before proceeding.
- **Design**: Propose three structured options for architectural decisions before implementation.
- **Knowledge Capture**: Summarize architecture decisions after completing a phase milestone.
- **Compliance**: Explicitly flag any implementation that violates this constitution.
- **Governance**: Phase progression requires stability and completion of all constraints.

**Version**: 1.0.0 | **Ratified**: 2026-03-04 | **Last Amended**: 2026-03-04
