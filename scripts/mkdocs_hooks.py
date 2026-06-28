"""MkDocs build hooks.

The repo's `docs/*.md` are written to render correctly **on GitHub**, where they
sit in `docs/` and link up to repo-root files with `../` — e.g. `../CONTRIBUTING.md`
and `../templates/`. Those targets live outside the MkDocs `docs_dir`, so on the
built site the relative links would 404.

Rather than rewrite the source (which would break GitHub rendering), we rewrite
just those `../`-escaping links to absolute GitHub URLs at build time. The source
files stay pristine; both surfaces get working links.
"""

from __future__ import annotations

import re

GITHUB_BLOB = "https://github.com/jassics/awesome-claude-security/blob/main/"
GITHUB_TREE = "https://github.com/jassics/awesome-claude-security/tree/main/"

# Matches markdown links whose target starts with one or more `../` segments.
_LINK = re.compile(r"(\]\()(\.\./[^)\s]+)(\))")


def _rewrite(match: re.Match) -> str:
    target = match.group(2)
    # Normalize away the leading ../ that escape docs/ — what remains is the
    # repo-root-relative path (e.g. CONTRIBUTING.md, templates/plugin-template/).
    cleaned = re.sub(r"^(\.\./)+", "", target)
    base = GITHUB_TREE if cleaned.endswith("/") else GITHUB_BLOB
    # Preserve any #anchor on the path.
    return f"{match.group(1)}{base}{cleaned}{match.group(3)}"


def on_page_markdown(markdown: str, *, page=None, config=None, files=None, **kwargs) -> str:
    return _LINK.sub(_rewrite, markdown)
