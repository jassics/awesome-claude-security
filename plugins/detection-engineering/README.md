# detection-engineering

Detection-as-code for the blue team. Develop and tune **detection rules**
(Sigma, YARA, KQL/SPL/EQL) mapped to **MITRE ATT&CK**, assess **coverage** against
the ATT&CK matrix, and run **hypothesis-driven threat hunts**.

A **domain** plugin; member of [`blueops-suite`](../blueops-suite/). It turns the
IOCs/TTPs from `dfir` and `threat-intelligence` into durable detections.

## Install

```
/plugin install detection-engineering@awesome-claude-security
# or the whole defensive stack:
/plugin install blueops-suite@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/detection-engineering:detection-rule-development` | Write/review a detection rule (Sigma/YARA/KQL/SPL) mapped to ATT&CK, with FP tuning. |
| `/detection-engineering:detection-coverage-review` | Gap-assess detection coverage against MITRE ATT&CK. |
| `/detection-engineering:threat-hunting` | Run a hypothesis-driven threat hunt. |

## Pairs well with

`threat-intelligence` (TTPs to detect), `dfir` (incident-derived detections),
`security-reporting`, `security-diagramming`.
