---
name: ioc-development
description: >-
  Extract and operationalize indicators (IOCs) and behaviors (IOAs) from an incident
  or sample — atomic, computed, and behavioral — and prepare them for detection,
  blocking, and intel sharing. Use after/within an investigation to turn findings
  into defensive value.
---

# Goal

A structured, prioritized indicator set that drives detection and containment, with
behaviors (not just atomic indicators) captured so the adversary pays to evade.

# Indicator types (climb the Pyramid of Pain)

- **Atomic** — hashes, IPs, domains, URLs, email addresses (easy for the adversary
  to change; useful for fast blocking).
- **Computed** — regexes, YARA conditions, certificate/JA3 hashes, registry/file
  patterns.
- **Behavioral (IOAs / TTPs)** — the actions and techniques (ATT&CK) — the most
  durable and the priority to capture.

# Steps

1. **Extract** from forensic findings/sample: files, network, host, and behavioral
   indicators. Note context (where seen, confidence, observation time).
2. **Validate** — filter out benign/legitimate indicators (e.g. shared CDNs, common
   LOLBins) to avoid false-positive-heavy blocks.
3. **Prioritize** — emphasize behavioral/TTP indicators over fragile atomic ones;
   mark which are safe to block vs. monitor-only.
4. **Operationalize** —
   - Detection: hand TTPs/patterns to `detection-engineering:detection-rule-development`.
   - Blocking: provide atomic indicators for blocklists (with caveats).
   - Intel: structure for sharing (`threat-intelligence`), ideally STIX-friendly.

# Output

An indicator set: indicator · type · context · confidence · block/monitor · ATT&CK
mapping. Feeds `detection-engineering` and `threat-intelligence`.

# Notes

Atomic indicators are cheap to rotate — lead with **behavioral** indicators for
durable defense. Always validate before blocking: a shared IP or common binary on a
blocklist causes outages and alert fatigue. Record confidence so downstream consumers
can weigh each indicator.
