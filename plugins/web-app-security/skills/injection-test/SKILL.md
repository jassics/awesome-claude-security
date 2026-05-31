---
name: injection-test
description: >-
  Test a web app for injection flaws — SQL/NoSQL, OS command, LDAP, template
  injection, and cross-site scripting (XSS). Use to validate OWASP A03 on an
  authorized target by probing where untrusted input reaches an interpreter or sink.
---

# Goal

Evidence on whether untrusted input can break out of data context into an
interpreter (DB, shell, template, browser DOM) — with reproducible, non-destructive
proof.

# Prerequisites

- Authorization to test. Keep payloads non-destructive (prove the flaw; don't drop
  tables or run harmful commands).

# Classes to test

1. **SQL / NoSQL injection** — error-based, boolean/time-based blind; check ORDER
   BY, auth bypass, JSON/operator injection for NoSQL.
2. **Cross-site scripting (XSS)** — reflected, stored, DOM-based; test HTML, attr,
   JS, and URL contexts; check the CSP.
3. **OS command injection** — input reaching shell calls; blind via timing/OOB.
4. **Template injection (SSTI)** — input rendered by a server-side template engine.
5. **LDAP / header / other interpreter injection** as applicable.

# Steps

1. Enumerate input → sink paths (params, headers, JSON, file names, stored fields).
2. Probe each with safe marker payloads; confirm the interpreter is reached
   (reflection, error, timing, OOB callback). Use non-destructive proofs.
3. Determine context to craft a minimal working PoC (e.g. the encoding XSS needs).
4. Record: class · location · context · PoC · evidence · impact.

# Output

A results table: class · parameter/sink · context · PoC · evidence · remediation
(parameterized queries, context-aware output encoding, allow-list validation, safe
templating/sandboxing, CSP). Confirmed issues → `security-reporting:finding`.

# Notes

Fixes are sink-specific: parameterize for SQL, encode-per-context for XSS, avoid
shell for commands, sandbox templates. Input validation alone is not a reliable
fix — pair it with safe output/interpreter handling. Keep all payloads benign.
