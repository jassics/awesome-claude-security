---
name: secure-by-design-program
description: >-
  Establish or assess an org-wide secure-by-design program — paved roads / golden
  paths with secure defaults, automated guardrails, and developer enablement — so the
  secure way is the default, fast way. Use for engineering-org security strategy at
  scale (not a single system's design).
---

# Goal

A program that makes security the path of least resistance across the engineering
org: secure defaults built into platforms and templates, guardrails that prevent
classes of issues automatically, and developers enabled to build securely without
friction.

# Pillars

1. **Paved roads / golden paths** — blessed, secure-by-default templates, platforms,
   and libraries (service scaffolds, hardened base images, IaC modules, auth/secrets
   handled for you). Make the secure choice the easy default.
2. **Guardrails (automated)** — policy-as-code and platform controls that prevent or
   catch whole classes of issues: CI/CD gates (`security-engineer:secure-pipeline`),
   admission control (`k8s-security`), org-wide cloud guardrails (`cloud-security`),
   secure defaults that are hard to turn off.
3. **Developer enablement** — security champions program, self-service security
   tooling, just-in-time guidance, threat-modeling-as-a-habit (`threat-modeling`),
   and training that targets the org's real defect patterns.
4. **Shift-left integration** — security built into the SDLC and developer workflow,
   not bolted on; fast, actionable feedback in the tools devs already use.
5. **Measurement** — adoption of paved roads, guardrail coverage, escaped-defect and
   mean-time-to-remediate trends; measure the program by outcomes, not policies.

# Steps

1. Assess the current state: where security is friction vs. default; common defect
   classes; existing platforms/templates.
2. Design paved roads and guardrails that eliminate the top defect classes by default.
3. Plan enablement (champions, self-service, training) and shift-left integration.
4. Define adoption/outcome metrics and a phased rollout.

# Output

A secure-by-design program plan: paved roads · guardrails · enablement · integration ·
metrics · phased rollout. Use `security-reporting`; diagram the target developer/
platform flow with `security-diagramming`.

# Notes

Make security the default, not a gate to argue with — friction that developers route
around isn't security. Eliminate whole **classes** of issues via paved roads and
guardrails rather than finding them one by one. Measure adoption and escaped defects,
not the existence of a policy.
