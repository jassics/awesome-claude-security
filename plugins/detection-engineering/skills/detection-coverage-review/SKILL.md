---
name: detection-coverage-review
description: >-
  Assess detection coverage against the MITRE ATT&CK matrix: which tactics/techniques
  are covered, partially covered, or blind, weighted by data-source availability and
  threat relevance. Use to find and prioritize detection gaps for a SOC/program.
---

# Goal

A coverage map across ATT&CK with honest gap analysis — not a vanity "we cover X
techniques" count, but where you're actually blind and what to build next.

# Steps

1. **Inventory detections** — map each existing rule/alert to ATT&CK technique(s)
   (use the metadata from `detection-rule-development`).
2. **Inventory data sources** — what telemetry is actually collected and onboarded
   (you cannot detect what you don't log). Coverage is gated by data, not rule count.
3. **Rate each technique** — None / Partial / Good, factoring rule quality (does it
   really detect the technique or just one variant?) and data availability.
4. **Weight by threat relevance** — prioritize techniques used by actors targeting
   your sector/environment (pull from `threat-intelligence`); don't chase the whole
   matrix uniformly.
5. **Identify gaps & plan** — blind spots on relevant, high-impact techniques first;
   note whether the fix is a new rule, new data source, or tuning.

# Output

An ATT&CK coverage view (tactic × technique with None/Partial/Good), a data-source
gap list, and a prioritized build backlog. Visualize as an ATT&CK-style heatmap
(`security-diagramming`) and report with `security-reporting`.

# Notes

Coverage is bounded by **data sources**, not rule count — a missing log source is a
bigger gap than a missing rule. Prioritize by adversary relevance (threat-informed
defense), not raw matrix completeness. Beware "coverage theater": one weak rule
mapped to a technique is not real coverage.
