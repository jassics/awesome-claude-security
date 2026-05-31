# Reference: OWASP Top 10 (2021)

Checks and fixes for `owasp-web-top10`. Verify against the current OWASP list.

| ID | Category | Look for | Fix |
| --- | --- | --- | --- |
| A01 | Broken Access Control | IDOR/BOLA, missing function-level authz, forced browsing, privilege escalation, JWT/role tampering. | Deny by default; server-side authz on every object & function; tie to authenticated identity. (`access-control-test`) |
| A02 | Cryptographic Failures | Cleartext transport/storage, weak/old algorithms, hardcoded keys, bad randomness. | TLS everywhere; strong algorithms; managed keys/secrets; encrypt sensitive data at rest. |
| A03 | Injection | SQL/NoSQL, OS command, LDAP, template injection, XSS. | Parameterized queries; context-aware output encoding; allow-list validation; safe templating. (`injection-test`) |
| A04 | Insecure Design | Missing threat model, unsafe flows, no rate limiting on sensitive actions. | Threat model (`threat-modeling`); secure design patterns; abuse-case testing. |
| A05 | Security Misconfiguration | Default creds, verbose errors, open cloud storage, missing headers, unneeded features. | Hardening baselines; least functionality; security headers; config review. |
| A06 | Vulnerable & Outdated Components | Known-CVE libraries, unsupported versions, no inventory. | SBOM + SCA (`sast-sca`); patch cadence; remove unused deps. |
| A07 | Identification & Auth Failures | Weak passwords, credential stuffing, broken session mgmt, missing MFA. | MFA; secure session handling; rate-limit/lockout; strong password policy. |
| A08 | Software & Data Integrity Failures | Unsigned updates, insecure deserialization, untrusted CI/CD or plugins. | Verify integrity/signatures; avoid unsafe deserialization; secure pipeline (`supply-chain-security`). |
| A09 | Logging & Monitoring Failures | No audit logs, no alerting, logs missing security events or leaking secrets. | Log security events (no secrets); centralize; alert & monitor; detection (`detection-engineering`). |
| A10 | SSRF | Server fetches user-supplied URLs; cloud metadata reachable. | Allow-list egress; validate/resolve URLs; block internal ranges & metadata endpoints. |
