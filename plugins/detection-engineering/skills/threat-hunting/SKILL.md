---
name: threat-hunting
description: >-
  Run a hypothesis-driven threat hunt: form a hypothesis (often from ATT&CK or
  threat intel), query telemetry for evidence, analyze findings, and convert
  results into detections. Use to proactively search for adversary activity that
  existing alerts may miss.
---

# Goal

A structured hunt that either finds adversary activity or builds confidence it's
absent — and leaves behind a new detection or a documented data/coverage gap.

# Steps

1. **Hypothesize** — a specific, testable statement, e.g. "an adversary is using
   [ATT&CK technique] via [mechanism] in [scope]." Source it from ATT&CK, fresh
   `threat-intelligence`, an anomaly, or a recent incident (`dfir`).
2. **Scope & data** — which telemetry answers the hypothesis; confirm it exists and
   the time window.
3. **Hunt** — query for the behavior; baseline normal to separate signal from noise;
   pivot on what you find (hosts, accounts, processes, network).
4. **Analyze** — triage hits: benign / suspicious / malicious. If malicious, escalate
   to `dfir:incident-response`.
5. **Operationalize** — turn a successful hunt into a durable rule
   (`detection-rule-development`); if you couldn't hunt it, log the data/visibility
   gap for `detection-coverage-review`.

# Output

A hunt report: hypothesis · data sources · queries · findings (with evidence) ·
outcome (clean / escalated) · follow-up (new detection or coverage gap). Use
`security-reporting`.

# Notes

A hunt that finds nothing is still a success if it produced a new detection or
revealed a visibility gap — capture that, don't just close it out. Always baseline
normal before calling activity suspicious. Hunt the techniques most relevant to your
threat model first.
