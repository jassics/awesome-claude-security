# Reference: Kubernetes cluster checks

Checks for `k8s-cluster-review`, anchored to the CIS Kubernetes Benchmark and the
4Cs model. Verify against the current benchmark and your Kubernetes version.

## Control plane

- [ ] API server: `--anonymous-auth=false`, no `AlwaysAllow` authz, RBAC enabled,
      `--authorization-mode=Node,RBAC`.
- [ ] etcd: encryption at rest enabled for secrets; etcd peer/client TLS; access
      restricted to API server.
- [ ] kubelet: authn/authz on (`--anonymous-auth=false`, `--authorization-mode=
      Webhook`), read-only port disabled.
- [ ] Audit logging enabled and shipped off-cluster.
- Managed (EKS/AKS/GKE): provider owns much of this — verify the shared-responsibility
  split (`cloud-security`).

## RBAC & identity (see `k8s-rbac-review`)

- [ ] No unnecessary `cluster-admin`; no wildcard verbs/resources.
- [ ] `automountServiceAccountToken: false` where not needed; scoped SA per workload.
- [ ] No dangerous verbs broadly granted (see RBAC reference).

## Workloads (see `k8s-workload-hardening`)

- [ ] Pod Security Standards enforced (baseline/restricted) via admission.
- [ ] No privileged containers, hostPID/hostIPC/hostNetwork, hostPath mounts.
- [ ] Drop capabilities, `runAsNonRoot`, read-only root FS, seccomp.

## Network

- [ ] Default-deny NetworkPolicy per namespace; explicit allow-lists.
- [ ] Namespace isolation; no unintended cross-namespace access.
- [ ] Services not unintentionally exposed (NodePort/LoadBalancer review); ingress TLS.

## Secrets

- [ ] Secrets encrypted at rest (etcd); access scoped via RBAC.
- [ ] No secrets baked into images or passed as plain env where avoidable; consider
      external secret managers / CSI secrets.

## Admission & supply chain

- [ ] Policy engine in place (OPA Gatekeeper / Kyverno / PSA) enforcing standards.
- [ ] Image provenance: trusted registries, signing/verification (e.g. cosign),
      image vulnerability scanning (`sast-sca` for deps).
- [ ] Admission webhooks secured; no overly permissive mutating webhooks.

## Frameworks

CIS Kubernetes Benchmark, NSA/CISA Kubernetes Hardening Guidance, MITRE ATT&CK for
Containers, Pod Security Standards.
