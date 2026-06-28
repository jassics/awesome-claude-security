# Getting started

A practical, shareable onboarding guide for **awesome-claude-security** — from
"never heard of it" to "installed a plugin and used it" in a few minutes. Hand this
to a teammate who's new to the marketplace.

- New to *installing*? Start here, then see [INSTALL.md](INSTALL.md) for the full reference.
- Want end-to-end workflows? See [RECIPES.md](RECIPES.md).
- Want to *build* a plugin? See [AUTHORING.md](AUTHORING.md) and [CONTRIBUTING.md](../CONTRIBUTING.md).

---

## What this is (in one sentence)

`awesome-claude-security` is a **Claude Code plugin marketplace** — a catalog of
installable plugins that teach Claude Code how to do real security work: pentesting,
threat modeling, detection engineering, DFIR, GRC, GenAI security, and CISO-level
strategy.

There is nothing to "run." You **add the marketplace once**, then **install only the
plugins you need**. Each plugin adds **skills** (namespaced slash commands like
`/llm-security:owasp-llm-top10`) and **agents** to your Claude Code session.

> A pentester knows which OWASP test bends a broken-access-control endpoint. An analyst
> knows which Sigma rule catches Kerberoasting. **Claude Code doesn't — until you install
> the plugin that teaches it.**

---

## The mental model (learn this first)

Plugins are grouped into buckets. Knowing the buckets is how you pick the right plugin —
or the right bundle that pulls several in at once.

| Bucket | What it gives you | Examples |
| --- | --- | --- |
| **Core** | Cross-cutting capabilities every task reuses | `security-diagramming`, `security-reporting`, `security-integrations`, `security-knowledge` |
| **Domain** | One deep skillset per discipline | `web-app-security`, `threat-modeling`, `cloud-security`, `dfir`, `detection-engineering` |
| **GenAI security** | Protecting AI/LLM systems *from attackers* | `llm-security`, `rag-security`, `agentic-ai-security`, `multimodal-security`, `mlops-security` |
| **AI safety** | Stopping AI systems *from causing harm* (a distinct discipline) | `ai-safety` |
| **Role / Executive** | Persona bundles that **auto-install** their whole stack | `pentester`, `blue-team`, `security-architect`, `ciso-toolkit` |
| **Suite** | One-shot domain bundles | `genai-suite`, `appsec-suite`, `cloud-suite`, `blueops-suite` |

**Why bundles matter:** a **role** like `pentester` or a **suite** like `genai-suite`
auto-installs its dependencies, so you get a working stack without assembling it by hand.
Granular and bundled installs both come from the same catalog — see [BUNDLES.md](BUNDLES.md).

---

## Five steps to using it

### 1. Add the marketplace (once)

In any Claude Code session:

```
/plugin marketplace add jassics/awesome-claude-security
```

This reads the catalog from `.claude-plugin/marketplace.json` in the repo. You can also
point at a local clone: `/plugin marketplace add /path/to/awesome-claude-security`.

### 2. Install only what you need

À la carte:

```
/plugin install llm-security@awesome-claude-security
/plugin install threat-modeling@awesome-claude-security
```

…or grab a whole stack with a bundle (the install output lists everything it pulled in):

```
/plugin install pentester@awesome-claude-security    # pulls osint, web, network, threat-modeling, reporting, diagramming
/plugin install genai-suite@awesome-claude-security  # pulls the full GenAI-security stack
```

Prefer to browse? Run `/plugin` and pick from the **Discover** tab.

**Install scope** (useful for teams):

| Scope | Flag | Use |
| --- | --- | --- |
| user (default) | `--scope user` | Available in all your projects |
| project | `--scope project` | Checked into the repo's `.claude/settings.json`, shared with teammates |
| local | `--scope local` | Project-only, gitignored |

### 3. Use it — two ways

1. **Just describe the task.** Once a plugin is installed, Claude auto-invokes the right
   skill or agent. *"Threat model this auth service"* → fires the threat-modeling skill.
   This is the recommended default.
2. **Call a skill explicitly.** Skills are namespaced by plugin:

   ```
   /llm-security:owasp-llm-top10
   /threat-modeling:stride
   /security-diagramming:attack-tree
   ```

Agents show up in `/agents` and fire automatically when a task matches their description.

### 4. Chain plugins into real workflows

[RECIPES.md](RECIPES.md) has full end-to-end flows. Where a role bundle exists, a single
command runs the whole thing. For example, a web pentest:

```
/pentester:engagement <target + rules of engagement>
```

…orchestrates recon → OSINT footprinting → a STRIDE pass → OWASP Web Top 10 +
access-control / injection testing → risk prioritization → a pentest report with an
attack-tree diagram. Other recipes cover incident response, vuln triage, security design
review, securing a GenAI feature, supply-chain hardening, and GRC gap assessments.

### 5. Maintain

```
/plugin marketplace update awesome-claude-security    # refresh the catalog
/plugin update llm-security@awesome-claude-security   # update one plugin
/plugin uninstall llm-security@awesome-claude-security
claude plugin prune                                   # remove deps a bundle pulled in
```

---

## Two things to know

- **MCP-dependent plugins degrade gracefully.** `security-diagramming` renders via the
  Excalidraw MCP server when present; otherwise it emits Excalidraw-importable JSON and
  Mermaid you can paste anywhere. `security-integrations` uses the Jira / Confluence /
  Google Drive MCP servers to publish artifacts. Configure MCP via `/mcp`; skills tell
  you what's missing.
- **Scope & ethics.** Everything targets **authorized** security testing, defensive
  security, detection, GRC, research, education, and CTF. Role agents confirm scope /
  rules of engagement before acting. See [CONTRIBUTING.md](../CONTRIBUTING.md#scope--ethics).

---

## Troubleshooting

- **Skills not appearing?** Make sure the plugin's `skills/` and `agents/` folders sit at
  the plugin **root**, not inside `.claude-plugin/`.
- `claude plugin validate ./plugins/<name>` checks a plugin's manifest and frontmatter.
- `claude --debug` surfaces plugin load errors.

---

## The 30-second version (hand this to anyone)

> 1. `/plugin marketplace add jassics/awesome-claude-security`
> 2. `/plugin install <plugin-or-bundle>@awesome-claude-security`
> 3. Describe your security task — Claude uses the installed skill/agent automatically
>    (or call `/<plugin>:<skill>` directly).
> 4. See [docs/RECIPES.md](RECIPES.md) for full chained workflows.
