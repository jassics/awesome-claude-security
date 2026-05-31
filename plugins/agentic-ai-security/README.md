# agentic-ai-security

Security for **autonomous, tool-using AI agents** — single-agent and multi-agent.
Focuses on the agentic blast radius: **excessive agency**, **tool privileges and
abuse**, **autonomy/permission boundaries**, **memory/state poisoning**, and
**prompt-injection-to-action** chains.

A **genai** domain plugin; member of [`genai-suite`](../genai-suite/). It picks up
where `llm-security` (LLM06 Excessive Agency) leaves off and goes deep on actions.

## Install

```
/plugin install agentic-ai-security@awesome-claude-security
# or the whole GenAI stack:
/plugin install genai-suite@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/agentic-ai-security:agent-security-review` | Assess an agent's security end-to-end (tools, autonomy, memory, multi-agent trust). |
| `/agentic-ai-security:tool-permission-audit` | Inventory the agent's tools and their privileges; find least-privilege gaps. |
| `/agentic-ai-security:autonomy-boundary-test` | Test what the agent will do without human confirmation, incl. injected-goal scenarios. |

## Security vs. safety

This plugin covers agent **security** — an *attacker* inducing unintended actions.
The **safety** side — an agent causing harm through its *own* autonomous behavior,
malfunction, or foreseeable misuse (no attacker required) — is in
[`ai-safety`](../ai-safety/) (`harm-modeling`). Autonomous systems usually need both.

## Pairs well with

`llm-security`, `rag-security`, `threat-modeling`,
`security-diagramming` (attack trees for action chains), `security-reporting`,
and [`ai-safety`](../ai-safety/).
