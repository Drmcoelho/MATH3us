#!/usr/bin/env python3
"""Triple oracle for Chapter 7 (Complex numbers) numeric invariants.

MATH3us.md section 1.8: every central numeric result passes three
independent checks:
  1. symbolic derivation  -> audit/symbolic-check.md (hand-written algebra
     S1..S12; this script exercises the same identities numerically)
  2. independent numeric verification -> two implementations compared
     wherever a claim is central:
       - field axioms: exact Fraction pairs  vs  2x2 matrix representation
         [[a, -b], [b, a]] (matrix product is an independent multiplication
         route; agreement is structural, not accidental)
       - n-th roots: construction by de Moivre (math.cos/sin)  vs
         verification by ITERATED MULTIPLICATION of the candidate
         (polynomial route), with explicit float error bounds
       - two squares: exhaustive search over ALL primes p < 50000
       - Gaussian primes: norm criterion  vs  brute-force divisor search
  3. edge / degenerate / adversarial cases -> audit/edge-cases.md
     (w = 0 refused/degenerate, division by zero refused, p = 2,
      unit-multiplication invariance, float argument wraparound recorded
      as an observation-layer note)

Also carries independent numeric witnesses for the preregistered
conjectures C1..C5 (conjecturas.md, 2026-07-28).

Stdlib only. Usage:
  python3 caps/07-complexos/oracle.py
"""
import json
import math
import platform
import random
import subprocess
import sys
from datetime import date
from fractions import Fraction
from pathlib import Path

CHAPTER_DIR = Path(__file__).resolve().parent
AUDIT_DIR = CHAPTER_DIR / "audit"
TWO_SQUARES_BOUND = 50000          # exhaustive prime domain
GAUSS_BRUTE_BOUND = 14             # brute-force Gaussian-prime square
ROOT_ERR_BOUND = 1e-9              # float bound for z_k^n - w (|w|<=4, n<=12)
SEED = 20260728


# ---------------------------------------------------------------------------
# exact complex arithmetic over Fraction pairs (implementation A)
def cadd(z, w):
    return (z[0] + w[0], z[1] + w[1])


def cmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def cnorm(z):
    return z[0] * z[0] + z[1] * z[1]


def cinv(z):
    n = cnorm(z)
    if n == 0:
        raise ZeroDivisionError("refused: inverse of 0 does not exist in C")
    return (z[0] / n, -z[1] / n)


# implementation B: the 2x2 matrix representation a+bi -> [[a,-b],[b,a]]
def mat(z):
    a, b = z
    return ((a, -b), (b, a))


def matmul(M, N):
    return (
        (M[0][0] * N[0][0] + M[0][1] * N[1][0], M[0][0] * N[0][1] + M[0][1] * N[1][1]),
        (M[1][0] * N[0][0] + M[1][1] * N[1][0], M[1][0] * N[0][1] + M[1][1] * N[1][1]),
    )


# ---------------------------------------------------------------------------
# exact Gaussian-integer arithmetic
def gdivmod(z, d):
    """Rounding division in Z[i]: z = q*d + r with N(r) <= N(d)/2.
    Exact integer arithmetic throughout (nearest integer via floor)."""
    if d == (0, 0):
        raise ZeroDivisionError("refused: division by 0 in Z[i]")
    n = cnorm(d)
    x = z[0] * d[0] + z[1] * d[1]          # Re(z * conj(d))
    y = z[1] * d[0] - z[0] * d[1]          # Im(z * conj(d))
    def rnd(t):                            # nearest integer to t/n, exact
        return (2 * t + n) // (2 * n)
    q = (rnd(x), rnd(y))
    r = (z[0] - (q[0] * d[0] - q[1] * d[1]), z[1] - (q[0] * d[1] + q[1] * d[0]))
    return q, r


def ggcd(z, w):
    while w != (0, 0):
        _, r = gdivmod(z, w)
        z, w = w, r
    return z


