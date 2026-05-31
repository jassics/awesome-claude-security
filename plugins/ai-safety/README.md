# ai-safety

AI **safety** — distinct from AI security. Security protects an AI system from
**adversaries**; safety prevents the system from **causing harm** to users, third
parties, vulnerable groups, and society, even when no attacker is involved. The
concerns are alignment, harmful content, bias and fairness, reliability/truthfulness,
misuse, human oversight, and responsible-AI governance.

> **Security ≠ Safety.** A perfectly secure model can still be unsafe (e.g. it
> confidently gives dangerous medical advice, or is biased against a group). A
> perfectly safe model can still be insecure (e.g. it leaks data under prompt
> injection). You usually need **both** — pair this with the GenAI security plugins
> ([`genai-suite`](../genai-suite/)).

This is its own first-class **domain**. The role-oriented bundle is
[`ai-safety-engineer`](../ai-safety-engineer/).

## Install

```
/plugin install ai-safety@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/ai-safety:harm-modeling` | Enumerate potential harms of an AI system (the safety analog of threat modeling). |
| `/ai-safety:safety-evaluation` | Design/run a safety eval suite across harm categories with rubrics. |
| `/ai-safety:safety-red-team` | Responsible adversarial testing for harmful/misuse outputs, to drive mitigations. |
| `/ai-safety:bias-fairness-assessment` | Assess a model/feature/dataset for bias and fairness across groups. |
| `/ai-safety:guardrail-review` | Review/design content-safety guardrails, moderation, and refusal behavior. |
| `/ai-safety:responsible-ai-assessment` | Gap-assess against NIST AI RMF / ISO 42001 / EU AI Act and produce a roadmap. |

## Agents

| Agent | Use for |
| --- | --- |
| `ai-safety-reviewer` | A full, multi-step AI safety assessment of a model or feature. |

## Pairs well with

`llm-security` / `genai-suite` (the security counterpart), `threat-modeling`
(harm-modeling is its safety sibling), `security-reporting`, `security-diagramming`.

## Scope

Safety work here is for **building safeguards and reducing harm** — evaluations,
red-teaming to find and fix failures, and governance. Red-teaming is framed to
measure whether safeguards hold, not to produce or retain harmful artifacts.
