# dfir

Digital forensics & incident response. Drive the **IR lifecycle** (NIST SP 800-61 /
SANS PICERL), perform **forensic triage** (disk/memory/log evidence with proper
handling and timelining), and **develop IOCs** that feed detection and intel.

A **domain** plugin; member of [`blueops-suite`](../blueops-suite/). Its incident
findings flow to `threat-intelligence` (enrich) and `detection-engineering` (detect).

## Install

```
/plugin install dfir@awesome-claude-security
# or the whole defensive stack:
/plugin install blueops-suite@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/dfir:incident-response` | Drive an incident through the IR lifecycle (triage → contain → eradicate → recover). |
| `/dfir:forensic-triage` | Collect and analyze evidence (disk/memory/logs) and build a timeline. |
| `/dfir:ioc-development` | Extract and operationalize IOCs/IOAs from an incident. |

## Pairs well with

`threat-intelligence` (enrich/attribute), `detection-engineering` (turn findings
into detections), `security-reporting` (incident report), `security-diagramming`.
