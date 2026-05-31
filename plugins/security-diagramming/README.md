# security-diagramming

Visuals for security work. Generates **attack trees**, **threat-model data flow diagrams**, **architecture/trust-boundary diagrams**, **mindmaps**, and **infographics**. Renders with the **Excalidraw** MCP server when it's available; otherwise emits Excalidraw-importable JSON, Mermaid, and Graphviz/DOT you can paste into any tool.

This is a **core** plugin — other plugins (threat-modeling, pentester, reporting) lean on it instead of drawing their own diagrams.

## Install

```
/plugin install security-diagramming@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/security-diagramming:attack-tree` | You need an attack tree for a goal/asset (AND/OR decomposition). |
| `/security-diagramming:threat-model-dfd` | You need a data flow diagram with trust boundaries for threat modeling. |
| `/security-diagramming:architecture-diagram` | You need a security architecture / network / trust-boundary diagram. |
| `/security-diagramming:mindmap` | You need to map a topic (recon surface, framework, attack chain) as a mindmap. |
| `/security-diagramming:infographic` | You need a shareable infographic/one-pager (metrics, posture, summary). |

## Rendering

- **Excalidraw MCP present** → diagrams are created/exported directly.
- **No MCP** → you get `.excalidraw` JSON + a Mermaid block + (for graphs) DOT, plus instructions to import.
