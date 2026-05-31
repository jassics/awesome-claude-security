# Reference: OWASP Top 10 for LLM Applications

Working reference for the `owasp-llm-top10` skill. Categories follow the OWASP
GenAI Security Project "Top 10 for LLM Applications" (2025 list). Verify against
the latest published list at genai.owasp.org, as identifiers evolve.

| ID | Category | What to look for | Mitigations |
| --- | --- | --- | --- |
| LLM01 | **Prompt Injection** | Untrusted text (user input, retrieved docs, tool output, web pages) altering model behavior; instruction override; indirect injection via RAG/email/files. | Treat all model input as untrusted; segregate instructions from data; constrain with system prompts + output schemas; human-in-the-loop for sensitive actions; input/output filtering; least-privilege tools. |
| LLM02 | **Sensitive Information Disclosure** | Secrets/PII in prompts, training data, or context; model echoing system prompt or other users' data. | Data minimization; redact/scrub inputs; access controls on retrieval; don't put secrets in prompts; output filtering; per-tenant isolation. |
| LLM03 | **Supply Chain** | Compromised base models, poisoned datasets, malicious plugins/adapters, tampered model artifacts. | Verify model provenance/signatures; pin and scan dependencies; vet plugins; SBOM for the AI stack; trusted registries. |
| LLM04 | **Data and Model Poisoning** | Tampered training/fine-tune/RAG data; backdoors; biased or attacker-influenced corpora. | Validate/curate data sources; provenance tracking; anomaly detection; isolate and review RAG ingestion; integrity checks. |
| LLM05 | **Improper Output Handling** | LLM output passed unsanitized to downstream systems (SQL, shell, HTML/JS, eval, API calls) → XSS/SSRF/SQLi/RCE. | Treat output as untrusted; encode/validate before use; parameterized queries; sandbox execution; never `eval` raw output. |
| LLM06 | **Excessive Agency** | Agent/tools with too much permission, autonomy, or functionality; unchecked actions with side effects. | Least-privilege tools; minimize functionality; require approval for high-impact actions; scope tokens; rate/spend limits. |
| LLM07 | **System Prompt Leakage** | System prompt extractable; secrets or authz logic embedded in the system prompt. | Don't store secrets/authz decisions in prompts; enforce authorization in code; assume the prompt is discoverable. |
| LLM08 | **Vector and Embedding Weaknesses** | RAG: embedding inversion, cross-tenant retrieval, poisoned vectors, retrieval of unauthorized docs. | Access-control retrieval per user/tenant; validate ingested content; isolate vector stores; monitor retrieval; partition indexes. |
| LLM09 | **Misinformation** | Hallucinated facts, unsafe code suggestions, overreliance without verification. | Ground with retrieval + citations; constrain claims; human review for high-stakes output; communicate uncertainty. |
| LLM10 | **Unbounded Consumption** | Resource/cost exhaustion, denial-of-wallet, model extraction via high-volume querying. | Rate limits, quotas, timeouts, spend caps; input size limits; abuse detection; throttle expensive operations. |

## Quick test ideas per category

- LLM01 — see `prompt-injection-test` (direct + indirect payload set).
- LLM05 — feed output that contains `<script>`, `'; DROP TABLE`, `$(...)`, SSRF
  URLs and trace where it lands downstream.
- LLM06 — enumerate tools the agent can call; check whether destructive/external
  actions require confirmation; test scope of tokens.
- LLM07 — attempt system-prompt extraction; check whether any authz/secret is in it.
- LLM08 — as user A, try to retrieve user B's documents; ingest a poisoned doc and
  see if it influences answers.
- LLM10 — measure cost/latency under large/looping inputs; check for caps.
