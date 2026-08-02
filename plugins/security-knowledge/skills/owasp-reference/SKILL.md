---
name: owasp-reference
description: >-
  Look up and map to the right OWASP Top 10 family — Web, API, LLM, or Mobile — and
  give the canonical category ID/name for a finding. Use when you need a consistent
  OWASP reference for tagging findings, scoping a review, or aligning a report across
  the appsec/genai plugins.
---

# Goal

The correct OWASP family and category for a finding or scope, cited consistently — so
reviews and reports across web, API, LLM, and mobile work line up.

# Steps

1. **Pick the right list** by the asset under review:
   - Web app → **OWASP Web Top 10 (2021)**
   - REST/GraphQL API → **OWASP API Security Top 10 (2023)**
   - LLM/GenAI feature → **OWASP Top 10 for LLM Applications (2025)**
   - Mobile app → **OWASP Mobile Top 10 (2024)** + MASVS/MASTG
2. **Map the finding** to the closest category; cite ID + name (e.g., `A01:2021 –
   Broken Access Control`, `API1:2023 – BOLA`, `LLM01 – Prompt Injection`). See
   `reference.md` for all four lists.
3. **Hand off to the deep skill** — the family plugins own the actual testing
   methodology (`web-app-security`, `api-security`, `llm-security`, `mobile-security`);
   this skill is the consistent *reference/tagging* layer.
4. **For control-level verification depth** (not just a Top-10 category tag), see
   `asvs-reference` — OWASP ASVS gives the requirement + level (L1/L2/L3) a finding
   should be checked against.

# Output

The family + category ID/name, a one-line rationale, and a pointer to the relevant
testing skill. For multi-category findings, list each with the primary one first.

# Notes

OWASP lists are versioned and renumber between editions — always cite the year/edition
(A01:2021, API1:2023, LLM01:2025). Don't force a finding into a category it doesn't
fit; "doesn't map cleanly" is a valid, useful answer. See `reference.md` for the full
category lists.
