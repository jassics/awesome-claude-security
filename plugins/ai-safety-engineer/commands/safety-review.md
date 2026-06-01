---
description: Run an AI safety review for a feature/model — harms, evaluations, guardrails, and a documented safety case.
argument-hint: [AI feature / model / release to review]
---

Run an AI safety review for: **$ARGUMENTS**

Walk it, using installed skills (note any whose plugin is missing). This is **safety** (harm, bias, misuse), distinct from security:

1. **Harm modeling** — `/ai-safety:harm-modeling` to enumerate plausible harms, affected groups, and misuse paths.
2. **Evaluate** — `/ai-safety:safety-evaluation` and `/ai-safety:safety-red-team` to test for the modeled harms; `/ai-safety:bias-fairness-assessment` for disparate impact.
3. **Guardrails** — `/ai-safety:guardrail-review` to check the mitigations actually cover the evaluated risks.
4. **Safety case** — `/ai-safety-engineer:safety-case` to assemble the structured, evidence-backed argument that the system is acceptably safe to ship.
5. **Report** — `/security-reporting:executive-summary` for the go/no-go; `/security-diagramming:mindmap` for the harm/mitigation map.

For deep execution, hand off to the `ai-safety-engineer` agent. The safety case is the deliverable — claims must be backed by evaluation evidence, not assertions.
