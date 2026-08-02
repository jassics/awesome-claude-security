# security-gates template

A ready-to-copy **enforcement** layer: a pre-commit config and a GitHub Actions
workflow that wire up the same open-source scanners this marketplace's skills
already name, so "secure before commit/deploy" is an actual gate — not just
review guidance.

This is a **consumer template** — for a project *using* the marketplace's
guidance, not for authoring a plugin (see `../plugin-template/` for that).

## What's in here

| File | Purpose |
| --- | --- |
| `.pre-commit-config.yaml` | Local, pre-commit-time gate: secrets, SAST, shell, Dockerfile, IaC. |
| `.github/workflows/security-gates.yml` | CI-time gate: secrets, SAST, SCA/dependencies, IaC — fails the build on HIGH/CRITICAL. |
| `SECURITY-GATE-NOTES.md` | How to tune severity thresholds and roll this out without it getting bypassed. |

## Install

```bash
cp templates/security-gates/.pre-commit-config.yaml <your-repo>/.pre-commit-config.yaml
cp -r templates/security-gates/.github <your-repo>/.github
```

Then, in `<your-repo>`:

1. **Pin every hook/action** to a specific tagged release — this template deliberately
   uses placeholder pins (`v<PIN_ME>`) rather than a hardcoded version that will go
   stale. Check each tool's releases page and pin to the current stable tag.
2. Install `pre-commit` (`pip install pre-commit` or `pipx install pre-commit`) and run
   `pre-commit install` to activate the local git hook.
3. Run `pre-commit run --all-files` once to baseline the repo before enabling it as a
   blocking gate — see `SECURITY-GATE-NOTES.md` for a warn-first rollout.
4. Adjust the `files:`/`exclude:` patterns per hook to your repo's actual layout
   (e.g. drop the Python/Dockerfile/IaC hooks entirely if none apply).

## Tools wired in

- **Secrets** — [gitleaks](https://github.com/gitleaks/gitleaks) (pre-commit + CI).
- **SAST** — [semgrep](https://github.com/semgrep/semgrep) (pre-commit + CI), plus
  [bandit](https://github.com/PyCQA/bandit) for Python-specific checks.
- **Shell** — [shellcheck](https://github.com/koalaman/shellcheck).
- **Dockerfile** — [hadolint](https://github.com/hadolint/hadolint).
- **IaC** — [checkov](https://github.com/bridgecrewio/checkov) (Terraform/CloudFormation/K8s manifests).
- **SCA / dependencies** — [OSV-Scanner](https://github.com/google/osv-scanner) (CI only —
  needs a full dependency graph, not a fast per-commit fit).

## Tuning severity (avoid noise-driven bypass)

Every scanner here supports a severity/confidence threshold. Start permissive
(report-only) and tighten — see `SECURITY-GATE-NOTES.md`. A gate that blocks on
every low-confidence or unreachable finding gets `--no-verify`'d or merged with
"required check" disabled within a month; that's worse than no gate.

## Mapping back to marketplace skills

A finding this gate flags is the start of triage, not the end:

- Secret hit → `infrastructure-security:secrets-management-review` (rotate/revoke,
  not just remove — see that skill's Notes on git history).
- SAST/semgrep/bandit hit → `sast-sca:sast-review` for the code-level fix and the
  secure pattern to prevent recurrence.
- OSV-Scanner hit → `sast-sca:sca-review` for reachability/fix-version guidance.
- Checkov/IaC hit → `infrastructure-security:iac-security-review`.
- If the repo itself ships Claude Code config (`.claude/`, `.mcp.json`, agents/skills)
  → `claude-config-security:config-security-scan` for that surface specifically
  (this gate does not scan Claude Code configuration).

For the full rationale behind *which* gates to run and how to design pipeline
hardening beyond scanning (supply-chain integrity, runner isolation, deploy gates),
see `security-engineer:secure-pipeline`.
