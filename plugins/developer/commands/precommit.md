---
description: Run the pre-commit security gate on the current changeset and report a single pass/fail verdict.
argument-hint: [optional: path/scope to check instead of the full diff]
---

Run the pre-commit security gate for: **$ARGUMENTS** (default: the current
staged/unstaged changeset).

1. **Scope** — `git status` / `git diff --cached` (fall back to `git diff` if
   nothing is staged) to find changed files. Stay scoped to the diff; this is a
   fast pre-commit check, not a full-repo audit.
2. **Run the gate** — `/developer:pre-commit-gate` to aggregate secret/gitignore
   hygiene, SAST/SCA on the diff, and (if relevant) IaC and Claude-config checks
   into one verdict.
3. **Report** — a single **BLOCK** or **PASS** line at the top, followed by the
   verdict table (check · result · blocking findings). On BLOCK, give the exact
   fix for each blocking finding, not just the diagnosis.

For deep, multi-step coordination beyond a single commit gate (e.g. reviewing a
whole new feature's security posture), hand off to the `developer` agent.
