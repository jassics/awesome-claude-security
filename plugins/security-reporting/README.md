# security-reporting

Turn raw security work into consistent, audience-appropriate deliverables: a
single **finding**, a full **pentest/assessment report**, a **vulnerability
writeup**, or an **executive summary**. Severity is scored with **CVSS v3.1**
and findings carry concrete, testable remediation.

A **core** plugin — domain and role plugins hand their findings here instead of
re-inventing report structure.

## Install

```
/plugin install security-reporting@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/security-reporting:finding` | Write up one finding (severity, evidence, impact, fix). |
| `/security-reporting:pentest-report` | Assemble a full engagement report from findings + scope. |
| `/security-reporting:executive-summary` | Distill results for leadership / board. |
| `/security-reporting:cvss` | Score a vuln with CVSS v3.1 and produce vector + rationale. |

## Pairs well with

`security-diagramming` (embed attack trees / architecture diagrams), every domain
and role plugin (as the reporting backend), and the roadmap `security-integrations`
plugin (publish to Jira/Confluence/Drive).
