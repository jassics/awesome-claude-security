---
name: ai-use-case-intake
description: >-
  Intake a proposed AI use case and risk-classify it (EU AI Act tier / NIST AI RMF
  context), then gate it with the controls and documentation required before it can
  proceed. Use for AI governance intake, an AI use-case review board, or deciding
  what rigor a new AI project needs.
---

# Goal

A governance decision record for a proposed AI use case: its risk classification,
the obligations that follow, the required controls/evidence, and a clear
proceed / proceed-with-conditions / do-not-proceed outcome.

# Steps

1. **Capture the use case** — purpose, users and affected people, data used,
   autonomy/impact on decisions, deployment context, and vendor/build status.
2. **Classify risk:**
   - **EU AI Act tier** — unacceptable (prohibited) / high-risk / limited
     (transparency) / minimal. High-risk and prohibited categories drive most
     obligations; check whether the use case falls in a listed high-risk area.
   - **NIST AI RMF context** — characterize impact, stakeholders, and harm
     potential (reuse `ai-safety:harm-modeling`).
3. **Derive obligations** from the tier: required documentation (model/data cards,
   intended-use + limitations), human oversight, transparency/disclosure, data
   governance, testing/eval evidence, logging, and post-market monitoring.
4. **Map required controls to evidence** — which already exist vs. gaps. Pull from
   `ai-safety:safety-evaluation`, `bias-fairness-assessment`, `guardrail-review`,
   `responsible-ai-assessment`.
5. **Decide & record** — proceed / conditions / stop, with owner, conditions, and
   review date. Add to the AI inventory/register.

# Output

An intake decision record: use case · risk tier · obligations · required controls ·
evidence status · decision · conditions · owner · review date. Use
`security-reporting` for the record and an executive summary; this also feeds the
org's AI inventory.

# Notes

Classify the risk tier first — it sets how much rigor everything else needs, and it
catches prohibited uses before effort is spent. Keep the register current; intake
is the front door of the governance program, not a one-time form. Verify current EU
AI Act / NIST AI RMF text and any sector rules.
