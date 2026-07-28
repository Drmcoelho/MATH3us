#!/usr/bin/env python3
"""Triple oracle for Chapter 0 (A Inferencia) numeric invariants.

MATH3us.md section 1.8: every central numeric result passes three
independent checks:
  1. symbolic derivation -> audit/symbolic-check.md (hand-written algebra;
     this script cross-validates every inequality numerically)
  2. independent numeric verification -> three implementations compared:
       A. float64 STABLE forms (mirrors in-page JS):
          rho = cos(pi/n); deficit = 2 sin^2(pi/2n); gap = 2 sin(a) sin(b)
       B. float64 GEOMETRY: polygon built from vertex coordinates;
          R, r, L/2 measured; area by shoelace (no closed trig formulas)
       C. Decimal 50-digit Taylor series for sin/cos (different arithmetic)
  3. edge / degenerate / adversarial cases -> audit/edge-cases.md
     (domain refusal; the DOCUMENTED collapse of the direct float64
     representations - preregistered as C0.8 and observed during
     development in the naive gap check)

Stdlib only. Usage:
  python3 tools/oracle-ch00.py          # full oracle, writes artifacts
  python3 tools/oracle-ch00.py --n 2    # adversarial: must be refused
"""
import argparse
import json
import math
import platform
import subprocess
import sys
from datetime import date
from decimal import Decimal, getcontext
from pathlib import Path

CHAPTER_DIR = Path(__file__).resolve().parent.parent / "caps" / "00-inferencia"
AUDIT_DIR = CHAPTER_DIR / "audit"
getcontext().prec = 60

PI = math.pi
PI_D = Decimal("3.14159265358979323846264338327950288419716939937510582097494")


