---
name: rag-security-review
description: >-
  Assess a Retrieval-Augmented Generation application end-to-end — ingestion,
  embedding, vector store, retrieval, prompt assembly, and generation — for
  poisoning, data leakage, isolation, and citation-integrity issues. Use when
  reviewing the security of any RAG / knowledge-base-backed LLM feature.
---

# Goal

A structured RAG security assessment that walks each pipeline stage, names the
risks present, and maps mitigations — bridging into the OWASP LLM Top 10
(especially LLM04 poisoning and LLM08 vector/embedding weaknesses).

# Pipeline stages to assess (see `reference.md` for checks per stage)

1. **Ingestion** — what content enters the corpus, from where, with what trust and
   provenance? Can an attacker get content in (user uploads, crawled pages, tickets,
   emails)?
2. **Embedding** — model used, where it runs, and whether embeddings can be
   inverted to recover sensitive source text.
3. **Vector store** — partitioning per tenant/user, access controls on retrieval,
   metadata filtering, and write access.
4. **Retrieval** — does retrieval enforce the requester's authorization? Can it
   return documents the user shouldn't see? Relevance vs. confidentiality.
5. **Prompt assembly** — how retrieved (untrusted) content is combined with the
   system prompt and user query; is content marked as data vs. instructions?
6. **Generation & output** — citation/grounding integrity, sensitive-data echo,
   and downstream output handling.

# Steps

1. Map the pipeline and data sources; identify every place untrusted content
   enters or is retrieved. A quick `llm-security:ai-threat-model` pass helps.
2. Walk each stage using `reference.md`; record finding · severity · evidence ·
   mitigation. Substantiate, don't assert: use `retrieval-poisoning-test` and
   `vector-store-isolation-test` for the testable claims.
3. Rank findings (`threat-modeling:risk-rank`) and summarize top risks.

# Output

A per-stage findings table plus a ranked top-risks list. Route confirmed issues
through `security-reporting:finding`.

# Notes

The decisive RAG question: *can untrusted retrieved content influence trusted
behavior, and can a user retrieve data they're not authorized to see?* Access
control on retrieval and instruction/data separation in the prompt are the two
controls most often missing.
