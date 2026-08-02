# security-knowledge

Shared **reference packs** so every plugin maps to the same frameworks the same way.
Look up **MITRE ATT&CK/DEF3ND** tactics/techniques, the **OWASP Top 10** families
(Web/API/LLM/Mobile) and **ASVS** verification levels, crosswalk findings/controls
across **CWE, NIST CSF & 800-53, CIS Controls, and ISO 27001**, and pull a
per-language **secure-coding quick reference** for design/build-time guidance.

A **core**, cross-cutting plugin. It's the consistent *reference/tagging* layer —
the deep testing methodology lives in the domain plugins (`web-app-security`,
`detection-engineering`, etc.); this keeps their IDs and mappings aligned. Heavy
reference data lives in each skill's `reference.md`, loaded on demand.

## Install

```
/plugin install security-knowledge@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/security-knowledge:attack-lookup` | Find/cite the right ATT&CK tactic + technique ID for a behavior, finding, or detection. |
| `/security-knowledge:owasp-reference` | Map to the correct OWASP Top 10 family + category (Web/API/LLM/Mobile). |
| `/security-knowledge:asvs-reference` | Look up the OWASP ASVS chapter + verification level (L1/L2/L3) for a control or finding. |
| `/security-knowledge:framework-mapping` | Crosswalk a finding/control across CWE, NIST CSF/800-53, CIS, ISO 27001, MITRE DEF3ND. |
| `/security-knowledge:secure-coding-kb` | Safe idiom + risky API/library lookup by language/framework, for design/build-time guidance. |

## Pairs well with

Everything — `detection-engineering` and `threat-intelligence` (ATT&CK), the appsec
and genai plugins (OWASP), `grc` and `ciso-toolkit` (framework crosswalks),
`security-reporting` (consistent citations).
