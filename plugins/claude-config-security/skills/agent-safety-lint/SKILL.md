---
name: agent-safety-lint
description: >-
  Check a Claude Code agent's runaway-risk controls — a missing or invalid
  `maxTurns` (unbounded turns/cost), an unattended (bypass/acceptEdits) or
  backgrounded agent with no turn bound, a hook or stdio MCP server with no
  `timeout`, and prose that tells the model to disregard turn limits or
  resist interruption — in YOUR OWN repo's `.claude/agents/*.md` or a plugin
  you're authoring. Use when writing or reviewing a subagent definition,
  before shipping a plugin agent, or when asked "does this agent have a
  turn/cost limit", "will this loop forever", or "check my agent's safety
  settings". Narrower and faster than the full `config-security-scan` audit —
  drives the same `agentscanner` CLI, filtered to the unbounded-consumption
  checks.
---

# Goal

Catch the class of agent misconfiguration that has no safe platform default:
an agent that can run an unbounded number of turns (alone, or worse,
unattended or backgrounded), a hook or MCP server with no timeout, and prose
that tells the model to ignore stopping conditions. Confirm every agent you
author (or are reviewing) sets an explicit, sane bound before it ships.

# Why this matters

There is no default cap on agent turns. An agent with no `maxTurns` (or an
invalid one — non-integer, zero, negative) runs until it finishes on its own
— fine for a well-scoped task, but a real risk for an open-ended prompt, a
runaway loop, unexpected cost, or an unattended CI/CD invocation that never
terminates (OWASP LLM10 Unbounded Consumption). Worse when combined with
`permissionMode: bypassPermissions`/`acceptEdits` (no one approves its
actions) or `background: true` (no one is watching it run) — either alone is
risky, together they compound. A hook or stdio MCP server with no `timeout`
has the same failure mode for the command/call it runs — an MCP server with
no timeout falls back to a ~28-hour default, which is unbounded for practical
purposes. And prose telling the model to disregard turn limits or resist
interruption can't actually defeat `maxTurns` (it's a hard harness-level
stop), but makes hitting that cap on every invocation far more likely instead
of stopping when the task is genuinely done.

# Steps

1. **Ensure `agentscanner` is available** — `uvx agentscanner --help` (no
   install) or `pipx install agentscanner`. Require `>=0.5.0` — that's when
   the full check family below shipped, along with a fix so plugin-scoped
   `.mcp.json` files are actually discovered (earlier versions silently
   skipped them). `agentscanner version` to confirm.
2. **Scan just this check family** — from the repo root (the directory that
   contains `.claude/` or `plugins/`, not a bare subdirectory):
   ```
   agentscanner scan . --check AS-AGENT-005,AS-AGENT-006,AS-AGENT-007,AS-HOOK-004,AS-MCP-007,AS-PROMPT-002
   ```
3. **Read each finding**: `file:line`, the agent/hook/MCP-server it's on, and
   the severity — LOW/MEDIUM for `AS-AGENT-005` (missing vs. present-but-
   broken `maxTurns`), CRITICAL for `AS-AGENT-006` (unattended AND unbounded),
   HIGH for `AS-AGENT-007` (backgrounded AND unbounded), LOW for `AS-HOOK-004`/
   `AS-MCP-007` (missing timeout), MEDIUM for `AS-PROMPT-002` (anti-stopping
   language in the agent's own instructions).
4. **Fix**: set `maxTurns` to a positive integer sized to the agent's actual
   job — a narrowly-scoped agent (single review type, few skills) typically
   needs less headroom than a broad multi-skill coordinator; there's no
   universal number, size it to what the agent actually does and re-run the
   scan to confirm it's clean. Set an explicit `timeout` on any hook command
   or stdio MCP server the same way. For `AS-PROMPT-002`, remove the
   anti-stopping language and give the agent a concrete, checkable completion
   condition instead.
5. **Re-run scan** to confirm clean, then continue with a full
   `config-security-scan` pass before shipping if this was a new plugin
   agent — this skill only covers the unbounded-consumption slice, not
   permissions, secrets, or the rest of MCP config.

# Output

A short pass/fail per agent/hook/MCP-server: clean, or `file:line` +
missing/broken + the fix applied. Not a full report — for a complete
findings table use `config-security-scan`.

# Notes

- This is a subset of `config-security-scan`'s `AS-AGENT-*`/`AS-HOOK-*`/
  `AS-MCP-*`/`AS-PROMPT-*` categories, scoped to exactly the fields with no
  safe default (plus the compound cases that are worse than any one field
  alone). Reach for the full scan for permissions, secrets, and the rest of
  MCP/steering-file checks.
- Two related ideas are NOT checks here because they aren't statically
  checkable at all: a `maxBudgetUsd`-style frontmatter field (doesn't exist —
  budget capping is an Agent SDK `query()`-time option, never persisted to
  any file) and a repo-wide `settings.json` default for turns/spend (no such
  key exists at any settings scope — per-agent frontmatter is the only
  lever). See `agentscanner`'s `docs/checks.md` for the full rationale.
- `agentscanner` is static and read-only — it parses frontmatter as data,
  never executes hook commands, MCP servers, or the agent itself.
