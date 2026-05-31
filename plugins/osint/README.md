# osint

Open-source intelligence and reconnaissance. Map an organization's **external
footprint / attack surface**, discover **exposures** (leaked credentials, exposed
services, public data), and run **people/social recon** for authorized social-
engineering assessments.

A **domain** plugin; the recon front-end for `pentester` and `red-team`. Also
strengthens defensive **attack-surface management**. Passive/public-source recon;
use within an authorized scope.

## Install

```
/plugin install osint@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/osint:osint-footprinting` | Map a target org's external footprint and attack surface from public sources. |
| `/osint:exposure-discovery` | Find exposed assets, leaked credentials/secrets, and public data exposure. |
| `/osint:people-osint` | Recon people/org structure for authorized social-engineering assessment. |

## Pairs well with

`network-security` (active follow-up on discovered hosts), `pentester` / `red-team`
(engagement recon), `threat-intelligence` (infrastructure pivoting),
`security-reporting`.
