---
name: tech-risk-assessment
description: >-
  Assess the security risk of a technology or product decision for leadership — new
  technology/vendor adoption, build-vs-buy, third-party/supply-chain, or M&A
  technical due diligence — and give a clear recommendation with trade-offs. Use to
  inform a strategic technology decision.
---

# Goal

A decision-ready security risk assessment of the option(s) under consideration, with
a recommendation that weighs security against velocity, cost, and strategic fit.

# Steps

1. **Frame the decision** — what's being decided (adopt X / build vs. buy / acquire Y),
   the options, the data/systems involved, and the decision criteria.
2. **Assess each option's security posture:**
   - **Build** — can we build and operate it securely? cost of doing so, our maturity.
   - **Buy / adopt** — vendor security posture, certifications/attestations, data
     handling and residency, integration and access scope, lock-in, and exit.
   - **Third-party / supply-chain risk** — dependencies, provenance, and the blast
     radius if the vendor/component is compromised.
   - **M&A due diligence** — target's security posture, debt, incident history,
     compliance exposure, and integration risk.
3. **Assess integration & data risk** — trust boundaries created, data exposure,
   identity/access, and the new attack surface (`threat-modeling`).
4. **Total cost incl. security** — build/operate/secure cost over time, not just
   license/sticker.
5. **Recommend** — a clear call with the risk trade-offs, required conditions/
   mitigations, and residual risk stated honestly.

# Output

A tech-risk assessment: decision · options · per-option security posture · third-
party/integration/data risk · total cost incl. security · recommendation + conditions
+ residual risk. Use `security-reporting`; diagram integration/trust boundaries with
`security-diagramming`.

# Notes

Decide with explicit trade-offs, not security absolutism — the goal is the best
risk-adjusted technology choice for the business. Weight third-party/supply-chain and
exit/lock-in risk; they're routinely underestimated. State residual risk and the
conditions under which the recommendation holds.
