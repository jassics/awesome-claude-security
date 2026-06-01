---
name: ml-supply-chain-review
description: >-
  Review the provenance and integrity of models, datasets, and ML artifacts pulled
  from hubs/registries — unsafe deserialization (pickle, PyTorch/Keras/joblib),
  untrusted model sources, model/dataset tampering, and signing. Use when an app
  loads third-party model weights or datasets, or before promoting a model.
---

# Goal

Assurance that every model and dataset entering the system is from a trusted source,
hasn't been tampered with, and can't execute code or carry a backdoor when loaded.
This is the **supply-chain** layer for ML artifacts (parallel to
`supply-chain-security` for software).

# What to look for

- **Unsafe deserialization / code execution on load** — `pickle`, PyTorch `.pt/.bin`
  (pickle under the hood), `joblib`, Keras `.h5`/Lambda layers, and custom loaders run
  arbitrary code. Prefer **safetensors** or other non-executable formats; scan model
  files (e.g., picklescan-style checks) before loading.
- **Untrusted sources** — models/datasets from public hubs without verified
  publisher; no pinning to a specific revision/commit hash; "latest" tag.
- **Tampering / backdoors** — no integrity hash or signature on weights; no
  provenance linking weights → training run → data. Watch for trojaned/backdoored
  models (poisoned to misbehave on a trigger).
- **Dataset integrity** — training/eval data from unverified sources; no checksum;
  poisoning surface (see `ml-pipeline-security-review`).
- **Dependency risk** — ML stack pulls large transitive trees; defer software-package
  trust to `supply-chain-security`.

# Steps

1. Inventory every external model/dataset artifact and its source, format, and
   load path.
2. Flag executable serialization formats and untrusted/unpinned sources; recommend
   safe formats, pinning to immutable revisions, and pre-load scanning.
3. Establish integrity: checksums/signatures on artifacts, provenance to the training
   run, and a vetting gate before a model is registered/promoted.
4. Recommend a trusted internal model registry with scanning + signing over direct
   hub pulls in production.

# Output

A findings list (artifact · source · format · risk · fix) plus recommended controls:
safe-format policy, pre-load scanning, pinning, signing, and a promotion gate. Pair
with `supply-chain-security` (software deps), `llm-security` (model behavior).

# Notes

Loading a pickle-based model from an untrusted source is **remote code execution**,
full stop — it's the most common and most underrated ML supply-chain risk. safetensors
exists precisely to remove this; prefer it. A signed, hashed model from an unknown
training run still isn't trustworthy — provenance must reach back to the data and run.
