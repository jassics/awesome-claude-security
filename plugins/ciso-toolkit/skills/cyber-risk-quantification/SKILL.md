---
name: cyber-risk-quantification
description: >-
  Translate technical security risk into business and financial terms — top risk
  scenarios, likelihood × impact, a risk register, and (where useful) quantified loss
  ranges (FAIR-aware) — to support executive decisions on treat/transfer/accept. Use
  to communicate or prioritize cyber risk for leadership.
---

# Goal

Cyber risk expressed the way executives make decisions: which scenarios matter, what
they could cost the business, how that compares to risk appetite, and what to do
(treat / transfer / accept).

# Steps

1. **Identify risk scenarios** — concrete, business-relevant loss events (e.g.
   "ransomware halts operations for N days", "breach of customer PII") rather than raw
   vulnerabilities. Derive from `threat-modeling`, findings, and threat intel.
2. **Estimate likelihood and impact** — qualitative (heat map: likelihood × impact)
   and, where the decision warrants, quantitative loss ranges (a FAIR-style estimate:
   frequency × magnitude, expressed as a range, not false precision).
3. **Compare to appetite** — plot residual risk against the org's stated risk
   appetite/tolerance; flag what exceeds it.
4. **Recommend treatment** — for each significant risk: mitigate (and the control +
   cost), transfer (insurance/contract), or accept (with owner and sign-off).
5. **Maintain the register** — owner, current vs. residual risk, treatment, status,
   review date; track trend over time.

# Output

A risk register + a heat map, plus quantified top risks (loss ranges) where relevant,
and treatment recommendations. Use `security-reporting`; visualize the heat map with
`security-diagramming:infographic`. Feeds `security-strategy` and `board-deck`.

# Notes

Quantify in ranges, not false precision — "likely $2–8M annual loss exposure" beats a
single fabricated number. Frame risks as business loss scenarios, not CVEs. Tie every
significant risk to an explicit treatment decision and an accountable owner; accepted
risk must be consciously accepted, not defaulted.
