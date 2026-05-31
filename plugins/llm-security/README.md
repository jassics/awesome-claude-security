# llm-security

Security for GenAI systems. Assess an LLM-backed app against the **OWASP Top 10
for LLM Applications**, test for **prompt injection** (direct and indirect), and
**threat model** LLM / RAG / agentic architectures. Includes a senior
**`llm-security-reviewer`** agent for end-to-end assessments.

A **genai** plugin. Sibling plugins on the roadmap go deeper per surface:
`rag-security`, `agentic-ai-security`, `multimodal-security`, `mlops-security`.

## Install

```
/plugin install llm-security@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/llm-security:owasp-llm-top10` | Assess an LLM app against the OWASP LLM Top 10. |
| `/llm-security:prompt-injection-test` | Test a feature for direct/indirect prompt injection. |
| `/llm-security:ai-threat-model` | Threat model an LLM/RAG/agent system (trust boundaries, data flows, tool access). |

## Agents

| Agent | Use for |
| --- | --- |
| `llm-security-reviewer` | A full, multi-step security review of a GenAI feature. |

## Security vs. safety

This plugin covers **security** — protecting LLM systems from attackers (injection,
disclosure, abuse). It does **not** cover **AI safety** — whether the system causes
harm to users/society absent any attacker (harmful content, bias, reliability,
misuse). For that, see [`ai-safety`](../ai-safety/). Most GenAI features need both.

## Pairs well with

`threat-modeling`, `security-diagramming`, `security-reporting`,
and [`ai-safety`](../ai-safety/) (the complementary safety discipline).
