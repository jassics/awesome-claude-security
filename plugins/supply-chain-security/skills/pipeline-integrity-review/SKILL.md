---
name: pipeline-integrity-review
description: >-
  Review a CI/CD pipeline for supply-chain tampering risk — build isolation,
  runner/agent trust, secret exposure, mutable dependencies, and poisoned-pipeline
  (PPE) / unauthorized-workflow paths. Use when hardening GitHub Actions, GitLab CI,
  Jenkins, or similar against build-system compromise.
---

# Goal

A CI/CD pipeline that an attacker can't subvert to inject code or steal secrets —
mapped to recognized risks (OWASP Top 10 CI/CD Security Risks, SLSA build track).

# What to review

- **Poisoned Pipeline Execution (PPE)** — can a PR/fork or a config file in the repo
  cause attacker-controlled code to run in a privileged build? `pull_request_target`
  / auto-run on fork PRs with secrets is the classic hole.
- **Runner/agent trust** — shared/self-hosted runners reused across trust levels;
  ephemeral vs. persistent; can one job tamper with the next?
- **Secrets hygiene** — secrets scoped to least privilege, not exposed to fork PRs,
  not printed in logs; OIDC short-lived creds over long-lived tokens.
- **Mutable inputs** — actions/images pinned by digest (not floating tags); third-party
  actions reviewed; base images and toolchains pinned.
- **Identity & permissions** — default token permissions least-privilege; branch
  protection and required reviews; who can modify pipeline definitions.
- **Build isolation & provenance** — hermetic/isolated builds; provenance emitted
  (hand to `artifact-provenance-verification`).

# Steps

1. Map the pipeline: triggers, jobs, runners, secrets, external actions/images,
   deploy steps, and trust boundaries between them.
2. Walk each OWASP CI/CD risk and PPE/injection path; flag where untrusted input
   meets privileged execution or secrets.
3. Check pinning, token scope, runner isolation, and review gates.
4. Recommend fixes prioritized by exploitability (privileged code-exec paths first).

# Output

A findings list (risk · pipeline location · exploit path · fix) mapped to OWASP CI/CD
risks and the SLSA build track, plus quick wins (pin by digest, scope tokens, isolate
fork PRs). Formalize with `security-reporting`.

# Notes

The build system is production: it has the secrets and ships the code, so compromising
CI is often easier and higher-impact than compromising prod. Floating action/image
tags are silent supply-chain risk — pin by digest. `pull_request_target` with secrets
on fork PRs is the single most common critical CI finding.
