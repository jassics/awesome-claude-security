---
name: secure-pipeline
description: >-
  Review or design the security of a CI/CD pipeline: shift-left scanning gates
  (SAST/SCA/secret/IaC), software supply-chain integrity (SBOM, pinning, signing/
  provenance), and pipeline hardening (least-privilege runners, isolation, protected
  branches). Use to build security into the SDLC or assess a pipeline's controls.
---

# Goal

A pipeline that catches security issues before release and can't itself be
subverted — with the right automated gates, supply-chain integrity, and a hardened
build/deploy path.

# What to cover

1. **Shift-left gates** — wire scanning into the pipeline and define pass/fail policy:
   - **SAST** on code changes (`sast-sca:sast-review`).
   - **SCA / SBOM** on dependencies (`sast-sca:sca-review`).
   - **Secret scanning** pre-commit and in CI (`infrastructure-security:secrets-management-review`).
   - **IaC scanning** on infra changes (`infrastructure-security:iac-security-review`).
   - **Container/image scanning** for builds (cross-ref `k8s-security`).
   Tune to fail on real, reachable, high-severity issues — not noise (avoid breaking
   builds on unreachable CVEs).
2. **Supply-chain integrity** — pinned dependencies and base images (by digest),
   generated and stored SBOMs, artifact **signing and provenance** (e.g. cosign /
   SLSA), trusted registries, and verification at deploy.
3. **Pipeline hardening** — least-privilege, short-lived runner credentials; isolated/
   ephemeral build environments; protected branches and required reviews; no secrets
   in logs/env; pinned third-party CI actions/plugins (a common compromise vector);
   separation of build vs. deploy permissions.
4. **Deploy gates & feedback** — policy gates before prod; fast, actionable feedback
   to developers; exceptions tracked with owners and expiry, not silent bypasses.

# Steps

1. Map the pipeline (stages, triggers, runners, credentials, artifacts, deploy path).
2. Assess against the four areas above; for each gap note severity and the fix.
3. Recommend the gate set + policy, supply-chain controls, and hardening changes;
   prefer failing closed on high-severity, reachable findings.
4. Provide concrete config (pipeline steps / policy) where helpful. When the gates
   need to be **implemented**, not just designed, start from
   `templates/security-gates/` in this repo (a working `.pre-commit-config.yaml` +
   GitHub Actions workflow already wired to gitleaks/semgrep/bandit/checkov/
   OSV-Scanner) rather than writing gate config from scratch — copy it in, pin
   every hook/action to a real release tag, then tune severity thresholds and
   file globs to the target repo.

# Output

A secure-pipeline review: stage · control · present? · gap · severity · fix, plus a
target pipeline design (gates + supply-chain + hardening). Use `security-reporting`.

# Notes

A pipeline is itself a high-value target — an attacker who owns CI owns prod. Pin
third-party actions and scope runner credentials tightly. Make gates **actionable**:
gates that fire constant false positives get bypassed, which is worse than no gate.
Track exceptions with owners and expiry. See `templates/security-gates/
SECURITY-GATE-NOTES.md` for a concrete burn-in rollout (report-only → tuned →
blocking) so a new gate doesn't get bypassed on day one.
