---
name: alert-triage
description: >-
  Triage a SIEM/EDR alert end-to-end — validate it's real, enrich and scope it,
  reach a consistent verdict, and decide escalate vs. close with documented rationale.
  Use when working a SOC alert queue and you need a repeatable, defensible triage.
---

# Goal

A consistent, evidence-backed verdict on an alert — true positive / false positive /
benign-true-positive — with the right next action (escalate, close, tune) and a
record that the next analyst can follow.

# Steps

1. **Understand the alert** — what detection fired, the underlying logic, the ATT&CK
   technique, and why it triggered. Read the rule, don't guess.
2. **Validate** — is this real activity or a known false-positive pattern? Confirm
   against the source telemetry, not just the alert summary.
3. **Enrich** — add context: user/asset criticality, the involved IOCs
   (`threat-intelligence:ioc-enrichment`), process lineage, recent related alerts,
   and whether it matches known-good behavior.
4. **Scope** — pivot to see if it's isolated or part of a broader pattern (same host/
   user/campaign, lateral movement). Check for related alerts you should correlate.
5. **Decide & act:**
   - **Escalate** → `dfir:incident-response` for confirmed/likely incidents, with the
     evidence package and scope assembled.
   - **Close** → document why (benign/expected), preserving the rationale.
   - **Tune** → recurring false positive → feed back to
     `detection-engineering:detection-rule-development` (don't just mute).
6. **Record** — verdict, evidence, actions, and timestamps.

# Output

A triage record: alert · ATT&CK technique · verdict · evidence · scope · action
(escalate/close/tune) · rationale. Confirmed incidents → `dfir`; recurring FPs →
`detection-engineering`.

# Notes

Consistency is the goal — the same alert should get the same verdict regardless of
analyst. Always validate against source telemetry before deciding, and feed recurring
false positives back into detection tuning rather than muting them (muting hides the
problem and erodes coverage). Preserve evidence and rationale for every verdict.
