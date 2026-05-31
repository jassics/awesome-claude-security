---
name: bias-fairness-assessment
description: >-
  Assess an AI model, feature, or dataset for bias and fairness across groups —
  representational and allocative harms, disparate performance, and skewed
  refusals — using appropriate fairness metrics, and recommend mitigations. Use
  when evaluating whether an AI system treats people equitably.
---

# Goal

A fairness assessment that identifies where the system performs or behaves
disparately across groups, quantifies it with suitable metrics, and proposes
mitigations — distinguishing the *type* of harm.

# Frame the harm type first

- **Allocative** — the system influences resource/opportunity decisions (hiring,
  lending, housing, moderation, healthcare). Fairness of *outcomes* matters most.
- **Representational** — the system depicts/describes groups (stereotyping,
  erasure, demeaning content, quality-of-service gaps). Fairness of *treatment*.

# Steps

1. **Identify groups and context** — protected/sensitive attributes relevant to the
   use case and jurisdiction; note intersectional groups. Define what "fair" means
   *here* (it's context-dependent and metrics can conflict).
2. **Choose metrics** to match the harm:
   - Allocative: demographic parity, equalized odds, equal opportunity, predictive
     parity, calibration — pick by which error is most harmful; they trade off.
   - Representational/generative: disparate refusal rate, sentiment/toxicity skew,
     stereotype rate, quality (accuracy/helpfulness) parity across groups.
3. **Measure** on a representative, consented dataset (watch for unrepresentative or
   skewed data — that's itself a finding). Report gaps with confidence.
4. **Diagnose sources** — data imbalance, label bias, proxy features, objective
   mismatch, feedback loops.
5. **Recommend mitigations** — data/representation fixes, reweighting/constraints,
   threshold adjustment, post-processing, human review, scope limits — and note
   residual disparity and metric trade-offs.

# Output

A fairness report: harm type · groups · metric · measured disparity · likely source
· mitigation · residual/trade-off. Use `security-reporting`; visualize gaps with
`security-diagramming:infographic`.

# Notes

There is no single "fair" — metrics conflict and the right choice depends on which
error harms people most in this context. State the chosen definition and why.
Beware proxies: removing a protected attribute doesn't remove bias carried by
correlated features.
