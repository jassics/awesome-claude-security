---
description: Run a compliance gap-assessment for a framework, tie gaps to risk, and produce findings + remediation.
argument-hint: [framework + scope, e.g. "SOC 2 for the prod platform"]
---

Run a GRC assessment for: **$ARGUMENTS**

Walk the assessment, using installed skills (note any whose plugin is missing):

1. **Gap-assess** — `/grc:compliance-assessment` against the named framework (SOC 2 / ISO 27001 / PCI / HIPAA / GDPR / NIST), control by control.
2. **Map across frameworks** — `/security-knowledge:framework-mapping` to express each gap in CWE/NIST/CIS/ISO terms so one finding serves multiple audiences.
3. **Risk** — `/grc:risk-assessment` to rank gaps by risk and feed the register.
4. **Policy** — `/grc:policy-management` for any policy/documentation gaps the controls require.
5. **Report** — a gap report with prioritized remediation; `/security-reporting:executive-summary` for leadership; `/security-diagramming:infographic` for the posture snapshot.

For deep execution, hand off to the `grc-analyst` agent. Tie every control gap to a business risk and an owner — a gap list without risk and ownership doesn't drive action.
