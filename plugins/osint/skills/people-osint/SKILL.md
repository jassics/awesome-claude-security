---
name: people-osint
description: >-
  Gather people- and organization-focused OSINT for an authorized social-engineering
  assessment — org structure, roles, contact patterns, and public footprint that
  inform realistic phishing/pretext scenarios. Use only within an authorized
  engagement; focus on assessing susceptibility and improving awareness.
---

# Goal

Enough organizational and personnel context to design realistic social-engineering
test scenarios (and to inform defensive awareness) — without overcollecting or
crossing ethical/legal lines.

# Scope & ethics first

- Only within an **authorized** engagement with agreed rules of engagement.
- Collect from **public** sources; gather the **minimum** needed for the assessment.
- The objective is to **measure susceptibility and improve awareness/controls**, not
  to harm or harass individuals. Handle personal data with care; minimize and protect
  it; respect privacy law.

# What to gather (organization-centric)

1. **Structure & roles** — departments, reporting lines, key functions (finance, IT,
   HR — common phishing targets), and high-value roles.
2. **Contact patterns** — corporate email format, naming conventions, public contact
   info, out-of-office/role mailboxes.
3. **Public footprint** — professional profiles, conference talks, public posts that
   reveal tooling, processes, or pretext hooks (events, vendors, projects).
4. **Pretext material** — current initiatives, partners, and vendors that make a
   believable, testable scenario.

# Steps

1. Confirm authorization and RoE; define what's in scope and off-limits.
2. Collect organization-level context and the email/naming pattern.
3. Build realistic, role-appropriate scenarios (e.g. vendor/IT/HR themes) for the
   authorized phishing/vishing test.
4. Keep records minimal and protected.

# Output

An assessment-support pack: org/role map · email/naming pattern · candidate pretext
themes · suggested target roles (by function, not gratuitous personal detail). Use
`security-reporting`; results inform awareness training and email controls.

# Notes

Stay authorized, public-source, and minimal — this measures and improves resilience,
it is not a license to profile or harm people. Finance/IT/HR are common targets;
weak SPF/DMARC (see `exposure-discovery`) makes spoofing easier and is a key
defensive fix.
