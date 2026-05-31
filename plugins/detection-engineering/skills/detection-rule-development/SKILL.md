---
name: detection-rule-development
description: >-
  Develop or review a detection rule (Sigma, YARA, KQL/SPL/EQL) for a specific
  behavior or threat, mapped to MITRE ATT&CK, with test cases and false-positive
  tuning. Use when building, porting, or reviewing detections from a TTP, IOC, or
  incident finding.
---

# Goal

A robust, documented detection rule that catches the intended behavior, is mapped to
ATT&CK, has known false positives addressed, and is testable.

# Aim high on the Pyramid of Pain

Prefer detecting **TTPs/behaviors** over brittle atomic indicators (hashes, IPs).
Behavior-based detections cost the adversary more to evade. Use IOC-based rules for
fast wins, but pair them with behavioral coverage.

# Steps

1. **Define what you're detecting** — the specific behavior/technique, the data
   source required (process creation, EDR telemetry, auth logs, DNS, etc.), and the
   ATT&CK technique ID(s).
2. **Confirm log/telemetry availability** — no rule works without the data; note the
   source and any onboarding gap.
3. **Write the rule** — in the target language (Sigma as portable source of truth;
   YARA for files/memory; KQL/SPL/EQL for the SIEM/EDR). Make the logic specific to
   the behavior, not incidental artifacts.
4. **Test** — true positives (does it fire on the behavior? use an emulation like
   Atomic Red Team) and false positives (what benign activity matches?). Tune to cut
   FPs without blinding the rule.
5. **Document** — ATT&CK mapping, data source, FP notes, severity, and response
   guidance for the analyst.

# Output

The rule (in the requested format) plus a metadata block: ATT&CK technique · data
source · test cases · known FPs · severity · triage steps. Add to the detection
library; track coverage with `detection-coverage-review`.

# Notes

A detection without a tuned false-positive story creates alert fatigue and gets
muted — tuning is part of "done." Validate against real telemetry/emulation, not
just by reading the logic. Map every rule to ATT&CK so coverage is measurable.
