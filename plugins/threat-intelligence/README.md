# threat-intelligence

Cyber threat intelligence (CTI). Run the **intelligence lifecycle** with structured
analytic techniques, **enrich and pivot** on IOCs (with confidence scoring), and
**profile threat actors / campaigns** against MITRE ATT&CK and the Diamond Model.

A **domain** plugin; member of [`blueops-suite`](../blueops-suite/). It enriches
`dfir` findings and tells `detection-engineering` which TTPs to prioritize.

## Install

```
/plugin install threat-intelligence@awesome-claude-security
# or the whole defensive stack:
/plugin install blueops-suite@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/threat-intelligence:cti-analysis` | Run the CTI lifecycle and produce an assessed intelligence product. |
| `/threat-intelligence:ioc-enrichment` | Enrich/pivot on IOCs and assess confidence and relevance. |
| `/threat-intelligence:threat-actor-profiling` | Profile an actor/campaign (TTPs, targeting, tooling) against ATT&CK. |

## Pairs well with

`dfir` (incident IOCs to enrich), `detection-engineering` (prioritize detections by
threat), `threat-modeling` (threat-informed design), `security-reporting`.
