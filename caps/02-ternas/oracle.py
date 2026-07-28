#!/usr/bin/env python3
"""Triple oracle for Chapter 2 (As Ternas do Impar) numeric invariants.

MATH3us.md section 1.8: every central numeric result passes three
independent checks:
  1. symbolic derivation  -> audit/symbolic-check.md (hand-written algebra
     S1..S7; this script exercises the same identities numerically)
  2. independent numeric verification -> two implementations compared:
       A. direct family formulas  L = (n^2-1)/2, R = (n^2+1)/2 and the
          derived measures (P, s, K, r, r_n) by their closed forms
       B. Euclid reconstruction   u = (n+1)/2, v = (n-1)/2, triple
          rebuilt as (u^2-v^2, 2uv, u^2+v^2); s rebuilt by literal
          summation 1+2+...+n; K rebuilt as leg*leg/2; radii rebuilt
          from K/s and K/(s-n)
     All arithmetic is exact Python bignum -- no floats anywhere in the
     verification path (see edge case E5 for why that matters).
  3. edge / degenerate / adversarial cases -> audit/edge-cases.md
     (even n refused, n = 1 degenerate refused, negatives refused,
      huge n = 10^6 + 1 exact)

Also carries independent numeric witnesses for the preregistered
conjectures C1..C5 (conjecturas.md, 2026-07-28).

Stdlib only. Usage:
  python3 caps/02-ternas/oracle.py          # full oracle, writes artifacts
  python3 caps/02-ternas/oracle.py --n 9    # validate one n (refuses evens)
"""
import argparse
import json
import math
import platform
import subprocess
import sys
from datetime import date
from pathlib import Path

CHAPTER_DIR = Path(__file__).resolve().parent
AUDIT_DIR = CHAPTER_DIR / "audit"
N_MIN, N_MAX, STEP = 3, 20001, 2      # canonical numeric domain (odd n)
HUGE_N = 10**6 + 1                    # exact bignum edge case
EUCLID_SCAN_U = 60                    # C5 general right-triangle scan bound
DIFF2_SCAN_M = 2000                   # C3 mirror-family scan bound


def validate_n(n):
    """Adversarial gate: only odd integers n >= 3 belong to the family.
    Everything else must be refused, not silently accepted."""
    if not isinstance(n, int):
        raise ValueError(f"refused: n={n!r} is not an integer")
    if n % 2 == 0:
        raise ValueError(
            f"refused: n={n} is even -- L=(n^2-1)/2={(n*n-1)/2} and "
            f"R=(n^2+1)/2={(n*n+1)/2} are not integers (lemma 5.4)")
    if n < 3:
        raise ValueError(
            f"refused: n={n} < 3 -- n=1 degenerates (L=0, no triangle); "
            f"negatives and zero are outside the family's domain")
    return n


# --- implementation A: direct closed formulas ------------------------------
def family_direct(n):
    L = (n * n - 1) // 2
    R = (n * n + 1) // 2
    return {
        "n": n, "L": L, "R": R,
        "P": n * (n + 1),
        "s": n * (n + 1) // 2,
        "K": n * (n * n - 1) // 4,
        "r": (n - 1) // 2,
        "rn": (n + 1) // 2,
    }


# --- implementation B: Euclid reconstruction (independent path) ------------
def family_euclid(n):
    u, v = (n + 1) // 2, (n - 1) // 2
    a, b, c = u * u - v * v, 2 * u * v, u * u + v * v   # Euclid triple
    P = a + b + c
    s2, rem = divmod(P, 2)
    assert rem == 0
    K2, rem2 = divmod(a * b, 2)
    assert rem2 == 0
    return {"n": a, "L": b, "R": c, "P": P, "s": s2, "K": K2,
            "r": K2 // s2, "rn": K2 // (s2 - a),
            "r_exact": K2 % s2 == 0, "rn_exact": K2 % (s2 - a) == 0,
            "u": u, "v": v}


