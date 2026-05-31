---
name: ai-threat-model
description: >-
  Threat model an LLM / RAG / agentic AI system: map prompts, data sources,
  tools, identities, and trust boundaries, then enumerate AI-specific threats and
  mitigations. Use when designing or reviewing a GenAI feature's security.
---

# Goal

A threat model tailored to GenAI: the AI-specific trust boundaries and data flows
made explicit, threats enumerated against them, and mitigations mapped — bridging
classic threat modeling with the OWASP LLM Top 10.

# AI-specific elements to map

- **Model boundary** — which model(s), hosted where, what trust level.
- **Prompt assembly** — system prompt, user input, retrieved context, tool output:
  what's trusted vs. untrusted, and where they mix (the core injection risk).
- **Data sources** — RAG stores, knowledge bases, fine-tune data, embeddings;
  per-tenant isolation and ingestion provenance.
- **Tools/actions** — every tool/function the model can call, its privileges,
  side effects, and approval requirements (agency boundary).
- **Identities & secrets** — tokens the model/tools use; whose authority they act
  under; what's reachable.
- **Output sinks** — where model output flows (rendered HTML, code exec, DB, API).

# Steps

1. Build/ingest a DFD with AI elements above (`security-diagramming:threat-model-dfd`),
   marking the **trust boundary between trusted instructions and untrusted
   content/tool output** explicitly.
2. Run **STRIDE** over the DFD (`threat-modeling:stride`) AND overlay the **OWASP
   LLM Top 10** categories (`owasp-llm-top10`) — GenAI threats don't all fit
   STRIDE neatly (e.g. excessive agency, misinformation).
3. For agentic systems, model the autonomy/permission boundary specifically: what
   the agent can do without a human, and worst-case action chains
   (`security-diagramming:attack-tree`).
4. Enumerate threats, rank (`threat-modeling:risk-rank`), map mitigations.

# Output

A GenAI threat model: AI DFD + threat table (element · threat · STRIDE/LLM-Top-10
ref · risk · mitigation) + top-risks summary. Use `security-reporting` for the
deliverable.

# Notes

The decisive question for most GenAI systems: *where does untrusted content gain
the ability to influence trusted actions?* Find every such crossing and constrain
it. For RAG-heavy or agent-heavy systems, the `rag-security` / `agentic-ai-security`
plugins go deeper.

This is a **security** threat model (attacker-driven). It does not cover **AI
safety** — harm to users/society without an attacker (harmful content, bias,
reliability, misuse). For that, run `ai-safety:harm-modeling` alongside this.
