# Capítulo 0 — A Inferência · Pré-registro de conjecturas

**Tipo declarado:** território virgem.
**Data do pré-registro:** 28/07/2026.
**Estatuto (§1.3):** território virgem — não existe descoberta pessoal anterior
suficientemente formada para escavação. A ideia nasceu em 28/07/2026, na crítica
do leitor primário ao Capítulo 1 implementado (documento registrado em
`sources.md`): a configuração dual — duas circunferências e um polígono — e o
triângulo fundamental R, r, L/2 que aquele capítulo havia omitido. Para todas as
conjecturas abaixo o pré-registro vale com **força probatória plena**: nenhuma
foi verificada (numérica ou simbolicamente) antes deste commit. As derivações
mencionadas são esboços de caminho, não provas conferidas; o oráculo decidirá.

---

## Pergunta central (registrada antes do desenvolvimento)

> Todo polígono regular carrega duas circunferências — a inscrita (raio r, o
> apótema) e a circunscrita (raio R). **O que esse par de circunferências sabe
> sobre o polígono?** Se eu só puder medir r e R — com erro — o que posso
> inferir: quantos lados, que tamanho, com que certeza? E onde a inferência
> **morre**?

Contexto: o Capítulo 1 cerca uma circunferência com dois polígonos. Este
prólogo inverte o cerco: duas circunferências aprisionam um polígono. A
restrição editorial fixada em E20: tudo por desigualdades explícitas, sem
linguagem de limite — os limites pertencem ao Capítulo 1.

Notação: θ = π/n é o semiângulo central; ρ_n = r/R = cos(π/n); L é o lado;
g_n = ρ_{n+1} − ρ_n é a folga entre razões consecutivas. π entra como constante
da área do disco (E20), não como número construído.

---

## Conjecturas

### C0.1 — Suficiência do par
**Enunciado:** o par (r, R) determina o polígono regular a menos de rotação em
torno do centro comum. Especificamente: ρ_n = cos(π/n) é estritamente crescente
em n ≥ 3, de ρ_3 = 1/2 rumo a 1; logo n é recuperável da razão, e L = 2√(R² − r²)
fecha a reconstrução. Uma circunferência sozinha (r ou R isolado) não determina
nada sobre n: todo raio serve a todo n. E o par concêntrico (r, R) é realizado
por um polígono regular **se, e somente se**, r/R ∈ {cos(π/n) : n ≥ 3} — conjunto
discreto; razões abaixo de 1/2 refutam a hipótese "isto são as circunferências
de um polígono regular".
**Confiança inicial:** alta.
**Exemplos disponíveis no registro:** ρ_3 = 1/2; ρ_4 = √2/2 ≈ 0,7071;
ρ_6 = √3/2 ≈ 0,8660 — crescente nos casos calculáveis à mão.
**Refutadores possíveis:** dois inteiros n ≠ m com cos(π/n) = cos(π/m); par
(r, R) com razão admissível não realizado por polígono.

### C0.2 — A identidade da coroa
**Enunciado:** a coroa circular entre as duas circunferências tem área igual à
do círculo de raio L/2: C·R² − C·r² = C·(L/2)², onde C é a constante da área do
disco. Equivale a Pitágoras no triângulo fundamental OMV e vale **qualquer que
seja C** — o capítulo não precisa do valor de π.
**Confiança inicial:** alta (é Pitágoras vestido).
**Refutadores possíveis:** qualquer n com discrepância numérica entre área da
coroa e C(L/2)²; falha do triângulo OMV em algum n.

### C0.3 — Sanduíche do déficit (quadrático)
**Enunciado:** para todo n ≥ 3,
(π²/2n²)·ρ_{2n}² ≤ 1 − ρ_n ≤ π²/2n²,
com igualdade em nenhum n. O fator de correção do lado esquerdo é a razão do
polígono de **2n** lados ao quadrado — a sequência controla o próprio erro.
Caminho esboçado (não conferido): 1 − cos x = 2 sen²(x/2) com x = π/n, e a
desigualdade da cunha y·cos y < sen y < y.
**Confiança inicial:** média-alta.
**Refutadores possíveis:** violação numérica em qualquer n ≥ 3 (o lado esquerdo
parece apertado; se falhar, falhará ali).

