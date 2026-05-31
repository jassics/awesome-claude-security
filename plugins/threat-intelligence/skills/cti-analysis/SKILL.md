---
name: cti-analysis
description: >-
  Run the cyber threat intelligence lifecycle for a question or dataset — direction,
  collection, processing, analysis with structured techniques, and dissemination —
  to produce an assessed, actionable intelligence product. Use to turn raw threat
  data into decision-useful intelligence for a defined audience.
---

# Goal

An intelligence product that answers a specific requirement, states assessments with
calibrated confidence, and tells the consumer what to do — not just a pile of data.

# The intelligence lifecycle

1. **Direction** — define the intelligence requirement and the audience (SOC, IR,
   leadership). What decision will this inform? This sets relevance.
2. **Collection** — gather from the right sources (internal telemetry/`dfir`, OSINT,
   feeds, ISAC/sharing, vendor reports). Track source reliability.
3. **Processing** — normalize, deduplicate, translate, and structure (IOCs, TTPs);
   map to ATT&CK.
4. **Analysis** — apply structured analytic techniques (e.g. Analysis of Competing
   Hypotheses) to reduce bias; use the Diamond Model and Kill Chain to frame
   adversary activity; assign confidence and source-reliability ratings.
5. **Dissemination** — deliver in the form/altitude the audience needs (strategic /
   operational / tactical) with clear, actionable recommendations.
6. **Feedback** — capture whether it met the requirement; refine.

# Steps

1. Pin the requirement and audience first; scope collection to it.
2. Process and map data to ATT&CK; enrich indicators (`ioc-enrichment`).
3. Analyze with explicit hypotheses and calibrated confidence (distinguish fact vs.
   assessment vs. assumption).
4. Produce the right product for the audience with recommended actions.

# Output

An intelligence product: requirement · key judgments (with confidence) · supporting
evidence · ATT&CK/Diamond framing · recommendations · sources (with reliability).
Use `security-reporting`; tactical output feeds `detection-engineering`.

# Notes

Intelligence is requirement-driven and decision-oriented — data without a consumer
and a recommendation isn't intelligence. State confidence explicitly and separate
fact from assessment from assumption. Match altitude to audience: leadership wants
strategic implications, the SOC wants tactical TTPs/IOCs.
