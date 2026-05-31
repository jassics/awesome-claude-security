# web-app-security

Web application security testing. Assess against the **OWASP Web Top 10**, test
**access control** (IDOR, privilege escalation), and test for **injection**
(SQLi, XSS, command, template). Methodology-anchored on OWASP WSTG.

A **domain** plugin; member of the planned `appsec-suite`. Authorized testing only.

## Install

```
/plugin install web-app-security@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/web-app-security:owasp-web-top10` | Assess a web app against the OWASP Top 10 (2021). |
| `/web-app-security:access-control-test` | Test authorization: IDOR, BOLA, privilege escalation, forced browsing. |
| `/web-app-security:injection-test` | Test for SQLi, XSS, command, and template injection. |

## Pairs well with

`pentester` (engagement context), `api-security`, `threat-modeling`,
`security-reporting`, `security-diagramming`.
