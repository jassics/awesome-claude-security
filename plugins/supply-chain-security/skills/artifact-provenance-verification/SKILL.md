---
name: artifact-provenance-verification
description: >-
  Assess and establish build artifact provenance and integrity — SLSA provenance
  level, signing/attestation (Sigstore/cosign, in-toto), and verification at
  deploy/admission. Use when you need to prove an artifact (container image,
  package, binary) came from the expected source and build, untampered.
---

# Goal

A clear picture of an artifact's provenance maturity and a path to "only verified,
attested artifacts are deployed" — so a tampered or unknown-origin artifact can't
reach production.

# Frame against SLSA

Map the build/artifact flow to a **SLSA** build level and identify the next gap:

- **L1** — provenance exists (build is scripted, provenance generated).
- **L2** — provenance is signed and from a hosted build service.
- **L3** — build runs on hardened, isolated infrastructure; provenance is
  non-forgeable. This is the meaningful bar for tamper resistance.

# Steps

1. **Inventory trust signals** — is the artifact signed? By what identity
   (keyless/OIDC via Sigstore, or a managed key)? Is there a provenance attestation
   (in-toto / SLSA) linking artifact ↔ source commit ↔ builder?
2. **Verify the chain** — source → build → artifact → registry → deploy. Confirm the
   signing identity and provenance are checked, not just present.
3. **Find the enforcement gap** — is verification *required* at admission/deploy
   (e.g., cosign verify in an admission controller / policy gate), or merely
   available? Unverified-but-signed is theater.
4. **Recommend** — signing in CI (keyless preferred), provenance generation,
   verification policy at the gate, and key/identity trust roots + revocation.

# Output

A provenance assessment: current SLSA level · signing/attestation state · where
verification is (and isn't) enforced · prioritized steps to the next level. Pair with
`pipeline-integrity-review` for the build side and `security-diagramming` for the
chain-of-custody diagram.

# Notes

Signing without enforced verification buys nothing — the control is the *gate that
rejects unverified artifacts*. Keyless (OIDC/Fulcio) signing avoids long-lived key
management and is the modern default. Provenance must bind artifact → exact source
commit → builder, or it can't prove "this came from that build."
