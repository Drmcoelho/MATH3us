# CODEX.md — Plano canônico de pendências do MATH3us

**Repositório:** `Drmcoelho/MATH3us`  
**Fotografia operacional:** 29/07/2026  
**`main` observada:** `6d36dc8`  
**Destinatários:** Codex, agentes de capítulo, sessão-coordenadora e leitor primário.

---

## 0. Função deste documento

Este arquivo consolida as pendências técnicas, matemáticas, editoriais e operacionais do projeto depois da integração dos PRs #6, #18 e #22–#26.

Ele é uma fila executiva, não uma segunda constituição. Em conflito:

1. `MATH3us.md` governa a doutrina;
2. tags remotas e manifests governam releases;
3. `STATUS.md`, quando criado, governará a fotografia corrente;
4. `AUDIT.md` preserva execuções, incidentes e decisões;
5. este documento organiza o trabalho ainda não concluído.

> O objetivo é fazer o estado público, o estado Git, os artefatos de auditoria e a estratégia multiagentes descreverem a mesma obra.

---

## 1. Avanços já incorporados — não reabrir

- PR #18 foi mesclada: E23, regime visual “gibi rigoroso”, retrofit dos Caps. 0–4, exercícios do Cap. 0, navegação, README e correções da revisão automática;
- Caps. 0 e 1 foram reauditados depois do retrofit;
- releases `cap-00-gate0-r2` e `cap-01-gate0-r4` possuem manifests;
- as seis tags dos Caps. 0–1 existem no remoto e foram verificadas;
- Caps. 0 e 1 estão formalmente fechados;
- PR #6 foi mesclada: `MATHeu$` existe na `main` como laboratório aberto;
- Vercel recebeu configuração explícita de site estático e o status observado está verde;
- GitHub Pages permanece o deployment canônico;
- gate v2 existe e foi executado sobre os Caps. 0–4;
- existe workflow diário `coordination-sweep`;
- existe workflow manual `create-release-tags`, derivando tags dos manifests sem mover tags existentes;
- a reconstrução geométrica do Cap. 1, com áreas, duplo cerco e razão das folgas, está integrada;
- C5 foi refutada e a razão `1/4` foi promovida a teorema;
- o Cap. 10 não deve continuar descrito como futuro juiz de C4/C5.

---

# P0 — BLOQUEADORES OPERACIONAIS

## P0.1 Fechar formalmente os Capítulos 2–4

Os Caps. 2, 3 e 4 passaram por gate v0, gate v1 e gate v2, mas ainda aguardam a decisão editorial D4 e releases remotas.

### Ações

1. inspecionar visualmente a versão final de cada capítulo;
2. registrar uma decisão de fechamento por capítulo;
3. criar manifests independentes:
   - `cap-02-gate2-r1`;
   - `cap-03-gate2-r1`;
   - `cap-04-gate2-r1`;
4. atualizar rodapés, portal, README, `AUDIT.md`, `ROADMAP.md` e `models.md`;
5. despachar `create-release-tags`;
6. confirmar as três tags no remoto;
7. registrar a execução e a idempotência do workflow.

### Regra

Cada capítulo recebe decisão, manifest e release próprios. Não criar release coletiva da Onda 1.

### Critério de aceite

- os três manifests apontam para commits auditados;
- as três tags existem no remoto;
- portal, README e documentos operacionais concordam;
- o segundo disparo do workflow não move nem recria tags;
- a revisão r2 do Cap. 2 só começa depois de `cap-02-gate2-r1` existir.

---

## P0.2 Criar `STATUS.md`

O repositório ainda distribui a fotografia corrente entre portal, README, `AUDIT.md` e `ROADMAP.md`.

Criar `STATUS.md` curto, sem narrativa arqueológica, contendo:

- data e commit observado;
- estado de cada capítulo;
- release remota vigente;
- gates passados;
- PRs abertas;
- workflows pendentes;
- bloqueios;
- frentes ativas;
- próxima ação autorizada.

