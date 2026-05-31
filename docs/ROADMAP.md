# Roadmap

Legend: ✅ shipped · 🚧 in progress · ⬜ planned

The catalog in `.claude-plugin/marketplace.json` only lists plugins that actually exist (so installs never break). This file tracks the full vision.

## Core

| Plugin | Status |
| --- | --- |
| `security-diagramming` | ✅ |
| `security-reporting` | ✅ |
| `security-integrations` (Jira / Confluence / Google Drive) | ⬜ |
| `security-knowledge` (ATT&CK, OWASP, CWE, NIST reference packs) | ⬜ |

## Domain

| Plugin | Status |
| --- | --- |
| `threat-modeling` | ✅ |
| `web-app-security` | ✅ |
| `api-security` | ✅ |
| `mobile-security` | ✅ |
| `network-security` | ⬜ |
| `cloud-security` | ✅ |
| `k8s-security` | ✅ |
| `infrastructure-security` | ⬜ |
| `sast-sca` | ✅ |
| `osint` | ⬜ |
| `dfir` | ⬜ |
| `detection-engineering` | ⬜ |
| `threat-intelligence` | ⬜ |
| `vulnerability-management` | ⬜ |
| `supply-chain-security` | ⬜ |

## GenAI

| Plugin | Status |
| --- | --- |
| `llm-security` | ✅ |
| `rag-security` | ✅ |
| `agentic-ai-security` | ✅ |
| `multimodal-security` | ✅ |
| `mlops-security` | ⬜ |

## AI safety (distinct from GenAI security — see [TAXONOMY](TAXONOMY.md#ai-security-vs-ai-safety))

| Plugin | Status |
| --- | --- |
| `ai-safety` (domain) | ✅ |
| `ai-safety-engineer` (role) | ✅ |
| `responsible-ai-officer` (role — governance/GRC) | ✅ |
| `ai-safety-suite` (suite — pairs safety + GenAI security) | ✅ |

## Role

| Plugin | Status |
| --- | --- |
| `pentester` | ✅ |
| `red-team` | ⬜ |
| `security-analyst` | ⬜ |
| `security-engineer` | ⬜ |
| `security-architect` | ⬜ |
| `grc` | ⬜ |
| `blue-team` | ⬜ |
| `soc-siem` | ⬜ |
| `ciso-toolkit` (board decks, strategy, risk narratives) | ⬜ |
| `cto-security` (tech strategy, secure-by-design) | ⬜ |

## Bundles (roles + domain suites)

Bundles auto-install their members via `dependencies`. They're wired incrementally —
a bundle only depends on plugins that already exist. See [BUNDLES.md](BUNDLES.md)
for each bundle's intended members.

| Bundle | Kind | Status |
| --- | --- | --- |
| `pentester` | role | ✅ (deps: reporting, diagramming, threat-modeling) |
| `ai-safety-engineer` | role | ✅ (deps: ai-safety, reporting, diagramming) |
| `genai-suite` | domain suite | ✅ (deps: llm-security, rag-security, agentic-ai-security, multimodal-security) |
| `responsible-ai-officer` | role | ✅ (deps: ai-safety, reporting, diagramming) |
| `appsec-suite` | domain suite | ✅ (deps: web-app, api, mobile, sast-sca) |
| `ai-safety-suite` | suite | ✅ (deps: ai-safety, genai-suite) |
| `red-team` · `security-analyst` · `security-engineer` · `security-architect` | role | ⬜ |
| `grc` · `blue-team` · `soc-siem` · `ciso-toolkit` · `cto-security` | role | ⬜ |
| `cloud-suite` · `blueops-suite` | domain suite | ⬜ |

## Cross-cutting workstreams

- **Integrations**: Jira, Confluence, Google Drive (and later Slack, GitHub, ServiceNow) wired through MCP so every reporting/diagram skill can publish where teams already work.
- **Knowledge packs**: versioned reference data (frameworks, mappings) shared via `security-knowledge` so skills stay consistent and current.
- **Executive layer**: CISO/CTO decks, strategy planning, risk quantification — built on `security-reporting` + `security-diagramming`.

## How to claim work

Open an issue or PR referencing the plugin name. Use [templates/](../templates/) to scaffold, follow [AUTHORING.md](AUTHORING.md), then add the entry to `marketplace.json` in the same PR. Flip the box here from ⬜ to ✅.
