---
description: Triage a SOC alert end-to-end — validate, enrich, decide, and escalate or close with rationale.
argument-hint: [alert / detection name + context]
---

Triage this alert: **$ARGUMENTS**

Walk the triage, using installed skills (note any whose plugin is missing):

1. **Triage** — `/soc-siem:alert-triage` to validate the alert, gather the surrounding telemetry, and judge true vs. false positive.
2. **Enrich** — `/threat-intelligence:ioc-enrichment` on any indicators (IPs, domains, hashes) to add reputation and context.
3. **Map** — `/security-knowledge:attack-lookup` to tag the behavior with its ATT&CK technique.
4. **Decide** — close (with reason) if benign; otherwise escalate. State the tier, severity, and what the next responder needs.
5. **Hand off / report** — escalate to `/security-analyst:investigate` for deeper analysis, or capture a short `/security-reporting:finding` if actionable. Note detection-tuning feedback for `detection-engineering`.

For deep execution, hand off to the `soc-analyst` agent. Every verdict needs evidence and a one-line rationale — no "looks suspicious, escalating" without specifics.
