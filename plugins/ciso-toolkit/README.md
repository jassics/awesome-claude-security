# ciso-toolkit

The **executive** toolkit for a CISO. Turns security work into business decisions:
**security strategy** and program roadmaps, **cyber-risk quantification** in
financial/business terms, and **board/executive decks**. The job is risk
communication and prioritization, not running scans.

Thin orchestrator: it **auto-installs** `security-reporting`, `security-diagramming`,
and `threat-modeling`, and adds a CISO persona + strategy/risk/board skills. It
consumes the *outputs* of the operational plugins rather than bundling them.

## Install

```
/plugin install ciso-toolkit@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/ciso-toolkit:security-strategy` | Build or assess a security program strategy and prioritized roadmap. |
| `/ciso-toolkit:cyber-risk-quantification` | Translate technical risk into business/financial terms and a risk register. |
| `/ciso-toolkit:board-deck` | Produce a board / executive security presentation. |

## Agents

| Agent | Use for |
| --- | --- |
| `ciso` | Security leadership: strategy, risk, program, and board communication. |

## Pairs well with

`cto-security` (the technology-strategy counterpart), every operational plugin (whose
results feed the risk picture), and `responsible-ai-officer` / `grc` for governance.
