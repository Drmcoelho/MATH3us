# architecture.md — Arquitetura editorial, epistemológica e operacional do MATH3us

> Documento prospectivo subordinado a [MATH3us.md](MATH3us.md).
>
> **Objeto:** organizar o tratado em uma arquitetura de longo prazo — Volumes I–V, ondas de desenvolvimento, micro-ondas internas dos capítulos, dependências, portas, regime visual, estrutura de repositório e critérios de fechamento — sem transformar prospecção em contrato matemático por decreto.
>
> **Regra de precedência:** em qualquer conflito, `MATH3us.md` vence. `architecture.md` descreve a forma futura pretendida; `STATUS.md`, quando criado, descreve o estado presente; `ROADMAP.md` descreve a fila operacional vigente; `AUDIT.md` preserva o histórico de decisões e verificações.

---

## 0. Por que este documento existe

O MATH3us já possui uma constituição epistemológica robusta, contratos editoriais para o primeiro ciclo, gates versionados, releases imutáveis por capítulo e uma política multiagentes baseada em ondas. O que ainda não estava formalizado era a arquitetura acima do capítulo: como o primeiro ciclo se relaciona com os ciclos seguintes, que assuntos pertencem a cada macroarco, como impedir que “volume” se torne sinônimo de acúmulo enciclopédico e como preservar a doutrina do tratado quando a matemática avançar para geometria não euclidiana, topologia, medida, probabilidade, análise complexa e geometria aritmética.

Este documento resolve essa lacuna por meio de cinco distinções:

1. **capítulo é unidade epistemológica e de release; volume é unidade editorial e de leitura**;
2. **onda é unidade de coordenação; micro-onda é unidade de maturação interna de um capítulo**;
3. **porta é antecipação declarada; dependência é resultado já disponível e resolvível**;
4. **prospecção define horizonte; contrato editorial define obrigação demonstrativa**;
5. **imagem matemática nasce de construção verificável; imagem generativa é, no máximo, referência estética**.

O documento não cria automaticamente novos capítulos. Um título prospectado só se torna capítulo contratado quando passa pelo critério de corte do manual, tem sítio ou falha futura identificada, recebe dependências explícitas e é incorporado ao manual por emenda.

---

# PARTE I — CAMADAS DE AUTORIDADE

## 1. Documentos e responsabilidades

| Documento | Função | Pode conter estado corrente? | Pode criar obrigação matemática? |
|---|---|---:|---:|
| `MATH3us.md` | Constituição, doutrina, contratos editoriais e emendas | apenas quando estrutural | sim |
| `architecture.md` | Arquitetura de longo prazo e mapa prospectivo | apenas marcos amplos | não, sozinho |
| `STATUS.md` | Fotografia curta e factual do repositório | sim | não |
| `ROADMAP.md` | Fila de produção, ondas ativas, pré-condições e propriedade de arquivos | sim | não |
| `models.md` | Protocolo de agentes e paralelismo | sim, operacional | não |
| `AUDIT.md` | Registro histórico de verificações, decisões e incidentes | sim, como história | não |
| `CODEX.md` / `docs/codex.md` | Fila consolidada de pendências | sim | não |
| `claims.yml` | Ledger de afirmações de um capítulo | sim, por claim | sim, localmente |
| manifest de release | Identidade imutável de uma release | sim | não |

### 1.1 Regra de não duplicação

Uma informação deve possuir uma fonte primária clara:

- doutrina → `MATH3us.md`;
- arquitetura futura → `architecture.md`;
- estado presente → `STATUS.md`;
- fila de trabalho → `ROADMAP.md`;
- histórico → `AUDIT.md`;
- verdade matemática local → `claims.yml` e prova no capítulo.

Textos secundários podem resumir, mas devem apontar para a fonte primária e não permanecer semanticamente ativos depois de ficarem obsoletos.

---

# PARTE II — VOCABULÁRIO ARQUITETURAL

## 2. Unidades do tratado

### 2.1 Obra

A obra é o repositório vivo completo. Não possui estado “terminado”. Pode atravessar múltiplos ciclos e volumes.

### 2.2 Ciclo

Ciclo é um arco de maturação intelectual com dependências relativamente fechadas. Um ciclo pode coincidir com um volume, mas não precisa. O primeiro ciclo corresponde ao atual arco `0 → 12`.

### 2.3 Volume

Volume é uma **macroestrutura editorial** composta por capítulos independentes. Organiza leitura, tese, ritmo e síntese. Não é unidade de release e não possui `claims.yml` coletivo.

Um volume:

- tem tese central;
- possui pré-requisitos declarados;
- contém capítulos com contratos próprios;
- culmina, preferencialmente, em capítulo de síntese;
- pode permanecer prospectivo por anos sem contaminar o estado dos capítulos existentes;
- não permite que capítulo incompleto seja escondido pela expressão “volume em andamento”.

### 2.4 Parte

Parte é agrupamento temático interno a um volume. Não altera o tipo epistêmico do capítulo.

### 2.5 Capítulo

Capítulo é a unidade de entrega, prova, auditoria e release. Cada capítulo possui pergunta, tipo, ledger, demonstração, experimento, exercícios, auditoria e horizonte.

### 2.6 Onda

Onda é um conjunto coordenado de frentes que podem ser produzidas em paralelo porque possuem diretórios disjuntos e dependências satisfeitas.

Uma onda não afirma que seus capítulos têm o mesmo peso; afirma apenas que podem amadurecer simultaneamente sem violar o grafo.

