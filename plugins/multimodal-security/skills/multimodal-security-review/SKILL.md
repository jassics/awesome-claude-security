---
name: multimodal-security-review
description: >-
  Review a multimodal AI application's input handling and trust boundaries across
  every modality it accepts (image, audio, video, document), covering injection,
  unsafe parsing, provenance, and output handling. Use when assessing the security
  of a vision/audio/document-accepting feature.
---

# Goal

A structured review of how a multimodal app ingests and trusts non-text input,
identifying where untrusted media can influence behavior and where parsing/handling
is unsafe.

# Review dimensions

1. **Input channels** — enumerate every accepted modality and its processing path
   (OCR, vision model, captioning, transcription, file parser, embedding).
2. **Trust treatment** — is content extracted from media treated as untrusted
   **data**, or can it act as instructions? (The central multimodal risk.)
3. **Parser safety** — format/size validation, sandboxing, decompression/entity
   limits, auto-fetch of embedded URLs (SSRF), timeouts.
4. **Provenance & moderation** — is media source tracked; does safety/moderation
   run on extracted content and on the raw media?
5. **Output handling** — where do generations and any extracted data flow
   downstream (see `llm-security` LLM05).
6. **Privacy** — sensitive content in images/docs (PII, faces, IDs); retention.

# Steps

1. Map channels and processing (ask for the design if not provided).
2. Walk each dimension; substantiate injection/parsing claims with
   `multimodal-injection-test` rather than asserting.
3. Identify where any modality bypasses the text input controls.
4. Rank (`threat-modeling:risk-rank`) and map mitigations.

# Output

A dimension-by-dimension findings table + ranked top risks. Confirmed issues →
`security-reporting:finding`.

# Notes

Non-text channels are the commonly-forgotten input surface — they often skip the
sanitization and instruction/data separation that text inputs get. Verify the same
controls apply to every modality.
