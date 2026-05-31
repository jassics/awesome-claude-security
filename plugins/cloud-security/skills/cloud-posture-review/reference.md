# Reference: cloud posture checks (AWS / Azure / GCP)

Per-domain checks for `cloud-posture-review`. Anchor to the current CIS Benchmark for
each provider and the provider's Well-Architected / security best-practice guidance.

## Identity & access

- [ ] No use of the root/global-admin account for daily ops; MFA on root and all
      privileged identities.
- [ ] Least-privilege policies; no wildcard `*:*` admin grants beyond break-glass.
- [ ] No long-lived access keys where short-lived/federated creds are possible;
      rotate and remove unused keys/credentials.
- [ ] Cross-account/cross-tenant and public principal grants reviewed.
- AWS: IAM, STS, permissions boundaries, SCPs · Azure: Entra ID, RBAC, PIM ·
  GCP: IAM, service accounts, org policies.

## Network

- [ ] No unrestricted `0.0.0.0/0` ingress to sensitive ports (SSH/RDP/DB).
- [ ] Private connectivity for data services; no public DB endpoints.
- [ ] Segmentation (VPC/VNet subnets), egress filtering, flow logs enabled.

## Data protection

- [ ] Object/blob storage not public; block-public-access on.
- [ ] Encryption at rest with managed keys; TLS enforced in transit.
- [ ] No public snapshots/AMIs/images; backups protected.
- AWS: S3/EBS/RDS/KMS · Azure: Storage/Disk/Key Vault · GCP: GCS/PD/Cloud KMS.

## Logging & monitoring

- [ ] Org-wide audit logging on, immutable, centralized:
      CloudTrail (AWS) · Activity/Diagnostic Logs (Azure) · Cloud Audit Logs (GCP).
- [ ] Threat detection enabled: GuardDuty · Defender for Cloud · Security Command
      Center.
- [ ] Alerting on high-risk events (root login, policy changes, key deletion).

## Workload & service config

- [ ] Metadata service hardened (AWS IMDSv2 required); no creds in user-data.
- [ ] Serverless/function roles least-privilege; secrets in a vault, not env/plain.
- [ ] Managed-service public access reviewed (databases, caches, queues).

## Governance

- [ ] Multi-account/subscription/project structure with baseline guardrails
      (SCPs / Azure Policy / Org Policy).
- [ ] Tagging for ownership; drift detection; new-resource guardrails.

## Map to frameworks

CIS Benchmarks (per provider), CIS Controls, NIST CSF, and the provider
Well-Architected security pillar. For attack techniques, MITRE ATT&CK Cloud matrix.
