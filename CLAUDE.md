# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

`awesome-claude-security` is a **Claude Code plugin marketplace**: a catalog of installable plugins (skills, agents, MCP integrations) covering the cybersecurity and GenAI-security lifecycle. The end goal is public distribution — users add the marketplace and install plugins à la carte. There is no application to "run"; the deliverables are the plugins themselves.

## Architecture

- **`.claude-plugin/marketplace.json`** — the catalog. Each plugin's `source` must be `./plugins/<name>` (a bare directory name fails schema validation with "source type your claude code version does not support" — the local-path source string must start with `./`). **Only list plugins that actually exist** here, or installs break. The full vision (including unbuilt plugins) lives in `docs/ROADMAP.md`, not the catalog.
- **`plugins/<name>/`** — one installable plugin per directory. Layout: `.claude-plugin/plugin.json` (manifest), `skills/<skill>/SKILL.md`, optional `agents/<agent>.md`, optional `.mcp.json`, and a `README.md`. Every component folder must be at the plugin **root**, never inside `.claude-plugin/`.
- **`templates/`** — copy-to-start scaffolds for new plugins/skills/agents.
- **`docs/`** — `TAXONOMY.md` (how plugins are bucketed: core / domain / genai / role), `ROADMAP.md` (shipped vs planned), `INSTALL.md`, `AUTHORING.md`.

The **taxonomy is the key mental model**: *core* plugins (diagramming, reporting, integrations) are cross-cutting; *domain* and *genai* plugins are deep skillsets; *role* plugins (pentester, analyst, CISO…) are thin bundles that compose the others rather than duplicating them. When adding capability, prefer composing existing core plugins over re-implementing diagrams/reports.

## Conventions (consistency matters across plugins)

- Plugin directory name == `plugin.json` `name` == marketplace entry `name` (kebab-case).
- Skills are single-responsibility. The SKILL.md `description` is the **trigger** — write it to tell Claude *when* to fire (situation + inputs + outcome), since it's always in context.
- Put long checklists/payload catalogs in a skill's sibling `reference.md` (loaded on demand) to keep always-on context small.
- Bump `plugin.json` `version` when you want installed users to get changes; otherwise the cache serves the old copy.
- Plugin agents may NOT declare `hooks`, `mcpServers`, or `permissionMode` (security restriction).

## Common commands

```bash
# Validate the whole marketplace's structural invariants (catalog<->dir parity,
# dependency existence, naming, skill/agent frontmatter). Pure stdlib, no deps.
# This is the CI gate (.github/workflows/validate.yml) — run it before committing.
python3 scripts/validate-marketplace.py

# Validate a single plugin manifest + component frontmatter against the schema
claude plugin validate ./plugins/<name> --strict

# Smoke-test locally
/plugin marketplace add /path/to/awesome-claude-security
/plugin install <name>@awesome-claude-security
```

Correctness is enforced by `scripts/validate-marketplace.py` (structural invariants, run in CI) plus `claude plugin validate --strict` (manifest schema) and manual smoke-testing.

## Scope

All content targets **authorized** security testing, defensive security, detection, GRC, research, education, and CTF. Frame skills around assessment, detection, hardening, and remediation. See `CONTRIBUTING.md` for the full ethics/scope policy.

## License

GPL-3.0 (`LICENSE`). New content inherits it; keep third-party material compatible.
