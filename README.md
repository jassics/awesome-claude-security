# awesome-claude-security

A **Claude Code plugin marketplace** of skills, agents, and tooling that turn Claude Code into a force multiplier across the full cybersecurity and GenAI-security lifecycle — from recon and threat modeling to detection engineering, GRC, and CISO-level strategy.

Everything installs **à la carte** — one repo, but you install only the plugins you want, never "the whole thing." Want only LLM red-teaming? Install `llm-security`. Only threat modeling? Install `threat-modeling`.

Prefer a ready-made stack? Install a **bundle** and it auto-pulls its parts: a **role bundle** like `pentester`, or a **domain suite** like `genai-suite`. Granular and bundled both come from the same catalog — see [docs/BUNDLES.md](docs/BUNDLES.md).

> Status: **early / actively building.** The marketplace, taxonomy, templates, and a first wave of plugins are in place. The [roadmap](docs/ROADMAP.md) tracks what's shipped vs. planned. Contributions welcome — see [CONTRIBUTING](CONTRIBUTING.md).

## Quick install

In any Claude Code session:

```
/plugin marketplace add jassics/awesome-claude-security
/plugin install llm-security@awesome-claude-security
```

Then invoke a skill, e.g. `/llm-security:owasp-llm-top10`, or just describe your task and let Claude pick the right skill/agent. Full instructions: [docs/INSTALL.md](docs/INSTALL.md).

## What's inside

Plugins are grouped into four buckets (see the full [taxonomy](docs/TAXONOMY.md)):

| Bucket | What it is | Examples |
| --- | --- | --- |
| **Core** | Cross-cutting capabilities every security task reuses | `security-diagramming`, `security-reporting`, integrations (Jira/Confluence/Drive) |
| **Domain** | Deep skillsets per security discipline | `threat-modeling`, web/mobile/cloud/k8s/network/infra security, SAST-SCA, OSINT, DFIR, detection engineering |
| **GenAI security** | Protecting AI/LLM systems from attackers | `llm-security`, RAG security, agentic-AI security, multimodal security |
| **AI safety** | Preventing AI systems from causing harm (a *distinct* discipline — [see why](docs/TAXONOMY.md#ai-security-vs-ai-safety)) | `ai-safety`, `ai-safety-engineer` |
| **Role** | Persona bundles that combine domains + workflow | `pentester`, `ai-safety-engineer`, security analyst, engineer, architect, GRC, blue team, SOC/SIEM, CISO/CTO |

### Shipped today (29 plugins)

**Core** — [`security-diagramming`](plugins/security-diagramming/) (attack trees, DFDs, architecture diagrams, mindmaps, infographics) · [`security-reporting`](plugins/security-reporting/) (findings, pentest reports, exec summaries, CVSS).

**Domain** — [`threat-modeling`](plugins/threat-modeling/) (STRIDE/PASTA) · [`web-app-security`](plugins/web-app-security/) (OWASP Web Top 10, access control, injection) · [`api-security`](plugins/api-security/) (OWASP API Top 10, BOLA/BFLA) · [`mobile-security`](plugins/mobile-security/) (MASVS/MASTG) · [`sast-sca`](plugins/sast-sca/) (static analysis + dependency/SBOM) · [`cloud-security`](plugins/cloud-security/) (AWS/Azure/GCP posture, IAM, misconfig) · [`k8s-security`](plugins/k8s-security/) (CIS/4Cs, RBAC, pod hardening) · [`infrastructure-security`](plugins/infrastructure-security/) (IaC review, host hardening, secrets) · [`detection-engineering`](plugins/detection-engineering/) (Sigma/YARA, ATT&CK coverage, threat hunting) · [`dfir`](plugins/dfir/) (incident response, forensic triage, IOCs) · [`threat-intelligence`](plugins/threat-intelligence/) (CTI lifecycle, IOC enrichment, actor profiling).

**GenAI security** — [`llm-security`](plugins/llm-security/) (OWASP LLM Top 10, prompt injection) · [`rag-security`](plugins/rag-security/) (retrieval poisoning, isolation) · [`agentic-ai-security`](plugins/agentic-ai-security/) (tool-permission audit, autonomy boundaries) · [`multimodal-security`](plugins/multimodal-security/) (cross-modal injection).

**AI safety** *(≠ security — [see why](docs/TAXONOMY.md#ai-security-vs-ai-safety))* — [`ai-safety`](plugins/ai-safety/) (harm modeling, safety evals, responsible red-team, bias/fairness, guardrails, RAI governance).

**Roles** *(auto-install their stack)* — [`pentester`](plugins/pentester/) · [`blue-team`](plugins/blue-team/) (threat-informed defense + purple teaming) · [`soc-siem`](plugins/soc-siem/) (alert triage, monitoring) · [`security-architect`](plugins/security-architect/) (secure-by-design, design review) · [`ai-safety-engineer`](plugins/ai-safety-engineer/) · [`responsible-ai-officer`](plugins/responsible-ai-officer/) (AI governance, EU AI Act risk-tiering).

**Suites** *(one-shot bundles)* — [`genai-suite`](plugins/genai-suite/) (all GenAI security) · [`appsec-suite`](plugins/appsec-suite/) (web+api+mobile+SAST/SCA) · [`cloud-suite`](plugins/cloud-suite/) (cloud+k8s+infrastructure) · [`blueops-suite`](plugins/blueops-suite/) (detection+dfir+threat-intel) · [`ai-safety-suite`](plugins/ai-safety-suite/) (safety + GenAI security together).

See [docs/ROADMAP.md](docs/ROADMAP.md) for the ~40 plugins and bundles planned across all buckets.

> **Security vs. safety:** the GenAI plugins protect AI systems from *attackers*; `ai-safety` prevents AI systems from *causing harm* even absent an attacker. They're complementary — most AI features need both.

## Built-in capabilities

Several features are designed to be shared across every plugin:

- **Diagrams & visuals** — Excalidraw diagrams, mindmaps, attack trees, and infographics via `security-diagramming`.
- **Reporting** — repeatable report generation via `security-reporting`, from a single finding to a board deck.
- **Integrations** — push findings, reports, and diagrams to Jira, Confluence, and Google Drive (roadmap: `security-integrations`, leveraging the matching MCP servers).

## Repository layout

```
.
├── .claude-plugin/marketplace.json   # the marketplace catalog
├── plugins/<plugin-name>/            # one installable plugin per directory
│   ├── .claude-plugin/plugin.json
│   ├── skills/<skill>/SKILL.md
│   ├── agents/<agent>.md
│   └── README.md
├── templates/                        # copy-to-start scaffolds for new plugins
└── docs/                             # taxonomy, roadmap, install, authoring guides
```

## Contributing

This is meant to be a community resource. New domains, roles, skills, and agents are very welcome — start from [templates/](templates/) and read [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/AUTHORING.md](docs/AUTHORING.md).

## Scope & ethics

These assets are for **authorized** security testing, defensive security, detection, GRC, education, and CTF use. Skills assume you have permission to test the systems involved. See [CONTRIBUTING.md](CONTRIBUTING.md#scope--ethics).

## License

[GPL-3.0](LICENSE).
