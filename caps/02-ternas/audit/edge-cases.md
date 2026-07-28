# Capítulo 2 — Casos extremos, degenerados e adversariais

Gerado por `caps/02-ternas/oracle.py` em 2026-07-28, commit `3c8942d`.

- **adversarial even n=2** — refused with: refused: n=2 is even -- L=(n^2-1)/2=1.5 and R=(n^2+1)/2=2.5 are not integers (lemma 5.4) (n^2±1 odd: True) → **passou**
- **adversarial even n=4** — refused with: refused: n=4 is even -- L=(n^2-1)/2=7.5 and R=(n^2+1)/2=8.5 are not integers (lemma 5.4) (n^2±1 odd: True) → **passou**
- **adversarial even n=100** — refused with: refused: n=100 is even -- L=(n^2-1)/2=4999.5 and R=(n^2+1)/2=5000.5 are not integers (lemma 5.4) (n^2±1 odd: True) → **passou**
- **degenerate/invalid n=1** — refused with: refused: n=1 < 3 -- n=1 degenerates (L=0, no triangle); negatives and zero are outside the family's domain → **passou**
- **degenerate/invalid n=0** — refused with: refused: n=0 is even -- L=(n^2-1)/2=-0.5 and R=(n^2+1)/2=0.5 are not integers (lemma 5.4) → **passou**
- **degenerate/invalid n=-5** — refused with: refused: n=-5 < 3 -- n=1 degenerates (L=0, no triangle); negatives and zero are outside the family's domain → **passou**
- **smallest member n=3** — (3, 4, 5); P=12, s=6, K=6, r=1, r_n=2 → **passou**
- **huge n = 10^6 + 1 exact** — L=500001000000, R=500001000001; all invariants exact in bignum → **passou**
- **float64 observation-layer trap at n = 10^6 + 1** — exact test = 0; float64 test = -33554432.0 (L^2 = 250001000001000000000000 > 2^53 = 9007199254740992). The observation layer would refute a true identity -- manual section 2.3, computational imperfection; the oracle therefore uses exact integers only. → **passou**
- **boundary acceptance n=3** — accepted as smallest member → **passou**

Resultado global: **passou**.
