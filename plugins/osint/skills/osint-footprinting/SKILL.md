---
name: osint-footprinting
description: >-
  Map a target organization's external footprint and attack surface from public
  sources — domains, subdomains, IP ranges, exposed services, technologies, and
  organizational details. Use at the start of an engagement (or for attack-surface
  management) to see what an attacker sees. Authorized scope, public sources.
---

# Goal

A structured, organized map of the target's internet-facing attack surface, built
from public/passive sources, ready to drive testing or defensive remediation.

# What to gather (see `reference.md` for sources)

1. **Domains & subdomains** — root domains, subdomains (passive DNS, CT logs),
   related/typosquat domains.
2. **IP space & hosting** — IP ranges, ASNs, cloud footprint, CDNs.
3. **Exposed services** — internet-reachable hosts/ports/services (passive sources
   like internet-wide scan datasets), web apps, login portals, remote access.
4. **Technologies** — stacks, frameworks, third-party services, email/DNS records
   (SPF/DMARC/MX).
5. **Organizational context** — business units, acquisitions, brands (each expands
   the surface), code repos and public assets.

# Steps

1. Confirm scope (which org/domains are authorized) — stay within it.
2. Collect from public/passive sources; avoid active scanning here (hand live hosts
   to `network-security:network-pentest` if/when authorized).
3. Organize by asset, deduplicate, and flag the most exposed/sensitive (admin
   portals, remote access, forgotten/legacy assets, dev/staging exposed to internet).
4. Map it — an attack-surface mindmap (`security-diagramming:mindmap`).

# Output

An attack-surface inventory: asset · type · service/tech · exposure · source · notes,
plus a prioritized list of where to test (offense) or remediate (defense). Feed
exposures to `exposure-discovery` and live hosts to `network-security`.

# Notes

Footprinting is passive and public-source — it shows the attacker's outside view.
Forgotten/legacy and dev/staging assets exposed to the internet are the highest-value
finds. Acquisitions and alternate brands quietly expand the surface — enumerate them.
Stay within the authorized scope even though sources are public.