def run_oracle():
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    results = {}
    dom = range(N_MIN, N_MAX + 1, STEP)

    ok1 = ok2 = ok3 = ok4 = ok5 = ok6 = ok7 = ok8 = True
    prev_L = prev_dL = None
    sum_check_hits = 0
    for n in dom:
        A = family_direct(n)
        L, R = A["L"], A["R"]

        # I1: contract item 1 -- Pythagoras exact, gap exactly 1, L > n
        if not (n * n + L * L == R * R and R - L == 1 and L > n):
            ok1 = False

        # I2: independent Euclid reconstruction matches implementation A
        B = family_euclid(n)
        if not (B["r_exact"] and B["rn_exact"] and
                all(A[k] == B[k] for k in ("n", "L", "R", "P", "s", "K", "r", "rn")) and
                B["u"] - B["v"] == 1 and math.gcd(B["u"], B["v"]) == 1 and
                (B["u"] + B["v"]) % 2 == 1):
            ok2 = False

        # I3: contract item 3 + conjecture C1 -- pairwise coprime
        if not (math.gcd(n, L) == 1 and math.gcd(n, R) == 1
                and math.gcd(L, R) == 1):
            ok3 = False

        # I4: contract item 4 -- modular structure
        if not (n * n % 8 == 1 and L % 4 == 0 and R % 4 == 1):
            ok4 = False

        # I5: contract item 5 + conjecture C4 -- measures
        #     s checked BOTH by formula and by literal summation
        s_by_sum = sum(range(1, n + 1))
        if s_by_sum == A["s"]:
            sum_check_hits += 1
        four_K = n * (n * n - 1)
        if not (A["P"] == n * (n + 1) == n + L + R
                and A["s"] * 2 == A["P"] and s_by_sum == A["s"]
                and four_K % 4 == 0 and A["K"] == four_K // 4
                and A["K"] % 2 == 0 and A["K"] % 6 == 0
                and A["K"] * 2 == n * L):
            ok5 = False

        # I6: contract item 6 -- radii, with the exact area identities
        r, rn = A["r"], A["rn"]
        if not (2 * r == n - 1 and 2 * rn == n + 1 and rn - r == 1
                and A["K"] == r * A["s"] and A["K"] == rn * (A["s"] - n)
                and 2 * r == n + L - R):
            ok6 = False

        # I7: exradii + conjecture C5 inside the family:
        #     s-L = (n+1)/2, s-R = (n-1)/2, r_R = s, r_L = s - n,
        #     and the four-radii identity r_n + r_L + r_R = r + 2R
        sL, sR = A["s"] - L, A["s"] - R
        if not (2 * sL == n + 1 and 2 * sR == n - 1
                and A["K"] % sL == 0 and A["K"] % sR == 0
                and A["K"] // sR == A["s"] and A["K"] // sL == A["s"] - n
                and rn + A["K"] // sL + A["K"] // sR == r + 2 * R):
            ok7 = False

        # I8: conjecture C2 -- second differences constant 4
        if prev_L is not None:
            dL = L - prev_L
            if dL != 2 * (n - 2 + 1):        # L(n) - L(n-2) = 2(n-1)
                ok8 = False
            if prev_dL is not None and dL - prev_dL != 4:
                ok8 = False
            prev_dL = dL
        prev_L = L

    n_count = len(dom)
    results["I1_pythagoras_gap_one"] = {"passed": ok1}
    results["I2_euclid_reconstruction_independent"] = {"passed": ok2}
    results["I3_pairwise_coprimality_C1"] = {"passed": ok3}
    results["I4_modular_structure_mod8_mod4"] = {"passed": ok4}
    results["I5_measures_P_s_K_C4"] = {
        "passed": ok5 and sum_check_hits == n_count,
        "s_by_literal_summation_hits": sum_check_hits, "expected": n_count}
    results["I6_radii_identities"] = {"passed": ok6}
    results["I7_exradii_and_C5_in_family"] = {"passed": ok7}
    results["I8_second_differences_C2"] = {"passed": ok8}

    # I9: conjecture C5 general -- K == s(s-c) for EVERY Euclid right
    #     triangle (u > v >= 1, coprime, opposite parity), not just u-v=1
    ok9, scanned = True, 0
    for u in range(2, EUCLID_SCAN_U + 1):
        for v in range(1, u):
            if math.gcd(u, v) != 1 or (u + v) % 2 == 0:
                continue
            a, b, c = u * u - v * v, 2 * u * v, u * u + v * v
            s2 = (a + b + c) // 2
            K2 = a * b // 2
            if K2 != s2 * (s2 - c):
                ok9 = False
            scanned += 1
    results["I9_C5_general_right_triangles"] = {
        "passed": ok9, "triangles_scanned": scanned}

    # I10: conjecture C3 -- gap-2 mirror family (2m, m^2-1, m^2+1):
    #      always a triple; primitive iff m even
    ok10 = True
    for m in range(2, DIFF2_SCAN_M + 1):
        a, b, c = 2 * m, m * m - 1, m * m + 1
        g = math.gcd(math.gcd(a, b), c)
        if a * a + b * b != c * c or (g == 1) != (m % 2 == 0):
            ok10 = False
    results["I10_diff2_family_C3"] = {
        "passed": ok10, "m_scanned": DIFF2_SCAN_M - 1}

    sample_rows = []
    for n in [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 1001, 20001]:
        A = family_direct(n)
        sample_rows.append(A)

    all_passed = all(v["passed"] for v in results.values())
    commit = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"], capture_output=True,
        text=True, cwd=CHAPTER_DIR).stdout.strip() or "unknown"

    report = {
        "chapter": 2,
        "script": "caps/02-ternas/oracle.py",
        "code_commit": commit,
        "date": date.today().isoformat(),
        "environment": f"python {platform.python_version()}, stdlib only, "
                       f"{platform.system().lower()}",
        "implementations": {
            "A": "direct closed formulas (exact ints): L, R, P, s, K, r, r_n",
            "B": "Euclid reconstruction u=(n+1)/2, v=(n-1)/2 -> "
                 "(u^2-v^2, 2uv, u^2+v^2); s by literal summation; "
                 "radii from K/s and K/(s-n)"},
        "tested_domain": {
            "odd_n": {"min": N_MIN, "max": N_MAX, "step": STEP},
            "adversarial_even": [2, 4, 100],
            "degenerate": [1, 0, -5],
            "huge_exact": HUGE_N,
            "euclid_scan_u_max": EUCLID_SCAN_U,
            "diff2_scan_m_max": DIFF2_SCAN_M},
        "invariants": results,
        "all_passed": all_passed,
        "sample_values": sample_rows,
    }
    (AUDIT_DIR / "numeric-check.json").write_text(
        json.dumps(report, indent=2) + "\n")

    # ---- edge / adversarial cases -> edge-cases.md ------------------------
    edge = []
    # E1: adversarial evens must be refused, with the non-integer witness
    for bad in (2, 4, 100):
        try:
            validate_n(bad)
            edge.append((f"adversarial even n={bad}", "was NOT refused", False))
        except ValueError as e:
            halves_ok = (bad * bad - 1) % 2 == 1 and (bad * bad + 1) % 2 == 1
            edge.append((f"adversarial even n={bad}",
                         f"refused with: {e} (n^2±1 odd: {halves_ok})",
                         halves_ok))
    # E2: degenerate n=1 refused (L would be 0 -- no triangle)
    for bad in (1, 0, -5):
        try:
            validate_n(bad)
            edge.append((f"degenerate/invalid n={bad}", "was NOT refused", False))
        except ValueError as e:
            edge.append((f"degenerate/invalid n={bad}", f"refused with: {e}", True))
    # E3: smallest member n=3 is exactly (3,4,5) with all measures
    A3 = family_direct(3)
    edge.append(("smallest member n=3",
                 f"(3, {A3['L']}, {A3['R']}); P={A3['P']}, s={A3['s']}, "
                 f"K={A3['K']}, r={A3['r']}, r_n={A3['rn']}",
                 (A3["L"], A3["R"], A3["P"], A3["s"], A3["K"], A3["r"],
                  A3["rn"]) == (4, 5, 12, 6, 6, 1, 2)))
    # E4: huge n = 10^6 + 1, fully exact in bignum arithmetic
    n = HUGE_N
    A = family_direct(n)
    B = family_euclid(n)
    huge_ok = (n * n + A["L"] ** 2 == A["R"] ** 2 and A["R"] - A["L"] == 1
               and all(A[k] == B[k] for k in ("n", "L", "R", "P", "s", "K",
                                              "r", "rn"))
               and math.gcd(n, A["L"]) == 1 and n * n % 8 == 1
               and A["L"] % 4 == 0 and A["R"] % 4 == 1
               and A["K"] % 6 == 0 and A["rn"] - A["r"] == 1)
    edge.append((f"huge n = 10^6 + 1 exact",
                 f"L={A['L']}, R={A['R']}; all invariants exact in bignum",
                 huge_ok))
    # E5: the float64 trap -- the same test in floats REFUTES a true theorem
    fn, fL, fR = float(n), float(A["L"]), float(A["R"])
    float_test = fn * fn + fL * fL - fR * fR
    edge.append(("float64 observation-layer trap at n = 10^6 + 1",
                 f"exact test = 0; float64 test = {float_test:.1f} "
                 f"(L^2 = {A['L']**2} > 2^53 = {2**53}). The observation "
                 "layer would refute a true identity -- manual section 2.3, "
                 "computational imperfection; the oracle therefore uses "
                 "exact integers only.",
                 float_test != 0.0 and n * n + A["L"]**2 - A["R"]**2 == 0))
    # E6: near-domain boundary: n=3 accepted, n=2 refused, n=1 refused
    try:
        validate_n(3)
        b_ok = True
    except ValueError:
        b_ok = False
    edge.append(("boundary acceptance n=3", "accepted as smallest member", b_ok))

    lines = ["# Capítulo 2 — Casos extremos, degenerados e adversariais",
             "",
             f"Gerado por `caps/02-ternas/oracle.py` em "
             f"{date.today().isoformat()}, commit `{commit}`.", ""]
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
        print(f"n={args.n} accepted (odd, >= 3)")
        return 0
    return run_oracle()


if __name__ == "__main__":
    sys.exit(main())
