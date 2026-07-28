# MATH3us.md — Manual Operacional do Tratado

> Reconstrução formal de uma matemática já vivida.
> Leitor primário: Matheus M. Coelho. Autor: o mesmo. Testemunha: o repositório.
> Revisão 2 — emendas E1–E19 (ver §13).

---

## 0. Identidade do projeto

- **Nome de trabalho:** *Do Número ao Contínuo — reconstrução formal de uma matemática já vivida*
- **Nome do manual:** MATH3us.md. O caractere 3 é um numeral que representa o número três e, simultaneamente, substitui graficamente a letra "E" (E1). Três é o menor ímpar admissível do Capítulo 2 e o primeiro primo ímpar. O nome realiza a doutrina da §2.1 no próprio título. O nome público da obra permanece *Do Número ao Contínuo*; MATH3us.md é a constituição operacional do repositório.
- **Natureza:** biografia intelectual em curso, não currículo, enciclopédia nem curso convencional. O projeto documenta a distância entre o que foi intuído, o que foi afirmado, o que era demonstrável e o que precisou ser reconstruído.
- **Formato canônico:** repositório GitHub `Drmcoelho`, linhagem visual e editorial `atlas-artefato`.
- **Unidade de entrega:** capítulo fechado, seja ele uma escavação completa ou um território virgem integralmente coberto. Nunca volume.
- **Formato de release:** um `index.html` autocontido por capítulo. **A autocontenção e o funcionamento sem rede são invariantes desde o Gate v0** (E9); durante o desenvolvimento, componentes podem residir em `lib/`, e nos gates v0 e v1 o empacotamento e sua inspeção podem ser manuais.
- **Estado da obra:** não existe "obra terminada". Existe um repositório vivo que compila, preserva sua linhagem e produz releases verificáveis.
- **Leitor público eventual:** permitido, mas secundário. O texto não será simplificado artificialmente para um leitor abstrato à custa da precisão da reconstrução.
- **Status do antigo "Volume V — A Geometria do que Não Fecha":** material de prospecção transversal. Não constitui um quinto volume editorial. Seus resultados, perguntas e estruturas são absorvidos pelos capítulos existentes conforme o mapa definido neste manual.

---

## 1. Doutrina

### 1.1 Critério de corte único

Um conteúdo só entra no tratado se responder satisfatoriamente:

**Onde Matheus falharia se tentasse provar isso sozinho agora?**

Se a demonstração, reconstrução ou verificação puder ser produzida corretamente em aproximadamente dez minutos, sem introdução de uma técnica nova e sem risco epistemológico relevante, o conteúdo não merece capítulo. Pode aparecer como nota, passagem, experimento ou consequência, mas não como eixo estrutural.

O tratado não recompensa quantidade de assuntos. Recompensa a localização precisa de obstáculos reais.

### 1.2 Dois tipos de capítulo

Todo capítulo declara, no início, uma destas categorias:

**Escavação** — sítio arqueológico intelectual próprio. Parte de uma pergunta, intuição, padrão, tentativa de prova ou descoberta anterior de Matheus e reconstrói formalmente o caminho. A teoria é introduzida apenas quando se torna necessária.

A escavação deve preservar: o enunciado original; a linguagem original, quando disponível; o que estava correto; o que estava incompleto; o que estava errado; a teoria que faltava; a diferença entre redescoberta pessoal e prioridade histórica.

**Território virgem** — não existe descoberta prévia suficientemente formada para ser escavada. O capítulo cobre o território necessário de modo integral, mas continua obedecendo ao critério de corte: só entra aquilo que prepara uma falha futura já identificada ou destranca um capítulo posterior.

A assimetria deve ser declarada. O livro não fingirá que todo conhecimento surgiu por redescoberta pessoal. O tipo é declaração epistêmica por capítulo; o agrupamento em Partes (§3) é temático e não o substitui.

### 1.3 Conjectura antes do texto

Cada capítulo começa por um registro anterior ao desenvolvimento: pergunta datada; conjectura datada; exemplos disponíveis naquele momento; justificativa intuitiva original; grau de confiança inicial; condições que poderiam refutá-la.

`conjecturas.md` deve ser criado e commitado antes de o desenvolvimento de `index.html` começar.

Uma conjectura refutada nunca é apagada. Recebe uma autópsia, que deve responder:

1. Qual passo parecia plausível?
2. Onde ocorreu a falha lógica?
3. Qual contraexemplo ou teorema expôs a falha?
4. O que havia de aproveitável na intuição?
5. Qual reformulação sobreviveu?

Editar o passado para remover uma conjectura errada é falsificação do experimento intelectual.

**Retrospectividade das escavações (E2).** O pré-registro é um instrumento *prospectivo*. Nas escavações, a descoberta antecede o tratado; portanto `conjecturas.md` registra o estado documental do sítio — com as datas originais quando existirem — e o mecanismo de honestidade é a cadeia de proveniência do dossiê (`sources.md`, citações verbatim), não a anterioridade do commit. O pré-registro com força probatória plena aplica-se a três casos: conjecturas novas surgidas durante a redação; territórios virgens; extensões que não constavam do sítio original. O conteúdo matemático fixado neste manual para os Capítulos 1–5 tem estatuto de **contrato editorial**, não de conjectura pré-registrada — reivindicar o contrário seria a primeira desonestidade do projeto.

**Falsificabilidade do contrato editorial (E15).** O contrato editorial fixa as proposições a investigar e as obrigações demonstrativas previstas. Se uma proposição contratada se revelar falsa, incompleta ou mal formulada, o capítulo deve refutá-la e o manual deve receber emenda explícita. O contrato não obriga a matemática a obedecer ao planejamento.

### 1.4 Ledger epistemológico normalizado (E6)

Toda afirmação matematicamente relevante recebe, no `claims.yml` do capítulo, campos **ortogonais** — natureza, estado, proveniência e modo de prova são dimensões diferentes e não podem ser fundidas em um único enum:

**`kind`** — natureza da afirmação:
`theorem` | `lemma` | `definition` | `conjecture` | `estimate` | `question` | `synthesis`

**`status`** — situação de verdade e prova:
`proved` | `supported` | `conjectured` | `refuted` | `open` | `conditional`

**`provenance`** — origem do resultado:
`classical` | `rediscovered` | `derived_in_treatise` | `authorial` | `unknown`

**`proof_mode`** — como a prova comparece no tratado:
`proved_here` | `cited` | `computational_only` | `not_applicable`

**`role`** *(opcional)* — função editorial:
`central_result` | `supporting_result` | `example` | `bridge`

Mapeamento da doutrina anterior (os sete estados de E5 tornam-se combinações):

| Estado antigo | Combinação canônica |
|---|---|
| teorema clássico | `kind: theorem` + `provenance: classical` + `proof_mode: cited` ou `proved_here` |
| dedução do tratado | `kind: theorem`/`lemma` + `status: proved` + `provenance: derived_in_treatise` + `proof_mode: proved_here` |
| síntese autoral | `kind: synthesis` + `provenance: authorial` |
| conjectura experimental | `kind: conjecture` + `status: supported` |
| questão aberta | `kind: question` + `status: open` |
| afirmação refutada | `status: refuted` |
| estimativa | `kind: estimate` |

