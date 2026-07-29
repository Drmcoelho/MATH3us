# CODEX.md — Plano canônico de pendências do MATH3us

**Repositório:** `Drmcoelho/MATH3us`  
**Fotografia operacional:** 29/07/2026  
**`main` observada:** `e61c577`  
**Destinatários:** Codex, agentes de capítulo, sessão-coordenadora e leitor primário.

---

## 0. Função deste documento

Este arquivo consolida as pendências técnicas, matemáticas, editoriais e operacionais que ainda permanecem depois da integração dos PRs #6, #18, #22, #23, #24 e #25.

Ele substitui a fotografia anterior baseada em `65b7516`, que ficou obsoleta enquanto o repositório avançava. Em conflito, prevalece `MATH3us.md`; para estado corrente, prevalecem tags remotas, manifests, `STATUS.md` quando existir e a `main` efetivamente publicada.

O objetivo imediato é simples:

> fazer o estado público, o estado Git, os artefatos de auditoria e a estratégia multiagentes descreverem a mesma obra.

---

## 1. Avanços já incorporados

Não reabrir como pendência aquilo que já foi concluído:

- PR #18 foi mesclada: E23, regime visual “gibi rigoroso”, retrofits dos Caps. 0–4, exercícios do Cap. 0, navegação, README e correções da revisão automática;
- Caps. 0 e 1 foram reauditados depois do retrofit;
- releases `cap-00-gate0-r2` e `cap-01-gate0-r4` possuem manifests;
- PR #6 foi mesclada: `MATHeu$` agora existe na `main` como laboratório aberto;
- Vercel recebeu configuração explícita de site estático e o status atual está verde;
- GitHub Pages permanece o deployment canônico;
- o gate v2 existe e foi executado sobre os Caps. 0–4;
- existe `coordination-sweep` diário;
- existe workflow manual `create-release-tags`, derivando tags de manifests sem mover tags existentes;
- a reconstrução geométrica do Cap. 1, incluindo áreas, duplo cerco e razão das folgas, já está integrada;
- C5 foi refutada e a razão `1/4` foi promovida a teorema; o Cap. 10 não deve ser descrito como futuro juiz dessa conjectura.

---

# P0 — BLOQUEADORES OPERACIONAIS

## P0.1 Executar o workflow de criação de tags

O workflow `.github/workflows/create-release-tags.yml` já está na `main`, mas precisa ser disparado manualmente e inspecionado.

### Ações

1. executar `create-release-tags` via `workflow_dispatch`;
2. confirmar que as tags derivadas dos manifests foram criadas no remoto;
3. confirmar que uma segunda execução é idempotente;
4. registrar o run em `AUDIT.md`;
5. atualizar portal, README e futuro `STATUS.md` para não falar em “tag remota pendente” depois da criação.

### Tags atualmente cobertas por manifests

- `cap-00-gate0-r1`;
- `cap-00-gate0-r2`;
- `cap-01-gate0-r1`;
- `cap-01-gate0-r2`;
- `cap-01-gate0-r3`;
- `cap-01-gate0-r4`.

### Critério de aceite

- tags aparecem no GitHub remoto;
- apontam para os commits registrados nos manifests;
- nenhuma tag existente é movida;
- run repetido apenas informa `skip`;
- falha em commit inexistente interrompe o workflow.

---

## P0.2 Fechar formalmente os Capítulos 2–4

Os Caps. 2, 3 e 4 passaram por gate v0, gate v1 e gate v2, mas ainda precisam do ato editorial de release.

### Ações

- revisar visualmente a versão final de cada capítulo;
- registrar decisões de fechamento separadas;
- criar manifests:
  - `cap-02-gate2-r1`;
  - `cap-03-gate2-r1`;
  - `cap-04-gate2-r1`;
- executar novamente `create-release-tags`;
- atualizar rodapés, portal, README, `AUDIT.md`, `ROADMAP.md` e `models.md`.

### Regra

Cada capítulo recebe decisão e manifest próprios. Não criar um único manifest coletivo da Onda 1.

---

## P0.3 Criar `STATUS.md`

O repositório ainda mistura fotografia corrente, decisões históricas e incidentes no mesmo documento.

Criar `STATUS.md` curto, sem narrativa arqueológica, contendo:

- commit observado;
- data;
- estado de cada capítulo;
- release remota vigente;
- gates passados;
- PRs abertas;
- workflows pendentes;
- bloqueios;
- próxima ação autorizada.

### Critério de aceite

- `STATUS.md`, portal, tags, manifests e README concordam;
- toda sessão que muda estado atualiza `STATUS.md`;
- histórico permanece em `AUDIT.md`, não em `STATUS.md`.

---

## P0.4 Reconciliar `AUDIT.md`, `ROADMAP.md` e `models.md`

Após as últimas mesclas, executar uma revisão de coerência documental.

### `AUDIT.md`

