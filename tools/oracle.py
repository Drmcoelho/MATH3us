#!/usr/bin/env python3
"""Triple oracle for Chapter 1 (A Exaustao) numeric invariants.

MATH3us.md section 1.8: every central numeric result passes three
independent checks:
  1. symbolic derivation  -> audit/symbolic-check.md (hand-written algebra;
     this script cross-validates the recurrences against the closed trig
     forms, which exercises the same half-angle identities numerically)
  2. independent numeric verification -> three implementations compared:
       A. float64 mean recurrences (mirrors the in-page JS)
       B. float64 closed trigonometric forms  a_n = n sin(pi/n), b_n = n tan(pi/n)
       C. 60-digit Decimal mean recurrences (different arithmetic entirely)
  3. edge / degenerate / adversarial cases -> audit/edge-cases.md

Stdlib only. Usage:
  python3 tools/oracle.py            # run full oracle, write artifacts
  python3 tools/oracle.py --n 7      # adversarial: must be refused
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

CHAPTER_DIR = Path(__file__).resolve().parent.parent / "caps" / "01-exaustao"
AUDIT_DIR = CHAPTER_DIR / "audit"
MAX_K = 16          # matches the domain exposed by the in-page experiment
DEEP_K = 40         # Decimal-only continuation, past the float64 plateau
getcontext().prec = 60

# 50 significant digits of pi, independent reference constant.
PI_50 = Decimal("3.1415926535897932384626433832795028841971693993751")


def domain_n(k: int) -> int:
    return 6 * (2 ** k)


def validate_n(n: int) -> int:
    """Adversarial gate: only n = 6 * 2^k, k >= 0, belongs to the chapter's
    domain. Anything else must be refused, not silently accepted."""
    if not isinstance(n, int) or n < 6:
        raise ValueError(f"refused: n={n!r} outside domain (need integer n = 6*2^k)")
    m = n
    while m % 2 == 0 and m > 6:
        m //= 2
    if m != 6 and m != 3:  # 6*2^k halves down to 6 (k>=0); 3 would mean n=3*2^j
        raise ValueError(f"refused: n={n} is not of the form 6*2^k")
    if m == 3:
        raise ValueError(f"refused: n={n} is not of the form 6*2^k")
    return n


# --- implementation A: float64 recurrences (mirror of the page JS) ---------
def seq_float(kmax):
    a, b = 3.0, 2.0 * math.sqrt(3.0)
    out = [(6, a, b)]
    for _ in range(kmax):
        b = 2.0 * a * b / (a + b)
        a = math.sqrt(a * b)
        out.append((out[-1][0] * 2, a, b))
    return out


# --- implementation B: float64 closed trigonometric forms ------------------
def closed_trig(n):
    x = math.pi / n
    return n * math.sin(x), n * math.tan(x)


# --- implementation C: 60-digit Decimal recurrences ------------------------
def seq_decimal(kmax):
    a, b = Decimal(3), Decimal(2) * Decimal(3).sqrt()
    out = [(6, a, b)]
    for _ in range(kmax):
        b = Decimal(2) * a * b / (a + b)
        a = (a * b).sqrt()
        out.append((out[-1][0] * 2, a, b))
    return out


def run_oracle():
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    A = seq_float(MAX_K)
    C = seq_decimal(DEEP_K)
    results = {}
    rows = []

    # I1: A vs B agreement (float recurrence vs float trig closed form)
    worst_ab = 0.0
    for (n, a, b) in A:
        at, bt = closed_trig(n)
        worst_ab = max(worst_ab, abs(a - at), abs(b - bt))
    results["I1_recurrence_vs_trig"] = {
        "tolerance": 5e-15, "worst_abs_diff": worst_ab, "passed": worst_ab < 5e-15}

    # I2: A vs C agreement (float recurrence vs Decimal-60 recurrence)
    worst_ac = 0.0
    for (n, a, b), (n2, ad, bd) in zip(A, C):
        assert n == n2
        worst_ac = max(worst_ac, abs(a - float(ad)), abs(b - float(bd)))
    results["I2_float_vs_decimal"] = {
        "tolerance": 5e-15, "worst_abs_diff": worst_ac, "passed": worst_ac < 5e-15}

    # I3/I4: strict double monotonicity and trapping order (Decimal, k<=MAX_K)
    mono = all(C[i + 1][1] > C[i][1] and C[i + 1][2] < C[i][2] for i in range(MAX_K))
    order = all(a < b for (_, a, b) in C[: MAX_K + 1])
    results["I3_strict_monotonicity"] = {"passed": mono}
    results["I4_trapping_order_a_lt_b"] = {"passed": order}

    # I5: gap halving, strict (Decimal)
    halving = all(
        (C[i + 1][2] - C[i + 1][1]) < (C[i][2] - C[i][1]) / 2 for i in range(MAX_K))
    results["I5_gap_halving"] = {"passed": halving}

    # I6: explicit bound gap <= (2*sqrt(3)-3)/2^k, equality ONLY at k=0,
    # strict for k >= 1. (First statement used < for all k; refuted by this
    # very invariant at k=0 on 2026-07-28 and corrected — see symbolic-check.)
    g0 = Decimal(2) * Decimal(3).sqrt() - Decimal(3)
    eq_at_0 = (C[0][2] - C[0][1]) == g0
    strict_rest = all(
        (C[k][2] - C[k][1]) < g0 / (Decimal(2) ** k) for k in range(1, MAX_K + 1))
    results["I6_explicit_error_bound"] = {
        "equality_at_k0": eq_at_0, "strict_for_k_ge_1": strict_rest,
        "passed": eq_at_0 and strict_rest}

    # I7: the trap contains the independent 50-digit pi at every step
    contains = all(a < PI_50 < b for (_, a, b) in C[: MAX_K + 1])
    results["I7_trap_contains_pi_reference"] = {"passed": contains}

    # I8: conjecture C4 support ONLY (not proof): gap ratio near 1/4 at depth
    ratios = []
    for i in range(1, MAX_K + 1):
        r = (C[i][2] - C[i][1]) / (C[i - 1][2] - C[i - 1][1])
        ratios.append(float(r))
    results["I8_gap_ratio_supports_quarter"] = {
        "final_ratio": ratios[-1],
        "abs_dev_from_0.25": abs(ratios[-1] - 0.25),
        "passed": abs(ratios[-1] - 0.25) < 1e-4,
        "note": ("independent numeric witness for chapter-01.gap-ratio-quarter "
                 "(proved in-chapter on 2026-07-28 via exact factorization, "
                 "symbolic-check S6; originally preregistered as conjecture C4)")}


    # ---- rebuild invariants (D3, preregistration R1-R5) -------------------
    def area_in(a, b): return a * a / b        # Enunciado E
    # I9 (R1): area identities vs closed trig forms (independent route)
    worst = 0.0
    for (n, a, b) in A:
        x = math.pi / n
        worst = max(worst,
                    abs(area_in(a, b) - n * math.sin(x) * math.cos(x)),
                    abs(b - n * math.tan(x)))
    results["I9_area_identities"] = {
        "tolerance": 5e-15, "worst_abs_diff": worst, "passed": worst < 5e-15}

    # I10 (R2): inheritance A-_{2n} = a_n, exact in Decimal-60
    worst_d = Decimal(0)
    for i in range(MAX_K):
        (_, a0, _), (_, a1, b1) = C[i], C[i + 1]
        worst_d = max(worst_d, abs(a1 * a1 / b1 - a0))
    results["I10_area_inherits_semiperimeter"] = {
        "tolerance": "1e-55 (Decimal-60 rounding)",
        "worst_abs_diff": float(worst_d), "passed": worst_d < Decimal("1e-55")}

    # I11 (R3): the double-siege chain, strict links at every step
    chain = True
    for i in range(MAX_K):
        (_, a0, b0), (_, a1, b1) = C[i], C[i + 1]
        Am0 = a0 * a0 / b0
        if not (Am0 < a0 < PI_50 < b1 < b0):
            chain = False
    results["I11_double_siege_chain"] = {"passed": chain}

    # I12 (R4): exact gap identity + ratio -> 2 support at depth
    worst_id = Decimal(0)
    for (_, a, b) in C[: MAX_K + 1]:
        worst_id = max(worst_id, abs((b - a * a / b) - (b - a) * (b + a) / b))
    _, aK, bK = C[MAX_K]
    dev2 = abs((aK + bK) / bK - 2)
    results["I12_gap_identity_and_ratio_two"] = {
        "identity_worst_abs": float(worst_id),
        "ratio_dev_from_2_at_k16": float(dev2),
        "passed": worst_id < Decimal("1e-55") and dev2 < Decimal("1e-9"),
        "note": "ratio -> 2 is a THEOREM in-chapter (section 7.5); this is its independent witness"}

    # I13 (R5): duality constants SUPPORT ONLY (conjecture; door to ch. 10)
    # Deep Decimal row (k = DEEP_K, n ~ 6.6e12) against pi^3/6, pi^3/3, 2pi^3/3.
    nD = Decimal(domain_n(DEEP_K))
    _, aD, bD = C[DEEP_K]
    AmD = aD * aD / bD
    p3 = PI_50 ** 3
    targets = {
        "n2_pi_minus_a": (nD * nD * (PI_50 - aD), p3 / 6),
        "n2_b_minus_pi": (nD * nD * (bD - PI_50), p3 / 3),
        "n2_pi_minus_Ain": (nD * nD * (PI_50 - AmD), 2 * p3 / 3),
        "n2_Aout_minus_pi": (nD * nD * (bD - PI_50), p3 / 3),
    }
    devs = {k: float(abs(v / t - 1)) for k, (v, t) in targets.items()}
    # exact consistency identities (provable already; must hold to Decimal rounding)
    cons1 = abs((PI_50 - aD) + (bD - PI_50) - (bD - aD))
    cons2 = abs((PI_50 - AmD) - ((PI_50 - aD) + aD * (bD - aD) / bD))
    results["I13_duality_constants_support"] = {
        "relative_devs_at_deep_k": devs,
        "consistency_identity_1_abs": float(cons1),
        "consistency_identity_2_abs": float(cons2),
        "passed": max(devs.values()) < 1e-9 and cons1 < Decimal("1e-55") and cons2 < Decimal("1e-55"),
        "note": ("SUPPORT for preregistered conjecture R5, not proof; the four "
                 "individual constants await chapter 10 expansions. The two "
                 "consistency identities are exact algebra, proved in-chapter.")}

    for i, (n, a, b) in enumerate(C[: MAX_K + 1]):
        rows.append({
            "k": i, "n": n,
            "a_n": str(+a), "b_n": str(+b), "gap": str(+(b - a)),
            "gap_ratio": ratios[i - 1] if i >= 1 else None})

    all_passed = all(v["passed"] for v in results.values())
    commit = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
        cwd=CHAPTER_DIR).stdout.strip() or "unknown"

    report = {
        "chapter": 1,
        "script": "tools/oracle.py",
        "code_commit": commit,
        "date": date.today().isoformat(),
        "environment": f"python {platform.python_version()}, stdlib only, {platform.system().lower()}",
        "implementations": {
            "A": "float64 mean recurrences (mirrors in-page JS)",
            "B": "float64 closed trig forms n*sin(pi/n), n*tan(pi/n)",
            "C": "Decimal 60-digit mean recurrences"},
        "tested_domain": {"n": "6 * 2^k", "k_min": 0, "k_max": MAX_K,
                          "decimal_deep_k": DEEP_K},
        "invariants": results,
        "all_passed": all_passed,
        "values": rows,
    }
    (AUDIT_DIR / "numeric-check.json").write_text(
        json.dumps(report, indent=2) + "\n")

    # ---- edge / adversarial cases -> edge-cases.md ------------------------
    edge = []
    # E1: exact base case
    edge.append(("base case exactness",
                 "a_6 == 3 exactly (rational); b_6 == 2*sqrt(3) to 60 digits",
                 C[0][1] == Decimal(3)))
    # E2: minimal k = 0 already traps pi
    edge.append(("minimal domain value k=0",
                 "3 < pi < 2*sqrt(3) holds at the very first step",
                 C[0][1] < PI_50 < C[0][2]))
    # E3: float64 plateau vs Decimal continuation (computational imperfection)
    fdeep = seq_float(DEEP_K)
    fgap_40 = fdeep[DEEP_K][2] - fdeep[DEEP_K][1]
    dgap_40 = C[DEEP_K][2] - C[DEEP_K][1]
    edge.append(("float64 plateau at deep k",
                 f"k=40: float gap = {fgap_40:.3e} (plateaued near machine epsilon), "
                 f"Decimal-60 gap = {dgap_40:.3E} (still contracting by ~1/4). "
                 "Representation-layer artifact (manual section 2.3, computational), "
                 "not a property of the object.",
                 float(dgap_40) < 1e-24 and (fgap_40 == 0.0 or fgap_40 < 1e-15)))
    # E4: degenerate fixed point a == b
    a = b = Decimal(1)
    b2 = Decimal(2) * a * b / (a + b); a2 = (a * b2).sqrt()
    edge.append(("degenerate a=b fixed point",
                 "if a=b the recurrences return a=b unchanged (closed trap stays closed)",
                 a2 == a and b2 == b))
    # E5/E6: invalid inputs refused
    for bad in (7, 100):
        try:
            validate_n(bad)
            edge.append((f"adversarial n={bad}", "was NOT refused", False))
        except ValueError as e:
            edge.append((f"adversarial n={bad}", f"refused with: {e}", True))

    lines = ["# Capítulo 1 — Casos extremos, degenerados e adversariais",
             "",
             f"Gerado por `tools/oracle.py` em {date.today().isoformat()}, "
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
    p.add_argument("--n", type=int, help="validate a single n against the domain")
    args = p.parse_args()
    if args.n is not None:
        validate_n(args.n)      # raises (refuses) on invalid input
        print(f"n={args.n} accepted (n = 6*2^k)")
        return 0
    return run_oracle()


if __name__ == "__main__":
    sys.exit(main())
