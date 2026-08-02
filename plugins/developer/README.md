# developer

A **role bundle** for developers and engineers — including AI-assisted/agentic
("vibe coding") workflows — who want secure-by-default coding folded into their
normal flow without needing to know which of this marketplace's ~40 security
plugins to reach for. Ships a `developer` agent that coordinates security across
the feature lifecycle, a `pre-commit-gate` skill, and **declares dependencies**
so installing it pulls in the building blocks it always uses.

Role plugins are intentionally thin — they orchestrate. The capabilities live in
the standalone plugins this one depends on, so you can also install any of those
on their own.

## Install

```
/plugin install developer@awesome-claude-security
```

This **auto-installs** its full stack: `security-knowledge`, `sast-sca`,
`security-architect`, `infrastructure-security`, and `secure-coding`. (`claude
plugin prune` cleans them up later if you remove this bundle.)

`secure-coding` is the one dependency that's *enforced*, not just advisory — it
installs a Claude Code hook plus real git hooks that block a commit/push
containing a secret or a banned Python/React function, from any tool, not only
inside a Claude Code session. Run its `install-git-hooks.sh` once per repo for
that guarantee; `pre-commit-gate` below is the fast, diff-scoped check for
everything `secure-coding` doesn't cover (broader SAST/SCA/IaC, other
languages).

## Command

| Command | What it runs |
| --- | --- |
| `/developer:precommit` | Run the pre-commit security gate on the current changeset and report a pass/fail verdict. |

## Skills

| Skill | When it fires |
| --- | --- |
| `/developer:pre-commit-gate` | Diff-scoped secrets/SAST/SCA/IaC/Claude-config check before commit or push, aggregated into one BLOCK/PASS verdict. |

## Agents

| Agent | Use for |
| --- | --- |
| `developer` | Coordinate security across a feature's lifecycle — PRD/prompt requirements, secure-coding guidance while writing code, and the pre-commit gate before shipping. |

## Scope

This bundle is aimed at **developers and engineers**, not security specialists —
it's the low-friction entry point. For a formal design review, penetration test,
or GRC assessment, use the standalone plugins directly: `security-architect`,
`pentester`, `grc`, or any domain plugin (`web-app-security`, `k8s-security`, …).