### Critério de aceite

- `STATUS.md`, portal, tags, manifests e README concordam;
- toda sessão que muda estado atualiza `STATUS.md`;
- decisões e incidentes históricos permanecem em `AUDIT.md`;
- `STATUS.md` não acumula versões superadas no corpo principal.

---

## P0.3 Reconciliar `AUDIT.md`, `ROADMAP.md` e `models.md`

O PR #26 atualizou parte da governança após a criação das tags. Ainda é necessária uma varredura completa.

### `AUDIT.md`

- confirmar que D6/D7 estão plenamente executadas, não apenas decididas;
- registrar o run de criação das seis tags;
- registrar a segunda execução idempotente quando ocorrer;
- separar claramente estado corrente de texto histórico preservado;
- registrar D4 e releases dos Caps. 2–4 quando ocorrerem;
- eliminar frases superadas que ainda pareçam instruções vigentes.

### `ROADMAP.md`

- registrar PR #6 e PR #18 como concluídas;
- registrar `MATHeu$` como laboratório integrado;
- registrar Vercel corrigido, mantendo Pages canônico;
- incluir PR #20 na fila corrente;
- não manter D3 como trabalho futuro;
- registrar a pré-condição do Cap. 6 como satisfeita;
- manter `agent-cap-02r2` bloqueado até a release remota do Cap. 2;
- atualizar releases para gate v2 onde aplicável.

### `models.md`

- atualizar o estado dos Caps. 0–4;
- registrar Cap. 1 em `r4`;
- remover C4/C5 da lista de questões abertas;
- registrar gate v2 como entregue e executado;
- acrescentar `STATUS.md` ao handoff obrigatório;
- distinguir audit core transversal de specs específicas por capítulo;
- registrar a situação institucional do `MATHeu$`.

---

## P0.4 Validar os workflows em condições reais

### `coordination-sweep`

- disparar manualmente sobre a `main` atual;
- confirmar gate v1 e gate v2 em todos os `caps/*/`;
- armazenar logs e artifacts;
- confirmar que relatórios versionados não são alterados sem registro;
- testar a abertura de issue em uma falha controlada, sem contaminar a `main`.

### `create-release-tags`

A primeira execução foi bem-sucedida. Ainda verificar formalmente:

- segunda execução idempotente;
- tags existentes permanecem imutáveis;
- manifest inválido ou commit inexistente reprova o job;
- manifest aprovado permanece a única fonte autorizada de nova tag.

---

# P1 — PR #20 E EXPERIÊNCIA DE LEITURA

## P1.1 Rebase e contenção de escopo da PR #20

A PR #20 está aberta em draft e nasceu antes de várias mesclas posteriores.

### Ações

- rebasear sobre a `main` atual;
- reconciliar a navegação proposta com `nav.capnav` já introduzida pela E23;
- garantir que o codemod não duplique navegação;
- manter a PR estrutural: home, navegação e ferramenta idempotente;
- não misturar revisão matemática de capítulos;
- executar o codemod;
- revisar o diff dos cinco capítulos;
- executar novamente e comprovar diff vazio na segunda passagem.

### Critérios de aceite

- nenhuma fórmula, prova, exercício ou claim é alterada;
- links anterior/índice/próximo são corretos;
- não há navegação duplicada;
- HTML permanece válido;
- zero recurso externo;
- teclado, foco, mobile e zoom textual são verificados;
- a PR está mergeável e sem thread P1/P2 aberta.

---

# P1 — MATHeu$: ESTABILIZAÇÃO DO LABORATÓRIO

O `MATHeu$` foi integrado como laboratório aberto, não como release fechada.

## P1.2 Revalidar os três findings históricos do PR #6

Verificar na `main`, corrigindo e registrando se ainda presentes:

