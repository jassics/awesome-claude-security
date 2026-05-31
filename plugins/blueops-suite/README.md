# blueops-suite

A **domain suite** for blue-team / defensive operations: one-shot install of the
defensive stack. Manifest-only bundle — it owns no skills, just composes standalone
plugins you can also install individually.

## Install

```
/plugin install blueops-suite@awesome-claude-security
```

## Members

| Plugin | Covers |
| --- | --- |
| `detection-engineering` | Detection-as-code (Sigma/YARA/KQL), ATT&CK coverage, threat hunting. |
| `dfir` | Incident response (NIST 800-61/PICERL), forensic triage, IOC development. |
| `threat-intelligence` | CTI lifecycle, IOC enrichment, threat-actor profiling. |

## How they interlock

```
   dfir ──IOCs/TTPs──▶ threat-intelligence ──prioritized TTPs──▶ detection-engineering
     ▲                                                                    │
     └────────────────────── new detections / hunts ─────────────────────┘
```

Incidents produce indicators → intel enriches and attributes them → detection
engineering turns them into durable detections and hunts → which catch the next
incident earlier. All three map to **MITRE ATT&CK** as the common language.

## Note on scope

Domain suites bundle **domain** plugins only. The shared **core** plugins
(`security-diagramming`, `security-reporting`) stay standalone — install them
directly, or get them via a role bundle. See [docs/BUNDLES.md](../../docs/BUNDLES.md).