- registrar os runs dos workflows de tags e coordenação;
- marcar decisões D6/D7 como plenamente executadas após as tags remotas;
- separar texto histórico de estado corrente;
- eliminar frases superadas que permaneçam semanticamente ativas;
- registrar releases dos Caps. 2–4 quando ocorrerem.

### `ROADMAP.md`

- registrar PR #6 e PR #18 como concluídas;
- registrar Vercel como corrigido, mantendo Pages canônico;
- registrar `MATHeu$` como laboratório integrado;
- atualizar a fila para incluir PR #20 e as próximas ondas;
- não manter reconstrução D3 como tarefa futura;
- atualizar nomes de releases para gate v2 onde aplicável.

### `models.md`

- atualizar o estado dos Caps. 0–4;
- registrar Cap. 1 em `r4`;
- remover qualquer referência a C4/C5 como problema ainda aberto;
- registrar gate v2 como entregue e executado;
- acrescentar `STATUS.md` ao handoff obrigatório;
- distinguir claramente audit core transversal de specs por capítulo.

---

## P0.5 Validar os workflows em condições reais

### `coordination-sweep`

- disparar manualmente sobre a `main` atual;
- confirmar gate v1 e v2 em todos os `caps/*/`;
- confirmar criação de issue em falha controlada;
- armazenar logs e artifacts;
- verificar que relatórios versionados não são alterados silenciosamente.

### `create-release-tags`

- executar, repetir e confirmar idempotência;
- documentar a política: manifest aprovado é a única fonte de novas tags.

---

# P1 — PR #20 E EXPERIÊNCIA DE LEITURA

## P1.1 Rebase e redução de escopo da PR #20

A PR #20 está aberta em draft e nasceu antes de várias mesclas posteriores.

### Ações

- rebasear sobre a `main` atual;
- revisar conflito com navegação já introduzida pela E23;
- garantir que o codemod não duplique `nav.capnav`;
- manter a PR estrutural: home, navegação e ferramenta idempotente;
- não misturar revisão matemática de capítulos;
- executar o codemod, revisar o diff gerado e comprovar idempotência em segunda execução.

### Critérios

- nenhum capítulo recebe mudança de fórmula, prova ou claim;
- links anterior/índice/próximo são corretos;
- nenhuma navegação duplicada;
- HTML válido;
- zero recurso externo;
- mobile e teclado verificados.

---

# P1 — MATHeu$: ESTABILIZAÇÃO DO LABORATÓRIO

O `MATHeu$` foi integrado como laboratório aberto, não como release fechada.

## P1.2 Revalidar os três findings históricos do PR #6

Verificar na `main`, e corrigir se ainda presentes:

1. arco local para `n=3` e `n=4` deve começar com `M`, não `L`;
2. triângulo circunscrito de `n=3` deve caber integralmente no `viewBox`;
3. marcador do gráfico não pode fingir representar o `n` atual quando `n` estiver fora do intervalo exibido.

Não considerar os threads superados apenas porque a PR foi mesclada.

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

### Domínio mínimo de teste

- `n = 3, 4, 5, 6, 12, 24, 48, 96`;
- todos os modos gráficos;
- `n` dentro e fora do alcance do gráfico;
- desktop e iPhone;
- Safari/iOS real quando disponível;
- teclado;
- zoom textual;
- decimal com ponto e vírgula;
- ausência de overflow e rede.

### Invariantes semânticos

- círculo, corda e tangente realmente presentes;
- vértices inscritos pertencem à circunferência;
- tangências distinguíveis dos vértices;
- nenhum objeto central fora do viewport;
- séries não dependem só de cor;
- marcador representa o estado correto;
- tabela textual equivale ao gráfico.

---

# P2 — EXPANSÃO 02 DO MATHeu$

A especificação existe, mas continua prospectiva. Implementar em seis unidades independentes.

## D2.1 Estado, regimes e raio

- estado único `{regime, n, rho, phi}`;
- circunferência circunscrita fixa;
- incircunferência fixa;
- presets `1`, `1/π`, `1/√π`;
- entrada livre `ρ>0`;
- grandezas absolutas e adimensionais;
- box “O que ficou fixo?”.

## D2.2 Limites e gráficos

Implementar e comparar:

\[
P_n=2n\rho\sin(\pi/n),
\qquad
A_n=\frac{n\rho^2}{2}\sin(2\pi/n).
\]

Gráficos obrigatórios:

- `P_n` e `2πρ`;
- `A_n` e `πρ²`;
- erros absolutos;
- escala logarítmica;
- `n²E_P`;
- `n²E_A`;
- `E_A/E_P`;
- razões adimensionais.

Verificar:

\[
n^2E_P(n)\to\frac{\pi^3\rho}{3},
\qquad
n^2E_A(n)\to\frac{2\pi^3\rho^2}{3},
\qquad
\frac{E_A(n)}{E_P(n)}\to2\rho.
\]

## D2.3 Três triângulos locais