1. para `n=3` e `n=4`, o arco local deve começar com comando SVG `M`, não `L`;
2. para `n=3`, o polígono circunscrito e seus marcadores devem caber integralmente no `viewBox`;
3. quando o `n` selecionado estiver fora do alcance do gráfico, o marcador deve desaparecer ou ser explicitamente identificado como endpoint, nunca fingir representar o estado atual.

A mescla da PR não substitui a resolução técnica dos findings.

---

## P1.3 Criar gate próprio do braço

Estrutura mínima:

```text
arms/matheus-dollar/
├── index.html
├── claims.yml
├── conjecturas.md
├── sources.md
├── oracle.py
├── audit.spec.mjs
└── audit/
    ├── numeric-check.json
    ├── symbolic-check.md
    ├── interaction-report.json
    ├── edge-cases.md
    ├── desktop.png
    └── iphone.png
```

### Domínio mínimo

- `n = 3, 4, 5, 6, 12, 24, 48, 96`;
- todos os modos gráficos;
- `n` dentro e fora do alcance do gráfico;
- desktop e iPhone;
- Safari/iOS real quando disponível;
- teclado e foco;
- zoom textual a 200%;
- decimal com ponto e vírgula;
- ausência de overflow e rede.

### Invariantes semânticos

- círculo, corda e tangente realmente presentes;
- vértices inscritos pertencem à circunferência;
- tangências distinguíveis dos vértices;
- nenhum objeto central desaparece ou é cortado;
- séries não dependem exclusivamente de cor;
- marcador representa o estado correto;
- tabela textual equivale ao gráfico;
- o teste “há pixels pintados” não basta.

---

# P2 — EXPANSÃO 02 DO MATHeu$

A especificação existe, mas continua prospectiva. Implementar em seis unidades auditáveis.

## D2.1 Estado, regimes e raio

- estado único `{regime, n, rho, phi}`;
- regime de circunferência circunscrita fixa;
- regime de incircunferência fixa;
- presets `1`, `1/π`, `1/√π`;
- entrada livre `ρ>0`;
- validação de entradas;
- grandezas absolutas e adimensionais;
- box “O que ficou fixo?”.

### Critério

Mudar `n`, `ρ`, `φ` ou regime atualiza todos os painéis a partir do mesmo estado matemático imutável.

---

## D2.2 Limites e gráficos

Implementar:

\[
P_n=2n\rho\sin\left(\frac{\pi}{n}\right),
\qquad
A_n=\frac{n\rho^2}{2}\sin\left(\frac{2\pi}{n}\right).
\]

Gráficos obrigatórios:

- `P_n` e `2πρ`;
- `A_n` e `πρ²`;
- erros absolutos;
- erros em escala logarítmica;
- `n²E_P`;
- `n²E_A`;
- `E_A/E_P`;
- razões adimensionais para raios diferentes.

Verificar:

\[
n^2E_P(n)\longrightarrow\frac{\pi^3\rho}{3},
\qquad
n^2E_A(n)\longrightarrow\frac{2\pi^3\rho^2}{3},
\qquad
\frac{E_A(n)}{E_P(n)}\longrightarrow2\rho.
\]

Cada gráfico deve possuir tabela equivalente, descrição textual e indicação explícita do valor selecionado.

---

## D2.3 Três triângulos locais

Implementar e comparar:

- triângulo retângulo fundamental `O-M-V`;
- isósceles dos vértices `O-V_k-V_{k+1}`;
- isósceles das tangências `O-T_k-T_{k+1}`;
- lados, perímetros e áreas;
- razões `cos θ` e `cos² θ`;
- comportamento quando `n→∞`.

A interface deve mostrar o efeito linear da escala nos comprimentos e quadrático nas áreas.

---

## D2.4 Setores e segmentos — o “sorvete”

Distinguir visual e terminologicamente:

- triângulo;
- corda;
- arco;
- setor circular;
- segmento circular;
- perímetro com arco;
- perímetro com corda.

