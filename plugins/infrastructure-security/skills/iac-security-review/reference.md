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
- [ ] Role session duration (`max_session_duration` / `MaxSessionDuration`) is no
      longer than the workload actually needs. AWS defaults to 1h if unset — that's
      already safe; the real risk is IaC that explicitly raises it toward the 12h
      ceiling "for convenience" (a long CI job, a lazy default copied across roles).
      Once raised, the wider window silently applies to *every* future assumption
      of that role, including ones that only needed a few minutes — a leaked token
      now has hours of blast radius instead of one. Flag any explicit value above
      what the role's actual workload duration requires, and flag any role with no
      value set that's assumed by a third party or cross-account principal (that
      combination should set an explicit, tight value, not rely on the default).
- [ ] Trust policies scope the assuming principal precisely, and — wherever a
      third-party or cross-account principal is trusted (SaaS integrations, CI/CD
      OIDC providers, cross-account roles) — include a confused-deputy condition
      (`aws:SourceArn`, `aws:SourceAccount`, `sts:ExternalId`, or the OIDC
      equivalent `sub`/`aud` claim scoping). A bare `Principal` with no `Condition`
      lets *any* caller who knows or guesses the ARN/account ID assume the role,
      not just the intended one.

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

## Helm chart defaults (distribution-scale blast radius)

A chart's `values.yaml` default isn't just this deployment's config — it's every
future `helm install`'s config, silently, unless that installer knows to override
it. Treat a permissive chart default as a finding that multiplies across every
consumer, not a single misconfiguration:

- [ ] `resources` (CPU/memory requests+limits) isn't empty/absent by default — an
      unset default here reproduces the same missing-resource-limit gap
      `k8s-security` flags at the manifest level, but now every chart consumer
      inherits it without writing a single line of YAML.
- [ ] `networkPolicy.enabled` (or equivalent) defaults to `true`/default-deny where
      the chart's own templates support it, not `false`/absent — cross-ref
      `k8s-security`'s default-deny `NetworkPolicy` check.
- [ ] `ingress.tls` isn't an empty list (`[]`) by default if the chart ships an
      Ingress template — TLS-off should be an explicit opt-out, not the shipped
      default.
- [ ] Auto-created RBAC (`serviceAccount.create: true` plus a generated
      Role/RoleBinding) doesn't grant more than the chart's own workload needs by
      default; check the templated Role, not just the values-file toggle.
- [ ] If a control is intentionally left off by default for portability (e.g. a
      chart meant to run on clusters without a CNI that supports NetworkPolicy),
      that trade-off is documented in `values.yaml` comments or the README with the
      security implication stated — not silently defaulted with no note anywhere.

## Per-format notes

- **Terraform**: watch `*.tfvars`, `locals`, and state files for secrets; pin
  module `source` + `version`.
- **CloudFormation**: parameters with `NoEcho`, no secrets in `Default`.
- **ARM/Bicep**: `secureString` params; avoid secrets in outputs.
- **Ansible**: use Vault for secrets; avoid plaintext in playbooks/inventory.
- **Helm/K8s manifests**: cross-ref `k8s-security` (Pod Security, RBAC, NetworkPolicy)
  for a specific manifest/cluster, and the "Helm chart defaults" section above for
  a chart's `values.yaml` defaults, which apply to every future install.
