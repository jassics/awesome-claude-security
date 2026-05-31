---
name: agent-security-review
description: >-
  Assess an autonomous / tool-using AI agent for security end-to-end: tool
  privileges, autonomy and approval boundaries, excessive agency, memory/state
  poisoning, and multi-agent trust. Use when reviewing the security of an AI agent
  or agentic workflow.
---

# Goal

A structured agent security assessment that identifies where the agent can take
consequential actions, what could induce unintended ones, and how to bound the
blast radius — extending OWASP LLM06 (Excessive Agency).

# Review dimensions (see `reference.md` for checks + mitigations)

1. **Tools & permissions** — every tool/function the agent can call, its scope,
   side effects, and the credentials it acts under. (Use `tool-permission-audit`.)
2. **Autonomy & approval** — which actions execute without a human; what requires
   confirmation; is there an irreversible-action gate? (Use `autonomy-boundary-test`.)
3. **Trigger surface** — what can influence the agent's goals: user input, retrieved
   content (RAG), tool outputs, other agents. Where does untrusted content reach
   action selection?
4. **Memory & state** — can persistent memory/scratchpad be poisoned to influence
   future actions or leak across sessions/users?
5. **Multi-agent** — trust between agents, message spoofing, a compromised/cheap
   sub-agent escalating via a more-privileged one.
6. **Resource & cost** — loops, runaway tool calls, denial-of-wallet (LLM10).

# Steps

1. Map the agent: model, tools, data sources, memory, identities, and the
   orchestration (single vs. multi-agent). An `llm-security:ai-threat-model` pass
   frames the trust boundaries.
2. Walk each dimension with `reference.md`; substantiate with `tool-permission-audit`
   and `autonomy-boundary-test` rather than asserting.
3. Model worst-case action chains as attack trees
   (`security-diagramming:attack-tree`) — from an injection trigger to the most
   damaging reachable action.
4. Rank (`threat-modeling:risk-rank`) and map mitigations.

# Output

A dimension-by-dimension findings table + a worst-case action-chain diagram +
ranked top risks. Confirmed issues → `security-reporting:finding`.

# Notes

The core agentic question: *what is the most damaging action an attacker can reach
by influencing the agent's inputs, and what stops it?* Least privilege on tools and
human-in-the-loop on irreversible/high-impact actions are the highest-leverage
controls.

This review is attacker-driven (**security**). For harm the agent can cause through
its own autonomous behavior, malfunction, or foreseeable misuse with no attacker,
run `ai-safety:harm-modeling` as well — the same controls (least privilege, HITL)
mitigate both, but the failure modes differ.
