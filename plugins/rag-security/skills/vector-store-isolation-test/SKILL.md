---
name: vector-store-isolation-test
description: >-
  Test that retrieval enforces per-user / per-tenant authorization so one user
  cannot retrieve another's documents through the RAG system. Use on an authorized
  multi-tenant or multi-user RAG app to validate access control on retrieval.
---

# Goal

Evidence on whether the retrieval layer leaks documents across users/tenants —
the highest-impact RAG confidentiality failure (OWASP LLM08 / LLM02).

# Prerequisites

- Authorization, and ideally two test identities (User A and User B / Tenant A and
  Tenant B) with distinct, identifiable documents.

# Test cases

1. **Direct cross-tenant retrieval** — as User A, ask questions whose best answers
   live only in User B's documents. Does any B content surface?
2. **Filter bypass** — if isolation relies on a client-supplied filter/namespace,
   try altering or omitting it. Is authorization enforced server-side?
3. **Relevance-driven leakage** — craft queries semantically close to B's private
   docs to see if relevance overrides authorization.
4. **Metadata/citation leak** — even if content is withheld, are titles, sources,
   or snippets exposed via citations or errors?
5. **Embedding inversion (if applicable)** — can returned embeddings or similarity
   responses be used to reconstruct unauthorized source text?

# Steps

1. Seed distinct, labeled documents under each identity.
2. Authenticate as User A and run the cases above; never use B's session to "prove"
   A's access.
3. Record per case: isolated / partial leak / full leak, with evidence (query,
   surfaced content/metadata, response).
4. Identify the gap: client-side-only filtering, retrieve-then-(not)-filter,
   shared index without ACLs.

# Output

A results table: case · result · leaked element · evidence · mitigation
(authorize-then-retrieve, per-tenant namespaces, server-side ACL enforcement).
Confirmed leaks → `security-reporting:finding` (rate severity high+).

# Notes

Authorization must be enforced on the **server** at retrieval time and tied to the
authenticated caller — never trust a client-provided tenant/filter. Test the
metadata/citation path too; it leaks even when document bodies are withheld.
