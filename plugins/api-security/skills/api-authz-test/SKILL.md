---
name: api-authz-test
description: >-
  Test an API's authorization — BOLA (object-level), BFLA (function-level), and
  BOPLA (property-level / mass assignment) — to confirm each request is authorized
  for the caller. Use to validate the top OWASP API risks on an authorized target.
---

# Goal

Evidence on whether the API enforces authorization server-side for every object,
function, and property against the authenticated caller — or whether a user can
reach data/operations/fields they shouldn't.

# Prerequisites

- Authorization to test, ideally two users at different privilege/tenant levels and
  an admin, with identifiable objects.

# Test cases

1. **BOLA (object level)** — as User A, swap object identifiers (path/query/body,
   IDs, UUIDs, GraphQL node IDs) to read or modify User B's objects.
2. **BFLA (function level)** — call admin/privileged operations as a normal user;
   try alternate methods/verbs, hidden endpoints, and GraphQL mutations not exposed
   to your role.
3. **BOPLA / mass assignment** — add privileged properties to a write (e.g.
   `"role":"admin"`, `"isVerified":true`) and check if they're accepted; inspect
   responses for over-exposed fields.
4. **Tenant isolation** — cross-tenant object access where multi-tenant.

# Steps

1. Map objects, operations, roles, and the property model (use the schema/spec).
2. Run cases as the lower-privilege identity; capture request+response evidence.
3. Record per case: enforced / leaked / accepted, with evidence (redact secrets).
4. Identify the gap: ID trusted from request, no per-object/function/property authz,
   writable fields not allow-listed.

# Output

A results table: case · object/function/property · result · evidence · remediation
(deny-by-default authz per object/function/property tied to identity; field
allow-listing). Confirmed issues → `security-reporting:finding` (high+ for
cross-user/tenant access).

# Notes

BOLA + BFLA are the #1 and #5 API risks and cause most API breaches. Authorization
must be enforced server-side per request — never infer it from the client-supplied
ID, role, or tenant. Same class as web `access-control-test`.
