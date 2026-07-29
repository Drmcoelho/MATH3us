# Capítulo 7 — Casos extremos, degenerados e adversariais

Gerado por `caps/07-complexos/oracle.py` em 2026-07-29, commit `df8cfdd`.

- **degenerate w = 0** — z^n = 0 forces z = 0 (|z|^n = 0); explorer announces the single collapsed root instead of drawing a polygon → **passou**
- **division by 0 in Z[i]** — refused with: refused: division by 0 in Z[i] → **passou**
- **inverse of 0 in C** — refused with: refused: inverse of 0 does not exist in C → **passou**
- **p = 2 special case** — 2 = 1^2 + 1^2 (reps: [(1, 1)]); (1+i)^2 = (0, 2), -i*(1+i)^2 = (2, 0) → **passou**
- **float wraparound at the cut (observation layer)** — z = -1 + 1e-15 i: Arg z + Arg z = 6.283185307179584 lies outside (-pi, pi]; Arg(z^2) = -2.00e-15; the 2*pi correction is the REPRESENTATIVE failing, not the set-law arg(zw) = arg z + arg w -- recorded as an observation-layer note (section 10) → **passou**
- **unit-multiplication invariance** — associates u*z (u in {1,-1,i,-i}) share primality with z (brute-force check on 5 witnesses x 4 units) → **passou**
- **largest 1-mod-4 prime checked by hand in text (49993)** — 49993 = 68^2 + 213^2; reps found: [(68, 213)] → **passou**

Resultado global: **passou**.