Combinações incompatíveis (por exemplo, `kind: synthesis` com `proof_mode: proved_here` para uma identidade demonstrável — a identidade é `theorem`; a síntese é a organização) bloqueiam a release a partir do gate v1.

"Parece", "provavelmente" e "talvez" não substituem classificação. A incerteza deve ser localizada, nunca diluída por hedging genérico.

### 1.5 Affirm versus infer aplicado à matemática

O tratado distingue: o que foi observado; o que foi inferido; o que foi demonstrado; o que foi verificado computacionalmente; o que continua dependendo de hipótese.

Verificação numérica não é demonstração. Demonstração simbólica não dispensa teste de implementação. Representação gráfica não constitui evidência suficiente de convergência, continuidade, inexistência ou universalidade.

**Proveniência executável (E12).** Nenhuma alegação de que algo "passou pelo oráculo" entra no tratado ou neste manual sem artefato correspondente: script, hash de commit, domínio testado, ambiente, implementação e data. Sem artefato, a alegação é rebaixada a *verificação exploratória não canônica* e declarada como tal — ou removida. Testemunho exige testemunha; a testemunha é o repositório.

### 1.6 Computacional-nativo

Experimentos são executáveis dentro do HTML. Não existem como anexos decorativos.

O código deve cumprir ao menos uma destas funções: gerar exemplos; procurar contraexemplos; explorar parâmetros; revelar invariantes; comparar uma conjectura com o comportamento real; verificar numericamente uma derivação; expor falhas de representação; permitir que o leitor destrua uma intuição inadequada.

O código faz parte do argumento, mas não substitui a prova. Sempre que houver fórmula central, o capítulo deve separar visualmente:

**O experimento sugere. A demonstração obriga.**

### 1.7 Gate de verificação — versionado (E4, corrigido por E9)

O gate é versionado para que o primeiro capítulo não se transforme em projeto de infraestrutura. **A autocontenção e o funcionamento sem rede são invariantes desde o v0**; os gates posteriores automatizam a verificação desses invariantes, não os inauguram.

**Gate v0** — vigente até o fechamento do primeiro capítulo:

- `audit.mjs`: screenshots em viewport desktop real e viewport equivalente a iPhone; teste básico de interação; inspeção de overflow, clipping, canvas, fórmulas e tipografia;
- `oracle.py`: oráculo triplo para cada invariante numérico;
- `claims.yml` escrito e conferido manualmente;
- autocontenção verificada por inspeção manual (sem CDN, fonte remota ou chamada de rede);
- render efetivamente visto por um agente responsável.

**Gate v1** — a partir do segundo capítulo fechado: adiciona `claims.schema.json` e `verify-claims.mjs` (validação automática de campos, combinações e dependências).

**Gate v2** — a partir do terceiro capítulo fechado: adiciona `bundle.mjs` e `validate-release.mjs`, **automatizando** o empacotamento e a verificação de autocontenção.

**Endurecimento não autoriza reescrita silenciosa (E9).** Capítulos fechados sob gate anterior são reauditados quando o gate endurece. Se a reauditoria revelar erro de conteúdo — bug matemático, fórmula inacessível, interação incorreta, dependência remota, discrepância entre prova e experimento — a correção recebe commit, entrada no changelog e release próprios.

**Convenção de releases (E9).** Tags Git são imutáveis. Formato: `cap-01-gate0-r1`, `cap-01-gate1-r1`, `cap-01-gate2-r1`; revisão de conteúdo incrementa `r`. O manifest registra:

```yaml
chapter: 1
content_revision: 1
gate_version: 2
commit: abc1234
previous_release: cap-01-gate1-r1
```

Revisão matemática e reauditoria infraestrutural nunca se confundem.

**Acessibilidade funcional mínima (E4, refinada por E14).** Em dois níveis:

*Figura simples:* `aria-label` ou legenda textual suficiente.

*Figura analítica ou interativa:* resumo textual adjacente; controles operáveis por teclado; valores atuais anunciáveis; tabela ou lista equivalente quando a figura carrega dados; foco visível; nenhuma dependência exclusiva de hover; indicação explícita do que mudou após interação.

*Transversal:* contraste AA no texto corrente; nenhuma informação transmitida apenas por cor; fórmulas centrais com representação textual ou MathML no HTML final — LaTeX renderizado como imagem não é acessível por si.

Nenhuma exceção é permitida sob entusiasmo.

### 1.8 Oráculo triplo

Todo resultado numérico central passa por três verificações independentes:

1. **Derivação simbólica** — álgebra explícita; hipóteses declaradas; domínio verificado; simplificação simbólica, quando pertinente.
2. **Verificação numérica independente** — implementação distinta da utilizada no experimento principal; amostragem ampla; precisão adequada; registro dos valores testados.
3. **Caso extremo, degenerado ou adversarial** — menor valor permitido; proximidade de singularidade; limite assintótico; caso que costuma quebrar a fórmula; entrada inválida que deve ser recusada.

A doutrina deriva do incidente Viviani: uma identidade visualmente convincente pode permanecer errada por tempo suficiente para contaminar o projeto inteiro.

### 1.9 Prosa antes de enumeração

O corpo dos capítulos privilegia prosa contínua. Listas são usadas quando enumeração é a forma real da estrutura: hipóteses, casos, etapas algorítmicas, campos do ledger ou critérios de release.

Setas e encadeamentos compactos são permitidos quando representam uma transformação real:

observação → conjectura → formalização → prova → recíproca → limite.

### 1.10 Idioma

- Texto, interface e explicações: português.
- Código, nomes internos, commits, branches e tooling: inglês.
- Símbolos matemáticos: notação internacional, definida na primeira aparição.
- Termos autorais: declarados como termos do tratado, nunca apresentados como nomenclatura universal.

### 1.11 Antienciclopedismo

Nenhum capítulo será expandido apenas porque existe teoria relacionada. Uma seção só entra quando: resolve uma falha prevista; completa uma demonstração; fornece uma recíproca necessária; delimita corretamente o resultado; prepara uma dependência posterior; destrói uma interpretação errada provável.

O tratado não é um depósito de curiosidades matemáticas, ainda que algumas curiosidades sejam estruturalmente úteis.

### 1.12 Honestidade de prioridade

O tratado distingue rigorosamente: descoberta pessoal; redescoberta independente; resultado clássico reencontrado; nova demonstração pessoal de resultado conhecido; nova organização de resultados conhecidos; conexão possivelmente original; novidade matemática demonstrável.

Nenhuma identidade será chamada de inédita apenas porque foi encontrada sem consulta prévia. Quando não houver busca bibliográfica suficiente para avaliar prioridade, o texto dirá:

*Síntese autoral no âmbito deste tratado; prioridade histórica não estabelecida.*

---

## 2. Gramática epistemológica transversal

### 2.1 Objeto, representação e observação

Todo capítulo deve distinguir três camadas.

**Objeto** — a estrutura matemática que independe da notação escolhida. Exemplos: o número sete; a primalidade; uma transformação linear; uma função contínua; uma classe de equivalência.

