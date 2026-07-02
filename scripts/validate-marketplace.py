#!/usr/bin/env python3
"""Structural validator for the awesome-claude-security marketplace.

Pure standard-library — no deps, runs anywhere. Guards the invariants that, if
broken, make `/plugin install` fail for users:

  1. marketplace.json parses and each entry is well-formed.
  2. Catalog <-> directory parity: every listed plugin has a directory and vice versa.
  3. name == directory == catalog entry (kebab-case), per CLAUDE.md conventions.
  4. Every `dependencies` entry resolves to a plugin that exists in this repo.
  5. Every SKILL.md has non-empty `name`/`description`, and skill dir == skill name.
  6. Every agent .md has non-empty `name`/`description` and declares none of the
     forbidden keys (hooks / mcpServers / permissionMode).

Exit code 0 = clean, 1 = one or more violations (printed).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGINS_DIR = ROOT / "plugins"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"

KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FORBIDDEN_AGENT_KEYS = ("hooks", "mcpServers", "permissionMode")

errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def parse_frontmatter(path: Path) -> dict | None:
    """Minimal YAML-frontmatter reader: top-level scalar + folded-block values.

    Enough to check that `name`/`description` exist and are non-empty, and to
    detect forbidden top-level keys. Not a full YAML parser by design.
    """
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    lines = text.splitlines()
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return None
    data: dict[str, str] = {}
    cur: str | None = None
    for line in lines[1:end]:
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m and not line.startswith((" ", "\t")):
            cur = m.group(1)
            val = m.group(2).strip()
            data[cur] = "" if val in (">-", ">", "|", "|-", ">+", "") else val.strip("\"'")
        elif cur is not None and line.strip():
            data[cur] = (data[cur] + " " + line.strip()).strip()
    return data


def check_skill(skill_dir: Path, plugin: str) -> None:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        err(f"{plugin}: skill '{skill_dir.name}' has no SKILL.md")
        return
    fm = parse_frontmatter(skill_md)
    if fm is None:
        err(f"{plugin}/{skill_dir.name}: SKILL.md missing frontmatter")
        return
    if not fm.get("name"):
        err(f"{plugin}/{skill_dir.name}: SKILL.md has no `name`")
    elif fm["name"] != skill_dir.name:
        err(f"{plugin}/{skill_dir.name}: skill name '{fm['name']}' != directory name")
    if not fm.get("description"):
        err(f"{plugin}/{skill_dir.name}: SKILL.md has empty `description` (it's the trigger)")


def check_agent(agent_md: Path, plugin: str) -> None:
    fm = parse_frontmatter(agent_md)
    if fm is None:
        err(f"{plugin}/agents/{agent_md.name}: missing frontmatter")
        return
    if not fm.get("name"):
        err(f"{plugin}/agents/{agent_md.name}: no `name`")
    if not fm.get("description"):
        err(f"{plugin}/agents/{agent_md.name}: empty `description`")
    for k in FORBIDDEN_AGENT_KEYS:
        if k in fm:
            err(f"{plugin}/agents/{agent_md.name}: declares forbidden key '{k}' (not allowed in plugin agents)")


def main() -> int:
    if not MARKETPLACE.is_file():
        err(f"missing {MARKETPLACE.relative_to(ROOT)}")
        return report()

    try:
        catalog = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        err(f"marketplace.json is not valid JSON: {e}")
        return report()

    entries = catalog.get("plugins", [])
    catalog_names: set[str] = set()
    for e in entries:
        name, source = e.get("name"), e.get("source")
        if not name:
            err(f"marketplace entry missing `name`: {e}")
            continue
        catalog_names.add(name)
        for field in ("source", "description", "category"):
            if not e.get(field):
                err(f"marketplace entry '{name}' missing `{field}`")
        expected_source = f"./plugins/{name}"
        if source and source != expected_source:
            err(f"marketplace entry '{name}': source '{source}' should be '{expected_source}'")
        if not KEBAB.match(name):
            err(f"marketplace entry '{name}' is not kebab-case")
        if not (ROOT / (source or expected_source)).is_dir():
            err(f"marketplace entry '{name}' points to missing directory {source or expected_source}")

    # Reverse parity + per-plugin checks.
    dirs = sorted(p for p in PLUGINS_DIR.iterdir() if p.is_dir())
    dir_names = {p.name for p in dirs}
    for p in dirs:
        if p.name not in catalog_names:
            err(f"plugin directory '{p.name}' is not listed in marketplace.json")

        manifest = p / ".claude-plugin" / "plugin.json"
        if not manifest.is_file():
            err(f"{p.name}: missing .claude-plugin/plugin.json")
            continue
        try:
            mf = json.loads(manifest.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            err(f"{p.name}: plugin.json is not valid JSON: {e}")
            continue
        if mf.get("name") != p.name:
            err(f"{p.name}: plugin.json name '{mf.get('name')}' != directory name")
        for dep in mf.get("dependencies", []):
            dep_name = dep if isinstance(dep, str) else dep.get("name")
            if dep_name not in dir_names:
                err(f"{p.name}: dependency '{dep_name}' does not exist in this marketplace")

        skills_dir = p / "skills"
        if skills_dir.is_dir():
            for s in sorted(x for x in skills_dir.iterdir() if x.is_dir()):
                check_skill(s, p.name)
        agents_dir = p / "agents"
        if agents_dir.is_dir():
            for a in sorted(agents_dir.glob("*.md")):
                check_agent(a, p.name)

    # Wrong-place components: catch folders nested under .claude-plugin/.
    for p in dirs:
        cp = p / ".claude-plugin"
        if cp.is_dir():
            for stray in ("skills", "agents", "commands", "hooks"):
                if (cp / stray).exists():
                    err(f"{p.name}: '{stray}/' is inside .claude-plugin/ — must be at plugin root")

    return report()


def report() -> int:
    if errors:
        print(f"✗ {len(errors)} validation error(s):\n")
        for e in errors:
            print(f"  - {e}")
        return 1
    n_plugins = len([p for p in PLUGINS_DIR.iterdir() if p.is_dir()])
    n_skills = len(list(PLUGINS_DIR.glob("*/skills/*/SKILL.md")))
    n_agents = len(list(PLUGINS_DIR.glob("*/agents/*.md")))
    print(f"✓ marketplace OK — {n_plugins} plugins, {n_skills} skills, {n_agents} agents, all invariants hold")
    return 0


if __name__ == "__main__":
    sys.exit(main())
