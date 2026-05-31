# blue-team

A **role bundle** for the defender. Drives **threat-informed defense** end to end —
detection engineering, incident response, threat hunting, and threat intelligence —
and validates it with **purple-team** exercises.

Thin orchestrator: it **auto-installs** the defensive stack (`blueops-suite`) plus
core reporting/diagramming, and adds a defender persona + a purple-team skill. Each
underlying plugin is also installable on its own.

## Install

```
/plugin install blue-team@awesome-claude-security
```

Auto-installs: `blueops-suite` (→ `detection-engineering`, `dfir`,
`threat-intelligence`), `security-reporting`, `security-diagramming`.

## Skills

| Skill | When it fires |
| --- | --- |
| `/blue-team:purple-team-exercise` | Plan and run a purple-team exercise: emulate ATT&CK techniques and validate detection + response. |

## Agents

| Agent | Use for |
| --- | --- |
| `blue-team-defender` | Coordinating defensive operations across detection, response, hunting, and intel. |

## Related roles

`soc-siem` (monitoring/triage operations), and the offensive `pentester` /
`red-team` (roadmap) on the other side of a purple-team exercise.
