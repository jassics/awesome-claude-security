---
name: architecture-diagram
description: >-
  Produce a security architecture, network, or trust-boundary diagram of a
  system, highlighting components, zones, controls, and exposure. Use when
  documenting a design review, network segmentation, or cloud architecture from
  a security perspective.
---

# Goal

A diagram that makes the security-relevant structure legible: components, the
zones/segments they sit in, the controls between them, and where the system is
exposed.

# Steps

1. Gather the components (services, gateways, data stores, identities) and how
   they connect. Ask for the design if not provided.
2. Group into **zones** (internet, edge/DMZ, app tier, data tier, management,
   each cloud account/VPC/namespace). Draw zone boundaries explicitly.
3. Annotate **controls** on the links: TLS, authn/authz, WAF, firewall rules,
   network policy, encryption-at-rest on stores.
4. Mark **exposure**: anything internet-reachable, public buckets, admin planes.
5. Render: prefer the Excalidraw MCP; otherwise emit Mermaid `flowchart` with
   `subgraph` per zone, plus DOT for tooling that prefers Graphviz.

# Rendering contract (shared by all diagram skills)

- If an Excalidraw MCP server/tool is available, create the diagram there and
  save/export it; tell the user the file location.
- Otherwise output, in this order: (a) a fenced ```mermaid block, (b) a fenced
  `.excalidraw` JSON block the user can import at excalidraw.com, (c) for graphs,
  a ```dot block. Keep node labels short.

# Output

- The diagram (rendered or importable).
- A legend mapping shapes/colors to zones and control types.
- A short "exposure & controls gaps" note for follow-up.
