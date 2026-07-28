# Capítulo 1 — A Exaustão · Pré-registro de conjecturas

**Tipo declarado:** escavação.
**Data do pré-registro:** 28/07/2026.
**Estatuto (§1.3, E2):** este é o registro *prospectivo* do desenvolvimento do capítulo. O sítio arqueológico (contato anterior do autor com o método de Arquimedes) ainda não foi minerado: nenhum fragmento verbatim foi commitado até esta data, e `sources.md` registrará o estado documental quando a mineração ocorrer. Lacunas documentais **não** serão preenchidas com memória apresentada como fato. As conjecturas abaixo referem-se ao desenvolvimento que este capítulo fará a partir de agora — para elas o pré-registro vale com força probatória plena.

---

## Pergunta central (registrada antes do desenvolvimento)

> Por que o aprisionamento de Arquimedes — polígonos por dentro, polígonos por fora — **converge**? E com que **velocidade**? O que exatamente garante que apertar o cerco funciona, além de "as figuras se aproximam"?

Contexto: Arquimedes chegou a 3 + 10/71 < π < 3 + 1/7 com polígonos de 96 lados. A obrigação estrutural do capítulo (MATH3us.md §3) é não encerrar na evidência visual.

---

## Conjecturas

### C1 — Monotonia dupla
**Enunciado:** com a_n = semiperímetro do polígono regular inscrito de n lados no círculo unitário e b_n = semiperímetro do circunscrito, a sequência (a_n) é estritamente crescente e (b_n) estritamente decrescente sob duplicação de lados, com a_n < b_n sempre.
**Confiança inicial:** alta.
**Exemplos disponíveis:** hexágono → dodecágono (a_6 = 3; b_6 = 2√3 ≈ 3,4641; a_12 ≈ 3,1058; b_12 ≈ 3,2154).
**Justificativa intuitiva:** duplicar lados só pode aproximar o polígono do círculo, por dentro e por fora.
**Refutadores possíveis:** um passo de duplicação em que a_2n ≤ a_n ou b_2n ≥ b_n; falha do argumento de inclusão para perímetros (perímetro não é monótono sob inclusão em geral — apenas sob convexidade; ver C5).

### C2 — Limite comum
**Enunciado:** (a_n) e (b_n) convergem para o mesmo limite, e esse limite é π (o semiperímetro do círculo unitário).
**Confiança inicial:** alta.
**Justificativa intuitiva:** o cerco aperta e a diferença b_n − a_n parece esvaziar-se.
**Refutadores possíveis:** b_n − a_n não tender a zero; impossibilidade de identificar o limite com o comprimento do círculo sem hipótese adicional não declarada.

### C3 — As recorrências de médias
**Enunciado:** a duplicação obedece exatamente a b_{2n} = média harmônica(a_n, b_n) e a_{2n} = média geométrica(a_n, b_{2n}); logo toda a tabela de Arquimedes é computável apenas com as quatro operações e raiz quadrada, sem trigonometria.
**Confiança inicial:** alta (é a estrutura clássica do algoritmo de Arquimedes; a redescoberta aqui é do *caminho*, não do resultado).
**Refutadores possíveis:** discrepância numérica entre a recorrência e os valores geométricos diretos em qualquer n.

### C4 — Razão de contração 1/4
**Enunciado:** a razão entre diferenças sucessivas, (b_{2n} − a_{2n})/(b_n − a_n), converge para **1/4** quando n cresce.
**Confiança inicial:** média-alta. A assintótica clássica prevê erro da ordem de 1/n², o que sugere fator 4 por duplicação; mas o enunciado preciso da razão-limite será testado no experimento antes de qualquer prova.
**Exemplos disponíveis no momento do registro:** nenhum calculado ainda; a tabela do experimento será a primeira evidência.
**Refutadores possíveis:** razões observadas estabilizando em valor ≠ 1/4; não estabilização.

### C5 — A prova elementar entrega menos que o experimento sugere
**Enunciado:** a demonstração elementar via recorrências (desigualdade das médias) entregará apenas o fator **1/2** por duplicação — b_{2n} − a_{2n} < (1/2)(b_n − a_n) — suficiente para provar convergência com cota explícita, mas mais fraco que o 1/4 observado. Fechar o 1/4 exigirá análise local (expansões), que pertence a capítulo posterior.
**Confiança inicial:** média.
**Justificativa intuitiva:** a desigualdade harmônica dá naturalmente a_n/(a_n+b_n) < 1/2; nada no argumento parece render 1/4 sem expansão fina.
**Refutadores possíveis:** existência de prova elementar do fator 1/4 (ou melhor) dentro do próprio aparato do capítulo — o que refutaria C5 e mereceria autópsia.

