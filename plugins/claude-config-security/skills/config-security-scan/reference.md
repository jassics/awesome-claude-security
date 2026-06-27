# agentscanner — invocation reference

`claude-config-security` is a thin Claude Code skill over **[agentscanner](https://pypi.org/project/agentscanner/)**,
a standalone, independently-versioned static scanner for Claude Code / AI-agent
configuration. This skill **invokes the published CLI** — it does not bundle, vendor,
or reimplement it, and it does not copy its check catalog. The catalog below is a
category summary; `agentscanner list-checks` is always the source of truth.

> **Safety invariant (from agentscanner's design):** the scanner *never executes what
> it parses*. It does not run hook commands, launch MCP servers, resolve
> `apiKeyHelper`/`statusLine` scripts, or fetch any URL — it reads untrusted config as
> data only.

## Getting the tool

```bash
uvx agentscanner --help          # zero-install, recommended
pipx install agentscanner        # isolated install
pip install agentscanner         # into the current environment
```

Python 3.9+. License: Apache-2.0 (the plugin is GPL-3.0; the coupling is runtime
invocation only, so the licenses do not mix).

## Common invocations

```bash
agentscanner scan .                       # scan this repo's .claude/, .mcp.json, CLAUDE.md
agentscanner scan . --include-user        # also scan ~/.claude (user scope)
agentscanner scan . --severity-threshold HIGH
agentscanner scan . --check AS-HOOK-001,AS-MCP-001   # run only specific checks
agentscanner scan . --skip-check AS-PERM-003          # skip a noisy check
agentscanner scan . --output json
agentscanner scan . --output sarif --output-file agentscanner.sarif   # GitHub code scanning
agentscanner scan . --fail-on HIGH        # CI gate: nonzero exit on HIGH+ findings
agentscanner scan . --soft-fail           # always exit 0 (report-only)
agentscanner list-checks                  # authoritative check catalog
agentscanner version
```

Every resource is tagged with its **scope** — project / local / user / managed /
plugin — so one run covers a repo, your global config, or both.

## Scanning a plugin or marketplace

This marketplace ships hooks-capable settings, `.mcp.json` files, agents, and skills —
exactly agentscanner's input surface.

> **Always scan from the repo / marketplace root.** The `PATH` argument is a *repo
> root*: agentscanner discovers artifacts at known path patterns relative to it
> (`.claude/`, `.mcp.json`, `CLAUDE.md`, and `plugins/*/{skills,agents}/…`). Pointing
> it at a bare plugin subdirectory (`agentscanner scan ./plugins/<name>`) finds the
> `plugins/` anchor missing and **silently scans 0 artifacts** — a false-negative
> trap. Scan the root; the run covers every plugin.

```bash
agentscanner scan .                        # the whole marketplace tree — covers all plugins
```

To focus on one plugin, scan the root and filter the output by path (e.g. JSON output
piped through a `location` filter, or `--check` for specific rules) — keep the scan
root at the directory that contains `plugins/`, not inside it.

## Check categories (summary — run `list-checks` for the live catalog)

| Prefix | Area | Examples of what it flags |
|---|---|---|
| `AS-HOOK-*` | Hooks | remote-code execution (`curl\|sh`), untrusted script paths, context-injecting hooks making network calls, missing `timeout` |
| `AS-PERM-*` | Permissions | `bypassPermissions`/`acceptEdits` as default, over-broad `Bash(*)`, unscoped dangerous commands |
| `AS-MCP-*` | MCP servers | plaintext secrets in `env`, cleartext `http://`, auto-trust-all project MCP, unpinned remote packages |
| `AS-ENV-*` | Endpoint/token | API base URL / auth token redirected away from Anthropic |
| `AS-SECRET-*` | Secrets | hardcoded API keys/tokens in config |
| `AS-AGENT-*` | Agents | over-privileged agent/skill (`tools: *` + bypass mode) |
| `AS-SKILL-*` | Skills | identity-file write access, social-engineering prerequisites, missing signatures, risk-tier spoofing, obfuscated payloads |
| `AS-PROMPT-*` | Steering files | prompt-injection / hidden-unicode indicators in `CLAUDE.md` / skills / agents |

## CI wiring

GitHub Actions (SARIF → code scanning):

```yaml
- run: pipx install agentscanner
- run: agentscanner scan . --output sarif --output-file agentscanner.sarif --soft-fail
- uses: github/codeql-action/upload-sarif@v3
  with: { sarif_file: agentscanner.sarif }
```

pre-commit:

```yaml
- repo: local
  hooks:
    - id: agentscanner
      name: agentscanner
      entry: agentscanner scan . --fail-on HIGH
      language: system
      pass_filenames: false
```

## Triage & suppression

- Confirm every finding at its cited `file:line` before reporting — the scanner is
  high-signal but static; intent and reachability are human calls.
- Suppress accepted findings with agentscanner's documented ignore/baseline
  mechanism rather than disabling a whole check globally.
- Route confirmed issues to `security-reporting:finding` for a consistent writeup.

## Links

- PyPI: https://pypi.org/project/agentscanner/
- Source & design (threat model, verified Claude Code semantics, hardened baseline):
  the `agentscanner` repository.
