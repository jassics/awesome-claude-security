---
name: finding
description: >-
  Write up a single security finding in a consistent, actionable format:
  title, severity (CVSS), affected assets, evidence, impact, reproduction, and
  remediation. Use whenever you've identified one issue and need it documented
  for a report or ticket.
---

# Goal

One self-contained, defensible finding that an engineer can act on and a reviewer
can verify.

# Required structure

```
## <ID> — <concise title>
- Severity: <Critical/High/Medium/Low/Info>  (CVSS 4.0: <score> <vector>)
- Affected: <assets / endpoints / components>
- Status: Open

### Summary
One or two sentences: what the issue is and why it matters.

### Evidence
Request/response, code excerpt, screenshot ref, log line, or command output.
Redact secrets. Make it reproducible.

### Impact
What an attacker achieves; tie to confidentiality/integrity/availability and to
business consequence.

### Reproduction
Numbered, minimal steps to observe the issue.

### Remediation
Specific, testable fix(es). Prefer the durable root-cause fix; note interim
mitigations. Link references (OWASP/CWE/vendor docs).

### References
CWE-XXX, OWASP item, advisories.
```

# Steps

1. Confirm severity via `/security-reporting:cvss` (don't eyeball it).
2. Map to a **CWE** and the relevant framework item (OWASP Top 10 / API / LLM,
   ATT&CK technique) — improves triage and dedup.
3. Ensure evidence is reproducible and secrets are redacted.
4. Write remediation that is specific enough to be tested as "fixed".

# Output

The finding in the structure above (Markdown). Keep one finding per issue so it
can be ticketed independently and rolled into `pentest-report`.
