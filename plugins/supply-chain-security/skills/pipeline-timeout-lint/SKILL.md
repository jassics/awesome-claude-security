---
name: pipeline-timeout-lint
description: >-
  Check GitHub Actions workflows for the two runaway-risk controls that have
  no safe platform default — a job with no `timeout-minutes`, and a workflow
  with no `concurrency` group. Use when authoring or reviewing a
  `.github/workflows/*.yml` file, before merging a new/changed pipeline, or
  when asked "will this pipeline run forever", "does this workflow have a
  timeout", or "check my CI config for runaway risk". Narrower and faster
  than the full `pipeline-integrity-review` audit (which covers supply-chain
  tampering, not resource/cost exhaustion) — drives a small bundled script,
  no external tool required beyond PyYAML.
---

# Goal

Catch the CI/CD equivalent of a missing `maxTurns`: a pipeline job or run
that can consume runner-minutes indefinitely because nothing bounds it, and
confirm every workflow you author (or are reviewing) sets an explicit,
tighter-than-default bound before it merges.

# Why this matters

On a GitHub-hosted runner, a job with no `timeout-minutes` still falls back
to the platform's hard 360-minute (6h) ceiling — generous, but bounded. On a
self-hosted runner (or a custom runner-group label), that ceiling does **not**
apply — the only remaining bound is the whole workflow run's absolute
72-hour maximum, which is practically unbounded for most workflows. Separately,
a workflow with no top-level `concurrency` key lets GitHub run **unlimited**
concurrent/duplicate runs for the same ref — a rapid sequence of pushes, or a
`workflow_dispatch` storm, piles up runner-minutes (and, on paid runners,
cost) with nothing to dedupe or cancel earlier, now-stale runs.

# Steps

1. **Ensure PyYAML is available** — `python3 -c "import yaml"`. It's a very
   common transitive dependency (most DevOps tooling pulls it in); install
   with `pip install pyyaml` if missing. The script fails open (exit 2, does
   not block) if it's absent, rather than crashing a caller.
2. **Run the linter** from the repo root (it discovers
   `.github/workflows/*.yml`/`*.yaml` itself; or pass specific file paths):
   ```
   python3 <plugin-root>/scripts/pipeline-timeout-lint.py
   ```
3. **Read each finding.** Severity is baked into the message itself:
   - `HIGH` — a job runs on a non-hosted/self-hosted-labeled runner with no
     `timeout-minutes`. This is the real "practically unbounded" case (up to
     72h), fix first.
   - `MEDIUM` — the workflow has no `concurrency` group.
   - `LOW` — a job on a standard hosted runner (`ubuntu-*`/`windows-*`/
     `macos-*`) has no `timeout-minutes`. Already hard-capped at 6h
     platform-wide, so this is a tightening/hygiene nudge, not an unbounded-run
     risk.
4. **Fix**: add `timeout-minutes: N` to each job, sized to what the job
   actually does (a lint/test job rarely needs more than 10–30 minutes; a
   build/deploy job may need more, but should still be an explicit, reasoned
   number, not silence). Add a `concurrency` block, typically:
   ```yaml
   concurrency:
     group: ${{ github.workflow }}-${{ github.ref }}
     cancel-in-progress: true
   ```
5. **Re-run the linter** to confirm clean, then continue with the full
   `pipeline-integrity-review` audit before merging a new/changed pipeline —
   this skill only covers the resource/cost-exhaustion slice, not PPE,
   secrets, runner trust, or pinning.

# Output

A short pass/fail per workflow file/job: clean, or file + job + severity +
the fix to apply. Not a full report — for pipeline tampering/trust risk use
`pipeline-integrity-review`.

# Notes

- GitLab CI, CircleCI, and other CI systems are out of scope for v1 — GitHub
  Actions was chosen first because its default (a 6h ceiling that silently
  stops applying on self-hosted runners) is the clearest instance of the
  "looks harmless, isn't" pattern this skill targets.
- This is a small bundled script (`scripts/pipeline-timeout-lint.py`), not an
  external tool invocation — it parses workflow YAML as data only and never
  executes anything in it.
- Pairs with `claude-config-security:agent-safety-lint` (same pattern applied
  to Claude Code agent/hook/MCP config instead of CI pipelines) and
  `agentic-ai-security:agent-harness-review` (iteration/budget caps for
  agents you build, a different execution surface entirely).
