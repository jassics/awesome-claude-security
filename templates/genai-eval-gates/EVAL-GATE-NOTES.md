# Rolling out a GenAI eval gate without it getting bypassed

Same failure mode as `security-gates/SECURITY-GATE-NOTES.md`: a gate that blocks
on noise gets disabled, merged with the required check turned off, or ignored
within a month. This is the GenAI-specific version of that guidance.

## Define "regression" precisely, before turning on blocking

Don't gate on absolute finding counts (LLM outputs are non-deterministic —
some run-to-run variance is normal). Gate on:

- **Pass-rate drop beyond a tolerance** against the committed baseline (the
  workflow template uses a 2-point tolerance as a starting default — tune it).
- **Any newly-failing case in a fixed regression set** — a small, stable set of
  cases that should *always* pass (clear-cut refusal cases, clear-cut benign
  cases, known-injection patterns already fixed once). A regression here means
  something that used to work now doesn't — that's a real signal, not noise.

## Burn-in before blocking

1. **Weeks 1-2 — report only.** No `eval-baseline.json` committed yet, or the
   gate job set to advisory. Let the team see pass-rate variance and separate
   real regressions from eval-set flakiness (adjust rubrics/assertions that
   are themselves poorly worded before blocking on them).
2. **Weeks 3-4 — commit a baseline, tighten the eval set.** Fix any test cases
   that were ambiguous or wrong. Commit `eval-baseline.json` (the promptfoo
   output from a known-good run) so the gate has something to compare against.
3. **Week 5+ — make it blocking.** Mark the gate job as a required status
   check. Keep the garak adversarial-probe job advisory longer than the
   promptfoo regression job — it's exploratory/automated and noisier by nature.

## Version the eval set

Per `ai-safety:safety-evaluation`'s existing note: keep the test set versioned
(commit it, tag releases) so pass rates are comparable across model/prompt
changes over time, not just pass/fail at a point in time.

## Exceptions need an owner and an expiry

```yaml
# eval-exceptions.yaml
- case_id: injection-resistance-002
  reason: "Known model limitation on multi-turn injection; mitigation tracked separately, not blocking this release"
  owner: jane@example.com
  expires: 2026-06-30
- case_id: over-refusal-legal-advice-003
  reason: "Model intentionally over-refuses regulated legal-advice category pending compliance review"
  owner: john@example.com
  expires: 2026-09-30
```

An exception with no expiry is a permanent hole — review expiring exceptions on
a recurring cadence, same as `security-gates/SECURITY-GATE-NOTES.md`'s pattern.

## This gate feeds a decision, it isn't the decision

A passing gate is evidence, not a safety case on its own. Wire the gate's live
pass rate into `ai-safety-engineer:safety-case` for the actual go/no-go release
argument — a gate that's green because the eval set is stale is worse than an
honest red.
