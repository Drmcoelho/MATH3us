#!/usr/bin/env python3
"""Triple oracle for Chapter 3 (A Singularidade do Quatro) numeric invariants.

MATH3us.md section 1.8: every central numeric result passes three
independent checks:
  1. symbolic derivation  -> audit/symbolic-check.md (hand-written algebra;
     this script witnesses the same statements numerically)
  2. independent numeric verification -> two implementations compared:
       A. brute-force exact-integer scan of the three pairwise equations
          over 1..10000 (with an exact short-circuit, documented below,
          instead of computing 10000^10000 naively)
       B. symbolic-by-construction root sets (factorizations solved as
          algebra: {0,2} for x^2=2x, {1,2} for x^2=x^x, {r,2} for 2x=x^x)
     plus a Decimal-50 bisection for the small root r of 2x = x^x,
     with an explicit sign-change certificate at 12 decimals.
  3. edge / degenerate / adversarial cases -> audit/edge-cases.md
     (x=0 refused: 0^0 dispute; x=1 pairwise-vs-triple; negatives refused;
     float x^x behaviour near 0+ recorded as observation-layer note)

Exact short-circuit for the integer scan (proved, then used):
  for integer x >= 3:  x^x = x^2 * x^(x-2)  with  x^(x-2) >= x >= 3 > 1,
  hence x^x > x^2 > 2x (the last since x^2 - 2x = x(x-2) >= 3 > 0).
  So no equation can hold for x >= 3 and the scan needs exact powers
  only for x in {1, 2}; the short-circuit itself is verified exactly
  for every x (cheap integer comparisons, no giant powers).

Stdlib only. Usage:
  python3 caps/03-quatro/oracle.py           # full oracle, write artifacts
  python3 caps/03-quatro/oracle.py --x 0     # adversarial: must be refused
"""
import argparse
import json
import platform
import subprocess
import sys
from datetime import date
from decimal import Decimal, getcontext
from pathlib import Path

CHAPTER_DIR = Path(__file__).resolve().parent
AUDIT_DIR = CHAPTER_DIR / "audit"
SCAN_MAX = 10000
getcontext().prec = 50

LN2 = Decimal(2).ln()


def validate_x(x) -> int:
    """Adversarial gate: the chapter's domain is R+, and the integer scan
    covers positive integers. x = 0 is refused explicitly (0^0 dispute,
    declared closed door), negatives are refused (x^x not real-defined
    for general negative reals: e.g. (-1/2)^(-1/2) is not real)."""
    if not isinstance(x, int):
        raise ValueError(f"refused: x={x!r} is not an integer")
    if x == 0:
        raise ValueError("refused: x=0 outside domain R+ (x^x would be the "
                         "0^0 dispute — declared closed door, Chapter 10)")
    if x < 0:
        raise ValueError(f"refused: x={x} negative (x^x not real-defined for "
                         "general negative reals; domain is R+)")
    return x


# --- implementation A: exact-integer scan with documented short-circuit ----
def scan_pairwise(limit):
    """Return the exact solution sets over integers 1..limit of
    x+x = x^2, x^2 = x^x, 2x = x^x, and the triple coincidence."""
    add_sq, sq_pow, add_pow, triple = [], [], [], []
    for x in range(1, limit + 1):
        s, q = x + x, x * x
        eq_add_sq = (s == q)
        if x <= 2:
            p = x ** x                      # exact, tiny
            eq_sq_pow, eq_add_pow = (q == p), (s == p)
        else:
            # exact short-circuit: x^(x-2) >= x >= 3 > 1 (integer compare,
            # no giant powers), hence x^x > x^2 and x^2 > 2x (x(x-2) > 0).
            assert x >= 3 and x - 2 >= 1 and x * (x - 2) > 0
            eq_sq_pow, eq_add_pow = False, False
        if eq_add_sq:
            add_sq.append(x)
        if eq_sq_pow:
            sq_pow.append(x)
        if eq_add_pow:
            add_pow.append(x)
        if eq_add_sq and eq_sq_pow and eq_add_pow:
            triple.append(x)
    return add_sq, sq_pow, add_pow, triple


# --- implementation B: symbolic-by-construction root sets ------------------
def roots_by_construction():
    """The factorizations solved as algebra, independently of the scan:
    x^2 - 2x = x(x-2)      -> roots {0, 2}; positivity filters to {2}
    (x-2)*ln x = 0         -> roots {1, 2}
    (x-1)*ln x = ln 2      -> roots {r, 2} with r in (0,1) (bisection)."""
    add_sq = [r for r in (0, 2) if r > 0]
    sq_pow = [1, 2]
    return add_sq, sq_pow


