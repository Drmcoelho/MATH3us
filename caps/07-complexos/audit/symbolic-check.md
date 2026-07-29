# Capítulo 7 — Verificação simbólica (braço 1 do oráculo triplo)

Data: 28/07/2026. Hipóteses globais: pares ordenados de reais com
(a, b) + (c, d) = (a + c, b + d) e (a, b)·(c, d) = (ac − bd, ad + bc);
i = (0, 1); N(a + bi) = a² + b²; seno e cosseno em estatuto geométrico
(círculo unitário — E11), com as definições escolares em razões fixadas
antes do primeiro uso (E22). Domínio conferido em cada passo.

## S1. Axiomas de corpo (Teorema 1)

Comutatividade do produto: (ac − bd, ad + bc) = (ca − db, cb + da) — comutatividade
de · e + em ℝ, termo a termo.

Associatividade: [(a,b)(c,d)](e,f) tem primeira coordenada
(ac − bd)e − (ad + bc)f = ace − bde − adf − bcf; e (a,b)[(c,d)(e,f)] tem
a(ce − df) − b(cf + de) = ace − adf − bcf − bde. Iguais. Segunda coordenada:
(ac − bd)f + (ad + bc)e = acf − bdf + ade + bce; e
a(cf + de) + b(ce − df) = acf + ade + bce − bdf. Iguais.

Distributividade: (a,b)[(c,d) + (e,f)] = (a(c+e) − b(d+f), a(d+f) + b(c+e))
= (ac − bd, ad + bc) + (ae − bf, af + be). ✓

Neutros: (a,b)+(0,0) = (a,b); (a,b)(1,0) = (a·1 − b·0, a·0 + b·1) = (a,b).
Oposto: (−a, −b). i² = (0·0 − 1·1, 0·1 + 1·0) = (−1, 0). ✓

Inverso: z z̄ = (a + bi)(a − bi) = a² − (bi)² = a² + b² = N(z); para z ≠ 0,
N(z) > 0 (soma de quadrados reais com um deles ≠ 0) e z·(z̄/N(z)) = 1.
Domínio: a divisão por N(z) exige exatamente z ≠ 0 — declarado. ∎

Sem divisores de zero: zw = 0, z ≠ 0 ⟹ w = z⁻¹·0 = 0.

Rota independente (espelhada no oráculo I1): a representação matricial
a + bi ↦ [[a, −b], [b, a]] transforma o produto complexo no produto de
matrizes; a associatividade herda-se da associatividade matricial.

## S2. Norma multiplicativa = identidade de Brahmagupta (Teorema 2)

(ac − bd)² + (ad + bc)²
= a²c² − 2abcd + b²d² + a²d² + 2abcd + b²c²
= a²c² + a²d² + b²c² + b²d² = (a² + b²)(c² + d²). ∎

Rota estrutural: conj(zw) = z̄·w̄ (conta em E2.1 do capítulo);
N(zw) = zw·conj(zw) = (z z̄)(w w̄) = N(z)N(w).

## S3. Rotação em coordenadas e multiplicação como rotação-escala (Lema 3, Teorema 4)

Fatos geométricos importados e declarados: rotação em torno da origem é
linear (preserva paralelogramos e escalas); R_θ(1,0) = (cos θ, sen θ)
(definição do círculo); o quarto de volta leva (p, q) a (−q, p).

R_θ(x, y) = x·R_θ(1,0) + y·R_θ(0,1) = x·(cos θ, sen θ) + y·(−sen θ, cos θ)
= (x cos θ − y sen θ, x sen θ + y cos θ).

Multiplicação: (cos θ + i sen θ)(x + iy)
= (x cos θ − y sen θ) + i(x sen θ + y cos θ) — as mesmas coordenadas. Para
w = s(cos φ + i sen φ), s > 0: w·z = s·(u·z), escala ∘ rotação. ∎

## S4. Fórmulas de adição (Teorema 5) — derivadas, não importadas

R_α ∘ R_β = R_{α+β} (composição de giros soma ângulos — fato geométrico
declarado). Aplicando ao 1 via Teorema 4:

(cos α + i sen α)(cos β + i sen β) = cos(α + β) + i sen(α + β).

Expansão do lado esquerdo pela regra do produto:
(cos α cos β − sen α sen β) + i(sen α cos β + cos α sen β).
Igualdade de pares ⟹ as duas fórmulas, coordenada a coordenada. ∎

