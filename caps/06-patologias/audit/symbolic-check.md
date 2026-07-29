# Capítulo 6 — Verificação simbólica (braço 1 do oráculo triplo)

Derivações algébricas explícitas das provas do capítulo, conferidas à mão em
28/07/2026. Cada bloco declara hipóteses e domínio. Os braços 2 e 3 estão em
`numeric-check.json` e `edge-cases.md` (script `oracle.py`).

## S1 — Irracionalidade de √2 (seção 5.1)

Hipótese: p/q reduzida (mdc(p,q) = 1, q ≥ 1) com p² = 2q².
p² par ⟹ p par (se p = 2t+1, p² = 4t²+4t+1 ímpar). p = 2m ⟹ 4m² = 2q²
⟹ q² = 2m² ⟹ q par (mesmo argumento). p e q pares contradiz mdc = 1. ∎
Domínio: aplica-se a qualquer racional; nenhuma hipótese sobre sinal (quadrados
ignoram sinal).

## S2 — Arquimediana e densidade de ℚ (seções 5.2–5.3)

Arquimediana: se s = sup ℕ existisse, s − 1 &lt; s não seria cota superior,
logo ∃n com n &gt; s − 1 ⟹ n + 1 &gt; s com n + 1 ∈ ℕ. Contradição. Dado
ε &gt; 0: n &gt; 1/ε ⟹ 1/n &lt; ε (inversão preserva ordem em positivos).

Densidade: x &lt; y; n com 1/n &lt; y − x; M = {m ∈ ℤ : m &gt; nx} não vazio
e limitado inferiormente; m = min M (boa ordenação, princípio declarado).
Cadeia: nx &lt; m (pertinência) e m − 1 ≤ nx (minimalidade) ⟹
m ≤ nx + 1 &lt; nx + n(y − x) = ny. Divisão por n &gt; 0 preserva:
x &lt; m/n &lt; y. ∎

## S3 — Densidade dos irracionais (seção 5.4)

x − √2 &lt; r &lt; y − √2 (por S2) ⟹ x &lt; r + √2 &lt; y (somar √2 preserva
ordem). Se w = r + √2 = a/b então √2 = a/b − r ∈ ℚ, contra S1. ∎
Também usado no oráculo (I1): testemunha w = a + √2/n com certificado
√2/n &lt; b − a ⟺ 2 &lt; n²(b − a)² (elevar ao quadrado preserva ordem em
positivos); irracionalidade de √2/n idem S3.

## S4 — Dirichlet descontínua em todo ponto (seção 5.5)

ε₀ = 1/2. Para todo δ, (a − δ, a + δ) contém racional r e irracional w
(S2, S3). a ∈ ℚ ⟹ |D(w) − D(a)| = |0 − 1| = 1 ≥ 1/2;
a ∉ ℚ ⟹ |D(r) − D(a)| = |1 − 0| = 1 ≥ 1/2. A negação da continuidade fica
realizada com o mesmo ε₀ em todos os pontos. ∎

## S5 — Thomae (seção 5.6)

Descontinuidade em a = p/q reduzida: ε₀ = 1/q; todo δ-intervalo contém
irracional w; |T_h(w) − T_h(a)| = 1/q ≥ ε₀. ∎

Continuidade em a irracional: Q &gt; 1/ε (S2). Violadores (T_h ≥ ε) têm
q ≤ Q (1/q ≥ ε ⟺ q ≤ 1/ε). F = frações reduzidas com q ≤ Q em
(a − 1, a + 1): para cada q, p ∈ (q(a−1), q(a+1)), intervalo de comprimento
2q ⟹ no máximo 2q + 1 inteiros; |F| ≤ Σ_{q≤Q}(2q+1) = Q² + 2Q, finito.
a ∉ F (a irracional) ⟹ δ = min{|a − r| : r ∈ F} &gt; 0 (mínimo de conjunto
FINITO de positivos é positivo — o passo insubstituível). Para |x − a| &lt; δ
(e &lt; 1): x irracional ⟹ |ΔT_h| = 0 &lt; ε; x = p/q reduzida ⟹ p/q ∉ F
mas p/q ∈ (a−1, a+1) ⟹ q &gt; Q ⟹ 1/q &lt; 1/Q &lt; ε. ∎

## S6 — A serra é 1-Lipschitz (seção 5.7)

s(x) = min_n |x − n|, atingido. n_y realiza s(y):
s(x) ≤ |x − n_y| ≤ |x − y| + |y − n_y| = |x − y| + s(y). Simetria em x, y
fecha |s(x) − s(y)| ≤ |x − y|. Cotas: 0 ≤ s ≤ 1/2 (o inteiro mais próximo
dista no máximo 1/2). Continuidade: δ = ε.

## S7 — Lema dos declives diádicos (seção 5.8)

I = [j/2^m, (j+1)/2^m]. Termos k ≥ m: 2^k·(j/2^m) = j·2^{k−m} ∈ ℤ e idem
para j + 1 ⟹ s = 0 nos dois extremos ⟹ incremento 0. (Consequência: em
pontos diádicos a série de T é soma finita — exatidão computacional do
oráculo, rota A.)

Termos k &lt; m: 2^k·I = [j/2^{m−k}, (j+1)/2^{m−k}], comprimento
2^{k−m} ≤ 1/2, extremos múltiplos consecutivos de 2^{k−m}. Como 2^{k−m}
divide 1/2, os semi-inteiros são múltiplos de 2^{k−m}; múltiplos consecutivos
não têm semi-inteiro no interior ⟹ 2^k·I cabe numa única rampa da serra.
Rampa de subida ⟺ frac(j/2^{m−k}) &lt; 1/2 ⟺ bit m−k−1 de j é 0.
Declive do termo: (±1 · 2^k)/2^k = ε_k. Soma: S_m(j) = Σ_{k&lt;m} ε_k.

