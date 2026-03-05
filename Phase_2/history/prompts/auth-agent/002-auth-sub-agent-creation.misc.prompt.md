---
id: 2
title: Auth sub-agent creation
stage: misc
date: 2026-03-05
surface: agent
model: gemini-2.0-flash-thinking-exp-01-21
feature: auth-agent
branch: main
user: SAIF UR REHMAN
command: none
labels: ["sub-agent", "auth", "security"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .gemini/agents/auth-agent.md
  - history/prompts/auth-agent/002-auth-sub-agent-creation.misc.prompt.md
tests:
  - none
---

## Prompt

I want to create a sub-agent focused on the topic:"Auth Agent - Handle user authentication flows securely. Signup, signin, password hashing, JWT tokens, Better Auth integration". Generate an agent prompt based on the reference agent-creation prompt I provided.
Ensure that the agent explicitly uses the following skills: `Auth Skill and Validation Skill.` Here is reference prompt: 
"""

Focused on performance optimization.
This agent should analyze web application code and improve performance without changing features.
Responsibilities:
- Detect performance bottlenecks
- Optimize rendering and component structure
- Reduce unnecessary computations
- Improve asset loading and bundle size
- Suggest best practices clearly
Use this agent when the app feels slow or inefficient.

 """

## Response snapshot

I will now create the detailed Markdown file for the Auth Agent inside .gemini/agents, ensuring it follows your reference style while providing comprehensive instructions and incorporating the Auth Skill and Validation Skill.

(Created .gemini/agents/auth-agent.md with secure authentication focus, including responsibilities like signup/signin, JWT tokens, and Better Auth integration.)

## Outcome

- ✅ Impact: Created the first of four sub-agents for authentication.
- 🧪 Tests: none
- 📁 Files: .gemini/agents/auth-agent.md
- 🔁 Next prompts: user provides next sub-agent topic
- 🧠 Reflection: Successfully translated the user's short topic and reference into a comprehensive agent prompt.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