## S5. De Moivre (Teorema 7)

Indução: caso n = 1 trivial; passo usa S4 com α = nθ, β = θ:
(cos θ + i sen θ)^{n+1} = (cos nθ + i sen nθ)(cos θ + i sen θ)
= cos(n+1)θ + i sen(n+1)θ. ∎

## S6. Raiz n-ésima real positiva (Lema 8)

Unicidade: t ↦ tⁿ estritamente crescente em (0, ∞). Existência: r = sup A,
A = {t > 0 : tⁿ ≤ s} (não vazio: min(1, s); limitado: 1 + s). Cotas por
fatoração de diferença de potências:
(r+h)ⁿ − rⁿ = h·Σ_{j<n} (r+h)^{n−1−j} r^j ≤ h·n·(r+1)^{n−1}  (0 < h ≤ 1),
rⁿ − (r−h)ⁿ = h·Σ_{j<n} r^{n−1−j}(r−h)^j ≤ h·n·r^{n−1}.
rⁿ < s contradiz supremo (r + h ∈ A para h pequeno); rⁿ > s contradiz
minimalidade da cota (r − h ainda cota). Logo rⁿ = s. Dependência declarada:
princípio do supremo — chapter-01.supremum-principle (capítulo fechado). ∎

## S7. As n raízes (Teorema 9) e a soma zero (Teorema 10, C3)

z_k = s^{1/n}(cos((φ + 2kπ)/n) + i sen((φ + 2kπ)/n)), k = 0..n−1.
(i) z_kⁿ = s(cos(φ + 2kπ) + i sen(φ + 2kπ)) = w (S5 + periodicidade).
(ii) distintas: argumentos diferem por 2π(k′−k)/n ∈ (0, 2π).
(iii) completas: |z|ⁿ = s ⟹ |z| = s^{1/n} (S6, unicidade); nα ≡ φ (mod 2π)
⟹ α = (φ + 2mπ)/n; m = qn + k (divisão euclidiana) ⟹ z = z_k.
(iv) polígono regular: módulo comum, passos angulares iguais 2π/n.
Degenerado declarado: w = 0 ⟹ |z|ⁿ = 0 ⟹ z = 0, raiz única.

Soma: z_k = z₀ ωᵏ com ω = cos(2π/n) + i sen(2π/n);
(ω − 1)(1 + ω + … + ω^{n−1}) = ωⁿ − 1 = 0 e ω ≠ 1 para n ≥ 2 ⟹ soma dos
ωᵏ nula ⟹ S = 0. Domínio: n ≥ 2 (n = 1 tem soma w ≠ 0). ∎

## S8. Custo do ramo (Teorema 11, C5)

arg z = {θ₀ + 2kπ}; Arg z ∈ (−π, π] (escolha declarada). Arg z + Arg w e
Arg(zw) pertencem ambos a arg(zw) (lei de conjuntos, S3/S4) ⟹ diferem por
2mπ. Cotas: soma ∈ (−2π, 2π], Arg(zw) ∈ (−π, π] ⟹ diferença ∈ (−3π, 3π)
⟹ m ∈ {−1, 0, 1}. Ocorrência dos três valores: (1)(1); (−1 + εi)²;
(−1 − εi)². ∎

## S9. ℤ[i]: unidades (Teorema 12) e divisão (Teorema 13)

Unidades: uv = 1 ⟹ N(u)N(v) = 1 em inteiros ≥ 0 ⟹ N(u) = 1 ⟹
a² + b² = 1 ⟹ u ∈ {±1, ±i}; os quatro invertem-se mutuamente.

Divisão: z/d = z d̄ / N(d) = x + yi, x, y ∈ ℚ; m, n inteiros mais próximos
(|x − m| ≤ 1/2, |y − n| ≤ 1/2 — sempre existem; empates resolvidos por
escolha declarada); q = m + ni, r = z − qd = d((x−m) + (y−n)i);
N(r) = N(d)((x−m)² + (y−n)²) ≤ N(d)(1/4 + 1/4) = N(d)/2 < N(d).
Domínio: d ≠ 0 (divisão por zero recusada — caso adversarial A2). ∎

## S10. Cadeia euclidiana em ℤ[i] (seção 9.3)

