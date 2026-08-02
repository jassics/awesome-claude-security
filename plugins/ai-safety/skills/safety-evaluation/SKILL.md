---
name: safety-evaluation
description: >-
  Design and run a safety evaluation suite for an AI model or feature across harm
  categories — refusals on disallowed content, robustness, over-refusal vs
  helpfulness, groundedness/truthfulness — with rubrics and pass/fail thresholds.
  Use to measure an AI system's safety, establish a baseline, or gate a release.
---

# Goal

A repeatable safety eval: a structured test set across harm categories, clear
grading rubrics, measured pass rates, and a report that supports a release/no-release
decision and tracks regression over time.

# What to evaluate (cover both failure directions)

- **Under-refusal (unsafe)** — does it produce disallowed/harmful content across
  the harm categories from `harm-modeling`? (toxicity, dangerous instructions,
  self-harm, illegal facilitation, hate, sexual content involving minors, etc.)
- **Over-refusal (unhelpful)** — does it wrongly refuse benign requests? Safety
  that destroys utility is its own failure; measure both.
- **Robustness** — does safety hold under paraphrase, role-play, multilingual,
  encoded, and multi-turn pressure? (Deeper adversarial work: `safety-red-team`.)
- **Groundedness / truthfulness** — for factual/high-stakes tasks, are answers
  correct and properly hedged/cited? (RAG groundedness: see `rag-security`.)
- **Bias** — disparate quality/refusal across groups (full analysis:
  `bias-fairness-assessment`).

# Steps

1. Derive harm categories and high-stakes scenarios from `harm-modeling`.
2. Build/select a test set per category: clearly-unsafe, benign-but-sensitive
   (over-refusal probes), and borderline cases. Note provenance; keep prompts
   non-operational (don't author working harmful artifacts).
3. Define a **rubric** per category (what a pass vs fail looks like) and a grading
   method (human, model-graded with spot checks, or known-answer).
4. Run, score, and compute pass rates with thresholds per category.
5. Report results, failures with examples, trends vs prior runs, and gaps.

# Output

A safety eval report: per-category pass rate vs threshold, notable failures
(redacted), over- vs under-refusal balance, and prioritized fixes. To make this a
durable, enforced release gate rather than a one-off report, install
`templates/genai-eval-gates/` (ready-to-copy promptfoo/garak CI workflow) and see
`ai-safety-engineer:evals-ci-gate` for rolling it out. Use
`security-diagramming:infographic` for a scorecard and `security-reporting` for
the writeup.

# Notes

Measure both safety **and** helpfulness — a model that refuses everything scores
"safe" but is useless. Keep the eval set versioned so results are comparable across
releases. Don't include genuinely operational harmful content in the test set;
probe the boundary, not the payload.
