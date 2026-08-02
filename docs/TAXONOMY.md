# Taxonomy

How this marketplace is organized. The unit of installation is a **plugin**. Every plugin declares a `category` in the marketplace catalog so it shows up under the right bucket in `/plugin`. The four buckets are deliberately orthogonal: **roles** are bundles that lean on **domain** and **core** plugins rather than re-implementing them.

```
                 ┌──────────────────────────────────────────┐
   ROLE bundles  │ pentester · analyst · engineer · architect│
   (personas)    │ GRC · blue-team · SOC/SIEM · CISO · CTO    │
                 └───────────────┬──────────────────────────-┘
                                 │ compose
        ┌────────────────────────┼─────────────────────────┐
        ▼                        ▼                          ▼
 ┌─────────────┐        ┌─────────────────┐        ┌─────────────────┐
 │   DOMAIN    │        │     GENAI       │        │      CORE       │
 │ threat-model│        │ llm-security    │        │ diagramming     │
 │ web/mobile  │        │ rag-security    │        │ reporting       │
 │ cloud/k8s   │        │ agentic-ai-sec  │        │ integrations    │
 │ network/infra│       │ multimodal-sec  │        │ knowledge base  │
 │ sast-sca/dfir│       │ ...             │        │ ...             │
 └─────────────┘        └─────────────────┘        └─────────────────┘
```

## Core (cross-cutting capabilities)

Reused by every role and domain. Keep these self-contained and dependency-light.

| Plugin | Purpose |
| --- | --- |
| `security-diagramming` | Attack trees, DFDs, architecture diagrams, mindmaps, infographics (Excalidraw). |
| `security-reporting` | Findings, pentest reports, vuln writeups, executive summaries, CVSS scoring. |
| `security-integrations` | Push artifacts to Jira, Confluence, Google Drive (via their MCP servers). |
| `security-knowledge` | Shared reference packs: MITRE ATT&CK, OWASP Top 10 / LLM Top 10, CWE, NIST, STRIDE. |

## Domain (skillsets, in depth)

| Plugin | Covers |
| --- | --- |
| `threat-modeling` | STRIDE, PASTA, attack trees, DFDs, risk ranking. |
| `web-app-security` | OWASP Web Top 10, auth, injection, SSRF, access control. |
| `api-security` | OWASP API Top 10, authz, rate limiting, schema abuse. |
| `mobile-security` | OWASP MASVS/MASTG, Android/iOS, mobile threat modeling. |
| `network-security` | Recon, segmentation, firewall/IDS review, protocol attacks. |
| `cloud-security` | AWS/Azure/GCP posture, IAM, CSPM, misconfig review. |
| `k8s-security` | Kubernetes/CNCF, pod security, RBAC, supply chain. |
| `infrastructure-security` | IaC review, hardening, CIS benchmarks, secrets. |
| `sast-sca` | Static analysis + dependency/SCA scanning, SBOM, triage. |
| `secure-coding` | Python/React secure-coding enforcement: outdated/vulnerable function detection with safe alternatives, secret/credential blocking on commit+push (Claude Code hook + real git hooks), `.gitignore` hygiene. |
| `osint` | Footprinting, recon, exposure discovery, attribution. |
| `dfir` | Incident response, forensics, timeline, triage. |
| `detection-engineering` | Sigma/YARA rules, detection-as-code, threat hunting. |
| `threat-intelligence` | CTI lifecycle, IOC enrichment, ATT&CK mapping. |
| `vulnerability-management` | Prioritization, SLAs, remediation tracking. |
| `supply-chain-security` | SBOM, provenance, SLSA, dependency risk. |
| `claude-config-security` | Audit the Claude Code config itself (hooks, MCP, permissions, agents, skills, `CLAUDE.md`) via the `agentscanner` CLI. |

## GenAI security (AI/LLM **security**)

Protecting AI systems from **adversaries**. See "AI security vs AI safety" below —
these are a different discipline from the `ai-safety` bucket.

| Plugin | Covers |
| --- | --- |
| `llm-security` | OWASP LLM Top 10, prompt injection, jailbreaks, output handling. |
| `rag-security` | Retrieval poisoning, data exfiltration, context isolation. |
| `agentic-ai-security` | Tool abuse, autonomy/permission boundaries, agent threat modeling. |
| `multimodal-security` | Image/audio/document injection and adversarial inputs. |
| `mlops-security` | Model supply chain, training-data integrity, model registries. |

## AI safety (a distinct bucket — **not** security)

