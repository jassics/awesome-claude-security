# cloud-security

Cloud security posture for **AWS, Azure, and GCP**. Review an environment's overall
**posture** (CSPM-style, CIS-anchored), audit **IAM** for least privilege and
privilege-escalation paths, and scan for the **misconfigurations** that cause most
cloud incidents (public storage, open ingress, unencrypted data, exposed metadata).

A **domain** plugin; member of the planned `cloud-suite`. Works on environments you
are authorized to assess.

## Install

```
/plugin install cloud-security@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/cloud-security:cloud-posture-review` | Comprehensive posture review across IAM, network, data, logging, and more. |
| `/cloud-security:cloud-iam-review` | Audit cloud IAM for over-permission, public/cross-account access, and escalation paths. |
| `/cloud-security:cloud-misconfig-scan` | Find high-impact misconfigurations and quick-win exposures. |

## Pairs well with

`k8s-security`, `infrastructure-security` (roadmap), `threat-modeling`,
`security-reporting`, `security-diagramming` (architecture/trust-boundary views).
