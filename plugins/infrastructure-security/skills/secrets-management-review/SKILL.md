---
name: secrets-management-review
description: >-
  Review how secrets are handled across code, IaC, CI/CD, containers, and config —
  hardcoding, sprawl, exposure, vaulting, rotation, and access scope. Use to assess
  secrets hygiene for a project or environment and find exposed credentials.
---

# Goal

An assessment of secrets handling: where secrets are exposed or poorly managed, and
a path to centralized, least-privilege, rotated secrets.

# What to review

1. **Hardcoded secrets** — passwords/API keys/tokens/private keys in source, IaC
   variables/state, container images, config files, or scripts. (Scan history too:
   git history, image layers.)
2. **Exposure surface** — secrets in environment variables, build logs, CI/CD
   variables, error messages, or client-side code; secrets in plaintext at rest.
3. **Storage** — is a secrets manager/vault used (HashiCorp Vault, cloud secret
   managers, k8s external secrets)? Or are secrets scattered ("sprawl")?
4. **Gitignore hygiene** — confirm sensitive paths are actually excluded, not just
   assumed: `.env`/`.env.*`, `*.pem`/`*.key`/`*.p12`/`*.pfx`, `id_rsa*`,
   `credentials.json`, `*kubeconfig*`, `terraform.tfstate*`/`.terraform/`, vendored
   cloud-CLI creds (`.aws/credentials`, `.azure/`, `.gcloud/`), and tool local-state
   dirs that can carry secrets/session data (`.claude/`, `.vscode/` settings with
   tokens, `.idea/`). Check both directions: pattern present in `.gitignore` **and**
   the inverse via `git ls-files` — a file already tracked stays tracked even after
   it's added to `.gitignore`, so gitignoring it later doesn't remove it from
   history. Flag high-severity any sensitive path that's untracked-but-not-ignored
   (next `git add .`/`-A` will commit it) or tracked-and-should-be-untracked.
5. **Access & scope** — who/what can read each secret; least privilege; per-service
   scoping vs. shared god-secrets.
6. **Rotation & lifecycle** — rotation policy, expiry, revocation on compromise,
   detection of leaked secrets.

# Steps

1. Scope the surfaces (repos, IaC, CI/CD, registries, runtime config). Run secret
   scanners where possible (gitleaks, trufflehog, detect-secrets) and review results.
   Check `.gitignore` coverage and `git ls-files` for sensitive paths as above.
2. For each finding: classify (hardcoded / exposed / unrotated / over-scoped),
   confirm it's a real secret, and assess blast radius.
3. Treat any live, committed secret as an incident: flag for **rotation/revocation**,
   not just removal (it's in history/layers).
4. Recommend: move to a vault, scope access, enable rotation, add pre-commit/CI
   secret scanning.

# Output

A findings table: location · secret type · issue · severity · action (rotate/
revoke/vault/scope/gitignore). Confirmed live secrets → `security-reporting:finding`
(rate high+; recommend rotation, not just deletion).

# Notes

Removing a committed secret does **not** make it safe — it lives in git history and
image layers, so it must be rotated/revoked. Centralize into a vault with
least-privilege access and rotation; add secret scanning to pre-commit and CI to
prevent recurrence. This skill is the manual/audit pass across any stack; for a
repo that wants this *enforced* automatically (blocked at commit/push, not just
reviewed on request), `secure-coding:secret-guard` installs the actual git hooks
(via `install-git-hooks.sh`) plus a Claude Code `PreToolUse` hook — point the
user at it when they want prevention, not just detection.
