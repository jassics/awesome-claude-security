---
description: Run a threat-informed defense cycle for a technique or threat — coverage check, hunt, detection, and purple-team validation.
argument-hint: [threat / ATT&CK technique / actor to defend against]
---

Run a threat-informed defense cycle for: **$ARGUMENTS**

Walk the cycle, using installed skills (note any whose plugin is missing):

1. **Scope the threat** — `/threat-intelligence:threat-actor-profiling` (or `/security-knowledge:attack-lookup`) to pin the relevant ATT&CK technique(s) and how the threat behaves.
2. **Assess coverage** — `/detection-engineering:detection-coverage-review` to find the gap: do we have telemetry and a detection for this?
3. **Hunt** — `/detection-engineering:threat-hunting` to check whether the activity is already present.
4. **Build the detection** — `/detection-engineering:detection-rule-development` for any gap, mapped to ATT&CK and FP-tuned.
5. **Validate** — `/blue-team:purple-team-exercise` to confirm the new detection actually fires against the emulated behavior.
6. **Report** — `/security-reporting:executive-summary` or a defense writeup; `/security-diagramming:mindmap` for the coverage picture.

For deep execution, hand off to the `blue-team-defender` agent. Close the loop: every gap found should end as a tested, deployed detection.
