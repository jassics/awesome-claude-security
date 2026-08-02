---
name: secure-coding-kb
description: >-
  Look up the safe idiom and known-risky API/library for a language or framework
  (Python, JS/TS/Node, Java, Go, C/C++, Ruby) before or while writing code — a
  design/build-time cheat-sheet, distinct from post-hoc scanning. Use when writing
  or reviewing code, scoping a PRD's tech stack, or advising an AI-assisted/vibe-coded
  change on which APIs and libraries to avoid up front.
---

# Goal

The safe pattern and the risky API/library to avoid for the language(s)/framework(s)
in scope — consulted *while designing or writing code*, so unsafe patterns are never
introduced rather than caught later by a scanner.

# Steps

1. **Identify the language(s)/framework(s) in scope** for the code, PRD, or feature
   being built.
2. **Pull the relevant guidance from `reference.md`** for each: unsafe API/pattern →
   safe replacement, and risky/abandoned libraries → maintained alternative.
3. **Flag framework-specific footguns** (e.g. Django/Flask, Express/Node,
   Spring/Java, Rails, Go stdlib) — defaults that are insecure unless explicitly
   hardened.
4. **Cite OWASP Cheat Sheet Series** for depth beyond this quick-reference — it's
   the canonical, continuously-updated source; this skill is a fast lookup, not a
   replacement.

# Output

A short table: pattern/library flagged · why risky · safe replacement · source
(OWASP Cheat Sheet name). For an existing codebase, hand off found instances to
`sast-sca:sast-review` for the code-level fix; for new work, this *is* the fix —
inject the safe pattern before code is written.

# Notes

This complements, not replaces, `sast-sca:sast-review`: that skill scans code that
already exists and reports what's wrong; this skill guides what to write in the
first place — most valuable during design, PRD scoping, or AI-assisted/"vibe coded"
implementation where no security requirement was stated up front (see
`security-architect:prd-security-injection` for injecting requirements into the
PRD/prompt itself). See `reference.md` for the per-language tables.
