# secure-coding

Secure-coding enforcement for Python and React/JS: flags outdated or vulnerable
functions with the exact safe alternative, and blocks commits/pushes that carry
secrets — hardcoded API keys, cloud credentials, `.env`/config files — even ones
that were never in `.gitignore`.

## What's in it

| Component | What it does |
|---|---|
| `agents/secure-coding-guardian.md` | Dedicated review agent — narrowly scoped to the two skills below, not a general code reviewer. |
| `skills/safe-function-lint` | Curated Python + React/JS rule pack (CWE / OWASP ASVS 5.0 cited) mapping banned/outdated functions to safe replacements. Backed by `rules/semgrep-python.yml` / `rules/semgrep-react.yml` when Semgrep is installed. |
| `skills/secret-guard` | Interactive secret/sensitive-file/`.gitignore` audit — the manual counterpart to the enforcement below. |
| `hooks/hooks.json` | Claude Code `PreToolUse` hook — blocks `git commit`/`git push` **inside a Claude Code session** if the change contains a secret or a file that must never be tracked. |
| `scripts/install-git-hooks.sh` | Installs **real git hooks** (via `pre-commit`, or a native fallback) into a target repo — enforces the same thing from any terminal/IDE/CI, with or without Claude Code. |

## Enforcement — two layers, on purpose

1. **Claude Code hook** (`hooks/hooks.json`) only fires when Claude itself runs the
   `git commit`/`git push` command in a session. It's fast, needs no setup, but a
   developer pushing from a plain terminal or another IDE bypasses it.
2. **Real git hooks** (`scripts/install-git-hooks.sh`) fire for *any* commit/push,
   regardless of tool — this is the actual "can't push if secrets are found"
   guarantee. Run it once per repo:
   ```
   ./scripts/install-git-hooks.sh /path/to/your/repo
   ```
   It prefers the [`pre-commit`](https://pre-commit.com) framework (gitleaks +
   detect-secrets + the Semgrep rule packs + a `.gitignore` coverage check) and
   falls back to a native `.git/hooks/pre-push` script if `pre-commit` isn't
   installed.

Install both. Neither alone gives full coverage.

## Install

```
/plugin install secure-coding@awesome-claude-security
```

Then, per repo you want hard enforcement in:
```
./scripts/install-git-hooks.sh /path/to/repo
```

Recommended external tools (the hooks/skills degrade gracefully — falling back to
regex patterns — but are meaningfully weaker without these):
- [gitleaks](https://github.com/gitleaks/gitleaks) — secret scanning
- [semgrep](https://semgrep.dev) — runs the bundled rule packs
- [detect-secrets](https://github.com/Yelp/detect-secrets) — secret scanning (belt & suspenders with gitleaks)
- [bandit](https://github.com/PyCQA/bandit) — Python-specific SAST
- [pre-commit](https://pre-commit.com) — the hook runner `install-git-hooks.sh` targets

## Usage examples

- "Review this diff for secure-coding issues before I push" → `secure-coding-guardian` agent, or `/safe-function-lint`.
- "Did I hardcode a secret anywhere?" → `/secret-guard`.
- "Is my .gitignore missing anything?" → `/secret-guard`.

## Pairs well with

This plugin is deliberately narrow (Python + React/JS, ~12 rules/language) and
its edge is *enforcement* (real git hooks + a Claude Code hook), not breadth.
For the marketplace's broader coverage, install alongside:

- [`sast-sca`](../sast-sca/) — multi-language SAST/SCA, dependency/SBOM scanning.
- [`infrastructure-security`](../infrastructure-security/) — secrets/gitignore
  review across IaC, CI/CD, and containers, not just source.
- [`security-knowledge`](../security-knowledge/) — `secure-coding-kb` gives the
  same safe-idiom guidance as reference material for other languages.
- [`developer`](../developer/) — the role bundle that installs this plugin
  alongside the above as one coherent secure-coding-companion stack.

## Design notes / roadmap

- Rule packs are deliberately small and curated (~12 rules/language) rather than
  exhaustive — grown from real findings, to avoid alert fatigue. See each skill's
  `reference.md`.
- Not a linter replacement (Ruff/ESLint stay as-is) — this is an opinionated
  security layer on top, matching the "curated opinion layer, not a new linter"
  approach from the originating secure-coding-tooling ideation.
- Roadmap: expand rule packs from real PR findings; add a `secrets.baseline`
  bootstrap step to `install-git-hooks.sh`; consider a Node/JS-specific SCA check
  (`npm audit` / OSV-Scanner) alongside the existing Python-focused SCA overlap
  with the `sast-sca` plugin in the `awesome-claude-security` marketplace.

## License

GPL-3.0
