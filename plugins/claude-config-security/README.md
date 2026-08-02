# claude-config-security

Static security review of a **Claude Code / AI-agent configuration** — the
trust-bearing artifacts that steer the agent and run code on its behalf:
`settings.json`, permissions, hooks, MCP servers, agents/subagents, skills, slash
commands, and `CLAUDE.md`. *Checkov for your `.claude/` directory.*

A **domain** plugin. It drives **[agentscanner](https://pypi.org/project/agentscanner/)**,
a standalone, Apache-2.0, static, **read-only** scanner (it never executes what it
parses). The plugin invokes the published CLI — it does **not** bundle or
reimplement it — exactly the way `sast-sca` invokes Semgrep rather than embedding it.

## Install

```
/plugin install claude-config-security@awesome-claude-security
```

You also need the scanner on your `PATH` (zero-install option shown):

```
uvx agentscanner --help    # or: pipx install agentscanner / pip install agentscanner
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/claude-config-security:config-security-scan` | Audit a `.claude/` setup, `settings.json`, `.mcp.json`, a plugin/marketplace, or `CLAUDE.md` for misconfigurations — risky hooks, over-broad permissions, untrusted/cleartext MCP, secrets, endpoint redirection, over-privileged agents/skills, prompt-injection in steering files — then triage, remediate, and harden. |
| `/claude-config-security:agent-safety-lint` | Narrow, fast check for agents/hooks with no runaway-risk bound — a missing or invalid `maxTurns`, or a hook with no `timeout` — before shipping a subagent or plugin. Requires `agentscanner>=0.3.0`. |

## What it catches

Hooks (remote-code execution, unsafe paths, missing timeouts), permissions (bypass
modes, over-broad `Bash`, unscoped dangerous commands), MCP (plaintext secrets,
cleartext `http://`, auto-trust-all, unpinned packages), endpoint/token redirection,
hardcoded secrets, over-privileged agents/skills (incl. risk-tier spoofing, missing
signatures), and prompt-injection / hidden-unicode in steering files. Run
`agentscanner list-checks` for the authoritative catalog.

## Pairs well with

`security-reporting` (consistent findings + SARIF), `supply-chain-security` (dependency
provenance), `sast-sca` (your application source). Distinct from `agentic-ai-security`,
which secures agents you *build* — this secures the Claude Code **setup itself**.

## Related project

[`agentscanner`](https://pypi.org/project/agentscanner/) — the engine. Independently
versioned and licensed (Apache-2.0); this marketplace lists it as prior art /
related tooling and invokes it at runtime. See its repository for the threat model,
verified Claude Code semantics, and a hardened reference baseline.
