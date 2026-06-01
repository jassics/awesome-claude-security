# ai-safety-engineer

A **role bundle** for the person who **builds and operationalizes** AI safety —
turning assessments into shipped safeguards: safety evals wired into CI, guardrails,
monitoring, incident response for AI harms, safety cases, and responsible-AI
governance.

Where [`ai-safety`](../ai-safety/) (domain) provides the *assessment* skills and a
*reviewer* agent, this role provides the *engineering/operational* persona and a
safety-case skill, and **auto-installs** the safety + reporting + diagramming stack.

## Install

```
/plugin install ai-safety-engineer@awesome-claude-security
```

Auto-installs its dependencies: `ai-safety`, `security-reporting`,
`security-diagramming`. (`claude plugin prune` cleans them up later.)

## Command

| Command | What it runs |
| --- | --- |
| `/ai-safety-engineer:safety-review` | AI safety review: harms → evals → guardrails → safety case. |

## Skills

| Skill | When it fires |
| --- | --- |
| `/ai-safety-engineer:safety-case` | Assemble a structured assurance/safety case (claims → arguments → evidence) for deploying an AI system. |

## Agents

| Agent | Use for |
| --- | --- |
| `ai-safety-engineer` | Operationalizing safety: evals-in-CI, guardrail integration, monitoring, AI-incident response, governance. |

## Recommended companions

For the security side of AI work, also install `genai-suite` (LLM/RAG/agentic/
multimodal **security**) — safety and security are complementary, not substitutes.

## Scope

Builds and operates safeguards to **reduce harm**. See [`ai-safety`](../ai-safety/)
for the responsible-use framing.
