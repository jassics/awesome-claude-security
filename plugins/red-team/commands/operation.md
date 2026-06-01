---
description: Run an objectives-based adversary-emulation operation aligned to real threat-actor TTPs, recon to impact.
argument-hint: [objective / threat actor to emulate + scope]
---

Plan and run an **authorized** red-team operation for: **$ARGUMENTS**

Confirm authorization, objective(s), and rules of engagement first — red-team work is objective-driven (e.g., "reach the crown-jewel data"), not vulnerability-coverage. If the objective or scope is unclear, ask.

Walk the operation, using installed skills (note any whose plugin is missing):

1. **Threat intel** — `/threat-intelligence:threat-actor-profiling` to pick a realistic actor and its TTPs.
2. **Map TTPs** — `/security-knowledge:attack-lookup` to translate the actor's behaviors into ATT&CK techniques to emulate.
3. **Recon** — `/osint:osint-footprinting` and `/osint:exposure-discovery` for the initial-access surface.
4. **Emulate** — `/red-team:adversary-emulation` to execute the chosen TTP chain (initial access → execution → persistence → priv-esc → lateral movement → impact), with `/network-security:network-pentest` for the network legs.
5. **Report** — `/security-reporting:pentest-report` for the operation narrative and `/security-diagramming:attack-tree` for the attack path; map findings to ATT&CK for the blue team.

For deep execution, hand off to the `red-team-operator` agent. Emulate adversary behavior to test detection & response — log what *should* have been caught for the purple-team debrief.
