---
name: secure-review
description: >-
  Manual, adversarial secure code review focused on exploitable vulnerabilities —
  OWASP Top 10, injection, authn/authz, business-logic abuse, crypto, SSRF,
  deserialization, secrets, race conditions. Reviews the current git diff by
  default, or a path/PR. Supports phase-scoped commands (auth, bizlogic,
  injection, headers, pii, deadcode, all) and poc/fix/chain/triage follow-ups.
  Complements `sast-review` (scanner triage) with human-style reasoning over
  the full change, especially business-logic flaws scanners can't see.
---

# Goal

An adversarial, code-evidenced vulnerability review of a diff/path/PR — including
business-logic abuse a scanner would miss — ranked by severity with concrete fixes.

# Phase commands

If invoked with an argument, run only that phase against the scoped code:

| Command | Scope |
|---|---|
| `auth` | Authn/session + authz/IDOR |
| `bizlogic` | Business-logic abuse — see `reference.md` |
| `injection` | Injection + input validation |
| `headers` | Security headers & transport (CSP/HSTS/CORS/TLS) |
| `pii` | Sensitive-data/PII handling |
| `deadcode` | Orphan endpoints, debug routes, stale API versions |
| `all` | Full flow below |
| `poc <FINDING-ID>` | Burp + Postman repro steps for a prior finding |
| `fix <FINDING-ID>` | Concrete code fix for a prior finding |
| `chain` | Findings that combine into a higher-severity exploit chain |
| `triage` | Re-rank existing findings by business impact × exploitability |

Cloud/IaC misconfig and structural secure-by-design architecture review are out of
scope here — hand off to `infrastructure-security:iac-security-review` /
`host-hardening-review` and `security-architect:security-design-review`.

# Steps

1. **Scope the change.**
   ```bash
   git diff --stat 2>/dev/null && git diff 2>/dev/null   # default: working changes
   # or: git diff main...HEAD   for a branch/PR
   ```
   If given a path, review that path. Read surrounding code for context, not just diff hunks.

2. **Interactive intake — only for business-critical flows** (checkout, payment,
   KYC, order/refund, auth, admin actions) or when no context has been given yet.
   Ask in one batch, wait for answers, then proceed; skip silently for small/
   non-critical diffs:
   - What does this flow do, and which user roles can reach it?
   - Primary threat actor (external attacker, malicious authenticated user, insider, bot)?
   - Sensitive data types involved (PII/PCI/health/credentials)?
   - Blast radius if this is compromised?

3. **Review against the checklist** — for every function, ask "how would I abuse this?":
   - **Injection**: SQL/NoSQL/command/LDAP/template; unsanitized input reaching a sink.
   - **AuthN/AuthZ**: missing checks, IDOR, broken access control, privilege escalation, mass assignment.
   - **Business-logic abuse** (highest priority for critical flows): step-skipping,
     client-controlled state tampering, replay, TOCTOU races (double-spend, coupon
     reuse, negative inventory), price/quantity/discount tampering, quota/rate-limit
     bypass, self-approval/workflow abuse. Full checklist + abuse-scenario template
     in `reference.md`.
   - **Secrets/crypto**: hardcoded secrets, weak/re-rolled crypto, bad randomness,
     secrets in logs (`secure-coding:secret-guard`).
   - **SSRF / path traversal / open redirect / file upload.**
   - **Deserialization / unsafe reflection / pickle/yaml.load.**
   - **Input validation & output encoding** (XSS), CSRF.
   - **Security headers/transport**: CSP, HSTS, X-Frame-Options, CORS
     wildcard+credentials, TLS version — only on endpoint/middleware config changes.
   - **PII/sensitive data**: logged PII, over-fetching in API responses, PII in
     URLs/analytics, masking in lower envs — only on data-model/logging/serialization changes.
   - **Race conditions / TOCTOU, resource exhaustion / DoS.**
   - **Dependency & supply-chain risk** introduced by the change (`sca-review`).
   - **Logging/observability**: are security events (login, password reset, role
     change, admin action) logged with actor/outcome; error handling that leaks internals.
   - **Orphan/dead code**: debug endpoints, old API versions still reachable,
     commented-out auth-bypass logic — only on routing/controller changes.

4. **Cross-check with tools where useful**: suggest or run `sast-review`,
   `sca-review`, `secure-coding:secret-guard`, `secure-coding:safe-function-lint`
   on the touched files.

# Output

- Findings ordered by severity (Critical/High/Medium/Low), each with `file:line`
  and the exploit/abuse scenario, formatted as a before/after code pair:

  ```
  **Vulnerable** (`file:line`):
  ```<lang>
  <exact vulnerable snippet from the diff/file>
  ```
  **Fixed:**
  ```<lang>
  <minimal corrected snippet — same shape, only the fix changed>
  ```
  ```
  Keep both snippets minimal (just the vulnerable statement + immediate
  context, not the whole function) so the diff is obvious at a glance.
- For business-logic findings, use the abuse-scenario format in `reference.md`
  (actor, goal, steps, business impact).
- Score meaningful findings with CVSS via `security-reporting:cvss` rather than a guessed label.
- On `poc <ID>`, add Burp Suite and Postman repro steps — template in `reference.md`.
- Distinguish confirmed issues from things to verify — if unsure, say "likely
  vulnerable — please confirm: does X happen?" rather than filing it as confirmed.
- A short go/no-go recommendation for merging the change.
- For a full multi-finding review, close with a quick-win vs. long-term-fix table
  (Finding ID | Effort | Priority | Owner) and hand off to
  `security-reporting:finding` / `security-reporting:pentest-report` for a formal writeup.
- Only apply fixes if the user explicitly asks.