Verificar as relações lineares para comprimentos e quadráticas para áreas. O arco jamais pode ser desenhado como se fosse a corda.

---

## D2.5 Cartesiano e complexo

- coordenadas de vértices e tangências;
- rotação global `φ`;
- normais e tangentes;
- distância euclidiana;
- área por decomposição e por fórmula do cadarço;
- comparação entre as duas rotas independentes;
- órbita complexa dos vértices;
- módulo, argumento e raiz da unidade;
- fórmula de Euler marcada como importada ou porta futura;
- 3D fora do núcleo até demonstrar relação invisível em 2D.

Uma divergência entre área trigonométrica e área pelo cadarço acima da tolerância bloqueia a visualização.

---

## D2.6 Exercícios e auditoria

- exercícios N0–N4;
- gabaritos robustos N0–N3;
- portas N4 honestas;
- oráculo independente;
- audit semântico;
- screenshots de edge cases;
- Safari/iOS;
- revisão adversarial;
- release própria somente depois de todos os gates.

---

# P2 — CI, PROVENIÊNCIA E FERRAMENTAS

## P2.1 Ampliar os gatilhos da CI

Os gates devem rodar também em:

```yaml
on:
  pull_request:
  push:
    branches: [main]
  schedule:
  workflow_dispatch:
```

A ronda diária não substitui a barreira pré-merge.

---

## P2.2 Fixar dependências e ambiente

Criar e versionar:

- `package.json`;
- lockfile;
- scripts canônicos;
- versão de Node;
- versão de Playwright;
- versão do Chromium nos relatórios;
- cache de dependências.

Evitar `npm install --no-save` como única definição do ambiente reproduzível.

---

## P2.3 Separar core e specs

Estrutura preferida:

```text
tools/
├── audit-core.mjs
├── verify-claims.mjs
├── bundle.mjs
└── validate-release.mjs

caps/NN-slug/
├── oracle.py
└── audit.spec.mjs
```

O core verifica invariantes transversais. O spec verifica a semântica específica de cada capítulo.

---

## P2.4 Formalizar conteúdo e evidência

Todo manifest deve distinguir:

- `subject_commit`: conteúdo efetivamente auditado;
- `evidence_commit`: commit que acrescenta os artifacts;
- diff permitido entre os dois.

Bloquear release se existir alteração matemática, visual ou interativa não reauditada entre ambos.

---

## P2.5 Publicar artifacts dos workflows

Preservar por run:

- logs;
- JSONs;
- screenshots;
- bundles;
- SHA do código;
- hashes dos artifacts;
- versões do ambiente.

---

# P2 — DOCUMENTAÇÃO E ARQUITETURA

## P2.6 Estruturar `docs/`

Estrutura alvo:

```text
docs/
├── codex.md
├── decisions/
├── architecture/
│   ├── gates.md
│   ├── agents.md
│   └── releases.md
└── changelog/
```

Mover gradualmente decisões completas para `docs/decisions/`. `AUDIT.md` deve manter resumo, execução e incidente, não todas as atas integrais misturadas à fotografia corrente.

---

## P2.7 Protocolo de upstream do MATHeu$

Cada módulo do braço deve declarar:

```yaml
upstream:
  target_chapter: 9
  status: blocked_by_dependency
  reason: arc length not yet constructed
```

Estados permitidos:

- `experimental`;
- `ready_for_upstream`;
- `blocked_by_dependency`;
- `absorbed`;
- `rejected`.

Nenhuma absorção ocorre por cópia silenciosa.

---

## P2.8 README e licença

Confirmar que o README explica:

- o tratado;
- o `MATHeu$`;
- estado real dos capítulos;
- deployment canônico;
- execução dos gates;
- fluxo de contribuição;
- política de releases;
- localização de constituição, status, audit, roadmap e codex;
- licença ou regime de direitos.

---

