---
name: compliance-assessment
description: >-
  Gap-assess an organization or system against a compliance framework (SOC 2, ISO
  27001, PCI DSS, HIPAA, GDPR, NIST CSF/800-53), mapping controls to evidence,
  identifying gaps, and producing a prioritized remediation and audit-readiness plan.
  Use for compliance gap analysis, certification prep, or audit readiness.
---

# Goal

A clear picture of where the org stands against the chosen framework: which controls
are met, partial, or missing; the evidence for each; and a prioritized path to
compliant + audit-ready.

# Steps

1. **Scope & framework** — pick the framework(s) and define scope (systems, data,
   business units, the audit boundary). See `reference.md` for a per-framework map.
2. **Map controls** — enumerate the framework's controls/requirements; map each to
   the org's existing controls and the **evidence** that demonstrates it (policy,
   config, logs, tickets, attestations).
3. **Assess each control** — Met / Partial / Not met, with the evidence or the gap.
   Be honest; reuse outputs from the operational plugins as technical evidence
   (e.g. `cloud-security`, `sast-sca`, `detection-engineering`).
4. **Identify gaps & risk** — for each gap, the control intent, the exposure it
   leaves (link `risk-assessment`), and the effort to close.
5. **Prioritize remediation** — by risk and by audit deadline; assign owners and
   target dates.
6. **Audit readiness** — organize evidence, dry-run control testing, and a remediation
   tracker an auditor can follow.

# Output

A compliance gap analysis: control · requirement · status · evidence · gap · owner ·
priority · target date, plus a remediation roadmap and an evidence index. Use
`security-reporting`; visualize control coverage with `security-diagramming`.

# Notes

Compliance ≠ security, but done well it raises the floor — map controls to *real*
evidence, not aspirational policy. Many frameworks overlap heavily (ISO 27001, SOC 2,
NIST); assess once and map to several to avoid duplicate work. Verify the current
version of each framework. Track gaps with owners and dates — an audit is a deadline.
