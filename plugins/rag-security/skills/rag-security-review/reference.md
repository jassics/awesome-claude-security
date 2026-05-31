# Reference: RAG security review

Per-stage checks and mitigations for `rag-security-review`. Maps to the OWASP Top
10 for LLM Applications (LLM02 disclosure, LLM04 poisoning, LLM08 vector/embedding).

## 1. Ingestion

- [ ] What sources feed the corpus? Which are attacker-influenceable (uploads,
      crawled web, email/tickets, third-party feeds)?
- [ ] Is ingested content validated/sanitized? Is provenance recorded?
- [ ] Can a low-privilege user plant content that high-privilege users will retrieve?
- **Mitigations:** source allow-listing, content review/sanitization on ingest,
  provenance/trust labels, quarantine for untrusted sources, signing for trusted docs.

## 2. Embedding

- [ ] Where does the embedding model run; who can call it?
- [ ] Could stored embeddings be inverted to reconstruct sensitive source text?
- [ ] Are embeddings of sensitive docs stored with the same protection as the docs?
- **Mitigations:** treat embeddings as sensitive as their source; access-control the
  embedding endpoint; encrypt at rest; avoid embedding secrets/PII unnecessarily.

## 3. Vector store

- [ ] Is the index partitioned per tenant/user, or shared with filter-only separation?
- [ ] Are retrieval filters enforced server-side and tied to the caller's identity
      (not just passed by the client)?
- [ ] Who can write/update/delete vectors? Can that be abused to poison results?
- **Mitigations:** hard partitioning or per-tenant namespaces; server-side authz on
  retrieval; least-privilege write access; integrity monitoring of the index.

## 4. Retrieval

- [ ] Does retrieval enforce the *requester's* authorization on every candidate doc?
- [ ] Can crafted queries surface unrelated/unauthorized documents?
- [ ] Is there a cap on how much retrieved content enters the prompt?
- **Mitigations:** authorize-then-retrieve (or post-filter with the user's ACLs);
  per-user/tenant scoping; monitor anomalous retrieval; bound context size.

## 5. Prompt assembly

- [ ] Is retrieved content clearly delimited as **data**, not instructions?
- [ ] Could a retrieved document contain instructions the model will follow
      (indirect prompt injection)?
- [ ] Are tool calls / actions reachable from content-influenced generations?
- **Mitigations:** strong instruction/data separation, structured/delimited context,
  output schemas, least-privilege tools, human-in-the-loop for sensitive actions.
  Test with `retrieval-poisoning-test`.

## 6. Generation & output

- [ ] Are citations/grounding accurate, or can the model fabricate sources?
- [ ] Does output echo sensitive context (other users' data, secrets)?
- [ ] Is output sanitized before it hits downstream sinks (HTML, code, queries)?
- **Mitigations:** require and verify citations; output filtering for sensitive data;
  treat output as untrusted downstream (see `llm-security` LLM05).

## Cross-cutting

- Cost/availability: bound retrieval volume and query rate (LLM10).
- Logging: record retrieval decisions for audit and abuse detection.
- Multi-tenant: test as user A trying to reach user B's data — the highest-impact
  RAG failure.
