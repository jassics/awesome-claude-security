#!/usr/bin/env python3
"""Compute an exact CVSS 4.0 score from a vector string.

CVSS 4.0 does not use a closed-form arithmetic formula like 3.1 did -- it
maps the vector to one of 270 "MacroVectors" (via 6 equivalence classes)
and looks up/interpolates a score from a table defined in the official
specification (first.org/cvss/v4-0). Reproducing that table by hand or from
an LLM's memory is exactly the kind of thing that looks fine but silently
produces a wrong number -- so this wraps the `cvss` PyPI package (RedHat
Product Security's implementation of the official algorithm) rather than
reimplementing it.

Usage:
    python3 cvss4-score.py "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N"

Accepts Base metrics alone, or a vector that also includes Threat (E) and/or
Environmental (CR/IR/AR, MAV/MAC/MAT/MPR/MUI/MVC/MVI/MVA/MSC/MSI/MSA) metrics
-- CVSS 4.0 computes all of these through the same single scoring algorithm,
there is no separate "environmental score" formula to call out to.

Exit 0 = scored successfully (prints the result), 1 = invalid vector,
2 = the `cvss` package isn't installed (fails open rather than blocking
the caller).
"""
from __future__ import annotations

import sys

try:
    from cvss import CVSS4
    from cvss.exceptions import CVSS4MalformedError
except ImportError:
    print(
        "cvss4-score requires the `cvss` package (`pip install cvss`) to compute "
        "an exact score -- skipping rather than guessing.",
        file=sys.stderr,
    )
    sys.exit(2)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: cvss4-score.py '<CVSS:4.0/... vector string>'", file=sys.stderr)
        return 1
    vector = sys.argv[1]

    try:
        c = CVSS4(vector)
    except CVSS4MalformedError as e:
        print(f"Invalid CVSS 4.0 vector: {e}", file=sys.stderr)
        return 1

    score = c.base_score
    severity = c.severities()[0]
    refinement_prefixes = ("E:", "CR:", "IR:", "AR:", "MAV:", "MAC:", "MAT:", "MPR:",
                            "MUI:", "MVC:", "MVI:", "MVA:", "MSC:", "MSI:", "MSA:")
    refined = any(f"/{m}" in vector for m in refinement_prefixes)

    print(f"CVSS 4.0: {score} ({severity})")
    print(f"Vector: {c.clean_vector()}")
    if refined:
        print("Note: score reflects Threat and/or Environmental refinement metrics "
              "present in the vector, computed by the same single algorithm as the "
              "Base score (CVSS 4.0 has no separate environmental formula).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