def validate_n(n) -> int:
    """Adversarial gate: the chapter's domain is integer n >= 3.
    Anything else must be refused, not silently accepted."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise ValueError(f"refused: n={n!r} is not an integer")
    if n < 3:
        raise ValueError(f"refused: n={n} outside domain (need n >= 3; "
                         "n=2 is a degenerate digon, n<=1 is not a polygon)")
    return n


# --- implementation A: float64 stable forms (mirrors in-page JS) ----------
def rho_A(n): return math.cos(PI / n)
def deficit_A(n): return 2.0 * math.sin(PI / (2 * n)) ** 2
def gap_A(n):
    a = PI * (2 * n + 1) / (2 * n * (n + 1))
    b = PI / (2 * n * (n + 1))
    return 2.0 * math.sin(a) * math.sin(b)


# --- implementation B: coordinate geometry (no closed trig formulas) ------
def polygon_B(n, R=1.0):
    """Vertices at angles (2k+1)*pi/n; returns (R_meas, r_meas, half_side,
    shoelace_area). Uses trig only to PLACE points (representation layer);
    all measured quantities come from coordinates."""
    verts = [(R * math.cos((2 * k + 1) * PI / n), R * math.sin((2 * k + 1) * PI / n))
             for k in range(n)]
    vx0, vy0 = verts[0]
    vx1, vy1 = verts[-1]           # adjacent vertex across the x-axis midpoint
    mx, my = (vx0 + vx1) / 2, (vy0 + vy1) / 2
    R_meas = math.hypot(vx0, vy0)
    r_meas = math.hypot(mx, my)
    half_side = math.hypot(vx0 - mx, vy0 - my)
    area = 0.0
    for i in range(n):
        x1, y1 = verts[i]
        x2, y2 = verts[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return R_meas, r_meas, half_side, abs(area) / 2.0


# --- implementation C: Decimal 50-digit Taylor series ---------------------
def dsin(x: Decimal) -> Decimal:
    s, t, k = x, x, 1
    while True:
        k += 2
        t *= -x * x / (k * (k - 1))
        s += t
        if abs(t) < Decimal(10) ** -55:
            return s

def dcos(x: Decimal) -> Decimal:
    s, t, k = Decimal(1), Decimal(1), 0
    while True:
        k += 2
        t *= -x * x / (k * (k - 1))
        s += t
        if abs(t) < Decimal(10) ** -55:
            return s

def rho_C(n): return dcos(PI_D / n)
def deficit_C(n): return 2 * dsin(PI_D / (2 * n)) ** 2
def gap_C(n):
    N = Decimal(n)
    a = PI_D * (2 * N + 1) / (2 * N * (N + 1))
    b = PI_D / (2 * N * (N + 1))
    return 2 * dsin(a) * dsin(b)


# --- decision rule (mirrors the in-page lab) ------------------------------
def decide(meas: float) -> int:
    """Nearest admissible rho_m, m >= 3."""
    if meas <= 0.5:
        return 3
    guess = max(3, int(PI / math.acos(min(meas, 1.0 - 1e-15))))
    best_m, best_d = None, None
    for m in range(max(3, guess - 3), guess + 5):
        d = abs(rho_A(m) - meas)
        if best_d is None or d < best_d:
            best_m, best_d = m, d
    return best_m


def run_oracle():
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    checks = []
    def record(inv, passed, detail):
        checks.append({"invariant": inv, "passed": bool(passed), "detail": detail})
        print(("ok   " if passed else "FAIL ") + inv + " - " + detail)

    # I1: fundamental triangle r^2 + (L/2)^2 = R^2 (geometry, several scales)
    worst = 0.0
    for n in [3, 4, 5, 7, 12, 96, 1000, 9973]:
        for R in [1.0, 1e-3, 1e3, PI]:
            Rm, rm, h, _ = polygon_B(n, R)
            worst = max(worst, abs(rm * rm + h * h - Rm * Rm) / (Rm * Rm))
    record("I1 fundamental-triangle", worst < 1e-14,
           f"max relative |r^2+(L/2)^2-R^2|/R^2 = {worst:.2e} over n and scales")

    # I2: polygon area n*(L/2)*r equals shoelace; trapped between C r^2 and C R^2
    # Tolerance scales with n: the shoelace accumulates ~n rounding steps.
    worst, trap_ok = 0.0, True
    for n in [3, 4, 5, 7, 12, 96, 1000, 9973]:
        Rm, rm, h, sho = polygon_B(n)
        formula = n * h * rm
        worst = max(worst, abs(formula - sho) / (sho * n * 2.3e-16))
        if not (PI * rm * rm < formula < PI * Rm * Rm):
            trap_ok = False
    record("I2 area-formula-and-trapping", worst < 50 and trap_ok,
           f"max |n(L/2)r - shoelace| = {worst:.1f} x (n*eps); strict trapping held")

    # I3: annulus identity C(R^2 - r^2) = C(L/2)^2, C-independent (test C=pi and C=1)
    # R^2 - r^2 is a subtraction of near-equal numbers for large n: its float64
    # relative error grows like eps/sin^2(pi/n) (the chapter's own section-8
    # lesson). The tolerance declares that cancellation factor explicitly.
    worst = 0.0
    for n in [3, 4, 5, 7, 12, 96, 1000, 9973]:
        Rm, rm, h, _ = polygon_B(n)
        tol = 50 * 2.3e-16 / math.sin(PI / n) ** 2
        for C in [PI, 1.0]:
            rel = abs(C * (Rm * Rm - rm * rm) - C * h * h) / (C * h * h)
            worst = max(worst, rel / tol)
    record("I3 annulus-identity", worst < 1,
           f"max relative error = {worst:.2f} x tolerance 50*eps/sin^2(pi/n) "
           "(cancellation-aware); identity holds within declared precision for C in {pi, 1}")

    # I4: strict monotonicity of rho (stable gap positive) + A vs C agreement
    mono = all(gap_A(n) > 0 for n in range(3, 100001))
    agree = max(abs(Decimal(repr(rho_A(n))) - rho_C(n)) for n in [3, 7, 96, 1000, 99991])
    record("I4 ratio-monotone-and-crosscheck", mono and agree < Decimal("1e-15"),
           f"gap>0 for all n in [3,100000]; max |float64 - Decimal50| = {agree:.1E}")

    # I5: deficit sandwich (C0.3), float stable on a range + Decimal spot checks
    bad = [n for n in range(3, 200001)
           if not ((PI * PI / (2 * n * n)) * rho_A(2 * n) ** 2 < deficit_A(n) < PI * PI / (2 * n * n))]
    dec_ok = True
    for n in [10 ** 6, 10 ** 9, 10 ** 12]:
        N = Decimal(n)
        d = deficit_C(n)
        lo = (PI_D * PI_D / (2 * N * N)) * rho_C(2 * n) ** 2
        hi = PI_D * PI_D / (2 * N * N)
        if not (lo < d < hi):
            dec_ok = False
    record("I5 deficit-sandwich", not bad and dec_ok,
           f"float64 stable: 0 violations in [3,200000]; Decimal50 holds at n=1e6,1e9,1e12")

    # I6: gap sandwich (C0.4), stable form + Decimal spot checks
    bad = [n for n in range(3, 200001)
           if not (PI * PI * rho_A(n) / (n * (n + 1) ** 2) < gap_A(n) < PI * PI / n ** 3)]
    dec_ok = True
    for n in [14921, 10 ** 6, 10 ** 9]:
        N = Decimal(n)
        g = gap_C(n)
        lo = PI_D * PI_D * rho_C(n) / (N * (N + 1) ** 2)
        hi = PI_D * PI_D / N ** 3
        if not (lo < g < hi):
            dec_ok = False
    record("I6 gap-sandwich", not bad and dec_ok,
           f"float64 stable: 0 violations in [3,200000]; Decimal50 holds at n=14921,1e6,1e9")

    # I6b: the DOCUMENTED representation incident - the naive float64 form
    # cos(pi/(n+1)) - cos(pi/n) must FAIL the same sandwich somewhere
    # (catastrophic cancellation), which is the section-8 incident, not a
    # failure of the theorem. Decimal50 (I6) is the arbiter.
    naive_bad = [n for n in range(3, 200001)
                 if not (PI * PI * rho_A(n) / (n * (n + 1) ** 2)
                         < (math.cos(PI / (n + 1)) - math.cos(PI / n))
                         < PI * PI / n ** 3)]
    record("I6b naive-gap-collapse-documented", len(naive_bad) > 0,
           f"naive cos-difference violates the (true) sandwich {len(naive_bad)} times, "
           f"first at n={naive_bad[0] if naive_bad else None} - observation-layer artifact, "
           "recorded in edge-cases.md")

    # I7: identification guarantee (C0.5a) at worst-case measurements
    ok = True
    for n in [3, 4, 5, 10, 50, 100, 169]:
        guard_r = PI * PI * rho_A(n) / (n * (n + 1) ** 2)
        guard_l = PI * PI * rho_A(n - 1) / ((n - 1) * n * n) if n > 3 else math.inf
        delta = 0.4999 * min(guard_r, guard_l)
        for meas in (rho_A(n) - delta, rho_A(n) + delta):
            if decide(meas) != n:
                ok = False
    record("I7 identification-guarantee", ok,
           "worst-case measurements at +/-delta decided correctly for sampled n, "
           "delta = 0.4999 * min sandwich guard")

    # I8: constructible ambiguity (C0.5b): midpoint within delta of both.
    # The strict margin is delta - g_n/2 ~ delta * (deficit + 2/n): below
    # float64 resolution for large n, so float64 handles n <= 1000 and
    # Decimal50 arbitrates the large cases (margin ~1e-24 at n = 1e5).
    ok = True
    for n in [3, 10, 100, 1000]:
        delta = PI * PI / (2 * n ** 3)
        mid = (rho_A(n) + rho_A(n + 1)) / 2
        if not (abs(mid - rho_A(n)) < delta and abs(mid - rho_A(n + 1)) < delta):
            ok = False
    for n in [100000, 10 ** 7]:
        N = Decimal(n)
        delta = PI_D * PI_D / (2 * N ** 3)
        r1, r2 = rho_C(n), rho_C(n + 1)
        mid = (r1 + r2) / 2
        if not (abs(mid - r1) < delta and abs(mid - r2) < delta):
            ok = False
    record("I8 ambiguity-midpoint", ok,
           "midpoint compatible with n and n+1 when 2*delta = pi^2/n^3; float64 for "
           "n <= 1000, Decimal50 for n in {1e5, 1e7} (strict margin below float64 there)")

    # I9: twilight window (C0.6) for delta in {1e-2, 1e-4, 1e-6}
    ok, windows = True, {}
    for p in [2, 4, 6]:
        delta = 10.0 ** -p
        nlo = math.ceil((PI * PI / (2 * delta)) ** (1.0 / 3.0))
        nhi = math.floor(delta ** -0.5)
        windows[f"1e-{p}"] = [nlo, nhi]
        if nhi - nlo < 1:
            ok = False
        for n in [nlo, (nlo + nhi) // 2, nhi]:
            if not (gap_A(n) / 2 <= delta):            # (a) ambiguity
                ok = False
            if not (rho_A(n) + 2 * delta < 1):         # (b) circle excluded
                ok = False
    if windows.get("1e-6") != [171, 1000]:
        ok = False
    record("I9 twilight-window", ok,
           f"windows: {windows}; both ends verified at edges and midpoint; "
           "delta=1e-6 window is [171,1000] as stated in the chapter")

    # I10: worked-example boundary numbers (delta = 1e-6)
    d6 = 1e-6
    g170_half = gap_A(170) / 2
    guard169 = 2 * d6 < min(PI * PI * rho_A(169) / (169 * 170 ** 2),
                            PI * PI * rho_A(168) / (168 * 169 ** 2))
    guard170 = 2 * d6 < min(PI * PI * rho_A(170) / (170 * 171 ** 2),
                            PI * PI * rho_A(169) / (169 * 170 ** 2))
    amb171 = 2 * d6 >= PI * PI / 171 ** 3
    amb170 = 2 * d6 >= PI * PI / 170 ** 3
    excl1570 = deficit_A(1570) > 2 * d6
    excl1571 = deficit_A(1571) <= 2 * d6
    # INCIDENT (2026-07-28, first run): the chapter's first wording claimed
    # g_170/2 > 1e-6 (n=170 still identifiable). This run measured
    # g_170/2 = 9.956e-7 < 1e-6: n=170 is ALREADY ambiguous by direct
    # computation, though the sandwich bounds are silent about it. Chapter
    # text corrected; incident recorded per the honesty clause.
    ok = (guard169 and not guard170 and not amb170 and g170_half < d6
          and amb171 and excl1570 and excl1571)
    record("I10 worked-example-boundaries", ok,
           f"guarantee holds at 169; bounds silent at 170 but g/2={g170_half:.6e} < 1e-6 "
           "(already ambiguous - first chapter wording refuted here, corrected); "
           "bound-certified ambiguity from 171; circle excluded through 1570, not 1571")

    # I11: float collapse (C0.8): direct form dies at n=3e8, stable survives
    n = 3 * 10 ** 8
    direct = 1.0 - math.cos(PI / n)
    stable = deficit_A(n)
    ref = deficit_C(n)
    rel = abs(Decimal(repr(stable)) - ref) / ref
    ok = direct == 0.0 and stable > 0.0 and rel < Decimal("1e-10")
    record("I11 float-collapse", ok,
           f"n=3e8: 1-cos = {direct!r} (collapsed), 2sin^2 = {stable:.3e}, "
           f"Decimal50 relative agreement {rel:.1E}")

    # adversarial refusals
    refused = []
    for bad_n in [2, 1, 0, -6, 2.5, "12"]:
        try:
            validate_n(bad_n)
            refused.append((bad_n, False))
        except (ValueError, TypeError):
            refused.append((bad_n, True))
    all_refused = all(r for _, r in refused)
    record("I12 domain-refusal", all_refused,
           f"refused: {[b for b, _ in refused]}")

    all_passed = all(c["passed"] for c in checks)
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                            capture_output=True, text=True).stdout.strip()
    report = {
        "chapter": 0,
        "script": "tools/oracle-ch00.py",
        "date": date.today().isoformat(),
        "code_commit": commit,
        "environment": f"python {platform.python_version()}, stdlib only, {sys.platform}",
        "implementations": [
            "A: float64 stable forms (mirrors in-page JS)",
            "B: float64 coordinate geometry + shoelace (no closed trig formulas)",
            "C: Decimal 50-digit Taylor sin/cos (independent arithmetic)",
        ],
        "tested_domain": {
            "dense_n": {"min": 3, "max": 200000},
            "decimal_spot_n": [14921, 10**6, 10**9, 10**12],
            "adversarial_refused": [2, 1, 0, -6, 2.5, "12"],
        },
        "checks": checks,
        "result": "all_passed" if all_passed else "FAILED",
    }
    (AUDIT_DIR / "numeric-check.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"\n{'ALL PASSED' if all_passed else 'FAILURES PRESENT'} -> "
          f"{AUDIT_DIR / 'numeric-check.json'}")
    return 0 if all_passed else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=float, default=None,
                    help="adversarial single-n gate check (must refuse bad n)")
    args = ap.parse_args()
    if args.n is not None:
        n = int(args.n) if float(args.n).is_integer() else args.n
        try:
            validate_n(n)
            print(f"accepted: n={n}")
        except ValueError as e:
            print(e)
            sys.exit(2)
        return
    sys.exit(run_oracle())


if __name__ == "__main__":
    main()
