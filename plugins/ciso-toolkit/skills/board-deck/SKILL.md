---
name: board-deck
description: >-
  Produce a board / executive security presentation — risk posture and direction,
  top risks in business terms, program progress against strategy, the metrics that
  matter, and investment asks tied to risk. Use to prepare for a board or leadership
  meeting. Audience is non-technical decision-makers.
---

# Goal

A concise, decision-oriented deck that gives the board what they need: how exposed
are we, are we improving, and what should they fund or decide — in business language.

# Structure (lead with the answer)

1. **Bottom line** — overall risk posture and direction vs. last review (1 slide).
2. **Top risks** — 3–5 in business terms (loss scenarios, not CVEs), with severity
   and trend (`cyber-risk-quantification`).
3. **Program progress** — where the strategy stands vs. plan; key wins and what's
   behind (`security-strategy`).
4. **Metrics that matter** — a small, stable set (e.g. risk reduction, critical
   remediation %, MTTR, coverage, incident trend) — consistent across meetings so
   trend is readable.
5. **The ask** — investment/decisions needed, each tied to the risk it reduces and
   the consequence of inaction.
6. **Appendix** — supporting detail, incidents, benchmarks, regulatory items.

# Steps

1. Confirm the audience and the **decision/ask** this meeting must produce — build
   backward from it.
2. Pull the risk picture (`cyber-risk-quantification`) and program status
   (`security-strategy`); translate to business language, drop jargon.
3. Keep it tight: one message per slide, few stable metrics, clear asks.
4. Generate the visuals (posture scorecard, risk heat map, trend) with
   `security-diagramming:infographic`; assemble narrative via
   `security-reporting:executive-summary`.

# Output

A board deck (slide outline + content + visual specs) plus a one-page executive
summary. Render visuals with `security-diagramming`.

# Notes

Boards optimize for decisions under uncertainty — lead with posture and the ask, not
a tour of activity. Keep the metric set small and **stable** so trends are
comparable meeting to meeting. Every ask ties to a risk and the cost of not acting.
