# infrastructure-security

Security for the infrastructure layer. Review **Infrastructure-as-Code** (Terraform,
CloudFormation, ARM/Bicep, Pulumi, Ansible, Helm) before it ships, harden **hosts/OS**
against CIS Benchmarks, and review **secrets management** (sprawl, hardcoding,
vaulting, rotation).

A **domain** plugin and the third member of [`cloud-suite`](../cloud-suite/). It
catches misconfigurations at the IaC/host layer that `cloud-security` and
`k8s-security` find at runtime — shift-left.

## Install

```
/plugin install infrastructure-security@awesome-claude-security
# or the whole cloud stack:
/plugin install cloud-suite@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/infrastructure-security:iac-security-review` | Review IaC for security misconfig before deploy (shift-left). |
| `/infrastructure-security:host-hardening-review` | Review host/OS hardening against CIS benchmarks. |
| `/infrastructure-security:secrets-management-review` | Review secrets handling: hardcoding, sprawl, vaulting, rotation. |

## Pairs well with

`cloud-security`, `k8s-security`, `sast-sca` (code + dep scanning),
`supply-chain-security` (roadmap), `security-reporting`.
