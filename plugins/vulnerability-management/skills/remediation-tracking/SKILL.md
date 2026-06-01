---
name: remediation-tracking
description: >-
  Manage the vulnerability remediation lifecycle: assign owners and SLAs, track
  fix/verify/close states, handle risk acceptances and exceptions, and report
  program metrics (SLA compliance, MTTR, aging, recurrence). Use when turning a
  prioritized list into tracked, accountable work.
---

# Goal

Every prioritized vulnerability has an owner, an SLA, and a current lifecycle state —
and the program can report how it's doing, not just dump a scan.

# Lifecycle states

`Open → Assigned → In Progress → Remediated → Verified → Closed`, plus
`Risk Accepted` / `Exception` (time-boxed, with an owner and review date) and
`Reopened` (regressed or re-detected).

# Steps

1. **Assign** — owner (team that controls the asset), tier-based SLA, and target
   date. SLA clock starts at first detection, not at assignment.
2. **Define "done"** — patch, config change, compensating control, or
   decommission. A compensating control is a mitigation, not a closure — track it as
   such with a re-review date.
3. **Verify** — confirm the fix via rescan or manual check before closing; never
   close on the owner's say-so alone.
4. **Govern exceptions** — risk acceptances are time-boxed, justified, owned, and
   expire into a re-review. No permanent exceptions.
5. **Report metrics** — SLA compliance %, MTTR by severity, open aging buckets,
   backlog trend, recurrence rate, and KEV exposure. Surface what's breaching.

# Output

A tracker view (per-item: owner · tier · SLA · state · due/aging · verification) plus
a program-metrics summary. For exec/board framing use `security-reporting`; for trend
visuals use `security-diagramming`.

# Notes

Recurrence rate is the health signal everyone ignores — vulns that keep coming back
mean the root cause (golden image, base layer, IaC module) isn't fixed. Verify before
close, or your metrics lie. Aging exceptions are debt; make them expire.