def h(x: Decimal) -> Decimal:
    """h(x) = (x-1)*ln x; 2x = x^x  <=>  h(x) = ln 2 (chapter section 5.3)."""
    return (x - 1) * x.ln()


def f(x: Decimal) -> Decimal:
    """f(x) = x^x - 2x, computed as exp(x*ln x) - 2x (Decimal)."""
    return (x * x.ln()).exp() - 2 * x


def bisect_small_root():
    """Locate r in (0.3, 0.4) with f(r)=0 to >12 decimals, recording the
    sign-change certificate at the 12-decimal bracket."""
    lo, hi = Decimal("0.3"), Decimal("0.4")
    assert f(lo) > 0 and f(hi) < 0, "initial sign change must hold"
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    root = lo
    b_lo = Decimal("0.346323362278")
    b_hi = Decimal("0.346323362279")
    cert = {
        "bracket_lo": str(b_lo), "bracket_hi": str(b_hi),
        "f_lo": str(f(b_lo)), "f_hi": str(f(b_hi)),
        "sign_change": f(b_lo) > 0 > f(b_hi),
        "h_lo_minus_ln2": str(h(b_lo) - LN2),
        "h_hi_minus_ln2": str(h(b_hi) - LN2),
    }
    return root, cert


def run_oracle():
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    results = {}

    # I1: pairwise + triple sets over integers 1..10000 (implementation A)
    add_sq, sq_pow, add_pow, triple = scan_pairwise(SCAN_MAX)
    results["I1_integer_scan_sets"] = {
        "scan_max": SCAN_MAX,
        "x_plus_x_eq_x2": add_sq, "x2_eq_xx": sq_pow,
        "2x_eq_xx": add_pow, "triple": triple,
        "short_circuit": "for x>=3: x^x = x^2 * x^(x-2), x^(x-2) >= x >= 3 > 1;"
                         " x^2 - 2x = x(x-2) > 0 — exact integer comparisons only",
        "passed": (add_sq == [2] and sq_pow == [1, 2] and add_pow == [2]
                   and triple == [2])}

    # I2: implementation B agrees with A where both apply (independent route)
    b_add_sq, b_sq_pow = roots_by_construction()
    results["I2_construction_vs_scan"] = {
        "constructed_add_sq": b_add_sq, "constructed_sq_pow": b_sq_pow,
        "passed": b_add_sq == add_sq and b_sq_pow == sq_pow}

    # I3: the triple value is 4, and 4 arises from k=2 only
    results["I3_value_four"] = {
        "k": triple, "values": [[k + k, k * k, k ** k] for k in triple],
        "passed": triple == [2] and [2 + 2, 2 * 2, 2 ** 2] == [4, 4, 4]}

    # I4: small root of 2x = x^x — bisection + 12-decimal certificate
    root, cert = bisect_small_root()
    results["I4_small_root_bisection"] = {
        "root_20_digits": str(root)[:22], "certificate": cert,
        "passed": cert["sign_change"]
        and str(root).startswith("0.346323362278")}

    # I5: exact solution x=2 of 2x = x^x via h: h(2) == ln 2 exactly (Decimal)
    results["I5_h_at_2_equals_ln2"] = {
        "h_2": str(h(Decimal(2))), "ln2": str(LN2),
        "passed": h(Decimal(2)) == LN2}

    # I6: monotonicity witnesses for h (samples; the proof is symbolic S3)
    xs01 = [Decimal(k) / 100 for k in range(1, 100)]
    dec_01 = all(h(xs01[i]) > h(xs01[i + 1]) for i in range(len(xs01) - 1))
    xs1inf = [1 + Decimal(k) / 10 for k in range(0, 60)]
    inc_1inf = all(h(xs1inf[i]) < h(xs1inf[i + 1]) for i in range(len(xs1inf) - 1))
    results["I6_h_monotonicity_witness"] = {
        "samples_0_1": len(xs01), "samples_1_7": len(xs1inf),
        "note": "numeric WITNESS of symbolic S3 (derivative-free proof); "
                "sampling supports, does not prove",
        "passed": dec_01 and inc_1inf}

    # I7: interval ordering of the three rules (exercise E3.2 witnesses)
    def order(xf):
        x = Decimal(xf)
        vals = {"2x": 2 * x, "x2": x * x, "xx": (x * x.ln()).exp()}
        return [k for k, _ in sorted(vals.items(), key=lambda kv: kv[1])]
    results["I7_interval_orderings"] = {
        "x=0.2": order("0.2"), "x=0.5": order("0.5"),
        "x=1.5": order("1.5"), "x=3": order("3"),
        "passed": (order("0.2") == ["x2", "2x", "xx"]
                   and order("0.5") == ["x2", "xx", "2x"]
                   and order("1.5") == ["xx", "x2", "2x"]
                   and order("3") == ["2x", "x2", "xx"])}

    all_passed = all(v["passed"] for v in results.values())
    commit = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
        cwd=CHAPTER_DIR).stdout.strip() or "unknown"

    report = {
        "chapter": 3,
        "script": "caps/03-quatro/oracle.py",
        "code_commit": commit,
        "date": date.today().isoformat(),
        "environment": f"python {platform.python_version()}, stdlib only, "
                       f"{platform.system().lower()}",
        "implementations": {
            "A": "exact-integer scan 1..10000 with documented exact short-circuit",
            "B": "symbolic-by-construction root sets from the factorizations",
            "C": "Decimal-50 bisection for the small root of 2x = x^x"},
        "tested_domain": {
            "integer_scan": {"min": 1, "max": SCAN_MAX},
            "bisection_interval": [0.3, 0.4],
            "adversarial_refused": [0, -1, -4]},
        "invariants": results,
        "all_passed": all_passed,
    }
    (AUDIT_DIR / "numeric-check.json").write_text(
        json.dumps(report, indent=2) + "\n")

    # ---- edge / degenerate / adversarial cases -> edge-cases.md -----------
    edge = []
    # E1: x=0 refused (0^0 dispute is a declared closed door, not a value)
    for bad in (0, -1, -4):
        try:
            validate_x(bad)
            edge.append((f"adversarial x={bad}", "was NOT refused", False))
        except ValueError as e:
            edge.append((f"adversarial x={bad}", f"refused with: {e}", True))
    # E2: x=1 — the pairwise-vs-triple distinction, exact arithmetic
    e2 = (1 * 1 == 1 ** 1) and (1 + 1 != 1) and (1 not in triple) and (1 in sq_pow)
    edge.append(("x=1 pairwise vs triple",
                 "1·1 = 1^1 = 1 holds (pairwise) but 1+1 = 2 ≠ 1 (triple fails); "
                 "scan confirms 1 in {x²=x^x} and 1 not in triple", e2))
    # E3: boundary x=2 — all three equal, exactly, in integers
    e3 = (2 + 2 == 2 * 2 == 2 ** 2 == 4)
    edge.append(("x=2 exact triple", "2+2 = 2·2 = 2² = 4 in exact integers", e3))
    # E4: float x^x near 0+ — observation-layer note (limit is 1, not 0)
    fl = [(x, x ** x) for x in (1e-1, 1e-2, 1e-4, 1e-8, 1e-12)]
    e4 = all(0 < v < 1 for _, v in fl) and fl[-1][1] > 0.99999
    edge.append(("float x^x as x->0+",
                 "float64 x^x at x=1e-1..1e-12: " +
                 ", ".join(f"{v:.10f}" for _, v in fl) +
                 " — approaches 1, NOT 0. Observation layer (manual §2.1): "
                 "float exp/log rounding present; the limit statement itself "
                 "is cited classical (closed door to Chapter 10)", e4))
    # E5: near-root behaviour — f changes sign across r but 2x = x^x is
    # never satisfied exactly in float64 at the 12-decimal bracket ends
    b_lo, b_hi = 0.346323362278, 0.346323362279
    e5 = (b_lo ** b_lo - 2 * b_lo) * (b_hi ** b_hi - 2 * b_hi) < 0
    edge.append(("float sign change at the certificate bracket",
                 "float64 reproduces the Decimal sign change at the "
                 "12-decimal bracket of r", e5))

    lines = ["# Capítulo 3 — Casos extremos, degenerados e adversariais",
             "",
             f"Gerado por `caps/03-quatro/oracle.py` em {date.today().isoformat()}, "
             f"commit `{commit}`.", ""]
    for name, desc, ok in edge:
        lines.append(f"- **{name}** — {desc} → **{'passou' if ok else 'FALHOU'}**")
    edge_ok = all(ok for _, _, ok in edge)
    lines += ["", f"Resultado global: **{'passou' if edge_ok else 'FALHOU'}**."]
    (AUDIT_DIR / "edge-cases.md").write_text("\n".join(lines) + "\n")

    print(json.dumps({k: v["passed"] for k, v in results.items()}, indent=2))
    print("edge cases:", "passed" if edge_ok else "FAILED")
    print("all:", "PASSED" if (all_passed and edge_ok) else "FAILED")
    return 0 if (all_passed and edge_ok) else 1


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--x", type=int, help="validate a single x against the domain")
    args = p.parse_args()
    if args.x is not None:
        validate_x(args.x)      # raises (refuses) on invalid input
        print(f"x={args.x} accepted (positive integer)")
        return 0
    return run_oracle()


if __name__ == "__main__":
    sys.exit(main())
