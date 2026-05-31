# sast-sca

Static analysis and software composition analysis for a codebase. Run and **triage
SAST** results, run **SCA** over dependencies (with SBOM), and turn noisy scanner
output into a prioritized, low-false-positive finding set.

A **domain** plugin; member of the planned `appsec-suite`. Works on code you're
authorized to analyze.

## Install

```
/plugin install sast-sca@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/sast-sca:sast-review` | Run/triage static analysis on a codebase and confirm real issues. |
| `/sast-sca:sca-review` | Analyze dependencies/SBOM for known-vulnerable and risky components. |

## Pairs well with

`web-app-security` / `api-security` (confirm SAST findings dynamically),
`supply-chain-security` (roadmap), `security-engineer` (roadmap), `security-reporting`.
