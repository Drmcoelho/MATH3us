# Capítulo 2 — Verificação simbólica (braço 1 do oráculo triplo)

Data: 28/07/2026. Hipóteses globais: n inteiro ímpar, n ≥ 3;
L = (n² − 1)/2; R = (n² + 1)/2. Domínio conferido em cada passo.
Os itens S1–S7 seguem a ordem lógica do contrato editorial (MATH3us.md §3).

## S1. Direta: n² + L² = R², com R − L = 1 (contrato, item 1)

Inteireza: n ímpar ⟹ n² ímpar ⟹ n² − 1 e n² + 1 pares ⟹ L, R ∈ ℤ.
Positividade: n ≥ 3 ⟹ L ≥ 4 > 0. Folga: R − L = [(n²+1) − (n²−1)]/2 = 1.

    R² − L² = (R − L)(R + L) = 1 · (L + R) = (n² − 1)/2 + (n² + 1)/2 = n².

Logo n² + L² = R².                                                        ∎

Cateto maior: 2(L − n) = n² − 2n − 1 = (n − 1)² − 2 ≥ 4 − 2 = 2 > 0 para
n ≥ 3; em n = 1, L = 0 (degenerado, fora do domínio por hipótese).

## S2. Recíproca e classificação (contrato, item 2)

Hipótese: a, b, c inteiros positivos, a² + b² = c², c = b + 1.

    a² = c² − b² = (c − b)(c + b) = c + b = 2b + 1.

a² ímpar ⟹ a ímpar (o quadrado de um par é par). Isolando:
b = (a² − 1)/2, c = (a² + 1)/2 — a forma da família com n = a.
a = 1 daria b = 0 (não positivo), logo a ≥ 3.
Bijeção: n ↦ (n, L, R) e (a, b, c) ↦ a são inversas — partindo de n a
leitura devolve n; partindo da terna, b e c ficam determinados por a
(cálculo acima), e a regra os reconstrói. Injetividade e sobrejetividade
simultâneas.                                                              ∎

Domínio conferido: a divisão por 2 em b = (a² − 1)/2 é legítima porque
a² − 1 é par (a ímpar). Nenhuma hipótese de primitividade foi usada.

## S3. Primitividade e coprimalidade dois a dois (contrato, item 3; conjectura C1)

    d | L e d | R  ⟹  d | (R − L) = 1.
    d | n e d | L  ⟹  d | n² e d | 2L = n² − 1 ⟹ d | n² − (n² − 1) = 1.
      (Refinamento do fator 2 — exercício E2.2: d | n com n ímpar força
       d ímpar, e para d ímpar, d | 2L ⟺ d | L; a cadeia acima só precisa
       de d | 2L, obtida de d | L por multiplicação, sem divisão alguma.)
    d | n e d | R  ⟹  d | n² e d | 2R = n² + 1 ⟹ d | 1.

Qualquer divisor comum dos três lados divide em particular L e R ⟹ é 1:
terna primitiva.                                                          ∎

## S4. Estrutura modular (contrato, item 4)

n = 2k + 1 ⟹ n² = 4k² + 4k + 1 = 4k(k + 1) + 1. Entre k e k + 1 um é
par ⟹ 2 | k(k + 1) ⟹ 8 | 4k(k + 1) ⟹ n² ≡ 1 (mod 8).
Então 8 | n² − 1 ⟹ 4 | (n² − 1)/2 = L ⟹ L ≡ 0 (mod 4), e
R = L + 1 ≡ 1 (mod 4).                                                    ∎

Recusa dos pares: n par ⟹ n² par ⟹ n² ± 1 ímpar ⟹ (n² ± 1)/2 ∉ ℤ.
A máquina recusa n par por inteireza, não por convenção.

## S5. Medidas (contrato, item 5; conjectura C4)

    P = n + L + R = n + (L + R) = n + n² = n(n + 1).
    s = P/2 = n(n + 1)/2  — inteiro (entre n e n+1 um é par);
      s = 1 + 2 + … + n: a lista somada com sua invertida dá n parcelas
      (1+n), (2+(n−1)), …, todas iguais a n + 1; total n(n+1); metade
      para cada cópia. s é o n-ésimo número triangular.
    K = n·L/2 = n(n² − 1)/4.

Inteireza e paridade de K: por S4, 8 | n² − 1 ⟹ (n² − 1)/4 é inteiro par
⟹ K = n · (n² − 1)/4 é inteiro par.
Divisibilidade por 6 (C4): 4K = (n − 1)·n·(n + 1) contém um múltiplo de 3
(janela de três consecutivos) ⟹ 3 | 4K e mdc(3, 4) = 1 ⟹ 3 | K; par e
múltiplo de 3 ⟹ 6 | K.                                                    ∎

## S6. Raios (contrato, item 6)

