---
name: cvss
description: >-
  Score a vulnerability with CVSS v4.0: derive the metric vector (Base, plus
  Threat/Environmental refinement where context supports it), compute the
  exact score via the official algorithm, and explain each metric choice.
  Use whenever a finding needs a defensible severity rather than a guess.
---

# Goal

A defensible CVSS 4.0 score: the full vector string, numeric score, severity
band, and a one-line justification per metric — computed exactly, not
eyeballed or hand-calculated.

# Why not compute it by hand

CVSS 3.1's base score was a closed-form arithmetic formula reasoning could
walk through step by step. CVSS 4.0 is not: it maps the vector to one of 270
"MacroVectors" (via 6 equivalence classes) and looks up/interpolates a score
from a table defined in the official specification. Reproducing that table
from memory is exactly the kind of thing that looks plausible and is quietly
wrong. Reason through *which metric values apply* from the evidence (that
part is still judgment), then get the actual number from
`scripts/cvss4-score.py`, which wraps the `cvss` PyPI package (RedHat
Product Security's implementation of the official algorithm) rather than
reimplementing the lookup table.

# Base metrics (decide each, then state why)

Exploitability:
- **AV** Attack Vector — Network / Adjacent / Local / Physical
- **AC** Attack Complexity — Low / High
- **AT** Attack Requirements — None / Present (new in 4.0: does exploitation
  need a specific pre-existing condition — a race window, a prior
  misconfiguration already in place — beyond the attacker's own actions?)
- **PR** Privileges Required — None / Low / High
- **UI** User Interaction — None / Passive / Active

Impact — **two separate sets**, replacing 3.1's single Scope-gated C/I/A:
- **VC / VI / VA** — Confidentiality / Integrity / Availability impact on the
  **Vulnerable System** itself (the thing with the flaw).
- **SC / SI / SA** — Confidentiality / Integrity / Availability impact on a
  **Subsequent System** (anything downstream the vulnerable system can affect
  but didn't itself contain the flaw) — None / Low / High for both sets.

This is the single most important conceptual change from 3.1: there is no
`Scope` metric anymore. Where 3.1 forced a binary Unchanged/Changed judgment
call (the most-misjudged metric in that spec), 4.0 asks directly "what
happens to the vulnerable system" and "what happens beyond it" as two
independently-scored impact sets. If a flaw only affects the component that
has it, leave SC/SI/SA at None. If exploiting it lets an attacker reach data
or systems outside that component's own authority (as with the KubeHawk
agent finding — its own cluster-wide RBAC read access meant compromising it
disclosed data belonging to the whole cluster, not just the agent pod), that
belongs in VC (what the agent itself discloses) with the broader blast
radius reasoned about in the writeup even though CVSS 4.0's SC/SI/SA is
specifically about *causing* impact on a separate system, not merely *having
read access* to one — be precise about which set actually applies.

# Optional refinement metrics (only score these if the context supports it)

- **Threat (E — Exploit Maturity):** Not Defined / Unreported / Proof-of-
  Concept / Attacked. Renamed from 3.1's "Temporal" group.
- **Environmental:** `CR`/`IR`/`AR` (Confidentiality/Integrity/Availability
  Requirements for the affected asset — how much does *this* organization
  depend on it), plus Modified Base metrics (`MAV`, `MAC`, `MAT`, `MPR`,
  `MUI`, `MVC`, `MVI`, `MVA`, `MSC`, `MSI`, `MSA`) if a compensating control
  or asset-specific context changes a Base value. There is no separate
  "environmental formula" to run afterward — `cvss4-score.py` computes the
  final score from whatever combination of Base/Threat/Environmental metrics
  the vector contains in one pass.
- **Supplemental (informational only, never changes the score):** Safety,
  Automatable, Recovery, Value Density, Vulnerability Response Effort,
  Provider Urgency. Include these in the writeup when they materially affect
  how a reader should prioritize the finding, but don't expect them to move
  the number.

# Severity bands

Unchanged from 3.1: `0.0` None · `0.1–3.9` Low · `4.0–6.9` Medium ·
`7.0–8.9` High · `9.0–10.0` Critical.

# Steps

1. Reason through each Base metric from the evidence; note assumptions
   explicitly (especially for AT, and for which impact set — VC/VI/VA vs
   SC/SI/SA — actually applies).
2. Add Threat/Environmental metrics only if the engagement/report context
   actually supports them (a known exploit-maturity signal, a stated asset
   criticality, a documented compensating control) — don't invent values to
   fill out the vector.
3. Build the vector string: `CVSS:4.0/AV:_/AC:_/AT:_/PR:_/UI:_/VC:_/VI:_/VA:_/SC:_/SI:_/SA:_`
   (append any Threat/Environmental metrics after the Base block).
4. Run the script to get the exact score:
   ```
   python3 <plugin-root>/scripts/cvss4-score.py "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N"
   ```
   Requires the `cvss` package (`pip install cvss`); the script fails open
   (exit 2) rather than fabricating a score if it's missing.
5. Report the score, vector, and a one-line rationale per metric — state
   assumptions so the score can be challenged and reproduced.

# Output

```
CVSS 4.0: <score> (<Severity>)
Vector: CVSS:4.0/AV:_/AC:_/AT:_/PR:_/UI:_/VC:_/VI:_/VA:_/SC:_/SI:_/SA:_
Rationale: AV=… AC=… AT=… PR=… UI=… VC=… VI=… VA=… SC=… SI=… SA=…
```

# Notes

- Be explicit about which impact set (VC/VI/VA vs SC/SI/SA) applies to each
  consequence you describe — this replaces Scope as the metric most likely
  to be misjudged, so state the reasoning, not just the letter values.
- `security-reporting:finding`'s template references this skill for
  severity — use CVSS 4.0 there now, not 3.1.
