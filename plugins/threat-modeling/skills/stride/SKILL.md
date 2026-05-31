---
name: stride
description: >-
  Run a STRIDE threat model over a system: build/ingest a DFD, then enumerate
  Spoofing, Tampering, Repudiation, Information disclosure, Denial of service,
  and Elevation of privilege threats per element and trust-boundary crossing,
  with mitigations. Use when threat modeling an application, service, or design.
---

# Goal

A STRIDE threat model: each DFD element and trust-boundary crossing examined for
the six threat classes, threats recorded with risk, and each mapped to a mitigation.

# STRIDE ↔ property

| Threat | Violates | Typical mitigation theme |
| --- | --- | --- |
| **S**poofing | Authentication | Strong authn, MFA, mutual TLS, signed tokens |
| **T**ampering | Integrity | Input validation, signing, integrity checks, least privilege writes |
| **R**epudiation | Non-repudiation | Audit logging, tamper-evident logs, timestamps |
| **I**nformation disclosure | Confidentiality | Encryption in transit/at rest, authz, data minimization |
| **D**enial of service | Availability | Rate limiting, quotas, autoscaling, timeouts |
| **E**levation of privilege | Authorization | Least privilege, authz checks, sandboxing, segmentation |

# Steps

1. **Get the DFD.** If none exists, invoke `security-diagramming:threat-model-dfd`
   first. Confirm elements (external entities, processes, data stores, flows) and
   trust boundaries.
2. **Per element/flow, walk all six letters.** Focus on **trust-boundary
   crossings** — that's where threats concentrate. Apply only the letters that
   make sense for the element type (e.g. data stores rarely "spoof").
3. **Record each threat**: ID · element · STRIDE class · description · preconditions.
4. **Rank** with `/threat-modeling:risk-rank` (likelihood × impact).
5. **Map mitigations** per threat; note existing controls vs. gaps.
6. Optionally model the top threats as attack trees (`security-diagramming:attack-tree`).

# Output

A STRIDE table (element · STRIDE class · threat · risk · mitigation · status) plus
a short "top risks & recommended controls" summary. Hand to `security-reporting`
if a formal document is needed.

# Notes

Don't force all six letters onto every element — apply per element type. Tie each
threat to a real data flow so it's concrete and testable.
