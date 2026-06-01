# security-knowledge

Shared **reference packs** so every plugin maps to the same frameworks the same way.
Look up **MITRE ATT&CK** tactics/techniques, the **OWASP Top 10** families
(Web/API/LLM/Mobile), and crosswalk findings/controls across **CWE, NIST CSF &
800-53, CIS Controls, and ISO 27001**.

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
| `/security-knowledge:framework-mapping` | Crosswalk a finding/control across CWE, NIST CSF/800-53, CIS, ISO 27001. |

## Pairs well with

Everything — `detection-engineering` and `threat-intelligence` (ATT&CK), the appsec
and genai plugins (OWASP), `grc` and `ciso-toolkit` (framework crosswalks),
`security-reporting` (consistent citations).