**Representação** — a forma pela qual o objeto é escrito ou visualizado. Exemplos: 7, VII, 111₂; coordenadas de um vetor; expansão decimal; gráfico cartesiano; matriz de uma transformação.

**Observação** — o resultado produzido por um instrumento, algoritmo, amostra ou experimento. Exemplos: pixels de um gráfico; aproximação de uma integral; amostra de uma sequência; resultado em ponto flutuante.

Confundir essas camadas é uma das fontes recorrentes de erro que o tratado deve tornar visível.

### 2.2 Fechamento e resíduo (corrigida por E8)

"Fechamento" será um motivo transversal, não um teorema único. Um sistema fecha quando duas descrições, operações ou periodicidades coincidem exatamente após um número finito de passos.

**Domínios e referência.** Exige-se A > 0 e B > 0; B funciona como unidade de referência declarada, o que torna a medida **assimétrica por construção**: C_N(A,B) ≠ C_N(B,A) em geral, e isso é intencional. Para referentes físicos não estacionários (ano trópico, dia solar), a notação C_N(A,B; t) reconhece a dependência temporal.

**Forma canônica (aditiva).** Com x = A/B:

C_N(A,B) = min |p·x − q|, sobre 1 ≤ p ≤ N e **q ∈ ℤ livre**.

O inteiro p funciona como denominador da aproximação racional q/p de x. A limitação simultânea de p e q (forma da revisão anterior) admitia minimizadores fora da teoria clássica; a forma canônica com q livre é a que se conecta ao teorema da melhor aproximação.

**Forma canônica (multiplicativa).** Para α, β > 0 com α ≠ 1 e β ≠ 1:

L̃_N(α,β) = min |p·(ln α / ln β) − q|, sobre 1 ≤ p ≤ N e q ∈ ℤ.

A normalização pela razão de logaritmos torna o valor independente da base do logaritmo (os minimizadores já o eram; o valor, não). A relação com aproximação racional fica explícita: ln α / ln β ≈ q/p. Para quinta e oitava: ln(3/2)/ln 2 ≈ 7/12.

**Promessa restrita (E8).** O Capítulo 5 deverá transformar a busca do menor resíduo em problema de aproximação racional e demonstrar, *para a formulação adotada*, quais minimizadores são fornecidos pelos convergentes e quando os semiconvergentes entram. A afirmação genérica "os pares ótimos são as reduzidas" fica revogada: era mais forte do que o teorema que será realmente provado.

Essas quantidades são ferramentas sintéticas do tratado, não nomenclatura clássica. Permitem comparar, sem confundir: ano e dia; quinta e oitava; aproximações racionais; resolução computacional; ciclos que quase retornam; representações que não terminam.

### 2.3 Taxonomia da imperfeição

O tratado reconhece pelo menos cinco formas distintas de não fechamento:

**Representacional** — o objeto está perfeitamente definido, mas sua escrita em determinada base é infinita ou periódica. Exemplo: 1/3 = 0,3̄.

**Estrutural** — não existem inteiros que produzam o fechamento pretendido. Exemplo: (3/2)^p ≠ 2^q para todos os inteiros positivos p, q.

**Física** — o referente medido varia com o tempo ou possui flutuação maior que a precisão exigida.

**Computacional** — a implementação trabalha com precisão finita, arredondamento, truncamento, overflow ou instabilidade numérica.

**Epistemológica** — o estado do conhecimento não permite decidir a proposição ou ainda não contém demonstração suficiente.

As cinco categorias não são intercambiáveis. Um erro de representação não deve ser descrito como falha do objeto. Uma limitação computacional não refuta um teorema.

### 2.4 Método canônico de descoberta

Sempre que o sítio permitir, o capítulo explicita o percurso:

**intuição → exemplos → padrão → enunciado → fórmula → prova → recíproca → generalização → limites**

A recíproca não é ornamental. Ela determina se o resultado apenas produz exemplos ou se classifica integralmente o fenômeno.

---

## 3. Arquitetura do tratado (renumerada por E7)

A numeração dos capítulos é a **ordem canônica de leitura** e é topologicamente compatível com as dependências. A ordem de produção, distinta, está na §5.

### Prólogo (E20)

| Cap. | Título | Sítio | Teoria puxada | Obrigação canônica | Falha prevista |
|---|---|---|---|---|---|
| 0 | A Inferência | Duas circunferências e um polígono: a configuração dual do Cap. 1. A cunha fundamental R, r, L/2 e a pergunta inferencial — o que o par de circunferências sabe sobre o polígono? | Pitágoras → semelhança e monotonia de área → medida do ângulo por área → desigualdade da cunha → sanduíches explícitos → decisão sob erro de medição | Demonstrar que (r, R) determina o polígono a menos de rotação; quantificar por desigualdades explícitas, **sem linguagem de limite**, o limiar quadrático (excluir o círculo) e o cúbico (decidir n) | Usar linguagem de limite antes de possuí-la; confundir a constante do déficit (π²/2, quadrática) com a da folga entre razões (π², cúbica) |

**Capítulo 0 — obrigação estrutural (E20).** O capítulo precede o Capítulo 1 na leitura porque precisa de **menos**: nenhuma completude, nenhum limite, nenhum postulado de convexidade — apenas Pitágoras, semelhança, monotonia de área sob inclusão e a medida do ângulo pela área varrida. Obrigações: (i) o triângulo fundamental R² = r² + (L/2)² como átomo do polígono regular; (ii) a identidade da coroa (área da coroa = área do círculo de raio L/2), independente do valor de π; (iii) a razão r/R como portadora integral da forma — inferência de n a partir do par de circunferências, com o conjunto admissível discreto; (iv) desigualdades-sanduíche explícitas para o déficit 1 − r/R e para a folga entre razões consecutivas; (v) teoria da decisão sob erro δ: garantia de identificação, possibilidade de ambiguidade e a janela crepuscular (polígono certo, identidade indecidível). O símbolo π entra como **constante da área do disco** (ângulo medido por área); sua identificação com a constante perimetral do Cap. 1 é porta fechada → Cap. 9. Toda afirmação assintótica com seta (→) é observação de tabela ou conjectura pré-registrada — a linguagem de limite pertence ao Cap. 1. O capítulo fornece a cunha que a reconstrução geométrica do Cap. 1 (pendência editorial registrada) utilizará.

### Parte I — Escavações

