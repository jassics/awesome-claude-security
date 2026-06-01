---
description: Run a T2/T3 security investigation — correlate telemetry, enrich, reconstruct the timeline, reach an evidence-backed verdict.
argument-hint: [case / escalated alert + context]
---

Investigate: **$ARGUMENTS**

Walk the investigation, using installed skills (note any whose plugin is missing):

1. **Frame** — `/security-analyst:security-investigation` to set hypotheses and the questions to answer.
2. **Correlate** — pull and connect telemetry across sources; `/detection-engineering:threat-hunting` to find related activity.
3. **Enrich** — `/threat-intelligence:ioc-enrichment` and `/threat-intelligence:threat-actor-profiling` to attribute and contextualize.
4. **Timeline** — `/dfir:forensic-triage` to reconstruct what happened, in order, with evidence.
5. **Verdict** — confirmed incident or not; scope, impact, and confidence. If confirmed, hand to `/dfir:incident-response`.
6. **Report** — `/security-reporting:finding` or an investigation writeup; `/security-diagramming:mindmap` for the timeline/relationship view.

For deep execution, hand off to the `security-analyst` agent. Anchor every conclusion to specific evidence and state your confidence.
