# Capítulo 1 — Casos extremos, degenerados e adversariais

Gerado por `tools/oracle.py` em 2026-07-28, commit `cca24d6`.

- **base case exactness** — a_6 == 3 exactly (rational); b_6 == 2*sqrt(3) to 60 digits → **passou**
- **minimal domain value k=0** — 3 < pi < 2*sqrt(3) holds at the very first step → **passou**
- **float64 plateau at deep k** — k=40: float gap = 0.000e+00 (plateaued near machine epsilon), Decimal-60 gap = 3.562E-25 (still contracting by ~1/4). Representation-layer artifact (manual section 2.3, computational), not a property of the object. → **passou**
- **degenerate a=b fixed point** — if a=b the recurrences return a=b unchanged (closed trap stays closed) → **passou**
- **adversarial n=7** — refused with: refused: n=7 is not of the form 6*2^k → **passou**
- **adversarial n=100** — refused with: refused: n=100 is not of the form 6*2^k → **passou**

Resultado global: **passou**.
