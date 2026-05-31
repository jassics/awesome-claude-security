---
name: exposure-discovery
description: >-
  Discover an organization's public exposures — leaked credentials and secrets,
  exposed services and storage, source-code/config leaks, and breach data — from
  public sources. Use to find what's already exposed about a target (offense) or to
  reduce your own exposure (defense). Authorized scope.
---

# Goal

A prioritized list of real public exposures that an attacker could use immediately,
with the action to remediate or exploit (within scope) each.

# What to look for

1. **Leaked credentials** — corporate emails/passwords in breach datasets; reused
   credentials; exposed API keys/tokens.
2. **Secrets in code** — keys, tokens, and credentials in public repos, gists,
   package artifacts, CI logs, and historical commits.
3. **Exposed services & storage** — internet-reachable admin panels, databases,
   dashboards; public cloud buckets/blobs; open directories; dev/staging exposed.
4. **Sensitive documents/data** — indexed files, metadata, internal info in public
   caches/archives, paste sites.
5. **Spoofability** — weak SPF/DMARC enabling phishing as the org.

# Steps

1. Confirm scope. Use public/passive sources (breach-exposure services, code search,
   passive scan datasets, archives).
2. Validate findings — confirm a leak is real and current (many are stale/recycled);
   never log into accounts with found credentials unless explicitly authorized.
3. Prioritize by exploitability and impact: live valid credentials and exposed
   data/services first.
4. Recommend action: rotate/revoke leaked secrets, remove/secure exposed assets,
   takedowns, harden email auth.

# Output

An exposure list: exposure · type · source · validity/confidence · impact · action
(rotate/revoke/remove/harden). Confirmed exposures → `security-reporting:finding`
(live credentials and exposed data = high+). Defensively, feed an ASM remediation plan.

# Notes

Validate before acting — many "leaks" are stale or recycled. Treat found credentials
as **rotate/revoke** items; do **not** authenticate with them unless the engagement
explicitly authorizes it. Secrets in git history and public buckets are the most
common high-impact exposures.