### 2.7 Micro-onda

Micro-onda é uma fase interna de maturação de um capítulo. Todo capítulo atravessa a mesma sequência mínima, ainda que algumas fases sejam curtas.

### 2.8 Porta

Porta é uma dependência futura explicitamente não resolvida. Deve declarar:

- pergunta ou resultado antecipado;
- por que não pode ser resolvido agora;
- capítulo ou volume de reabertura;
- quais ferramentas ainda faltam.

### 2.9 Síntese

Síntese é organização autoral de resultados demonstrados ou importados. Não deve receber `proof_mode: proved_here` quando o que está sendo provado são os teoremas componentes.

---

## 3. Estados editoriais prospectivos

Os itens deste documento usam quatro estados, distintos dos estados dos claims:

| Estado | Significado |
|---|---|
| **canônico** | já contratado no `MATH3us.md` |
| **candidato forte** | encaixe arquitetural e dependências claros; falta emenda contratual |
| **condicionado** | depende de mineração de sítio, decisão do autor ou fundação ainda inexistente |
| **fora do ciclo** | reconhecido, mas deliberadamente excluído do arco atual |

Nenhum item candidato ou condicionado deve aparecer no portal público como capítulo previsto antes de sua incorporação ao manual.

---

# PARTE III — HIERARQUIA DE DEPENDÊNCIAS

## 4. Grafo macro dos volumes

```text
Volume I — número, prova, contínuo e funções
        │
        ├──→ Volume II — métrica, geometria e curvatura
        │          │
        │          └──→ Volume III — topologia, análise complexa e compactificação
        │                         │
        │                         └──→ Volume V — aritmética local-global e geometria aritmética
        │
        └──→ Volume IV — medida, probabilidade e decisão
                         │
                         └───────→ Volume V — linguagem de medida e distribuição quando necessária
```

O Volume V depende principalmente do III, mas pode importar ferramentas do IV quando a apresentação de densidades, distribuições ou heurísticas exigir uma linguagem de medida já construída.

## 4.1 Dependência não é ordem de inspiração

A ordem de leitura segue dependências. A ordem em que uma pergunta surgiu na vida do autor pode ser diferente e deve permanecer registrada no sítio.

## 4.2 Proibição de circularidade silenciosa

Um capítulo não pode usar uma ferramenta futura e depois alegar que o capítulo futuro apenas a “explica melhor”. As opções honestas são:

1. importar formalmente um teorema clássico e registrá-lo;
2. marcar a passagem como porta;
3. reordenar os capítulos;
4. reduzir o contrato atual.

---

# PARTE IV — ARQUITETURA COMUM DOS CAPÍTULOS

## 5. As sete micro-ondas

### M0 — sítio, pergunta e pré-registro

Entregáveis:

- `conjecturas.md` em commit próprio;
- pergunta datada;
- formulação original e reconstruída;
- exemplos disponíveis;
- confiança inicial;
- possíveis refutadores;
- classificação escavação/território virgem;
- lacunas documentais declaradas.

Critério de saída: é possível dizer exatamente qual obstáculo justifica o capítulo.

### M1 — contrato e grafo de claims

Entregáveis:

- primeira versão de `claims.yml`;
- claim central;
- lemas necessários;
- recíproca, quando pertinente;
- domínio e casos degenerados;
- dependências intercapítulos;
- portas futuras;
- mapa `claim → proof_location → verification`.

Critério de saída: nenhum elemento visual ou seção de prosa está sendo construído sem saber qual claim serve.

### M2 — fundação visual exata

Entregáveis:

- `source/visual-spec.md`;
- figuras calculadas ou construídas;
- geradores versionados;
- invariantes geométricos e semânticos;
- equivalentes textuais;
- desenho dos objetos antes da fórmula;
- protótipo de layout em desktop e mobile.

Critério de saída: toda figura central pode ser regenerada e explicada sem depender da interpretação estética de um modelo generativo.

### M3 — demonstração canônica

Entregáveis:

- hipóteses;
- derivação completa;
- justificativa de cada passagem;
- direta e recíproca;
- classificação, quando prometida;
- limites do resultado;
- distinção entre prova, observação e importação.

Critério de saída: a prova continua válida se todas as animações forem removidas.

### M4 — experimento computacional

Entregáveis:

- implementação principal;
- implementação numérica independente;
- controles e parâmetros;
- casos adversariais;
- busca de contraexemplo;
- tabela textual equivalente;
- declaração explícita do que o experimento não prova.

Critério de saída: o experimento pode contrariar a intuição do autor e registrar a refutação.

### M5 — transferência socrática e aplicabilidade

Entregáveis:

- exercícios N0–N4;
- gabaritos robustos N0–N3;
- N4 com porta declarada;
- ao menos uma transferência para outra representação;
- aplicação cotidiana, científica ou tecnológica quando estruturalmente real;
- caixa de curiosidade apenas se ancorada;
- caixa de segredo oculto apontando para diante.

Critério de saída: o leitor demonstra compreensão operando o aparato, não repetindo frases.

### M6 — oráculo, render, auditoria e release

Entregáveis:

- derivação simbólica registrada;
- verificação numérica independente;
- casos extremos;
- gate vigente;
- screenshots desktop e iPhone;
- auditoria de acessibilidade;
- inspeção humana do render;
- manifest, decisão e tag quando autorizado.

Critério de saída: capítulo fechado nos termos do manual.

---

