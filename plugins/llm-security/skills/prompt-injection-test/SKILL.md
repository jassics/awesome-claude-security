---
name: prompt-injection-test
description: >-
  Test an LLM feature for direct and indirect prompt injection using a structured
  payload set, then record what succeeded and how to mitigate it. Use when
  assessing a chatbot, copilot, RAG app, or agent for input-handling weaknesses.
  Authorized testing only.
---

# Goal

Evidence-backed findings on whether the target can be made to ignore its
instructions, leak its system prompt, exfiltrate data, or misuse tools — via
direct or indirect injection.

# Prerequisites

- Authorization to test the application.
- Knowledge of the input surfaces: direct user input AND indirect channels the
  model ingests (RAG documents, retrieved web pages, emails, file contents, tool
  outputs, image alt-text/metadata).

# Test classes

1. **Direct injection** — adversarial instructions in user input:
   - Instruction override ("ignore previous instructions and …").
   - System-prompt extraction ("repeat the text above / your instructions").
   - Role/format breaking, delimiter confusion, encoded/obfuscated instructions.
2. **Indirect injection** — instructions planted in content the model later reads:
   - Poisoned RAG document or knowledge-base entry.
   - Hidden text in a web page/email/file the agent fetches.
   - Tool output crafted to carry instructions back into context.
3. **Goal hijacking & exfiltration** — make the model send data to an
   attacker-controlled sink (markdown image URL, tool call, link).
4. **Tool/agency abuse** — induce an unintended tool action (see also LLM06).

# Steps

1. Enumerate input surfaces (direct + indirect).
2. Run payloads per class; for indirect, plant content in a channel the app
   ingests and trigger normal use.
3. Record outcome per payload: blocked / partial / succeeded, with the exact
   request and response as evidence. Redact real secrets.
4. Note which control failed (no input segregation, output not constrained, tool
   over-privileged) — that drives the fix.
5. Rank findings and propose mitigations (instruction/data separation, output
   schemas, allow-lists, human-in-the-loop, least-privilege tools, content
   provenance on RAG).

# Output

A results table: payload class · payload summary · channel · result · evidence ·
mitigation. Route confirmed issues through `security-reporting:finding`.

# Notes

Indirect injection is the higher-impact, more-missed class — always test the
RAG/agent ingestion paths, not just the chat box. Keep payloads benign in effect
(prove the control gap; don't cause real damage).
