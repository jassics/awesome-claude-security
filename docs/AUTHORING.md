# Authoring guide

How to add a plugin, skill, or agent to this marketplace. Read [TAXONOMY.md](TAXONOMY.md) first to decide where your work belongs.

## Anatomy of a plugin

```
plugins/<plugin-name>/
├── .claude-plugin/
│   └── plugin.json        # manifest (name required; rest optional)
├── README.md              # what it does, skills/agents list, install line
├── skills/
│   └── <skill-name>/
│       ├── SKILL.md       # required: frontmatter + instructions
│       └── reference.md   # optional: deeper knowledge loaded on demand
├── agents/
│   └── <agent-name>.md    # optional: subagent persona
└── .mcp.json              # optional: MCP servers this plugin needs
```

> Only `plugin.json` goes inside `.claude-plugin/`. Every other folder (`skills/`, `agents/`, `commands/`, `hooks/`) must be at the plugin **root**, or it won't load.

Scaffold from [`templates/plugin-template/`](../templates/plugin-template/) — copy it to `plugins/<your-plugin>/` and edit.

## `plugin.json`

```json
{
  "name": "web-app-security",
  "description": "OWASP Web Top 10 testing, auth and access-control review.",
  "version": "0.1.0",
  "author": { "name": "Your Name" },
  "license": "GPL-3.0",
  "keywords": ["web", "owasp", "appsec"]
}
```

`name` is the only required field. Keep `name` identical to the directory name and the marketplace entry. Bump `version` when you want existing users to receive changes (otherwise the cache keeps the old copy).

## Writing a SKILL.md

A skill is a focused, invocable capability. Frontmatter + a markdown body of instructions Claude follows when the skill fires.

```markdown
---
name: prompt-injection-test
description: Test an LLM feature for direct and indirect prompt injection using a structured payload set. Use when assessing an LLM-backed app, chatbot, or agent for input-handling weaknesses.
---

# Goal
...what "done" looks like...

# Steps
1. ...
2. ...

# Output
...the artifact/format to produce...
```

Guidelines:

- **`description` is the trigger.** Write it so Claude knows *when* to use the skill — name the situation, inputs, and outcome. This text is always in context, so be specific but concise.
- **One responsibility per skill.** Prefer `owasp-llm-top10` + `prompt-injection-test` over one giant `llm-audit`.
- **Be procedural.** Give numbered steps, a methodology, and the exact output format. Reference frameworks by name (OWASP LLM Top 10, STRIDE, MASTG).
- **Stay authorized & defensive.** Assume permission exists; focus on assessment, detection, and remediation rather than weaponization. See [CONTRIBUTING.md](../CONTRIBUTING.md#scope--ethics).
- **Put depth in `reference.md`.** Long checklists, payload catalogs, and rubrics go in a sibling file the skill tells Claude to read on demand — keeps always-on context small.
- **Compose, don't duplicate.** If you need a diagram or report, defer to `security-diagramming` / `security-reporting` rather than re-implementing.

## Writing an agent

Agents are personas Claude can delegate multi-step work to. Frontmatter supported by plugin agents: `name`, `description`, `model`, `effort`, `maxTurns`, `tools`, `disallowedTools`, `skills`, `memory`, `background`, `isolation`. (`hooks`, `mcpServers`, and `permissionMode` are not allowed in plugin agents.)

```markdown
---
name: llm-security-reviewer
description: Reviews LLM/GenAI features for security weaknesses end-to-end. Use for a full assessment rather than a single check.
model: sonnet
effort: high
---

You are a senior AI security reviewer. ...
```

## Authoring a bundle (role or domain suite)

A bundle is a plugin that composes others via `dependencies`. Role bundles usually
ship a thin agent + a skill or two; domain suites are manifest-only (no components).

```json
{
  "name": "genai-suite",
  "description": "One-shot install of the GenAI / AI-security plugins.",
  "version": "0.1.0",
  "license": "GPL-3.0",
  "dependencies": ["llm-security"]
}
```

Rules:

- **Only depend on plugins that exist in this marketplace.** A dependency on a
  not-yet-built plugin makes the bundle fail to install. Add members to
  `dependencies` as those plugins ship.
- Bare strings (`"llm-security"`) track the latest version. To pin, use
  `{ "name": "llm-security", "version": "~0.1.0" }` and tag releases:
  `claude plugin tag --push` (tags as `genai-suite--v0.1.0`).
- Role bundles depend on the **domains they use + shared core**; domain suites
  depend on **domain plugins only** (core stays shared — see [BUNDLES.md](BUNDLES.md)).
- Register the bundle in `marketplace.json` with `category` `role` or `suite`.

## Add it to the marketplace

In `.claude-plugin/marketplace.json`, append an entry to `plugins`:

```json
{
  "name": "web-app-security",
  "source": "web-app-security",
  "description": "...",
  "category": "domain",
  "keywords": ["web", "owasp"],
  "license": "GPL-3.0"
}
```

`source` is relative to `metadata.pluginRoot` (`./plugins`), so it's just the directory name.

Once your entry is in `marketplace.json`, the [docs-site plugin catalog](https://jassics.github.io/awesome-claude-security/catalog/) picks it up automatically — that page is generated from `marketplace.json` at build time (`scripts/gen_pages.py`), so there's no separate list to update.

## Docs site (optional, local preview)

The public docs site is [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) built from `docs/` and deployed by `.github/workflows/pages.yml`. To preview locally:

```bash
pip install -r requirements-docs.txt
mkdocs serve            # http://127.0.0.1:8000
mkdocs build --strict   # what CI runs; fails on broken links/anchors
```

You only need this when changing site structure or docs content — editing plugins never requires touching it.

## Validate

```bash
claude plugin validate ./plugins/web-app-security --strict
```

Then add it locally and smoke-test:

```
/plugin marketplace add /path/to/awesome-claude-security
/plugin install web-app-security@awesome-claude-security
```

## Checklist before PR

- [ ] Directory name = `plugin.json` name = marketplace entry name.
- [ ] `claude plugin validate --strict` passes.
- [ ] Each skill has a trigger-worthy `description` and a concrete output.
- [ ] README lists every skill/agent and the install line.
- [ ] Roadmap box flipped to ✅.
- [ ] Content is authorized/defensive in framing.