## 6. Estrutura-alvo de um capítulo

```text
caps/NN-slug/
├── index.html
├── conjecturas.md
├── claims.yml
├── sources.md
├── source/
│   ├── visual-spec.md
│   ├── figures.yml
│   ├── figures/
│   │   ├── figure-01.svg
│   │   └── figure-02.svg
│   ├── generators/
│   │   ├── figure-01.mjs
│   │   └── figure-02.py
│   ├── data/
│   │   └── canonical-cases.json
│   └── drafts/
│       └── moodboard.png
└── audit/
    ├── symbolic-check.md
    ├── numeric-check.json
    ├── edge-cases.md
    ├── interaction-report.json
    ├── figure-invariants.json
    ├── desktop.png
    └── iphone.png
```

`source/` é área de construção. O `index.html` de release continua autocontido.

---

## 7. Regime visual: fonte, derivado e testemunha

### 7.1 Fonte

É o objeto editável e verificável:

- SVG semântico;
- código gerador;
- coordenadas;
- dados;
- especificação textual;
- expressões matemáticas.

### 7.2 Derivado

É produzido a partir da fonte:

- SVG otimizado;
- canvas renderizado;
- fragmento inline no HTML;
- imagem de divulgação.

### 7.3 Testemunha

É evidência de que a entrega foi vista e funcionou:

- screenshot;
- relatório de interação;
- hash;
- comparação de invariantes;
- registro de viewport.

### 7.4 Imagem generativa

Imagem criada por modelo generativo:

- pode compor `source/drafts/` como moodboard;
- não constitui demonstração;
- não pode conter fórmula central rasterizada como fonte canônica;
- não pode ser usada para afirmar tangência, escala, convergência, proporcionalidade ou contagem sem reconstrução calculada;
- não substitui SVG, Canvas, tabela ou prova.

### 7.5 Manifesto de figura

Cada figura analítica deve possuir entrada em `figures.yml`:

```yaml
figures:
  - id: chapter-02.odd-triple-family
    source: source/generators/odd-triples.mjs
    output: source/figures/odd-triples.svg
    claims:
      - chapter-02.odd-triple-forward
      - chapter-02.consecutive-classification
    invariants:
      - right_angle_is_exact
      - side_labels_match_generated_values
      - hypotenuse_minus_larger_leg_equals_one
    accessible_equivalent: "#odd-triples-table"
```

---

## 8. Arquitetura de leitura do front-end

Todo capítulo longo deve oferecer:

- título e declaração de tipo;
- pergunta central em uma frase;
- mapa local do capítulo;
- navegação anterior · índice · próximo;
- âncoras estáveis;
- indicador de portas abertas e fechadas;
- progresso editorial, não gamificado;
- rodapé recolhível para metadados extensos;
- retorno ao início;
- nenhuma dependência do botão “voltar” do navegador.

### 8.1 Rodapé

O rodapé deve conter apenas metadados cuja presença no documento publicado seja necessária:

- release;
- gate;
- revisão;
- commit;
- links para ledger, fontes e auditoria;
- nota de errata, quando existir.

Narrativa histórica extensa pertence ao `AUDIT.md`, não ao rodapé visível por padrão.

### 8.2 Aplicação cotidiana

Aplicação não é um box ornamental. Deve responder:

1. qual estrutura do capítulo aparece no problema real;
2. quais hipóteses são satisfeitas;
3. quais não são;
4. o que a matemática permite concluir;
5. qual erro surge ao extrapolar.

Quando não houver aplicação cotidiana honesta, o capítulo declara isso. Não se inventa “utilidade” para legitimar matemática estrutural.

---

# PARTE V — PROGRAMA DOS CINCO VOLUMES

## 9. Visão geral

| Volume | Título | Pergunta estrutural | Estado |
|---|---|---|---|
| I | **Do Número ao Contínuo** | Como uma intuição se torna resultado demonstrado e ferramenta? | canônico, em produção |
| II | **A Geometria do que Permanece** | O que permanece quando coordenadas, escala ou geometria mudam? | candidato forte |
| III | **A Forma sem Medida** | O que resta quando distância e ângulo deixam de importar? | candidato forte |
| IV | **A Medida do Incerto** | Como representar e decidir sob informação incompleta? | condicionado à mineração de sítio |
| V | **A Geometria do que Não Fecha** | Como diferentes extensões, completamentos e locais resolvem ou preservam falhas de fechamento? | candidato forte, dependente dos Volumes III–IV |

---

# VOLUME I — DO NÚMERO AO CONTÍNUO

## 10. Estatuto

O Volume I corresponde ao primeiro ciclo já contratado nos capítulos 0–12. Seu título público permanece *Do Número ao Contínuo*.

### Tese

> Uma regularidade observada só se torna matemática do tratado quando seu domínio, prova, recíproca, erro, representação e limites são explicitados.

### Arco

```text
inferência geométrica
→ convergência
→ classificação aritmética
→ representação em bases
→ aproximação e resíduo
→ patologias
→ complexos
→ invariância linear
→ integral
→ séries de funções
→ Fourier
→ Euler como consequência
```

## 10.1 Partes

- Prólogo — Cap. 0;
- Parte I — escavações, Caps. 1–5;
- Parte II — territórios virgens, Caps. 6–8;
- Parte III — contínuo e síntese, Caps. 9–12.

## 10.2 Ondas já executadas

- Onda 0: Cap. 1;
- Onda 1: Caps. 2, 3 e 4;
- Onda 2: Caps. 6 e 7.

