---
name: infographic
description: >-
  Create a shareable single-page infographic / one-pager summarizing a security
  posture, assessment result, metric set, or program update for a non-technical
  or executive audience. Use when the ask is "make this presentable / visual /
  board-ready" rather than a full report.
---

# Goal

A clean, at-a-glance visual one-pager: a headline message, 3–6 key stats or
findings, a simple visual (gauge, severity bars, timeline), and a clear "so
what / next steps" footer.

# Steps

1. Identify the **single message** the one-pager must land.
2. Pick 3–6 supporting data points (counts by severity, posture score, trend,
   coverage %). Don't crowd it.
3. Choose a layout: hero stat + supporting tiles, or severity bar + callouts.
4. Render: prefer the Excalidraw MCP for an editable visual; otherwise emit
   `.excalidraw` JSON plus an HTML one-pager (inline CSS, print-friendly) the
   user can open or convert to PDF.
5. Use a restrained palette and severity-consistent colors (critical=red,
   high=orange, medium=amber, low=blue).

# Output

- The infographic (Excalidraw and/or standalone HTML).
- A note on what data to refresh to regenerate it next cycle.

# Notes

For a full narrative document use `security-reporting` instead; this skill is for
the visual summary. Executive decks (CISO/CTO) compose this skill with
`security-reporting`.