| Cap. | Título | Sítio | Teoria puxada | Obrigação canônica | Falha prevista |
|---|---|---|---|---|---|
| 1 | A Exaustão | Reconstrução do método de Arquimedes; aproximações por dentro e por fora | Sequências monótonas limitadas → convergência → erro → ordem → linguagem ε-N | Demonstrar por que o aprisionamento converge e produzir limite explícito para o erro | Aceitar convergência por evidência gráfica |
| 2 | As Ternas do Ímpar | 3-4-5, 5-12-13, 7-24-25 e a intuição de que todo ímpar gera uma terna | Paridade → divisão euclidiana → mdc → TFA → parametrização de Euclides → recíproca → descida infinita quando necessária | Classificar exatamente as ternas em que cateto maior e hipotenusa são consecutivos | Reconhecer o padrão sem provar universalidade, unicidade ou primitividade |
| 3 | A Singularidade do Quatro | 2+2 = 2·2 = 2² | Unicidade → prova de inexistência → classificação de soluções → variação de regras | Demonstrar que 2 é o único inteiro positivo x com x+x = x² = x^x, produzindo 4 | Confundir coincidência notacional com singularidade estrutural |
| 4 | Os Algarismos Repetidos | 8, 80, 44, 0,142857̄ | Valor posicional → congruências → critério de terminação em base b → ordem multiplicativa → primos full-reptend | Distinguir número de numeral e demonstrar por que toda base finita deixa infinitos primos "de fora" | Conhecer o fenômeno sem a teoria que o torna inevitável |
| 5 | A Consonância | Travessia calendário → segundo atômico → números regulares → razões musicais | Razões 2, 3, 5 → logaritmos → aproximação racional → frações contínuas → coma pitagórica → temperamento | Quantificar o não fechamento; ancorar C_N e L̃_N na aproximação diofantina conforme §2.2; mostrar por que administrar o resíduo não equivale a eliminá-lo | Usar aproximações sem algoritmo, erro ou critério de optimalidade |

**Capítulo 1 — obrigação estrutural.** O capítulo não poderá encerrar em "as figuras se aproximam". Deverá demonstrar: monotonicidade da aproximação inferior; monotonicidade da aproximação superior; existência de limite comum; estimativa explícita do erro; diferença entre convergência visual, numérica e demonstrada; tradução do método geométrico para linguagem moderna. O capítulo apresenta pela primeira vez a ideia de que o erro também possui forma.

**Capítulo 2 — contrato matemático (E5, tipagem por E6).** Para todo inteiro ímpar n ≥ 3, definem-se L = (n²−1)/2 e R = (n²+1)/2. O capítulo deverá demonstrar, nesta ordem lógica:

1. **Direta:** n² + L² = R², com R − L = 1.
2. **Recíproca e classificação:** todo triângulo retângulo inteiro com cateto maior e hipotenusa consecutivos pertence à família; correspondência biunívoca com os ímpares n ≥ 3.
3. **Primitividade:** consecutividade de L e R implica terna primitiva; gcd(n, L) = 1.
4. **Estrutura modular:** n² ≡ 1 (mod 8), logo L ≡ 0 (mod 4) e R ≡ 1 (mod 4).
5. **Medidas:** P = n(n+1); o semiperímetro s é o n-ésimo número triangular; K = n(n²−1)/4, inteiro e par.
6. **Raios:** r = (n−1)/2; ex-raio oposto ao cateto ímpar r_n = (n+1)/2; portanto r_n − r = 1.
7. **Leitura euclidiana:** u = (n+1)/2 e v = (n−1)/2 recuperam a parametrização de Euclides pelo caminho inverso (u²−v² = n; 2uv = L; u²+v² = R).

**Tipagem correta dos itens 6–7 (E6):** as identidades r = (n−1)/2, r_n = (n+1)/2 e r_n − r = 1 são **deduções demonstráveis** (`kind: theorem`, `proof_mode: proved_here`). A **síntese autoral** (`kind: synthesis`, `provenance: authorial`) é a observação organizacional de que os mesmos dois inteiros consecutivos aparecem simultaneamente como parâmetros de Euclides, inraio e ex-raio — *prioridade histórica não estabelecida*.

As derivações completas pertencem ao `index.html` do capítulo. Este manual fixa o contrato, não o texto. Porta trancada: primos representáveis como soma de dois quadrados → Capítulo 7.

*Proveniência (rebaixada por E12):* em 28/07/2026 foi executada verificação **exploratória não canônica** dos itens do contrato — ímpares n ∈ {3, 5, …, 20001}, Python, implementação única, sem artefato versionado, sem casos pares adversariais, sem comparação com implementação independente. Ela informa confiança de trabalho, não constitui oráculo do tratado. O oráculo canônico será executado na abertura do diretório do capítulo, com script, hash, relatório em `audit/` e domínio declarado, incluindo pares adversariais (que devem produzir L e R não inteiros e ser recusados).

**Capítulo 3 — formato mínimo.** Capítulo-modelo contra o gigantismo editorial. Pergunta central: para quais inteiros positivos x a adição de x consigo mesmo, sua multiplicação por si mesmo e sua exponenciação por si mesmo produzem o mesmo resultado? De x + x = x² segue x(x−2) = 0; no domínio dos inteiros positivos, x = 2, e então 2+2 = 2·2 = 2² = 4. Se três páginas bastarem, o capítulo terá três páginas. Nenhuma expansão histórica ou filosófica sem função demonstrativa.

**Capítulo 4 — bases e fuga dos primos.** O capítulo deverá provar o critério: uma fração reduzida a/d possui expansão finita na base b se, e somente se, existe k ∈ ℕ tal que d | b^k — equivalentemente, todos os fatores primos de d dividem b. Consequências obrigatórias: base 10 incorpora apenas 2 e 5; base 12 incorpora 2 e 3; base 60 incorpora 2, 3 e 5; nenhuma base finita incorpora todos os primos; trocar de base desloca a fronteira da periodicidade, mas não a elimina. O capítulo distinguirá explicitamente: número; numeral; base; expansão; propriedade aritmética; artefato representacional. O sete funcionará como primeiro grande caso de estudo: 1/7 = 0,142857̄, com o período relacionado à ordem multiplicativa de 10 módulo 7 — sem transformar o capítulo em tratado geral de teoria algébrica dos números.

**Capítulo 5 — o defeito de fechamento.** Parte de três sítios: o ano não é um número inteiro de dias; uma unidade atômica extremamente estável ainda contém escolha convencional; doze quintas justas não equivalem a sete oitavas. Relação central: (3/2)¹² ≠ 2⁷, demonstrada por fatoração — a igualdade exigiria 3¹² = 2¹⁹ (531.441 ≠ 524.288; razão ≈ 1,0136), contradizendo a unicidade da fatoração em primos. O capítulo quantificará a diferença, introduzirá frações contínuas **pelo algoritmo** — não apenas pelo resultado — e cumprirá a obrigação de ancoragem na formulação corrigida da §2.2: transformar a busca do menor resíduo em problema de aproximação racional e demonstrar, para a formulação adotada, quais minimizadores vêm dos convergentes e quando entram os semiconvergentes. Distinguirá: fechamento exato; aproximação ótima sob denominador limitado; fechamento convencional; distribuição de erro; variação física do referente. Tese editorial: o temperamento não elimina a incomensurabilidade; distribui sua manifestação. O calendário não elimina o resíduo entre ano e dia; administra seu acúmulo.

### Parte II — Territórios virgens

| Cap. | Título | Cobertura | Dependências e função |
|---|---|---|---|
| 6 | As Patologias | Dirichlet, Thomae, Weierstrass; TVI; completude de ℝ versus ℚ | Depende do Cap. 1. Existe contra a confiança excessiva na imagem e na intuição de regularidade |
| 7 | ℂ | Construção, forma polar, rotação-escala, raízes n-ésimas, argumento multivalorado, escolha de ramo, ℤ[i], Fermat para soma de dois quadrados | Reabre a porta do Cap. 2. A exponencial complexa é **porta fechada** (E11): reaberta no Cap. 10 |
| 8 | Álgebra Linear como Estrutura | Espaços vetoriais, núcleo, imagem, posto, autovetores, mudança de base, Fibonacci matricial | Travessia de ferramenta para objeto. Responde: "o que permanece quando as coordenadas mudam?" |