## 10.3 Ondas remanescentes

### Onda I-3 — pontes estruturais

- Cap. 5 — A Consonância;
- Cap. 8 — Álgebra Linear como Estrutura;
- revisão autorizada do Cap. 2, se a release-base estiver fechada.

Paralelismo recomendado: dois produtores e coordenadora.

### Onda I-4 — integral

- Cap. 9, isolado.

Pré-condição: Caps. 1–8 fechados e dependências resolvidas.

### Onda I-5 — fábrica de funções

- Cap. 10, isolado.

### Onda I-6 — Fourier

- Cap. 11, isolado.

### Onda I-7 — síntese

- Cap. 12, isolado.

### Onda I-R — fechamento editorial do volume

- verificar que todos os capítulos possuem releases;
- auditar grafo completo;
- eliminar portas internas que deveriam estar reabertas;
- construir portal do volume;
- emitir manifesto editorial do volume sem substituir tags de capítulo.

---

# VOLUME II — A GEOMETRIA DO QUE PERMANECE

## 11. Tese e função

> Geometria é o estudo das estruturas preservadas por uma classe declarada de transformações; não é sinônimo de desenho euclidiano.

O Volume II parte de álgebra linear, cálculo e números complexos do Volume I para reconstruir distância, geodésica, curvatura e geometria não euclidiana.

## 11.1 Pré-requisitos mínimos

- Cap. 7 — representação complexa de rotações;
- Cap. 8 — mudança de base e invariância;
- Cap. 9 — comprimento e integral;
- Cap. 10 — funções e séries quando necessárias.

## 11.2 Capítulos candidatos

### II.1 — A Régua

**Pergunta:** o que significa dizer que dois pontos estão próximos?

**Obrigações:**

- métrica e axiomas;
- norma e produto interno;
- desigualdade triangular;
- exemplos de métricas não euclidianas;
- equivalência e não equivalência de noções de distância;
- instrumento físico versus objeto matemático.

**Figuras:** bolas em diferentes métricas; comparação Euclidiana, Manhattan e máximo.

**Experimento:** arrastar pontos e alternar métricas, com tabela de distâncias.

**Aplicações:** rotas urbanas, similaridade de dados, imagens e planejamento de movimento.

**Porta:** variedades métricas e curvatura → II.4–II.5.

### II.2 — O Quinto Postulado

**Pergunta:** o que muda quando a unicidade das paralelas deixa de ser axioma?

**Obrigações:**

- enunciados equivalentes do quinto postulado;
- modelos euclidiano, esférico e hiperbólico;
- consistência relativa por modelos;
- distinção entre axioma, teorema e observação visual.

**Figuras:** mesma construção nos três regimes.

**Aplicações:** perspectiva, cartografia e navegação.

### II.3 — Triângulos que Não Somam 180°

**Pergunta:** a soma dos ângulos de um triângulo é propriedade do triângulo ou do espaço?

**Obrigações:**

- excesso esférico;
- déficit hiperbólico;
- relação com área em modelos declarados;
- limite local euclidiano;
- falhas de desenho plano ao representar superfícies curvas.

**Experimento:** triângulo móvel na esfera e no disco de Poincaré.

**Aplicações:** rotas aéreas, astronomia e geodesia.

### II.4 — Geodésicas

**Pergunta:** o caminho mais curto é sempre único?

**Obrigações:**

- comprimento de curva;
- minimização local versus global;
- geodésicas em plano, esfera, cilindro e toro;
- pontos conjugados e corte apenas no nível necessário;
- múltiplas soluções.

**Aplicações:** robótica, navegação e análise de superfícies anatômicas.

### II.5 — A Curvatura

**Pergunta:** uma superfície pode descobrir sua curvatura sem olhar de fora?

**Obrigações:**

- curvatura de curvas;
- primeira e segunda formas no nível compatível com o Volume I;
- curvatura gaussiana;
- intrínseco versus extrínseco;
- Teorema Egregium importado ou demonstrado em escopo declarado.

**Figuras:** cilindro versus esfera; mapas locais; transporte de vetores.

### II.6 — O Mapa Mente

**Pergunta:** quais propriedades um mapa pode preservar simultaneamente?

**Obrigações:**

- projeções;
- conformidade;
- preservação de área;
- distorção de distância;
- Jacobiano local;
- impossibilidade de isometria global esfera-plano.

**Aplicações:** Mercator, mapas epidemiológicos, imagens médicas e reconstrução de superfícies.

### II.7 — Localmente Plano, Globalmente Curvo

**Pergunta:** como informação local determina uma restrição global?

**Obrigações:**

- atlas local;
- curvatura total;
- característica de Euler;
- Gauss–Bonnet em classe declarada;
- ponte explícita para topologia.

**Síntese:** o volume termina quando “forma”, “medida” e “curvatura” deixam de ser sinônimos.

## 11.3 Ondas do Volume II

| Onda | Frentes | Dependência | Paralelismo |
|---|---|---|---:|
| II-0 | contrato, II.1 e biblioteca geométrica | Volume I fechado | 1 |
| II-1 | II.2 ∥ II.3 | II.1 | 2 |
| II-2 | II.4 ∥ II.5 | II.1–II.3 | 2 |
| II-3 | II.6 | II.4–II.5 | 1 |
| II-4 | II.7 | anteriores fechados | 1 |
| II-R | reauditoria e portal | todos | coordenadora |

