# ai-safety-suite

A **suite** for **trustworthy AI** — installs both halves of responsible AI work in
one shot: **AI safety** (harm to people/society) **and** **GenAI security**
(harm from attackers). Use this when you own an AI feature end-to-end and need full
coverage.

Manifest-only bundle; it owns no skills, just composes existing plugins (each of
which you can also install on its own).

## Install

```
/plugin install ai-safety-suite@awesome-claude-security
```

## What it pulls in

| Dependency | Brings |
| --- | --- |
| `ai-safety` | Harm modeling, safety evals, responsible red-team, bias/fairness, guardrails, RAI governance. |
| `genai-suite` | The GenAI **security** stack: `llm-security`, `rag-security`, `agentic-ai-security`, `multimodal-security`. |

Transitively, that's the complete AI security **and** safety toolkit. (It does not
include the shared core `security-reporting` / `security-diagramming` directly —
install those, or get them via a role bundle like `ai-safety-engineer`.)

## Why both

> A secure model can still be unsafe; a safe model can still be insecure. Security
> and safety are complementary disciplines — most real AI features need both. See
> [docs/TAXONOMY.md](../../docs/TAXONOMY.md#ai-security-vs-ai-safety).
