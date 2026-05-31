---
name: attack-tree
description: >-
  Build an attack tree for a stated attacker goal or asset, decomposing it into
  AND/OR sub-goals and leaf attack steps, then render it. Use when threat
  modeling, planning an engagement, or explaining how an asset could be
  compromised.
---

# Goal

Produce a clear attack tree: a root attacker goal decomposed via AND/OR logic
into intermediate sub-goals and concrete leaf attacks, optionally annotated with
cost / difficulty / detectability, and rendered as a diagram.

# Steps

1. **Define the root.** Confirm the single attacker goal (e.g. "exfiltrate
   customer PII", "obtain domain admin"). One tree per goal.
2. **Decompose top-down.** Break the goal into sub-goals. Mark each node:
   - **OR** — any child achieves the parent (alternative paths).
   - **AND** — all children required together.
   Continue until leaves are concrete, actionable attack steps.
3. **Annotate leaves** (optional but recommended): cost, skill required,
   likelihood, and detectability. These drive prioritization and detection gaps.
4. **Identify cheapest/least-detectable path** to the root — that's the priority
   to mitigate and to build detections for.
5. **Render** with the `architecture-diagram` rendering approach: prefer the
   Excalidraw MCP; otherwise emit a Mermaid `flowchart TD` (root at top, AND
   nodes labeled, leaves as boxes) plus Graphviz DOT.

# Output

- The attack tree diagram (rendered or as importable Mermaid/DOT/Excalidraw JSON).
- A short table of leaf paths ranked by cost × likelihood ÷ detectability.
- A "mitigations & detections" list keyed to the highest-risk path.

# Notes

Use AND/OR semantics correctly — mislabeling changes the risk story. Keep node
labels short; put detail in the ranked table. Hand the ranked findings to
`security-reporting` if a writeup is needed.