**Capítulo 6 — função epistemológica.** Existe para destruir proposições visualmente plausíveis. Deve demonstrar que: uma função pode ser descontínua em todos os pontos; uma função pode ser contínua em todos os pontos e não diferenciável em nenhum; densidade não implica completude; um gráfico computacional pode ocultar precisamente a propriedade investigada. Prepara o leitor para desconfiar da frase "dá para ver".

**Capítulo 7 — inversão e multivaloração, sem exponencial (E11).** O capítulo constrói: números complexos; representação polar; multiplicação como rotação e escala; raízes n-ésimas; argumento multivalorado; escolha de ramo **do argumento**; inteiros gaussianos; soma de dois quadrados. O operador de rotação é escrito cos θ + i·sin θ, com o estatuto de seno e cosseno explicitamente geométrico (importado do círculo, não construído por séries). A notação e^{iθ} aparece exclusivamente em caixa de porta fechada: *esta igualdade será demonstrada quando exponencial, seno e cosseno forem reconstruídos por séries (Cap. 10) e sintetizados (Cap. 12)*. O logaritmo complexo completo é adiado; se mencionado, apenas como relação formal cuja inversão será validada posteriormente, com w ≠ 0 e a forma z = ln|w| + i(Arg w + 2kπ), k ∈ ℤ. A falha prevista enfrentada permanece: presumir que toda operação inversa devolve um único valor — as raízes n-ésimas já a destroem sem precisar da exponencial. Superfícies de Riemann completas e topologia de recobrimentos permanecem fora deste ciclo.

**Capítulo 8 — invariância sob mudança de base.** Recupera a distinção objeto–representação: vetor não é lista de coordenadas; transformação linear não é sua matriz; autovalores sobrevivem à mudança de base; núcleo e imagem são estruturas; coordenadas são descrições. A palavra "base" deverá ser comparada cuidadosamente com base numérica, evitando falsa equivalência entre conceitos homônimos.

### Parte III — O contínuo e a síntese

O Capítulo 11 permanece território virgem por declaração de tipo; o agrupamento aqui é temático (§1.2).

| Cap. | Título | Cobertura | Obrigação central |
|---|---|---|---|
| 9 | A Integral como Erro Somado | Riemann rigoroso; somas inferiores e superiores; Cavalieri como teorema; Teorema Fundamental do Cálculo | Mostrar por que infinitas contribuições podem produzir valor finito sem tratar infinito como número ordinário |
| 10 | A Fábrica de Funções | Sequências e séries de funções; convergência uniforme; séries de potências; sin, cos e exp redefinidas; Taylor com resto explícito | Separar aproximação formal, raio de convergência e igualdade demonstrada |
| 11 | Fourier | Do timbre à decomposição; ortogonalidade; coeficientes; convergência em classe declarada; espectro | Decompor sem destruir, na classe de funções que o tratado realmente construiu (E10) |
| 12 | Síntese: e^{iπ} + 1 = 0 | Leitura símbolo a símbolo; reconstrução integral da identidade | O livro termina quando a identidade deixa de ser citação e se torna consequência |

**Capítulo 9 — zero, infinito e limite.** Deverá impedir duas confusões: x → 0⁺ ⟹ 1/x → +∞ não significa 1/0 = ∞, e tampouco 0 = ∞. Zero pertence ao domínio numérico em contextos específicos; infinito, no cálculo elementar, descreve comportamento não limitado. A integral será construída sem usar "infinitamente pequeno" como licença retórica; quando uma linguagem infinitesimal for mencionada, seu estatuto formal deverá ser declarado. O capítulo deverá explicar: soma de Riemann; refinamento de partição; erro; limite; integrabilidade; diferença entre símbolo ∞, limite infinito e número real. Compactificações e esfera de Riemann são adiadas.

**Capítulo 10 — a fábrica e seu interlúdio (E19).** O núcleo inegociável do capítulo é: *como uma série de potências deixa de ser aproximação formal e passa a definir uma função?* — convergência uniforme; troca de soma por derivada e por integral; raio de convergência; resto de Taylor; definição rigorosa de exp, sin e cos; extensão complexa da exponencial (que reabre a porta fechada do Cap. 7). O material sobre a⁰ = 1, colapso de f(a) = a⁰, inexistência de inversa global, perda de informação e 0⁰ (diferenciando expressão algébrica isolada, convenção combinatória, limite dependente do caminho e implementação computacional) entra como **abertura ou interlúdio**, não como eixo: a autópsia de 0⁰ não pode deixar a fábrica sem maquinário.

**Capítulo 11 — decomposição sem destruição, em classe declarada (E10).** Fourier será tratado como passagem: função → componentes → reconstrução, restrito a funções periódicas **suaves por partes com número finito de descontinuidades** (variação limitada, se necessário). Obrigações: convergência pontual nos pontos de continuidade; convergência para a média dos limites laterais nos saltos (Dirichlet); convergência em média quadrática na classe explicitamente definida; fenômeno de Gibbs; truncamento computacional; interpretação física do espectro. A obrigação de "convergência quase em todo ponto" fica **removida do contrato**: em generalidade exige medida e integração de Lebesgue, que os Caps. 9 e 10 não constroem — e cuja adição violaria o antienciclopedismo. Se mencionada, entra como porta explicitamente fechada para um segundo ciclo. Dependências: Caps. 5, 7, 8, 9 e 10 — todos anteriores na leitura e na produção. A música retorna aqui não como metáfora, mas como dado analisável, imediatamente antes da síntese.

**Capítulo 12 — consequência, não ícone (critério corrigido por E16).** A identidade e^{iπ} + 1 = 0 será decomposta em dependências: 0 (identidade aditiva, origem e limite); 1 (identidade multiplicativa); i (extensão de ℝ para ℂ, Cap. 7); π (geometria e periodicidade); e (exponencial por séries, Cap. 10); exponenciação complexa (Cap. 10); fórmula de Euler; avaliação em θ = π. Critério de fechamento operacional: **nenhuma etapa central poderá depender de resultado não demonstrado no tratado, não explicitamente importado como teorema clássico ou não representado no grafo de dependências do `claims.yml`**. "Nenhum é sabido que" era promessa metafísica; ausência de dependência implícita é gate verificável. A última página deverá mostrar a diferença entre "conheço a fórmula" e "a fórmula agora é inevitável".

---

## 4. Mapa de absorção do antigo Volume V (renumerado por E7)

