---
name: protocol-security-review
description: >-
  Assess the network protocols and services in use for security weaknesses —
  cleartext protocols, weak/outdated crypto and TLS, insecure or legacy services,
  and man-in-the-middle exposure. Use to review what's running on the network and
  how securely it communicates.
---

# Goal

A view of where network communications and services are weak — unencrypted, weakly
encrypted, or inherently insecure — with concrete upgrades.

# What to check

1. **Cleartext protocols** — Telnet, FTP, HTTP, SNMPv1/2c, unencrypted LDAP/POP3/
   IMAP/SMTP, rsh — anything carrying credentials or data in the clear.
2. **TLS/crypto quality** — protocol versions (no SSLv3/TLS1.0/1.1), weak ciphers,
   expired/self-signed/mismatched certs, weak key exchange, missing forward secrecy.
3. **Insecure/legacy services** — SMBv1, weak NTLM, LLMNR/NBT-NS, deprecated services
   that should be disabled; default credentials/community strings.
4. **MITM exposure** — name-resolution poisoning (LLMNR/NBT-NS/mDNS), missing SMB
   signing, lack of network auth (802.1X), rogue-device risk.
5. **Service exposure** — sensitive services reachable from untrusted zones
   (cross-ref `network-segmentation-review`).

# Steps

1. Inventory services/protocols in scope (from `network-pentest` enumeration or
   config review).
2. Assess each against the checks above; capture protocol, weakness, and exposure.
3. Recommend the secure replacement (e.g. SSH for Telnet, SNMPv3, TLS1.2+/1.3, disable
   SMBv1, enable signing, deploy 802.1X) and where to enforce it.

# Output

A table: service/protocol · weakness · exposure · severity · secure replacement.
Confirmed issues → `security-reporting:finding`.

# Notes

Cleartext credentials on the wire and name-resolution poisoning (LLMNR/NBT-NS) are
classic, high-impact, and common — prioritize them. Disabling legacy protocols
(SMBv1, SSLv3/TLS1.0) is usually a high-value, low-friction win.
