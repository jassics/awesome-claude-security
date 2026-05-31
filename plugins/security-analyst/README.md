# security-analyst

A **role bundle** for the security analyst — the **investigation and analysis**
persona (T2/T3). Takes leads, escalations, and complex cases and drives them to an
evidence-backed conclusion: correlate telemetry across sources, enrich with intel,
reconstruct timelines, scope impact, and produce an analytical assessment.

Thin orchestrator: it **auto-installs** the defensive stack (`blueops-suite`) plus
core reporting/diagramming, and adds an analyst persona + an investigation skill.

## Install

```
/plugin install security-analyst@awesome-claude-security
```

Auto-installs: `blueops-suite` (→ `detection-engineering`, `dfir`,
`threat-intelligence`), `security-reporting`, `security-diagramming`.

## Skills

| Skill | When it fires |
| --- | --- |
| `/security-analyst:security-investigation` | Drive an investigation from a lead to an evidence-backed conclusion (correlate, enrich, timeline, scope, assess). |

## Agents

| Agent | Use for |
| --- | --- |
| `security-analyst` | Conducting a security investigation or analytical deep-dive across telemetry and intel. |

## How it relates to the other defensive roles

- **`soc-siem`** — fast, repeatable **alert-queue triage** (T1/T2). Escalates here.
- **`security-analyst`** *(this)* — **deeper investigation/analysis** of escalated or
  complex cases; hands confirmed incidents to IR.
- **`blue-team`** — broad **threat-informed defense** and purple-team validation.

Confirmed incidents escalate to `dfir:incident-response`; findings feed
`detection-engineering`.
