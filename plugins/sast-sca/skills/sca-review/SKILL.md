---
name: sca-review
description: >-
  Analyze a project's dependencies (software composition analysis): generate/inspect
  an SBOM, find known-vulnerable and risky components, and prioritize upgrades. Use
  when reviewing third-party/open-source risk in a codebase or build.
---

# Goal

A prioritized dependency-risk view: which components are vulnerable or risky, how
reachable/exploitable they are, and the upgrade path — backed by an SBOM.

# Steps

1. **Inventory** — generate or ingest an **SBOM** (e.g. CycloneDX/SPDX) covering
   direct and transitive dependencies; capture versions and licenses.
2. **Match vulnerabilities** — map components to known advisories (CVE/GHSA/OSV).
   Record severity and whether a fixed version exists.
3. **Assess reachability/exploitability** — is the vulnerable function actually used?
   Prefer reachability over raw CVE counts to cut noise. Note runtime vs. build-only
   and dev-only dependencies.
4. **Check hygiene** — unmaintained/abandoned packages, suspicious or typosquatted
   names, integrity/provenance (lockfiles, signing), and risky licenses.
5. **Prioritize remediation** — reachable + high-severity + fix-available first;
   plan upgrades and watch for breaking changes.

# Output

A prioritized table: component · version · advisory · severity · reachable? ·
fixed-version · action, plus the SBOM and a short upgrade plan. Confirmed issues →
`security-reporting:finding` (maps to OWASP A06 / API-adjacent supply-chain risk).

# Notes

Rank by reachability and exploitability, not CVE count — most flagged CVEs aren't
reachable. Don't ignore transitive deps (where most real risk hides) or unmaintained
packages (a risk even without a current CVE). For deeper provenance/SLSA/signing,
see `supply-chain-security` (roadmap).
