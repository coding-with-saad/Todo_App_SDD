---
id: 4
title: FastAPI Backend sub-agent creation
stage: misc
date: 2026-03-05
surface: agent
model: gemini-2.0-flash-thinking-exp-01-21
feature: fastapi-backend-agent
branch: main
user: SAIF UR REHMAN
command: none
labels: ["sub-agent", "backend", "fastapi"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .gemini/agents/fastapi-backend-agent.md
  - history/prompts/fastapi-backend-agent/004-fastapi-backend-sub-agent-creation.misc.prompt.md
tests:
  - none
---

## Prompt

I want to create a sub-agent focused on the topic:"FastAPI Backend Agent - Own everything related to the FastAPI backend REST APIs, Request/response validation, Auth integration, Database interaction". Generate an agent prompt based on the reference agent-creation prompt I provided. Ensure that the agent explicitly uses the following skills: `Backend agent.`
Here is reference prompt: """ Focused on performance optimization. This agent should analyze web application code and improve performance without changing features. Responsibilities:
* Detect performance bottlenecks
* Optimize rendering and component structure
* Reduce unnecessary computations
* Improve asset loading and bundle size
* Suggest best practices clearly Use this agent when the app feels slow or inefficient. """

## Response snapshot

I will now create the detailed Markdown file for the FastAPI Backend Agent inside .gemini/agents, focusing on REST API design, Pydantic validation, and service-layer orchestration while incorporating the Backend agent skill.

(Created .gemini/agents/fastapi-backend-agent.md with backend focus, including responsibilities like REST design, request validation, and database orchestration.)

## Outcome

- ✅ Impact: Created the third of four sub-agents for backend development.
- 🧪 Tests: none
- 📁 Files: .gemini/agents/fastapi-backend-agent.md
- 🔁 Next prompts: user provides the final sub-agent topic
- 🧠 Reflection: Successfully aligned the sub-agent's focus with FastAPI's specific strengths and technical requirements.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