Filhos: dígitos de 2j em janela m+1 = dígitos de j + [0] ⟹ S+1; de
2j+1 = dígitos de j + [1] ⟹ S−1. Metades diferem por (S+1)−(S−1) = 2 (C4).
Em j = 0: todos os bits 0 ⟹ S_m = m; T(0) = 0 ⟹ quociente = m (C3).
Soma parcial T_N em profundidade N: só termos rasos, todos lineares ⟹ linear.

## S8 — Lema do aperto (seção 5.9)

Diferenciabilidade em x: |f(y) − f(x) − f′(x)(y − x)| ≤ ε|y − x| para
|y − x| &lt; δ (inclui y = x: 0 ≤ 0). Para a ≤ x ≤ b, b − a &lt; δ:
f(b) − f(a) − f′(x)(b − a)
  = [f(b) − f(x) − f′(x)(b − x)] − [f(a) − f(x) − f′(x)(a − x)]
(identidade algébrica: os f(x) e os f′(x)x cancelam). Valor absoluto
≤ ε(b − x) + ε(x − a) = ε(b − a); dividir por b − a &gt; 0. ∎

## S9 — Não diferenciabilidade de T (seção 5.10)

j_m = ⌊2^m x⌋ ⟹ j_m ≤ 2^m x &lt; j_m + 1 ⟹ x ∈ I_m, |I_m| = 2^{−m} → 0.
Duplicando: 2j_m ≤ 2^{m+1}x &lt; 2j_m + 2 ⟹ j_{m+1} ∈ {2j_m, 2j_m + 1}
⟹ (S7, filhos) |S_{m+1} − S_m| = 1. Se T′(x) existisse, S8 daria
S_m → T′(x); Cauchy com ε = 1/2 exigiria |S_{m+1} − S_m| &lt; 1/2 para m
grande. Contradição com o passo constante 1. ∎

## S10 — Preservação de sinal e TVI (seção 5.11)

Preservação: ε = g(c)/2 ⟹ g(x) &gt; g(c) − g(c)/2 = g(c)/2 &gt; 0 no δ-viz.
TVI: g = f − u reduz ao caso g(a) &lt; 0 &lt; g(b); c = sup A,
A = {x : g(x) &lt; 0}. g(c) &gt; 0 ⟹ A ⊆ (−∞, c−δ] ⟹ cota menor: contra.
g(c) &lt; 0 ⟹ c &lt; b e ∃t ∈ (c, c+δ)∩[a,b] com g(t) &lt; 0 ⟹ t ∈ A,
t &gt; c: contra. Resta g(c) = 0. Falha em ℚ: g(x) = x² − 2 em [1,2]∩ℚ,
g(1) = −1, g(2) = 2, zero exigiria quadrado 2 (S1). ∎

## S11 — O buraco de ℚ (seção 5.12)

r &gt; 0 racional. Identidades (expansão direta):
r′ = r/2 + 1/r ⟹ r′² − 2 = r²/4 + 1 + 1/r² − 2 = (r⁴ − 4r² + 4)/(4r²)
  = (r² − 2)²/(4r²);   r − r′ = r/2 − 1/r = (r² − 2)/(2r).
t = (2r+2)/(r+2) ⟹ t − r = (2r + 2 − r² − 2r)/(r+2) = (2 − r²)/(r+2);
t² − 2 = (4r² + 8r + 4 − 2r² − 8r − 8)/(r+2)² = (2r² − 4)/(r+2)²
  = 2(r² − 2)/(r+2)².
Caso r² &gt; 2: r′ &lt; r, r′² &gt; 2, e r′ é cota (x &gt; r′ &gt; 0 ⟹
x² &gt; r′² &gt; 2). Caso r² &lt; 2: t &gt; r, t² &lt; 2 ⟹ t ∈ A. Caso
r² = 2: S1. Nenhuma menor cota racional existe. ∎
Cadeias numéricas: 3/2 → 17/12 → 577/408 (excessos 1/4, 1/144, 1/166464);
1 → 4/3 → 7/5 (déficits 2/9, 1/25) — conferidas em frações exatas (I6).

## S12 — Todo float é racional (seção 7)

Float finito IEEE-754 = ±M·2^E com M, E inteiros (definição do formato)
= ±M·2^E/1 ou ±M/2^{−E}: quociente de inteiros. Exemplos exatos:
0,1 ↦ 3602879701896397/2^55; float(√2/2) = 6369051672525773/2^53. ∎

## S13 — T(1/3) = 2/3 (gabarito E2.2; invariante I4)

frac(2^k/3) alterna 1/3, 2/3 (indução: 2·(1/3) = 2/3; 2·(2/3) = 4/3 ≡ 1/3);
s = 1/3 nos dois casos. T(1/3) = (1/3)·Σ 2^{−k}; soma parcial
Σ_{k&lt;N} 2^{−k} = 2 − 2^{1−N} (indução), crescente, limitada por 2, converge
a 2 (convergência monótona, Cap. 1; ε-N explícito por S2). Logo 2/3. Cauda
exata: Σ_{k≥N} (1/3)2^{−k} = (1/3)2^{1−N}, e parcial + cauda = 2/3 exatamente
(conferido em frações, I4).
