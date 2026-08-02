# genai-eval-gates template

A ready-to-copy **enforcement** layer for LLM/agent releases — the GenAI
equivalent of [`../security-gates/`](../security-gates/README.md). Where that
template gates commits/deploys on SAST/SCA/secrets/IaC findings, this one gates
releases on **safety-eval and prompt-injection regressions**, so "safe before
it ships" is an actual CI check, not just a one-off eval report someone read once.

This is a **consumer template** — for a project *using* this marketplace's
guidance, not for authoring a plugin (see `../plugin-template/` for that).

## What's in here

| File | Purpose |
| --- | --- |
| `promptfoo.config.yaml` | Eval/regression test-set skeleton: refusal, over-refusal, prompt-injection resistance. |
| `.github/workflows/genai-eval-gate.yml` | CI-time gate: runs the eval set + an adversarial probe pass, fails on regression vs. baseline. |
| `EVAL-GATE-NOTES.md` | What counts as a "regression," burn-in rollout, and an exceptions/waiver format. |

## Tools wired in

- **[promptfoo](https://github.com/promptfoo/promptfoo)** — LLM eval/regression testing with assertion-based test cases, CI-friendly config and exit codes, and built-in red-team/adversarial test generation.
- **[garak](https://github.com/NVIDIA/garak)** — NVIDIA's open-source LLM vulnerability scanner: automated probes for prompt injection, jailbreak, data leakage, and other known failure classes.

Both tools' CLIs and flags evolve — treat the exact commands/flags below as a
starting skeleton, not a permanently-correct reference. Check each tool's current
docs before relying on a specific flag in a blocking gate.

## Install

```bash
cp templates/genai-eval-gates/promptfoo.config.yaml <your-repo>/promptfoo.config.yaml
cp -r templates/genai-eval-gates/.github <your-repo>/.github
```

Then, in `<your-repo>`:

1. Point the `providers` section in `promptfoo.config.yaml` at your actual
   model/endpoint (it ships with a generic placeholder provider).
2. Build out the `tests` section — the three cases shipped here (refusal,
   over-refusal, injection-resistance) are illustrative, not a real eval suite.
   Derive the real test set from `ai-safety:safety-evaluation`'s harm categories
   and `llm-security:prompt-injection-test`'s payload taxonomy.
3. Run `promptfoo eval` locally once to baseline the repo before enabling this
   as a blocking gate — see `EVAL-GATE-NOTES.md` for a report-only-first rollout.
4. Install `garak` (`pip install garak`) and confirm it can reach your target
   endpoint/provider before wiring the CI job.

## Mapping back to marketplace skills

A finding this gate flags is the start of triage, not the end:

- Eval-set design, harm categories, rubrics, thresholds → `ai-safety:safety-evaluation`.
- Deeper adversarial/jailbreak work beyond garak's automated probes → `ai-safety:safety-red-team`.
- The injection payload taxonomy behind the injection-resistance test case → `llm-security:prompt-injection-test`.
- Turning this gate's live pass rate into a go/no-go release decision → `ai-safety-engineer:safety-case`.
- Operationalizing the rollout itself (baseline, burn-in, blocking) → `ai-safety-engineer:evals-ci-gate`.

## Tuning (avoid noise-driven bypass)

Same failure mode as `security-gates/`: a gate that blocks on every non-zero
finding gets disabled within a month. Fail on **regression against a committed
baseline**, not on absolute finding counts — see `EVAL-GATE-NOTES.md`.
