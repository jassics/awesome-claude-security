---
name: attack-lookup
description: >-
  Look up MITRE ATT&CK tactics, techniques, and mitigations, and map an observed
  behavior, finding, or detection to the right technique ID(s). Use whenever work
  needs a consistent ATT&CK reference — detection coverage, threat reports, red-team
  TTP planning, or tagging a finding.
---

# Goal

Correct, consistent ATT&CK references — the right tactic + technique ID(s) for a
behavior — so detections, reports, and emulation across the team all speak the same
language.

# Steps

1. **Classify the behavior** by adversary goal → that's the **tactic** (the "why":
   Initial Access, Execution, Persistence, … Impact).
2. **Find the technique** under that tactic that matches the "how"; pick the
   sub-technique when one fits (e.g., T1059.001 PowerShell under T1059
   Command and Scripting Interpreter). See `reference.md` for the tactic list and
   common techniques.
3. **Map to mitigations/data sources** when relevant — what detects or prevents it
   (feeds `detection-engineering`).
4. **Cite precisely** — technique ID + name, and note the ATT&CK version/domain
   (Enterprise/Mobile/ICS). For anything beyond the common set, verify the current ID
   against attack.mitre.org rather than guessing — IDs and sub-technique structure
   change between versions.

# Output

The matched tactic(s) + technique ID(s) with names, optional mitigation/data-source
pointers, and a one-line rationale for the mapping. For coverage gap analysis use
`detection-engineering:detection-coverage-review`; for actor TTP sets use
`threat-intelligence`.

# Notes

ATT&CK is a living matrix — don't trust a memorized ID for an obscure technique;
confirm against the current version. Map to the most specific sub-technique that's
actually supported by evidence; over-precise tagging is as misleading as vague tagging.
See `reference.md` for the tactic taxonomy and frequently used techniques.
