# Reference: control & weakness frameworks

Anchors + crosswalk pointers. Cite the edition; frameworks revise. For authoritative
crosswalks use the source mappings (NIST OLIR, CIS mappings, ISO Annex A).

## CWE — weakness taxonomy (the engineering anchor)

Common, high-signal CWEs:

- **CWE-79** Cross-site Scripting (XSS) · **CWE-89** SQL Injection · **CWE-78** OS
  Command Injection · **CWE-94** Code Injection
- **CWE-22** Path Traversal · **CWE-918** SSRF · **CWE-611** XXE
- **CWE-287** Improper Authentication · **CWE-862** Missing Authorization ·
  **CWE-863** Incorrect Authorization · **CWE-639** IDOR (authorization bypass)
- **CWE-352** CSRF · **CWE-434** Unrestricted File Upload · **CWE-502** Deserialization
  of Untrusted Data
- **CWE-798** Hard-coded Credentials · **CWE-209** Sensitive Info in Error ·
  **CWE-200** Exposure of Sensitive Information
- **CWE-1188 / CWE-16** Insecure/Misconfiguration · **CWE-732** Incorrect Permission
  Assignment

Reference sets: **CWE Top 25** (most dangerous) and **OWASP→CWE** mappings (each OWASP
category lists its CWEs).

## NIST Cybersecurity Framework (CSF) 2.0 — functions

`GV` Govern · `ID` Identify · `PR` Protect · `DE` Detect · `RS` Respond · `RC` Recover.
Program-level language for leadership; each function has categories/subcategories that
crosswalk to 800-53 and CIS.

## NIST SP 800-53 (Rev 5) — control families (selected)

`AC` Access Control · `AU` Audit & Accountability · `CM` Configuration Management ·
`CP` Contingency Planning · `IA` Identification & Authentication · `IR` Incident
Response · `RA` Risk Assessment · `SC` System & Comms Protection · `SI` System &
Information Integrity · `SR` Supply Chain Risk Management. (Detailed/federal mapping.)

## CIS Controls v8 — prioritized safeguards (18 controls)

1 Inventory of Enterprise Assets · 2 Inventory of Software · 3 Data Protection ·
4 Secure Configuration · 5 Account Management · 6 Access Control Management ·
7 Continuous Vulnerability Management · 8 Audit Log Management · 9 Email/Web Browser
Protections · 10 Malware Defenses · 11 Data Recovery · 12 Network Infrastructure
Management · 13 Network Monitoring & Defense · 14 Security Awareness · 15 Service
Provider Management · 16 Application Software Security · 17 Incident Response ·
18 Penetration Testing. (Implementation Groups IG1–IG3 prioritize by org maturity.)

## ISO/IEC 27001:2022 — Annex A control themes

93 controls in 4 themes: **A.5 Organizational** · **A.6 People** · **A.7 Physical** ·
**A.8 Technological**. ISMS/certification framing.

## MITRE DEF3ND — defensive countermeasures

DEF3ND is MITRE's countermeasure framework, technique-mapped to **ATT&CK** (see
`attack-lookup`) — it answers "what defensive control stops/detects this attacker
technique," complementing ATT&CK's "what does the attacker do."

Five top-level tactics: **Harden** (reduce attack surface) · **Detect** (identify
adversary activity) · **Isolate** (restrict lateral movement/access) · **Deceive**
(mislead the adversary) · **Evict** (remove adversary presence).

Example technique ↔ countermeasure pairs:

- ATT&CK **T1055** Process Injection ↔ DEF3ND **D3-PSA** (Process Spawn Analysis) /
  **D3-PMAD** (Process Memory Anomaly Detection) — Detect.
- ATT&CK **T1078** Valid Accounts ↔ DEF3ND **D3-UBA** (User Behavior Analysis) /
  **D3-MFA** (Multi-factor Authentication) — Detect / Harden.
- ATT&CK **T1021** Remote Services (lateral movement) ↔ DEF3ND **D3-NI**
  (Network Isolation) / **D3-ANCI** (Authentication Cache Invalidation) — Isolate.

Cite the DEF3ND technique ID alongside the ATT&CK ID it defends against; treat exact
D3FEND IDs as approximate if you're not certain — confirm against the current
d3fend.mitre.org taxonomy for precision-critical work (e.g. detection engineering
rule justification, control-gap audits).

## Crosswalk pointers

- **800-53 ↔ CSF**: NIST provides subcategory-to-control mappings (and OLIR catalog).
- **CIS ↔ 800-53 / ISO 27001 / CSF**: CIS publishes mappings per safeguard.
- **OWASP ↔ CWE**: each OWASP Top 10 category enumerates contributing CWEs.
- Treat all crosswalks as *approximate* — confirm against the source mapping and note
  confidence. Route gap assessments/registers to `grc`.
