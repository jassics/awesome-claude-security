# Reference: OWASP API Security Top 10 (2023)

Checks and fixes for `owasp-api-top10`. Verify against the current OWASP API list.

| ID | Category | Look for | Fix |
| --- | --- | --- | --- |
| API1 | Broken Object Level Authorization (BOLA) | Object IDs in requests not checked against the caller's ownership. | Per-object authz on every access, tied to identity. (`api-authz-test`) |
| API2 | Broken Authentication | Weak/again-usable tokens, no expiry, credential stuffing, JWT flaws. | Strong auth, short-lived/rotated tokens, MFA, validate signatures/claims. |
| API3 | Broken Object Property Level Auth (BOPLA) | Mass assignment; over-exposed response fields. | Allow-list readable/writable fields; per-property authz; minimal responses. |
| API4 | Unrestricted Resource Consumption | No rate/size/pagination limits; expensive queries; cost abuse. | Rate limits, quotas, pagination, query cost limits, timeouts. |
| API5 | Broken Function Level Authorization (BFLA) | Admin/privileged operations callable by lower roles; method swap. | Deny-by-default function authz per role. (`api-authz-test`) |
| API6 | Unrestricted Access to Sensitive Business Flows | Automatable abuse of business flows (purchase, signup, vote). | Bot/abuse protection, throttling, business-logic limits. |
| API7 | Server-Side Request Forgery | Server fetches client-supplied URLs; metadata reachable. | Allow-list egress; validate URLs; block internal ranges/metadata. |
| API8 | Security Misconfiguration | Verbose errors, missing headers, permissive CORS, defaults. | Hardening baselines, least functionality, strict CORS, security headers. |
| API9 | Improper Inventory Management | Shadow/zombie endpoints, old versions, undocumented APIs, exposed non-prod. | API inventory; retire old versions; environment separation; docs. |
| API10 | Unsafe Consumption of APIs | Blindly trusting third-party API data; injection via upstream. | Validate/sanitize upstream responses; least trust; timeouts. |

## GraphQL extras

Introspection exposure, deeply nested/recursive queries (DoS), batching/aliasing
abuse, field-level authorization gaps. Fix: disable introspection in prod, depth/
complexity limits, per-field authz, rate limiting.
