---
name: risk-assessment
description: >-
  Run a structured security risk assessment and maintain a risk register —
  identify, analyze, evaluate, and treat risks (ISO 27005 / NIST SP 800-30) against
  the organization's risk criteria. Use for an enterprise/security risk assessment,
  risk register upkeep, or treatment decisions.
---

# Goal

A defensible risk register: the organization's security risks identified, analyzed
against consistent criteria, evaluated against risk appetite, and assigned explicit
treatment decisions with owners.

# Process (ISO 27005 / NIST 800-30)

1. **Establish context** — scope, assets in scope, the risk criteria (likelihood/
   impact scales) and the org's risk appetite/acceptance thresholds.
2. **Identify risks** — asset × threat × vulnerability scenarios (and the consequence).
   Draw on `threat-modeling`, findings, incidents (`dfir`), and threat intel.
3. **Analyze** — assign likelihood and impact per the defined scales; derive a risk
   level. Note existing controls and their effect (inherent vs. residual risk).
4. **Evaluate** — compare residual risk to the criteria/appetite; decide which risks
   require treatment and their priority.
5. **Treat** — choose per risk: **mitigate** (control + cost), **transfer**
   (insurance/contract), **avoid** (stop the activity), or **accept** (with owner and
   documented sign-off). Define the treatment plan.
6. **Register & monitor** — record in the risk register (ID, description, owner,
   inherent/residual level, treatment, status, review date); review on a cadence and
   on change.

# Output

A risk register + a risk heat map, with treatment plans and accountable owners. Use
`security-reporting`; visualize the heat map with `security-diagramming:infographic`.
Feeds `compliance-assessment` (risk-based controls) and the CISO view.

# Notes

Use consistent, documented criteria so risks are comparable and the register is
defensible. Distinguish **inherent vs. residual** risk (after controls). This is the
operational, register-based view; for financial/board framing of top risks use
`ciso-toolkit:cyber-risk-quantification`. Accepted risk must be explicitly owned and
signed off — never defaulted.
