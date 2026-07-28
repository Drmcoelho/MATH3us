# Capítulo 4 — Casos extremos, degenerados e adversariais

Gerado por `caps/04-algarismos/oracle.py` em 2026-07-28, commit `7497538`.

Reduções registradas (nunca silenciosas): [{"input": "2/6", "reduced_to": "1/3", "divided_by": 2}, {"input": "3/6", "reduced_to": "1/2", "divided_by": 3}]

- **adversarial a=1, d=0, b=10 (d = 0)** — refused with: refused: d = 0 (division by zero is not an expansion) → **passou**
- **adversarial a=-1, d=7, b=10 (negative numerator)** — refused with: refused: negative input a=-1, d=7 (domain: a >= 0, d >= 1) → **passou**
- **adversarial a=1, d=-7, b=10 (negative denominator)** — refused with: refused: negative input a=1, d=-7 (domain: a >= 0, d >= 1) → **passou**
- **adversarial a=1, d=7, b=1 (base 1)** — refused with: refused: base b=1 (positional notation needs integer b >= 2) → **passou**
- **adversarial a=1, d=7, b=0 (base 0)** — refused with: refused: base b=0 (positional notation needs integer b >= 2) → **passou**
- **unreduced 2/6 base 10** — reduced to 1/3 (recorded: {'input': '2/6', 'reduced_to': '1/3', 'divided_by': 2}), expansion equals 1/3's → **passou**
- **unreduced 3/6 base 10** — reduced to 1/2 (recorded), terminates as 0.5 while 2/6 = 1/3 does not — the reduction hypothesis is load-bearing (Enunciado C) → **passou**
- **d = 1 (integer)** — 5/1 base 10 -> int 5, empty expansion: (5, [], []) → **passou**
- **a = 0** — 0/7 -> (0, [], []) (zero, empty expansion) → **passou**
- **a > d** — 22/7 base 10 -> int 3, same period as 1/7: 3, [1, 4, 2, 8, 5, 7] → **passou**
- **large prime d = 9973, base 10** — machine period 554 (pre 0) vs ord_9973(10) = 554 computed by successive powers; 9973 is prime; ord divides 9972: True → **passou**

Resultado global: **passou**.
