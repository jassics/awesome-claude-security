# red-team

A **role bundle** for adversary emulation. Runs **objectives-based**, full-scope
engagements that emulate a **real threat actor's TTPs** (mapped to MITRE ATT&CK) —
from recon through to objective/impact — to test detection and response under
realistic conditions, not just find vulnerabilities.

Thin orchestrator: it **auto-installs** the offensive + intel stack (`osint`,
`network-security`, `threat-intelligence`) plus core reporting/diagramming, and
adds a red-team operator persona + an adversary-emulation skill.

## Install

```
/plugin install red-team@awesome-claude-security
```

Auto-installs: `osint`, `network-security`, `threat-intelligence`,
`security-reporting`, `security-diagramming`.

## Command

| Command | What it runs |
| --- | --- |
| `/red-team:operation` | Objectives-based emulation: intel → ATT&CK TTPs → recon → emulate → report. |

## Skills

| Skill | When it fires |
| --- | --- |
| `/red-team:adversary-emulation` | Plan and run an objectives-based adversary-emulation engagement aligned to a threat actor. |

## Agents

| Agent | Use for |
| --- | --- |
| `red-team-operator` | Running a full-scope, objectives-based red-team engagement. |

## Red team vs. pentest

- **`pentester`** — find and demonstrate as many vulnerabilities as possible in scope
  (breadth, coverage).
- **`red-team`** *(this)* — emulate a specific adversary to achieve an objective and
  test the **blue team's** detection/response (depth, realism, stealth).

Best run collaboratively with `blue-team` as a **purple-team** exercise
(`blue-team:purple-team-exercise`).
