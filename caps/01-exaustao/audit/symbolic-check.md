# Capítulo 1 — Verificação simbólica (braço 1 do oráculo triplo)

Data: 28/07/2026. Hipóteses globais: círculo de raio 1; n = 6·2^k, k ≥ 0;
a_n, b_n = semiperímetros dos polígonos regulares inscrito e circunscrito.
Formas fechadas (estatuto geométrico de sen e tg — razões no círculo):
a_n = n·sen(π/n), b_n = n·tg(π/n).

## S1. Recorrência harmônica (b_2n)

Com x = π/n:

    2·a_n·b_n/(a_n + b_n)
      = 2·(n sen x)(n tg x) / (n sen x + n tg x)
      = 2n·sen x·tg x / (sen x + tg x)          [cancela n]
      = 2n·tg x / (1 + 1/cos x)                 [divide por sen x; sen x ≠ 0 pois 0 < x ≤ π/6]
      = 2n·sen x / (cos x + 1)                  [multiplica por cos x]
      = 2n·tg(x/2)                              [identidade tg(x/2) = sen x/(1+cos x)]
      = b_2n.                                   ∎

Domínio conferido: 0 < x ≤ π/6 ⟹ cos x > 0, sen x > 0, 1 + cos x > 0 —
nenhuma divisão por zero em passo algum.

## S2. Recorrência geométrica (a_2n)

    a_n · b_2n = (n sen x)(2n tg(x/2)) = 2n²·sen x·tg(x/2).

Com sen x = 2 sen(x/2) cos(x/2):

    2·sen x·tg(x/2) = 2·2 sen(x/2)cos(x/2)·sen(x/2)/cos(x/2) = 4 sen²(x/2).

Logo √(a_n·b_2n) = √(4n² sen²(x/2)) = 2n·sen(x/2) = a_2n
(raiz positiva legítima: sen(x/2) > 0 no domínio).                        ∎

## S3. Monotonia e aprisionamento (Enunciado B do capítulo)

Indução com base a_6 = 3 < 2√3 = b_6. Passo, supondo a_n < b_n:

1. Média harmônica de positivos distintos fica estritamente entre eles:
   a_n < b_2n < b_n. (Prova: H = 2ab/(a+b); H − a = a(b−a)/(a+b) > 0;
   b − H = b(b−a)/(a+b) > 0.)
2. a_2n = √(a_n·b_2n) > √(a_n²) = a_n   [pois b_2n > a_n].
3. a_2n = √(a_n·b_2n) < √(b_2n²) = b_2n [pois a_n < b_2n].              ∎

## S4. Queda da folga à metade (Enunciado C)

    b_2n − a_n = a_n(b_n − a_n)/(a_n + b_n) < ½(b_n − a_n)
                 [pois a_n/(a_n+b_n) < ½ ⟺ a_n < b_n, garantido por S3]

    b_2n − a_2n < b_2n − a_n                  [a_2n > a_n, por S3]
                < ½(b_n − a_n).                                           ∎

Iterando desde k = 0: b_n − a_n ≤ (2√3 − 3)/2^k para n = 6·2^k, com
igualdade apenas em k = 0 (o passo S4 só se aplica a partir da primeira
duplicação; para k ≥ 1 a desigualdade é estrita).

*Registro de correção (28/07/2026):* a primeira redação afirmava < para
todo k — refutada pelo invariante I6 do braço numérico em k = 0. Corrigida
aqui e no capítulo; o caso k = 0 permanece no domínio de teste do oráculo.

## S5. Convergência e limite comum

(a_n) crescente e limitada (por b_6), (b_n) decrescente e limitada (por a_6):
pelo teorema da convergência monótona (provado no capítulo a partir do
princípio do supremo, importado e declarado), ambas convergem. Por S4 a
diferença tende a zero, logo o limite é comum; π é *definido* como esse
limite. Cota de erro: |a_n − π| ≤ b_n − a_n < (2√3 − 3)/2^k.              ∎

## Simplificação simbólica independente

As cadeias S1–S2 foram conferidas passo a passo por manipulação algébrica
explícita (acima). Adicionalmente, o braço numérico (`numeric-check.json`,
invariante I1) compara as recorrências com as formas fechadas em todo o
domínio testado — uma discrepância em qualquer identidade de S1–S2
apareceria ali como desvio. As verificações são independentes: esta é
álgebra; aquela é amostragem em três implementações.

## O que este documento NÃO estabelece

- A razão de contração 1/4 (conjectura `chapter-01.gap-ratio-quarter`):
  aqui só está provado o fator 1/2 (S4).
- A identificação de π com o semiperímetro do círculo: condicional ao
  postulado de convexidade de Arquimedes (`chapter-01.circle-identification`,
  porta para o Cap. 9).
