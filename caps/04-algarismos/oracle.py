#!/usr/bin/env python3
"""Triple oracle for Chapter 4 (Os Algarismos Repetidos) numeric invariants.

MATH3us.md section 1.8: every central numeric result passes three
independent checks:
  1. symbolic derivation  -> audit/symbolic-check.md (hand-written algebra:
     both directions of the termination criterion, the digit/remainder
     periodicity lemma, period = multiplicative order, the d = d_b * d'
     split, the cyclic-permutation theorem)
  2. independent numeric verification -> TWO independent implementations:
       A. long-division state machine, digit by digit, detecting
          pre-period/period by first remainder repetition (observation leg;
          mirrors the in-page JS)
       B. theory prediction: pre-period = max_p ceil(v_p(d)/v_p(b)) over
          primes p | gcd-part, period = multiplicative order of b modulo
          the coprime part d' (order via successive powers; factorization
          via trial division) -- no division is ever simulated here
     compared over ALL reduced a/d with d <= 2000, bases {2,3,7,10,12,16,60},
     numerators a = 1 and the smallest nontrivial coprime a.
  3. edge / degenerate / adversarial cases -> audit/edge-cases.md
     (d = 0 refused; negatives refused; bases 0 and 1 refused; d = 1
     integer/empty expansion; unreduced input reduced and RECORDED;
     large prime d = 9973 in base 10, period computed both ways).

Stdlib only. Usage:
  python3 caps/04-algarismos/oracle.py
"""
import json
import math
import platform
import subprocess
import sys
from datetime import date
from pathlib import Path

CHAPTER_DIR = Path(__file__).resolve().parent
AUDIT_DIR = CHAPTER_DIR / "audit"
BASES = [2, 3, 7, 10, 12, 16, 60]
MAX_D = 2000
EXPECTED_FULL_REPTEND_LT_100 = [7, 17, 19, 23, 29, 47, 59, 61, 97]


# --- input gate (adversarial): refuse garbage, record reductions -----------
def validate(a, d, b, *, reductions_log=None):
    """Domain gate. Refuses d = 0, negatives, bases < 2, non-integers.
    Reduces a/d if needed and RECORDS the reduction (never silent)."""
    for name, v in (("a", a), ("d", d), ("b", b)):
        if not isinstance(v, int):
            raise ValueError(f"refused: {name}={v!r} is not an integer")
    if d == 0:
        raise ValueError("refused: d = 0 (division by zero is not an expansion)")
    if a < 0 or d < 0:
        raise ValueError(f"refused: negative input a={a}, d={d} (domain: a >= 0, d >= 1)")
    if b < 2:
        raise ValueError(f"refused: base b={b} (positional notation needs integer b >= 2)")
    g = math.gcd(a if a else d, d)
    if g > 1:
        if reductions_log is not None:
            reductions_log.append({"input": f"{a}/{d}", "reduced_to": f"{a // g}/{d // g}", "divided_by": g})
        a, d = a // g, d // g
    return a, d, b


