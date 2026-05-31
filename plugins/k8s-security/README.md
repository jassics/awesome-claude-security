# k8s-security

Kubernetes security. Review a cluster against the **CIS Kubernetes Benchmark** and
the **4Cs** model (Cloud, Cluster, Container, Code), audit **RBAC** for least
privilege and escalation, and harden **workloads** with Pod Security Standards and
admission control.

A **domain** plugin; member of the planned `cloud-suite`. Works on clusters you are
authorized to assess.

## Install

```
/plugin install k8s-security@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/k8s-security:k8s-cluster-review` | Review cluster security across control plane, RBAC, workloads, network, secrets, admission. |
| `/k8s-security:k8s-rbac-review` | Audit RBAC for over-permission and privilege-escalation paths. |
| `/k8s-security:k8s-workload-hardening` | Harden pods/workloads: securityContext, Pod Security Standards, capabilities, host access. |

## Pairs well with

`cloud-security` (managed clusters: EKS/AKS/GKE), `supply-chain-security` (roadmap),
`sast-sca` (image deps), `threat-modeling`, `security-reporting`.
