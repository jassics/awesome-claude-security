# genai-suite

A **domain suite**: a thin, manifest-only bundle that installs the GenAI /
AI-security plugins in one shot via `dependencies`. Install this if you want "all
of AI security" rather than picking plugins individually.

It owns no skills of its own — it just composes standalone plugins, every one of
which you can also install on its own.

## Install

```
/plugin install genai-suite@awesome-claude-security
```

## Members

| Plugin | Status |
| --- | --- |
| `llm-security` | ✅ included |
| `rag-security` | ✅ included |
| `agentic-ai-security` | ✅ included |
| `multimodal-security` | ✅ included |
| `mlops-security` | ⬜ added on release |

As each member plugin ships, it's added to this suite's `dependencies`; existing
suite users receive it automatically on `/plugin update`.

## Note on scope

Domain suites bundle **domain** plugins only. The shared **core** plugins
(`security-diagramming`, `security-reporting`) stay standalone — install them
directly, or get them via a role bundle like `pentester`. See
[docs/BUNDLES.md](../../docs/BUNDLES.md).
