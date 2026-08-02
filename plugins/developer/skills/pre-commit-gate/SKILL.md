---
name: pre-commit-gate
description: >-
  Aggregate a fast, diff-scoped security check before `git commit`/`git push` —
  secrets/gitignore hygiene, SAST/SCA on changed files, and IaC/Claude-config
  checks where relevant — into a single go/no-go verdict. Use before committing
  or pushing, not as a full-repo audit.
---

# Goal

A single **BLOCK** or **PASS** verdict on the current changeset, fast enough to
run before every commit — by aggregating existing scanning skills, not
reimplementing them.

# Steps

1. **Scope to the diff.** Use `git status` / `git diff --cached` (or `git diff`
   if nothing is staged yet) to get the changed-file list. Never widen to a
   full-repo scan here — that's what `sast-sca`/`infrastructure-security` are
   for on demand; this gate only exists because it's fast.
2. **Secrets & gitignore hygiene** — run `infrastructure-security:secrets-management-review`
   scoped to the changed files: hardcoded secrets in the diff, and the
   gitignore-hygiene check (sensitive paths like `.env`, keys, `.claude/`,
   `terraform.tfstate*` actually excluded, and not already tracked via
   `git ls-files`).
3. **SAST** — run `sast-sca:sast-review` on changed code files for unsafe
   methods/APIs, with the safe-pattern fix. For Python/React specifically, also
   note whether `secure-coding:safe-function-lint`'s curated rule pack (and its
   installed git hooks) already cover this changeset — if `secure-coding` isn't
   installed/enforced in this repo, flag that as a gap alongside the findings.
4. **SCA** — if a dependency manifest changed (`package.json`, `requirements.txt`,
   `go.mod`, `pom.xml`, lockfiles, etc.), run `sast-sca:sca-review` for
   outdated/vulnerable libraries and the safe version to move to.
5. **IaC** — if Terraform/CloudFormation/Kubernetes manifests changed, cross-ref
   `infrastructure-security:iac-security-review`.
6. **Claude/agent config** — if `.claude/`, `.mcp.json`, or an agent/skill
   definition changed, cross-ref `claude-config-security:config-security-scan`
   (a misconfigured AI-agent setup is itself an attack surface).
7. **Aggregate.** Any confirmed live secret, or any HIGH+ finding from the above
   → **BLOCK**. Everything else → **PASS with warnings** (list them, don't block).

# Output

Top line: **BLOCK** or **PASS**. Then a verdict table: check · result · blocking
findings (file:line · severity · fix). For BLOCK, give the exact fix per
finding, not just the diagnosis, so the developer can resolve it and re-run
immediately.

# Notes

This is deliberately a thin orchestrator over `sast-sca`, `infrastructure-security`,
and `claude-config-security` — it owns no scanning logic of its own. It's also
the diff-scoped, multi-language, Claude-session-only counterpart to
`secure-coding`'s narrower but *enforced* Python/React git hooks — install both;
this gate catches what the hooks don't cover (other languages, SCA, IaC), and
the hooks catch commits made outside a Claude Code session. Staying
scoped to the diff is the point: a gate that takes minutes gets skipped; a gate
that takes seconds gets run. For anything the diff-scoped pass can't catch
(architecture-level issues, cross-file trust boundaries), that's what a full
`security-architect:security-design-review` or `threat-modeling` pass is for —
this skill is the fast last line, not the only line.
