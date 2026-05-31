---
name: cvss
description: >-
  Score a vulnerability with CVSS v3.1: derive the base metric vector, compute
  the score and severity rating, and explain each metric choice. Use whenever a
  finding needs a defensible severity rather than a guess.
---

# Goal

A defensible CVSS v3.1 base score: the full vector string, numeric score,
severity band, and a one-line justification per metric.

# Base metrics (decide each, then state why)

Exploitability:
- **AV** Attack Vector — Network / Adjacent / Local / Physical
- **AC** Attack Complexity — Low / High
- **PR** Privileges Required — None / Low / High
- **UI** User Interaction — None / Required

Scope & impact:
- **S** Scope — Unchanged / Changed (does it break out of its security authority?)
- **C / I / A** Confidentiality / Integrity / Availability — None / Low / High

# Severity bands

`0.0` None · `0.1–3.9` Low · `4.0–6.9` Medium · `7.0–8.9` High · `9.0–10.0` Critical.

# Steps

1. Reason through each base metric from the evidence; note assumptions.
2. Produce the vector, e.g. `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N`.
3. Compute the base score and map to a band.
4. If temporal/environmental context is provided (exploit maturity, compensating
   controls, asset criticality), offer an adjusted environmental score too.

# Output

```
CVSS 3.1 Base: <score> (<Severity>)
Vector: CVSS:3.1/AV:_/AC:_/PR:_/UI:_/S:_/C:_/I:_/A:_
Rationale: AV=… AC=… PR=… UI=… S=… C=… I=… A=…
```

# Notes

Be explicit about Scope — it's the most-misjudged metric and it swings the score.
State assumptions so the score can be challenged and reproduced.
