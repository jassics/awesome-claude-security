---
name: guardrail-review
description: >-
  Review or design the content-safety guardrails of an AI system — input/output
  classifiers, refusal and safe-completion behavior, escalation/human handoff, and
  coverage across harm categories, languages, and modalities. Use when assessing or
  building the safety controls around a model.
---

# Goal

An assessment (or design) of the guardrail stack: what's blocked, how well, where
the gaps are, and whether it balances under- vs over-blocking.

# What to cover

1. **Input-side** — moderation/classification of prompts before the model; handling
   of disallowed and borderline requests; prompt-injection interaction (cross-ref
   `llm-security`).
2. **Output-side** — moderation of generations before they reach the user or
   downstream systems; safe-completion vs hard refusal; PII/sensitive-data filters.
3. **Refusal behavior** — are refusals correct, consistent, and helpful (offer safe
   alternatives)? Measure over-refusal of benign requests, not just under-refusal.
4. **Coverage** — across all harm categories from `harm-modeling`, across
   **languages**, and across **modalities** (image/audio/doc — cross-ref
   `multimodal-security`). Gaps usually hide in non-English and non-text.
5. **Escalation & oversight** — human-in-the-loop for high-stakes/uncertain cases;
   user reporting; appeal/override paths.
6. **Robustness & monitoring** — do guardrails hold under adversarial pressure
   (`safety-red-team`)? Is there logging, drift monitoring, and an update process?

# Steps

1. Inventory the existing guardrails (or requirements, if designing).
2. Assess each area above; for gaps note severity and the harm category exposed.
3. Check the under-/over-blocking balance with representative benign + unsafe sets.
4. Recommend concrete improvements and a layered (defense-in-depth) design.

# Output

A guardrail review: layer · coverage · gaps · severity · recommendation, plus a
target layered design. Validate changes with `safety-evaluation` and
`safety-red-team`.

# Notes

Guardrails are defense-in-depth, not a single classifier — combine input, output,
refusal, escalation, and monitoring. The two most common gaps: non-English/
non-text coverage, and over-refusal that quietly breaks legitimate use.
