# Capítulo 0 — Casos extremos, degenerados e adversariais (braço 3 do oráculo)

Data: 28/07/2026. Execução: `tools/oracle-ch00.py` (invariantes I6b, I11, I12).

## Domínio recusado (I12)

| Entrada | Resultado | Motivo |
|---|---|---|
| n = 2 | recusado | dígono degenerado: ρ = cos(π/2) = 0, "polígono" sem área; fora do domínio n ≥ 3 |
| n = 1, 0, −6 | recusado | não são polígonos |
| n = 2,5 | recusado | não inteiro |
| n = "12" (string) | recusado | tipo inválido; aceitação silenciosa seria coerção, não matemática |

Fronteira mínima aceita: n = 3 (ρ₃ = 1/2, o menor admissível — o triângulo
equilátero é o polígono de razão mais magra; abaixo dele a hipótese é refutável).

## O instrumento declara círculo (I11 · conjectura C0.8 confirmada)

Em float64, o espaçamento dos representáveis vizinhos de 1 é 2⁻⁵³ ≈ 1,1·10⁻¹⁶.
Em n = 3·10⁸: `1 − cos(π/n)` devolve exatamente 0,0 (déficit verdadeiro
≈ 5,48·10⁻¹⁷, confirmado por Decimal com 50 dígitos e pela forma estável
2·sen²(π/2n), concordância relativa 1,3·10⁻¹⁶). Classificação (§2.3):
imperfeição **computacional/representacional** — o objeto (o polígono de
3·10⁸ lados) permanece perfeitamente distinto do círculo; a representação
direta é que não tem resolução para dizê-lo.

## A folga afogada em cancelamento (I6b · incidente de desenvolvimento)

Durante a verificação exploratória pré-oráculo, o sanduíche da folga
(Enunciado H) foi testado com a forma direta `cos(π/(n+1)) − cos(π/n)` e
"falhou" 174.477 vezes em [3, 200000], primeira violação em n = 14.921.
Diagnóstico: cancelamento catastrófico — a folga vale ~10⁻¹², o erro de
arredondamento de cada cosseno ~10⁻¹⁶, sobrando ~10⁻⁴ de precisão relativa,
da própria ordem da largura do sanduíche. A forma de produto
2·sen α·sen β (a mesma da demonstração) computa sem cancelamento: zero
violações; Decimal 50 dígitos arbitra os casos originalmente "violados"
(ex.: n = 14.921) e confirma o sanduíche. O invariante I6b passou a exigir
que a forma ingênua FALHE — a falha é o registro do fenômeno, não um bug
tolerado. A prova forneceu a representação numericamente correta do próprio
teorema.

## Margem sub-float64 na ambiguidade (I8)

No Enunciado J, a margem estrita δ − g_n/2 encolhe como δ·(déficit + 2/n):
em n = 10⁵ ela vale ~10⁻²⁴, abaixo da resolução do float64 (que ali é
~10⁻¹⁶). O oráculo decide em float64 até n = 1000 e delega n ∈ {10⁵, 10⁷}
ao Decimal de 50 dígitos. Registrado como limitação declarada do instrumento,
não do teorema.

## Fronteiras do exemplo trabalhado, δ = 10⁻⁶ (I10)

- Garantia pelas cotas (Enunciado I): até n = 169 (2δ < 2,020·10⁻⁶ = cota).
- n = 170: cotas silenciosas; cálculo direto: g₁₇₀/2 = 9,9559·10⁻⁷ < δ —
  **já ambíguo** (a primeira redação do capítulo afirmou o contrário e foi
  refutada por este invariante; corrigida e registrada).
- Ambiguidade certificada pela cota (Enunciado J): de n = 171 em diante.
- Exclusão do círculo por cálculo direto: até n = 1570
  (1 − ρ₁₅₇₀ = 2,0020·10⁻⁶ > 2δ); falha a partir de n = 1571
  (1 − ρ₁₅₇₁ = 1,9995·10⁻⁶ ≤ 2δ).
