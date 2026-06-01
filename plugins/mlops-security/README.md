# mlops-security

Security for the **ML lifecycle and infrastructure** — the layer beneath the
prompt. Vet the **ML supply chain** (model/dataset provenance, unsafe
deserialization), harden the **training/MLOps pipeline** (data poisoning, registry
access, secrets, lineage), and secure **model serving** (authn/z, rate limiting,
extraction/inversion exposure).

A **genai** plugin; member of [`genai-suite`](../genai-suite/). It sits under
`llm-security` / `rag-security` / `agentic-ai-security` (which cover model *behavior*
and app-level risk) and handles how models are built, shipped, and served.

## Install

```
/plugin install mlops-security@awesome-claude-security
# or the whole GenAI stack:
/plugin install genai-suite@awesome-claude-security
```

## Skills

| Skill | When it fires |
| --- | --- |
| `/mlops-security:ml-supply-chain-review` | Provenance/integrity of models & datasets; unsafe deserialization (pickle), untrusted sources, signing. |
| `/mlops-security:ml-pipeline-security-review` | Training/MLOps pipeline: data poisoning, feature-store/registry access, secrets, lineage. |
| `/mlops-security:model-serving-security` | Inference endpoint hardening: authn/z, rate limits, model extraction/inversion/membership inference. |

## Pairs well with

`llm-security` (model behavior), `supply-chain-security` (software-package trust),
`cloud-security` / `k8s-security` (serving infra), `security-reporting`.
