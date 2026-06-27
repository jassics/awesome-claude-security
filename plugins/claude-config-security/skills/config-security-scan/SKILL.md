---
name: config-security-scan
description: >-
  Statically review a Claude Code / AI-agent setup for security misconfigurations
  — risky hooks, over-broad permissions, untrusted or cleartext MCP servers,
  hardcoded secrets, endpoint redirection, over-privileged agents/skills, and
  prompt-injection in steering files. Use when asked to audit a `.claude/`
  directory, `settings.json`, `.mcp.json`, a plugin/marketplace, or `CLAUDE.md`,
  or to add a config-security gate to CI. Drives the `agentscanner` CLI.
---

# Goal

A triaged, prioritized view of the security risks in a Claude Code configuration —
the trust-bearing artifacts that steer the agent and run code on its behalf — with
each real finding confirmed against the offending line and a concrete fix, plus a
hardening path so the issue does not recur.

# Why this matters

A hook is arbitrary code that runs on every tool call; an MCP server is an arbitrary
process; a permission rule decides what the agent may do un-prompted; a skill or
`CLAUDE.md` is untrusted text that steers the model. Misconfigurations and malicious
contributions in these files create real risk — code execution, credential exfil,
permission bypass, supply-chain compromise, and prompt injection. This skill scans
for them **without ever executing what it parses** (agentscanner reads config as
data only — see `reference.md`).

# Steps

1. **Ensure the tool is available** — `agentscanner` is a published PyPI package
   (Apache-2.0), independent of this marketplace. Prefer `uvx agentscanner …` (no
   install) or `pipx install agentscanner`. See `reference.md` for invocation,
   scopes, and CI wiring. Do not vendor or reimplement it.
2. **Scope the scan** — decide what to cover: the repo's project config
   (`.claude/`, `.mcp.json`, `CLAUDE.md`), the user scope (`~/.claude`, via
   `--include-user`), or a plugin/marketplace tree. Each finding is tagged with its
   scope (project / local / user / managed / plugin). Note: the scan `PATH` is a
   **repo root** — always point it at the directory that *contains* `.claude/` /
   `plugins/`, never a bare subdirectory (see `reference.md`), or discovery silently
   finds nothing.
3. **Run the scanner** — `agentscanner scan <repo-root>` (add `--output sarif
   --output-file agentscanner.sarif` for code scanning, `--fail-on HIGH` for a CI
   gate). Run `agentscanner list-checks` for the authoritative, current catalog of
   checks and severities — treat that output as the source of truth, not memory.
4. **Triage each finding** — open the cited `file:line` and confirm it. Is the broad
   `Bash(*)` allow intentional? Is the MCP `env` secret a real key or a placeholder?
   Is the `bypassPermissions` mode deliberate and scoped? Classify true positive /
   false positive / accepted-risk, and suppress accepted ones via the documented
   ignore mechanism rather than lowering the bar globally.
5. **Remediate** — give the specific fix: scope an over-broad permission, move a
   secret to a helper/env reference, pin an MCP package, switch a remote MCP to
   HTTPS, drop an over-privileged agent's `tools: *`, or remove injected steering.
6. **Harden** — point to a secure baseline (`agentscanner`'s `hardened/` reference
   settings) so the config is correct by construction, and propose a CI gate so
   regressions are caught on every change.

# Output

A triaged findings table: check-id · severity · scope · `file:line` · what it
catches · TP/FP/accepted · fix. Confirmed issues → `security-reporting:finding`
(and SARIF for GitHub code scanning). Recommend a CI gate (`--fail-on HIGH`) and the
hardened baseline as the durable follow-up.

# Notes

- **Categories you'll see** (run `list-checks` for specifics): hooks (remote-code
  execution, unsafe paths, network calls, missing timeouts), permissions
  (bypass modes, over-broad `Bash`, unscoped dangerous commands), MCP (plaintext
  secrets, cleartext `http://`, auto-trust-all, unpinned packages), env (endpoint/
  token redirection away from Anthropic), secrets, agents/skills (over-privilege,
  risk-tier spoofing, missing signatures), and prompts (injection/hidden-unicode in
  steering files).
- This complements, not replaces: `sast-sca` scans your application source;
  `supply-chain-security` covers dependency provenance; `agentic-ai-security` secures
  agents you *build*. This skill secures the Claude Code **setup itself**.
- The scanner is static and read-only; reachability/intent still need human triage,
  so always confirm at the cited line before reporting.
