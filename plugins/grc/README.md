# grc

A **role bundle** for Governance, Risk & Compliance. Covers the three pillars:
**compliance** gap-assessments against the major frameworks (SOC 2, ISO 27001, PCI
DSS, HIPAA, GDPR, NIST CSF/800-53), **risk** assessment and the risk register
(ISO 27005 / NIST 800-30), and **governance** via policy management.

Thin orchestrator: it **auto-installs** `security-reporting` and
`security-diagramming`, and adds a GRC persona + a skill per pillar. It consumes the
operational plugins' evidence rather than running scans.

## Install

```
/plugin install grc@awesome-claude-security
```

## Command

| Command | What it runs |
| --- | --- |
| `/grc:assessment` | Framework gap-assessment → risk → policy gaps → remediation report. |

## Skills

| Skill | When it fires |
| --- | --- |
| `/grc:compliance-assessment` | Gap-assess against a compliance framework and build a remediation/audit-readiness plan. |
| `/grc:risk-assessment` | Run a security risk assessment and maintain a risk register (identify→analyze→evaluate→treat). |
| `/grc:policy-management` | Develop or review security policies, standards, and procedures. |

## Agents

| Agent | Use for |
| --- | --- |
| `grc-analyst` | Governance, risk, and compliance program work — frameworks, audits, risk register, policy. |

## How it relates to the other roles

- **`grc`** *(this)* — operational governance/risk/compliance: frameworks, audits,
  register, policy.
- **`ciso-toolkit`** — executive strategy and *cyber-risk quantification* (financial/
  board framing); consumes the GRC risk picture.
- **`responsible-ai-officer`** — the AI-specific governance counterpart (NIST AI RMF
  / EU AI Act).

> A `security-knowledge` reference pack (shared frameworks/control catalogs) is on
> the roadmap and will become a companion dependency when it ships.
