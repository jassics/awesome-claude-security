---
name: owasp-web-top10
description: >-
  Assess a web application against the OWASP Top 10 (2021), producing a
  per-category finding set with severity and remediation. Use when reviewing or
  pentesting a web app for the most common, highest-impact web risks. Authorized
  testing only.
---

# Goal

A structured assessment across the ten OWASP Web categories, each with
applicability, evidence, severity, and remediation.

# Steps

1. **Map the app** — entry points, roles, auth model, sensitive functions, tech
   stack. A `threat-modeling:stride` pass helps prioritize.
2. **Walk each category** (see `reference.md` for checks + fixes):
   A01 Broken Access Control · A02 Cryptographic Failures · A03 Injection ·
   A04 Insecure Design · A05 Security Misconfiguration · A06 Vulnerable &
   Outdated Components · A07 Identification & Authentication Failures ·
   A08 Software & Data Integrity Failures · A09 Security Logging & Monitoring
   Failures · A10 Server-Side Request Forgery (SSRF).
3. **Substantiate** rather than assert: use `access-control-test` and
   `injection-test` for those categories; for components, cross-ref `sast-sca`.
4. **Score** each finding (`security-reporting:cvss`) and rank.

# Output

A per-category table (category · applicable? · finding · severity · remediation)
plus a ranked top-risks list. Confirmed issues → `security-reporting:finding`.

# Notes

A01 Broken Access Control is the most prevalent category — give it explicit, tested
attention. Read `reference.md` for the per-category checklist. Stay within
authorized scope.