Curva recomendada: **1 → 2 → 2 → 1 → 1**.

---

# VOLUME III — A FORMA SEM MEDIDA

## 12. Tese e função

> Topologia estuda propriedades preservadas por deformações contínuas; análise complexa mostra como estrutura local rígida produz consequências globais.

O Volume III remove progressivamente régua e ângulo, constrói vizinhança, conexão, compacidade, identificação e recobrimento, e retorna aos números complexos para resolver multivaloração e compactificação.

## 12.1 Pré-requisitos

- Volume II, especialmente atlas local, geodésica e curvatura;
- Caps. 6, 7, 9 e 10 do Volume I.

## 12.2 Capítulos candidatos

### III.1 — Vizinhanças

- conjuntos abertos;
- topologia;
- base topológica;
- interior, fecho, fronteira e aderência;
- múltiplas topologias no mesmo conjunto;
- comparação com métrica.

### III.2 — Continuidade sem Fórmula

- continuidade por pré-imagem de abertos;
- equivalência com ε–δ em espaços métricos;
- homeomorfismos;
- invariantes topológicos elementares;
- função versus gráfico.

### III.3 — Conexão

- conexidade;
- conexidade por caminhos;
- componentes;
- exemplos de divergência;
- alcance em redes e espaços.

### III.4 — Compacidade

- coberturas abertas;
- subcoberturas finitas;
- Heine–Borel;
- compacidade sequencial em espaços métricos adequados;
- compacidade como substituta estrutural da finitude.

### III.5 — Colar e Identificar

- espaços quociente;
- círculo como intervalo colado;
- cilindro, toro, faixa de Möbius e plano projetivo;
- diferença entre figura de imersão e espaço abstrato.

### III.6 — Buracos

- homotopia;
- laços;
- grupo fundamental;
- invariância;
- cálculo em exemplos essenciais;
- limite explícito do que ainda não foi construído em homologia.

### III.7 — Coberturas e Ramos

- espaços de recobrimento;
- levantamento de caminhos;
- argumento;
- logaritmo complexo;
- raízes multivaloradas;
- monodromia;
- reabertura das portas do Cap. 7.

### III.8 — Superfícies de Riemann

- cartas complexas;
- funções de transição;
- tornar relações multivaloradas univaloradas em espaço apropriado;
- exemplos mínimos: raiz, logaritmo e superfícies algébricas simples.

### III.9 — Holomorfia, Contornos e Resíduos

- derivabilidade complexa;
- equações de Cauchy–Riemann;
- integral de contorno;
- teorema de Cauchy em classe declarada;
- fórmula integral;
- resíduos;
- princípio do argumento.

Este capítulo é fundação obrigatória para o Volume V. A função zeta não pode aparecer antes dele como objeto global completo.

### III.10 — A Esfera de Riemann

- compactificação de ℂ;
- projeção estereográfica;
- ponto no infinito;
- transformações de Möbius;
- distinção entre infinito como comportamento e ponto de compactificação.

## 12.3 Ondas do Volume III

| Onda | Frentes | Paralelismo |
|---|---|---:|
| III-0 | III.1 → III.2 | 1 |
| III-1 | III.3 ∥ III.4 | 2 |
| III-2 | III.5 ∥ III.6 | 2 |
| III-3 | III.7 | 1 |
| III-4 | III.8 → III.9 | 1 |
| III-5 | III.10 | 1 |
| III-R | grafo, portas e portal | coordenadora |

Curva: **1 → 2 → 2 → 1**.

---

# VOLUME IV — A MEDIDA DO INCERTO

## 13. Estatuto condicionado

O Volume IV não deve ser contratado integralmente antes da mineração do sítio. O manual já registra probabilidade e estatística como segundo ciclo apenas se houver sítio. O possível sítio inclui:

- raciocínio clínico;
- sensibilidade, especificidade e valor preditivo;
- alarmes e falsos positivos;
- risco e prognóstico;
- decisões sob incerteza;
- interpretação de estudos;
- sobrevida e censura;
- calibração de modelos.

A Onda IV-0 é, portanto, obrigatoriamente arqueológica.

## 13.1 Tese provisória

> Probabilidade é medida sobre possibilidades; inferência é atualização controlada de informação; decisão acrescenta consequências e perdas.

## 13.2 Capítulos condicionados

### IV.1 — Medir Conjuntos

- σ-álgebras;
- medidas;
- mensurabilidade;
- medida de Lebesgue;
- conjuntos de medida zero;
- relação e diferença em relação à integral de Riemann.

### IV.2 — O Acaso como Medida

- espaço amostral;
- eventos;
- axiomas de Kolmogorov;
- independência;
- aleatoriedade física versus modelo.

### IV.3 — Variáveis Aleatórias são Funções

- variável aleatória;
- distribuição;
- massa, densidade e função de distribuição;
- transformação;
- expectativa como integral.

### IV.4 — Condicionar é Mudar o Universo

- probabilidade condicional;
- Bayes;
- independência condicional;
- odds;
- razão de verossimilhança;
- atualização sequencial.

### IV.5 — O Teste que Engana

- sensibilidade;
- especificidade;
- prevalência;
- valores preditivos;
- falácia da taxa-base;
- testes em série e paralelo;
- limiar e contexto de uso.

Aplicação central: teste diagnóstico e alarme clínico, com denominadores explícitos.

### IV.6 — Estimar sem Fingir Certeza

- estimador;
- viés;
- variância;
- erro padrão;
- intervalo de confiança;
- p-valor em estatuto correto;
- contraste com intervalo posterior.

