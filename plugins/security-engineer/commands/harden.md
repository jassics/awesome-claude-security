---
description: Run a build-and-harden pass across code, pipeline, cloud, and infra, then track remediation.
argument-hint: [repo / service / pipeline to harden]
---

Harden: **$ARGUMENTS**

Walk the hardening pass, using installed skills (note any whose plugin is missing):

1. **Secure the pipeline** — `/security-engineer:secure-pipeline` to assess and harden CI/CD as the control point.
2. **Code & deps** — `/sast-sca:sast-review` and `/sast-sca:sca-review`; for supply-chain trust add `/supply-chain-security:dependency-supply-chain-review` and `/supply-chain-security:pipeline-integrity-review`.
3. **Cloud & infra** — `/cloud-security:cloud-posture-review`, `/k8s-security:k8s-cluster-review`, `/infrastructure-security:iac-security-review` and `/infrastructure-security:secrets-management-review` as applicable.
4. **Prioritize & track** — `/vulnerability-management:vulnerability-prioritization` then `/vulnerability-management:remediation-tracking` to assign owners/SLAs.
5. **Report** — `/security-reporting:finding` per issue; optionally `/security-integrations:publish-finding-to-jira` to turn them into tracked work.

For deep execution, hand off to the `security-engineer` agent. Prefer durable fixes (golden images, IaC modules, pipeline gates) over one-off patches so issues don't recur.
