---
name: harm-modeling
description: >-
  Systematically enumerate the potential HARMS of an AI system — to users, third
  parties, vulnerable groups, and society — under normal use, misuse, and
  malfunction, then rank them and map mitigations. This is the AI-safety analog of
  threat modeling (which targets attackers). Use when designing or reviewing an AI
  feature for safety, not security.
---

# Goal

A harm model: who could be harmed, how, under what conditions, how badly, and what
reduces it — the safety counterpart to a security threat model.

# How this differs from threat modeling

- **Threat modeling** (`threat-modeling:stride`) asks *how could an attacker
  compromise the system?* The actor is adversarial.
- **Harm modeling** asks *how could the system harm people even with no attacker?*
  via normal use, foreseeable misuse, malfunction, bias, or over-reliance.
  Use both for a complete picture.

# Steps

1. **Define the system & context** — purpose, users (including vulnerable
   populations: minors, patients, at-risk groups), deployment context, and the
   stakes of the decisions it influences.
2. **Identify stakeholders** — direct users, non-user subjects (people the output
   is *about*), bystanders/third parties, and society at large.
3. **Enumerate harm categories** (see `reference.md`): physical, psychological,
   financial, discrimination/unfairness, privacy/dignity, misinformation,
   manipulation/autonomy, societal/democratic, environmental, and dangerous-
   capability/misuse harms.
4. **For each plausible harm, capture the condition**: normal use, foreseeable
   misuse, malfunction/error (hallucination, failure), distribution shift, or
   feedback effects at scale. Note *who* is harmed and how severe/irreversible.
5. **Rate** severity × likelihood × affected-population (weight irreversible and
   vulnerable-group harms up). Reuse `threat-modeling:risk-rank` scoring.
6. **Map mitigations** — design changes, guardrails, evals, human oversight,
   disclosures, usage policy, monitoring — and note residual harm.

# Output

A harm-model table: stakeholder · harm category · condition · severity ·
likelihood · affected group · mitigation · residual. Plus a top-harms summary and
recommended safeguards. Use `security-reporting` for the writeup and
`security-diagramming` to map harm pathways.

# Notes

Always include foreseeable **misuse** and **malfunction**, not just intended use —
most real-world AI harms come from those. Give extra weight to harms that are
irreversible or fall on people who can't opt out.