Coordenadas: ângulo reto em C = (0,0); A = (L, 0); B = (0, n).
Hipotenusa: reta n·x + L·y − n·L = 0, com norma √(n² + L²) = R (por S1).

Inscrita — centro (ρ, ρ), tangente aos dois eixos; tangência à hipotenusa:

    (n·L − ρ(n + L))/R = ρ  ⟺  ρ(n + L + R) = n·L  ⟺  ρ = n·L/P
    ρ = n·L/(n(n+1)) = L/(n+1) = (n²−1)/(2(n+1)) = (n − 1)/2 = r.

(Sinal do numerador: ρ < min(n, L)/1 e o centro está do lado da origem;
em n = 3: (12 − 1·7)/5 = 1 = ρ ✓.)

Ex-inscrita oposta ao cateto ímpar — centro (−ρ, ρ), tangente à reta
x = 0 e ao prolongamento de y = 0; tangência à hipotenusa:

    (n·L + ρ(n − L))/R = ρ  ⟺  ρ(R + L − n) = n·L,
    R + L − n = n² − n = n(n − 1)  ⟹  ρ = L/(n − 1) = (n + 1)/2 = r_n.

Logo r_n − r = (n+1)/2 − (n−1)/2 = 1.                                     ∎

Identidades de controle (verificadas exatas pelo braço numérico):
K = r·s   [(n−1)/2 · n(n+1)/2 = n(n²−1)/4]   e
K = r_n·(s − n)   [(n+1)/2 · n(n−1)/2 = n(n²−1)/4];
e r = s − R = (n + L − R)/2 [n + L − R = n − 1].

Ex-raios restantes (exercício E3.1; conjectura C5):
s − L = (n+1)/2, s − R = (n−1)/2;
r_L = K/(s−L) = n(n−1)/2 = s − n;  r_R = K/(s−R) = n(n+1)/2 = s.
Caso geral de C5: em todo triângulo retângulo, r = s − c ⟹
K = r·s = s(s − c) ⟹ r_c = K/(s − c) = s.
Soma: r_n + r_L + r_R = (n+1)/2 + n(n−1)/2 + n(n+1)/2 = (n−1)/2 + n² + 1
= r + 2R.                                                                 ∎

## S7. Leitura euclidiana inversa (contrato, item 7)

u = (n + 1)/2, v = (n − 1)/2 — inteiros (n ímpar), u − v = 1 ⟹ coprimos
(S3, primeiro argumento) e de paridades opostas (consecutivos).

    u² − v² = (u − v)(u + v) = 1 · n = n;
    2uv = [(u + v)² − (u − v)²]/2 = (n² − 1)/2 = L;
    u² + v² = [(u + v)² + (u − v)²]/2 = (n² + 1)/2 = R.

A terna do ímpar n é a terna de Euclides do par (u, v) com u − v = 1.
Recíproca euclidiana: (u² + v²) − 2uv = (u − v)²; a folga entre hipotenusa
e cateto par vale 1 ⟺ (u − v)² = 1 ⟺ u − v = 1 (pois u > v). Subproduto:
em toda terna primitiva, hipotenusa − cateto par é um quadrado perfeito
(ímpar, pois u − v é ímpar por paridades opostas).                        ∎

Domínio conferido: u > v ≥ 1 exige n ≥ 3 (n = 1 daria v = 0, fora da
parametrização primitiva com v ≥ 1).

## Conjecturas restantes (testemunhas simbólicas)

C2 (segundas diferenças): L(n+2) − L(n) = [(n+2)² − n²]/2 = 2n + 2 =
2(n + 1); a diferença das diferenças é 2(n+3) − 2(n+1) = 4, constante.  ∎

C3 (família da folga 2): c = b + 2 ⟹
a² = (c − b)(c + b) = 2(2b + 2) = 4(b + 1) ⟹ 2 | a, a = 2m,
b = m² − 1, c = m² + 1; e (2m)² + (m² − 1)² = (m² + 1)² é identidade
polinomial. Primitividade ⟺ m par: m ímpar ⟹ 2 divide os três lados;
m par ⟹ divisor comum d | (c − b) = 2 e d | b ímpar ⟹ d = 1.            ∎

## O que este documento NÃO estabelece

- A parametrização completa de Euclides (toda primitiva é (u²−v², 2uv,
  u²+v²)): entra **citada** como material clássico (`sources.md`); o
  capítulo demonstra apenas a leitura inversa e a fatia u − v = 1.
- A suficiência de p ≡ 1 (mod 4) para p ser soma de dois quadrados
  (Fermat): porta trancada → Capítulo 7. Aqui só a necessidade
  R ≡ 1 (mod 4) está provada (S4 + S7).
- A classificação das ternas de catetos consecutivos (Pell): porta →
  Capítulo 5 (exercício E4.1).
