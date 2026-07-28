# Capítulo 3 — Casos extremos, degenerados e adversariais

Gerado por `caps/03-quatro/oracle.py` em 2026-07-28, commit `e2cb3ef`.

- **adversarial x=0** — refused with: refused: x=0 outside domain R+ (x^x would be the 0^0 dispute — declared closed door, Chapter 10) → **passou**
- **adversarial x=-1** — refused with: refused: x=-1 negative (x^x not real-defined for general negative reals; domain is R+) → **passou**
- **adversarial x=-4** — refused with: refused: x=-4 negative (x^x not real-defined for general negative reals; domain is R+) → **passou**
- **x=1 pairwise vs triple** — 1·1 = 1^1 = 1 holds (pairwise) but 1+1 = 2 ≠ 1 (triple fails); scan confirms 1 in {x²=x^x} and 1 not in triple → **passou**
- **x=2 exact triple** — 2+2 = 2·2 = 2² = 4 in exact integers → **passou**
- **float x^x as x->0+** — float64 x^x at x=1e-1..1e-12: 0.7943282347, 0.9549925860, 0.9990793900, 0.9999998158, 1.0000000000 — approaches 1, NOT 0. Observation layer (manual §2.1): float exp/log rounding present; the limit statement itself is cited classical (closed door to Chapter 10) → **passou**
- **float sign change at the certificate bracket** — float64 reproduces the Decimal sign change at the 12-decimal bracket of r → **passou**

Resultado global: **passou**.
