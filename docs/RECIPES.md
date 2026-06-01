# Recipes

End-to-end workflows that chain skills across plugins to get a real job done. Each
recipe lists what to install, the step-by-step skill chain, and what you end up with.
Where a **role bundle** exists, a single orchestration **command** runs the whole
flow — those are noted up top.

> All recipes assume **authorized** work. The role agents confirm scope/rules of
> engagement before acting. See [CONTRIBUTING](../CONTRIBUTING.md#scope--ethics).

Recipes:

1. [Web application penetration test](#1-web-application-penetration-test)
2. [Incident response — from alert to report](#2-incident-response--from-alert-to-report)
3. [Vulnerability triage from a scan export](#3-vulnerability-triage-from-a-scan-export)
4. [Security design review of a new service](#4-security-design-review-of-a-new-service)
5. [Secure a GenAI feature](#5-secure-a-genai-feature)
6. [Harden a software supply chain](#6-harden-a-software-supply-chain)
7. [Compliance gap assessment (GRC)](#7-compliance-gap-assessment-grc)

---

## 1. Web application penetration test

**One-shot:** `/pentester:engagement <target + rules of engagement>`

**Install:** `/plugin install pentester@awesome-claude-security` (auto-pulls `osint`,
`web-app-security`, `network-security`, `threat-modeling`, `security-reporting`,
`security-diagramming`). Add `vulnerability-management` and `security-integrations`
for prioritization and ticketing.

**Flow:**

1. `/pentester:recon` — confirm scope, pick methodology (PTES / OWASP WSTG).
2. `/osint:osint-footprinting` + `/osint:exposure-discovery` — map the external
   attack surface and exposed assets.
3. `/threat-modeling:stride` — a quick pass to decide where to spend test time.
4. `/web-app-security:owasp-web-top10`, then targeted
   `/web-app-security:access-control-test` and `/web-app-security:injection-test`.
5. `/vulnerability-management:vulnerability-prioritization` — rank findings by real
   risk (CVSS + EPSS + KEV + exposure), not raw severity.
6. `/security-reporting:pentest-report` + `/security-diagramming:attack-tree` — the
   deliverable and the kill-chain visual.
7. *(optional)* `/security-integrations:publish-finding-to-jira` — turn findings into
   tracked work.

**You get:** a methodology-backed pentest report with risk-ranked, evidence-backed
findings and a remediation path.

---

## 2. Incident response — from alert to report

**Install:** `/plugin install blue-team@awesome-claude-security` (auto-pulls the
`blueops-suite`: `detection-engineering`, `dfir`, `threat-intelligence` + reporting).
Add `soc-siem` / `security-analyst` for the front-line roles.

**Flow:**

1. `/soc-siem:triage <alert>` — validate the alert, separate true from false positive,
   decide whether to escalate.
2. `/security-analyst:investigate <case>` — correlate telemetry and set hypotheses.
3. `/threat-intelligence:ioc-enrichment` + `/threat-intelligence:threat-actor-profiling`
   — enrich indicators and attribute the activity.
4. `/dfir:forensic-triage` — reconstruct the timeline from evidence.
5. `/dfir:incident-response` — drive containment → eradication → recovery
   (NIST 800-61 / PICERL).
6. `/dfir:ioc-development` → `/detection-engineering:detection-rule-development` — turn
   what you learned into a durable, ATT&CK-mapped detection so it's caught next time.
7. `/security-reporting:executive-summary` — the incident writeup and lessons learned.

**You get:** a contained incident, a tested new detection, and a report — the IOCs and
TTPs from the case feed back into your detection library.

---

## 3. Vulnerability triage from a scan export

**Install:** `/plugin install vulnerability-management@awesome-claude-security`. Add
`threat-intelligence` (exploit context) and `security-integrations` (ticketing).

**Flow:**

1. `/vulnerability-management:vulnerability-scan-triage` — normalize and dedupe the
   Nessus/Qualys/Trivy export, cut false positives (backported patches!), attach asset
   context.
2. `/vulnerability-management:vulnerability-prioritization` — tier by CVSS + EPSS +
   CISA KEV + exposure. KEV and high-EPSS internet-facing items rise to the top
   regardless of raw CVSS.
3. `/vulnerability-management:remediation-tracking` — assign owners and SLAs, track the
   lifecycle, govern time-boxed exceptions.
4. `/security-integrations:publish-finding-to-jira` — push the prioritized items as
   deduped, well-formed issues.
5. `/security-reporting:executive-summary` — program metrics (SLA compliance, MTTR,
   aging, KEV exposure) for leadership.

**You get:** a noisy scan turned into a ranked, owned, tracked backlog — effort goes to
what's actually exploitable.

---

## 4. Security design review of a new service

**One-shot:** `/security-architect:design-review <system / design doc>`

**Install:** `/plugin install security-architect@awesome-claude-security` (auto-pulls
`threat-modeling`, `security-diagramming`, `security-reporting`). Add
`security-knowledge` for control framework mapping.

**Flow:**

1. `/security-architect:security-design-review` — map components, data flows, and trust
   boundaries from the design.
2. `/threat-modeling:stride` (or `/threat-modeling:pasta`) — enumerate threats per trust
   boundary.
3. `/security-diagramming:threat-model-dfd` + `/security-diagramming:architecture-diagram`
   — make boundaries and threats visible.
4. `/threat-modeling:risk-rank` — prioritize; map each significant threat to a control.
5. `/security-knowledge:framework-mapping` — align chosen controls to NIST/ISO/CIS for
   the audit/GRC audience.
6. `/security-reporting:executive-summary` — the verdict: required vs. recommended
   controls and residual risk.

**You get:** a design-review verdict that pushes fixes left into the design, with a
threat model, diagrams, and framework-mapped controls.

---

## 5. Secure a GenAI feature

**Install:** `/plugin install genai-suite@awesome-claude-security` (`llm-security`,
`rag-security`, `agentic-ai-security`, `multimodal-security`, `mlops-security`). Pair
with `ai-safety-suite` if you also need safety (harm/bias), which is distinct from
security.

**Flow:**

1. `/llm-security:ai-threat-model` — model the LLM/RAG/agent system and its trust
   boundaries.
2. `/llm-security:owasp-llm-top10` + `/llm-security:prompt-injection-test` — assess
   against the OWASP LLM Top 10 and test direct/indirect injection.
3. `/rag-security:rag-security-review` + `/rag-security:retrieval-poisoning-test` +
   `/rag-security:vector-store-isolation-test` — if it retrieves.
4. `/agentic-ai-security:tool-permission-audit` +
   `/agentic-ai-security:autonomy-boundary-test` — if it has tools/agency (excessive
   agency is LLM06).
5. `/mlops-security:ml-supply-chain-review` + `/mlops-security:model-serving-security`
   — the model itself: provenance, unsafe deserialization, and inference-endpoint
   hardening (extraction/inversion).
6. `/multimodal-security:multimodal-injection-test` — if it takes images/audio/docs.
7. `/security-reporting:finding` per issue.

**You get:** coverage of the GenAI stack from prompt to model to serving infra, mapped
to the OWASP LLM Top 10.

---

## 6. Harden a software supply chain

**Install:** `/plugin install supply-chain-security@awesome-claude-security`. Pair with
`sast-sca` (dependency-CVE scanning + SBOM) and `vulnerability-management`.

**Flow:**

1. `/sast-sca:sca-review` — generate/ingest the SBOM and find known-vulnerable deps.
2. `/supply-chain-security:dependency-supply-chain-review` — the trust layer:
   typosquatting, dependency confusion, maintainer/abandonment risk, install-script
   execution, pinning.
3. `/supply-chain-security:pipeline-integrity-review` — harden CI/CD against tampering
   (poisoned-pipeline execution, runner trust, secret exposure, mutable action/image
   tags) per OWASP CI/CD + SLSA build track.
4. `/supply-chain-security:artifact-provenance-verification` — establish signing
   (Sigstore/cosign) and SLSA provenance, and *enforce verification* at deploy.
5. `/vulnerability-management:remediation-tracking` — own and track the fixes.
6. `/security-reporting:finding` + `/security-diagramming:architecture-diagram` — the
   report and chain-of-custody view.

**You get:** a build chain where dependencies are trust-vetted, the pipeline resists
tampering, and only signed, attested artifacts reach production.

---

## 7. Compliance gap assessment (GRC)

**One-shot:** `/grc:assessment <framework + scope>`

**Install:** `/plugin install grc@awesome-claude-security` (auto-pulls
`security-reporting`, `security-diagramming`). Add `security-knowledge` for
cross-framework crosswalks.

**Flow:**

1. `/grc:compliance-assessment` — gap-assess against the framework (SOC 2 / ISO 27001 /
   PCI / HIPAA / GDPR / NIST), control by control.
2. `/security-knowledge:framework-mapping` — crosswalk each gap across CWE / NIST /
   CIS / ISO so one finding serves engineering, audit, and leadership.
3. `/grc:risk-assessment` — rank gaps by business risk; populate the risk register.
4. `/grc:policy-management` — close policy/documentation gaps the controls require.
5. `/security-reporting:executive-summary` + `/security-diagramming:infographic` — the
   gap report and a one-page posture snapshot for leadership.

**You get:** a framework gap report where every gap is tied to a business risk, an
owner, and a remediation path — not just a checklist.

---

## Compose your own

These are starting points, not rails. The pattern is always the same: **recon/scope →
deep domain skills → prioritize → report/publish**, with `security-knowledge` keeping
mappings consistent and `security-diagramming` / `security-reporting` /
`security-integrations` as the shared output layer. Mix the skills your job needs —
see the [taxonomy](TAXONOMY.md) and [bundles](BUNDLES.md).