### IV.7 — Do Ruído à Lei

- lei dos grandes números;
- teorema central do limite;
- condições;
- falhas sob caudas pesadas ou dependência;
- simulação versus demonstração.

### IV.8 — Tempo Aleatório

- processos estocásticos;
- cadeias de Markov;
- tempo de espera;
- sobrevivência;
- censura;
- risco instantâneo;
- transições de estado.

### IV.9 — Informação e Decisão

- entropia;
- informação mútua;
- divergência KL;
- calibração;
- função de perda;
- previsão versus decisão;
- utilidade e assimetria de consequências.

### IV.10 — Saber Quanto Não Sabemos

- incerteza aleatória;
- incerteza epistemológica;
- atualização;
- robustez;
- sensibilidade a modelo;
- síntese aplicada.

## 13.3 Ondas do Volume IV

| Onda | Frentes | Condição |
|---|---|---|
| IV-0 | mineração de sítio e contrato | obrigatória |
| IV-1 | IV.1 → IV.2 | contrato aprovado |
| IV-2 | IV.3 ∥ IV.4 | IV.1–IV.2 |
| IV-3 | IV.5 ∥ IV.6 | IV.3–IV.4 |
| IV-4 | IV.7 ∥ IV.8 | fundação de medida |
| IV-5 | IV.9 → IV.10 | anteriores |
| IV-R | auditoria semântica estatística | todos |

## 13.4 Gate semântico adicional proposto

A incorporação ao manual deve propor um gate contra:

- inversão de condicionais;
- ausência de denominador;
- confusão entre risco relativo e absoluto;
- interpretação errada de intervalo ou p-valor;
- simulação apresentada como prova;
- seleção retrospectiva de hipótese;
- gráfico sem população de referência;
- uso de “probabilidade” para incerteza não modelada.

---

# VOLUME V — A GEOMETRIA DO QUE NÃO FECHA

## 14. Reativação condicionada do título

O antigo “Volume V — A Geometria do que Não Fecha” permanece, no manual vigente, como prospecção transversal absorvida. Este documento propõe uma futura reativação do título somente depois de o tratado conquistar as fundações necessárias.

Não se trata de restaurar o antigo conteúdo intacto. Trata-se de reconstruí-lo em nível mais profundo:

- fechamento algébrico;
- fatoração;
- completamentos;
- local versus global;
- continuação analítica;
- pontos racionais;
- geometria aritmética.

## 14.1 Tese

> Uma equação pode falhar em um domínio, fechar em uma extensão, adquirir outra noção de proximidade em um completamento e ainda conservar uma obstrução global. “Fechar” não é uma operação única.

## 14.2 Pré-requisitos

- Volume III completo, especialmente III.7–III.10;
- medida do Volume IV quando necessária;
- teoria de números elementar do Volume I;
- álgebra linear e complexos.

## 14.3 Capítulos candidatos

### V.1 — Quando a Fatoração Falha

- domínios integrais;
- unidades;
- primos e irreducíveis;
- fatoração única;
- ℤ[√−5] como falha;
- ideais como reparo;
- norma e divisibilidade.

### V.2 — Extensões e Simetrias

- corpos;
- extensões;
- polinômios;
- corpos de decomposição;
- automorfismos;
- grupos de Galois;
- solvabilidade por radicais em escopo declarado.

### V.3 — A Série dos Primos

- séries de Dirichlet;
- ζ(s) em Re(s) > 1;
- convergência absoluta;
- produto de Euler;
- unicidade de fatoração como fundamento do produto;
- domínio antes da continuação.

### V.4 — Continuar Além do Permitido

- continuação analítica;
- unicidade;
- equação funcional da zeta;
- zeros triviais;
- faixa crítica;
- Hipótese de Riemann como questão aberta corretamente tipada.

Nenhum gráfico de zeros será apresentado como evidência de universalidade.

### V.5 — Outras Distâncias

- valoração p-ádica;
- valor absoluto p-ádico;
- desigualdade ultramétrica;
- bolas encaixadas;
- séries que mudam de comportamento;
- proximidade por divisibilidade.

### V.6 — Completar de Novo

- sequências de Cauchy;
- completamento;
- ℚ → ℝ;
- ℚ → ℚₚ;
- múltiplos completamentos do mesmo corpo;
- o que cada um torna solucionável.

### V.7 — Local e Global

- soluções reais;
- soluções módulo p;
- soluções p-ádicas;
- princípio local-global;
- exemplos de sucesso;
- falhas e obstruções explicitamente limitadas ao aparato construído.

### V.8 — Curvas Elípticas

- cúbicas suaves;
- lei de grupo geométrica;
- ponto no infinito;
- pontos racionais;
- torsão e posto em nível declarado;
- criptografia como aplicação, sem desviar para engenharia de segurança completa.

### V.9 — Geometria Aritmética

- variedades algébricas;
- pontos racionais;
- redução módulo p;
- alturas;
- famílias de soluções;
- linguagem geométrica aplicada a problemas diofantinos.

### V.10 — O que Significa Fechar?

Síntese transversal:

- expansão finita em uma base;
- fechamento de ciclos musicais;
- fechamento algébrico;
- fecho topológico;
- completamento métrico;
- compactificação;
- fechamento local;
- obstrução global;
- questão aberta.

O volume encerra quando o termo “fechamento” deixa de funcionar como metáfora única e passa a ser uma taxonomia de operações distintas.

