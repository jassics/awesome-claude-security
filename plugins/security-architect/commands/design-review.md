---
description: Run a secure-by-design architecture review — threat model, trust boundaries, control selection, and a documented verdict.
argument-hint: [system / design doc / service to review]
---

Run a security design review for: **$ARGUMENTS**

Walk the review, using installed skills (note any whose plugin is missing):

1. **Understand the design** — `/security-architect:security-design-review` to map components, data flows, and trust boundaries.
2. **Model threats** — `/threat-modeling:stride` (or `/threat-modeling:pasta` for a richer process) against each trust boundary.
3. **Diagram** — `/security-diagramming:threat-model-dfd` and/or `/security-diagramming:architecture-diagram` to make the boundaries and threats explicit.
4. **Select controls** — map each significant threat to a control; `/threat-modeling:risk-rank` to prioritize; reference `/security-knowledge:framework-mapping` to align controls to NIST/ISO/CIS.
5. **Report** — a design-review verdict with required/recommended controls and residual risk; use `/security-reporting:executive-summary` for the leadership view.

For deep execution, hand off to the `security-architect` agent. Push fixes left into the design — a control chosen now is cheaper than a finding later.