# --- implementation A: long-division state machine (observation) -----------
def machine(a, d, b):
    """Digit-by-digit long division. Returns (int_part, pre_digits,
    period_digits). Pre/period detected by first remainder repetition."""
    q, r = divmod(a, d)
    seen, digits = {}, []
    while r != 0 and r not in seen:
        seen[r] = len(digits)
        r *= b
        digits.append(r // d)
        r %= d
    if r == 0:
        return q, digits, []
    i = seen[r]
    return q, digits[:i], digits[i:]


# --- implementation B: theory prediction (no division simulated) -----------
def factorize(n):
    f = {}
    m = n
    p = 2
    while p * p <= m:
        while m % p == 0:
            f[p] = f.get(p, 0) + 1
            m //= p
        p += 1
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f


def mult_order(b, d):
    """ord_d(b) by successive powers; requires gcd(b, d) = 1, d > 1."""
    assert d > 1 and math.gcd(b, d) == 1
    k, x = 1, b % d
    while x != 1:
        x = x * b % d
        k += 1
    return k


def predict(d, b):
    """(pre_period, period) for any reduced a/d in base b, from theory:
    d = d_b * d'; pre = max_p ceil(v_p(d)/v_p(b)); period = ord_{d'}(b)."""
    fd, fb = factorize(d), factorize(b)
    dprime, pre = 1, 0
    for p, e in fd.items():
        if p in fb:
            pre = max(pre, -(-e // fb[p]))  # ceil(e / v_p(b))
        else:
            dprime *= p ** e
    per = mult_order(b, dprime) if dprime > 1 else 0
    return pre, per, dprime


def smallest_coprime_above_1(d):
    if d <= 2:
        return None
    a = 2
    while math.gcd(a, d) != 1:
        a += 1
    return a


def run_oracle():
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    results = {}

    # ---- I1/I2/I3/I4: machine vs theory over the full domain --------------
    mismatches_pre, mismatches_per, criterion_fail, a_dependence = [], [], [], []
    tested = 0
    for b in BASES:
        fb = set(factorize(b))
        for d in range(1, MAX_D + 1):
            numerators = [1]
            a2 = smallest_coprime_above_1(d)
            if a2 is not None:
                numerators.append(a2)
            pre_t, per_t, dprime = predict(d, b) if d > 1 else (0, 0, 1)
            outcomes = []
            for a in numerators:
                _, pre_m, per_m = machine(a, d, b)
                tested += 1
                if len(pre_m) != pre_t:
                    mismatches_pre.append((a, d, b, len(pre_m), pre_t))
                if len(per_m) != per_t:
                    mismatches_per.append((a, d, b, len(per_m), per_t))
                terminates = (per_m == [])
                clean = set(factorize(d)) <= fb if d > 1 else True
                if terminates != clean:
                    criterion_fail.append((a, d, b, terminates, clean))
                outcomes.append((len(pre_m), len(per_m)))
            if len(set(outcomes)) > 1:
                a_dependence.append((d, b, outcomes))
    results["I1_preperiod_machine_vs_theory"] = {
        "tested_expansions": tested, "mismatches": mismatches_pre[:5],
        "passed": not mismatches_pre}
    results["I2_period_machine_vs_theory"] = {
        "mismatches": mismatches_per[:5], "passed": not mismatches_per}
    results["I3_termination_criterion"] = {
        "statement": "machine terminates <=> every prime factor of reduced d divides b",
        "failures": criterion_fail[:5], "passed": not criterion_fail}
    results["I4_independence_of_numerator"] = {
        "statement": "pre-period and period identical for a=1 and smallest coprime a>1",
        "failures": a_dependence[:5], "passed": not a_dependence}

    # ---- I5: the seven case study -----------------------------------------
    q, pre, per = machine(1, 7, 10)
    ord7 = mult_order(10, 7)
    block = int("".join(map(str, per)))
    cyclic_ok = True
    rotations = {int(("".join(map(str, per)) * 2)[i:i + 6]) for i in range(6)}
    multiples = {m * block for m in range(1, 7)}
    cyclic_ok = rotations == multiples and len(multiples) == 6
    results["I5_seven_case_study"] = {
        "digits_1_over_7": per, "period": len(per), "ord_7_10": ord7,
        "full_reptend": ord7 == 6, "block": block,
        "multiples_are_rotations": cyclic_ok,
        "block_identity_999999": 7 * block == 10 ** 6 - 1,
        "passed": (per == [1, 4, 2, 8, 5, 7] and len(per) == 6 == ord7
                   and cyclic_ok and 7 * block == 10 ** 6 - 1)}

    # ---- I6: full-reptend primes < 100 in base 10 -------------------------
    frs = []
    for p in range(3, 100):
        if all(p % i for i in range(2, int(p ** 0.5) + 1)) and p not in (2, 5):
            if mult_order(10, p) == p - 1:
                frs.append(p)
    results["I6_full_reptend_below_100"] = {
        "found": frs, "expected": EXPECTED_FULL_REPTEND_LT_100,
        "passed": frs == EXPECTED_FULL_REPTEND_LT_100}

    # ---- I7: representational pathology — same number, other bases --------
    checks7 = {
        "1/7 base 7 exact 0.1": machine(1, 7, 7) == (0, [1], []),
        "1/3 base 3 exact 0.1": machine(1, 3, 3) == (0, [1], []),
        "1/3 base 10 pure period 3": machine(1, 3, 10) == (0, [], [3]),
        "1/2 base 3 pure period 1": machine(1, 2, 3) == (0, [], [1]),
        "1/7 base 12 period 6 (full reptend)": machine(1, 7, 12)[2] == [1, 8, 6, 10, 3, 5]
            and mult_order(12, 7) == 6,
        "1/7 base 16 period 3": machine(1, 7, 16)[2] == [2, 4, 9] and mult_order(16, 7) == 3,
        "1/7 base 60 period 3 (8:34:17)": machine(1, 7, 60)[2] == [8, 34, 17]
            and mult_order(60, 7) == 3,
    }
    results["I7_pathology_is_representational"] = {
        "checks": {k: bool(v) for k, v in checks7.items()},
        "passed": all(checks7.values())}

    # ---- I8: pure-period block identity a*(b^t - 1) = d*B -----------------
    block_fail = []
    for (a, d, b) in [(1, 7, 10), (5, 13, 10), (1, 3, 2), (3, 11, 12),
                      (1, 9973, 10), (7, 41, 16), (1, 59, 60)]:
        assert math.gcd(d, b) == 1 and math.gcd(a, d) == 1
        _, pre_m, per_m = machine(a, d, b)
        t = len(per_m)
        B = 0
        for u in per_m:
            B = B * b + u
        if pre_m != [] or a * (b ** t - 1) != d * B:
            block_fail.append((a, d, b))
    results["I8_pure_period_block_identity"] = {
        "statement": "for gcd(d,b)=1: pre-period empty and a*(b^t-1) = d*B (B = period block)",
        "failures": block_fail, "passed": not block_fail}

    # ---- doors (witness only, no claim of proof) --------------------------
    results["W1_door_witness_998001"] = {
        "ord_998001_10": mult_order(10, 998001),
        "ord_9801_10": mult_order(10, 9801),
        "note": "witness values for the closed door (Cap. 10); 2997 and 198 as stated",
        "passed": mult_order(10, 998001) == 2997 and mult_order(10, 9801) == 198}

    all_passed = all(v["passed"] for v in results.values())
    commit = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
        cwd=CHAPTER_DIR).stdout.strip() or "unknown"

    report = {
        "chapter": 4,
        "script": "caps/04-algarismos/oracle.py",
        "code_commit": commit,
        "date": date.today().isoformat(),
        "environment": f"python {platform.python_version()}, stdlib only, {platform.system().lower()}",
        "implementations": {
            "A": "long-division state machine, digit by digit (mirrors in-page JS)",
            "B": "theory: pre = max ceil(v_p(d)/v_p(b)); period = mult. order via successive powers"},
        "tested_domain": {
            "d": {"min": 1, "max": MAX_D},
            "bases": BASES,
            "numerators": "a = 1 and smallest coprime a > 1 (reduced fractions only)",
            "expansions_compared": tested},
        "invariants": results,
        "all_passed": all_passed,
    }
    (AUDIT_DIR / "numeric-check.json").write_text(json.dumps(report, indent=2) + "\n")

    # ---- edge / degenerate / adversarial cases -> edge-cases.md -----------
    edge = []
    reductions = []

    def refused(a, d, b, why):
        try:
            validate(a, d, b)
            return (f"adversarial a={a}, d={d}, b={b}", "was NOT refused", False)
        except ValueError as e:
            return (f"adversarial a={a}, d={d}, b={b} ({why})", f"refused with: {e}", True)

    edge.append(refused(1, 0, 10, "d = 0"))
    edge.append(refused(-1, 7, 10, "negative numerator"))
    edge.append(refused(1, -7, 10, "negative denominator"))
    edge.append(refused(1, 7, 1, "base 1"))
    edge.append(refused(1, 7, 0, "base 0"))
    # unreduced input: must be reduced FIRST and recorded, then match reduced run
    a_, d_, b_ = validate(2, 6, 10, reductions_log=reductions)
    same = machine(a_, d_, b_) == machine(1, 3, 10) and (a_, d_) == (1, 3)
    edge.append(("unreduced 2/6 base 10",
                 f"reduced to {a_}/{d_} (recorded: {reductions[-1]}), expansion equals 1/3's",
                 same and bool(reductions)))
    a_, d_, b_ = validate(3, 6, 10, reductions_log=reductions)
    fin = machine(a_, d_, b_) == (0, [5], []) and (a_, d_) == (1, 2)
    edge.append(("unreduced 3/6 base 10",
                 f"reduced to {a_}/{d_} (recorded), terminates as 0.5 while 2/6 = 1/3 does not"
                 " — the reduction hypothesis is load-bearing (Enunciado C)", fin))
    # d = 1: integer, empty fractional expansion
    edge.append(("d = 1 (integer)",
                 f"5/1 base 10 -> int 5, empty expansion: {machine(5, 1, 10)}",
                 machine(5, 1, 10) == (5, [], [])))
    # a = 0
    edge.append(("a = 0", f"0/7 -> {machine(0, 7, 10)} (zero, empty expansion)",
                 machine(0, 7, 10) == (0, [], [])))
    # a > d (integer part nontrivial)
    edge.append(("a > d", f"22/7 base 10 -> int 3, same period as 1/7: {machine(22, 7, 10)[0]}, {machine(22, 7, 10)[2]}",
                 machine(22, 7, 10)[0] == 3 and len(machine(22, 7, 10)[2]) == 6))
    # large prime 9973: period computed both ways
    _, pre9973, per9973 = machine(1, 9973, 10)
    ord9973 = mult_order(10, 9973)
    edge.append(("large prime d = 9973, base 10",
                 f"machine period {len(per9973)} (pre {len(pre9973)}) vs ord_9973(10) = {ord9973} "
                 f"computed by successive powers; 9973 is prime; ord divides 9972: {9972 % ord9973 == 0}",
                 len(per9973) == ord9973 == 554 and pre9973 == []))

    lines = ["# Capítulo 4 — Casos extremos, degenerados e adversariais",
             "",
             f"Gerado por `caps/04-algarismos/oracle.py` em {date.today().isoformat()}, "
             f"commit `{commit}`.", "",
             "Reduções registradas (nunca silenciosas): " + json.dumps(reductions), ""]
    for name, desc, ok in edge:
        lines.append(f"- **{name}** — {desc} → **{'passou' if ok else 'FALHOU'}**")
    edge_ok = all(ok for _, _, ok in edge)
    lines += ["", f"Resultado global: **{'passou' if edge_ok else 'FALHOU'}**."]
    (AUDIT_DIR / "edge-cases.md").write_text("\n".join(lines) + "\n")

    print(json.dumps({k: v["passed"] for k, v in results.items()}, indent=2))
    print("edge cases:", "passed" if edge_ok else "FAILED")
    print("all:", "PASSED" if (all_passed and edge_ok) else "FAILED")
    return 0 if (all_passed and edge_ok) else 1


if __name__ == "__main__":
    sys.exit(run_oracle())
