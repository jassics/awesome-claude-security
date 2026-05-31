---
name: k8s-rbac-review
description: >-
  Audit Kubernetes RBAC for least privilege and privilege-escalation paths —
  cluster-admin sprawl, wildcard/dangerous verbs, risky bindings, and service-account
  token exposure. Use to review who can do what in a cluster and find escalation to
  cluster-admin.
---

# Goal

An RBAC risk assessment: which subjects (users, groups, service accounts) hold
excessive or dangerous permissions, and which paths lead to cluster-admin — with
least-privilege fixes.

# Dangerous permissions to hunt

- **Escalation primitives** — `create`/`update` on `roles`/`clusterroles`/
  `rolebindings`/`clusterrolebindings`; `escalate`/`bind` verbs; `impersonate`.
- **Workload-to-node/secret** — `create pods` (esp. with privileged/hostPath),
  `pods/exec`, `pods/attach`, `create` on `pods/ephemeralcontainers`.
- **Secret access** — `get`/`list` on `secrets` (cluster-wide is effectively
  cluster-admin via token theft).
- **Wildcards** — `verbs: ["*"]`, `resources: ["*"]`, `apiGroups: ["*"]`, and
  cluster-admin bindings.
- **Token exposure** — service accounts with auto-mounted tokens and broad rights.

# Steps

1. Enumerate Roles/ClusterRoles and their bindings; map subject → effective
   permissions (consider tooling like `kubectl auth can-i`, rbac audit tools).
2. Flag wildcard/admin grants, the dangerous verbs above, and broad secret access.
3. Trace escalation: can a namespace-scoped subject reach cluster-admin (e.g. via
   pod creation onto a privileged node, secret theft, or role self-grant)? Model the
   worst path (`security-diagramming:attack-tree`).
4. Record: subject · grant · risk · escalation? · least-priv recommendation.

# Output

An RBAC findings table + an escalation-path diagram for the worst case. Confirmed
issues → `security-reporting:finding` (rate escalation-to-cluster-admin high+).

# Notes

In Kubernetes, broad `secrets` read or `pods/exec` plus a privileged node is
effectively cluster-admin — treat those as escalation, not "just read access."
Recommend namespaced, least-privilege Roles and disabling unneeded SA token
auto-mount.
