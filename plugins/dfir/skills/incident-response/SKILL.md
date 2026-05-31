---
name: incident-response
description: >-
  Drive a security incident through the response lifecycle (NIST SP 800-61 / SANS
  PICERL): triage and scope, contain, eradicate, recover, and capture lessons
  learned. Use to coordinate or work an active incident. Authorized responders only.
---

# Goal

A controlled response that limits damage, removes the adversary, restores
operations, and produces an evidence-backed record — without destroying evidence or
tipping off the attacker prematurely.

# Lifecycle (NIST 800-61 / PICERL)

1. **Preparation** — confirm authority, roles, comms plan, and tooling (mostly
   pre-incident; verify they're in place).
2. **Identification / triage** — validate the incident is real; determine type,
   scope, affected assets, and severity. Preserve volatile evidence first
   (`forensic-triage`).
3. **Containment** — short-term (isolate hosts, block C2, disable accounts) then
   long-term, balancing speed against evidence preservation and attacker awareness.
4. **Eradication** — remove the foothold: malware, persistence, created accounts,
   and the root cause/initial access vector.
5. **Recovery** — restore from known-good, validate integrity, monitor for return,
   and lift containment in a controlled way.
6. **Lessons learned** — post-incident review: timeline, root cause, what worked,
   and improvements (detections, controls, process).

# Steps

1. Establish scope and severity; declare and track the incident.
2. Work the phases; at each step record actions, timestamps, and evidence handled.
3. Extract IOCs (`ioc-development`) and feed containment/detection in parallel.
4. Drive to root cause and confirm full eradication before recovery.

# Output

An incident record: classification · scope · timeline · actions · IOCs · root cause
· recovery status · lessons. Use `security-reporting` for the incident report;
recommend detections via `detection-engineering`.

# Notes

Contain without destroying evidence or alerting the adversary prematurely — sequence
matters. "Eradicated" means the **root cause and all persistence** are gone, not
just the malware you first saw. Capture lessons into durable detections and control
changes, or the next incident repeats.