# P3 — BACKLOG MATEMÁTICO

## P3.1 Capítulo 2 — revisão de densidade

Depois da release remota `cap-02-gate2-r1`:

- pré-registrar revisão r2;
- contar ternas primitivas com cateto ímpar fixado `n`;
- identificar a terna canônica;
- estudar a fração da família canônica entre hipotenusas `≤H`;
- distinguir provado, citado e estimado;
- manter essa revisão separada do retrofit visual.

---

## P3.2 Capítulos 6, 7 e 8

Com Cap. 1 formalmente fechado, o Cap. 6 está logicamente destravado. Cap. 7 depende das claims do Cap. 2 já integradas. Cap. 8 é logicamente independente.

### Capítulo 6 — As Patologias

- continuidade e descontinuidade;
- Dirichlet, Thomae e Weierstrass;
- completude e limites;
- diferença entre gráfico computacional e propriedade matemática;
- dependências explícitas do Cap. 1.

### Capítulo 7 — `ℂ`

- construção dos complexos;
- forma polar e rotação;
- raízes, argumentos e ramos;
- inteiros gaussianos;
- soma de dois quadrados;
- sem usar exponencial complexa como construção já merecida.

### Capítulo 8 — Álgebra Linear

- transformação, base, invariância e estrutura;
- evitar conflito terminológico com base numérica do Cap. 4;
- pode ser produzido em paralelo em diretório disjunto.

---

## P3.3 Sequência posterior

1. concluir a estabilização documental e os releases dos Caps. 2–4;
2. Caps. 6, 7 e 8 conforme a política vigente de paralelismo;
3. Cap. 2 r2 em janela exclusiva;
4. Cap. 5;
5. Cap. 9;
6. Cap. 10;
7. Cap. 11;
8. Cap. 12.

A cauda `9→10→11→12` permanece sequencial.

---

# 4. Definition of Done por PR

Uma PR só está pronta quando:

- [ ] parte da `main` atual;
- [ ] possui escopo declarado;
- [ ] não toca capítulo alheio sem autorização explícita;
- [ ] pré-registro existe quando há matemática nova;
- [ ] claims possuem tipo, estado e dependências corretos;
- [ ] oráculo é independente da visualização;
- [ ] audit roda sobre o commit final;
- [ ] edge cases do domínio foram testados;
- [ ] screenshots foram realmente inspecionados;
- [ ] acessibilidade foi testada além de `aria-label`;
- [ ] zero recursos externos não autorizados;
- [ ] mudança de conteúdo não é escondida como “apenas visual”;
- [ ] `STATUS.md` foi atualizado quando o estado mudou;
- [ ] `AUDIT.md` registra execução ou incidente relevante;
- [ ] PR está mergeável;
- [ ] não há thread P1/P2 aberta;
- [ ] deployment canônico está verde;
- [ ] gates vigentes estão verdes;
- [ ] leitor primário viu a versão final quando houver release.

---

# 5. Ordem operacional recomendada

1. criar `STATUS.md`;
2. reconciliar `AUDIT.md`, `ROADMAP.md` e `models.md`;
3. executar `coordination-sweep` manual;
4. executar novamente `create-release-tags` para comprovar idempotência;
5. rebasear e concluir a PR #20 sem duplicar navegação;
6. decidir e registrar releases dos Caps. 2–4;
7. despachar novamente `create-release-tags` e confirmar as novas tags;
8. revalidar os três findings históricos do `MATHeu$`;
9. criar gate próprio do braço;
10. implementar Expansão 02 em D2.1–D2.6;
11. iniciar Caps. 6, 7 e 8 conforme a política de paralelismo;
12. executar Cap. 2 r2;
13. seguir `5→9→10→11→12`.

---

## 6. Divisa operacional

> **MATHeu$ experimenta. MATH3us demonstra, ordena e publica. O repositório só avança quando código, prova, audit e release voltam a concordar.**