Preventing the AI system from **causing harm** to users, third parties, vulnerable
groups, and society — even with no attacker involved.

| Plugin | Covers |
| --- | --- |
| `ai-safety` | Harm modeling, safety evals, responsible red-teaming, bias/fairness, guardrails, responsible-AI governance (NIST AI RMF / ISO 42001 / EU AI Act). |
| `ai-safety-engineer` (role) | Operationalizing safeguards: evals-in-CI, guardrails, monitoring, safety cases, governance. |
| `mlops-security` *(shared)* | Overlaps both — model/data integrity matters for safety and security. |

### AI security vs AI safety

They are **different disciplines** and often different teams:

| | AI **security** (GenAI bucket) | AI **safety** (this bucket) |
| --- | --- | --- |
| Threat | An **attacker** compromises the system | The system **causes harm** with no attacker needed |
| Asks | How could it be exploited? | How could it hurt people/society? |
| Examples | Prompt injection, data poisoning, model theft | Harmful content, bias, hallucination, misuse, over-reliance |
| Frameworks | OWASP LLM Top 10, MITRE ATLAS | NIST AI RMF, EU AI Act, ISO/IEC 42001 |
| Method anchor | `threat-modeling` (STRIDE) | `ai-safety:harm-modeling` |

A secure model can still be unsafe, and a safe model can still be insecure — most
real AI features need **both**. Install `genai-suite` (security) and `ai-safety`
(safety) together for full coverage.

## Role (persona bundles)

Each role plugin ships a primary agent persona + a handful of role-specific skills, and is designed to be installed alongside the domain/core plugins it leans on.

| Plugin | Persona | Typically pairs with |
| --- | --- | --- |
| `pentester` | Offensive tester | `osint`, `web-app-security`, `network-security`, `security-reporting` |
| `red-team` | Adversary emulation | `threat-intelligence`, `detection-engineering` |
| `security-analyst` | Triage & investigation | `dfir`, `detection-engineering`, `threat-intelligence` |
| `security-engineer` | Build & harden | `sast-sca`, `cloud-security`, `k8s-security` |
| `security-architect` | Design & review | `threat-modeling`, `security-diagramming` |
| `grc` | Governance, risk, compliance | `security-reporting`, `security-knowledge` |
| `blue-team` | Defense & hardening | `detection-engineering`, `dfir` |
| `soc-siem` | Monitoring & response | `detection-engineering`, `dfir` |
| `ai-safety-engineer` | AI safety build & operate | `ai-safety`, `security-reporting`, `security-diagramming` |
| `responsible-ai-officer` | AI governance & risk-tiering | `ai-safety`, `security-reporting`, `security-diagramming` |
| `developer` | Secure-by-default coding companion | `security-knowledge`, `sast-sca`, `security-architect`, `infrastructure-security` |

## Executive (strategic tier)

Persona bundles for security leadership. Same bundle mechanics as roles, but
categorized `executive` in the catalog to mark the strategic altitude — they
synthesize the operational plugins' outputs into strategy, risk, and communication
rather than running tools.

| Plugin | Focus | Composes |
| --- | --- | --- |
| `ciso-toolkit` | Security strategy, cyber-risk quantification, board/exec decks | `security-reporting`, `security-diagramming`, `threat-modeling` |
| `cto-security` | Secure-by-design at scale, technology-risk decisions | `threat-modeling`, `security-diagramming`, `security-reporting` |

## Bundles vs. à-la-carte

Every capability is a **standalone plugin** — install just `threat-modeling` and
you get only that. On top of that, **bundle plugins** compose capabilities via the
`dependencies` field so one install pulls a whole stack:

- **Role bundles** (e.g. `pentester`) depend on the domains + shared core a role uses.
- **Domain suites** (e.g. `genai-suite`) depend on the plugins in one domain group.
- **Core stays shared** — diagramming/reporting/integrations are never bundled
  away; bundles pull them in as dependencies.

Full mechanics and the planned bundle list are in [BUNDLES.md](BUNDLES.md).

## Naming conventions

- Plugin names: kebab-case, descriptive, no `security-` prefix unless it disambiguates a cross-cutting/core capability.
- Skill names: verb-or-noun kebab-case that reads well after the namespace, e.g. `/llm-security:prompt-injection-test`.
- One responsibility per skill. Prefer several focused skills over one mega-skill.

See [ROADMAP.md](ROADMAP.md) for build order and [AUTHORING.md](AUTHORING.md) for how to add any of the above.
