# Bundles & dependencies

This marketplace gives you **both** granular and bundled installs from one catalog.

- **Granular** — install any single plugin; you get only that plugin.
  `/plugin install threat-modeling@awesome-claude-security`
- **Bundled** — install a bundle plugin; Claude Code **auto-installs its
  dependencies** too. `/plugin install pentester@awesome-claude-security`

Both come from the same repo. The repo is a *catalog*, never a single mega-install.

## How bundling works

A bundle is a plugin whose `plugin.json` declares a `dependencies` array. Installing
it pulls those plugins automatically (same marketplace, no extra config). Disable
cascades; `claude plugin prune` removes auto-installed deps you no longer need.

```json
{
  "name": "pentester",
  "dependencies": ["security-reporting", "security-diagramming", "threat-modeling"]
}
```

Bare strings track whatever version the marketplace provides. To pin, use
`{ "name": "security-reporting", "version": "~0.1.0" }` and tag releases with
`claude plugin tag --push` (see [AUTHORING.md](AUTHORING.md#authoring-a-bundle)).

> **Golden rule:** only list dependencies that **exist in the catalog**. A
> dependency on a not-yet-built plugin makes the bundle fail to install. Add
> members to a bundle's `dependencies` as those plugins ship.

## Three kinds of plugin

| Kind | Owns components? | Declares deps? | Example |
| --- | --- | --- | --- |
| **Capability** (core / domain / genai) | Yes (skills/agents) | No | `llm-security`, `security-reporting` |
| **Role bundle** | Usually a thin agent + a skill or two | Yes — its domain **and** core stack | `pentester` |
| **Domain suite** | No (manifest only) | Yes — the domain plugins in that group | `genai-suite` |

**Core stays shared.** `security-diagramming`, `security-reporting`, and (roadmap)
`security-integrations` are always standalone capability plugins. Role bundles pull
them in as shared dependencies; domain suites do not absorb them.

## Planned bundles

Each bundle lists its **intended** members. Only the ✅ members are wired today
(the rest are added as they ship). Build order is tracked in [ROADMAP.md](ROADMAP.md).

### Role bundles (domains + shared core)

| Role bundle | Intended dependencies |
| --- | --- |
| `pentester` ✅ | `security-reporting` ✅, `security-diagramming` ✅, `threat-modeling` ✅, `osint` ⬜, `web-app-security` ⬜, `network-security` ⬜ |
| `ai-safety-engineer` ✅ | `ai-safety` ✅, `security-reporting` ✅, `security-diagramming` ✅ |
| `responsible-ai-officer` ✅ | `ai-safety` ✅, `security-reporting` ✅, `security-diagramming` ✅ |
| `red-team` | `osint`, `network-security`, `threat-intelligence`, `detection-engineering`, `security-reporting` |
| `security-analyst` | `dfir`, `detection-engineering`, `threat-intelligence`, `security-reporting` |
| `security-engineer` | `sast-sca`, `cloud-security`, `k8s-security`, `security-reporting` |
| `security-architect` | `threat-modeling`, `security-diagramming`, `cloud-security` |
| `grc` | `security-reporting`, `security-knowledge` |
| `blue-team` | `detection-engineering`, `dfir`, `security-reporting` |
| `soc-siem` | `detection-engineering`, `dfir`, `threat-intelligence` |
| `ciso-toolkit` | `security-reporting`, `security-diagramming`, `threat-modeling` |
| `cto-security` | `threat-modeling`, `security-diagramming`, `security-reporting` |

### Domain suites (domain plugins only)

| Suite | Intended dependencies |
| --- | --- |
| `genai-suite` ✅ | `llm-security` ✅, `rag-security` ✅, `agentic-ai-security` ✅, `multimodal-security` ✅, `mlops-security` ⬜ |
| `appsec-suite` ✅ | `web-app-security` ✅, `api-security` ✅, `mobile-security` ✅, `sast-sca` ✅ |
| `ai-safety-suite` ✅ | `ai-safety` ✅, `genai-suite` ✅ *(safety + GenAI security — a suite-of-suites)* |
| `cloud-suite` ✅ | `cloud-security` ✅, `k8s-security` ✅, `infrastructure-security` ✅ |
| `blueops-suite` | `detection-engineering`, `dfir`, `threat-intelligence` |

## Choosing granular vs bundled

Every **enabled** plugin adds a little always-on context (its skill/agent
descriptions). So:

- Want one capability, lightest footprint → install the single plugin.
- Want a whole role/domain workflow, convenience over footprint → install the
  bundle and let it pull the stack.

You can always start with a bundle and `claude plugin disable` the parts you don't
use, or start granular and add more later.
