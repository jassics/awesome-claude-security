---
name: security-strategy
description: >-
  Build or assess a security program strategy and roadmap — current-vs-target
  maturity, gaps, prioritized initiatives aligned to business objectives and risk
  appetite, with outcomes, metrics, and budget framing. Use for security program
  planning, a strategy refresh, or a maturity assessment.
---

# Goal

A defensible security strategy: where the program is, where it needs to be (driven by
business risk, not fashion), and the prioritized, resourced roadmap to get there.

# Steps

1. **Business context** — objectives, regulatory drivers, crown-jewel assets, risk
   appetite, and constraints. Strategy serves the business, not the other way around.
2. **Assess current maturity** — against a recognized model (NIST CSF functions, or a
   CMMI-style tier per capability). Be honest about what's real vs. aspirational.
3. **Define target state** — the maturity warranted by the risk appetite and threat
   landscape (`threat-modeling`, threat intel) — not "max everything."
4. **Gap analysis** — current vs. target per capability; quantify the risk each gap
   leaves open (`cyber-risk-quantification`).
5. **Prioritize initiatives** — by risk reduction per unit cost/effort and business
   alignment; sequence quick wins and foundational work.
6. **Roadmap** — phased (e.g. now / next / later) with outcomes, owners, success
   metrics, and budget framing for each initiative.

# Output

A strategy document: business context · current vs. target maturity · gaps (with
risk) · prioritized initiative roadmap (phased, with outcomes/metrics/budget). Use
`security-reporting`; visualize the maturity and roadmap with `security-diagramming`.
Feed the headline into `board-deck`.

# Notes

Anchor everything to business risk and appetite — a strategy that maximizes controls
regardless of risk burns budget and credibility. Prioritize by risk-reduction-per-
dollar, and make the roadmap outcome- and metric-driven so progress is measurable.