- triângulo retângulo fundamental `O-M-V`;
- isósceles dos vértices `O-V_k-V_{k+1}`;
- isósceles das tangências `O-T_k-T_{k+1}`;
- áreas e perímetros locais;
- razões `cos θ` e `cos² θ`.

## D2.4 Setores e segmentos — o “sorvete”

Distinguir:

- triângulo;
- corda;
- arco;
- setor;
- segmento circular;
- perímetro com arco;
- perímetro com corda.

Verificar relações lineares para comprimentos e quadráticas para áreas.

## D2.5 Cartesiano e complexo

- coordenadas de vértices e tangências;
- rotação `φ`;
- normais e tangentes;
- área por decomposição e cadarço;
- órbita complexa dos vértices;
- fórmula de Euler marcada como importada ou porta futura;
- 3D fora do núcleo até demonstrar valor explicativo adicional.

## D2.6 Exercícios e auditoria

- exercícios N0–N4;
- gabaritos robustos N0–N3;
- portas N4 honestas;
- oráculo independente;
- audit semântico;
- screenshots de edge cases;
- revisão adversarial;
- release própria somente depois de todos os gates.

---

# P2 — CI, PROVENIÊNCIA E FERRAMENTAS

## P2.1 Ampliar gatilhos da CI

O gate deve rodar também em:

```yaml
on:
  pull_request:
  push:
    branches: [main]
  schedule:
  workflow_dispatch:
```

## P2.2 Fixar dependências

Criar e versionar:

- `package.json`;
- lockfile;
- scripts canônicos;
- versão de Node;
- versão de Playwright;
- versão do Chromium nos relatórios;
- cache de dependências.

Evitar `npm install --no-save` como única definição do ambiente.

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

O core verifica invariantes transversais; o spec verifica a semântica específica do capítulo.

## P2.4 Formalizar commits de conteúdo e evidência

Todo manifest deve distinguir:

- `subject_commit`: conteúdo auditado;
- `evidence_commit`: commit que adiciona artifacts;
- diff permitido entre ambos.

Bloquear release se houver alteração matemática ou visual não reauditada entre eles.

## P2.5 Publicar artifacts dos workflows

Preservar por run:

- logs;
- JSONs;
- screenshots;
- bundles;
- SHA do código;
- hashes dos artifacts.

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

Mover gradualmente decisões completas para `docs/decisions/`; `AUDIT.md` deve manter resumo, execução e incidente, não todas as atas integrais.

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

## P2.8 README e licença

Confirmar que o README explica:

- o tratado;
- o `MATHeu$`;
- estado real dos capítulos;
- deployment canônico;
- execução dos gates;
- fluxo de contribuição;
- política de releases;
- localização de constituição, status, audit e roadmap;
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

## P3.2 Capítulos 6, 7 e 8

Após fechamento formal dos Caps. 2–4 e estabilização da fila:

### Capítulo 6 — As Patologias

- continuidade e descontinuidade;
- Dirichlet, Thomae e Weierstrass;
- completude e limites;
- diferença entre gráfico computacional e propriedade matemática;
- dependências do Cap. 1.

### Capítulo 7 — `ℂ`

- construção dos complexos;
- forma polar e rotação;
- raízes, argumentos e ramos;
- Gaussianos;
- soma de dois quadrados;
- sem usar exponencial complexa como construção já merecida.

### Capítulo 8 — Álgebra Linear

- pode ser produzido em paralelo em diretório disjunto;
- transformação, base, invariância e estrutura;
- evitar conflito terminológico com base numérica do Cap. 4.

## P3.3 Sequência posterior

1. Caps. 6, 7 e 8 conforme alocação vigente;
2. Cap. 2 r2 em janela exclusiva;
3. Cap. 5;
4. Cap. 9;
5. Cap. 10;
6. Cap. 11;
7. Cap. 12.

A cauda 9→10→11→12 permanece sequencial.

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
- [ ] a PR está mergeável;
- [ ] não há thread P1/P2 aberta;
- [ ] deployment canônico está verde;
- [ ] gates vigentes estão verdes;
- [ ] leitor primário viu a versão final quando houver release.

---

# 5. Ordem operacional recomendada

1. disparar `create-release-tags` e verificar as seis tags atuais;
2. criar `STATUS.md`;
3. reconciliar `AUDIT.md`, `ROADMAP.md` e `models.md`;
4. executar `coordination-sweep` manual;
5. rebasear e concluir a PR #20 sem duplicar navegação;
6. decidir e registrar releases dos Caps. 2–4;
7. executar novamente `create-release-tags`;
8. revalidar os três findings históricos do `MATHeu$`;
9. criar gate próprio do braço;
10. implementar Expansão 02 em D2.1–D2.6;
11. iniciar Caps. 6, 7 e 8 conforme a política de paralelismo;
12. executar Cap. 2 r2;
13. seguir 5 → 9 → 10 → 11 → 12.

---

## 6. Divisa operacional

> **MATHeu$ experimenta. MATH3us demonstra, ordena e publica. O repositório só avança quando código, prova, audit e release voltam a concordar.**
