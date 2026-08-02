---
name: agent-safety-lint
description: >-
  Check a Claude Code agent's runaway-risk controls — a missing or invalid
  `maxTurns` (unbounded turns/cost), and hook commands with no `timeout` — in
  YOUR OWN repo's `.claude/agents/*.md` or a plugin you're authoring. Use when
  writing or reviewing a subagent definition, before shipping a plugin agent,
  or when asked "does this agent have a turn/cost limit", "will this loop
  forever", or "check my agent's safety settings". Narrower and faster than
  the full `config-security-scan` audit — drives the same `agentscanner` CLI,
  filtered to the unbounded-consumption checks.
---

# Goal

Catch the one class of agent misconfiguration that has no safe platform
default: an agent that can run an unbounded number of turns, and hooks with
no timeout. Confirm every agent you author (or are reviewing) sets an
explicit, sane bound before it ships.

# Why this matters

There is no default cap on agent turns. An agent with no `maxTurns` (or an
invalid one — non-integer, zero, negative) runs until it finishes on its own
— fine for a well-scoped task, but a real risk for an open-ended prompt, a
runaway loop, unexpected cost, or an unattended CI/CD invocation that never
terminates (OWASP LLM10 Unbounded Consumption). A hook with no `timeout` has
the same failure mode for the command it runs on every matching tool call.

# Steps

1. **Ensure `agentscanner` is available** — `uvx agentscanner --help` (no
   install) or `pipx install agentscanner`. Require `>=0.3.0` — `AS-AGENT-005`
   (missing/invalid `maxTurns`) shipped in that release; earlier versions
   won't have it. `agentscanner version` to confirm.
2. **Scan just this check family** — from the repo root (the directory that
   contains `.claude/` or `plugins/`, not a bare subdirectory):
   ```
   agentscanner scan . --check AS-AGENT-005,AS-HOOK-004
   ```
3. **Read each finding**: `file:line`, the agent/hook it's on, and whether the
   field is missing (LOW) or present-but-broken (MEDIUM — worse, since it
   looks safe but doesn't bound anything: a non-integer, `0`, a negative
   number, or a boolean).
4. **Fix**: set `maxTurns` to a positive integer sized to the agent's actual
   job — a narrowly-scoped agent (single review type, few skills) typically
   needs less headroom than a broad multi-skill coordinator; there's no
   universal number, size it to what the agent actually does and re-run the
   scan to confirm it's clean. Set an explicit `timeout` on any hook command
   the same way.
5. **Re-run scan** to confirm clean, then continue with a full
   `config-security-scan` pass before shipping if this was a new plugin
   agent — this skill only covers the unbounded-consumption slice, not
   permissions, secrets, or MCP config.

# Output

A short pass/fail per agent/hook: clean, or `file:line` + missing/broken +
the fix applied. Not a full report — for a complete findings table use
`config-security-scan`.

# Notes

- This is a subset of `config-security-scan`'s `AS-AGENT-*`/`AS-HOOK-*`
  categories, scoped to exactly the fields with no safe default. Reach for
  the full scan for permissions, MCP, secrets, and steering-file checks.
- `agentscanner` is static and read-only — it parses frontmatter as data,
  never executes hook commands or the agent itself.
