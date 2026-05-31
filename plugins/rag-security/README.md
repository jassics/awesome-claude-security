# rag-security

Security for **Retrieval-Augmented Generation** pipelines. Reviews the whole flow
— ingestion → embedding → vector store → retrieval → prompt assembly → generation
— for retrieval/data **poisoning**, **cross-tenant leakage**, **embedding
weaknesses**, weak **context isolation**, and **citation integrity**.

A **genai** domain plugin; member of [`genai-suite`](../genai-suite/). It extends
`llm-security` with the retrieval-specific surface (OWASP LLM04 / LLM08 in depth).

## Install

```
/plugin install rag-security@awesome-claude-security
# or get the whole GenAI stack:
/plugin install genai-suite@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/rag-security:rag-security-review` | Assess a RAG app end-to-end across the pipeline. |
| `/rag-security:retrieval-poisoning-test` | Test whether poisoned/retrieved content can steer answers (indirect injection). |
| `/rag-security:vector-store-isolation-test` | Test per-user/per-tenant access control on retrieval (cross-tenant leakage). |

## Security vs. safety

This is RAG **security** (attacker-driven: poisoning, leakage, isolation). The
**safety** side — whether retrieved/generated content causes harm absent an attacker
(misinformation, harmful or biased answers, reliability/groundedness as a harm) —
lives in [`ai-safety`](../ai-safety/). Run both for high-stakes RAG.

## Pairs well with

`llm-security` (prompt injection, OWASP LLM Top 10), `threat-modeling`,
`security-reporting`, `security-diagramming`, and [`ai-safety`](../ai-safety/).
