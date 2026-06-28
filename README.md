<div align="center">

<img src="assets/banner.png" alt="Awesome Claude Security — Claude Code Plugin Marketplace" width="100%">

# awesome-claude-security

**A Claude Code plugin marketplace for the full cybersecurity & GenAI-security lifecycle** — from recon and threat modeling to detection engineering, GRC, and CISO-level strategy.

[![Latest release](https://img.shields.io/github/v/release/jassics/awesome-claude-security?label=stable&color=2ea043)](https://github.com/jassics/awesome-claude-security/releases/latest)
[![Plugins](https://img.shields.io/badge/plugins-43-5ab0f5)](docs/ROADMAP.md)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-plugin%20marketplace-e8714d)](https://docs.anthropic.com/en/docs/claude-code)
[![License](https://img.shields.io/github/license/jassics/awesome-claude-security?color=blue)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)
[![Stars](https://img.shields.io/github/stars/jassics/awesome-claude-security?style=social)](https://github.com/jassics/awesome-claude-security/stargazers)

[Quick install](#quick-install) · [What's inside](#whats-inside) · [Taxonomy](docs/TAXONOMY.md) · [Roadmap](docs/ROADMAP.md) · [Recipes](docs/RECIPES.md) · [Contributing](CONTRIBUTING.md)

</div>

A pentester knows which OWASP test bends a broken-access-control endpoint. An analyst knows which Sigma rule catches Kerberoasting. A red-teamer knows which payload coaxes an LLM past its guardrails, and a CISO knows how to turn that finding into board-ready risk. **Your Claude Code doesn't — until you install the plugins that teach it.**

Everything installs **à la carte** — one repo, but you install only the plugins you want, never "the whole thing." Want only LLM red-teaming? Install `llm-security`. Only threat modeling? Install `threat-modeling`.

Prefer a ready-made stack? Install a **bundle** and it auto-pulls its parts: a **role bundle** like `pentester`, or a **domain suite** like `genai-suite`. Granular and bundled both come from the same catalog — see [docs/BUNDLES.md](docs/BUNDLES.md).

> **Stable: [`v1.0.0`](https://github.com/jassics/awesome-claude-security/releases/latest).** The marketplace, taxonomy, templates, and a full first wave of 43 plugins are shipped and installable — see the [roadmap](docs/ROADMAP.md) for what's next. This is a **community** project; it is not affiliated with or endorsed by Anthropic. Contributions welcome — see [CONTRIBUTING](CONTRIBUTING.md).

## Quick install

In any Claude Code session:

```
/plugin marketplace add jassics/awesome-claude-security
/plugin install llm-security@awesome-claude-security
```

Then invoke a skill, e.g. `/llm-security:owasp-llm-top10`, or just describe your task and let Claude pick the right skill/agent. Full instructions: [docs/INSTALL.md](docs/INSTALL.md).

**New here?** [docs/RECIPES.md](docs/RECIPES.md) shows end-to-end workflows — web pentest, incident response, vuln triage, design review, securing a GenAI feature — each chaining the right skills (and role bundles ship a one-shot command, e.g. `/pentester:engagement`).

## What's inside

Plugins are grouped into four buckets (see the full [taxonomy](docs/TAXONOMY.md)):

| Bucket | What it is | Examples |
| --- | --- | --- |
| **Core** | Cross-cutting capabilities every security task reuses | `security-diagramming`, `security-reporting`, integrations (Jira/Confluence/Drive) |
| **Domain** | Deep skillsets per security discipline | `threat-modeling`, web/mobile/cloud/k8s/network/infra security, SAST-SCA, OSINT, DFIR, detection engineering |
| **GenAI security** | Protecting AI/LLM systems from attackers | `llm-security`, RAG security, agentic-AI security, multimodal security |
| **AI safety** | Preventing AI systems from causing harm (a *distinct* discipline — [see why](docs/TAXONOMY.md#ai-security-vs-ai-safety)) | `ai-safety`, `ai-safety-engineer` |
| **Role** | Persona bundles that combine domains + workflow | `pentester`, `ai-safety-engineer`, security analyst, engineer, architect, GRC, blue team, SOC/SIEM, CISO/CTO |

### Shipped today (43 plugins)

**Core** — [`security-diagramming`](plugins/security-diagramming/) (attack trees, DFDs, architecture diagrams, mindmaps, infographics) · [`security-reporting`](plugins/security-reporting/) (findings, pentest reports, exec summaries, CVSS) · [`security-integrations`](plugins/security-integrations/) (publish to Jira/Confluence/Drive) · [`security-knowledge`](plugins/security-knowledge/) (ATT&CK / OWASP / framework reference packs).

**Domain** — [`threat-modeling`](plugins/threat-modeling/) (STRIDE/PASTA) · [`web-app-security`](plugins/web-app-security/) (OWASP Web Top 10, access control, injection) · [`api-security`](plugins/api-security/) (OWASP API Top 10, BOLA/BFLA) · [`mobile-security`](plugins/mobile-security/) (MASVS/MASTG) · [`sast-sca`](plugins/sast-sca/) (static analysis + dependency/SBOM) · [`network-security`](plugins/network-security/) (network pentest, segmentation, protocols) · [`osint`](plugins/osint/) (footprinting, exposure discovery, recon) · [`cloud-security`](plugins/cloud-security/) (AWS/Azure/GCP posture, IAM, misconfig) · [`k8s-security`](plugins/k8s-security/) (CIS/4Cs, RBAC, pod hardening) · [`infrastructure-security`](plugins/infrastructure-security/) (IaC review, host hardening, secrets) · [`detection-engineering`](plugins/detection-engineering/) (Sigma/YARA, ATT&CK coverage, threat hunting) · [`dfir`](plugins/dfir/) (incident response, forensic triage, IOCs) · [`threat-intelligence`](plugins/threat-intelligence/) (CTI lifecycle, IOC enrichment, actor profiling) · [`vulnerability-management`](plugins/vulnerability-management/) (triage, CVSS/EPSS/KEV prioritization, remediation SLAs) · [`supply-chain-security`](plugins/supply-chain-security/) (dependency trust, SLSA/Sigstore provenance, CI/CD integrity) · [`claude-config-security`](plugins/claude-config-security/) (audit the Claude Code config itself — hooks/MCP/permissions/skills — via the [`agentscanner`](https://pypi.org/project/agentscanner/) CLI).

**GenAI security** — [`llm-security`](plugins/llm-security/) (OWASP LLM Top 10, prompt injection) · [`rag-security`](plugins/rag-security/) (retrieval poisoning, isolation) · [`agentic-ai-security`](plugins/agentic-ai-security/) (tool-permission audit, autonomy boundaries) · [`multimodal-security`](plugins/multimodal-security/) (cross-modal injection) · [`mlops-security`](plugins/mlops-security/) (ML supply chain, pipeline security, model serving).

**AI safety** *(≠ security — [see why](docs/TAXONOMY.md#ai-security-vs-ai-safety))* — [`ai-safety`](plugins/ai-safety/) (harm modeling, safety evals, responsible red-team, bias/fairness, guardrails, RAI governance).

**Roles** *(auto-install their stack)* — [`pentester`](plugins/pentester/) · [`red-team`](plugins/red-team/) (adversary emulation, ATT&CK) · [`blue-team`](plugins/blue-team/) (threat-informed defense + purple teaming) · [`soc-siem`](plugins/soc-siem/) (alert triage, monitoring) · [`security-analyst`](plugins/security-analyst/) (investigation & analysis, T2/T3) · [`security-architect`](plugins/security-architect/) (secure-by-design, design review) · [`security-engineer`](plugins/security-engineer/) (DevSecOps, harden, secure pipelines) · [`ai-safety-engineer`](plugins/ai-safety-engineer/) · [`responsible-ai-officer`](plugins/responsible-ai-officer/) (AI governance, EU AI Act risk-tiering).

**Executive** *(strategic tier)* — [`ciso-toolkit`](plugins/ciso-toolkit/) (security strategy, cyber-risk quantification, board decks) · [`cto-security`](plugins/cto-security/) (secure-by-design at scale, tech-risk assessment).

**Suites** *(one-shot bundles)* — [`genai-suite`](plugins/genai-suite/) (all GenAI security) · [`appsec-suite`](plugins/appsec-suite/) (web+api+mobile+SAST/SCA) · [`cloud-suite`](plugins/cloud-suite/) (cloud+k8s+infrastructure) · [`blueops-suite`](plugins/blueops-suite/) (detection+dfir+threat-intel) · [`ai-safety-suite`](plugins/ai-safety-suite/) (safety + GenAI security together).

The [roadmap](docs/ROADMAP.md) is fully shipped — see it for how the buckets fit together and where the project goes next.

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
