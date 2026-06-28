#!/usr/bin/env python3
"""Build-time page generation for the MkDocs site (mkdocs-gen-files).

Single source of truth: `.claude-plugin/marketplace.json`. The catalog page is
GENERATED from it at every build, so the site's plugin list can never drift from
what users actually install. The repo's structural CI (scripts/validate-marketplace.py)
already guarantees marketplace.json <-> plugins/ parity, so this closes the chain:

    plugins/ dirs  <->  marketplace.json  ->  the site catalog

Run automatically by the `gen-files` plugin during `mkdocs build` / `mkdocs serve`.
The `build_catalog_markdown()` function is pure (no mkdocs import) so it can be
unit-tested or rendered standalone.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
BANNER = ROOT / "assets" / "banner.png"
GITHUB = "https://github.com/jassics/awesome-claude-security"
MARKETPLACE_REF = "awesome-claude-security"

# Display order + human titles + one-line intent for each bucket.
CATEGORIES: list[tuple[str, str, str]] = [
    ("core", "Core",
     "Cross-cutting capabilities every security task reuses — diagrams, reports, "
     "framework lookups, publishing."),
    ("domain", "Domain",
     "One deep skillset per discipline — appsec, cloud, network, detection, DFIR, "
     "threat intel, and more."),
    ("genai", "GenAI security",
     "Protecting AI/LLM systems *from attackers* — prompt injection, RAG poisoning, "
     "agent autonomy, ML supply chain."),
    ("ai-safety", "AI safety",
     "A distinct discipline — stopping AI systems *from causing harm*: harm modeling, "
     "safety evals, bias/fairness, guardrails."),
    ("role", "Roles",
     "Persona bundles that combine domains with a workflow and **auto-install their "
     "whole stack**."),
    ("executive", "Executive",
     "The strategic tier — security strategy, cyber-risk quantification, board-ready "
     "narratives."),
    ("suite", "Suites",
     "One-shot domain bundles — install a whole area at once; its parts come along "
     "automatically."),
]


def load_catalog() -> list[dict]:
    data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    return data.get("plugins", [])


def build_catalog_markdown(plugins: list[dict]) -> str:
    """Render the full catalog page as Markdown, grouped by bucket. Pure function."""
    by_cat: dict[str, list[dict]] = {}
    for p in plugins:
        by_cat.setdefault(p.get("category", "other"), []).append(p)

    total = len(plugins)
    out: list[str] = []
    out.append("---")
    out.append("hide:\n  - toc")
    out.append("---\n")
    out.append("# Plugin catalog\n")
    out.append(
        f"All **{total} plugins**, grouped by bucket. This page is generated from "
        f"[`marketplace.json`]({GITHUB}/blob/main/.claude-plugin/marketplace.json) at "
        "build time — it always matches what you can actually install. Use the search "
        "(press <kbd>/</kbd>) to find a plugin by keyword.\n"
    )
    out.append(
        "Install any of them with:\n\n"
        "```\n"
        f"/plugin install <name>@{MARKETPLACE_REF}\n"
        "```\n"
    )

    # Per-bucket count summary line.
    counts = " · ".join(
        f"**{title}** {len(by_cat.get(key, []))}"
        for key, title, _ in CATEGORIES
        if by_cat.get(key)
    )
    out.append(f"{counts}\n")

    for key, title, blurb in CATEGORIES:
        items = sorted(by_cat.get(key, []), key=lambda p: p["name"])
        if not items:
            continue
        out.append(f"## {title}\n")
        out.append(f"{blurb}\n")
        out.append("| Plugin | What it does | Install |")
        out.append("| --- | --- | --- |")
        for p in items:
            name = p["name"]
            desc = p.get("description", "").replace("|", "\\|")
            kws = p.get("keywords", [])
            kw_line = ""
            if kws:
                kw_line = "<br>" + " ".join(f"`{k}`" for k in kws[:6])
            link = f"[`{name}`]({GITHUB}/tree/main/plugins/{name})"
            install = f"`/plugin install {name}@{MARKETPLACE_REF}`"
            out.append(f"| {link} | {desc}{kw_line} | {install} |")
        out.append("")  # blank line after each table

    out.append("---\n")
    out.append(
        "*Bundles (roles, suites) auto-install their dependencies — see "
        "[Bundles & dependencies](BUNDLES.md). New to the marketplace? Start with "
        "[Getting started](GETTING_STARTED.md).*"
    )
    return "\n".join(out) + "\n"


def _generate() -> None:
    """mkdocs-gen-files entrypoint: write virtual pages into the build."""
    import mkdocs_gen_files  # imported lazily so the module stays unit-testable

    plugins = load_catalog()

    with mkdocs_gen_files.open("catalog.md", "w") as f:
        f.write(build_catalog_markdown(plugins))

    # Copy the banner into the site tree without duplicating it in git.
    if BANNER.is_file():
        with mkdocs_gen_files.open("assets/banner.png", "wb") as f:
            f.write(BANNER.read_bytes())


# mkdocs-gen-files executes this module top-to-bottom at build time. When run
# standalone (e.g. unit-testing build_catalog_markdown), the package is absent and
# we no-op instead of erroring.
try:
    import mkdocs_gen_files  # noqa: F401
except ImportError:
    pass
else:
    _generate()

