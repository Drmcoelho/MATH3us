# Capítulo 6 — Casos extremos, degenerados e adversariais

Gerado por `caps/06-patologias/oracle.py` em 2026-07-29, commit `95ed8ad`.

Os casos adversariais deste capítulo são o seu coração: cada um
documenta a camada de observação (manual §2.1/§2.3) falhando
estruturalmente — que é a tese do capítulo, não um acidente.

- **C1: cegueira float de Dirichlet** — 4096 floats amostrados, 4096 racionais (todo float e p*2^e, lema da secao 7); D = 1 em 100% das amostras. Imperfeicao COMPUTACIONAL (manual 2.3): a camada de observacao nao alcanca a propriedade. C1 confirmada. → **passou**
- **denominador 0** — recusado com: refused: denominator 0 is not a rational → **passou**
- **fracao nao reduzida 6/8** — T(6/8) = 1/4 (reduz antes); implementacao ingenua daria 1/8 — funcao mal definida (6/8 = 3/4 com dois valores). Registrado como armadilha de implementacao. → **passou**
- **piso em float para j = floor(2^60/3)** — exato 384307168202282325 vs float 384307168202282304 (diferenca -21); a sonda usa BigInt/Fraction por isso. → **passou**
- **sonda alem de m = 53 no float de sqrt2/2** — S_53..S_64 = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2]: cresce linearmente (digitos 0 para sempre) — o float diverge como um diadico, DIFERENTE do irracional que representava (secao 7 do capitulo). → **passou**
- **intervalo diadico mais a direita [1 - 2^-m, 1]** — declive = -m pelas duas rotas (espelho do +m em 0) → **passou**
- **serra fora de [0,1) e em negativos** — s(-1/4)=1/4, s(-7/3)=1/3, s(5/2)=1/2, s(17)=0 — exatos → **passou**

Veredito das conjecturas pré-registradas: C1 confirmada (E1); C2 confirmed (I5); C3 confirmada (I3a); C4 confirmada (I3c); C5 REFUTED (I8: 2 mudanças de sinal, max|S| = 9).

Resultado global: **passou**.
