---
name: threat-model-dfd
description: >-
  Draw a Data Flow Diagram with trust boundaries for threat modeling: external
  entities, processes, data stores, data flows, and the boundaries between them.
  Use when starting a STRIDE/PASTA threat model or documenting how data moves
  through a system.
---

# Goal

A DFD that a threat model can be built on: every element typed correctly and
every trust boundary drawn, so STRIDE can be applied per element/flow.

# Elements (use standard DFD notation)

- **External entity** — rectangle. Actors/systems outside your control.
- **Process** — circle/rounded box. Code that transforms data.
- **Data store** — open-ended/parallel lines. Databases, queues, files, caches.
- **Data flow** — arrow. Label with what data moves and the protocol.
- **Trust boundary** — dashed box/line. Where privilege or trust level changes
  (internet↔DMZ, app↔DB, tenant↔tenant, user↔kernel).

# Steps

1. List actors, processes, stores, and the data that flows between them (ask the
   user for the architecture if not supplied).
2. Place trust boundaries wherever data crosses a privilege/trust change — these
   are where threats concentrate.
3. Label every flow with **data + protocol + auth** (e.g. "PII over TLS, JWT").
4. Render: prefer the Excalidraw MCP; otherwise emit Mermaid `flowchart LR` with
   `subgraph` blocks for trust boundaries, plus an element/flow inventory table.

# Output

- The DFD (rendered or importable).
- An inventory table: element · type · trust zone · sensitive data handled.
- A list of trust-boundary crossings (the prime spots to enumerate threats next).

# Notes

This pairs directly with `threat-modeling:stride` — produce the DFD first, then
walk STRIDE per element and per boundary crossing.
