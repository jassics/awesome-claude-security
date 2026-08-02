#!/usr/bin/env python3
"""Claude Code PreToolUse hook: block `git commit`/`git push` when the change
being committed/pushed contains a secret or a file that must never be tracked.

Reads the Claude Code hook JSON payload from stdin ({"tool_name", "tool_input",
"cwd", ...}). Exit 0 = allow. Exit 2 with a stderr message = block the tool call.
Fails open (exit 0) on any internal error — this is a guard rail, not the only
line of defense (see scripts/install-git-hooks.sh for the enforcement that also
covers pushes made outside Claude Code).
"""
import json
import os
import re
import subprocess
import sys

PLUGIN_ROOT = os.environ.get("CLAUDE_PLUGIN_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

GIT_COMMIT_OR_PUSH = re.compile(r"(?<![\w-])git\s+(commit|push)\b")

SECRET_PATTERNS = [
    ("AWS Access Key ID", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("GCP API key", re.compile(r"AIza[0-9A-Za-z\-_]{35}")),
    ("GCP service account JSON", re.compile(r'"type"\s*:\s*"service_account"')),
    ("Azure storage key", re.compile(r"AccountKey=[A-Za-z0-9+/=]{88}")),
    ("Slack token", re.compile(r"xox[baprs]-[0-9A-Za-z-]{10,48}")),
    ("GitHub token", re.compile(r"gh[pousr]_[0-9A-Za-z]{36,}")),
    ("Stripe live key", re.compile(r"sk_live_[0-9a-zA-Z]{24,}")),
    ("Private key header", re.compile(r"-----BEGIN (RSA|EC|OPENSSH|PGP|DSA) PRIVATE KEY-----")),
    ("JWT", re.compile(r"eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+")),
    ("Generic secret assignment", re.compile(
        r"(?i)(api_?key|secret|token|password|passwd|pwd)\s*[:=]\s*['\"][^'\"]{12,}['\"]"
    )),
]


def load_sensitive_patterns():
    path = os.path.join(PLUGIN_ROOT, "rules", "gitignore-required.txt")
    patterns = []
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    patterns.append(line)
    except OSError:
        pass
    return patterns


def fnmatch_any(filename, patterns):
    import fnmatch
    base = os.path.basename(filename)
    return any(fnmatch.fnmatch(filename, p) or fnmatch.fnmatch(base, p) for p in patterns)


def run(cmd, cwd):
    try:
        out = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=15)
        return out.stdout
    except Exception:
        return ""


def run_rc(cmd, cwd):
    """Like run(), but also returns the process exit code (-1 on failure to run)."""
    try:
        out = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=15)
        return out.stdout, out.returncode
    except Exception:
        return "", -1


def which(binname):
    for d in os.environ.get("PATH", "").split(os.pathsep):
        if os.path.isfile(os.path.join(d, binname)):
            return True
    return False


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # fail open — not our job to break unrelated tool calls

    if payload.get("tool_name") != "Bash":
        sys.exit(0)

    command = (payload.get("tool_input") or {}).get("command", "")
    if not GIT_COMMIT_OR_PUSH.search(command):
        sys.exit(0)

    cwd = payload.get("cwd") or os.getcwd()
    is_commit = bool(re.search(r"(?<![\w-])git\s+commit\b", command))

    toplevel = run(["git", "rev-parse", "--show-toplevel"], cwd).strip()
    if not toplevel:
        sys.exit(0)  # not a git repo, nothing to guard

    if is_commit:
        files = [f for f in run(["git", "diff", "--cached", "--name-only"], toplevel).splitlines() if f]
        diff_text = run(["git", "diff", "--cached", "-U0"], toplevel)
    else:
        # Best-effort: commits reachable locally but not on any remote-tracking branch.
        files = [f for f in run(
            ["git", "log", "--branches", "--not", "--remotes", "--name-only", "--pretty=format:"], toplevel
        ).splitlines() if f]
        diff_text = run(["git", "log", "--branches", "--not", "--remotes", "-p"], toplevel)

    findings = []

    sensitive_patterns = load_sensitive_patterns()
    for f in sorted(set(files)):
        if fnmatch_any(f, sensitive_patterns):
            findings.append(f"sensitive file staged/committed: {f} (matches a pattern that must never be tracked)")

    if which("gitleaks"):
        if is_commit:
            gl_cmd = ["gitleaks", "protect", "--staged", "--verbose", "--no-banner"]
        else:
            # Use a relative --source (run from toplevel as cwd) so fingerprints match
            # a repo-committed .gitleaksignore regardless of the clone's absolute path.
            gl_cmd = ["gitleaks", "detect", "--source", ".", "--no-git", "-v", "--no-banner"]
        _gl_out, gl_rc = run_rc(gl_cmd, toplevel)
        # gitleaks exit codes: 0 = clean, 1 = leaks found, >1 = tool error (fail open).
        if gl_rc == 1:
            findings.append("gitleaks reported one or more leaks (run `gitleaks protect --staged -v` for detail)")
    else:
        for name, pattern in SECRET_PATTERNS:
            if pattern.search(diff_text):
                findings.append(f"pattern match for {name} in the diff being committed/pushed")

    if findings:
        msg = ["BLOCKED by secure-coding plugin (secret-guard): possible secret or sensitive file in this change.", ""]
        msg += [f"- {x}" for x in findings]
        msg += [
            "",
            "If this is a false positive, fix the underlying pattern or ask the user to run the command",
            "directly outside Claude Code. Do not bypass by rewriting the command to avoid this hook.",
            "Real fix: remove the secret/file from the change, load secrets from env/secret manager,",
            "and rotate any credential that was ever committed.",
        ]
        print("\n".join(msg), file=sys.stderr)
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
