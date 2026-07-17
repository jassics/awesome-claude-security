---
name: secret-guard
description: Detect hardcoded secrets, cloud keys (AWS/GCP/Azure), tokens, .env files, and sensitive config before they're committed or pushed, and verify .gitignore covers the patterns that must never be tracked. Use when the user is about to commit/push, asks "did I leak a secret", "check for hardcoded keys", "is my .gitignore missing anything", or when reviewing any diff that touches config/env files. This is the manual/interactive counterpart to the enforced git hooks this plugin installs — see README "Enforcement" section.
---

# Goal

Catch secrets and sensitive files before they reach git history — hardcoded or in
`.env`/config files — and make sure `.gitignore` actually excludes the categories of
file that should never be tracked. Enforcement (blocking) happens via the installed
git hooks (`scripts/install-git-hooks.sh`) and the Claude Code `PreToolUse` hook in
`hooks/hooks.json`; this skill is for the interactive/manual pass, e.g. reviewing a
diff before the user commits, or auditing an existing repo.

# Steps

1. Scope: staged changes (`git diff --cached`) by default, or the path the user names,
   or a full-repo audit (including history) if the user asks for that explicitly.
2. Secret detection, in order of preference:
   - `gitleaks detect --source <path> -v` (or `gitleaks protect --staged -v` for staged-only) if installed.
   - `detect-secrets scan <path>` if installed and gitleaks isn't.
   - Fall back to the pattern list in `reference.md` (cloud key formats, generic
     `key=`/`token=`/`secret=` assignments, PEM private key headers) — never skip
     the check for lack of a tool.
3. File-pattern check: flag any staged/tracked file matching the sensitive-file list
   in `reference.md` (`.env*`, `*.pem`, `*.key`, `id_rsa*`, `credentials.json`,
   `.aws/credentials`, `*.pfx`, `secrets.yml`, etc.) regardless of content — these
   files should not be tracked at all, secret-looking content or not.
4. `.gitignore` check: read the repo's `.gitignore` (root and any per-package ones)
   and diff it against the required-patterns list in `rules/gitignore-required.txt`
   (relative to `$CLAUDE_PLUGIN_ROOT`). Report any missing pattern.
5. If a real secret or a sensitive file is already committed (not just staged), say
   so explicitly and note it needs history rewrite + rotation, not just a new commit
   (removing it in a new commit does not remove it from git history).

# Output

```
SECRETS FOUND: <count>
[<severity>] <file>:<line> — <what matched> (<detector: gitleaks|detect-secrets|pattern>)
  → Remediation: remove from source, load from env/secret manager, ROTATE the credential.

SENSITIVE FILES TRACKED: <count>
<file> — matches sensitive-file pattern, must not be tracked.
  → Remediation: `git rm --cached <file>`, add pattern to .gitignore.

.GITIGNORE GAPS: <count>
Missing: <pattern> (<why it matters>)
```

If nothing found, say so plainly — don't pad a clean result with caveats.
