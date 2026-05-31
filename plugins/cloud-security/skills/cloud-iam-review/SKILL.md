---
name: cloud-iam-review
description: >-
  Audit cloud IAM (AWS/Azure/GCP) for least privilege: over-permissioned identities,
  wildcard/admin grants, public or cross-account access, unused credentials, and
  privilege-escalation paths. Use to review identity risk — the top cause of cloud
  compromise.
---

# Goal

An identity-risk assessment: which principals are over-permissioned, which grants
are dangerous or externally exposed, and what privilege-escalation paths exist —
with least-privilege remediations.

# What to review

1. **Excess privilege** — wildcard actions/resources, admin/owner roles, unused
   permissions vs. actual usage (access analyzer / last-used data).
2. **Dangerous permissions** — those enabling escalation: `iam:PassRole` +
   create-compute, policy/role modification, `*:CreatePolicyVersion`, key creation,
   `sts:AssumeRole` chains; Azure role-assignment writes; GCP `iam.serviceAccounts.
   actAs` / setIamPolicy.
3. **External exposure** — public principals (`"Principal":"*"`), cross-account/
   cross-tenant trust, federated/external identities.
4. **Credential hygiene** — long-lived keys, no MFA on privileged users, stale/
   unused identities, root/break-glass usage.
5. **Escalation paths** — chain grants to see if a low-priv identity can reach admin
   (model the worst path with `security-diagramming:attack-tree`).

# Steps

1. Pull IAM policies/roles/bindings and, where available, last-used/access-analyzer
   data for the in-scope accounts.
2. Flag over-permission, dangerous permissions, and external grants; verify against
   actual usage to avoid recommending breakage.
3. Trace escalation paths from notable low-priv identities to high-priv.
4. Record: principal · grant · risk · escalation? · least-priv recommendation.

# Output

An IAM findings table + an escalation-path diagram for the worst case. Confirmed
issues → `security-reporting:finding` (rate escalation paths and public grants
high+).

# Notes

`PassRole`/`actAs`-style permissions plus compute-creation are the classic cloud
privilege-escalation primitives — check them explicitly. Recommend least privilege
from observed usage, not guesses, so fixes don't break workloads.
