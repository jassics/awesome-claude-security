#!/usr/bin/env python3
"""Compare a promptfoo eval run against a committed baseline.

Exits non-zero only on a real pass-rate regression beyond TOLERANCE — not on
absolute finding counts (LLM outputs have natural run-to-run variance). See
../../EVAL-GATE-NOTES.md for the rollout/tuning rationale. Verify the JSON
shape below against your installed promptfoo version's actual output format —
it may not match exactly across versions.
"""

import json
import sys

TOLERANCE = 0.02  # allowed pass-rate drop before this counts as a regression


def pass_rate(report: dict) -> float:
    stats = report.get("results", {}).get("stats", {})
    passed = stats.get("successes", 0)
    total = passed + stats.get("failures", 0)
    return passed / total if total else 1.0


def main() -> int:
    baseline_path, current_path = sys.argv[1], sys.argv[2]
    baseline_rate = pass_rate(json.load(open(baseline_path)))
    current_rate = pass_rate(json.load(open(current_path)))
    print(f"baseline pass rate: {baseline_rate:.2%}, current: {current_rate:.2%}")

    if current_rate + TOLERANCE < baseline_rate:
        print("::error::Eval pass rate regressed vs. baseline")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
