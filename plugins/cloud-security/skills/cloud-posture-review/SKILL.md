---
name: cloud-posture-review
description: >-
  Review a cloud environment's security posture (AWS/Azure/GCP) across IAM,
  network, data protection, logging/monitoring, and workload configuration, mapped
  to CIS benchmarks, and produce ranked findings. Use for a CSPM-style assessment of
  an account/subscription/project you're authorized to review.
---

# Goal

A posture assessment across the major control domains, each with findings,
severity, and remediation, anchored to CIS Benchmarks / provider best practice.

# Control domains (see `reference.md` for per-provider checks)

1. **Identity & access** — IAM users/roles/policies, least privilege, MFA, root/
   admin usage, key rotation, federation. (Deep dive: `cloud-iam-review`.)
2. **Network** — security groups/NSGs/firewall rules, public exposure, private
   connectivity, segmentation, egress controls.
3. **Data protection** — storage exposure, encryption at rest/in transit, key
   management, backups, public snapshots/buckets.
4. **Logging & monitoring** — audit logging (CloudTrail/Activity Log/Cloud Audit
   Logs), log integrity, alerting, guard/threat services enabled.
5. **Workload & service config** — compute hardening, managed-service settings,
   serverless permissions, secrets handling, metadata service (IMDSv2 etc.).
6. **Governance** — account/org structure, baseline guardrails (SCPs/Policies),
   tagging, drift.

# Steps

1. Establish scope (accounts/subscriptions/projects, regions) and read access.
2. Walk each domain with `reference.md`; for identity use `cloud-iam-review`, for
   exposure quick-wins use `cloud-misconfig-scan`.
3. Record per finding: domain · control (CIS ref) · observation · severity ·
   remediation. Use provider config/posture data, not assumptions.
4. Score (`security-reporting:cvss`) and rank; highlight internet-exposed and
   identity findings first.

# Output

A posture report grouped by domain with a CIS-mapped findings table + ranked top
risks. Confirmed issues → `security-reporting:finding`; architecture via
`security-diagramming:architecture-diagram`.

# Notes

Most cloud breaches trace to **identity** over-permission and **public exposure** of
data/compute — weight those. Map findings to CIS controls for traceability; verify
against the current benchmark version for the provider.
