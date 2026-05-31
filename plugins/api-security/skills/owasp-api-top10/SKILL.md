---
name: owasp-api-top10
description: >-
  Assess a REST or GraphQL API against the OWASP API Security Top 10 (2023),
  producing a per-category finding set with severity and remediation. Use when
  reviewing or pentesting an API. Authorized testing only.
---

# Goal

A structured assessment across the ten OWASP API categories, each with
applicability, evidence, severity, and remediation.

# Steps

1. **Map the API** — endpoints/operations, auth model, object model, roles, and
   sensitive business flows. Use the spec (OpenAPI/GraphQL schema) if available.
2. **Walk each category** (see `reference.md`):
   API1 Broken Object Level Authorization (BOLA) · API2 Broken Authentication ·
   API3 Broken Object Property Level Authorization (BOPLA) · API4 Unrestricted
   Resource Consumption · API5 Broken Function Level Authorization (BFLA) ·
   API6 Unrestricted Access to Sensitive Business Flows · API7 SSRF ·
   API8 Security Misconfiguration · API9 Improper Inventory Management ·
   API10 Unsafe Consumption of APIs.
3. **Substantiate** the authorization categories with `api-authz-test`.
4. **Score** (`security-reporting:cvss`) and rank.

# Output

A per-category table (category · applicable? · finding · severity · remediation)
plus ranked top risks. Confirmed issues → `security-reporting:finding`.

# Notes

Authorization failures (API1 BOLA, API5 BFLA, API3 BOPLA) dominate real-world API
breaches — test them directly, don't infer. Improper inventory (API9: shadow/zombie
endpoints, undocumented versions) is a common blind spot. Read `reference.md`.
