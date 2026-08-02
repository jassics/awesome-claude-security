---
name: prd-security-injection
description: >-
  Read a PRD, feature brief, or an AI coding assistant's plan/prompt that has no
  security content, and inject concrete, testable security requirements and an
  acceptance checklist back into it — before code is written. Use for "vibe coded"
  or fast/AI-assisted features where security was never mentioned in the prompt,
  PRD, or design doc, not for reviewing a design that already exists (that's
  `security-design-review`).
---

# Goal

A PRD/feature-prompt/agent-plan that had zero security content now carries explicit,
non-negotiable security requirements proportionate to what the feature actually
does — injected before implementation starts, not discovered after.

# Why this exists

`security-design-review` assumes a design already exists to review. The common
failure mode with fast/AI-assisted ("vibe coded") development is earlier: security
is simply never in the prompt, PRD, or plan, so it's absent from what gets built and
there's nothing yet to "review." This skill intercepts that gap — it works on a PRD
draft, a one-paragraph feature brief, or the plan an AI coding agent is about to
execute against.

# Steps

1. **Read the brief** and identify: what data it touches (PII, credentials, payment,
   internal-only), what trust boundaries it crosses (new external integration, new
   API surface, third-party data ingestion), and what privileged actions it performs
   (auth changes, admin/elevated actions, file upload, money movement, agentic/
   tool-calling capability).
2. **Map informally** against the categories that matter for *this* feature only —
   don't run a full OWASP Top 10 / ASVS pass, just the categories the brief actually
   touches: authentication, authorization, input validation, cryptography/secrets,
   logging/audit, rate limiting, data retention.
3. **Write 1–3 concrete requirements per touched category**, in PRD-native language
   a product author or coding agent can paste in as-is:
   - Weak: "consider security for file uploads."
   - Strong: "reject uploads over 10MB and outside an allow-listed MIME/extension
     set; store outside the webroot; generate a random filename; scan before
     serving."
4. **Add a short security acceptance checklist** — the feature isn't done until each
   item is checked, sized to the feature (3–6 items typical, not a generic 30-item
   list).
5. **Flag for escalation** if the brief's blast radius warrants more than
   requirements injection: a new authorization boundary, a new external/third-party
   integration, or new agentic/tool-calling capability should route to a full
   `security-design-review` (or `threat-modeling:stride`/`maestro` for multi-agent
   scope) instead of stopping here.

# Output

- **Requirements block** — ready to paste into the PRD or the agent's prompt/plan,
  grouped by category, each requirement concrete and testable.
- **Acceptance checklist** — short, feature-sized.
- **Escalation flag** — yes/no + which deeper skill to run, with the one-line reason.

# Notes

This is deliberately lightweight and front-loaded: the point is catching "security
was never in the room" before code exists, not substituting for a real design
review on anything high-risk. Use it equally on a human-written PRD and on the
prompt/plan an AI coding agent is about to act on — the injection point is the same
either way: before generation, not after.
