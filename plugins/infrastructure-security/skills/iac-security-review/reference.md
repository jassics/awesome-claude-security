# Reference: IaC security checklist

Checks for `iac-security-review`, grouped by control area. Tooling: Checkov,
tfsec/Trivy, KICS, cfn-nag, terrascan. Anchor severities to the resource's exposure.

## Networking

- [ ] No `0.0.0.0/0` (or `::/0`) ingress to SSH/RDP/DB/admin ports.
- [ ] No unintended public IPs / public load balancers on sensitive workloads.
- [ ] Egress restricted where feasible; flow logs enabled.

## Identity & access

- [ ] No wildcard (`*`) actions/resources in inline policies/roles.
- [ ] Least-privilege roles; no overly broad managed-policy attachments.
- [ ] No access keys / long-lived credentials declared in code.
- [ ] Assume-role / trust policies scoped (no `Principal: *`).

## Data protection

- [ ] Encryption at rest enabled (buckets, volumes, databases, queues) with managed
      keys; versioning/backup where relevant.
- [ ] TLS/HTTPS enforced; no plaintext protocols.
- [ ] Storage block-public-access enabled; no public read/write ACLs.

## Logging & monitoring

- [ ] Audit logging (CloudTrail/Activity/Audit Logs) provisioned by the IaC.
- [ ] Log buckets protected and immutable; alarms for high-risk events.

## Secrets (see `secrets-management-review`)

- [ ] No hardcoded passwords/keys/tokens in variables, defaults, locals, or outputs.
- [ ] Sensitive values marked sensitive; not written to plaintext state where
      avoidable; remote state encrypted and access-controlled.

## Supply chain / hygiene

- [ ] Third-party modules pinned to versions/digests and from trusted sources.
- [ ] Provider versions pinned; deprecated resources flagged.
- [ ] Drift detection in place between code and deployed state.

## Per-format notes

- **Terraform**: watch `*.tfvars`, `locals`, and state files for secrets; pin
  module `source` + `version`.
- **CloudFormation**: parameters with `NoEcho`, no secrets in `Default`.
- **ARM/Bicep**: `secureString` params; avoid secrets in outputs.
- **Ansible**: use Vault for secrets; avoid plaintext in playbooks/inventory.
- **Helm/K8s manifests**: cross-ref `k8s-security` (Pod Security, RBAC, NetworkPolicy).
