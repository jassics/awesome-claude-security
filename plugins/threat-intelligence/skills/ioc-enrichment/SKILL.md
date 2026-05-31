---
name: ioc-enrichment
description: >-
  Enrich and pivot on indicators of compromise — resolve context, infrastructure,
  and relationships, assess confidence and relevance, and decide block vs. monitor.
  Use to add analytic value to raw IOCs from an incident, feed, or hunt.
---

# Goal

IOCs turned into context: what each indicator is, how it relates to others and to
known actors, how confident/relevant it is, and what defensive action it warrants.

# Steps

1. **Characterize** each indicator (hash, IP, domain, URL, email, cert/JA3) and its
   provenance and first/last-seen.
2. **Enrich** with context: passive DNS, WHOIS/registration, hosting/ASN,
   certificate and infrastructure overlaps, sandbox/sample reports, reputation, and
   prior sightings in your environment.
3. **Pivot** — use overlaps (shared infrastructure, registrant, TLS certs, malware
   config) to discover related indicators and cluster activity. Map to actors/
   campaigns where evidence supports it.
4. **Assess** — confidence and source reliability; filter benign/shared
   infrastructure (CDNs, sinkholes, common services) to avoid false positives.
5. **Decide** — block / monitor / ignore, with rationale and an expiry/review (atomic
   indicators age out).

# Output

An enriched indicator set: indicator · type · context/infrastructure · related
indicators · actor/campaign link · confidence · action · expiry. Confirmed-malicious
TTPs → `detection-engineering`; clusters → `threat-actor-profiling`.

# Notes

Validate before blocking — shared/benign infrastructure on a blocklist causes
outages. Pivot on durable overlaps (infrastructure, certs, malware config) rather
than treating indicators in isolation. Atomic IOCs decay; set review/expiry so stale
blocks don't accumulate.
