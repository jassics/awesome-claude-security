---
name: responsible-ai-assessment
description: >-
  Gap-assess an AI system or program against a responsible-AI / governance
  framework — NIST AI RMF, ISO/IEC 42001, EU AI Act, OECD principles — covering
  governance, transparency, accountability, human oversight, documentation, and
  monitoring, then produce a prioritized roadmap. Use for AI governance, audit
  readiness, or compliance gap analysis.
---

# Goal

A governance gap analysis: where the system/program stands against the chosen
framework(s), the gaps, and a prioritized roadmap to close them.

# Steps

1. **Pick the framework(s)** for the context:
   - **NIST AI RMF** — lifecycle functions: Govern, Map, Measure, Manage.
   - **EU AI Act** — first classify the risk tier (unacceptable / high / limited /
     minimal); high-risk triggers specific obligations.
   - **ISO/IEC 42001** — AI management system controls (org governance).
   - **OECD principles** — values-level checkpoints.
   (See `harm-modeling/reference.md` for the framework map.)
2. **Assess each control/function**: governance & accountability (who owns AI risk),
   risk mapping (intended use, harms — reuse `harm-modeling`), measurement (evals,
   bias, monitoring — reuse `safety-evaluation`, `bias-fairness-assessment`),
   transparency (model/data cards, user disclosures), human oversight, data
   governance, incident response, and ongoing monitoring/drift.
3. **Score each** (e.g. absent / partial / met) with evidence.
4. **Prioritize the roadmap** by risk (and regulatory deadline, for EU AI Act
   high-risk), with owners.

# Output

A gap-analysis table: framework area · requirement · status · evidence · gap ·
priority · owner, plus a phased roadmap. Use `security-reporting` for the report
and an executive summary for leadership; this feeds a CISO/CTO or
`ai-safety-engineer` program view.

# Notes

Governance ties the technical safety work (harm modeling, evals, guardrails,
fairness) to organizational accountability and regulation. Start by classifying the
use case's risk tier — it determines how much rigor each control needs. Verify
current framework versions and any jurisdiction-specific obligations.
