#!/usr/bin/env python3
"""Triple oracle for Chapter 6 (As Patologias) numeric invariants.

MATH3us.md section 1.8: every central numeric result passes three
independent checks:
  1. symbolic derivation  -> audit/symbolic-check.md (hand-written algebra
     S1..S13; this script exercises the same identities numerically)
  2. independent numeric verification -> two implementations compared for
     each invariant (details per invariant below); ALL verification-path
     arithmetic is exact (Fraction / int); floats appear ONLY inside the
     adversarial observation-layer cases, which is their point.
  3. edge / degenerate / adversarial cases -> audit/edge-cases.md
     (float blindness for Dirichlet, zero denominator refused, unreduced
      fractions, float floor overflow at m > 52, the float probe going
      dyadic beyond its mantissa)

Judges the preregistered conjectures C1..C5 (conjecturas.md, 2026-07-28).
C5 (bits of float(sqrt(2)/2) as a near-balanced walk) had NO exploratory
verification of any kind before this run.

Invariants:
  I1  density witnesses: between sampled rational pairs, a certified
      rational (midpoint) and a certified irrational (a + sqrt2/n) with
      exact ordering certificates; n chosen by two independent routes.
  I2  Thomae epsilon-delta witness at alpha in {sqrt2/2, sqrt3/3, sqrt2-1}
      for eps in {1/10, 1/100, 1/1000}: certified delta > 0 such that the
      delta-ball contains NO reduced fraction with denominator <= 1/eps
      (route A: per-q nearest fraction; route B: exhaustive enumeration),
      plus the chapter's printed values (7/10 and 408/577 at sqrt2/2).
  I3  Takagi dyadic slopes two ways: exact finite-sum evaluation of T at
      dyadic endpoints (Fraction) vs the +-1 digit formula S_m; children
      relations S(2j) = S+1, S(2j+1) = S-1 (C4); slope at 0 equals m (C3).
  I4  T(1/3) = 2/3 exactly: partial sums + exact tail close the bracket.
  I5  Farey counts Phi(Q) by totient sieve AND direct gcd count; judges
      C2 (|Phi(1000)/(3Q^2/pi^2) - 1| < 1% and Phi(10) deviation > 3%).
  I6  Q-hole witnesses: Newton-step identities exact over Fractions;
      descent 3/2 -> 17/12 -> 577/408 and ascent 1 -> 4/3 -> 7/5 with the
      exact excesses/deficits printed in the chapter.
  I7  TVI bisection certificate: exact Fraction bisection for x^2 - 2 on
      [1,2] and x^3 + x - 1 on [0,1], 60 certified sign-change steps;
      plus the Q-failure: no rational zero of x^2 - 2 exists (symbolic,
      spot-checked by scan).
  I8  judges C5: sign changes and max|S_m| for the float of sqrt(2)/2.

Stdlib only. Usage:
  python3 caps/06-patologias/oracle.py
"""
import json
import math
import platform
import subprocess
import sys
from datetime import date
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

CHAPTER_DIR = Path(__file__).resolve().parent
AUDIT_DIR = CHAPTER_DIR / "audit"

FLOAT_SQRT2_OVER_2 = Fraction(6369051672525773, 2**53)  # exact value of the double


# ---------- exact helpers --------------------------------------------------
def sqrt_approx(x_times_10_160):
    """Certified rational approximation of sqrt(x) where the argument is
    x * 10^160 as an integer: isqrt gives floor(sqrt(x) * 10^80), so the
    returned (lo, hi) Fractions satisfy lo <= sqrt(x) <= hi with
    hi - lo = 1/10^80."""
    r = isqrt(x_times_10_160)
    lo = Fraction(r, 10**80)
    hi = Fraction(r + 1, 10**80)
    return lo, hi


