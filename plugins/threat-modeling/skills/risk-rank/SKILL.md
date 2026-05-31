---
name: risk-rank
description: >-
  Rank a set of enumerated threats or findings by risk (likelihood × impact) and
  map each to a prioritized mitigation. Use after STRIDE/PASTA enumeration or any
  time you have a threat/finding list that needs prioritization.
---

# Goal

A defensible risk ranking that drives remediation order, with each item tied to a
mitigation and a suggested priority.

# Method

1. **Score likelihood** (1–5): attacker capability required, exposure/reachability,
   exploit availability, existing controls.
2. **Score impact** (1–5): confidentiality/integrity/availability damage, blast
   radius, business/compliance consequence.
3. **Risk = likelihood × impact** (1–25). Banding: 1–5 Low · 6–11 Medium ·
   12–18 High · 19–25 Critical. (For vuln-level items, prefer CVSS via
   `security-reporting:cvss` and reconcile the two.)
4. **Map mitigation** per item: the control that most reduces likelihood or impact;
   note whether it already exists (gap vs. present).
5. **Prioritize** by risk, then by remediation cost/effort (quick high-risk wins
   first).

# Output

A ranked table: ID · threat/finding · likelihood · impact · risk · band ·
mitigation · effort · priority. Plus a short "do first / do next / accept" list.

# Notes

State the scoring assumptions so the ranking is reproducible and challengeable.
Keep likelihood and impact independent — don't double-count exposure in both.
