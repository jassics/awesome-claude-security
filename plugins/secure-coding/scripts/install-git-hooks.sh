#!/usr/bin/env bash
# Installs real (non-Claude-Code) git enforcement into the target repo, so
# secrets/vulnerable-pattern blocking works even when pushing from a plain
# terminal, another IDE, or CI — not just inside a Claude Code session.
#
# Usage: install-git-hooks.sh [path-to-target-repo]   (defaults to cwd)
set -euo pipefail

TARGET="${1:-$(pwd)}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_ROOT="$(dirname "$SCRIPT_DIR")"

if ! git -C "$TARGET" rev-parse --show-toplevel >/dev/null 2>&1; then
  echo "error: $TARGET is not a git repository" >&2
  exit 1
fi
TARGET="$(git -C "$TARGET" rev-parse --show-toplevel)"

echo "Installing secure-coding git enforcement into: $TARGET"

if command -v pre-commit >/dev/null 2>&1; then
  echo "-> pre-commit found, writing .pre-commit-config.yaml"
  sed \
    -e "s#__RULES_DIR__#${PLUGIN_ROOT}/rules#g" \
    -e "s#__SCRIPTS_DIR__#${PLUGIN_ROOT}/scripts#g" \
    "$SCRIPT_DIR/pre-commit-config.template.yaml" > "$TARGET/.pre-commit-config.yaml.secure-coding"

  if [ -f "$TARGET/.pre-commit-config.yaml" ]; then
    echo "   NOTE: $TARGET/.pre-commit-config.yaml already exists."
    echo "   Wrote the secure-coding hooks to .pre-commit-config.yaml.secure-coding instead —"
    echo "   merge its 'repos:' entries into your existing config, then remove the .secure-coding file."
  else
    mv "$TARGET/.pre-commit-config.yaml.secure-coding" "$TARGET/.pre-commit-config.yaml"
  fi

  (cd "$TARGET" && pre-commit install --hook-type pre-commit --hook-type pre-push)
  echo "-> pre-commit hooks installed (pre-commit + pre-push)."
else
  echo "-> pre-commit not found; falling back to a native git pre-push hook."
  echo "   (Recommended: pip install pre-commit, then re-run this script for full coverage.)"
  HOOK="$TARGET/.git/hooks/pre-push"
  cat > "$HOOK" <<EOF
#!/usr/bin/env bash
# Installed by secure-coding plugin (native fallback, no pre-commit framework found).
"$PLUGIN_ROOT/scripts/check-gitignore.py" || exit 1
if command -v gitleaks >/dev/null 2>&1; then
  gitleaks detect --source "$TARGET" -v --no-banner || exit 1
else
  echo "gitleaks not installed — install it for real secret-scanning coverage: https://github.com/gitleaks/gitleaks" >&2
fi
EOF
  chmod +x "$HOOK"
  echo "-> wrote $HOOK"
fi

echo ""
echo "Done. Tools this relies on for full coverage (install what's missing):"
command -v gitleaks >/dev/null 2>&1 && echo "  [x] gitleaks" || echo "  [ ] gitleaks — https://github.com/gitleaks/gitleaks"
command -v semgrep >/dev/null 2>&1 && echo "  [x] semgrep" || echo "  [ ] semgrep — pip install semgrep"
command -v bandit >/dev/null 2>&1 && echo "  [x] bandit" || echo "  [ ] bandit — pip install bandit[toml]"
command -v detect-secrets >/dev/null 2>&1 && echo "  [x] detect-secrets" || echo "  [ ] detect-secrets — pip install detect-secrets"
