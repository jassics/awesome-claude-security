#!/usr/bin/env python3
"""Check the current repo's .gitignore against rules/gitignore-required.txt.
Exits non-zero (blocking, when wired as a pre-commit/pre-push hook) if a
required pattern is missing. Run with no args from anywhere inside the repo."""
import os
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PLUGIN_ROOT = os.path.dirname(SCRIPT_DIR)


def repo_root():
    try:
        return subprocess.run(
            ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True
        ).stdout.strip()
    except Exception:
        return os.getcwd()


def load_required():
    path = os.path.join(PLUGIN_ROOT, "rules", "gitignore-required.txt")
    required = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                required.append(line)
    return required


def main():
    root = repo_root()
    gitignore_path = os.path.join(root, ".gitignore")
    existing = ""
    if os.path.isfile(gitignore_path):
        with open(gitignore_path) as f:
            existing = f.read()

    missing = [p for p in load_required() if p not in existing]

    if missing:
        print("`.gitignore` is missing patterns that should never be trackable:", file=sys.stderr)
        for p in missing:
            print(f"  {p}", file=sys.stderr)
        print("\nAdd them (e.g. `cat >> .gitignore` with the list above) and re-run.", file=sys.stderr)
        sys.exit(1)

    print(".gitignore covers all required patterns.")
    sys.exit(0)


if __name__ == "__main__":
    main()