## 14.4 Ondas do Volume V

| Onda | Frentes | Paralelismo |
|---|---|---:|
| V-0 | V.1 ∥ V.2 | 2 |
| V-1 | V.3 → V.4 | 1 |
| V-2 | V.5 → V.6 | 1 |
| V-3 | V.7 | 1 |
| V-4 | V.8 → V.9 | 1 |
| V-5 | V.10 | 1 |
| V-R | prioridade, bibliografia, grafo e portal | coordenadora |

O paralelismo diminui porque as dependências ficam mais estreitas e o custo de uma importação silenciosa cresce.

---

# PARTE VI — PORTAS ENTRE VOLUMES

## 15. Matriz de portas

| Origem | Porta | Reabertura |
|---|---|---|
| I.7 — ℂ | logaritmo complexo completo e superfícies de ramos | III.7–III.8 |
| I.9 — integral | medida de Lebesgue | IV.1 |
| I.10 — séries | continuação analítica | III.9 e V.4 |
| I.11 — Fourier | convergência em classes mais amplas | IV.1 e ciclos posteriores |
| II.5 — curvatura | invariantes globais | II.7 e III.6 |
| II.7 — Gauss–Bonnet | topologia de superfícies | III.5–III.6 |
| III.7 — recobrimentos | monodromia algébrica | V.2 |
| III.9 — resíduos | zeta e princípio do argumento | V.3–V.4 |
| III.10 — esfera de Riemann | curvas algébricas compactas | V.8–V.9 |
| IV.4 — Bayes | decisão e informação | IV.9 |
| IV.8 — processos | modelos geométricos/estocásticos avançados | fora do programa atual |
| V.6 — completamentos | adeles e ideles | ciclo futuro, não contratado |

---

# PARTE VII — ONDAS, AGENTES E INTEGRAÇÃO

## 16. Princípios de paralelismo

1. diretórios disjuntos são condição necessária, não suficiente;
2. dependências matemáticas devem estar resolvidas;
3. uma fila de merge serializada limita o benefício de produtores adicionais;
4. o leitor primário é recurso de veredito, não detalhe administrativo;
5. capítulo produzido além da capacidade de revisão vira estoque;
6. no máximo uma revisão de conteúdo por capítulo pode estar ativa;
7. a coordenadora integra quando houver dois ou mais produtores.

## 16.1 Curva geral recomendada

- começo de volume: 2–3 frentes independentes;
- meio: 2 frentes;
- síntese e cauda: 1 frente;
- fechamento: coordenadora e leitor primário.

## 16.2 Handoff obrigatório

Todo agente recebe:

- `MATH3us.md`;
- `architecture.md`;
- `STATUS.md`;
- `ROADMAP.md`;
- `models.md`;
- claims das dependências;
- contrato do capítulo;
- escopo de arquivos;
- gate vigente;
- portas que deve reabrir e portas que deve deixar fechadas.

---

# PARTE VIII — EVOLUÇÃO DOS GATES

## 17. Gates vigentes e gates candidatos

Os gates v0–v2 permanecem definidos exclusivamente pelo manual.

Este documento prospecta endurecimentos futuros, que só entram em vigor por emenda.

### Gate v3 candidato — proveniência visual

- `figures.yml` validado;
- toda figura analítica possui fonte e gerador;
- regeneração determinística;
- invariantes de figura verificados;
- equivalente acessível;
- proibição automática de fórmula central rasterizada;
- screenshot não aceito como fonte.

### Gate v4 candidato — grafo transvolume

- dependências entre volumes resolvíveis;
- portas possuem destino existente;
- nenhuma porta vencida permanece aberta após o fechamento do capítulo de destino;
- manifesto editorial do volume;
- verificação topológica do grafo sem ciclos silenciosos.

### Gate v5 candidato — prioridade e bibliografia

Especialmente para Volumes III e V:

- referências primárias;
- escopo exato do resultado citado;
- distinção entre prova apresentada e teorema importado;
- busca de prioridade para sínteses possivelmente originais;
- registro de versões de fontes;
- nenhuma alegação de novidade por ausência de busca.

---

# PARTE IX — FECHAMENTO

## 18. Definição de capítulo fechado

Permanece a do manual. Este documento apenas a operacionaliza pelas micro-ondas M0–M6.

## 18.1 Definição de volume editorialmente fechado

Um volume pode ser declarado editorialmente fechado quando:

1. todos os capítulos canônicos possuem tags imutáveis;
2. todas as dependências internas estão resolvidas;
3. todas as portas que deveriam ser reabertas no próprio volume foram julgadas;
4. o capítulo de síntese está fechado;
5. o portal do volume foi auditado;
6. o índice e a ordem de leitura estão estáveis;
7. existe manifesto editorial do volume;
8. não há claim coletivo não localizado em capítulo;
9. nenhuma pendência matemática é escondida como “acabamento”.

O fechamento de volume não cria nova tag de conteúdo que substitua tags de capítulo. Pode existir uma tag editorial agregadora, desde que sua natureza seja explicitamente distinta.

## 18.2 Manifesto editorial de volume

Exemplo prospectivo:

```yaml
volume: 2
title: "A Geometria do que Permanece"
status: editorially_closed
chapters:
  - release: vol2-cap01-gate3-r2
  - release: vol2-cap02-gate3-r1
synthesis_release: vol2-cap07-gate3-r1
dependency_graph: audit/volume-02-graph.json
portal_commit: abc1234
closed_at: 2030-01-01
```