### C6 — A convergência visual antecipa (e engana)
**Enunciado:** no render em canvas, os três traços (inscrito, círculo, circunscrito) tornam-se indistinguíveis ao olho para n muito menor do que o necessário para a precisão de Arquimedes; uma lupa de zoom mostrará que a distinção persiste onde o olho jura que acabou.
**Confiança inicial:** alta.
**Função:** materializar a diferença entre convergência visual, numérica e demonstrada (camada de observação, §2.1).
**Refutadores possíveis:** indistinção visual coincidindo com indistinção numérica na precisão exibida.

---

## Condições gerais de refutação

Qualquer contraexemplo numérico reprodutível no experimento do capítulo, ou falha lógica apontada nas demonstrações, obriga autópsia nos termos da §1.3 — a conjectura ferida permanece no registro.

## O que este pré-registro não é

Não é reivindicação de prioridade: C1–C3 são resultados clássicos cuja *escavação* (o caminho de reconstrução) é o objeto do capítulo. A tipagem no `claims.yml` seguirá §1.4: proveniência `classical` onde couber, síntese apenas onde for síntese.

---

## Autópsia de C5 (28/07/2026)

C5 afirmava: *"a demonstração elementar via recorrências entregará apenas o
fator 1/2 por duplicação; fechar o 1/4 exigirá análise local (expansões),
que pertence a capítulo posterior."* **Refutada em 28/07/2026**, no mesmo
dia do pré-registro, durante o desenho do exercício E3.1.

1. **Qual passo parecia plausível?** As desigualdades de médias pareciam
   esgotar o aparato: a/(a+b) < 1/2 saía natural, e nada ali sugeria 1/4.
   A justificativa registrada foi literal: "nada no argumento parece render
   1/4 sem expansão fina".
2. **Onde ocorreu a falha lógica?** Em tratar "elementar" como sinônimo de
   "grosseiro". A conjectura avaliou o *método conhecido* (estimar por
   desigualdades) e concluiu sobre o *aparato inteiro*. Mas a folga admite
   fatoração exata — b_2n − a_2n = √b_2n·(b_2n − a_n)/(√a_n + √b_2n) — que
   não estima nada: reescreve. Combinada com b_2n − a_n = a_n(b_n − a_n)/(a_n + b_n),
   dá (b_2n − a_2n)/(b_n − a_n) = [a_n/(a_n+b_n)]·[√b_2n/(√a_n+√b_2n)],
   e a convergência comum a π (já provada no capítulo) leva cada colchete
   a 1/2 e o produto a 1/4.
3. **Qual contraexemplo ou teorema expôs a falha?** A própria identidade
   acima, encontrada ao redigir o gabarito de E3.1 (diferença de quadrados
   sobre a_2n = √(a_n·b_2n)).
4. **O que havia de aproveitável na intuição?** A distinção entre cota
   uniforme e comportamento assintótico, que era o núcleo da conjectura,
   sobrevive intacta: 1/2 vale desde o primeiro passo; 1/4 é limite.
   E a parte da intuição sobre a *constante fina* estava certa: π³/(2n²)
   continua exigindo as expansões do Cap. 10.
5. **Qual reformulação sobreviveu?** "O aparato elementar entrega o 1/4
   como limite (teorema, seção 6 do capítulo); a cota uniforme simples
   permanece 1/2; a forma exata da folga (∼ π³/(2n²)) permanece porta fechada
   para o Cap. 10."

*(Correção de 28/07/2026, pós-r2: os dois itens acima escreviam π³/n² —
a mesma troca de constante corrigida no capítulo e no ledger; esta
ocorrência escapou da varredura do merge e foi corrigida no pré-registro
da reconstrução D3. A folga de semiperímetros é ∼ π³/(2n²); π³/n² pertence
à folga de áreas. Registrado, não apagado.)*

**Consequências no ledger:** `chapter-01.gap-ratio-quarter` promovida de
conjectura sustentada a teorema (`status: proved`, prova na seção 6 e
exercício E3.1); `chapter-01.elementary-apparatus-limit` marcada
`status: refuted` com referência a esta autópsia.

