---
name: mindmap
description: >-
  Turn a security topic into a structured mindmap — recon surface, an attack
  chain, a framework breakdown, or study notes. Use when organizing or
  explaining a topic radially rather than as a flow or report.
---

# Goal

A hierarchical mindmap with a central topic and branching sub-topics, useful for
recon surface maps, framework breakdowns (e.g. OWASP/ATT&CK), or learning notes.

# Steps

1. Set the central node (the topic).
2. Add primary branches (the main categories), then sub-branches to a sensible
   depth (usually 2–3 levels).
3. Keep labels to a few words; lean on hierarchy, not sentences.
4. Render: prefer the Excalidraw MCP; otherwise emit a Mermaid `mindmap` block
   and an indented bullet outline as a fallback.

# Output

- The mindmap (rendered or as importable Mermaid).
- The same content as a nested outline (so it's usable in notes/tickets).

# Notes

Good for kicking off OSINT (map the target's surface) or for `security-knowledge`
study aids. For cause/effect or sequence, prefer `attack-tree` or an
`architecture-diagram` instead.
