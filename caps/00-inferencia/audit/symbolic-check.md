# Capítulo 0 — Verificação simbólica (braço 1 do oráculo triplo)

Data: 28/07/2026. Álgebra conferida à mão, enunciado por enunciado, com
hipóteses e domínio declarados. O braço numérico (`numeric-check.json`,
`tools/oracle-ch00.py`) exercita cada desigualdade de forma independente.

Convenções: n ≥ 3 inteiro; θ = π/n (medida do ângulo pela área, seção 3 do
capítulo); ρ_n = cos(π/n); g_n = ρ_{n+1} − ρ_n; sen/cos/tg com estatuto
geométrico (razões no triângulo retângulo).

## A — Triângulo fundamental

OVV′ isósceles (OV = OV′ = R) ⟹ mediana OM ⊥ VV′ ⟹ OMV retângulo em M.
Pitágoras: R² = r² + (L/2)². Razões: r/R = cos θ, (L/2)/R = sen θ, com θ o
semiângulo central (a volta é 2n cunhas; cada cunha subtende 2π/(2n) = π/n).
✓

## B — Identidade da coroa

C·R² − C·r² = C·(R² − r²) = C·(L/2)², direto de A. Independe do valor de C.
✓ (uma linha; sem consumo de π)

## C — Aprisionamento por área

Área da cunha OMV = (1/2)·(L/2)·r (triângulo retângulo de catetos r e L/2).
Polígono = 2n cunhas ⟹ A_n = n·(L/2)·r. Inclusões estritas
(disco inscrito ⊂ polígono ⊂ disco circunscrito) + monotonia da área ⟹
C·r² < A_n < C·R². ✓

## D — Monotonia da razão

cos θ′ − cos θ = 2·sen((θ+θ′)/2)·sen((θ−θ′)/2) > 0 para
0 < θ′ < θ < π (ambos os fatores positivos: os ângulos estão em (0, π)).
π/n estritamente decrescente em n ⟹ ρ_n estritamente crescente.
ρ_3 = cos(π/3) = 1/2; ρ_n < 1 pois L/2 > 0 em A. ✓

## E — Teorema da inferência

(i) injetividade de n ↦ ρ_n é D; L = 2√(R²−r²) é A; unicidade a menos de
rotação: n pontos equiespaçados em circunferência fixada. (ii) ida pela
definição; volta pela construção do n-ágono com circunraio R; razões < 1/2
inadmissíveis por D. (iii) construção L = 2r·tg(π/n) realiza qualquer r com
qualquer n. ✓

## F — Desigualdade da cunha

Triângulo OAB ⊂ setor OAB ⊂ triângulo OAT (T na tangente em A; existe pois
θ < π/2). Áreas: (1/2)sen θ < (1/2)θ < (1/2)tg θ — a área do setor é θ/2 POR
DEFINIÇÃO da medida do ângulo pela área (seção 3). Inclusões estritas ⟹
desigualdades estritas. Consequência: θ < tg θ = sen θ/cos θ ⟹ θ·cos θ < sen θ.
Hipótese usada: 0 < θ < π/2 — satisfeita por θ = π/n e θ = π/2n para n ≥ 3.
✓ (nenhum limite, nenhuma série)

## G — Sanduíche do déficit

1 − ρ_n = 1 − cos θ = 2·sen²(θ/2), θ = π/n (ângulo-metade).
Direita: sen(θ/2) < θ/2 ⟹ 2 sen²(θ/2) < θ²/2 = π²/2n².
Esquerda: sen(θ/2) > (θ/2)·cos(θ/2) ⟹ 2 sen²(θ/2) > (θ²/2)·cos²(θ/2)
       = (π²/2n²)·ρ_{2n}²,  pois cos(θ/2) = cos(π/2n) = ρ_{2n}.
Estritas para todo n ≥ 3 (θ/2 ∈ (0, π/2)). ✓

Sagita: R − r = R(1 − cos θ) = 2R·sen²(θ/2) = c²/(2R), c = 2R·sen(π/2n)
(lado do 2n-ágono de mesmo circunraio). ✓

## H — Sanduíche da folga

Produto: g_n = cos(π/(n+1)) − cos(π/n) = 2·sen α·sen β com
α = π(2n+1)/(2n(n+1)), β = π/(2n(n+1)); conferido: α+β = π/n, α−β = π/(n+1);
α < π/2 ⟺ 2n+1 < n(n+1) ⟺ n² − n − 1 > 0, verdadeiro para n ≥ 2. ✓

