#!/usr/bin/env python3
"""Lint GitHub Actions workflows for the two config gaps that have no safe
platform default: a job with no `timeout-minutes`, and a workflow with no
`concurrency` group.

Why these two, specifically: on GitHub-hosted runners a missing job timeout
still falls back to a hard 360-minute (6h) platform ceiling -- generous, but
bounded. On a self-hosted runner (or a custom runner-group label), that
ceiling does NOT apply; the only remaining bound is the workflow run's
absolute 72-hour maximum. A missing `concurrency` key means GitHub will run
unlimited concurrent/duplicate workflow runs for the same ref -- a rapid
sequence of pushes, or a workflow_dispatch storm, can pile up runner-minutes
with nothing to dedupe or cancel them.

Run with no args from a repo root (scans .github/workflows/*.yml|*.yaml), or
pass one or more paths to specific workflow files.

Exit 0 = clean, 1 = one or more findings, 2 = could not run (e.g. PyYAML
missing) -- fails open on runtime errors so a broken workflow file can't
crash a CI gate.
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print(
        "pipeline-timeout-lint requires PyYAML (`pip install pyyaml`) to parse "
        "workflow YAML -- skipping this check rather than failing the caller.",
        file=sys.stderr,
    )
    sys.exit(2)

# Labels GitHub documents as hosted (still bounded at 360 min if no
# timeout-minutes is set). Anything else -- custom labels, runner groups,
# the literal 'self-hosted' -- gets no per-job cap at all.
_HOSTED_PREFIXES = ("ubuntu-", "windows-", "macos-")


def _is_hosted(runs_on) -> bool:
    if isinstance(runs_on, list):
        return all(_is_hosted(r) for r in runs_on) if runs_on else False
    if isinstance(runs_on, dict):
        return False  # runner-group / custom-label object syntax -- treat as non-hosted
    if not isinstance(runs_on, str):
        return False
    return runs_on.lower().startswith(_HOSTED_PREFIXES)


def lint_workflow(path: Path) -> list[str]:
    findings: list[str] = []
    try:
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        findings.append(f"{path}: could not parse YAML ({e}) -- skipped")
        return findings
    if not isinstance(doc, dict):
        return findings

    if "concurrency" not in doc:
        findings.append(
            f"{path}: MEDIUM -- no top-level 'concurrency' group. GitHub runs "
            "unlimited concurrent/duplicate workflow runs for the same ref with "
            "no dedupe or cancellation. Add a 'concurrency' block (e.g. "
            "group: ${{ github.workflow }}-${{ github.ref }}, "
            "cancel-in-progress: true)."
        )

    jobs = doc.get("jobs")
    if not isinstance(jobs, dict):
        return findings

    for job_id, job in jobs.items():
        if not isinstance(job, dict):
            continue
        if "timeout-minutes" in job:
            continue
        runs_on = job.get("runs-on")
        if _is_hosted(runs_on):
            findings.append(
                f"{path}: LOW -- job '{job_id}' has no 'timeout-minutes'. "
                "Falls back to the platform's 360-minute (6h) ceiling for "
                f"hosted runners ({runs_on!r}) -- set an explicit, tighter bound."
            )
        else:
            findings.append(
                f"{path}: HIGH -- job '{job_id}' runs on a non-hosted runner "
                f"({runs_on!r}) with no 'timeout-minutes'. The 360-minute hosted "
                "ceiling does NOT apply here -- only the workflow's absolute "
                "72-hour maximum bounds it. Set an explicit timeout-minutes."
            )

    return findings


def discover(repo_root: Path) -> list[Path]:
    wf_dir = repo_root / ".github" / "workflows"
    if not wf_dir.is_dir():
        return []
    return sorted(list(wf_dir.glob("*.yml")) + list(wf_dir.glob("*.yaml")))


def main() -> int:
    args = sys.argv[1:]
    if args:
        paths = [Path(a) for a in args]
    else:
        paths = discover(Path.cwd())

    if not paths:
        print("No GitHub Actions workflow files found (.github/workflows/*.yml).")
        return 0

    all_findings: list[str] = []
    for p in paths:
        if p.is_file():
            all_findings.extend(lint_workflow(p))

    if all_findings:
        print(f"pipeline-timeout-lint: {len(all_findings)} finding(s):\n", file=sys.stderr)
        for f in all_findings:
            print(f"  - {f}", file=sys.stderr)
        return 1

    print(f"pipeline-timeout-lint: clean ({len(paths)} workflow file(s) scanned).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
