# Reference: OSINT footprinting sources

Source categories for `osint-footprinting`. Use public/passive sources; stay within
the authorized scope.

## Domains & DNS

- Certificate Transparency logs (subdomain discovery).
- Passive DNS datasets; DNS records (A/AAAA/MX/NS/TXT/SPF/DMARC/DKIM).
- WHOIS / registration data; related-domain and typosquat discovery.

## IP space & hosting

- ASN / IP range lookups (RIR data); BGP/route info.
- Cloud-provider IP ranges; CDN identification.

## Exposed services (passive)

- Internet-wide scan datasets (Shodan/Censys-style) for hosts/ports/services and
  banners — passive lookups rather than active scanning.
- Reverse-DNS and virtual-host data.

## Technology & web

- Web technology fingerprints (frameworks, CMS, analytics, third parties).
- robots.txt/sitemaps, JavaScript references, exposed paths (without active abuse).
- Public code repositories and package registries for org assets.

## Organizational

- Corporate structure, subsidiaries, acquisitions, brands and alternate domains.
- Job postings (reveal tech stack and internal tooling).
- Public filings, press, and partner mentions.

## Email & identity hygiene

- SPF/DKIM/DMARC posture (spoofability), MX providers.
- Breach-exposure of corporate domains (hand to `exposure-discovery`).

## Defensive use

The same map is your **attack-surface management** view — track it over time, and
remediate forgotten/legacy/dev assets and weak email auth.
