---
name: example-skill
description: >-
  One or two sentences naming the SITUATION, INPUTS, and OUTCOME so Claude knows
  exactly when to fire this skill. This text is always in context — be specific
  but tight. Example: "Assess an API endpoint against the OWASP API Top 10 and
  produce a ranked findings table. Use when reviewing a REST/GraphQL API for
  authz, rate-limiting, or schema-abuse issues."
---

# Goal

State what "done" looks like in one line.

# Prerequisites

- Authorization to test/assess the target.
- Any inputs the user must provide (URL, repo, scope, credentials channel).

# Steps

1. Establish scope and gather inputs.
2. Work the methodology — reference the relevant framework by name (OWASP, MITRE
   ATT&CK, STRIDE, MASTG, CIS...). For long checklists, read `reference.md`.
3. Validate findings; remove false positives.
4. Rank by severity/risk.

# Output

Produce a concrete artifact and say its format here, e.g. a findings table with
columns: ID · Title · Severity · Evidence · Remediation. For reports or diagrams,
defer to `security-reporting` / `security-diagramming`.

# Notes

Keep framing defensive and authorized. Don't fabricate evidence.
