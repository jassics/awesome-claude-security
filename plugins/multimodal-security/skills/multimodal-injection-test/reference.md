# Reference: multimodal injection techniques

Per-modality technique catalog and mitigations for `multimodal-injection-test`.
Keep all testing authorized and payloads non-destructive.

## Image

| Technique | What to try | Mitigation |
| --- | --- | --- |
| Visible text injection | Render instruction text into the image. | Treat OCR/vision-extracted text as data, not instructions; instruction/data separation. |
| Low-contrast / hidden text | Faint or same-color-as-background text the model still reads. | Same as above; flag images with embedded text. |
| Typographic / steganographic | Text in unusual fonts, watermarks, or steganographic channels. | Don't act on extracted instructions; provenance labels. |
| Adversarial perturbation | Perturbations causing misclassification or moderation bypass. | Robust models, ensemble checks, human review for high-stakes calls. |

## Document (PDF / Office / scans)

| Technique | What to try | Mitigation |
| --- | --- | --- |
| Embedded instructions | Instruction text in the doc body that gets OCR'd/extracted. | Treat extracted text as untrusted (see `rag-security`). |
| Hidden layers / white text | Invisible text extracted by parsers but unseen by humans. | Strip/normalize; flag hidden text. |
| Malicious structure | Decompression bombs, deeply nested objects, external entity refs. | Hardened parsers, size/most limits, disable external entity resolution. |
| Embedded URLs/SSRF | Links the system auto-fetches. | No auto-fetch of untrusted URLs; egress controls. |

## Audio / video

| Technique | What to try | Mitigation |
| --- | --- | --- |
| Spoken instruction injection | Commands spoken in the audio that the model obeys after transcription. | Treat transcripts as untrusted data; don't route to actions. |
| Inaudible / encoded | Near-ultrasonic or encoded commands. | Bandlimit/normalize input; act only on validated intents. |
| Frame injection (video) | Instruction frames or overlaid text in video. | Sample-and-OCR treated as data; provenance. |

## Metadata & adjacent fields

- EXIF, filenames, alt-text, captions, subtitles — instructions placed here that
  enter the prompt. **Mitigation:** never concatenate metadata into the instruction
  context; sanitize and treat as data.

## Parser / pipeline safety

- Oversized/malformed media → DoS; media URLs → SSRF; format confusion.
- **Mitigations:** strict format/size validation, sandboxed/hardened decoders,
  timeouts, no auto-fetch of embedded URLs, egress filtering.

## Cross-cutting principle

Every modality ultimately becomes text/features fed to the model. The universal
control: **extracted content from any modality is untrusted data, not
instructions, and must not be able to authorize actions.**