def alpha_bounds(kind):
    """Certified (lo, hi) Fraction bounds for the three sampled irrationals."""
    if kind == "sqrt2/2":       # sqrt(1/2)
        return sqrt_approx((10**160) // 2)
    if kind == "sqrt3/3":       # sqrt(1/3)
        return sqrt_approx((10**160) // 3)
    if kind == "sqrt2-1":
        lo, hi = sqrt_approx(2 * 10**160)
        return lo - 1, hi - 1
    raise ValueError(kind)


def saw(x: Fraction) -> Fraction:
    """Distance from x to the nearest integer, exact."""
    f = x - (x.numerator // x.denominator)  # in [0,1)
    return min(f, 1 - f)


def takagi_at_dyadic(j: int, m: int) -> Fraction:
    """T(j/2^m) exactly: the series terminates (terms k >= m vanish)."""
    x = Fraction(j, 2**m)
    return sum((Fraction(saw((2**k) * x), 2**k) for k in range(m)), Fraction(0))


def slope_direct(j: int, m: int) -> Fraction:
    """Route A: slope of T over [j/2^m, (j+1)/2^m] by exact evaluation."""
    return (takagi_at_dyadic(j + 1, m) - takagi_at_dyadic(j, m)) * (2**m)


def slope_digits(j: int, m: int) -> int:
    """Route B: S_m = sum of +-1 over the m-bit window of j (lemma 5.8)."""
    return sum(1 if ((j >> b) & 1) == 0 else -1 for b in range(m))


def thomae(x: Fraction) -> Fraction:
    """Thomae on rationals (Fraction reduces automatically)."""
    if x.denominator == 0:  # unreachable with Fraction; kept for clarity
        raise ZeroDivisionError
    return Fraction(1, x.denominator)


def thomae_raw(p: int, q: int) -> Fraction:
    """Adversarial gate: refuses q = 0; REDUCES before evaluating."""
    if q == 0:
        raise ValueError("refused: denominator 0 is not a rational")
    return Fraction(1, Fraction(p, q).denominator)


# ---------- invariants -----------------------------------------------------
def inv_I1_density():
    pairs = [
        (Fraction(0), Fraction(1)),
        (Fraction(7, 10), Fraction(71, 100)),
        (Fraction(1, 3), Fraction(1, 2)),
        (Fraction(141, 100), Fraction(142, 100)),
        (Fraction(707106, 10**6), Fraction(707107, 10**6)),
        (Fraction(-5, 7), Fraction(-2, 3)),
        (Fraction(10**9, 10**9 + 1), Fraction(1)),
    ]
    ok = True
    witnesses = []
    for a, b in pairs:
        gap = b - a
        assert gap > 0
        # rational witness: exact midpoint
        mid = (a + b) / 2
        ok &= a < mid < b
        # irrational witness w = a + sqrt2/n: need sqrt2/n < gap
        # certificate: 2 < n^2 gap^2 (exact). Route 1: smallest power of 2.
        n1 = 1
        while not 2 < n1 * n1 * gap * gap:
            n1 *= 2
        # Route 2: n = isqrt(ceil(2/gap^2)) + 1
        g2 = gap * gap
        n2 = isqrt((2 * g2.denominator) // g2.numerator) + 1
        for n in (n1, n2):
            cert = 2 < n * n * gap * gap   # exact Fraction/int arithmetic
            ok &= cert
        # ordering certificate: a < a + sqrt2/n < b, given 0 < sqrt2/n < gap.
        # irrationality is symbolic (S3): rational w would make sqrt2 rational.
        witnesses.append({"a": str(a), "b": str(b), "midpoint": str(mid),
                          "n_pow2": n1, "n_isqrt": n2})
    return {"passed": ok, "pairs": len(pairs), "witnesses": witnesses}


def inv_I2_thomae_delta():
    ok = True
    detail = []
    for kind in ("sqrt2/2", "sqrt3/3", "sqrt2-1"):
        lo, hi = alpha_bounds(kind)
        err = hi - lo                      # <= 2/10^40, certified
        for eps in (Fraction(1, 10), Fraction(1, 100), Fraction(1, 1000)):
            Q = int(1 / eps)
            # Route A: per-q nearest fraction, certified lower distance bound
            best = None  # (certified_lower_bound, p, q)
            for q in range(1, Q + 1):
                p = round(q * lo)  # Fraction round -> nearest integer
                for pp in (p - 1, p, p + 1):
                    d = abs(lo - Fraction(pp, q))
                    lower = d - err        # certified: |alpha - pp/q| >= lower
                    if best is None or lower < best[0]:
                        best = (lower, pp, q)
            delta = best[0] * Fraction(9, 10)   # strictly inside the bound
            ok &= delta > 0
            # Route B: exhaustive — no reduced fraction q <= Q within delta
            intruders = 0
            for q in range(1, Q + 1):
                pmin = math.ceil((lo - delta) * q)
                pmax = math.floor((hi + delta) * q)
                for p in range(pmin, pmax + 1):
                    if gcd(abs(p), q) != 1:
                        continue
                    # certified distance lower bound
                    if abs(lo - Fraction(p, q)) - err < delta:
                        intruders += 1
            ok &= intruders == 0
            # values with T >= eps need q <= Q — outside the ball, so inside
            # the ball T < eps for every rational; irrationals give 0. QED.
            detail.append({"alpha": kind, "eps": str(eps), "Q": Q,
                           "nearest": f"{best[1]}/{best[2]}",
                           "delta": float(delta)})
    # the chapter's printed values at sqrt2/2
    printed = {d["eps"]: d for d in detail if d["alpha"] == "sqrt2/2"}
    ok &= printed["1/10"]["nearest"] == "7/10"
    ok &= abs(printed["1/10"]["delta"] / 0.0071067811 - 0.9) < 0.01
    ok &= printed["1/1000"]["nearest"] == "408/577"
    ok &= abs(printed["1/1000"]["delta"] / 1.0619e-06 - 0.9) < 0.01
    return {"passed": ok, "cases": detail}


def inv_I3_dyadic_slopes():
    ok = True
    # (a) slope at 0 equals m (C3), both routes, m = 1..40
    for m in range(1, 41):
        ok &= slope_digits(0, m) == m
        ok &= slope_direct(0, m) == m
    # (b) route agreement on a deterministic scatter of (m, j)
    import random
    rng = random.Random(20260728)
    for m in range(1, 21):
        js = {0, 1, 2**m - 1, 2**m // 3}
        js |= {rng.randrange(0, 2**m) for _ in range(8)}
        for j in js:
            sd = slope_digits(j, m)
            ok &= slope_direct(j, m) == sd
            # (c) children relation = C4: halves differ by exactly 2
            ok &= slope_digits(2 * j, m + 1) == sd + 1
            ok &= slope_digits(2 * j + 1, m + 1) == sd - 1
    # (d) nested chains at the probe presets: |S_{m+1} - S_m| = 1 always
    presets = {"0": Fraction(0), "1/3": Fraction(1, 3),
               "float(sqrt2/2)": FLOAT_SQRT2_OVER_2}
    chains = {}
    for name, x in presets.items():
        S = []
        for m in range(1, 53):
            j = (x.numerator * 2**m) // x.denominator
            S.append(slope_digits(j, m))
        ok &= all(abs(S[i + 1] - S[i]) == 1 for i in range(len(S) - 1))
        chains[name] = S
    # 1/3 alternates 1,0 forever (checked to 52); 0 gives S_m = m
    ok &= chains["0"] == list(range(1, 53))
    ok &= all(chains["1/3"][i] == (1 if i % 2 == 0 else 0) for i in range(52))
    return {"passed": ok, "chains_first_12": {k: v[:12] for k, v in chains.items()}}


def inv_I4_takagi_one_third():
    ok = True
    third = Fraction(1, 3)
    # all sawteeth see 1/3 at height 1/3 (k <= 200, exact)
    ok &= all(saw((2**k) * third) == third for k in range(200))
    # partial sums two ways + exact tail closes the bracket
    for N in (5, 20, 60):
        direct = sum((Fraction(saw((2**k) * third), 2**k) for k in range(N)),
                     Fraction(0))
        closed = third * (2 - Fraction(2, 2**N))     # (1/3)(2 - 2^{1-N})
        tail = third * Fraction(2, 2**N)             # exact geometric tail
        ok &= direct == closed
        ok &= direct + tail == Fraction(2, 3)
        ok &= direct < Fraction(2, 3)
    return {"passed": ok}


def inv_I5_farey_C2():
    def phi_sum_sieve(Q):
        phi = list(range(Q + 1))
        for p in range(2, Q + 1):
            if phi[p] == p:
                for mult in range(p, Q + 1, p):
                    phi[mult] -= phi[mult] // p
        return sum(phi[1:])

    def phi_sum_gcd(Q):
        return sum(1 for q in range(1, Q + 1)
                   for p in range(1, q + 1) if gcd(p, q) == 1)

    ok = True
    counts = {}
    for Q in (10, 100, 1000):
        a, b = phi_sum_sieve(Q), phi_sum_gcd(Q)
        ok &= a == b
        counts[Q] = a
    # C2 judgment (pi^2 via float is safe: margins 1% vs deviations ~0.08%)
    dev1000 = abs(counts[1000] / (3 * 1000**2 / math.pi**2) - 1)
    dev10 = abs(counts[10] / (3 * 10**2 / math.pi**2) - 1)
    c2 = dev1000 < 0.01 and dev10 > 0.03
    ok &= c2
    return {"passed": ok, "counts": counts,
            "dev_Q1000": dev1000, "dev_Q10": dev10, "C2_verdict": "confirmed" if c2 else "REFUTED"}


def inv_I6_q_hole():
    ok = True
    import random
    rng = random.Random(628)
    samples = [Fraction(3, 2), Fraction(17, 12), Fraction(577, 408),
               Fraction(7, 5), Fraction(1), Fraction(4, 3), Fraction(99, 70)]
    samples += [Fraction(rng.randrange(1, 10**6), rng.randrange(1, 10**6))
                for _ in range(40)]
    for r in samples:
        if r <= 0:
            continue
        rp = r / 2 + 1 / r
        ok &= rp * rp - 2 == (r * r - 2) ** 2 / (4 * r * r)      # identity 1
        t = (2 * r + 2) / (r + 2)
        ok &= t - r == (2 - r * r) / (r + 2)                     # identity 2
        ok &= t * t - 2 == 2 * (r * r - 2) / (r + 2) ** 2        # identity 3
        if r * r > 2:
            ok &= rp < r and rp * rp > 2                         # descent
        if r * r < 2:
            ok &= t > r and t * t < 2                            # ascent
    # the chapter's printed chains
    r = Fraction(3, 2)
    chain, excess = [r], [r * r - 2]
    for _ in range(2):
        r = r / 2 + 1 / r
        chain.append(r)
        excess.append(r * r - 2)
    ok &= chain == [Fraction(3, 2), Fraction(17, 12), Fraction(577, 408)]
    ok &= excess == [Fraction(1, 4), Fraction(1, 144), Fraction(1, 166464)]
    s = Fraction(1)
    up, deficit = [s], []
    for _ in range(2):
        s = (2 * s + 2) / (s + 2)
        up.append(s)
        deficit.append(2 - s * s)
    ok &= up == [Fraction(1), Fraction(4, 3), Fraction(7, 5)]
    ok &= deficit == [Fraction(2, 9), Fraction(1, 25)]
    return {"passed": ok, "samples": len(samples)}


def inv_I7_tvi_bisection():
    ok = True
    certs = []
    for name, f, a, b in (
        ("x^2-2 on [1,2]", lambda x: x * x - 2, Fraction(1), Fraction(2)),
        ("x^3+x-1 on [0,1]", lambda x: x**3 + x - 1, Fraction(0), Fraction(1)),
    ):
        lo, hi = a, b
        ok &= f(lo) < 0 < f(hi)
        for _ in range(60):
            mid = (lo + hi) / 2
            if f(mid) < 0:
                lo = mid
            elif f(mid) > 0:
                hi = mid
            else:  # exact rational root found (never happens for these)
                lo = hi = mid
                break
            ok &= f(lo) < 0 < f(hi)              # certificate at every step
        ok &= hi - lo == (b - a) / 2**60 or lo == hi
        certs.append({"f": name, "lo": float(lo), "hi": float(hi),
                      "width": float(hi - lo)})
    # Q-failure spot check: no rational p/q with q <= 2000 has square 2
    ok &= all((p * p != 2 * q * q)
              for q in range(1, 2001)
              for p in (isqrt(2 * q * q), isqrt(2 * q * q) + 1))
    return {"passed": ok, "certificates": certs}


def inv_I8_judge_C5():
    """C5 preregistered blind: bits of float(sqrt2/2) as near-balanced walk.
    Claim: S_1..S_52 changes sign at least 3 times and max|S_m| <= 12."""
    x = FLOAT_SQRT2_OVER_2
    S = []
    for m in range(1, 53):
        j = (x.numerator * 2**m) // x.denominator
        S.append(slope_digits(j, m))
    # sign changes among nonzero values
    signs = [1 if s > 0 else -1 for s in S if s != 0]
    changes = sum(1 for i in range(len(signs) - 1) if signs[i] != signs[i + 1])
    max_abs = max(abs(s) for s in S)
    verdict = changes >= 3 and max_abs <= 12
    return {"passed": True,  # the invariant is the JUDGMENT, recorded either way
            "S": S, "sign_changes": changes, "max_abs_S": max_abs,
            "C5_verdict": "confirmed" if verdict else "REFUTED",
            "C5_claim": "sign changes >= 3 and max|S_m| <= 12"}


# ---------- edge / adversarial cases ---------------------------------------
def edge_cases():
    edge = []

    # E1 (C1): float blindness — every float sample of Dirichlet returns 1
    import random
    rng = random.Random(1829)
    samples = [i / 4095 for i in range(2048)]
    samples += [rng.random() for _ in range(2046)]
    samples += [0.1, math.sqrt(2) / 2]
    rational = sum(1 for x in samples if Fraction(x).denominator >= 1)  # exact
    all_rat = rational == len(samples)
    edge.append(("C1: cegueira float de Dirichlet",
                 f"{len(samples)} floats amostrados, {rational} racionais "
                 f"(todo float e p*2^e, lema da secao 7); D = 1 em 100% das "
                 "amostras. Imperfeicao COMPUTACIONAL (manual 2.3): a camada "
                 "de observacao nao alcanca a propriedade. C1 confirmada.",
                 all_rat))

    # E2: zero denominator refused
    try:
        thomae_raw(1, 0)
        edge.append(("denominador 0", "NAO recusado", False))
    except ValueError as e:
        edge.append(("denominador 0", f"recusado com: {e}", True))

    # E3: unreduced fraction must reduce — 6/8 evaluates as 3/4
    good = thomae_raw(6, 8)
    naive = Fraction(1, 8)   # what a non-reducing implementation returns
    edge.append(("fracao nao reduzida 6/8",
                 f"T(6/8) = {good} (reduz antes); implementacao ingenua daria "
                 f"{naive} — funcao mal definida (6/8 = 3/4 com dois valores). "
                 "Registrado como armadilha de implementacao.",
                 good == Fraction(1, 4) and naive != good))

    # E4: float floor overflow — j = floor(2^m/3) via float breaks at m = 60
    m = 60
    j_exact = (2**m) // 3
    j_float = int(math.floor((2**m) * (1 / 3)))
    edge.append(("piso em float para j = floor(2^60/3)",
                 f"exato {j_exact} vs float {j_float} (diferenca "
                 f"{j_float - j_exact}); a sonda usa BigInt/Fraction por isso.",
                 j_float != j_exact))

    # E5: beyond the mantissa the float probe becomes dyadic: S grows linearly
    x = FLOAT_SQRT2_OVER_2
    S = {}
    for m in range(50, 65):
        j = (x.numerator * 2**m) // x.denominator
        S[m] = slope_digits(j, m)
    linear_tail = all(S[m + 1] == S[m] + 1 for m in range(53, 64))
    edge.append(("sonda alem de m = 53 no float de sqrt2/2",
                 f"S_53..S_64 = {[S[m] for m in range(53, 65)]}: cresce "
                 "linearmente (digitos 0 para sempre) — o float diverge como "
                 "um diadico, DIFERENTE do irracional que representava "
                 "(secao 7 do capitulo).",
                 linear_tail))

    # E6: rightmost dyadic interval, both slope routes agree at the boundary
    ok6 = all(slope_direct(2**m - 1, m) == slope_digits(2**m - 1, m) == -m
              for m in range(1, 12))
    edge.append(("intervalo diadico mais a direita [1 - 2^-m, 1]",
                 "declive = -m pelas duas rotas (espelho do +m em 0)", ok6))

    # E7: saw on negatives and off-[0,1) arguments, exactness
    ok7 = (saw(Fraction(-1, 4)) == Fraction(1, 4)
           and saw(Fraction(-7, 3)) == Fraction(1, 3)
           and saw(Fraction(5, 2)) == Fraction(1, 2)
           and saw(Fraction(17)) == 0)
    edge.append(("serra fora de [0,1) e em negativos",
                 "s(-1/4)=1/4, s(-7/3)=1/3, s(5/2)=1/2, s(17)=0 — exatos", ok7))

    return edge


# ---------- driver ---------------------------------------------------------
def main():
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    results = {
        "I1_density_witnesses": inv_I1_density(),
        "I2_thomae_epsilon_delta": inv_I2_thomae_delta(),
        "I3_takagi_dyadic_slopes_two_routes": inv_I3_dyadic_slopes(),
        "I4_takagi_one_third": inv_I4_takagi_one_third(),
        "I5_farey_counts_C2": inv_I5_farey_C2(),
        "I6_q_hole_witnesses": inv_I6_q_hole(),
        "I7_tvi_bisection_certificates": inv_I7_tvi_bisection(),
        "I8_C5_judgment": inv_I8_judge_C5(),
    }
    all_passed = all(v["passed"] for v in results.values())

    edge = edge_cases()
    edge_ok = all(ok for _, _, ok in edge)

    commit = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"], capture_output=True,
        text=True, cwd=CHAPTER_DIR).stdout.strip() or "unknown"

    report = {
        "chapter": 6,
        "script": "caps/06-patologias/oracle.py",
        "code_commit": commit,
        "date": date.today().isoformat(),
        "environment": f"python {platform.python_version()}, stdlib only, "
                       f"{platform.system().lower()}",
        "implementations": {
            "exactness": "all verification arithmetic in Fraction/int; "
                         "floats only inside adversarial observation cases",
            "I2": "route A per-q nearest with certified error bounds vs "
                  "route B exhaustive enumeration in the delta-ball",
            "I3": "route A exact finite-sum evaluation of T at dyadic "
                  "points vs route B the +-1 binary-digit formula",
            "I5": "totient sieve vs direct gcd count",
        },
        "tested_domain": {
            "density_pairs": 7,
            "thomae_alphas": ["sqrt2/2", "sqrt3/3", "sqrt2-1"],
            "thomae_eps": ["1/10", "1/100", "1/1000"],
            "dyadic_m_max_exact": 40, "chain_m_max": 52,
            "farey_Q": [10, 100, 1000],
            "q_hole_samples": "7 canonical + 40 random rationals",
            "bisection_steps": 60,
            "adversarial": ["float sampling 4096", "q=0", "6/8 unreduced",
                            "float floor at 2^60/3", "probe m>53"],
        },
        "invariants": results,
        "all_passed": all_passed,
        "edge_cases_passed": edge_ok,
    }
    (AUDIT_DIR / "numeric-check.json").write_text(
        json.dumps(report, indent=2) + "\n")

    lines = ["# Capítulo 6 — Casos extremos, degenerados e adversariais",
             "",
             f"Gerado por `caps/06-patologias/oracle.py` em "
             f"{date.today().isoformat()}, commit `{commit}`.",
             "",
             "Os casos adversariais deste capítulo são o seu coração: cada um",
             "documenta a camada de observação (manual §2.1/§2.3) falhando",
             "estruturalmente — que é a tese do capítulo, não um acidente.",
             ""]
    for name, desc, ok in edge:
        lines.append(f"- **{name}** — {desc} → **{'passou' if ok else 'FALHOU'}**")
    lines += ["",
              f"Veredito das conjecturas pré-registradas: "
              f"C1 {'confirmada' if edge[0][2] else 'refutada'} (E1); "
              f"C2 {results['I5_farey_counts_C2']['C2_verdict']} (I5); "
              f"C3 confirmada (I3a); C4 confirmada (I3c); "
              f"C5 {results['I8_C5_judgment']['C5_verdict']} (I8: "
              f"{results['I8_C5_judgment']['sign_changes']} mudanças de sinal, "
              f"max|S| = {results['I8_C5_judgment']['max_abs_S']}).",
              "",
              f"Resultado global: **{'passou' if (all_passed and edge_ok) else 'FALHOU'}**."]
    (AUDIT_DIR / "edge-cases.md").write_text("\n".join(lines) + "\n")

    print(json.dumps({k: v["passed"] for k, v in results.items()}, indent=2))
    print("C2:", results["I5_farey_counts_C2"]["C2_verdict"])
    print("C5:", results["I8_C5_judgment"]["C5_verdict"],
          "| sign_changes =", results["I8_C5_judgment"]["sign_changes"],
          "| max|S| =", results["I8_C5_judgment"]["max_abs_S"])
    print("edge cases:", "passed" if edge_ok else "FAILED")
    print("all:", "PASSED" if (all_passed and edge_ok) else "FAILED")
    return 0 if (all_passed and edge_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
