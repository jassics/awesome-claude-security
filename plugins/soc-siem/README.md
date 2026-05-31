# soc-siem

A **role bundle** for SOC / SIEM operations — the day-to-day monitoring and triage
function. Consistent **alert triage**, enrichment, scoping, and tiered escalation,
backed by the defensive stack.

Thin orchestrator: it **auto-installs** `blueops-suite` (detection, DFIR, intel) plus
core reporting, and adds a SOC-analyst persona + an alert-triage skill.

## Install

```
/plugin install soc-siem@awesome-claude-security
```

Auto-installs: `blueops-suite` (→ `detection-engineering`, `dfir`,
`threat-intelligence`), `security-reporting`.

## Skills

| Skill | When it fires |
| --- | --- |
| `/soc-siem:alert-triage` | Triage a SIEM/EDR alert end-to-end: validate, enrich, scope, and decide escalate vs. close. |

## Agents

| Agent | Use for |
| --- | --- |
| `soc-analyst` | Working an alert queue and running tiered SOC monitoring/triage. |

## Related roles

`blue-team` (broader threat-informed defense + purple teaming). SOC triage escalates
into `dfir:incident-response` and feeds detection tuning back to
`detection-engineering`.
