# network-security

Network security — offensive and defensive. Run an **authorized network
penetration test** (discovery → enumeration → exploitation → lateral movement),
review **segmentation and firewall** architecture, and assess **protocols and
services** for weaknesses (cleartext, weak crypto, insecure services).

A **domain** plugin; companion to `pentester` and member of a fuller offensive
stack. Active testing is for authorized engagements only.

## Install

```
/plugin install network-security@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/network-security:network-pentest` | Run an authorized network penetration test end to end. |
| `/network-security:network-segmentation-review` | Review segmentation, firewall/ACL rules, and zero-trust architecture. |
| `/network-security:protocol-security-review` | Assess network protocols/services for weaknesses (cleartext, weak crypto, exposure). |

## Pairs well with

`osint` (external recon), `pentester` / `red-team` (engagement context),
`cloud-security` (cloud network), `security-reporting`, `security-diagramming`.
