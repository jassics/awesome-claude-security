---
name: executive-summary
description: >-
  Distill technical security results into a concise, business-oriented summary
  for leadership or a board. Use when the audience is executives/non-technical
  stakeholders and the ask is risk and decisions, not technical detail.
---

# Goal

A half-to-one-page summary that answers: how exposed are we, what's the headline
risk, and what should leadership decide/fund — in business language.

# Structure

- **Bottom line** (1–2 sentences): overall risk posture and direction vs. last time.
- **Why it matters**: business impact (revenue, compliance, trust, downtime) — not
  CVE numbers.
- **Top risks** (3–5): each one line, plain language, with relative severity.
- **What we recommend**: the few decisions/investments that move risk most.
- **Trend**: improving/declining, with one supporting metric if available.

# Steps

1. Translate findings into business consequences; drop jargon and tool names.
2. Aggregate to themes (e.g. "identity weaknesses", "unpatched exposure") rather
   than listing every finding.
3. Quantify where you can (residual risk, % critical remediated, MTTR).
4. Lead with the decision the reader must make.

# Output

The summary (Markdown). Offer to pair it with `security-diagramming:infographic`
for a board-ready one-pager, and to roll it into a `pentest-report` or CISO deck.

# Notes

Executives optimize for decisions under uncertainty — give them the "so what" and
the recommended action, not a finding dump.
