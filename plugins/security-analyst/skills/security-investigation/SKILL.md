---
name: security-investigation
description: >-
  Drive a security investigation from a lead or hypothesis to an evidence-backed
  conclusion — correlate telemetry across sources, enrich with intel, reconstruct a
  timeline, scope impact, and reach a defensible verdict. Use for a deeper analytical
  investigation (beyond single-alert triage), e.g. an escalated or complex case.
---

# Goal

A coherent answer to "what actually happened, how far did it go, and what does it
mean" — built from correlated evidence, with a clear verdict, scope, and recommended
action.

# How this differs from neighbors

- **Alert triage** (`soc-siem:alert-triage`) — a verdict on *one* alert, fast and
  repeatable. Escalates into an investigation.
- **Investigation** (this) — pulls *many* threads (multiple alerts, logs, intel,
  hosts, accounts) into one analytic picture.
- **Incident response** (`dfir:incident-response`) — the response *action* once an
  investigation confirms an incident. Hand off to it.

# Steps

1. **Frame the question** — the lead/hypothesis and what a conclusion would look like
   (confirmed malicious? scope? root cause?). Investigations are hypothesis-driven.
2. **Collect & correlate** — gather relevant telemetry (EDR, auth, network, app,
   SIEM) across the time window; correlate by entity (host, user, process, IP) into a
   single picture. Baseline normal to separate signal from noise.
3. **Enrich** — add intel context (`threat-intelligence:ioc-enrichment`,
   `threat-actor-profiling`) and asset/user criticality; reconcile aliases.
4. **Reconstruct the timeline** — normalize timestamps (UTC); order attacker/entity
   actions into a chronology (lean on `dfir:forensic-triage` for host/forensic depth).
5. **Scope** — pivot to find all affected entities, lateral movement, and dwell time;
   map observed behavior to MITRE ATT&CK.
6. **Assess & conclude** — verdict (confirmed/suspected/benign), confidence,
   impact/scope, root cause, and intelligence gaps. Separate fact from assessment.
7. **Act** — escalate to `dfir:incident-response` if confirmed; turn findings into
   detections (`detection-engineering`); document either way.

# Output

An investigation report: question · evidence (correlated, with sources) · timeline ·
ATT&CK mapping · scope/impact · verdict + confidence · root cause · recommended
actions. Visualize timeline/link analysis with `security-diagramming`; write up with
`security-reporting`.

# Notes

Correlation is the core skill — a single source rarely tells the truth; pivot across
entities and baseline normal before concluding. State confidence and separate fact
from assessment from assumption. Know when to stop analyzing and **escalate**: once
it's a confirmed incident, IR owns the response.
