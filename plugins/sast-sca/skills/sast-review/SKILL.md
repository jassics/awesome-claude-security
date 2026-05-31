---
name: sast-review
description: >-
  Run or ingest static application security testing (SAST) results on a codebase,
  triage them to remove false positives, and confirm the real issues with code
  evidence and remediation. Use when reviewing source code for security flaws or
  cleaning up noisy scanner output.
---

# Goal

A triaged SAST finding set: confirmed, code-evidenced issues mapped to CWE and
ranked — with the false positives filtered out.

# Steps

1. **Scope & scan** — identify languages/frameworks; run an appropriate SAST tool
   (e.g. Semgrep/CodeQL or the project's configured scanner), or ingest existing
   results. Note coverage and any excluded paths.
2. **Triage each finding** — open the flagged code and trace data flow from source
   (untrusted input) to sink. Classify: true positive / false positive / needs
   runtime confirmation. Watch for sanitizers/validation the tool missed.
3. **Confirm impact** — for true positives, identify the vulnerability class (CWE),
   reachability, and exploitability; mark which need dynamic confirmation
   (`web-app-security` / `api-security`).
4. **Score & rank** — severity (`security-reporting:cvss`) weighted by reachability;
   prioritize reachable, high-impact issues.
5. **Remediate** — give the specific code-level fix (parameterize, encode, validate,
   safe API) — and a secure pattern to prevent recurrence.

# Output

A triaged findings table: id · CWE · file:line · class · reachability · TP/FP ·
severity · remediation. Confirmed issues → `security-reporting:finding`.

# Notes

SAST is high-recall, low-precision — the value you add is triage. Always trace
source→sink before accepting a finding, and flag what needs dynamic confirmation
rather than over-claiming. Tune rules to cut recurring false positives.
