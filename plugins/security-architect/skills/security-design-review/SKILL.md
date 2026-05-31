---
name: security-design-review
description: >-
  Review a system or architecture design for security — trust boundaries, control
  selection, secure-by-design principles, defense-in-depth, and security
  requirements — and produce prioritized design recommendations. Use when assessing
  or shaping an architecture/design (not testing a running system).
---

# Goal

A design-level security assessment: where the design is weak by construction, which
controls are missing or misplaced, and the prioritized changes — caught at design
time, before it's built.

# What to review

1. **Architecture & trust boundaries** — components, data flows, and where trust/
   privilege changes. Build/ingest the picture with
   `security-diagramming:architecture-diagram` / `threat-model-dfd`.
2. **Threats by design** — run `threat-modeling:stride` (or `pasta`) over the design
   to enumerate threats per element and boundary crossing.
3. **Control selection** — are the right controls present at the right layers
   (authn/authz, encryption, segmentation, input handling, logging, key/secret
   management)? Map controls to the threats they address; find gaps and redundancies.
4. **Secure-by-design principles** — least privilege, defense-in-depth, fail-safe
   defaults, complete mediation, minimize attack surface, secure defaults, separation
   of duties, no security-by-obscurity.
5. **Security requirements** — derive the non-negotiable requirements the build must
   meet (and how they'll be verified later — ties to the relevant domain plugin's
   testing skills).
6. **Trade-offs** — weigh risk reduction against usability, performance, and cost;
   recommend proportionate controls, not maximal ones.

# Steps

1. Establish context: purpose, data sensitivity, users, threat model, and constraints.
2. Diagram the architecture and trust boundaries.
3. Enumerate threats (`threat-modeling`) and map existing/missing controls to them.
4. Assess against secure-by-design principles; identify design-level weaknesses.
5. Recommend prioritized changes and the security requirements for the build.

# Output

A design review: architecture diagram · threat→control mapping · design weaknesses ·
prioritized recommendations · security requirements (with verification method). Use
`security-reporting`; rank with `threat-modeling:risk-rank`.

# Notes

Fixing a design flaw on paper is far cheaper than after it ships — focus on
structural weaknesses (missing boundaries, wrong trust assumptions, absent controls),
not implementation bugs (those are the domain plugins' job). Recommend proportionate,
layered controls and make the trade-offs explicit for the decision-maker.
