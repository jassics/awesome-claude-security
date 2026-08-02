---
name: asvs-reference
description: >-
  Look up the right OWASP ASVS (Application Security Verification Standard) v5.0
  chapter and verification level (L1/L2/L3) for a control, requirement, or finding.
  Use when a design review, secure-code review, or pentest finding needs a
  consistent ASVS citation, or when scoping how deep a verification effort should go.
---

# Goal

The correct ASVS chapter/requirement and verification level for a control or
finding, cited consistently — so design reviews, secure-code reviews, and audits
anchor to the same standard.

# Steps

1. **Pick the verification level** by asset risk tier:
   - **L1** — opportunistic/low-assurance apps; baseline controls only, testable
     via black-box/automated checks.
   - **L2** — most applications handling sensitive data (the default target for
     most business apps).
   - **L3** — high-value, high-assurance apps (financial, healthcare, critical
     infra, regulatory mandate) — the full control set, deeper verification.
2. **Map the finding/control to the right ASVS chapter** — see `reference.md` for
   the chapter list. Cite the current ASVS chapter/requirement ID; don't hardcode a
   numbering you're not certain of — confirm against the live standard if precision
   matters (chapter numbering has shifted between ASVS editions).
3. **State the edition** — target **ASVS v5.0**; older reviews may cite v4.0.3,
   note the version if mixing.
4. **Hand off appropriately** — ASVS gives the control catalog; `security-architect:
   security-design-review` and `security-architect:secure-architecture-maturity` use
   it for design-time verification depth, `web-app-security`/`api-security` use it
   during testing.

# Output

Chapter/requirement + verification level (L1/L2/L3) + one-line rationale for the
level chosen. For control-maturity framing beyond a single finding, see
`security-architect:secure-architecture-maturity` (SAMM).

# Notes

ASVS is a **verification checklist**, not a maturity model — for "how mature is our
security program" use OWASP SAMM instead (see `security-architect:
secure-architecture-maturity`). Don't over-cite L3 requirements against an L1 asset;
match level to actual risk. See `reference.md` for the chapter table and level
criteria.
