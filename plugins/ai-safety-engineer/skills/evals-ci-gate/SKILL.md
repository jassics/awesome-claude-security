---
name: evals-ci-gate
description: >-
  Operationalize a safety/prompt-injection eval suite into an enforced CI gate —
  not just a one-off report — using the ready-to-copy promptfoo/garak template,
  a regression baseline, and a burn-in rollout. Use when a safety eval already
  exists (or is being designed) and needs to actually block regressions on every
  release rather than being run manually once.
---

# Goal

A working, tuned CI gate that fails releases on a real safety/injection
regression — durable and enforced, not a stale one-time eval someone read once.

# Steps

1. **Pull in the test material.** Eval set, harm categories, and rubrics come
   from `ai-safety:safety-evaluation`; the prompt-injection payload taxonomy for
   the injection-resistance cases comes from `llm-security:prompt-injection-test`.
   This skill doesn't design the tests — it makes them an enforced gate.
2. **Install the gate.** Copy `templates/genai-eval-gates/` into the target repo
   (`promptfoo.config.yaml` + `.github/workflows/genai-eval-gate.yml`). Point the
   config's `providers` section at the real model/endpoint and replace the
   illustrative test cases with the real eval set from step 1.
3. **Establish the regression baseline.** Run the suite once, review results by
   hand, fix any ambiguous/poorly-worded rubrics, then commit the run as
   `eval-baseline.json` — every future run is compared against this, not against
   an absolute pass-rate target (LLM outputs have natural run-to-run variance).
4. **Roll out in report-only mode first**, then flip to blocking, per the
   burn-in stages in `templates/genai-eval-gates/EVAL-GATE-NOTES.md` — do not
   make this a required check on day one.
5. **Wire the decision, not just the number.** Point `ai-safety-engineer:safety-case`
   at this gate's *live* pass rate as ongoing evidence for its safety argument,
   instead of citing a stale one-time eval run.

# Output

A short description of the installed gate: what it blocks on (regression vs.
baseline, tolerance used), the current baseline's date/version, and which
rollout stage it's at (report-only / tightening / blocking).

# Notes

This is the operationalization step, not the test design — that lives in
`ai-safety:safety-evaluation` and `ai-safety:safety-red-team`. A gate that's
green because the eval set or baseline has gone stale is worse than an honest
red; keep the eval set versioned and revisit the baseline whenever the model,
prompt, or eval set changes meaningfully.