| Elemento prospectado | Destino canônico |
|---|---|
| Defeito ou resíduo de fechamento | Gramática transversal; Caps. 5, 9 e 12 |
| Calendário, segundo atômico e precisão física | Cap. 5 |
| Número versus numeral | Cap. 4 e Cap. 8 |
| Bases como ecossistemas de divisibilidade | Cap. 4 |
| Fuga inevitável dos primos | Cap. 4 |
| Sete como primeiro grande exilado decimal | Cap. 4 |
| Consonância 5-smooth | Cap. 5 |
| Coma pitagórica e temperamento | Cap. 5 |
| Classificação das ternas do ímpar | Cap. 2 |
| Recíproca e unicidade da família | Cap. 2 |
| Semiperímetro triangular | Cap. 2 |
| Inraio e ex-raio consecutivos | Cap. 2 |
| Parábolas L(n) e R(n) | Experimento computacional do Cap. 2 |
| Operações inversas não injetivas | Caps. 7 e 10 |
| Zero e infinito | Cap. 9 |
| Raízes e logaritmos multivalorados | Cap. 7 (argumento) e Cap. 10 (exponencial) |
| Método intuição → prova → recíproca | Doutrina e template de capítulo |
| Geometria não euclidiana | Segundo ciclo |
| Compactificação e esfera de Riemann | Segundo ciclo |
| Topologia geral | Segundo ciclo |
| Probabilidade e estatística | Segundo ciclo, se surgir sítio (§11) |
| Teoria analítica dos números e função zeta | Fora do primeiro ciclo |
| Números p-ádicos e geometria aritmética | Fora do primeiro ciclo |

A absorção não é uma redução de importância. É controle de arquitetura.

---

## 5. Duas ordens explícitas (E7)

**Ordem canônica de leitura** — a numeração dos capítulos:

```
0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 12
```

Topologicamente compatível com as dependências: Fourier (11) sucede integral (9) e séries de funções (10); a porta fechada do Cap. 2 abre no 7; a exponencial complexa do 7 abre no 10.

**Ordem operacional de produção:**

```
1 → 0 → 2 → 3 → 4 → 6 → 7 → 5 → 8 → 9 → 10 → 11 → 12
```

As justificativas abaixo são **exclusivamente de produção** — descrevem a ordem em que o autor constrói, não a ordem em que o leitor recebe:

- **Capítulo 0 depois do 1 (E20):** o prólogo nasceu da crítica do leitor primário ao Capítulo 1 já produzido — a configuração dual (duas circunferências, um polígono) e a cunha fundamental surgiram como o que faltava *antes*. A leitura recebe o prólogo primeiro; a produção o recebeu depois. Registrar isso é mais honesto que fingir planejamento prévio.
- **Capítulo 3 cedo:** o menor sítio valida o formato mínimo com custo baixo. Deve provar que o projeto consegue produzir densidade sem gigantismo.
- **Capítulo 6 produzido antes do 5:** o autor endurece primeiro sua própria desconfiança de gráficos e regularidade visual, e escreve o Cap. 5 já vacinado. Na leitura, o 5 vem antes do 6 sem dependência lógica: frações contínuas não exigem ε-δ.
- **Capítulo 7 produzido antes do 5:** disponibiliza ao autor a linguagem de rotação e fase enquanto redige a ponte musical. Não é pré-requisito de leitura.
- **Bloco final em ordem numérica:** integral (9) → fábrica (10) → Fourier (11) → síntese (12), eliminando a inversão de dependência da revisão anterior tanto na produção quanto na leitura.

Quando um capítulo antecipar uma ideia futura, deverá marcá-la como porta fechada e indicar onde será reaberta. A ordem de produção não autoriza dependências circulares silenciosas — e a ordem de leitura tampouco.

---

## 6. Template de capítulo

### 6.1 Elementos obrigatórios

1. **Declaração de tipo** — escavação | território virgem.
2. **Pergunta registrada antes do desenvolvimento** — data; formulação original; contexto. (Nas escavações, vale a cláusula de retrospectividade da §1.3.)
3. **Conjecturas datadas** — confiança inicial; exemplos; possíveis refutadores; autópsia, quando aplicável.
4. **Dossiê do sítio** — fragmentos originais; citações verbatim; arquivos de origem; distinção entre memória, registro e reconstrução posterior.
5. **Ledger de afirmações** — `claims.yml` com campos ortogonais (§1.4); dependências resolvíveis; localização da prova; artefatos de verificação.
6. **Demonstração canônica** — hipóteses; domínio; derivação; casos especiais; recíproca, quando matematicamente pertinente; limites do resultado.
7. **Experimento computacional inline** — controles; valores legíveis; código determinístico quando possível; capacidade de procurar contraexemplos; explicação do que o experimento não prova.
8. **Gate de verificação** — na versão vigente (§1.7).
9. **Horizonte** — pergunta que o capítulo torna inevitável; porta que permanece fechada; capítulo em que será reaberta.

### 6.2 Elementos opcionais

Entram apenas quando organicamente necessários: Prova sem palavras · Traduza o objeto · O erro também tem forma · História de uma ideia · Matemática e música · Autópsia de uma conjectura · O computador quase mentiu · Mesma estrutura, outra representação · Recíproca · Caso degenerado · Porta trancada.

### 6.3 Forma mínima

Não existe extensão mínima em palavras, páginas ou telas. Existe **completude mínima**: pergunta preservada; obstáculo localizado; resultado demonstrado; implementação verificada; limites declarados.

Um capítulo de três páginas pode estar completo. Um capítulo de cem telas pode continuar epistemologicamente vazio.

---

## 7. Estrutura do repositório

```
matheus-tratado/
├── MATH3us.md
├── README.md
├── schemas/
│   └── claims.schema.json          # entra com o gate v1
├── caps/
│   ├── 01-exaustao/
│   │   ├── index.html
│   │   ├── conjecturas.md
│   │   ├── claims.yml
│   │   ├── sources.md
│   │   └── audit/
│   │       ├── desktop.png
│   │       ├── iphone.png
│   │       ├── interaction-report.json
│   │       ├── symbolic-check.md
│   │       ├── numeric-check.json
│   │       └── edge-cases.md
│   ├── 02-ternas/
│   ├── ...
│   ├── 09-integral/
│   ├── 10-fabrica/
│   ├── 11-fourier/
│   └── 12-euler/
├── lib/
│   ├── plots/
│   ├── geometry/
│   ├── number-theory/
│   └── ui/
├── tools/
│   ├── audit.mjs                   # gate v0
│   ├── oracle.py                   # gate v0
│   ├── verify-claims.mjs           # gate v1
│   ├── bundle.mjs                  # gate v2 (automatiza invariante já vigente)
│   └── validate-release.mjs        # gate v2
└── releases/
    └── manifests/
```

**Regras estruturais**

- Um capítulo corresponde a um diretório; um capítulo fechado, a uma tag de release imutável na convenção da §1.7.
- `conjecturas.md` é criado antes de `index.html`. O pré-registro recebe commit separado.
- `claims.yml` é legível por máquina; validado por schema a partir do gate v1.
- `sources.md` registra origem, escopo e estado de cada material utilizado.
- O diretório `audit/` faz parte da release.
- `lib/` é permitido no desenvolvimento. A autocontenção do `index.html` de release é invariante desde o v0 (verificação manual em v0/v1; automatizada pelo `bundle.mjs` em v2). Nenhuma release depende de CDN, fonte remota, API externa ou conexão de rede, salvo decisão explicitamente documentada.
- Nunca delegar busca em arquivos de conversa a subagente. A mineração de sítios é realizada inline, em série, preservando contexto e cadeia de proveniência.

---

## 8. Schema de afirmações (E6, E13)

