# Rolling out a security gate without it getting bypassed

A gate that blocks on noise gets `--no-verify`'d, merged with the required check
disabled, or quietly turned off within a month — that's worse than no gate at all.
This is the concrete version of `security-engineer:secure-pipeline`'s tuning notes.

## Fail closed only on reachable + high severity

- Block on: confirmed live secrets, HIGH/CRITICAL SAST findings in code that's
  actually reachable (not a dead code path), HIGH/CRITICAL CVEs with an available
  fix in a dependency actually exercised at runtime, IaC misconfigurations that are
  exploitable as deployed (not a finding on an unused example file).
- Warn (don't block) on: MEDIUM/LOW findings, unreachable/dead-code hits, CVEs
  with no fix version yet available, style/best-practice IaC findings.

## Burn-in before blocking

1. **Week 1-2 — report only.** Run every job with `continue-on-error: true` (CI)
   or as a non-blocking `pre-commit` stage. Let the team see volume and triage
   real vs. noise findings.
2. **Week 3-4 — tighten config.** Adjust each scanner's severity threshold, add
   justified suppressions (see exceptions format below), narrow file globs to
   what's actually relevant.
3. **Week 5+ — make it blocking.** Remove `continue-on-error`, mark the gate job
   as a required status check in branch protection.

## Exceptions need an owner and an expiry

An exception with no expiry is a permanent hole. Track them in a small file the
gate reads (adapt to your scanner's native suppression format where one exists —
e.g. `.semgrepignore` with inline `# nosemgrep: <rule-id>` comments, gitleaks
`.gitleaksignore`) plus a durable record of *why*:

```yaml
# security-exceptions.yaml
- id: CVE-2024-XXXXX
  component: some-transitive-dep@1.2.3
  reason: "No fix version yet upstream; not reachable from any external input path"
  owner: jane@example.com
  expires: 2026-09-30
- rule: semgrep.python.django.security.audit.raw-html-format.raw-html-format
  path: templates/admin_only_debug_view.py
  reason: "Admin-only, non-user-facing debug view; input is trusted internal config"
  owner: jane@example.com
  expires: 2026-06-30
```

Review expired/expiring exceptions on a recurring cadence (e.g. monthly) —
`vulnerability-management` in this marketplace covers the broader triage/SLA
process this feeds into.

## Keep it fast

- Pre-commit hooks should only scan **changed files** (most hooks do this by
  default) — a full-repo scan on every commit gets skipped by developers.
- Reserve full-repo/full-dependency-graph scans (SBOM generation, OSV-Scanner
  recursive) for CI, not the local pre-commit hook.