### C0.4 — Sanduíche da folga (cúbico)
**Enunciado:** para todo n ≥ 3,
π²·ρ_n/(n(n+1)²) < g_n < π²/n³.
Caminho esboçado (não conferido): cos A − cos B em produto de senos; no meio da
derivação deve aparecer a identidade exata cos α · cos β = (ρ_n + ρ_{n+1})/2
para os dois ângulos α, β do produto — se aparecer, é um pequeno presente.
**Confiança inicial:** média-alta.
**Refutadores possíveis:** violação numérica; a identidade do meio não valer.

### C0.5 — Limiar cúbico da identificação
**Enunciado:** medindo ρ com erro absoluto máximo δ e decidindo pelo cos(π/m)
mais próximo: (a) **garantia** — se 2δ < π²·ρ_{n−1}/((n−1)n²) e
2δ < π²·ρ_n/(n(n+1)²), a decisão devolve exatamente n (para n = 3 basta a
segunda condição); (b) **ambiguidade** — se 2δ ≥ π²/n³, o ponto médio
(ρ_n + ρ_{n+1})/2 é uma medição compatível simultaneamente com n e n+1.
O custo de distinguir n de n+1 cresce, portanto, **cubicamente**.
**Confiança inicial:** média-alta (segue de C0.4 se C0.4 valer).
**Refutadores possíveis:** contraexemplo de decisão no experimento ou no
oráculo; C0.4 cair.

### C0.6 — A janela crepuscular (assimetria inferencial)
**Enunciado:** excluir o círculo custa **quadrático** (o déficit 1 − ρ_n mede a
distância ao caso-limite; C0.3), mas decidir n custa **cúbico** (C0.5). Logo há
uma janela: para todo δ ≤ 1/100, todo inteiro n com
(π²/2δ)^{1/3} ≤ n ≤ 1/√δ satisfaz simultaneamente: (a) existe medição de erro
≤ δ compatível com n e n+1 (identidade indecidível); (b) toda medição honesta
de um n-ágono tem ρ̃ + δ < 1 (o círculo é excluído). Instância a testar:
δ = 10⁻⁶ deve dar pelo menos a janela n ∈ [171, 1000] — centenas de polígonos
certamente-polígonos de identidade indecidível.
**Confiança inicial:** média.
**Refutadores possíveis:** janela vazia para algum δ ≤ 1/100; alguma das duas
pontas falhar na instância δ = 10⁻⁶.

### C0.7 — Estabilizações (observação, com porta)
**Enunciado:** as colunas normalizadas n²(1 − ρ_n) e n³·g_n estabilizam,
respectivamente, em π²/2 ≈ 4,9348 e π² ≈ 9,8696. No âmbito deste capítulo isso
é **observação de tabela** amparada pelos sanduíches C0.3–C0.4 (que já
aprisionam as constantes por desigualdade); o enunciado com seta (→) é
linguagem de limite e só poderá ser *afirmado* com o aparato do Capítulo 1.
**Confiança inicial:** alta para a observação; a promoção a teorema-limite fica
para o Cap. 1 (ferramenta) e Cap. 10 (assintótica fina).
**Refutadores possíveis:** estabilização em constantes diferentes.

### C0.8 — O instrumento declara círculo (imperfeição computacional)
**Enunciado:** em float64, a representação direta ρ_n = cos(π/n) colapsa para
1,0 quando 1 − ρ_n < 2⁻⁵³ — ou seja, para n da ordem de 3·10⁸ o instrumento
**afirma** que o polígono é um círculo. A representação alternativa
1 − ρ_n = 2 sen²(π/2n) não colapsa. Mesma grandeza, duas representações, uma
mente (§2.1–2.3: imperfeição computacional/representacional, não do objeto).
**Confiança inicial:** alta.
**Refutadores possíveis:** o colapso não ocorrer na ordem prevista; a forma
2 sen² colapsar também.

---

## Condições gerais de refutação

Qualquer contraexemplo numérico reprodutível no experimento ou no oráculo, ou
falha lógica nas demonstrações, obriga autópsia nos termos da §1.3 — a
conjectura ferida permanece no registro.

## O que este pré-registro não é

Não é reivindicação de prioridade. C0.1 e C0.2 são, em substância, geometria
clássica cuja *organização inferencial* é deste tratado; C0.3–C0.6 são
elementares o bastante para provavelmente existirem na literatura — a tipagem
no `claims.yml` dirá "síntese autoral; prioridade histórica não estabelecida"
onde couber, e `theorem` clássico onde for clássico.
