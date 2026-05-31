# Reference: incident response

Working reference for `incident-response`. Anchored on NIST SP 800-61 and SANS
PICERL. Adapt to your org's IR plan and legal/regulatory obligations.

## Severity / triage questions

- What is affected (hosts, accounts, data, services) and how critical?
- Is sensitive/regulated data involved (breach notification triggers)?
- Is the adversary still active? Is there active data exfiltration?
- What is the likely entry vector and blast radius?

## Order of volatility (collect most-volatile first)

1. CPU registers/cache, memory (RAM)
2. Network state (connections, ARP, routing), running processes
3. Disk (filesystem, artifacts)
4. Remote logging / monitoring data
5. Physical config, archival media

## Containment options

- **Network**: isolate host/VLAN, block C2 domains/IPs, null-route, segment.
- **Identity**: disable/rotate compromised accounts and credentials, revoke tokens/
  sessions, force re-auth.
- **Host**: quarantine via EDR, suspend VM (preserves memory), pull from load balancer.
- Balance: speed of containment vs. evidence preservation vs. attacker awareness.

## Eradication checklist

- [ ] Remove malware and tools.
- [ ] Remove persistence (services, tasks, run keys, cron, webshells, startup, WMI).
- [ ] Remove attacker-created accounts and revoke credentials/keys touched.
- [ ] Close the initial access vector (patch, config, phishing control).
- [ ] Confirm no lateral footholds remain.

## Recovery

- Restore from known-good backups/images; validate integrity before reconnect.
- Heightened monitoring for adversary return; staged lifting of containment.
- Verify business functions restored.

## Evidence handling

- Maintain chain of custody; record who/what/when for each item.
- Work on forensic copies; preserve originals with hashes.
- Document timestamps in a consistent timezone (prefer UTC).

## Frameworks

NIST SP 800-61 (Computer Security Incident Handling Guide), SANS PICERL, MITRE
ATT&CK (map observed TTPs), VERIS (incident categorization).
