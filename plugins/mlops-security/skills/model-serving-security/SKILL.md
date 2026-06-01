---
name: model-serving-security
description: >-
  Harden a deployed model inference endpoint — authn/authz, rate limiting and abuse
  control, input validation, and exposure to model-extraction / inversion /
  membership-inference attacks. Use when reviewing how a model is served (REST/gRPC,
  Triton/TorchServe/KServe, or a hosted inference API), not how it was trained.
---

# Goal

An inference endpoint that's authenticated, abuse-resistant, and not leaking the
model or its training data through its outputs — covering the serving layer beneath
LLM/app-level concerns.

# What to review

- **AuthN/Z & exposure** — is the endpoint authenticated and authorized per caller?
  Not publicly reachable without controls? Tenant isolation for multi-tenant serving?
- **Rate limiting & abuse / cost** — per-caller quotas to blunt **model extraction**
  (stealing the model by querying it) and to cap inference cost/DoS.
- **Model extraction** — high-volume systematic querying to clone the model; mitigate
  with rate limits, anomaly detection, output granularity limits, and monitoring.
- **Model inversion / membership inference** — outputs (esp. confidence scores/logits)
  that leak training data or reveal whether a record was in the training set; limit
  exposed confidence detail.
- **Input validation & resource safety** — malformed/adversarial/oversized inputs;
  tensor/shape validation; timeouts and resource caps to prevent inference DoS.
- **Serving infra** — the model server itself (Triton/TorchServe/KServe) patched and
  hardened; management/metrics endpoints not exposed; no unsafe model auto-loading.

# Steps

1. Identify the serving stack, exposure, and who can call it.
2. Check authn/z, rate limiting/quotas, and input validation at the endpoint.
3. Assess extraction/inversion/membership-inference exposure — especially what
   confidence/score detail is returned.
4. Review the model server's own hardening and management-surface exposure.
5. Recommend controls prioritized by exposure (unauthenticated/public first).

# Output

A findings list (surface · risk · evidence · fix) plus controls: authn/z, rate
limits/quotas, input validation, output-granularity limits, and monitoring. For
LLM-specific output risks (prompt injection, jailbreaks) defer to `llm-security`; for
the app around it, the appsec plugins.

# Notes

The model is intellectual property and the training data is a confidentiality
boundary — both can leak through a perfectly "working" endpoint via extraction and
inversion. Returning raw confidence scores/logits is the quiet enabler of inversion
and membership inference; expose the minimum the use case needs. Rate limiting is the
single highest-leverage control here.
