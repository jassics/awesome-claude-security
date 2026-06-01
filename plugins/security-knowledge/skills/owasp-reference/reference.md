# Reference: OWASP Top 10 families

Cite by ID + year/edition. Confirm the current edition at **owasp.org** — these lists
are re-issued periodically.

## OWASP Web Application Top 10 (2021)

| ID | Category |
| --- | --- |
| A01:2021 | Broken Access Control |
| A02:2021 | Cryptographic Failures |
| A03:2021 | Injection (incl. XSS) |
| A04:2021 | Insecure Design |
| A05:2021 | Security Misconfiguration |
| A06:2021 | Vulnerable and Outdated Components |
| A07:2021 | Identification and Authentication Failures |
| A08:2021 | Software and Data Integrity Failures |
| A09:2021 | Security Logging and Monitoring Failures |
| A10:2021 | Server-Side Request Forgery (SSRF) |

→ testing: `web-app-security`

## OWASP API Security Top 10 (2023)

| ID | Category |
| --- | --- |
| API1:2023 | Broken Object Level Authorization (BOLA) |
| API2:2023 | Broken Authentication |
| API3:2023 | Broken Object Property Level Authorization |
| API4:2023 | Unrestricted Resource Consumption |
| API5:2023 | Broken Function Level Authorization (BFLA) |
| API6:2023 | Unrestricted Access to Sensitive Business Flows |
| API7:2023 | Server-Side Request Forgery (SSRF) |
| API8:2023 | Security Misconfiguration |
| API9:2023 | Improper Inventory Management |
| API10:2023 | Unsafe Consumption of APIs |

→ testing: `api-security`

## OWASP Top 10 for LLM Applications (2025)

| ID | Category |
| --- | --- |
| LLM01 | Prompt Injection |
| LLM02 | Sensitive Information Disclosure |
| LLM03 | Supply Chain |
| LLM04 | Data and Model Poisoning |
| LLM05 | Improper Output Handling |
| LLM06 | Excessive Agency |
| LLM07 | System Prompt Leakage |
| LLM08 | Vector and Embedding Weaknesses |
| LLM09 | Misinformation |
| LLM10 | Unbounded Consumption |

→ testing: `llm-security`, `rag-security` (LLM08), `agentic-ai-security` (LLM06),
`mlops-security` (LLM03/LLM04)

## OWASP Mobile Top 10 (2024)

| ID | Category |
| --- | --- |
| M1 | Improper Credential Usage |
| M2 | Inadequate Supply Chain Security |
| M3 | Insecure Authentication/Authorization |
| M4 | Insufficient Input/Output Validation |
| M5 | Insecure Communication |
| M6 | Inadequate Privacy Controls |
| M7 | Insufficient Binary Protections |
| M8 | Security Misconfiguration |
| M9 | Insecure Data Storage |
| M10 | Insufficient Cryptography |

→ testing: `mobile-security` (with MASVS verification + MASTG methodology)

## Notes

- The same class of bug appears across lists (Access Control → A01 / API1+API5 / LLM06;
  SSRF → A10 / API7). Tag in the family that matches the asset.
- OWASP also maintains ASVS (verification standard), MASVS/MASTG (mobile), and the
  CI/CD Top 10 — referenced by `supply-chain-security`.