Elo 1 (mdc): normas dos restos estritamente decrescentes em ℕ ⟹ o
algoritmo para; o último resto não nulo divide os dois de partida (subida)
e é dividido por todo divisor comum (descida).
Elo 2 (Bézout): cada resto é combinação x·α + y·β — indução na cadeia.
Elo 3 (lema de Euclides): π primo, π | αβ, π ∤ α ⟹ mdc(π, α) é unidade ⟹
1 = xπ + yα ⟹ β = xπβ + y(αβ), ambos múltiplos de π ⟹ π | β. ∎

## S11. Wilson (Teorema 14) e a testemunha (Teorema 15)

Wilson: em {1, …, p−1}, cada a tem inverso único (Bézout em ℤ);
a = a⁻¹ ⟺ p | (a−1)(a+1) ⟺ a ≡ ±1. Os demais formam pares {a, a⁻¹} de
produto 1: (p−1)! ≡ 1·(p−1) ≡ −1 (mod p). Conferências: 4! = 24 ≡ −1
(mod 5); 6! = 720 ≡ −1 (mod 7).

Testemunha: (p−1)! = Π_{k=1}^{(p−1)/2} k(p − k) ≡ Π k(−k)
= (−1)^{(p−1)/2} m², m = ((p−1)/2)!. Se p ≡ 1 (mod 4), o expoente é par:
m² ≡ (p−1)! ≡ −1. (Se p ≡ 3 (mod 4), expoente ímpar: m² ≡ +1 — contraste
verificado no oráculo I7.) Conferência: p = 13, m = 6! ≡ 5, 5² = 25 ≡ −1. ∎

## S12. Dois quadrados (Teorema 16), algoritmo do mdc (C2) e classificação (Teorema 17)

Ida: p ≡ 1 (mod 4) ⟹ ∃m: p | m² + 1 = (m + i)(m − i) (S11). p primo
gaussiano dividiria m ± i (S10, Elo 3), mas (m ± i)/p tem parte imaginária
±1/p ∉ ℤ. Logo p = πσ, não trivial; N(π)N(σ) = p², ambos > 1 ⟹
N(π) = p ⟹ π = a + bi com a² + b² = p.

Volta: quadrados mod 4 ∈ {0, 1} ⟹ a² + b² mod 4 ∈ {0, 1, 2} ∌ 3.
p = 2 = 1² + 1² à mão; 2 = −i(1 + i)² ramifica.

Algoritmo (C2): π | (m+i)(m−i) ⟹ (trocando π ↔ σ̄ = conjugado de norma p
se preciso) π | m + i; π | p; nenhum divisor comum maior: p ∤ m + i (parte
imaginária 1/p) e N(m + i) = m² + 1 satisfaz p | m² + 1, p² ∤ m² + 1
(m ≤ p − 1 ⟹ m² + 1 ≤ p² − 2p + 2 < p²) ⟹ o mdc tem norma exatamente p.

Classificação: (a) N(z) primo ⟹ divisor próprio teria norma própria
dividindo primo — impossível. (c) p ≡ 3 (mod 4): fatoração não trivial
exigiria N(α) = p = a² + b², vetado pela volta. (d) p ≡ 1: ida + (a);
σ = π̄ por cancelamento em π π̄ = N(π) = p = π σ. (e) C4: z primo fora dos
eixos divide N(z) = Π q_j ⟹ z | q (Elo 3 iterado) ⟹ N(z) ∈ {q, q²};
N(z) = q² ⟹ z associado de q (γ = q/z tem norma 1) ⟹ z nos eixos —
contradição; logo N(z) = q primo. ∎

## Unicidade (C1 — exercício E3.1)

p = a² + b² = c² + d² (0 < a ≤ b, 0 < c ≤ d, mdc(a,b) = mdc(c,d) = 1).
(ac + bd)(ac − bd) = a²c² − b²d² = a²(c² + d²) − d²(a² + b²) = p(a² − d²)
⟹ p | (ac + bd)(ac − bd) ⟹ (Euclides em ℤ) p divide um fator.
p² = (ac + bd)² + (ad − bc)² = (ac − bd)² + (ad + bc)² (duas formas de S2).
Caso p | ac − bd: p | ad + bc (da segunda forma); dividindo por p²,
soma de dois quadrados inteiros = 1 ⟹ ac = bd ⟹ (coprimalidades) c = b,
d = a. Caso p | ac + bd: simetricamente ad = bc ⟹ c = a, d = b.
Em ambos, {a, b} = {c, d}. ∎
