# api-security

API security testing for REST and GraphQL. Assess against the **OWASP API Security
Top 10 (2023)** and test **object- and function-level authorization** (BOLA/BFLA) —
the dominant API risks.

A **domain** plugin; member of the planned `appsec-suite`. Authorized testing only.

## Install

```
/plugin install api-security@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/api-security:owasp-api-top10` | Assess an API against the OWASP API Security Top 10 (2023). |
| `/api-security:api-authz-test` | Test BOLA (object-level) and BFLA (function-level) authorization. |

## Pairs well with

`web-app-security` (shared access-control class), `pentester`, `threat-modeling`,
`security-reporting`.
