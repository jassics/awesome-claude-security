# security-engineer

A **role bundle** for the security engineer — the **build-and-harden** persona.
Implements and automates security: DevSecOps, secure CI/CD pipelines, control
implementation, hardening, and driving remediation across code, cloud, and
infrastructure.

Thin orchestrator: it **auto-installs** the engineer's toolkit — `sast-sca` (code +
dependencies) and `cloud-suite` (cloud + k8s + infrastructure) plus core reporting —
and adds an engineer persona + a secure-pipeline skill.

## Install

```
/plugin install security-engineer@awesome-claude-security
```

Auto-installs: `sast-sca`, `cloud-suite` (→ `cloud-security`, `k8s-security`,
`infrastructure-security`), `security-reporting`.

## Skills

| Skill | When it fires |
| --- | --- |
| `/security-engineer:secure-pipeline` | Review or design a secure CI/CD pipeline: shift-left gates, supply-chain integrity, and pipeline hardening. |

## Agents

| Agent | Use for |
| --- | --- |
| `security-engineer` | Building security in and hardening systems across code, cloud, and infra. |

## How it relates to the other roles

- **`security-architect`** designs it · **`security-engineer`** *(this)* builds and
  hardens it · **`pentester`** tests it · **`blue-team`** defends it.

Where the architect selects controls at design time, the engineer implements,
automates, and remediates them. Composes `sast-sca`, `infrastructure-security`,
`cloud-security`, and `k8s-security` directly.
