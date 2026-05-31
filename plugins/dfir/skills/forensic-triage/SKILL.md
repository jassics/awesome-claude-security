---
name: forensic-triage
description: >-
  Perform forensic triage on a host or artifacts — collect and analyze disk, memory,
  and log evidence with proper handling, then build an incident timeline. Use to
  investigate a compromised system or scope an incident. Preserve evidence integrity.
---

# Goal

A defensible analysis of the available evidence that answers what happened, when, and
how far it spread — with a timeline and chain of custody intact.

# Evidence sources & artifacts

- **Memory** — running/hidden processes, network connections, injected code,
  credentials, command lines (capture early — most volatile).
- **Disk** — filesystem timeline, prefetch/shimcache/amcache (Windows), bash history/
  systemd/cron (Linux), browser/registry artifacts, deleted-file recovery.
- **Persistence** — services, scheduled tasks, run keys, startup, WMI, webshells.
- **Logs** — auth/security, EDR, process creation, PowerShell, web/proxy, DNS,
  firewall/netflow; central SIEM.
- **Network** — connections, beaconing patterns, DNS, captured traffic.

# Steps

1. **Preserve first** — respect order of volatility (see `incident-response`
   reference); work on copies; hash and log every item (chain of custody).
2. **Triage** — quick wins: suspicious processes, persistence, recent logons, new
   accounts, anomalous network. Identify the foothold.
3. **Build a timeline** — normalize timestamps (UTC), correlate across sources into a
   single chronology of attacker actions.
4. **Scope** — pivot on IOCs/accounts/hosts to find lateral movement and the full
   set of affected systems; estimate dwell time.
5. **Map to ATT&CK** — tag observed techniques for clarity and detection follow-up.

# Output

A triage report: evidence collected (with hashes) · key artifacts · timeline · scope/
dwell time · ATT&CK techniques · IOCs (hand to `ioc-development`). Use
`security-reporting`; visualize the timeline/attack path with `security-diagramming`.

# Notes

Preserve before you analyze — and capture memory early, it's gone on reboot. A
correct, source-correlated **timeline** in UTC is the backbone of the investigation.
Maintain chain of custody if the findings might be used in legal/HR proceedings.
