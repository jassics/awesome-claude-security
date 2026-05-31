# cloud-suite

A **domain suite** for cloud & infrastructure security: one-shot install of the full
cloud stack. Manifest-only bundle — it owns no skills, just composes standalone
plugins you can also install individually.

## Install

```
/plugin install cloud-suite@awesome-claude-security
```

## Members

| Plugin | Covers |
| --- | --- |
| `cloud-security` | AWS/Azure/GCP posture, IAM, misconfiguration scanning. |
| `k8s-security` | Kubernetes CIS/4Cs review, RBAC, pod hardening. |
| `infrastructure-security` | IaC review, host/OS hardening (CIS), secrets management. |

Together these cover the cloud-native stack at both **design time** (IaC, host
images) and **runtime** (cloud posture, live clusters).

## Note on scope

Domain suites bundle **domain** plugins only. The shared **core** plugins
(`security-diagramming`, `security-reporting`) stay standalone — install them
directly, or get them via a role bundle. See [docs/BUNDLES.md](../../docs/BUNDLES.md).
