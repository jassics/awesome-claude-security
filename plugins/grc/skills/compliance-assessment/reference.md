# Reference: compliance frameworks

Quick map for `compliance-assessment`. Verify against the current published version
of each framework; details and version numbers change.

| Framework | What it is | Structure / focus |
| --- | --- | --- |
| **ISO/IEC 27001** | ISMS certification standard | Mgmt-system clauses + Annex A controls (organizational, people, physical, technological). Risk-based ISMS. |
| **SOC 2** | AICPA attestation report | Trust Services Criteria: Security (common), plus Availability, Processing Integrity, Confidentiality, Privacy. Type I (design) vs Type II (operating effectiveness over time). |
| **PCI DSS** | Payment-card data security | Prescriptive requirements over the cardholder data environment (CDE); network seg, encryption, access, monitoring, testing. |
| **HIPAA** | US healthcare (PHI) | Security Rule (administrative/physical/technical safeguards), Privacy Rule, Breach Notification. |
| **GDPR** | EU data protection | Lawful basis, data-subject rights, DPIAs, breach notification (72h), privacy by design, processor obligations. |
| **NIST CSF** | Risk-management framework | Functions: Govern, Identify, Protect, Detect, Respond, Recover. Outcome-based; maps to many others. |
| **NIST SP 800-53** | US federal control catalog | Control families (AC, AU, SC, IR, etc.); basis for FedRAMP. |
| **CIS Controls** | Prioritized safeguards | Implementation Groups (IG1–IG3); practical, prioritized. |

## Cross-mapping tips

- Most frameworks share a common control core (access control, crypto, logging,
  IR, vulnerability mgmt, vendor risk). Build one control set and map outward.
- NIST CSF is a good "hub" to map other frameworks to.
- Technical evidence comes from the operational plugins: access/IAM
  (`cloud-security`), vuln mgmt (`sast-sca`), logging/detection
  (`detection-engineering`), IR (`dfir`), hardening (`infrastructure-security`).

## Evidence types auditors expect

Policies & procedures · system configurations · access reviews · logs &
monitoring · ticketing/change records · training records · risk register ·
vendor assessments · pentest/scan reports · incident records.
