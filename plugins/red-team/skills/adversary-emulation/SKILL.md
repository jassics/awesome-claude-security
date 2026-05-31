---
name: adversary-emulation
description: >-
  Plan and run an objectives-based adversary-emulation engagement: select a relevant
  threat actor, build an ATT&CK-mapped emulation plan across the attack lifecycle,
  execute within rules of engagement, and assess detection/response. Use for
  full-scope red-team work. Strictly authorized engagements only.
---

# Goal

A realistic, objectives-based engagement that emulates a chosen adversary's TTPs to
reach a defined objective — producing both offensive findings and an honest measure
of the blue team's detection and response.

# Prerequisites

- **Authorization, scope, objectives, and rules of engagement** agreed in writing:
  permitted techniques, off-limits systems/data, deconfliction contacts, and the
  win condition (the "flag"/objective). Stay within them at all times.

# Steps

1. **Select the adversary & objective** — pick a threat actor relevant to the org
   (`threat-intelligence:threat-actor-profiling`) and define the objective (e.g.
   "access crown-jewel data X"). Realism comes from emulating a real actor's TTPs.
2. **Build the emulation plan** — map the engagement across the attack lifecycle
   (recon → initial access → execution → persistence → privilege escalation →
   defense evasion → credential access → discovery → lateral movement → collection →
   C2 → exfiltration/impact), choosing ATT&CK techniques the actor actually uses.
3. **Recon** — `osint` (footprinting, exposure, people) to find a realistic entry.
4. **Execute within RoE** — work the plan; on network use `network-security`. Operate
   with appropriate stealth where authorized, but never outside scope and never
   destructively. Log every action with timestamps for deconfliction.
5. **Track detection** — record, per technique, whether it generated telemetry, fired
   a detection, and prompted response (this is the core value vs. a pentest).
6. **Assess & debrief** — did you reach the objective? Which TTPs were detected vs.
   missed? Where are the gaps?

# Output

An engagement report: objective & outcome · adversary emulated · ATT&CK technique
timeline (executed vs. detected vs. responded) · attack path
(`security-diagramming:attack-tree`) · findings · detection/response gaps ·
recommendations. Use `security-reporting`. Feed gaps to `detection-engineering` and
run a `blue-team:purple-team-exercise` to close them.

# Notes

Red teaming measures **outcomes and detection**, not vulnerability count — the
deliverable is "could a realistic adversary achieve X, and would we have caught
them?" Stay rigorously within RoE: authorized, non-destructive, deconflicted, and
logged. The highest value is collaborative (purple) — emulate, measure, then help
the defenders close the gaps.
