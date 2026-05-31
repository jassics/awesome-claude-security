---
name: k8s-workload-hardening
description: >-
  Review and harden Kubernetes workloads (pods/Deployments) against Pod Security
  Standards — privileged containers, host namespaces, hostPath, capabilities,
  securityContext, and admission enforcement. Use to assess or fix pod-level
  security for a workload or namespace.
---

# Goal

Workloads that meet the Pod Security Standards (baseline → restricted), with
dangerous settings removed and enforcement guaranteed by admission, not just policy
on paper.

# What to check / set

1. **Privilege** — no `privileged: true`; `allowPrivilegeEscalation: false`;
   `runAsNonRoot: true`, non-zero `runAsUser`.
2. **Host access** — no `hostNetwork`/`hostPID`/`hostIPC`; no `hostPath` mounts; no
   host ports.
3. **Capabilities** — `drop: ["ALL"]`, add back only what's required; no `SYS_ADMIN`/
   `NET_ADMIN` unless justified.
4. **Filesystem** — `readOnlyRootFilesystem: true`; writable paths via emptyDir/
   volumes.
5. **Seccomp / AppArmor** — `seccompProfile: RuntimeDefault` (or stricter); AppArmor
   where available.
6. **Resources & images** — set requests/limits (DoS containment); pinned image
   digests from trusted registries; non-root images; scanned (`sast-sca`).
7. **Enforcement** — Pod Security Admission level (baseline/restricted) per namespace,
   or a policy engine (Kyverno/OPA) so violations are rejected, not just flagged.

# Steps

1. Pull the workload manifests / running pod specs in scope.
2. Compare against the restricted Pod Security Standard; flag each gap with severity.
3. Verify admission actually enforces the standard (test that a bad pod is rejected),
   not just that good pods exist.
4. Provide the corrected securityContext/manifest snippets.

# Output

A hardening table: workload · setting · current · required · severity · fix, plus
corrected manifest snippets and the namespace admission level to enforce. Confirmed
issues → `security-reporting:finding`.

# Notes

A privileged or hostPath-mounted container is a node-takeover and often cluster-admin
path — treat those as the top severities. Hardening the pod is only durable if
**admission enforces** the standard; verify enforcement, don't assume it.
