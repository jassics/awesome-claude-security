# supply-chain-security

Secure the **software supply chain** — the trust and integrity of everything you
ship that you didn't write line-by-line. Vet dependency *trust* (typosquatting,
dependency confusion, maintainer risk, install scripts), establish **artifact
provenance and signing** (SLSA, Sigstore/cosign, in-toto), and harden the
**CI/CD pipeline** against tampering.

A **domain** plugin. It **complements `sast-sca`**: `sast-sca` answers *"is this
dependency vulnerable?"*; this plugin answers *"can I trust this dependency, this
artifact, and this build?"*

## Install

```
/plugin install supply-chain-security@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/supply-chain-security:dependency-supply-chain-review` | Trust-vet dependencies: typosquatting, dependency confusion, maintainer/abandonment, install scripts, pinning. |
| `/supply-chain-security:artifact-provenance-verification` | Assess/establish provenance & signing (SLSA level, Sigstore, in-toto) and enforced verification. |
| `/supply-chain-security:pipeline-integrity-review` | Harden CI/CD against tampering: PPE, runner trust, secrets, mutable inputs (OWASP CI/CD, SLSA build track). |

## Pairs well with

`sast-sca` (dependency-CVE scanning + SBOM generation), `vulnerability-management`
(remediation), `infrastructure-security` (IaC/secrets), `security-reporting`,
`security-diagramming`.
