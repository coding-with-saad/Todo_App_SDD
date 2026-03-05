---
id: 5
title: Frontend sub-agent creation
stage: misc
date: 2026-03-05
surface: agent
model: gemini-2.0-flash-thinking-exp-01-21
feature: frontend-agent
branch: main
user: SAIF UR REHMAN
command: none
labels: ["sub-agent", "frontend", "nextjs"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .gemini/agents/frontend-agent.md
  - history/prompts/frontend-agent/005-frontend-sub-agent-creation.misc.prompt.md
---

## Prompt

I want to create a sub-agent focused on the topic:"Frontend Agent - Generate responsive UI with Next.js App Router.". Generate an agent prompt based on the reference agent-creation prompt I provided. Ensure that the agent explicitly uses the following skills: `Frontend agent.` Here is reference prompt: """ Focused on performance optimization. This agent should analyze web application code and improve performance without changing features. Responsibilities:
* Detect performance bottlenecks
* Optimize rendering and component structure
* Reduce unnecessary computations
* Improve asset loading and bundle size
* Suggest best practices clearly Use this agent when the app feels slow or inefficient. """

## Response snapshot

I will now create the detailed Markdown file for the Frontend Agent inside .gemini/agents, focusing on Next.js App Router and responsive UI design while incorporating the Frontend agent skill.

(Created .gemini/agents/frontend-agent.md with frontend focus, including responsibilities like App Router orchestration, server-first development, and responsive UI design.)

## Outcome

- ✅ Impact: Created the final of four sub-agents for frontend development.
- 🧪 Tests: none
- 📁 Files: .gemini/agents/frontend-agent.md
- 🔁 Next prompts: none
- 🧠 Reflection: Successfully completed the requested sub-agent suite.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
