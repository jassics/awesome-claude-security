# Installing & using

## Add the marketplace

From any Claude Code session:

```
/plugin marketplace add jassics/awesome-claude-security
```

This works because the catalog lives at `.claude-plugin/marketplace.json` in this Git repo. (You can also point at a local clone: `/plugin marketplace add /path/to/awesome-claude-security`.)

Refresh later with:

```
/plugin marketplace update awesome-claude-security
```

## Install plugins

Install only what you need:

```
/plugin install llm-security@awesome-claude-security
/plugin install threat-modeling@awesome-claude-security
/plugin install security-reporting@awesome-claude-security
```

Or browse interactively with `/plugin` and pick from the Discover tab.

### Single plugins vs. bundles

- A **single plugin** installs just that capability.
- A **bundle** (a role like `pentester`, or a domain suite like `genai-suite`)
  **auto-installs its dependencies**. The install output lists what else was added.

```
/plugin install pentester@awesome-claude-security    # pulls reporting, diagramming, threat-modeling
/plugin install genai-suite@awesome-claude-security  # pulls llm-security (+ more as they ship)
```

Remove the extras a bundle brought in (once you uninstall the bundle) with:

```
claude plugin prune
```

See [BUNDLES.md](BUNDLES.md) for how granular vs. bundled installs compare.

### Install scopes

| Scope | Flag | Use |
| --- | --- | --- |
| user (default) | `--scope user` | Available in all your projects. |
| project | `--scope project` | Checked into a repo's `.claude/settings.json`, shared with the team. |
| local | `--scope local` | Project-only, gitignored. |

```
/plugin install pentester@awesome-claude-security --scope project
```

## Using the plugins

Plugin skills are namespaced by plugin name:

```
/llm-security:owasp-llm-top10
/threat-modeling:stride
/security-diagramming:attack-tree
```

You usually don't need to call them explicitly — describe your task ("threat model this auth service", "write up this XSS finding") and Claude will invoke the relevant skill or agent automatically once the plugin is installed.

Agents appear in `/agents` and are auto-invoked when a task matches their description.

## Plugins that need MCP servers

Some plugins (diagramming, integrations) work best with an MCP server available:

- **`security-diagramming`** can render with the **Excalidraw** MCP server when present; otherwise it produces Excalidraw-importable JSON and Mermaid you can paste anywhere.
- **`security-integrations`** (roadmap) will use the **Jira**, **Confluence**, and **Google Drive** MCP servers to publish artifacts.

Configure MCP servers via `/mcp` or your `settings.json`. Skills degrade gracefully and tell you what's missing.

## Updating & removing

```
/plugin update llm-security@awesome-claude-security
/plugin uninstall llm-security@awesome-claude-security
```

## Troubleshooting

- `claude plugin validate ./plugins/<name>` checks a plugin's manifest and component frontmatter.
- Run `claude --debug` to see plugin load errors.
- Skills not appearing? Make sure `skills/` and `agents/` sit at the **plugin root**, not inside `.claude-plugin/`.