Direita: g_n < 2αβ = π²(2n+1)/(2n²(n+1)²) < π²/n³
  ⟺ n(2n+1) < 2(n+1)² ⟺ 2n²+n < 2n²+4n+2 ⟺ 0 < 3n+2. ✓
Esquerda: g_n > 2αβ·cos α·cos β, e
  cos α·cos β = ½[cos(α−β) + cos(α+β)] = (ρ_{n+1} + ρ_n)/2  (produto-para-soma)
⟹ g_n > αβ(ρ_n + ρ_{n+1}) = π²(2n+1)(ρ_n+ρ_{n+1})/(4n²(n+1)²)
       > π²·(2n)·(2ρ_n)/(4n²(n+1)²) = π²·ρ_n/(n(n+1)²). ✓
(usa 2n+1 > 2n e ρ_{n+1} > ρ_n, de D)

## I — Garantia de identificação

Hipóteses ⟹ (por H) 2δ < g_n e, se n > 3, 2δ < g_{n−1}. Para m ≠ n,
|ρ_m − ρ_n| ≥ min(g_{n−1}, g_n) > 2δ (monotonia D); |ρ̃ − ρ_n| ≤ δ ⟹
|ρ̃ − ρ_m| > δ ≥ |ρ̃ − ρ_n|. O mais próximo é ρ_n. n = 3: não há admissível
à esquerda; condição sobre g_{n−1} vazia. ✓

## J — Ambiguidade

2δ ≥ π²/n³ > g_n (por H) ⟹ g_n/2 < δ ⟹ o ponto médio dista g_n/2 < δ de
ambos. Dois estados do mundo, mesmo dado. ✓

## K — Janela crepuscular

(a) n ≥ (π²/2δ)^{1/3} ⟺ 2δ ≥ π²/n³ ⟹ J.
(b) ρ_{2n} ≥ ρ_6 = √3/2 (D, 2n ≥ 6) ⟹ (por G)
    1 − ρ_n > (π²/2n²)(3/4) = 3π²/8n² > 2/n²  (3π²/8 = 3,701… > 2);
    n ≤ 1/√δ ⟹ 2δ ≤ 2/n² < 1 − ρ_n ⟹ ρ̃ + δ ≤ ρ_n + 2δ < 1;
    conjunto compatível limitado pois ρ_m ↑ 1 e o intervalo fica abaixo de 1.
Não-vazia para δ ≤ 1/100:
    δ^{−1/2} = δ^{−1/6}·δ^{−1/3} ≥ 100^{1/6}·δ^{−1/3} > 2,15·δ^{−1/3};
    (π²/2)^{1/3} = 1,7010… < 1,71;
    diferença das pontas > (2,15 − 1,71)·δ^{−1/3} = 0,44·δ^{−1/3}
    ≥ 0,44·100^{1/3} = 0,44·4,64… > 2 ⟹ ao menos dois inteiros. ✓
Conferências: 100^{1/6} = 2,154…; (π²/2)^{1/3} = (4,9348…)^{1/3} = 1,7010…;
100^{1/3} = 4,641… ✓

## O que esta verificação NÃO estabelece

- Nenhum enunciado com seta (→): as estabilizações de n²(1−ρ_n) e n³·g_n em
  π²/2 e π² são conjectura pré-registrada (C0.7), sustentada pelos sanduíches
  mas não enunciável sem linguagem de limite — porta para o Cap. 1.
- A identificação da constante de área C (chamada π aqui) com a constante
  perimetral do Cap. 1 — porta para o Cap. 9. As implementações numéricas
  (funções trigonométricas padrão) pressupõem essa coincidência: camada de
  observação, declarada.

## Incidente registrado (I10)

A primeira redação do exemplo trabalhado (δ = 10⁻⁶) afirmava
g₁₇₀/2 ≈ 1,004·10⁻⁶ > δ (n = 170 identificável). O braço numérico mediu
g₁₇₀/2 = 9,9559·10⁻⁷ < δ: n = 170 já é ambíguo, embora as cotas I e J sejam
silenciosas ali. Texto corrigido; incidente preservado — dentro da fresta
entre as cotas, só o cálculo decide, inclusive contra o autor.
