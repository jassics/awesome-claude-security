---
name: secure-architecture-maturity
description: >-
  Assess an architecture's control completeness against OWASP ASVS and an
  organization's security-practice maturity against OWASP SAMM. Use when a design
  review needs to state *how much* verification is enough (ASVS level) and whether
  secure-architecture practice is repeatable or one-off (SAMM maturity) — not just
  a single design's threats and controls.
---

# Goal

Two answers `security-design-review` doesn't give on its own: which **ASVS**
verification level this system must satisfy, and how mature the organization's
**SAMM** practice is at producing/verifying designs like it — so the review lands on
a defensible bar, not a vibe.

# What to assess

1. **ASVS level (system-specific)** — OWASP ASVS 5.0 defines three verification
   levels by asset criticality:
   - **L1** — opportunistic; low-risk, low-sensitivity apps; baseline hygiene only.
   - **L2** — standard; most business apps handling sensitive data (the default
     target for anything with auth, PII, or payments).
   - **L3** — high-value/high-assurance; safety-critical, high-value transactions,
     regulated data at scale, or systems where compromise is catastrophic.
   Pick the level from data sensitivity, user base, and blast radius — not from what's
   convenient to build. For requirement-level detail once the level is picked, use
   `security-knowledge:asvs-reference`; this skill only decides *which level applies*
   and *whether the architecture as designed can plausibly satisfy it*.
2. **SAMM maturity (organization-specific)** — OWASP SAMM v2 (formerly OpenSAMM,
   sometimes referenced as OSAMM) scores practice maturity 0–3 across five business
   functions: **Governance, Design, Implementation, Verification, Operations**. For
   architecture work, **Design** (threat assessment, security requirements, secure
   architecture) and **Verification** (architecture assessment, requirements-driven
   testing) are the relevant functions — score whether this review is a repeatable
   practice or a one-off favor.

# Steps

1. Classify the asset: data sensitivity, user population, financial/safety impact,
   regulatory exposure → target **ASVS level** (L1/L2/L3).
2. Walk the architecture against that level's chapters (auth, session, access
   control, input handling, cryptography, data protection, communications, API/web
   service — see `security-knowledge:asvs-reference`); list what's satisfied, what's
   gap, what's unverifiable from the design alone.
3. Separately, score current **SAMM** maturity (0–3) for the Design and Verification
   functions at minimum — is threat modeling/design review routine and gated, or did
   it happen only because someone asked this time? Add Governance/Implementation/
   Operations if in scope.
4. For each SAMM function below target, state the concrete next-level action (e.g.
   "Design 1→2: require a documented security requirements step before build starts
   on any L2+ system," not "improve design maturity").

# Output

Two artifacts:
- **ASVS gap table** — chapter · requirement area · status (met/gap/unverifiable) ·
  target level.
- **SAMM maturity scorecard** — business function · current level (0–3) · target
  level · next-maturity action.
Feed both into `security-design-review`'s recommendations and rank with
`threat-modeling:risk-rank`.

# Notes

Don't conflate the two: **ASVS** measures whether *this system's controls* are
complete enough for its criticality; **SAMM** measures whether *the organization's
process* that produced (and will re-verify) those controls is repeatable. A system
can pass an ASVS L2 check today and still sit inside a SAMM Design-maturity-0 org —
that's a real finding, not noise, because it predicts whether the next system built
this way will also need a rescue review.
