# responsible-ai-officer

A **role bundle** for AI governance — the GRC counterpart to
[`ai-safety-engineer`](../ai-safety-engineer/). Where the engineer *builds*
safeguards, this role *governs*: intake and risk-classification of AI use cases,
oversight and accountability, documentation discipline, and regulatory compliance
(NIST AI RMF, EU AI Act, ISO/IEC 42001).

Auto-installs the `ai-safety` stack and produces governance artifacts via the
reporting/diagramming plugins.

## Install

```
/plugin install responsible-ai-officer@awesome-claude-security
```

Auto-installs: `ai-safety`, `security-reporting`, `security-diagramming`.

## Skills

| Skill | When it fires |
| --- | --- |
| `/responsible-ai-officer:ai-use-case-intake` | Intake a proposed AI use case, classify its risk tier, and gate it with required controls. |

## Agents

| Agent | Use for |
| --- | --- |
| `responsible-ai-officer` | Standing up/running an AI governance program and reviews. |

## Pairs well with

`ai-safety` (the technical safety work it governs), `grc` (general security GRC,
roadmap), `ciso-toolkit` (roadmap), and the GenAI **security** plugins for the
attacker-risk side.
