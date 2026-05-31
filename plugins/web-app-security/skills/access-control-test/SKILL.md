---
name: access-control-test
description: >-
  Test a web app's authorization: IDOR/BOLA, missing function-level access control,
  privilege escalation (horizontal and vertical), and forced browsing. Use to
  validate OWASP A01 on an authorized target — the most prevalent web risk.
---

# Goal

Evidence on whether the app enforces authorization server-side on every object and
function, tied to the authenticated user — or whether a user can reach data/actions
they shouldn't.

# Prerequisites

- Authorization to test, ideally two accounts at different privilege levels (User
  A, User B, and an admin) with identifiable resources.

# Test cases

1. **IDOR / BOLA (horizontal)** — as User A, manipulate object identifiers (IDs,
   UUIDs, filenames, GUIDs in URLs/bodies/JWT) to access User B's resources.
2. **Function-level (vertical)** — call admin/privileged endpoints as a normal
   user; check hidden/undocumented functions and HTTP-method overrides.
3. **Forced browsing** — request resources/pages not linked for your role.
4. **Privilege escalation** — tamper with role/tenant claims (JWT, cookies, hidden
   fields, mass-assignment) to elevate.
5. **Missing ownership checks on writes** — update/delete another user's object.

# Steps

1. Map roles and sensitive objects/functions.
2. Run cases as the lower-privilege identity; never use the higher account's
   session to "prove" access.
3. Record per case: enforced / leaked / action-performed, with request+response
   evidence (redact secrets).
4. Identify the gap: client-side-only checks, IDs trusted from the request, missing
   server-side ownership/role enforcement.

# Output

A results table: case · object/function · result · evidence · remediation
(deny-by-default, server-side authz tied to identity). Confirmed issues →
`security-reporting:finding` (rate high+ for cross-user data access).

# Notes

Authorization must be enforced on the **server**, per object and per function,
against the authenticated identity — never trust IDs, roles, or tenant hints from
the client. This is the same class as API `BOLA/BFLA` — see `api-security`.
