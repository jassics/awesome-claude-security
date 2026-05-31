# Reference: harm taxonomy & safety frameworks

Working reference for `harm-modeling`. Harm categories synthesize common
responsible-AI taxonomies (NIST AI RMF, EU AI Act, MLCommons AILuminate hazard
taxonomy, OECD AI Principles, major lab usage policies). Verify against the current
published versions — these evolve.

## Harm categories

| Category | Examples | Especially watch for |
| --- | --- | --- |
| **Physical** | Unsafe medical/legal/financial advice; unsafe instructions; safety-critical control errors. | Irreversible harm; high-stakes domains. |
| **Psychological** | Self-harm encouragement, harassment, emotional manipulation, distressing content. | Minors and at-risk users. |
| **Financial** | Faulty advice, scams enabled, automated decisions denying resources. | People who can't absorb loss. |
| **Discrimination / unfairness** | Biased outputs or decisions across protected groups; stereotyping. | Allocative decisions (hiring, lending, housing). |
| **Privacy / dignity** | Exposure of personal data, inference of sensitive attributes, non-consensual content. | Re-identification; intimate imagery. |
| **Misinformation / reliability** | Hallucinated facts, fabricated citations, confidently wrong output. | High-stakes reliance; health, news, law. |
| **Manipulation / autonomy** | Dark patterns, persuasion, deception, undue influence. | Vulnerable or dependent users. |
| **Societal / democratic** | Disinformation at scale, election interference, erosion of trust. | Scale and amplification effects. |
| **Dangerous capabilities / misuse** | Uplift for CBRN, cyber-offense, mass surveillance. | Foreseeable misuse; frontier capability. |
| **Environmental** | Disproportionate compute/energy for the value delivered. | Sustainability commitments. |
| **Labor / economic** | Displacement, degraded work, accountability gaps. | Automation of consequential decisions. |

## Conditions to model (not just intended use)

- **Normal use** — harm arising even when used as designed.
- **Foreseeable misuse** — predictable off-label use; dual-use prompts.
- **Malfunction / error** — hallucination, wrong output, model failure, edge cases.
- **Distribution shift** — inputs/users unlike the design assumptions.
- **Scale / feedback effects** — harms that only emerge at population scale or via
  feedback loops (recommendation spirals, model-trains-on-its-own-output).

## Frameworks to anchor against

| Framework | Use it for |
| --- | --- |
| **NIST AI RMF** (Govern · Map · Measure · Manage) | Lifecycle risk management structure; pairs with `responsible-ai-assessment`. |
| **EU AI Act** (risk tiers: unacceptable / high / limited / minimal) | Risk classification and obligations for the use case. |
| **ISO/IEC 42001** (AI management system) | Organizational governance of AI. |
| **OECD AI Principles** | High-level values: transparency, accountability, human-centered. |
| **MLCommons AILuminate** | Hazard category taxonomy for safety evals (see `safety-evaluation`). |
| **MITRE ATLAS** | Adversarial ML — mostly *security*, cross-reference where misuse overlaps. |

## Severity weighting hints

Weight up: irreversibility, harm to people who can't opt out or consent, harm to
vulnerable populations, and harms amplified by scale. A low-likelihood but
catastrophic/irreversible harm can still be the top item.
