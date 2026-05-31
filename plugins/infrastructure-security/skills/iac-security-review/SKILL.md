---
name: iac-security-review
description: >-
  Review Infrastructure-as-Code (Terraform, CloudFormation, ARM/Bicep, Pulumi,
  Ansible, Helm) for security misconfigurations before deployment — public exposure,
  weak IAM, missing encryption, open networking, and hardcoded secrets. Use to
  shift-left and catch cloud/k8s misconfig at the code layer.
---

# Goal

A triaged set of IaC security findings, each tied to the resource/line and a fix —
so misconfigurations are caught before they reach a live environment.

# What to review (see `reference.md` for the checklist)

1. **Public exposure** — resources open to the internet (security groups/NSGs/
   firewall `0.0.0.0/0`, public buckets/storage, public IPs on sensitive hosts).
2. **Identity** — over-broad IAM policies, wildcard permissions, default/no roles,
   long-lived credentials defined in code.
3. **Encryption** — storage/volumes/databases without encryption at rest; TLS not
   enforced; default/unmanaged keys.
4. **Logging & monitoring** — audit logging/flow logs not enabled by the IaC.
5. **Secrets** — hardcoded passwords/keys/tokens in variables, defaults, or state
   (cross-ref `secrets-management-review`).
6. **Module/provider hygiene** — untrusted/unpinned modules, provider versions,
   drift between code and deployed state.

# Steps

1. Identify the IaC type and scope; run an IaC scanner if available (Checkov,
   tfsec/Trivy, KICS, cfn-nag) or review the templates directly.
2. Triage findings: map each to the resource and confirm it's a real exposure (not
   a scanner false positive); note severity and blast radius.
3. Check for hardcoded secrets and sensitive values in variables/state.
4. Provide the corrected IaC snippet per finding.

# Output

A findings table: file:line · resource · misconfig · severity · fix (corrected
snippet). Confirmed issues → `security-reporting:finding`. These map to the same
controls `cloud-security` / `k8s-security` check at runtime.

# Notes

Shift-left: fixing in IaC prevents the misconfig everywhere it's deployed and stops
drift. Treat secrets in code/state as high severity. Pin and vet third-party modules
— they run with your deploy credentials.
