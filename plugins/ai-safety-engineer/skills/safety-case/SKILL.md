---
name: safety-case
description: >-
  Assemble a structured assurance / safety case for deploying an AI system — an
  explicit argument that it is acceptably safe for its context, backed by evidence
  (harm model, evals, guardrails, fairness, governance). Use to support a
  go/no-go deployment decision or an audit/sign-off.
---

# Goal

A defensible safety case: a top-level claim that the system is acceptably safe for
its intended use and context, decomposed into arguments, each supported by concrete
evidence and with residual risks stated honestly.

# Structure (claims → arguments → evidence)

1. **Top claim** — "System X is acceptably safe to deploy for use case Y in context
   Z," with the acceptance criteria and who owns the decision.
2. **Sub-claims / arguments** — typically:
   - Harms are identified and bounded (evidence: `ai-safety:harm-modeling`).
   - Safety behavior is measured and meets thresholds (evidence:
     `ai-safety:safety-evaluation`, `ai-safety:safety-red-team`).
   - Treatment is equitable (evidence: `ai-safety:bias-fairness-assessment`).
   - Guardrails and human oversight are adequate (evidence:
     `ai-safety:guardrail-review`).
   - Governance, monitoring, and incident response are in place (evidence:
     `ai-safety:responsible-ai-assessment`).
3. **Evidence** — link each argument to the actual artifacts/results; note their
   date, scope, and limitations.
4. **Residual risk & conditions** — what remains, why it's acceptable, and the
   conditions/monitoring/kill-switches that keep it acceptable post-deployment.

# Steps

1. State the deployment context and acceptance criteria first (they set the bar).
2. Build the argument tree; for each leaf, attach evidence or mark it as a gap.
3. Make gaps explicit — a safety case with honest gaps beats one that hides them.
4. Conclude with a clear go / no-go / go-with-conditions recommendation.

# Output

A safety-case document (claims → arguments → evidence → residual risk →
recommendation). Render the argument tree with `security-diagramming` and produce
the document + executive summary with `security-reporting`.

# Notes

A safety case is an honest argument, not a checklist or a rubber stamp. Unsupported
arguments and unaddressed residual risks are the point — surface them so the
decision-maker owns them explicitly.
