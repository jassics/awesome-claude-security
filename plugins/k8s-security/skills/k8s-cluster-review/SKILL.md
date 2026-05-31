---
name: k8s-cluster-review
description: >-
  Review a Kubernetes cluster's security across control plane, RBAC, workload
  configuration, network policy, secrets, and admission control, mapped to the CIS
  Kubernetes Benchmark and the 4Cs model. Use for a comprehensive cluster security
  assessment of a cluster you're authorized to review.
---

# Goal

A cluster assessment across all major control areas, each with findings, severity,
and remediation, anchored to the CIS Kubernetes Benchmark.

# Areas (see `reference.md` for checks)

1. **Control plane** — API server flags, anonymous/authn-authz config, etcd
   encryption & access, kubelet config, audit logging. (Managed clusters: provider
   owns some — cross-ref `cloud-security`.)
2. **RBAC & identity** — least privilege, cluster-admin sprawl, dangerous verbs,
   service-account token use. (Deep dive: `k8s-rbac-review`.)
3. **Workloads** — Pod Security Standards/admission, privileged/hostPath/hostNetwork
   pods, securityContext, capabilities. (Deep dive: `k8s-workload-hardening`.)
4. **Network** — default-deny NetworkPolicies, namespace isolation, exposed services/
   LoadBalancers, ingress.
5. **Secrets** — etcd encryption at rest, secret access scope, secrets in env/images,
   external secret managers.
6. **Admission & supply chain** — admission controllers/policy engines (e.g. OPA/
   Kyverno), image provenance/signing, registry trust, image scanning.

# Steps

1. Establish scope and read access (`kubectl`/manifests/IaC). Note managed vs.
   self-managed (who owns the control plane).
2. Walk each area with `reference.md`; delegate RBAC and workload depth to the
   companion skills.
3. Record: area · control (CIS ref) · finding · severity · remediation.
4. Score (`security-reporting:cvss`) and rank.

# Output

A cluster report grouped by area with a CIS-mapped findings table + ranked top
risks. Confirmed issues → `security-reporting:finding`.

# Notes

Think in **4Cs** (Cloud, Cluster, Container, Code): a hardened pod on a wide-open API
server is still exposed. On managed clusters, confirm which controls the provider
owns vs. you. Default-deny network policy and restricting privileged pods are the
highest-leverage wins.
