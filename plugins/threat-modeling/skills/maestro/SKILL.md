---
name: maestro
description: >-
  Run a MAESTRO threat model — the Cloud Security Alliance's layered framework
  for multi-agent / agentic AI systems — enumerating threats at each layer of the
  agent stack and across agent-to-agent and cross-layer trust boundaries. Use when
  threat modeling a multi-agent or agentic AI system where agent-to-agent trust,
  orchestration logic, and delegated tool use matter more than a single data flow.
---

# Goal

A MAESTRO-layered threat analysis for a multi-agent/agentic system: the agent
stack decomposed into layers, cross-layer and cross-agent trust breaks enumerated,
and each mapped to a mitigation.

# Why MAESTRO, and when

STRIDE and PASTA are asset/data-flow-centric — excellent for a single system with a
clear DFD. Agentic systems add a different threat surface: autonomous agents
delegating to sub-agents, orchestrators trusting sub-agent output, tools/MCP
servers returning content that itself becomes an instruction, and emergent
behavior from agent-to-agent interaction that no single data flow captures.
MAESTRO (CSA, "Agentic AI Threat Modeling Framework: MAESTRO") decomposes the
agentic stack into layers and asks what can go wrong *at* each layer and *across*
layer/agent boundaries — complementary to, not a replacement for, STRIDE/PASTA.

- **Single-agent, simple system** → `stride` is enough.
- **Multi-agent, orchestrated, or tool/MCP-delegating system** → run MAESTRO
  alongside STRIDE; MAESTRO catches the cross-layer/cross-agent breaks STRIDE's
  per-element pass tends to miss.
- **GenAI feature generally** (RAG, single LLM call, etc.) → see
  `llm-security:ai-threat-model` for the OWASP LLM Top 10 overlay; that skill
  points back here for the multi-agent case.

# The layers (working model — see Notes)

1. **Foundation Models** — the model(s) themselves: training/fine-tune
   provenance, model-level vulnerabilities, jailbreak/alignment weaknesses.
2. **Data Operations** — data ingestion, RAG stores, embeddings, memory:
   provenance, poisoning, cross-tenant leakage.
3. **Agent Frameworks / Orchestration** — the orchestration logic, planning
   loops, inter-agent messaging: how one agent's output becomes another's input.
4. **Deployment & Infrastructure** — runtime, network exposure, secrets/identity
   the agents run under, sandboxing of tool execution.
5. **Evaluation & Observability** — monitoring, logging, eval harnesses: can an
   agent's misbehavior actually be detected, and can logs be trusted/tampered?
6. **Security & Compliance** — the controls layered on top (authz, guardrails,
   policy enforcement) and whether they apply consistently across agents.
7. **Agent Ecosystem** — the multi-agent system as a whole: agent-to-agent trust,
   delegation chains, third-party/external agents, and emergent behavior from
   their interaction.

# Steps

1. **Map the agents and their layer placement.** Identify every agent/sub-agent,
   what it's built on (layer 1), what data/memory it touches (layer 2), how it's
   orchestrated and what it messages to/from (layer 3), where it runs (layer 4).
2. **Per layer, enumerate trusted vs. untrusted.** What enters and leaves each
   layer, and is it treated as trusted instruction or untrusted content?
3. **Focus on cross-layer and cross-agent breaks.** The highest-value threats are
   boundary crossings: a compromised or manipulated sub-agent's output flowing
   untrusted into an orchestrator's decision layer; a tool/MCP result silently
   treated as trusted instruction; an eval/observability gap that lets layer-3
   misbehavior go undetected. Walk every agent-to-agent and agent-to-tool edge
   explicitly — don't stop at per-layer analysis alone.
4. **Rank** with `threat-modeling:risk-rank` (likelihood × impact).
5. **Map mitigations** per threat, noting existing controls vs. gaps — for
   tool/MCP-boundary specifics, hand off to `agentic-ai-security:mcp-security-review`
   and `agentic-ai-security:agent-security-review`.

# Output

A layer-by-layer threat table (layer · element/edge · threat · risk · mitigation ·
status) plus a short "top cross-layer/cross-agent risks" summary. Hand to
`security-reporting` if a formal document is needed.

# Notes

The 7-layer breakdown above is this skill's working model of MAESTRO based on
CSA's publicly described framework — cite CSA's published MAESTRO documentation
for the canonical, current layer names/count rather than treating the numbering
here as a fixed standard; the framework has evolved since its initial publication.
What matters operationally is the discipline: decompose the agent stack into
layers, then hunt specifically for trust breaks *between* layers and *between*
agents, which per-DFD STRIDE passes systematically under-weight. Use standalone
for a pure agentic-architecture review, or alongside `llm-security:ai-threat-model`
when the system is also GenAI/LLM-specific.