Exemplo de `claims.yml` com campos ortogonais, verificação apontando artefatos e dependências resolvíveis:

```yaml
chapter: 2
claims:
  - id: chapter-02.odd-triple-forward
    statement: >
      For every odd integer n >= 3,
      (n, (n^2 - 1)/2, (n^2 + 1)/2)
      is a primitive Pythagorean triple.
    kind: theorem
    status: proved
    provenance: rediscovered
    proof_mode: proved_here
    dependencies:
      - claim: "chapter-02.parity-lemma"
      - claim: "chapter-02.euclid-parameterization"
    proof_location: "#demonstracao-direta"
    verification:
      symbolic:
        status: passed
        artifact: "audit/symbolic-check.md"
      numeric:
        status: passed
        artifact: "audit/numeric-check.json"
        implementation: "tools/oracle.py"
      edge_cases:
        status: passed
        artifact: "audit/edge-cases.md"

  - id: chapter-02.consecutive-classification
    statement: >
      Every integer right triangle whose larger leg and
      hypotenuse differ by one belongs to the odd family.
    kind: theorem
    status: proved
    provenance: derived_in_treatise
    proof_mode: proved_here
    dependencies:
      - claim: "chapter-02.odd-triple-forward"
    proof_location: "#reciproca"
    verification:
      symbolic: { status: passed, artifact: "audit/symbolic-check.md" }
      numeric:  { status: passed, artifact: "audit/numeric-check.json", implementation: "tools/oracle.py" }
      edge_cases: { status: passed, artifact: "audit/edge-cases.md" }

  - id: chapter-02.inradius-exradius-identity
    statement: >
      In the odd family, r = (n-1)/2 and the exradius opposite
      the odd leg is (n+1)/2; hence they differ by one.
    kind: theorem
    status: proved
    provenance: derived_in_treatise
    proof_mode: proved_here
    proof_location: "#geometria-interna"
    verification:
      symbolic: { status: passed, artifact: "audit/symbolic-check.md" }
      numeric:  { status: passed, artifact: "audit/numeric-check.json", implementation: "tools/oracle.py" }
      edge_cases: { status: passed, artifact: "audit/edge-cases.md" }

  - id: chapter-02.consecutive-integers-triple-role
    statement: >
      The same consecutive integers (n-1)/2 and (n+1)/2 appear
      as Euclid parameters, as inradius and exradius, and as the
      family's second structural consecutiveness.
    kind: synthesis
    status: supported
    provenance: authorial
    proof_mode: not_applicable
    priority_note: >
      Authorial synthesis within this treatise;
      historical priority not established.
    dependencies:
      - claim: "chapter-02.inradius-exradius-identity"
      - claim: "chapter-02.odd-triple-forward"
```

O par de claims final demonstra a separação exigida por E6: a identidade é teorema demonstrado; a coincidência organizacional é síntese.

**Deveres do `verify-claims.mjs` (E13):** IDs únicos; dependências existentes e resolvíveis (erro ortográfico não pode criar dependência fantasma silenciosa); ausência de ciclos proibidos; âncoras de prova existentes no HTML; artefatos de auditoria existentes nos caminhos declarados; compatibilidade entre `kind`, `status` e `proof_mode`; capítulos dependentes já fechados ou explicitamente marcados como porta futura.

Campos inválidos, combinações incompatíveis ou artefatos ausentes bloqueiam a release (validação manual no gate v0; automática a partir do v1).

**Proveniência do oráculo (E12):** após execução real, o registro assume a forma:

```yaml
oracle_run:
  script: tools/oracle.py
  report: caps/02-ternas/audit/numeric-check.json
  code_commit: abc1234
  environment: "python 3.12, stdlib only"
  date: 2026-XX-XX
  tested_domain:
    odd_n: { min: 3, max: 20001, step: 2 }
    adversarial_even: [2, 4, 100]
```

---

## 9. Protocolo de sessão de trabalho

**Abertura**

1. Identificar o capítulo corrente.
2. Ler `conjecturas.md`.
3. Ler `claims.yml`.
4. Separar: afirmado; observado; demonstrado; refutado; ainda não investigado.
5. Definir uma única meta verificável para a sessão.

**Mineração de sítio**

1. Buscar arquivos antes de formalizar.
2. Preservar citações verbatim quando existirem.
3. Registrar a origem em `sources.md`.
4. Diferenciar: fala original; transcrição; resumo posterior; reconstrução atual.
5. Não preencher lacunas documentais com memória apresentada como fato.

**Desenvolvimento**

1. Formular o enunciado com domínio explícito.
2. Tentar refutá-lo antes de prová-lo.
3. Procurar os menores casos.
4. Procurar casos extremos.
5. Produzir derivação simbólica.
6. Executar verificação independente.
7. Implementar experimento visual.
8. Atualizar `claims.yml` no mesmo commit da alteração conceitual.

**Encerramento**

1. Rodar o oráculo triplo.
2. Rodar testes locais pertinentes.
3. Registrar novas conjecturas com data.
4. Atualizar a lista de falhas previstas.
5. Fazer commit descritivo em inglês.
6. Declarar explicitamente o que permaneceu incompleto.

Exemplo de commit: `prove reciprocal classification for consecutive odd triples`

Não encerrar uma sessão com "praticamente pronto". Registrar exatamente o que falta.

---

## 10. Definição de capítulo fechado

A lista aplica-se **sob o gate vigente** (§1.7): itens cuja *automação* pertence a gates posteriores são verificados manualmente até lá — os invariantes em si valem desde o v0.

Um capítulo só pode receber release quando:

- a pergunta original está preservada;
- as conjecturas anteriores ao texto estão registradas (ou o estado documental do sítio, nas escavações);
- conjecturas refutadas possuem autópsia;
- o resultado central está corretamente enunciado;
- as hipóteses estão declaradas;
- a demonstração foi revisada;
- a recíproca foi considerada;
- casos extremos foram examinados;
- o experimento computacional funciona;
- o experimento não é apresentado como prova;
- todos os invariantes numéricos passaram pelo oráculo triplo, com artefatos em `audit/`;
- `claims.yml` está válido, com campos ortogonais, dependências resolvíveis e artefatos existentes;
- as fontes estão registradas;
- o HTML funciona sem rede (verificação manual em v0/v1; `validate-release.mjs` em v2);
- o empacotamento foi produzido (manual em v0/v1; `bundle.mjs` em v2);
- Playwright passou em desktop;
- Playwright passou em viewport de iPhone;
- screenshots foram inspecionados;
- não há overflow ou clipping relevante;
- a acessibilidade funcional mínima (§1.7) foi verificada no nível adequado a cada figura;
- a release foi efetivamente vista;
- existe pergunta-horizonte;
- a tag de release, imutável e na convenção da §1.7, aponta para o commit auditado.

A ausência de qualquer item vigente mantém o capítulo aberto.

---

## 11. Fora de escopo do primeiro ciclo (reformulado por E17)

Estas exclusões são decisões explícitas de escopo, não esquecimentos — e não constituem autoavaliação de competência. Os territórios abaixo são adiados por **ausência atual de necessidade interna**, não porque já estejam dominados.

