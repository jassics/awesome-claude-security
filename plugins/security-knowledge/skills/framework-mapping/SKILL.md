---
name: framework-mapping
description: >-
  Map a finding, control, or requirement across security frameworks — CWE, NIST CSF
  & SP 800-53, CIS Controls, ISO/IEC 27001 — so one piece of work can be expressed in
  whichever framework the audience uses. Use when a finding needs a CWE, or when
  aligning controls/gaps across compliance frameworks.
---

# Goal

A finding or control expressed consistently in the frameworks the audience cares
about — a CWE for the bug, and the corresponding control IDs for GRC/audit — without
forcing bad mappings.

# Steps

1. **Classify the root cause**, not the symptom — a weakness type maps to **CWE**
   (e.g., SQL injection → CWE-89; missing authz → CWE-862). That's the engineering
   anchor.
2. **Translate to the target framework(s)**:
   - **NIST CSF 2.0** functions (Govern, Identify, Protect, Detect, Respond, Recover)
     for program-level framing.
   - **NIST SP 800-53** control families for federal/detailed control mapping.
   - **CIS Controls v8** for prioritized, implementable safeguards.
   - **ISO/IEC 27001:2022 Annex A** for ISMS/certification framing.
   See `reference.md` for the families and common crosswalks.
3. **Map deliberately** — use authoritative crosswalks where they exist (e.g., 800-53
   ↔ CSF, CIS ↔ multiple). Note mapping confidence; flag "no clean equivalent" rather
   than inventing one.
4. **Cite versions** — frameworks revise (CSF 1.1→2.0, ISO 27001:2013→2022); state the
   edition.

# Output

A mapping row per item: root cause · CWE · NIST CSF · 800-53 family/control · CIS
Control · ISO 27001 Annex A · confidence. For gap assessments and registers route to
`grc`; for exec framing to `ciso-toolkit`/`security-reporting`.

# Notes

Map root cause, not symptom — the CWE for "what's actually wrong" drives every other
mapping. Crosswalks are approximate; over-precise control mappings mislead auditors.
Always cite the framework edition. See `reference.md` for families and crosswalk
pointers.
