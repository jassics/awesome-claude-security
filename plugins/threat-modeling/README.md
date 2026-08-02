# threat-modeling

Threat modeling in depth. Walk a system through **STRIDE** or **PASTA**, or a
multi-agent/agentic AI system through **MAESTRO**, build the **data flow
diagram**, enumerate threats per element/layer and trust boundary, rank them by
risk, and produce concrete, prioritized mitigations.

A **domain** plugin. It composes `security-diagramming` for DFDs/attack trees and
`security-reporting` for the writeup.

## Install

```
/plugin install threat-modeling@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/threat-modeling:stride` | Run a STRIDE threat model over a system/DFD. |
| `/threat-modeling:pasta` | Run the risk-centric 7-stage PASTA process. |
| `/threat-modeling:maestro` | Run CSA's MAESTRO layered threat model for multi-agent/agentic AI systems. |
| `/threat-modeling:risk-rank` | Rank enumerated threats and map them to mitigations. |

## The safety sibling

Threat modeling here is **attacker-centric** (how could an adversary compromise the
system?). For AI systems, its safety counterpart is `ai-safety:harm-modeling` —
*how could the system harm people even with no attacker?* They use a similar method
but a different lens; run both for AI features.

## Pairs well with

`security-diagramming` (`threat-model-dfd`, `attack-tree`), `security-reporting`,
[`ai-safety`](../ai-safety/) (harm-modeling), and any domain plugin for the system
under review (web, cloud, k8s, llm…).
