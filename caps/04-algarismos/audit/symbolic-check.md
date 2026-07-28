# Capítulo 4 — Verificação simbólica (braço 1 do oráculo triplo)

Data: 28/07/2026. Hipóteses globais: a ≥ 0, d ≥ 1 inteiros; base inteira
b ≥ 2; salvo menção, a/d **reduzida** (gcd(a, d) = 1). Máquina do
Enunciado A: q = ⌊a/d⌋, r₀ = a mod d, u_k = ⌊b·r_{k−1}/d⌋,
r_k = b·r_{k−1} − d·u_k.

## S1. O invariante da máquina

Indução em k. Base k = 0: a = d·q + r₀ é a divisão euclidiana. Passo:
supondo a·b^k = d·(q·b^k + U_k) + r_k com U_k = u₁b^{k−1} + ⋯ + u_k,
multiplique por b e substitua b·r_k = d·u_{k+1} + r_{k+1}:

    a·b^{k+1} = d·(q·b^{k+1} + b·U_k) + b·r_k
              = d·(q·b^{k+1} + b·U_k + u_{k+1}) + r_{k+1}
              = d·(q·b^{k+1} + U_{k+1}) + r_{k+1}.                        ∎

Corolário usado em toda parte: r_k = a·b^k mod d. Domínio conferido:
0 ≤ u_k ≤ b−1 pois 0 ≤ r_{k−1} ≤ d−1 ⟹ 0 ≤ b·r_{k−1} ≤ b·d − b < b·d.

## S2. A expansão só vê o valor (Enunciado C)

Do invariante, U_k = ⌊(a mod d)·b^k/d⌋: expressão função apenas do número
real (a mod d)/d. Pares (a, d), (a′, d′) com a·d′ = a′·d têm a mesma parte
inteira e o mesmo (a mod d)/d, logo os mesmos U_k para todo k, logo os
mesmos algarismos u_k = U_k − b·U_{k−1}.                                  ∎

Contraexemplo de proteção (necessidade da redução no Enunciado B):
3/6 = 1/2 termina na base 10 embora 3 | 6 e 3 ∤ 10; 2/6 = 1/3 não termina.
Mesmo denominador bruto, comportamentos opostos — o critério lê o
denominador reduzido, único representante canônico do valor.

## S3. Critério de terminação (Enunciado B), as duas direções

(ii) ⟹ (i): d | b^k ⟹ r_k = a·b^k mod d = 0 (S1): a máquina para em ≤ k
passos. Construtivamente, a/d = a·(b^k/d)/b^k tem numerador inteiro.

(i) ⟹ (ii): parada no passo k ⟹ d | a·b^k (S1). Lema de Euclides–Gauss:
d | a·m com gcd(a, d) = 1 ⟹ d | m — prova por valuações (TFA): para todo
primo p, v_p(d) ≤ v_p(a) + v_p(m) e v_p(d) > 0 ⟹ v_p(a) = 0, logo
v_p(d) ≤ v_p(m). Com m = b^k: d | b^k.

(ii) ⟺ (iii): p | d e d | b^k ⟹ p | b^k ⟹ p | b (primalidade).
Reciprocamente, primos de d todos em b: d = ∏pᵢ^{eᵢ} | b^E com
E = max eᵢ, pois pᵢ^{eᵢ} | pᵢ^E | b^E e os pᵢ^{eᵢ} são coprimos
dois a dois.                                                              ∎

## S4. Lema de herança: algarismos ↔ restos (mesma periodicidade)

Se u_{k+t} = u_k para todo k > i, então de S1 (aplicado a partir de i):

    r_{i+k} − r_{i+t+k} = b^k·(r_i − r_{i+t})   para todo k ≥ 0,

pois as somas de algarismos coincidem e cancelam. |esquerda| < d fixo;
|direita| = b^k·|r_i − r_{i+t}| → ∞ se r_i ≠ r_{i+t}. Logo r_i = r_{i+t}:
períodos (e pré-períodos) mínimos de algarismos e restos coincidem.
Nenhuma série infinita usada.                                             ∎

## S5. Caso coprimo: período = ord_d(b) (Enunciado D)

gcd(d, b) = 1, gcd(a, d) = 1, d > 1. r_k = a·b^k mod d é invertível
módulo d (produto de invertíveis) ⟹ nunca 0 ⟹ não termina. Casas de
pombo em {1, …, d−1} ⟹ retorno. Equação do retorno:

    r_i = r_j  ⟺  a·b^i(b^{j−i} − 1) ≡ 0 (mod d)  ⟺  b^{j−i} ≡ 1 (mod d),

