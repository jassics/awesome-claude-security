# multimodal-security

Security for **multimodal AI** systems that accept images, audio, video, or
documents. Covers **cross-modal prompt injection** (instructions hidden in images,
OCR'd text, file metadata, audio), **unsafe file parsing**, **adversarial inputs**,
and weak **content provenance**.

A **genai** domain plugin; member of [`genai-suite`](../genai-suite/). It extends
`llm-security` and `rag-security` to non-text input channels — often the
least-guarded path into a model.

## Install

```
/plugin install multimodal-security@awesome-claude-security
# or the whole GenAI stack:
/plugin install genai-suite@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/multimodal-security:multimodal-injection-test` | Test image/audio/document channels for embedded instructions or adversarial content. |
| `/multimodal-security:multimodal-security-review` | Review a multimodal app's input handling and trust boundaries across modalities. |

## Security vs. safety

This plugin covers multimodal **security** (attacker-driven: injection, unsafe
parsing, adversarial inputs). Harmful **content** concerns — generating or failing
to block harmful imagery, non-consensual/deepfake media, CSAM, etc. — are **AI
safety**; see [`ai-safety`](../ai-safety/) (`guardrail-review`, `safety-evaluation`).

## Pairs well with

`llm-security` (prompt injection, output handling), `rag-security` (document
ingestion), `security-reporting`, and [`ai-safety`](../ai-safety/).
