# appsec-suite

A **domain suite** for application security: one-shot install of the appsec stack.
Manifest-only bundle — it owns no skills, just composes standalone plugins you can
also install individually.

## Install

```
/plugin install appsec-suite@awesome-claude-security
```

## Members

| Plugin | Covers |
| --- | --- |
| `web-app-security` | OWASP Web Top 10, access control, injection. |
| `api-security` | OWASP API Top 10, BOLA/BFLA authorization. |
| `mobile-security` | OWASP MASVS/MASTG (Android/iOS). |
| `sast-sca` | Static analysis + dependency/SBOM scanning. |

## Note on scope

Domain suites bundle **domain** plugins only. The shared **core** plugins
(`security-diagramming`, `security-reporting`) stay standalone — install them
directly, or get them via a role bundle like `pentester`. See
[docs/BUNDLES.md](../../docs/BUNDLES.md).