cancelando a e b^i (invertíveis — as duas coprimalidades são exatamente
as hipóteses). Menor retorno: t = ord_d(b), que existe pois algum retorno
existe. Com i = 0: puramente periódica. Independe de a (a foi cancelado).
Por S4 o período dos algarismos é o mesmo.                                ∎

## S6. Caso geral: cisão d = d_b·d′ (Enunciado E)

d_b = parte de d com primos que dividem b; d′ = resto; gcd(d_b, d′) = 1,
gcd(d′, b) = 1. Coprimalidades estruturais: gcd(d_b, b^t − 1) = 1 (primo
comum dividiria b^t e b^t − 1, logo 1); gcd(d′, b^i) = 1. Então:

    r_i = r_{i+t} ⟺ d | b^i(b^t − 1)   [Euclides–Gauss remove a]
                  ⟺ d_b | b^i  e  d′ | b^t − 1   [separação pelas coprimalidades]

Menor i: ν = min{k : d_b | b^k}; como d_b | b^k ⟺ ∀p | d_b:
v_p(d) ≤ k·v_p(b), vale ν = max_p ⌈v_p(d)/v_p(b)⌉. Menor t ≥ 1:
ord_{d′}(b) se d′ > 1. Se d′ = 1: d = d_b | b^ν ⟹ r_ν = 0, e
r_{ν−1} ≠ 0 porque d ∤ b^{ν−1} (minimalidade de ν) e Euclides–Gauss —
termina em exatamente ν algarismos. Pré-período mínimo ν, período mínimo
ord_{d′}(b), independentes de a; por S4 valem para os algarismos.
S3 é o caso d′ = 1; S5 é o caso d_b = 1.                                  ∎

## S7. Consequências por base e fuga dos primos

Corolário (bases do contrato): denominadores finitos na base 10 = 2·5 são
d = 2^i5^j; na base 12 = 2²·3, d = 2^i3^j; na base 60 = 2²·3·5,
d = 2^i3^j5^k — leitura direta de S3(iii).

Euclides (IX.20, prova curta): dada lista finita p₁…p_n, todo fator primo
q de p₁⋯p_n + 1 está fora da lista (q | 1 seria absurdo). Infinitos
primos.                                                                   ∎

Fuga: b tem finitos fatores primos (TFA) ⟹ existe primo p ∤ b (Euclides)
⟹ 1/p infinita na base b (S3) — e são infinitos tais p. Deslocamento sem
eliminação: para d ≥ 2, a base b = d dá d | b¹ (finita); nenhuma base
elimina a fronteira.                                                      ∎

## S8. Permutações cíclicas (full-reptend)

p primo, ord_p(b) = p − 1, B = (b^{p−1} − 1)/p. (a) B é o bloco de 1/p:
invariante em k = p − 1 com r_{p−1} = r₀ = 1 dá b^{p−1} = p·U_{p−1} + 1,
U_{p−1} = B. (b) O ciclo de restos de 1/p percorre todo m ∈ {1, …, p−1}
(ordem máxima); no ponto k com b^k ≡ m (mod p), o determinismo da máquina
faz o bloco de m/p ser a rotação de B por k. (c) O bloco de m/p, como
inteiro, é m·B: invariante para m/p em k = p − 1, m·b^{p−1} = p·U + m ⟹
U = m·B. (d) Defasagens k distintas para m distintos (bijeção
k ↦ b^k mod p no ciclo): p − 1 múltiplos ↔ p − 1 rotações.               ∎

Caso p = 7, b = 10: B = 142857; as seis contas do capítulo são instâncias.
Sem ordem máxima a transitividade quebra: 13 (ord = 6 < 12) parte os
restos em 12/6 = 2 ciclos (exercício E3.2) — verificado no braço numérico.

## Simplificação simbólica independente

As cadeias S1–S8 foram conferidas passo a passo por manipulação algébrica
explícita (acima). O braço numérico (`numeric-check.json`) compara a
máquina real com as previsões de S6 em todos os a/d reduzidos com
d ≤ 2000 e sete bases (I1–I4), e testa S8 diretamente (I5). As
verificações são independentes: esta é álgebra; aquela é execução em duas
implementações distintas.

## O que este documento NÃO estabelece

- O estatuto **analítico** das expansões infinitas (em que sentido a
  escrita 0,333… denota 1/3): exige limites e séries — Capítulo 9. Aqui
  toda afirmação sobre expansões é sobre o fluxo de algarismos produzido
  pela máquina, com provas finitas (S4 evita séries de propósito).
- A infinitude dos primos full-reptend (Artin): problema aberto, porta
  declarada (E4.1).
- A explicação estrutural de 1/998001 (série geométrica ao quadrado):
  Capítulo 10. O oráculo registra apenas as ordens-testemunha (W1).
