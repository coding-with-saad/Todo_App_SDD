---
id: 1
title: Sub-agent creation request acknowledgment
stage: general
date: 2026-03-05
surface: agent
model: gemini-2.0-flash-thinking-exp-01-21
feature: none
branch: main
user: SAIF UR REHMAN
command: none
labels: ["sub-agents", "readiness"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - history/prompts/general/001-sub-agent-creation-request-acknowledgment.general.prompt.md
tests:
  - none
---

## Prompt

If I ask you to make me some sub-agents, you will make them.I will give you the topic and the reference form. You have to understand all this and Create a Markdown file that contains the details of sub-agents working on it, rather than creating strange files.You have to keep the content of sub-agents good and a little long so that all the concepts are clear and you have to keep the file of the agents inside .gemini/agents.I have to make 4 types of sub agents are you ready

## Response snapshot

I am ready to assist you in creating these sub-agents. Please provide the topic and the reference form for the 4 types of sub-agents you wish to develop. I will ensure their instructions are comprehensive, clear, and stored correctly within .gemini/agents.

## Outcome

- ✅ Impact: Acknowledged user request and confirmed readiness.
- 🧪 Tests: none
- 📁 Files: Created PHR
- 🔁 Next prompts: user provides sub-agent details
- 🧠 Reflection: User wants to define custom sub-agents for their workflow.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
