---
name: dependency-supply-chain-review
description: >-
  Review third-party dependencies for supply-chain trust risk — typosquatting,
  dependency confusion, maintainer/abandonment risk, unpinned versions, and
  malicious install scripts — not just known-CVE counts. Use when assessing how
  much a project trusts code it didn't write, or vetting a new dependency.
---

# Goal

A trust assessment of the dependency graph: which packages could become an attack
path, and the controls (pinning, allowlists, verification) that close them. This is
about **provenance and trust**, complementing the known-CVE scanning in `sast-sca`.

# What to look for

- **Typosquatting / brandjacking** — names a character off from popular packages,
  or impersonating an internal/well-known library.
- **Dependency confusion** — internal package names resolvable from public
  registries; scoping/namespace not reserved; public takes precedence over private.
- **Maintainer & health risk** — single maintainer, recently transferred ownership,
  abandoned/unmaintained, sudden new maintainer before a release, low download trust.
- **Install-time execution** — `postinstall`/build scripts, `setup.py` code, native
  build steps that run arbitrary code on `install`.
- **Pinning & integrity** — floating ranges vs. pinned versions; lockfile present and
  enforced; hash/integrity verification on install.
- **Transitive blast radius** — deep/risky transitive deps pulled by a trusted top
  level one.

# Steps

1. Inventory direct + transitive dependencies (ingest an SBOM or generate one —
   CycloneDX/SPDX).
2. Screen each against the risk patterns above; flag the install-script and
   confusion/typosquat cases first — those are active attack paths, not hygiene.
3. Check registry/namespace controls: are internal names reserved on public
   registries? Is a private-first resolver / allowlist enforced?
4. Recommend controls: pin + lockfile + integrity hashes, internal proxy/registry
   with allowlisting, scoped namespaces, and review gates for new dependencies.

# Output

A ranked findings list (package · risk type · evidence · blast radius · fix) plus
recommended org-level controls. Route CVE/version remediation to
`vulnerability-management`; formalize with `security-reporting`.

# Notes

The dangerous supply-chain attacks aren't "old CVE in a lib" — they're malicious
code shipped in a *legitimate* package (compromised maintainer, confusion, typo).
`sast-sca` answers "is this dependency vulnerable?"; this skill answers "should I
trust this dependency at all?"
