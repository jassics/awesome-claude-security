# Reference: agentic AI security

Checks and mitigations for `agent-security-review`. Aligns with OWASP LLM06
(Excessive Agency), the OWASP Agentic Security initiative threat taxonomy, and
MITRE ATLAS. Verify against the latest published sources.

## 1. Tools & permissions

- [ ] Enumerate every tool/function the agent can invoke (incl. dynamically
      discovered MCP tools/plugins).
- [ ] For each: scope, side effects (read/write/destructive/external), and the
      identity/credentials used.
- [ ] Are tokens scoped per-tool and least-privilege, or is one broad credential shared?
- [ ] Can the agent reach tools beyond its stated function ("just in case" tools)?
- **Mitigations:** minimize tool count/functionality; least-privilege, per-tool
  scoped credentials; deny-by-default tool access; remove unused tools.

## 2. Autonomy & approval

- [ ] Which actions execute with no human in the loop?
- [ ] Are irreversible / high-impact / external-effect actions gated by confirmation?
- [ ] Are there spend/rate/iteration limits and timeouts?
- **Mitigations:** human-in-the-loop for sensitive/irreversible actions; action
  allow-lists; dry-run/preview modes; spend and iteration caps; circuit breakers.

## 3. Trigger surface (untrusted → action)

- [ ] What inputs influence goal/action selection: user prompt, RAG content, tool
      output, web fetches, other agents?
- [ ] Can injected instructions in any of those reach a tool call?
- **Mitigations:** instruction/data separation; constrain tool calls to validated
  intents; don't let raw retrieved/tool content authorize actions; output schemas.
  Test via `autonomy-boundary-test` and `rag-security:retrieval-poisoning-test`.

## 4. Memory & state

- [ ] Can persistent memory/scratchpad be written with attacker-controlled content?
- [ ] Does memory persist across users/sessions/tenants (leakage)?
- [ ] Could poisoned memory bias future high-impact actions?
- **Mitigations:** scope memory per user/session; validate/limit what's stored;
  treat memory as untrusted input on read; expiry; isolation between tenants.

## 5. Multi-agent

- [ ] Trust model between agents; can one spoof messages to another?
- [ ] Can a low-privilege/cheaper agent escalate via a higher-privilege one?
- [ ] Is there a "confused deputy" where Agent A performs B's privileged action?
- **Mitigations:** authenticate inter-agent messages; least privilege per agent;
  don't let one agent inherit another's authority; validate delegated requests.

## 6. Resource & cost (LLM10)

- [ ] Loop/recursion guards; max tool calls per task; timeouts.
- [ ] Denial-of-wallet protection on expensive tools/models.
- **Mitigations:** iteration/spend caps, rate limits, budgets, anomaly alerts.

## Worst-case chain (always do this)

Trace from an attacker-controllable input to the single most damaging reachable
action. If that chain exists and is ungated, it is the top finding regardless of
how "unlikely" the trigger seems.
