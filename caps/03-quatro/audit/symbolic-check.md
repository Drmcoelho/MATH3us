# Capítulo 3 — Verificação simbólica (braço 1 do oráculo triplo)

Data: 28/07/2026. Hipóteses globais: domínio ℝ⁺ = {x real, x > 0};
x^x definido como e^{x·ln x}. Ferramentas importadas e declaradas no
capítulo (seção 4): ln : ℝ⁺ → ℝ bijeção estritamente crescente e contínua,
ln(uv) = ln u + ln v, ln 1 = 0 (construção → Cap. 10); teorema do valor
intermediário (demonstração → Cap. 6).

## S1. Soma = produto (Enunciado A)

Álgebra pura em ℝ, sem logaritmo:

    x + x = x²  ⟺  x² − 2x = 0  ⟺  x·(x − 2) = 0  ⟺  x ∈ {0, 2}.

Princípio usado: produto nulo ⟺ algum fator nulo (domínio de
integridade de ℝ). Filtro de domínio ℝ⁺: {2}.                        ∎

Método registrado: fatorar, nunca dividir — dividir por x embutiria a
hipótese x ≠ 0 sem declará-la.

## S2. Produto = potência (Enunciado B)

Para x > 0, ln é bijeção, logo aplicá-lo preserva equivalência:

    x² = x^x  ⟺  ln(x²) = ln(x^x)  ⟺  2·ln x = x·ln x
              ⟺  (x − 2)·ln x = 0
              ⟺  x = 2  ou  ln x = 0  ⟺  x ∈ {1, 2}.

Domínio conferido: x > 0 em todos os passos; ln x se anula exatamente em
x = 1 (injetividade de ln com ln 1 = 0).                              ∎

Sutileza documentada: dividir por ln x pressupõe ln x ≠ 0 e amputa a
solução x = 1 silenciosamente. A fatoração preserva os dois fatores.

## S3. Soma = potência (Enunciado C)

Para x > 0, com ln(2x) = ln 2 + ln x:

    2x = x^x  ⟺  ln 2 + ln x = x·ln x  ⟺  (x − 1)·ln x = ln 2.

Defina h(x) = (x − 1)·ln x. Classificação de h(x) = ln 2:

**Ramo [1, ∞).** h(1) = 0. Para 1 < u < v: 0 < u − 1 < v − 1 e
0 < ln u < ln v (ln crescente), logo (u−1)·ln u < (v−1)·ln u < (v−1)·ln v:
h estritamente crescente. h(2) = (2−1)·ln 2 = ln 2 **exatamente** — x = 2
é solução; a monotonia estrita proíbe outra no ramo.

**Ramo (0, 1).** Reescrita exata: h(x) = (−(x−1))·(−ln x) = (1 − x)·ln(1/x),
produto de dois fatores positivos em (0, 1). Ambos estritamente decrescem
quando x cresce: 1 − x diretamente; 1/x decresce e ln é crescente, logo
ln(1/x) decresce. Produto de positivos estritamente decrescentes é
estritamente decrescente (mesmo argumento de S3-ramo-1, espelhado):
para 0 < u < v < 1, (1−v)·ln(1/v) < (1−u)·ln(1/v) < (1−u)·ln(1/u).

Valores exibidos (troca de sinal):

    h(0,3) = 0,7·ln(10/3) ≈ 0,84278 > ln 2 ≈ 0,69315 > 0,54977 ≈ 0,6·ln(5/2) = h(0,4).

h é contínua em (0, 1) (produto/composição de contínuas — continuidade de
ln importada). Pelo TVI (importado), existe r ∈ (0,3; 0,4) com h(r) = ln 2;
pela monotonia estrita, é único em (0, 1). Conjunto solução: {r, 2}.  ∎

A localização fina de r é do braço numérico (bissecção certificada,
`numeric-check.json`, invariante I4): r ≈ 0,346323362279 com
h(0,346323362278) > ln 2 > h(0,346323362279). Forma fechada: porta
fechada (Lambert W → Cap. 10) — não reivindicada.

## S4. A interseção (Enunciado D)

    {x > 0 : x+x = x² = x^x} = {2} ∩ {1, 2} ∩ {r, 2} = {2},

pois r < 1 < 2 implica r ∉ {2} e 1 ∉ {2}. Conferência dos candidatos que
caem: x = 1 falha A (1+1 = 2 ≠ 1); x = r falha A (r ∉ {2}). Valor comum
em x = 2: 2+2 = 2·2 = 2² = 4 (aritmética exata).

Corolário inteiro: k inteiro positivo com k+k = k·k = k^k ⟹ k real
positivo satisfazendo as três ⟹ k = 2 ⟹ valor 4.                    ∎

## S5. Separação estrita para x ≥ 3 (curto-circuito do oráculo)

Para inteiro x ≥ 3:

    x² − 2x = x·(x − 2) ≥ 3·1 = 3 > 0        ⟹  x² > 2x;
    x^x = x²·x^{x−2},  x^{x−2} ≥ x¹ = x ≥ 3   ⟹  x^x ≥ 3·x² > x².

Logo 2x < x² < x^x para todo inteiro x ≥ 3: nenhuma das três equações
pode valer, e a varredura exata do oráculo só precisa de potências
completas em x ∈ {1, 2}. Este é o curto-circuito documentado usado por
`oracle.py` (invariante I1) para não computar 10000^10000.            ∎

## O que este documento NÃO estabelece

- A forma fechada de r: exige Lambert W sobre a exponencial do Cap. 10.
  Aqui r é apenas localizado numericamente com certificado.
- O valor (ou não-valor) de 0⁰ e o limite x^x → 1 quando x → 0⁺: citados
  como clássicos, porta fechada para o interlúdio do Cap. 10 (E19). O
  braço de casos extremos registra o comportamento float como nota de
  camada de observação, não como prova.
- As construções de ln, exp e a demonstração do TVI: importadas
  (Caps. 10 e 6), declaradas no capítulo e no `claims.yml`.
