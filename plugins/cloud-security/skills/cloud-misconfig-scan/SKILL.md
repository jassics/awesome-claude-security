---
name: cloud-misconfig-scan
description: >-
  Scan a cloud environment (AWS/Azure/GCP) for high-impact misconfigurations and
  exposures — public storage, open ingress, unencrypted data, exposed secrets/
  metadata, missing logging — and prioritize quick wins. Use for a fast exposure
  sweep on an authorized environment.
---

# Goal

A prioritized list of concrete misconfigurations, focused on the high-impact,
commonly-exploited exposures that deliver the fastest risk reduction.

# High-impact misconfigurations to check

1. **Public data** — world-readable/writable object storage, public snapshots/
   images, public databases/caches.
2. **Open network** — `0.0.0.0/0` to SSH/RDP/DB/admin ports; overly broad security
   groups/NSGs/firewall rules.
3. **Encryption gaps** — unencrypted storage/volumes/databases; TLS not enforced;
   default/unmanaged keys for sensitive data.
4. **Identity exposure** — public/cross-account grants, wildcard policies, no MFA on
   privileged users (cross-ref `cloud-iam-review`).
5. **Secrets & metadata** — secrets in user-data/env/code; metadata service
   unprotected (AWS IMDSv1 allowed); credentials reachable from compute.
6. **Logging off** — audit logging or threat detection disabled in any region/account.

# Steps

1. Confirm scope and read access. Use provider config data / a CSPM tool if available.
2. Check each category; for each hit, capture the resource, exposure, and blast
   radius. Prioritize internet-reachable and data-exposing findings.
3. Record: category · resource · exposure · severity · fix.

# Output

A prioritized misconfig table: category · resource · exposure · severity · remediation
(quick-win flag). Confirmed issues → `security-reporting:finding`.

# Notes

This is the fast exposure sweep; `cloud-posture-review` is the comprehensive,
CIS-mapped assessment — run this first for quick wins, then the full review.
Public data + open admin ports are the highest-frequency real-world cloud incidents.
