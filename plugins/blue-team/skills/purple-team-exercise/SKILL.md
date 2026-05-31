---
name: purple-team-exercise
description: >-
  Plan and run a purple-team exercise: collaboratively emulate specific ATT&CK
  techniques and measure whether detection and response actually work, then close the
  gaps. Use to validate defensive coverage against real adversary behavior. Authorized
  environments only.
---

# Goal

Measured evidence of which adversary techniques your defenses detect and respond to —
and a prioritized set of fixes — produced collaboratively (red emulates, blue
observes) rather than as a pass/fail contest.

# Steps

1. **Scope & objectives** — pick techniques to test, driven by threat relevance
   (`threat-intelligence:threat-actor-profiling`) and known coverage gaps
   (`detection-engineering:detection-coverage-review`). Define success criteria.
2. **Plan emulation** — map each technique to a concrete, safe emulation (e.g. Atomic
   Red Team / a known procedure). Confirm authorization, scope, and a rollback plan;
   coordinate timing with the defenders.
3. **Execute collaboratively** — run each technique; record for each: was telemetry
   generated? did a detection fire? did an alert reach an analyst? was response timely
   and correct? Capture timestamps.
4. **Score** — per technique: Detected / Partially / Missed, plus prevention and
   response outcomes. Identify whether gaps are data-source, detection, or process.
5. **Remediate** — turn misses into detections (`detection-engineering:detection-rule-development`),
   data-source onboarding, or runbook fixes; re-test to confirm closure.

# Output

A results matrix: technique (ATT&CK) · emulation · telemetry? · detected? · responded?
· gap type · fix · retest status. Visualize as an ATT&CK heatmap
(`security-diagramming`) and report with `security-reporting`.

# Notes

Purple teaming is collaborative measurement, not a competition — the win is closed
gaps, not "red won." Keep emulations safe, authorized, and reversible. Re-test after
fixes; an untested fix isn't a closed gap.
