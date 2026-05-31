---
name: host-hardening-review
description: >-
  Review a host/OS (Linux or Windows) or its baseline image against CIS Benchmark
  hardening — accounts, services, network, logging, file permissions, and patching.
  Use to assess server/VM/golden-image hardening you're authorized to review.
---

# Goal

A hardening assessment of the host or base image against a recognized benchmark
(CIS), with findings, severity, and remediation — suitable for building or auditing
a golden image.

# Areas (CIS-aligned)

1. **Accounts & auth** — no unused/default accounts, strong password/lockout policy,
   no empty passwords, sudo/admin scope, SSH config (no root login, key-based).
2. **Services & packages** — minimize installed packages and running services;
   disable unneeded daemons; no legacy/insecure services (telnet, ftp, rsh).
3. **Network** — host firewall on with default-deny; disable uncommon protocols;
   kernel network params (Linux sysctl) hardened.
4. **Filesystem & permissions** — secure mount options, world-writable files, SUID/
   SGID review, sensitive file permissions, separate partitions where applicable.
5. **Logging & audit** — auditd/Event Log configured, time sync, log retention and
   forwarding.
6. **Patching & integrity** — current patch level, automatic updates policy, file
   integrity monitoring, secure boot where relevant.

# Steps

1. Identify OS/version and scope; gather config (a CIS-CAT / OpenSCAP / Lynis scan
   helps) or review the build/image definition.
2. Compare against the matching CIS Benchmark level (L1 baseline / L2 stricter).
3. Record per control: control (CIS ref) · finding · severity · remediation.
4. For images built via IaC, fold fixes back into the build (`iac-security-review`).

# Output

A hardening findings table mapped to CIS controls + ranked gaps. Confirmed issues →
`security-reporting:finding`.

# Notes

Harden the **base image** once and deploy it everywhere rather than patching live
hosts ad hoc — pair with `iac-security-review` so the hardened build is codified.
Pick the CIS level (L1 vs L2) to match the host's role and risk.
