---
name: threat-actor-profiling
description: >-
  Profile a threat actor or campaign — their TTPs (mapped to MITRE ATT&CK),
  targeting, tooling, infrastructure, and likely intent — to support threat-informed
  defense. Use to understand who might target you and how, and to prioritize defenses.
---

# Goal

An actor/campaign profile that informs defense: what they do (TTPs), who they target,
how they operate, and what that means for your detection and control priorities.

# What to capture

1. **Identity & aliases** — actor/group names across vendors (naming differs);
   suspected motivation (espionage, financial, hacktivism) and sponsorship if assessed.
2. **Targeting** — sectors, geographies, and victimology; whether your org fits the
   pattern (relevance to *you* is the point).
3. **TTPs** — map observed behaviors to **MITRE ATT&CK** across the lifecycle (initial
   access → impact); note signature techniques and tooling/malware families.
4. **Infrastructure** — typical C2, hosting, domains/certs patterns (link via
   `ioc-enrichment`).
5. **Framing** — use the Diamond Model (adversary–capability–infrastructure–victim)
   and Kill Chain to structure the picture; note confidence and gaps.

# Steps

1. Aggregate reporting and your own telemetry/incidents (`dfir`); reconcile aliases.
2. Build the ATT&CK technique set and tooling profile; assess confidence per claim.
3. Assess relevance to your environment and which of their TTPs you can/can't detect.
4. Translate to action: detection priorities (`detection-engineering:detection-coverage-review`)
   and control/hardening recommendations.

# Output

An actor profile: aliases · motivation · targeting · ATT&CK TTP set · tooling/
infrastructure · relevance-to-us · confidence/gaps · recommended detections &
controls. Use `security-reporting`; visualize the ATT&CK profile with
`security-diagramming`.

# Notes

The deliverable isn't a biography — it's *what their TTPs mean for your defenses*.
Reconcile vendor aliases (the same group has many names) and be explicit about
confidence and intelligence gaps. Prioritize defending the techniques they actually
use and that you currently can't detect.
