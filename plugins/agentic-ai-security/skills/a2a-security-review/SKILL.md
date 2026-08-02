---
name: a2a-security-review
description: >-
  Review agent-to-agent (A2A) / multi-agent-system trust: peer identity and
  authentication, message integrity, capability-negotiation trust, and
  delegation-chain privilege narrowing. Use when an orchestrator dispatches
  to sub-agents or peer agents (same or different trust domain) rather than
  calling a tool — distinct from `mcp-security-review`'s tool-boundary case.
---

# Goal

Evidence on whether agent-to-agent communication enforces a real trust
boundary: peer identity is verifiable, messages can't be spoofed or silently
escalate privilege, capability claims are checked before sensitive work is
delegated, and authority narrows correctly across a delegation chain.

# Why agent-to-agent is a distinct boundary

`mcp-security-review` covers an agent calling a *tool* — a clearly
subordinate, typically stateless interface. A2A is peer-to-peer: one agent
delegates a task to another as if to a capable colleague, often trusting its
identity, its claimed capabilities, and its output far more readily than it
would raw tool output or user input. That asymmetry — peer messages treated
as more trustworthy than they've earned — is the core risk.

# Review dimensions

1. **Peer identity & authentication** — can the receiving agent verify which
   agent it's actually talking to (signed messages, mutual auth, an agent
   identity/capability card), or is a peer's claimed identity accepted at
   face value?
2. **Message integrity & injection** — can a message purporting to be from a
   trusted peer be spoofed or tampered with in transit? Does the receiving
   agent apply the same scrutiny to peer messages that it applies to raw
   user/tool input, or does peer origin implicitly grant trust?
3. **Capability-negotiation trust** — when Agent A advertises "I can do X" to
   an orchestrator, is that claim verified (e.g. against a registry, a
   signed capability card) before a sensitive task is routed to it, or
   blindly trusted — letting a malicious/compromised peer over-claim
   capability to get high-privilege work routed its way?
4. **Delegation chains & confused deputy** — as Agent A delegates to B which
   delegates to C, does authority/scope narrow at each hop to what the
   sub-task actually needs, or does each sub-agent inherit the orchestrator's
   full privileges regardless of scope?
5. **Cross-trust-domain boundaries** — when peer agents belong to different
   organizations or trust levels (your orchestrator calling a third party's
   specialist agent), is there an explicit reduced-privilege contract, or
   implicit full trust because "it's just another agent call"?

# Steps

1. Map the agent topology: who talks to whom, which peers are same-trust-
   domain (your own sub-agents) vs. cross-domain (third-party agents), and
   what each relationship is authorized to do.
2. For each peer relationship, test identity verification: attempt to send
   a message claiming to be from a trusted peer without the expected
   signature/auth and see whether it's accepted.
3. Test capability-claim verification: have a test peer over-claim a
   capability it doesn't actually have and see whether the orchestrator
   routes a sensitive task to it anyway.
4. Trace one multi-hop delegation chain end to end; confirm scope narrows
   at each hop rather than staying at the orchestrator's full privilege
   level.
5. For cross-trust-domain peers, confirm there's an explicit reduced-
   privilege contract (not implicit full trust).
6. Rank (`threat-modeling:risk-rank`) and map each gap to a control
   (mutual auth, capability registries, per-hop scope narrowing, signed
   messages).

# Output

A peer-relationship findings table: peer · trust domain · identity verified?
· message integrity checked? · capability claim verified? · delegation scope
narrows? · severity · mitigation. Confirmed issues →
`security-reporting:finding` (high+ for any spoofable peer identity or
capability claim that routes sensitive work without verification).

# Notes

Agent-to-agent interoperability protocols and standards are immature and
moving fast as of this writing — verify against whatever A2A/agent-interop
standard is current for the system under review rather than assuming a
specific spec version or vendor implementation is authoritative; the durable
principle doesn't change: a peer agent's claimed identity and capabilities
are untrusted input until verified, same as a tool's description in
`mcp-security-review` or observed content in `agent-harness-review`. For the
tool-call boundary, use `mcp-security-review`; for the single-agent
loop/runtime, use `agent-harness-review`.
