---
name: ml-pipeline-security-review
description: >-
  Review the training / MLOps pipeline for security weaknesses — data-poisoning
  surface, feature-store and data-source trust, experiment-tracking and model-registry
  access control, secrets, and reproducibility/provenance. Use when assessing how
  models are built and promoted, not how they're served or consumed.
---

# Goal

A training-to-registry pipeline where data is trusted, access is controlled, secrets
are protected, and every model is traceable to the data and code that produced it.

# What to review

- **Data-poisoning surface** — where does training/fine-tuning data come from? Can an
  attacker influence it (user-contributed data, scraped sources, feedback loops,
  public datasets)? Are there validation, anomaly detection, and provenance on the
  data?
- **Feature store / data pipeline trust** — integrity and access control on feature
  stores and data lakes; can features be tampered between source and training?
- **Experiment tracking & model registry** — auth/authz on MLflow/W&B/registry; who
  can register, promote, or overwrite a model? Audit logging on promotion.
- **Secrets & infra** — credentials for data stores, registries, and compute kept out
  of notebooks/code; least-privilege service accounts; notebook/Jupyter exposure.
- **Reproducibility & provenance** — pinned code + data + params; lineage linking a
  registered model to its run, data version, and commit (feeds
  `ml-supply-chain-review`).
- **Compute/job integrity** — training jobs run on trusted, isolated infrastructure;
  no arbitrary-code paths from untrusted notebooks into privileged compute.

# Steps

1. Map the pipeline: data sources → ingestion/feature store → training/fine-tuning →
   evaluation → registry → promotion. Mark trust boundaries.
2. Assess each stage against the risks above; prioritize poisoning paths and
   registry/promotion access (those alter what ships).
3. Check secrets handling, service-account scope, and audit logging on promotion.
4. Recommend controls: data validation/provenance, registry RBAC + promotion gates,
   secret management, and lineage/reproducibility.

# Output

A findings list (stage · risk · evidence · fix) plus pipeline-level controls (data
provenance, registry RBAC, promotion gates, secrets). Defer artifact provenance/signing
detail to `ml-supply-chain-review`; pipeline/CI hardening to `supply-chain-security`.

# Notes

Data poisoning is the ML-native attack with no clean software analog — small,
targeted training-data manipulation can implant a backdoor that passes normal eval.
Provenance is the through-line: if you can't trace a deployed model to its data and
run, you can't reason about its trustworthiness. The model registry is a deployment
gate — treat promotion rights like production deploy rights.
