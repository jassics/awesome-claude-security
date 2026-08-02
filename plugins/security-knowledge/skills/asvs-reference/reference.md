# Reference: OWASP ASVS v5.0

Chapter numbering shifts between ASVS editions — treat the list below as a scope
guide, and confirm exact requirement IDs against the current published standard
when precision matters.

## Verification levels

| Level | Criteria | Use for |
| --- | --- | --- |
| **L1** | Baseline, opportunistic-attacker resistant; every control black-box testable | Low-assurance apps, early-stage products |
| **L2** | Defends against most real-world attackers; the default | Apps handling sensitive data — most business apps |
| **L3** | Full depth, high-assurance; requires architecture/code review, not just black-box testing | Financial, healthcare, critical infra, regulated/high-value targets |

## Chapter scope (representative — confirm exact numbering against current ASVS)

| Chapter | Scope |
| --- | --- |
| Encoding & Sanitization | Output encoding, injection prevention |
| Validation & Business Logic | Input validation, business-logic abuse resistance |
| Web Frontend Security | CSP, cookies, clickjacking, CORS |
| API & Web Service | REST/GraphQL/SOAP security controls |
| File Handling | Upload validation, storage, path handling |
| Authentication | Credential handling, MFA, password policy |
| Session Management | Token lifecycle, fixation, timeout |
| Authorization | Access control enforcement, least privilege |
| Self-contained Tokens | JWT/token validation |
| OAuth/OIDC | Delegated auth flows |
| Cryptography | Algorithm choice, key management |
| Communications (Transport) | TLS configuration, certificate validation |
| Malicious/Self Code Protection | Anti-tampering, integrity checks |
| Data Protection | Sensitive data classification, storage, retention |
| Secure Coding & Architecture | SDLC controls, dependency management, configuration |
| Security Logging | Audit trail sufficiency, tamper resistance |

## When to use which level

- Public marketing site → L1.
- Internal app with PII or auth → L2.
- Payment processing, health records, critical infra control plane → L3.
- When unsure, default to **L2** and flag specific high-risk flows (auth, payment,
  admin) for L3 depth.

## Relationship to other frameworks

- ASVS requirements crosswalk to **CWE** (see `framework-mapping`) for the
  underlying weakness taxonomy.
- ASVS is verification depth for a single app; **OWASP SAMM** (see
  `security-architect:secure-architecture-maturity`) is program-level maturity
  across the SDLC — use both together, not interchangeably.
