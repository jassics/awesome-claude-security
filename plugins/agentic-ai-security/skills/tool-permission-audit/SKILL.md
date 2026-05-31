---
name: tool-permission-audit
description: >-
  Inventory the tools/functions an AI agent can call and audit their privileges,
  side effects, and approval requirements to find excessive-agency and
  least-privilege gaps. Use when reviewing an agent's tool/function surface.
---

# Goal

A complete tool inventory with a privilege/risk rating per tool and a clear list
of least-privilege and approval-gating gaps.

# Steps

1. **Enumerate tools.** List every tool/function/plugin/MCP server the agent can
   invoke, including dynamically discovered ones. Don't rely on the docs — check
   what's actually wired into the agent's toolset.
2. **Classify each tool:**
   - Effect: read-only / write / destructive / external-side-effect (email, pay,
     deploy, post).
   - Reversibility: reversible / irreversible.
   - Credentials: what identity/token it uses; what that token can do beyond this tool.
   - Reachability: always available, or gated by state/role?
3. **Rate risk** per tool (effect × reversibility × credential scope).
4. **Find gaps:**
   - Over-broad credentials (one token, many powers).
   - Destructive/irreversible/external actions with no human confirmation.
   - Tools present but unnecessary for the agent's function.
   - Missing rate/spend/iteration limits on expensive tools.

# Output

A tool inventory table: tool · effect · reversible? · credential scope · approval
required? · risk · gap/recommendation. Plus a prioritized least-privilege
remediation list. Feed high-risk gaps to `security-reporting:finding`.

# Notes

Excessive agency usually hides in credential scope, not tool count: a single
over-privileged token behind a "safe-looking" tool is the common root cause.
Recommend per-tool scoped credentials and confirmation gates on anything
irreversible or externally visible.