**Nota de método:** a refutação nasceu do desenho de exercícios (emenda
E20) — escrever gabarito "como para uma criança" obrigou a reescrever a
expressão em vez de estimá-la. O leitor didático é um instrumento de
descoberta.

---

## Pré-registro R — a reconstrução geométrica (D3), 28/07/2026

**Estatuto.** Extensão do capítulo decidida pelo leitor primário (decisão D3,
`AUDIT.md`), com sítio documental próprio: o documento fundador de 28/07/2026
(crítica do leitor primário ao capítulo implementado, verbatim em
`caps/00-inferencia/sources.md`), que contém as derivações originais do
autor para as afirmações abaixo. O pré-registro vale com força plena para o
que ainda não foi verificado: **nenhuma das identidades R1–R4 foi conferida
simbólica ou numericamente antes deste commit**, e as constantes de R5 vêm
do documento fundador, não de cálculo do tratado.

### R1 — As identidades de área
**Enunciado:** no círculo unitário, as áreas dos polígonos regulares
inscrito e circunscrito de n lados satisfazem A⁻ₙ = aₙ²/bₙ e A⁺ₙ = bₙ.
A segunda é a observação de que o "semiperímetro externo" É a área externa,
porque o apótema do circunscrito é o raio 1.
**Confiança:** alta (derivação do documento fundador: A⁻ₙ = n·sen θ·cos θ e
cos θ = aₙ/bₙ).
**Refutadores:** discrepância numérica em qualquer n entre as fórmulas e a
área computada por geometria direta (shoelace).

### R2 — A área herda o semiperímetro
**Enunciado:** A⁻₂ₙ = aₙ exatamente — a área do inscrito de 2n lados é o
semiperímetro do inscrito de n lados. Via recorrência: A⁻₂ₙ = a₂ₙ²/b₂ₙ =
aₙ·b₂ₙ/b₂ₙ = aₙ.
**Confiança:** alta.
**Refutadores:** qualquer n com A⁻₂ₙ ≠ aₙ além do erro de máquina.

### R3 — A cadeia do duplo cerco
**Enunciado:** A⁻ₙ < A⁻₂ₙ = aₙ < π < b₂ₙ = A⁺₂ₙ < A⁺ₙ, para todo n da
sequência de duplicação. As desigualdades novas custam uma linha cada sobre
os teoremas já provados (A⁻ₙ = aₙ·(aₙ/bₙ) < aₙ; o resto é monotonia já
demonstrada).
**Confiança:** alta.
**Refutadores:** violação de qualquer elo em qualquer k.

### R4 — A razão das duas folgas
**Enunciado:** ΔAₙ = A⁺ₙ − A⁻ₙ = (bₙ − aₙ)(bₙ + aₙ)/bₙ (identidade exata), e
ΔAₙ/(bₙ − aₙ) → 2, demonstrável com o aparato do capítulo (sem expansões):
(aₙ+bₙ)/bₙ = 1 + aₙ/bₙ e aₙ/bₙ → 1 com cota explícita pela folga já provada.
**Confiança:** alta.
**Refutadores:** razão estabilizando em valor ≠ 2; a prova elementar falhar.

### R5 — A dualidade das quatro constantes
**Enunciado:** n²(π − aₙ) → π³/6, n²(bₙ − π) → π³/3, n²(π − A⁻ₙ) → 2π³/3,
n²(A⁺ₙ − π) → π³/3. Consequências estruturais: no cerco por perímetros o
erro externo é o dobro do interno; no cerco por áreas, o interno é o dobro
do externo — **o erro dominante troca de lado**. Duas verificações de
consistência são exatas e demonstráveis já: (π−aₙ) + (bₙ−π) = bₙ−aₙ (logo
π³/6 + π³/3 = π³/2, a constante do E4.2); e π − A⁻ₙ = (π−aₙ) + aₙ(bₙ−aₙ)/bₙ
(logo 2π³/3 = π³/6 + π³/2). As quatro constantes individuais **não são
demonstráveis neste capítulo** — exigem as expansões locais do Cap. 10;
entram como conjectura sustentada por tabela normalizada.
**Confiança:** média-alta para os valores (documento fundador + consistência
interna); alta para a troca de dominância condicionada aos valores.
**Refutadores:** colunas normalizadas estabilizando em outras constantes;
violação das identidades de consistência (essas refutariam R1/R4 também).

**Porta declarada:** R5 → Capítulo 10 (expansões locais), junto com a
constante π³/2 do E4.2, da qual as quatro constantes são o refinamento.
