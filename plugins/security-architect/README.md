# security-architect

A **role bundle** for the security architect — the **design-and-review** persona.
Drives **secure-by-design**: architecture/design review, threat modeling, control
selection, trust-boundary analysis, and security requirements, balancing risk
reduction against usability and cost. Also covers **ASVS/SAMM maturity assessment**
and **pre-code security requirement injection** for PRDs and AI-assisted/"vibe
coded" feature work.

Thin orchestrator: it **auto-installs** `threat-modeling` + core diagramming/
reporting, and adds an architect persona + a design-review skill. Pair it with the
domain plugins for whatever you're reviewing (cloud, appsec, k8s, GenAI…).

## Install

```
/plugin install security-architect@awesome-claude-security
```

Auto-installs: `threat-modeling`, `security-diagramming`, `security-reporting`.

## Command

| Command | What it runs |
| --- | --- |
| `/security-architect:design-review` | Design review: threat-model → diagram → select controls → verdict. |

## Skills

| Skill | When it fires |
| --- | --- |
| `/security-architect:security-design-review` | Review a system/architecture design for security: trust boundaries, controls, secure-by-design, defense-in-depth. |
| `/security-architect:secure-architecture-maturity` | Assess ASVS verification level/gaps for a system and OWASP SAMM process maturity for the org producing it. |
| `/security-architect:prd-security-injection` | Inject concrete security requirements + acceptance checklist into a PRD/feature brief/AI-agent plan before code is written. |

## Agents

| Agent | Use for |
| --- | --- |
| `security-architect` | Designing or reviewing a system's security architecture end to end. |

## Recommended companions (install for the stack under review)

`cloud-suite` (cloud/k8s/infra designs) · `appsec-suite` (app designs) ·
`genai-suite` + `ai-safety` (AI systems). The architect composes whichever domains
the architecture touches.