def sieve(bound):
    s = bytearray([1]) * bound
    s[0:2] = b"\x00\x00"
    for i in range(2, int(bound ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return s


def is_gaussian_prime_brute(a, b):
    """Brute-force irreducibility in Z[i]: search a proper divisor."""
    N = a * a + b * b
    if N <= 1:
        return False
    for c in range(0, int(math.isqrt(N)) + 1):
        for d in range(0, int(math.isqrt(N)) + 1):
            n2 = c * c + d * d
            if n2 <= 1 or n2 >= N or N % n2 != 0:
                continue
            # does (c,d) (in some unit-rotation) divide (a,b) exactly?
            for cand in ((c, d), (c, -d), (-c, d), (d, c)):
                if cand == (0, 0):
                    continue
                nn = cnorm(cand)
                x = a * cand[0] + b * cand[1]
                y = b * cand[0] - a * cand[1]
                if x % nn == 0 and y % nn == 0:
                    return False
    return True


def gaussian_prime_criterion(a, b, prime_flags):
    """Theorem 17: off-axis iff N prime; on-axis iff |coord| prime = 3 mod 4."""
    if a == 0 and b == 0:
        return False
    if a == 0 or b == 0:
        q = abs(a + b)
        return q < len(prime_flags) and bool(prime_flags[q]) and q % 4 == 3
    N = a * a + b * b
    return bool(prime_flags[N]) if N < len(prime_flags) else None


def two_squares_all(p):
    """All (a, b), 0 < a <= b, with a^2 + b^2 = p. Exact."""
    out = []
    a = 1
    while 2 * a * a <= p:
        b2 = p - a * a
        b = math.isqrt(b2)
        if b * b == b2:
            out.append((a, b))
        a += 1
    return out


def run_oracle():
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    rng = random.Random(SEED)
    results = {}

    # --- I1: field axioms on exact Fraction samples + matrix route --------
    samples = []
    for _ in range(120):
        z = (Fraction(rng.randint(-50, 50), rng.randint(1, 9)),
             Fraction(rng.randint(-50, 50), rng.randint(1, 9)))
        samples.append(z)
    ok = True
    checked = 0
    for idx in range(0, len(samples) - 2, 3):
        z, w, v = samples[idx], samples[idx + 1], samples[idx + 2]
        # commutativity, associativity, distributivity (exact)
        if cmul(z, w) != cmul(w, z):
            ok = False
        if cmul(cmul(z, w), v) != cmul(z, cmul(w, v)):
            ok = False
        if cmul(z, cadd(w, v)) != cadd(cmul(z, w), cmul(z, v)):
            ok = False
        # identity, i^2 = -1
        if cmul(z, (Fraction(1), Fraction(0))) != z:
            ok = False
        # inverse (exact) when z != 0
        if z != (0, 0) and cmul(z, cinv(z)) != (Fraction(1), Fraction(0)):
            ok = False
        # independent route: matrix representation multiplies identically
        Mzw = matmul(mat(z), mat(w))
        if (Mzw[0][0], Mzw[1][0]) != cmul(z, w):
            ok = False
        checked += 1
    i_sq = cmul((Fraction(0), Fraction(1)), (Fraction(0), Fraction(1)))
    if i_sq != (Fraction(-1), Fraction(0)):
        ok = False
    results["I1_field_axioms_exact_and_matrix_route"] = {
        "passed": ok, "triples_checked": checked}

    # --- I2: norm multiplicativity, exact (Brahmagupta identity) ----------
    ok = True
    for idx in range(0, len(samples) - 1, 2):
        z, w = samples[idx], samples[idx + 1]
        if cnorm(cmul(z, w)) != cnorm(z) * cnorm(w):
            ok = False
    # and over a deterministic integer grid
    for a in range(-8, 9):
        for b in range(-8, 9):
            for (c, d) in ((3, 7), (-5, 2), (1, 1)):
                if (a * c - b * d) ** 2 + (a * d + b * c) ** 2 != (a * a + b * b) * (c * c + d * d):
                    ok = False
    results["I2_norm_multiplicative_exact"] = {"passed": ok}

    # --- I3: product modulus/argument in floats, two routes ---------------
    ok = True
    max_mod_err = 0.0
    max_arg_err = 0.0
    for _ in range(4000):
        z = complex(rng.uniform(-10, 10), rng.uniform(-10, 10))
        w = complex(rng.uniform(-10, 10), rng.uniform(-10, 10))
        if abs(z) < 1e-6 or abs(w) < 1e-6:
            continue
        # route 1: cmath on the product; route 2: math on the factors
        merr = abs(abs(z * w) - math.hypot(z.real, z.imag) * math.hypot(w.real, w.imag))
        max_mod_err = max(max_mod_err, merr)
        if merr > 1e-9 * max(1.0, abs(z * w)):
            ok = False
        s = math.atan2(z.imag, z.real) + math.atan2(w.imag, w.real)
        p = math.atan2((z * w).imag, (z * w).real)
        diff = (s - p) / (2 * math.pi)
        aerr = abs(diff - round(diff))
        max_arg_err = max(max_arg_err, aerr)
        if aerr > 1e-9:
            ok = False
    results["I3_product_modulus_argument_float"] = {
        "passed": ok, "max_modulus_rel_err": max_mod_err,
        "max_argument_winding_err": max_arg_err}

    # --- I4: n-th roots -- de Moivre vs iterated power; count; C3 ---------
    ok = True
    worst = 0.0
    cases = 0
    for (wr, wi) in [(1.0, 0.0), (2.0, 3.0), (-1.0, 0.0), (0.5, -2.0),
                     (-3.0, -3.0), (0.0, 4.0), (1e-3, 0.0)]:
        for n in range(1, 13):
            s = math.hypot(wr, wi)
            phi = math.atan2(wi, wr)
            r = s ** (1.0 / n)
            roots = []
            for k in range(n):
                a = (phi + 2 * math.pi * k) / n
                roots.append(complex(r * math.cos(a), r * math.sin(a)))
            # (a) each root, RAISED BY ITERATED MULTIPLICATION, returns w
            for zk in roots:
                acc = complex(1, 0)
                for _ in range(n):
                    acc *= zk
                err = abs(acc - complex(wr, wi))
                worst = max(worst, err / max(1.0, s))
                if err > ROOT_ERR_BOUND * max(1.0, s):
                    ok = False
            # (b) exactly n distinct (pairwise distance > 0 numerically)
            for a_ in range(n):
                for b_ in range(a_ + 1, n):
                    if abs(roots[a_] - roots[b_]) < 1e-12:
                        ok = False
            # (c) regular polygon: all moduli equal r; consecutive gaps equal
            for zk in roots:
                if abs(abs(zk) - r) > 1e-12 * max(1.0, r):
                    ok = False
            if n >= 3:
                side = abs(roots[1] - roots[0])
                for k in range(n):
                    if abs(abs(roots[(k + 1) % n] - roots[k]) - side) > 1e-9:
                        ok = False
            # (d) C3: sum of the n roots is 0 for n >= 2
            if n >= 2 and abs(sum(roots)) > 1e-9 * max(1.0, r) * n:
                ok = False
            cases += 1
    results["I4_nth_roots_count_polygon_sum_C3"] = {
        "passed": ok, "cases": cases, "worst_rel_power_err": worst}

    # --- I5: branch defect Arg(zw) - Arg z - Arg w in {-2pi, 0, 2pi} (C5) -
    ok = True
    seen = set()
    pairs = 0
    for _ in range(6000):
        z = complex(rng.uniform(-5, 5), rng.uniform(-5, 5))
        w = complex(rng.uniform(-5, 5), rng.uniform(-5, 5))
        if abs(z) < 1e-9 or abs(w) < 1e-9:
            continue
        d = math.atan2(z.imag, z.real) + math.atan2(w.imag, w.real) \
            - math.atan2((z * w).imag, (z * w).real)
        k = round(d / (2 * math.pi))
        if k not in (-1, 0, 1) or abs(d - k * 2 * math.pi) > 1e-9:
            ok = False
        seen.add(k)
        pairs += 1
    # deliberately near the cut (arguments close to pi)
    for eps in (1e-3, 1e-6, 1e-9):
        z = complex(-1.0, eps)
        d = 2 * math.atan2(z.imag, z.real) - math.atan2((z * z).imag, (z * z).real)
        k = round(d / (2 * math.pi))
        if k not in (-1, 0, 1) or abs(d - k * 2 * math.pi) > 1e-9:
            ok = False
        seen.add(k)
    results["I5_branch_defect_C5"] = {
        "passed": ok and seen == {-1, 0, 1},
        "pairs": pairs, "defects_observed_2pi_multiples": sorted(seen)}

    # --- I6: Z[i] division algorithm on random exact samples --------------
    ok = True
    trials = 0
    for _ in range(3000):
        z = (rng.randint(-10**6, 10**6), rng.randint(-10**6, 10**6))
        d = (rng.randint(-10**3, 10**3), rng.randint(-10**3, 10**3))
        if d == (0, 0):
            continue
        q, r = gdivmod(z, d)
        # identity and bound, both EXACT
        if cadd(cmul(q, d), r) != z:
            ok = False
        if 2 * cnorm(r) > cnorm(d):
            ok = False
        trials += 1
    results["I6_gaussian_division_remainder_shrinks"] = {
        "passed": ok, "trials": trials}

    # --- I7: Wilson + quadratic residue witness ---------------------------
    flags = sieve(TWO_SQUARES_BOUND)
    primes = [p for p in range(2, TWO_SQUARES_BOUND) if flags[p]]
    ok = True
    wilson_sample = primes[:60] + [primes[200], primes[1000], primes[-1]]
    for p in wilson_sample:
        f = 1
        for k in range(2, p):
            f = f * k % p
        if f != p - 1:
            ok = False
        if p % 2 == 1:
            m = 1
            for k in range(2, (p - 1) // 2 + 1):
                m = m * k % p
            sq = m * m % p
            if p % 4 == 1 and sq != p - 1:
                ok = False
            if p % 4 == 3 and sq != 1:
                ok = False
    # Wilson is sharp: composites n > 4 give (n-1)! = 0 mod n
    for n in (6, 8, 9, 12, 100):
        f = 1
        for k in range(2, n):
            f = f * k % n
        if f != 0:
            ok = False
    results["I7_wilson_and_qr_witness"] = {
        "passed": ok, "primes_sampled": len(wilson_sample),
        "largest_prime_sampled": wilson_sample[-1]}

    # --- I8: two squares, EXHAUSTIVE p < 50000 + uniqueness (C1) ----------
    ok = True
    n1 = n3 = 0
    for p in primes:
        reps = two_squares_all(p)
        if p == 2:
            if reps != [(1, 1)]:
                ok = False
        elif p % 4 == 1:
            n1 += 1
            if len(reps) != 1:            # existence AND uniqueness (C1)
                ok = False
            else:
                a, b = reps[0]
                if a * a + b * b != p:
                    ok = False
        else:
            n3 += 1
            if reps:                       # provably none
                ok = False
    # C1 contrast: uniqueness fails for a composite
    contrast = two_squares_all(65)
    results["I8_two_squares_exhaustive_and_C1"] = {
        "passed": ok and len(contrast) == 2,
        "primes_tested": len(primes), "p_1_mod_4": n1, "p_3_mod_4": n3,
        "composite_65_reps": contrast}

    # --- I9: C2 -- factorial witness + Gaussian gcd builds the split ------
    ok = True
    tested = []
    for p in [5, 13, 17, 29, 97, 101, 997, 4001, 9973, 49993]:
        assert flags[p] and p % 4 == 1
        m = 1
        for k in range(2, (p - 1) // 2 + 1):
            m = m * k % p
        if m * m % p != p - 1:
            ok = False
        g = ggcd((m, 1), (p, 0))
        if cnorm(g) != p:
            ok = False
        tested.append({"p": p, "gcd": list(g), "norm": cnorm(g)})
    results["I9_wilson_witness_gcd_algorithm_C2"] = {
        "passed": ok, "cases": tested}

    # --- I10: Gaussian prime criterion vs brute force (C4 + Theorem 17) ---
    ok = True
    mismatches = []
    for a in range(-GAUSS_BRUTE_BOUND, GAUSS_BRUTE_BOUND + 1):
        for b in range(-GAUSS_BRUTE_BOUND, GAUSS_BRUTE_BOUND + 1):
            crit = gaussian_prime_criterion(a, b, flags)
            brute = is_gaussian_prime_brute(a, b)
            if crit is None or crit != brute:
                ok = False
                mismatches.append((a, b))
    results["I10_gaussian_primes_criterion_vs_brute_C4"] = {
        "passed": ok, "square_bound": GAUSS_BRUTE_BOUND,
        "mismatches": mismatches[:10]}

    # ---- report ----------------------------------------------------------
    all_passed = all(v["passed"] for v in results.values())
    commit = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"], capture_output=True,
        text=True, cwd=CHAPTER_DIR).stdout.strip() or "unknown"
    report = {
        "chapter": 7,
        "script": "caps/07-complexos/oracle.py",
        "code_commit": commit,
        "date": date.today().isoformat(),
        "environment": f"python {platform.python_version()}, stdlib only, "
                       f"{platform.system().lower()}",
        "seed": SEED,
        "implementations": {
            "A": "exact Fraction pairs (field ops), exact Z[i] ints (division, gcd, sieve, two-squares search)",
            "B": "2x2 matrix representation (field), iterated multiplication (roots), brute-force divisor search (Gaussian primes), math vs cmath (polar)"},
        "tested_domain": {
            "field_fraction_samples": 120,
            "polar_float_pairs": 4000,
            "roots_cases": "7 targets x n in 1..12",
            "branch_pairs": 6000,
            "division_trials": trials,
            "two_squares_primes_below": TWO_SQUARES_BOUND,
            "gauss_brute_square": GAUSS_BRUTE_BOUND,
            "wilson_largest": wilson_sample[-1]},
        "invariants": results,
        "all_passed": all_passed,
    }
    (AUDIT_DIR / "numeric-check.json").write_text(
        json.dumps(report, indent=2) + "\n")

    # ---- edge / adversarial cases -> edge-cases.md ------------------------
    edge = []
    # A1: w = 0 has exactly one n-th root (degenerate, declared)
    only_zero = all(
        abs(z) ** n == 0 or z == 0
        for n in (2, 5) for z in [0j])
    # verify no nonzero z can have z^n = 0: |z^n| = |z|^n > 0
    nz = abs(complex(1e-8, 1e-8) ** 3) > 0
    edge.append(("degenerate w = 0",
                 "z^n = 0 forces z = 0 (|z|^n = 0); explorer announces the "
                 "single collapsed root instead of drawing a polygon",
                 only_zero and nz))
    # A2: division by zero refused in Z[i] and in C
    try:
        gdivmod((3, 2), (0, 0))
        edge.append(("division by 0 in Z[i]", "was NOT refused", False))
    except ZeroDivisionError as e:
        edge.append(("division by 0 in Z[i]", f"refused with: {e}", True))
    try:
        cinv((Fraction(0), Fraction(0)))
        edge.append(("inverse of 0 in C", "was NOT refused", False))
    except ZeroDivisionError as e:
        edge.append(("inverse of 0 in C", f"refused with: {e}", True))
    # A3: p = 2, the ramified special case
    r2 = two_squares_all(2)
    onepi2 = cmul((1, 1), (1, 1))                       # (1+i)^2 = 2i
    ram = cmul((0, -1), onepi2)                          # -i * 2i = 2
    edge.append(("p = 2 special case",
                 f"2 = 1^2 + 1^2 (reps: {r2}); (1+i)^2 = {onepi2}, "
                 f"-i*(1+i)^2 = {ram}",
                 r2 == [(1, 1)] and onepi2 == (0, 2) and ram == (2, 0)))
    # A4: float argument wraparound near the cut (observation layer)
    z = complex(-1.0, 1e-15)
    s2 = 2 * math.atan2(z.imag, z.real)
    p2 = math.atan2((z * z).imag, (z * z).real)
    wrap_ok = abs((s2 - p2) - 2 * math.pi) < 1e-9
    edge.append(("float wraparound at the cut (observation layer)",
                 f"z = -1 + 1e-15 i: Arg z + Arg z = {s2:.15f} lies outside "
                 f"(-pi, pi]; Arg(z^2) = {p2:.2e}; the 2*pi correction is the "
                 "REPRESENTATIVE failing, not the set-law arg(zw) = arg z + "
                 "arg w -- recorded as an observation-layer note (section 10)",
                 wrap_ok))
    # A5: unit-multiplication invariance of Gaussian primality
    ok_units = True
    for (a, b) in [(2, 1), (3, 2), (0, 3), (1, 1), (4, 5)]:
        base = is_gaussian_prime_brute(a, b)
        for u in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ua, ub = cmul((a, b), u)
            if is_gaussian_prime_brute(ua, ub) != base:
                ok_units = False
    edge.append(("unit-multiplication invariance",
                 "associates u*z (u in {1,-1,i,-i}) share primality with z "
                 "(brute-force check on 5 witnesses x 4 units)", ok_units))
    # A6: near-boundary of the exhaustive domain
    p = 49993
    reps = two_squares_all(p)
    edge.append(("largest 1-mod-4 prime checked by hand in text (49993)",
                 f"49993 = 68^2 + 213^2; reps found: {reps}",
                 reps == [(68, 213)]))

    lines = ["# Capítulo 7 — Casos extremos, degenerados e adversariais",
             "",
             f"Gerado por `caps/07-complexos/oracle.py` em "
             f"{date.today().isoformat()}, commit `{commit}`.", ""]
    for name, desc, okc in edge:
        lines.append(f"- **{name}** — {desc} → **{'passou' if okc else 'FALHOU'}**")
    edge_ok = all(okc for _, _, okc in edge)
    lines += ["", f"Resultado global: **{'passou' if edge_ok else 'FALHOU'}**."]
    (AUDIT_DIR / "edge-cases.md").write_text("\n".join(lines) + "\n")

    print(json.dumps({k: v["passed"] for k, v in results.items()}, indent=2))
    print("edge cases:", "passed" if edge_ok else "FAILED")
    print("all:", "PASSED" if (all_passed and edge_ok) else "FAILED")
    return 0 if (all_passed and edge_ok) else 1


if __name__ == "__main__":
    sys.exit(run_oracle())
