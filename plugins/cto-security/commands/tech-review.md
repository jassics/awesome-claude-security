---
description: Assess technology/security risk for a strategic decision and frame the secure-by-design path.
argument-hint: [decision / technology / initiative to assess]
---

Run a CTO-level security review for: **$ARGUMENTS**

Walk it, using installed skills (note any whose plugin is missing):

1. **Tech-risk assessment** — `/cto-security:tech-risk-assessment` to weigh the security/technology risk of the decision (build vs. buy, new platform, architecture bet).
2. **Threat context** — `/threat-modeling:stride` at the system level to surface the structural risks the decision creates or removes.
3. **Secure-by-design path** — `/cto-security:secure-by-design-program` to frame the paved road / guardrails that make the secure way the easy way at scale.
4. **Communicate** — `/security-diagramming:architecture-diagram` for the target-state picture; `/security-reporting:executive-summary` for the recommendation and trade-offs.

For deep execution, hand off to the `cto-security-advisor` agent. Optimize for enablement at scale — guardrails and paved roads beat per-project gates. State the recommendation and its trade-offs plainly.
