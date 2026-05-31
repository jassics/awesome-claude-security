# Contributing

Thanks for helping build a security toolkit for the Claude Code community. This repo is a **plugin marketplace** — see [docs/AUTHORING.md](docs/AUTHORING.md) for the mechanics and [docs/TAXONOMY.md](docs/TAXONOMY.md) for where things belong.

## Ways to contribute

- **New plugin** for a domain/role on the [roadmap](docs/ROADMAP.md) (or propose a new one).
- **New skill or agent** inside an existing plugin.
- **Reference packs** (frameworks, checklists, payload catalogs) under a skill's `reference.md`.
- **Integrations** (Jira/Confluence/Drive and beyond).
- **Fixes & docs.**

## Workflow

1. Open an issue naming the plugin/skill so work isn't duplicated.
2. Scaffold from [`templates/`](templates/).
3. Build following [docs/AUTHORING.md](docs/AUTHORING.md).
4. `claude plugin validate ./plugins/<name> --strict`.
5. Add/extend the entry in `.claude-plugin/marketplace.json`.
6. Update [docs/ROADMAP.md](docs/ROADMAP.md) (flip ⬜ → ✅).
7. Open a PR. Keep one plugin (or one coherent skill set) per PR.

## Quality bar

- Skills do **one** thing and say clearly **when** to fire (the `description` field).
- Be procedural and framework-anchored (OWASP, MITRE ATT&CK, NIST, STRIDE, MASTG, CIS).
- Compose with `security-diagramming` and `security-reporting` instead of re-inventing visuals/reports.
- No secrets, no real customer data, no live targets in examples.

## Scope & ethics

This project supports **authorized** security testing, defensive security, detection engineering, GRC, research, education, and CTF work. By contributing you agree that:

- Skills assume the operator has **permission** to test the systems involved, and should say so where relevant.
- Content is framed around **assessment, detection, hardening, and remediation** — not turnkey weaponization, mass exploitation, or evasion tooling whose primary purpose is to harm.
- Dual-use techniques are documented with defensive intent and the authorization context made explicit.

Contributions that are primarily for unauthorized intrusion, destruction, or large-scale abuse will be declined.

## Licensing

By contributing you agree your contributions are licensed under [GPL-3.0](LICENSE). Don't submit content you don't have the rights to, and keep third-party material GPL-compatible with attribution.
