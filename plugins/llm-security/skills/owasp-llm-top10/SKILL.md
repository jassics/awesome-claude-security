---
name: owasp-llm-top10
description: >-
  Assess an LLM-backed application against the OWASP Top 10 for LLM Applications,
  producing a per-category finding set with severity and mitigations. Use when
  reviewing a chatbot, copilot, RAG app, or any feature built on an LLM.
---

# Goal

A structured assessment across all ten OWASP LLM risk categories, with concrete
findings (or "not applicable / mitigated") and prioritized mitigations.

# Steps

1. **Map the system.** Identify the model(s), prompts/system prompts, data
   sources (RAG/tools), user input paths, output sinks, and what privileges the
   LLM and its tools hold. A quick `ai-threat-model` pass helps here.
2. **Walk each category** (see `reference.md` for the full LLM Top 10 with checks
   and mitigations): prompt injection, sensitive information disclosure, supply
   chain, data/model poisoning, improper output handling, excessive agency,
   system-prompt leakage, vector/embedding weaknesses, misinformation, and
   unbounded consumption.
3. **For each**: state applicability, evidence/observation, severity, and the
   specific mitigation. Use `prompt-injection-test` to substantiate injection
   findings rather than asserting them.
4. **Rank** the findings (`threat-modeling:risk-rank`) and summarize top risks.

# Output

A per-category table (category · applicable? · finding · severity · mitigation)
plus a ranked top-risks list. Route findings through `security-reporting:finding`
for formal writeups.

# Notes

Read `reference.md` for the authoritative category list, signs to look for, and
mitigations. Keep testing authorized and within the app's intended scope. Excessive
agency and improper output handling are the categories most often missed — give
them explicit attention.

The Top 10 increasingly folds in agentic risk (LLM06 Excessive Agency and
related entries) as apps move from single-turn chat to tool-using agents. For
MCP-specific and multi-tool agent trust-boundary review, see
`agentic-ai-security:mcp-security-review`; for the full agent threat model see
`agentic-ai-security:agent-security-review`.