**Probabilidade e estatística.** Nenhum sítio documental atualmente identificado em probabilidade ou estatística satisfaz o critério de corte do primeiro ciclo. O território permanece adiado até que surja uma falha demonstrativa concreta — candidatos naturais, se surgirem: inferência causal, Bayes, calibração, decisão sob incerteza, interpretação de ensaios.

**Topologia geral.** Adiada até que um problema interno do tratado torne indispensáveis: abertos e fechados; continuidade topológica; compactação; conexidade; quocientes; recobrimentos.

**Geometria não euclidiana e diferencial.** Adiada porque sua entrada adequada exige mais que analogias sobre curvatura. Deverá depender de uma necessidade demonstrativa concreta envolvendo métrica, geodésica ou variedade.

**Superfícies de Riemann.** O primeiro ciclo apresenta escolha de ramo do argumento e multivaloração (Cap. 7). A construção completa pertence a um ciclo posterior.

**Teoria da medida e integração de Lebesgue.** Excluídas explicitamente (E10): sua ausência é o que delimita o contrato de Fourier à classe suave por partes.

**Teoria analítica dos números.** Função zeta, distribuição de primos, teorema dos números primos e hipótese de Riemann não entram como expansão natural do Capítulo 4. Exigem projeto próprio.

**Números p-ádicos, teoria de Galois e geometria aritmética.** Permanecem como horizontes, não como promessas editoriais.

---

## 12. Cláusula de honestidade

Este livro tem valor na exata medida em que registra:

- falhas previstas que se confirmaram;
- falhas previstas que não se confirmaram;
- falhas não previstas;
- conjecturas corretas por motivos errados;
- conjecturas erradas que continham uma estrutura aproveitável;
- demonstrações que precisaram ser abandonadas;
- experimentos que quase produziram uma mentira convincente;
- resultados conhecidos que foram genuinamente redescobertos;
- conexões autorais cuja prioridade ainda não foi estabelecida.

As categorias são dados.

A pior corrupção possível do projeto é editar o passado para parecer mais inteligente. Isso o transformaria em currículo, e currículo já existe nas livrarias. A corrupção simétrica também é proibida: apagar um evento verdadeiro para parecer processualmente puro (ver E12 — a verificação exploratória do Cap. 2 foi rebaixada e declarada, não apagada).

O tratado não deve provar que Matheus estava sempre certo. Deve mostrar, com resolução suficiente, como uma intuição se transforma em matemática — e exatamente onde ela deixa de ser apenas intuição.

---

## 13. Registro de emendas (governança por E18)

Regras: emendas são **atômicas** — uma decisão por emenda; emendas nunca são reescritas retroativamente — uma nova emenda revoga ou corrige a antiga; cada emenda referencia commit quando o repositório existir ("—" indica fase pré-repositório).

| Emenda | Data | Commit | Seções | Substitui/corrige | Conteúdo |
|---|---|---|---|---|---|
| E1 | 28/07/2026 | — | §0 | — | MATHeus.md → MATH3us.md; redação precisada: o caractere 3 é numeral que representa o número três e substitui graficamente o "E" |
| E2 | 28/07/2026 | — | §1.3 | — | Cláusula de retrospectividade das escavações |
| E3 | 28/07/2026 | — | §5 | — | Fourier movido para depois de integral e séries **na produção** (correção completada por E7) |
| E4 | 28/07/2026 | — | §1.7 | — | Gate versionado v0/v1/v2 (corrigido por E9) |
| E5 | 28/07/2026 | — | §1.4, §3 | — | Enum de estados; Cap. 2 comprimido a contrato; ancoragem de resíduos (emenda não atômica; decomposta e corrigida por E6, E8; a compressão do Cap. 2 permanece válida) |
| E6 | 28/07/2026 | — | §1.4, §8 | corrige E5 | Ledger normalizado: `kind`/`status`/`provenance`/`proof_mode` ortogonais + `role` opcional; um enum único fundia estado, proveniência e função |
| E7 | 28/07/2026 | — | §3, §4, §5, §7 | completa E3 | Dupla ordem explícita; renumeração: Integral = 9, Fábrica = 10, Fourier = 11; ordem de leitura topologicamente compatível com dependências |
| E8 | 28/07/2026 | — | §2.2, §3 | corrige E5 | Resíduo corrigido: domínios A,B > 0; assimetria declarada; forma canônica com q ∈ ℤ livre; L̃ normalizado por razão de logaritmos; promessa sobre convergentes restrita (semiconvergentes reconhecidos) |
| E9 | 28/07/2026 | — | §0, §1.7, §7, §10 | corrige E4 | Autocontenção invariante desde v0 (v2 automatiza, não inaugura); endurecimento não autoriza reescrita silenciosa; convenção de tags imutáveis e manifest |
| E10 | 28/07/2026 | — | §3 (Cap. 11), §11 | — | Fourier restrito a classe suave por partes; "quase todo ponto" removido do contrato (exigiria Lebesgue); Dirichlet nos saltos; média quadrática em classe declarada |
| E11 | 28/07/2026 | — | §3 (Cap. 7) | — | Cap. 7 sem exponencial: cos θ + i·sin θ geométrico; e^{iθ} em porta fechada até o Cap. 10; log complexo formal/adiado; w ≠ 0; notação Arg |
| E12 | 28/07/2026 | — | §1.5, §3 (Cap. 2), §8 | — | Proveniência executável: alegações de oráculo exigem artefato, hash, domínio, ambiente e data; verificação de 28/07/2026 rebaixada a exploratória não canônica — declarada, não apagada |
| E13 | 28/07/2026 | — | §8 | — | `claims.yml` aponta artefatos em vez de booleanos; dependências resolvíveis com namespace; deveres do `verify-claims.mjs` |
| E14 | 28/07/2026 | — | §1.7 | refina E4 | Acessibilidade em dois níveis (figura simples vs. analítica/interativa); fórmulas com representação textual ou MathML |
| E15 | 28/07/2026 | — | §1.3 | complementa E2 | Falsificabilidade do contrato editorial: proposição contratada falsa deve ser refutada com emenda; o contrato não obriga a matemática a obedecer ao planejamento |
| E16 | 28/07/2026 | — | §3 (Cap. 12) | — | "Nenhum é sabido que" substituído por critério verificável: nenhuma dependência fora do grafo do `claims.yml` ou da importação explícita |
| E17 | 28/07/2026 | — | §11 | — | Fora de escopo reformulado: adiamento por ausência de sítio, não por competência presumida |
| E18 | 28/07/2026 | — | §13 | — | Governança de emendas: atomicidade; imutabilidade; colunas de commit, seções e substituição |
| E19 | 28/07/2026 | — | §3 (Cap. 10) | — | a⁰/0⁰ como interlúdio do Cap. 10; núcleo protegido: séries de potências como definição de função |
| E20 | 28/07/2026 | — | §3, §5 | — | Capítulo 0 (A Inferência) criado como Prólogo: duas circunferências e um polígono; cunha fundamental; inferência sob erro por desigualdades, sem linguagem de limite; π entra como constante de área (identificação perimetral: porta → Cap. 9); numeração 1–12 inalterada; reconstrução geométrica do Cap. 1 sobre a cunha registrada como pendência editorial |