A convenção real de nomes deverá ser decidida antes do primeiro capítulo do Volume II.

---

# PARTE X — MIGRAÇÃO DO REPOSITÓRIO

## 19. Etapas recomendadas

### Etapa A — documentação

- criar `architecture.md`;
- criar `STATUS.md`;
- reconciliar `README.md`, `ROADMAP.md`, `models.md` e `AUDIT.md`;
- incluir arquitetura no handoff de agentes.

### Etapa B — consolidar o Volume I

- fechar Caps. 2–4;
- concluir Caps. 5 e 8;
- executar a cauda 9 → 12;
- emitir manifesto editorial do Volume I;
- não iniciar produção do Volume II antes de o grafo do Volume I estar suficientemente estável.

### Etapa C — emenda de volumes

Antes do Volume II:

- emendar o manual definindo volume como unidade editorial;
- incorporar apenas o contrato do Volume II;
- manter Volumes III–V como prospecção no `architecture.md`;
- decidir nomenclatura de capítulos e tags multivolume.

### Etapa D — gate visual

- pilotar `figures.yml` em um capítulo do Volume I;
- validar regeneração e acessibilidade;
- propor gate v3 somente após o piloto funcionar.

---

# PARTE XI — RISCOS E ANTÍDOTOS

## 20. Risco: gigantismo editorial

**Sintoma:** capítulos acumulam teoria apenas porque será útil algum dia.

**Antídoto:** critério de corte, obrigação central e porta explícita.

## 20.1 Risco: curso convencional disfarçado

**Sintoma:** sequência escolar completa substitui a biografia intelectual.

**Antídoto:** cada capítulo deve nascer de obstáculo real, sítio ou dependência necessária.

## 20.2 Risco: imagem decorativa

**Sintoma:** infográfico bonito repete texto sem carregar estrutura.

**Antídoto:** `figures.yml`, invariantes, gerador e equivalente textual.

## 20.3 Risco: prospecção tratada como promessa

**Sintoma:** títulos futuros passam a ser cobrados como contratos já aprovados.

**Antídoto:** estados canônico, candidato, condicionado e fora do ciclo.

## 20.4 Risco: dependência implícita

**Sintoma:** capítulo usa ferramenta futura sem importação declarada.

**Antídoto:** grafo validado e portas.

## 20.5 Risco: aplicação forçada

**Sintoma:** exemplo cotidiano superficial cria falsa utilidade.

**Antídoto:** aplicação com hipóteses, limites e erro de extrapolação.

## 20.6 Risco: paralelismo performático

**Sintoma:** muitos agentes produzem branches envelhecidas e fila de veredito congestionada.

**Antídoto:** curva de paralelismo decrescente e merge serializado.

## 20.7 Risco: volume como esconderijo

**Sintoma:** “volume quase pronto” com capítulos sem release.

**Antídoto:** volume não é unidade de entrega; fechamento exige todos os capítulos.

---

# PARTE XII — DECISÕES FUTURAS DO LEITOR PRIMÁRIO

## 21. Decisões necessárias antes do Volume II

1. aprovar ou rejeitar a arquitetura de cinco volumes;
2. decidir se *MATH3us* é nome da coleção e *Do Número ao Contínuo* é o Volume I;
3. definir nomenclatura de capítulos futuros;
4. decidir se a numeração reinicia por volume ou permanece global;
5. aprovar o conceito de manifesto editorial de volume;
6. decidir quando o Volume II deixa de ser prospectivo e recebe contrato no manual;
7. autorizar ou não o gate v3 visual depois de piloto real;
8. determinar se o Volume IV possui sítio suficiente para existir.

Nenhuma dessas decisões deve ser inferida de silêncio.

---

# APÊNDICE A — TEMPLATE DE PROSPECÇÃO DE CAPÍTULO

```markdown
## Código e título provisório

**Estado:** candidato forte | condicionado
**Tipo provável:** escavação | território virgem | indeterminado
**Pergunta central:**
**Obstáculo que justifica o capítulo:**
**Sítio disponível:**
**Dependências:**
**Portas reabertas:**
**Portas criadas:**
**Claim central provável:**
**Recíproca/classificação necessária:**
**Figura fundamental:**
**Experimento mínimo:**
**Aplicação estrutural:**
**N4 futuro:**
**Risco de gigantismo:**
**Critério para não criar o capítulo:**
```

---

# APÊNDICE B — TEMPLATE DE ONDA

```yaml
wave: II-2
volume: 2
status: planned
producers:
  - chapter: II.4
    branch: agent/vol2-geodesics
    dependencies: [II.1, II.2, II.3]
  - chapter: II.5
    branch: agent/vol2-curvature
    dependencies: [II.1, II.2, II.3]
merge_order: [II.4, II.5]
coordinator_only_files:
  - architecture.md
  - ROADMAP.md
  - STATUS.md
  - index.html
exit_criteria:
  - all_prs_merged
  - gates_green
  - state_documents_reconciled
```

---

# APÊNDICE C — PRINCÍPIO FINAL

A arquitetura não existe para garantir que todos os assuntos sejam cobertos. Existe para garantir que cada assunto que entrar saiba:

- de onde veio;
- por que merece existir;
- de que depende;
- o que demonstra;
- o que apenas sugere;
- como é desenhado;
- como é testado;
- onde termina;
- qual porta deixa aberta.

> **A obra cresce por necessidade demonstrativa, não por ocupação de território.**
