---
name: pasta
description: >-
  Run the PASTA (Process for Attack Simulation and Threat Analysis) seven-stage,
  risk-centric threat model that ties technical threats to business impact. Use
  for a deeper, attacker-simulation threat model where business risk alignment
  matters (vs. the faster STRIDE pass).
---

# Goal

A PASTA threat model: business objectives → technical scope → decomposition →
threat analysis → vulnerability mapping → attack modeling → risk & countermeasures.

# The seven stages

1. **Define objectives** — business goals, compliance drivers, risk appetite, and
   the assets that matter. Anchors everything in business impact.
2. **Define technical scope** — architecture, dependencies, trust boundaries.
   Build/ingest the DFD (`security-diagramming:threat-model-dfd`).
3. **Application decomposition** — actors, entry points, assets, data flows, and
   the controls already present.
4. **Threat analysis** — relevant threat actors and TTPs; pull from threat intel
   and map to **MITRE ATT&CK** techniques.
5. **Vulnerability & weakness analysis** — known weaknesses (CWE), findings from
   scans/tests, and design flaws that the threats could use.
6. **Attack modeling** — build attack trees / attack paths from entry points to
   target assets (`security-diagramming:attack-tree`); simulate the chains.
7. **Risk & impact analysis** — score residual risk, prioritize, and define
   countermeasures with business-justified priority.

# Steps

Work the stages in order; each feeds the next. Capture outputs per stage so the
model is auditable. Map threats to ATT&CK and weaknesses to CWE for traceability.

# Output

A staged PASTA document: objectives → scope/DFD → decomposition → threats (ATT&CK)
→ weaknesses (CWE) → attack trees → ranked risks & countermeasures. Use
`security-reporting` for the final deliverable.

# Notes

PASTA's value is business alignment and attacker simulation — keep stage 1 and
stage 7 tightly connected so technical findings map back to business risk. Use
STRIDE instead when you need a faster, design-time pass.
