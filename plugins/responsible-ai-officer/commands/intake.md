---
description: Intake and risk-tier an AI use case, then produce the governance/oversight record (NIST AI RMF / EU AI Act / ISO 42001).
argument-hint: [AI use case / system to register]
---

Run AI governance intake for: **$ARGUMENTS**

Walk it, using installed skills (note any whose plugin is missing):

1. **Intake** — `/responsible-ai-officer:ai-use-case-intake` to capture purpose, data, users, autonomy, and context.
2. **Risk-tier** — classify against the relevant regime (EU AI Act risk tiers / NIST AI RMF / ISO 42001) and decide the oversight level required.
3. **Assess** — `/ai-safety:responsible-ai-assessment` to evaluate the use case against responsible-AI principles and surface obligations.
4. **Document & oversee** — produce the governance record: risk tier, required controls/evals, accountable owner, and review cadence. Reference `/security-knowledge:framework-mapping` to align obligations to frameworks.
5. **Report** — `/security-reporting:executive-summary` for the approval record; route higher-risk cases to `/ai-safety-engineer:safety-review`.

For deep execution, hand off to the `responsible-ai-officer` agent. Tier first — the risk tier sets how much scrutiny everything downstream needs. No high-risk use case ships without an owner and a review date.
