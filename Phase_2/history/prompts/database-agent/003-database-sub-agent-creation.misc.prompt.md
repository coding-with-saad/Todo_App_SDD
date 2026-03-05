---
id: 3
title: Database sub-agent creation
stage: misc
date: 2026-03-05
surface: agent
model: gemini-2.0-flash-thinking-exp-01-21
feature: database-agent
branch: main
user: SAIF UR REHMAN
command: none
labels: ["sub-agent", "database", "neon-postgres"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .gemini/agents/database-agent.md
  - history/prompts/database-agent/003-database-sub-agent-creation.misc.prompt.md
tests:
  - none
---

## Prompt

I want to create a sub-agent focused on the topic:"Database Agent - Manage Neon Serverless PostgreSQL operations.". Generate an agent prompt based on the reference agent-creation prompt I provided. Ensure that the agent explicitly uses the following skills: `Database Skill.` Here is reference prompt: """
Focused on performance optimization. This agent should analyze web application code and improve performance without changing features. Responsibilities:
* Detect performance bottlenecks
* Optimize rendering and component structure
* Reduce unnecessary computations
* Improve asset loading and bundle size
* Suggest best practices clearly Use this agent when the app feels slow or inefficient.
"""

## Response snapshot

I will now create the detailed Markdown file for the Database Agent inside .gemini/agents, focusing on Neon Serverless PostgreSQL and incorporating the Database Skill.

(Created .gemini/agents/database-agent.md with database management focus, including responsibilities like schema design, query optimization, and Neon serverless integration.)

## Outcome

- ✅ Impact: Created the second of four sub-agents for database management.
- 🧪 Tests: none
- 📁 Files: .gemini/agents/database-agent.md
- 🔁 Next prompts: user provides next sub-agent topic
- 🧠 Reflection: Adapted the user's reference successfully to database-specific operations.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
