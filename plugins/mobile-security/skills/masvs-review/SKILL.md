---
name: masvs-review
description: >-
  Review a mobile app (Android/iOS) against the OWASP MASVS control groups —
  storage, crypto, auth, network, platform, code quality, and resilience —
  producing a per-control finding set. Use for a structured mobile security
  assessment or design review. Authorized testing only.
---

# Goal

A MASVS-aligned assessment: each control group examined, with applicability,
evidence, severity, and remediation.

# MASVS control groups

- **MASVS-STORAGE** — sensitive data at rest, leakage via logs/backups/IPC/clipboard.
- **MASVS-CRYPTO** — key management and correct, current cryptography.
- **MASVS-AUTH** — authentication and authorization, biometrics, session handling.
- **MASVS-NETWORK** — TLS, certificate validation/pinning, no cleartext.
- **MASVS-PLATFORM** — IPC, WebViews, deep links, permissions, platform APIs.
- **MASVS-CODE** — input handling, dependencies, build/hardening settings.
- **MASVS-RESILIENCE** — anti-tampering, anti-reversing, integrity (defense-in-depth,
  not a substitute for the above).

# Steps

1. Gather artifacts: the app package (APK/IPA), and source if available.
2. Walk each control group; for static checks, cross-ref `sast-sca`; for runtime,
   use `mobile-pentest`.
3. Record per control: applicable? · finding · evidence · severity · remediation.
4. Score (`security-reporting:cvss`) and rank.

# Output

A per-control table grouped by MASVS category + ranked top risks. Confirmed issues →
`security-reporting:finding`.

# Notes

The highest-frequency mobile issues are insecure data storage and weak network/TLS
handling (broken cert validation, no pinning where warranted). Treat RESILIENCE as
defense-in-depth — never as a replacement for fixing storage/crypto/auth. Test only
apps you're authorized to assess.
