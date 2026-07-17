---
name: safe-function-lint
description: Scan Python or React/JS code for outdated, banned, or vulnerable functions/methods (eval, pickle.loads, subprocess shell=True, dangerouslySetInnerHTML, md5 for passwords, etc.) and propose the exact safe alternative for each hit. Use when reviewing a diff/PR, before a commit, or when the user asks "is this function safe", "any vulnerable functions here", or wants a secure-coding pass on Python or React code.
---

# Goal

For a given diff, file, or directory, find every use of a banned/outdated/vulnerable
function or API in Python or React/JS, and for each hit report: the exact standard it
violates, why it's risky, and the concrete safe replacement — never just "this is bad."

# Steps

1. Determine scope: staged diff (`git diff --cached`) by default if inside a git repo
   and no path is given; otherwise the path/files the user named.
2. Identify language(s) present (`.py` → Python rules; `.js/.jsx/.ts/.tsx` → React/JS rules).
3. Load `reference.md` in this skill directory — it is the rule pack (CWE/OWASP ASVS
   cited, matcher pattern, safe alternative) — and check the scoped code against it.
4. If Semgrep is installed, prefer running it for precision:
   ```
   semgrep --config "$CLAUDE_PLUGIN_ROOT/rules/semgrep-python.yml" <path>   # Python
   semgrep --config "$CLAUDE_PLUGIN_ROOT/rules/semgrep-react.yml" <path>   # React/JS
   ```
   If Semgrep isn't installed, fall back to manually pattern-matching against `reference.md`
   directly — do not skip the check, degrade to manual review instead.
5. De-duplicate and rank findings by severity (Critical/High/Medium/Low, per `reference.md`).

# Output

For each finding, report in this exact shape:

```
[<severity>] <file>:<line> — <banned function/pattern>
Standard: <CWE-ID / OWASP ASVS section>
Risk: <one sentence — what breaks and how it's exploited>
Fix: <exact safe replacement, as a code snippet if it's not a 1:1 rename>
```

Close with a one-line summary count by severity. Do not restate the whole file — only
the offending lines and their fixes.
