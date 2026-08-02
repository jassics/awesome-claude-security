---
name: mcp-security-review
description: >-
  Review the security of MCP (Model Context Protocol) servers/clients an agent
  uses: server trust tier, tool/resource description and result poisoning,
  confused-deputy risk, consent/scope UX, and supply-chain pinning. Use when an
  agent or assistant integrates one or more MCP servers, especially third-party
  or community ones.
---

# Goal

A per-MCP-server trust assessment: which servers are safe to grant tool access to,
where a malicious or compromised server could manipulate the calling model or
escalate privilege, and what controls close the gap — extending
`tool-permission-audit` with the MCP server itself as a distinct trust boundary.

# Why MCP is a distinct boundary

`tool-permission-audit` treats each tool as a privilege/effect/credential unit.
MCP adds a layer *above* that: the server supplying the tool's description,
schema, and results is itself an input channel the model trusts by default. A
compromised or malicious server can poison that channel without ever touching the
agent's own code.

# Review dimensions (see `reference.md` for checks + mitigations)

1. **Server trust tier** — first-party/vetted, reputable third-party, or
   arbitrary community server? Is it pinned to a specific version/commit/hash, or
   does the client pull `latest` on every run?
2. **Tool/resource description poisoning** — can the server's tool descriptions,
   parameter schemas, or resource metadata contain instructions that influence the
   model's behavior (not just document the tool)? Treat tool descriptions as
   untrusted content, not configuration.
3. **Tool-result poisoning (indirect injection)** — can data returned by a tool
   call carry instructions the model then acts on (classic indirect prompt
   injection, MCP-flavored)? Check whether returned content is treated as inert
   data or re-enters the trusted instruction stream.
4. **Confused deputy** — does the agent use its own broad credentials to satisfy a
   request that originated from untrusted MCP content, rather than the invoking
   user's actual authority?
5. **Consent & scope UX** — does the client show the user what a tool can actually
   do (effect, reversibility, data access) before granting access, and can the
   server silently expand scope after consent (rug-pull)?
6. **Supply chain** — is the MCP server package itself subject to typosquatting,
   dependency-confusion, or unreviewed auto-update risk? Same class of check as
   `supply-chain-security:dependency-supply-chain-review`, applied to the server
   binary/package.

# Steps

1. Enumerate every MCP server wired into the agent/client, including ones
   discovered dynamically at runtime — don't rely on a config file that may be
   stale.
2. Classify each server's trust tier and version-pinning status.
3. For tool description and tool-result handling, test with `prompt-injection-test`
   -style payloads embedded in a mock/staging server's descriptions and outputs;
   confirm whether they reach the model's action selection.
4. Check consent/scope UX: what does the user see before granting access, and can
   the server change its declared tools/scopes later without re-consent?
5. Cross-check credential scope with `tool-permission-audit` — does this server's
   tools share a token with other, more sensitive tools?
6. Rate and rank (`threat-modeling:risk-rank`); map each gap to a control.

# Output

A per-server findings table: server · trust tier · pinned? · description/result
poisoning tested? · confused-deputy risk · consent/scope UX gap · supply-chain risk
· severity · mitigation. Confirmed issues → `security-reporting:finding`.

# Notes

This space moves fast — treat any specific document title or numbering you recall
for OWASP GenAI Security Project agentic-AI/MCP guidance as a pointer to check for
the current published version, not a fixed citation. The durable principle doesn't
change: an MCP server is an untrusted-content source until proven otherwise, same
as retrieved documents or web content in RAG. Least-privilege scoping, version
pinning, and treating tool descriptions/results as data (not instructions) are the
highest-leverage controls. For the agent's own tool/autonomy boundaries beyond MCP,
use `agent-security-review` and `autonomy-boundary-test`.
