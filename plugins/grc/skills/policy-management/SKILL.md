---
name: policy-management
description: >-
  Develop or review security governance documents — policies, standards, procedures,
  and guidelines — aligned to a framework and the organization's risk, with a clear
  hierarchy, ownership, and lifecycle. Use to write, assess, or rationalize a security
  policy set.
---

# Goal

A coherent, usable governance document set: the right policies/standards/procedures,
aligned to frameworks and risk, written to be followed, with ownership, approval, and
review built in.

# Document hierarchy (keep these distinct)

- **Policy** — the *what* and *why*: high-level intent, mandatory, leadership-approved
  (e.g. Access Control Policy). Stable.
- **Standard** — the *specific requirements* that make a policy measurable (e.g.
  minimum password/MFA standard, crypto standard). Mandatory.
- **Procedure** — the *how*: step-by-step instructions to meet a standard.
- **Guideline** — recommended (non-mandatory) good practice.

# Steps

1. **Inventory & gap** — what governance docs exist vs. what the framework
   (`compliance-assessment`) and risks (`risk-assessment`) require; find gaps,
   overlaps, and stale/contradictory documents.
2. **Draft/revise** — write to the right level in the hierarchy; make requirements
   specific and testable; keep policies concise and durable, push detail to standards/
   procedures. Align to the framework's control language.
3. **Assign ownership & lifecycle** — each document has an owner, an approver, a
   version, an effective date, and a review cadence; define an **exception process**
   (request, risk-accept, expiry).
4. **Make it usable** — accessible, readable, and tied to enforcement (controls that
   actually implement the policy) so it isn't shelfware.

# Output

A policy set or review: document · type (policy/standard/procedure) · owner · status ·
gaps/changes, plus drafts/revisions and an exception process. Use `security-reporting`.

# Notes

Match the document to the level — putting how-to detail in a policy makes it churn;
putting mandatory specifics only in a guideline makes them optional. Policy without an
implementing control and an exception process is shelfware. Reuse framework control
language so policies map cleanly to `compliance-assessment`.
