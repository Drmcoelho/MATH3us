# models.md — Divisão da produção entre agentes paralelos

Documento operacional subordinado ao MATH3us.md. Em conflito, o manual vence.
Última atualização: 28/07/2026.

---

## 1. Propósito

O tratado tem doze capítulos e uma única constituição. A produção pode ser
paralelizada entre **sessões-agente independentes** (outras interações, em
paralelo), desde que cada sessão obedeça integralmente ao manual e que as
dependências lógicas entre capítulos nunca sejam violadas. Este documento
define a divisão, as ondas de paralelismo e as regras de coordenação.

## 2. O que nenhum agente pode receber por delegação

Estas obrigações são **indelegáveis** por doutrina:

1. **Mineração de sítio** (§7 do manual): a busca em arquivos e conversas
   pessoais é feita inline, em série, na sessão com o autor — nunca por
   subagente. Agentes de capítulo-escavação trabalham a partir do
   **contrato editorial** fixado no manual e do dossiê já minerado que
   encontrarem em `sources.md`; lacunas documentais ficam declaradas,
   jamais preenchidas.
2. **Pré-registro antes do desenvolvimento** (§1.3): cada sessão de
   capítulo começa por `conjecturas.md`, em commit separado, antes de
   qualquer linha de `index.html`.
3. **Emendas ao manual** (§13): qualquer agente pode *propor* emenda;
   somente a sessão-coordenadora comita no registro E, mantendo
   atomicidade e numeração.
4. **Tags de release**: imutáveis, criadas somente após a release ser
   efetivamente vista pelo leitor primário.

## 3. Modelo de sessão

Uma sessão-agente = um capítulo = uma branch.

- **Branch:** `claude/cap-NN-<slug>` (ex.: `claude/cap-02-ternas`).
- **Namespace de claims:** `chapter-NN.*` — dependência entre capítulos só
  para capítulo já fechado ou marcada explicitamente como porta futura (E13).
- **Entregáveis mínimos por sessão:** `conjecturas.md` (commit próprio) →
  `index.html` autocontido → seção de exercícios em cinco níveis com
  gabaritos robustos (E20, §6.1 item 10) → `claims.yml` ortogonal →
  `sources.md` → oráculo triplo com artefatos em `audit/` → auditoria de
  gate vigente → encerramento §9 com pendências declaradas.
- **Integração:** PR para `main`; um capítulo por PR; o PR carrega os
  artefatos de auditoria. Arquivos compartilhados (`index.html` da raiz,
  `MATH3us.md`, `models.md`, `tools/`) são tocados apenas pela
  sessão-coordenadora, eliminando conflitos de merge entre agentes.
- **Idioma:** texto em português; código, commits e branches em inglês.

## 4. Divisão por ondas

A ordem operacional de produção do manual (§5: 1→2→3→4→6→7→5→8→9→10→11→12)
é compatível com paralelismo dentro de ondas — as justificativas da §5 são
de sequenciamento do autor único; entre agentes, o que vincula são as
dependências lógicas e as portas.

| Onda | Cap. | Sessão-agente | Tipo | Pré-condições | Observações de contrato |
|---|---|---|---|---|---|
| 0 | 1 | coordenadora (esta) | escavação | — | Auditado sob gate v0; aguardando tag `cap-01-gate0-r1` |
| 1 | 2 | `agent-cap-02` | escavação | nenhuma | Contrato de 7 itens em §3 do manual; oráculo com pares adversariais; porta trancada → Cap. 7 |
| 1 | 3 | `agent-cap-03` | escavação | nenhuma | Capítulo-modelo do formato mínimo; se três páginas bastarem, três páginas |
| 1 | 4 | `agent-cap-04` | escavação | nenhuma | Critério d \| b^k completo com recíproca; sete como caso de estudo |
| 2 | 6 | `agent-cap-06` | virgem | Cap. 1 fechado | Usa a linguagem ε-N e o princípio do supremo do Cap. 1 |
| 2 | 7 | `agent-cap-07` | virgem | claims do Cap. 2 em `main` | Reabre a porta do Cap. 2 (soma de dois quadrados); **sem exponencial** (E11) |
| 3 | 5 | `agent-cap-05` | escavação | Caps. 6 e 7 em `main` | Ancoragem C_N/L̃_N na forma corrigida da §2.2 (E8); convergentes e semiconvergentes |
| 3 | 8 | `agent-cap-08` | virgem | nenhuma lógica; produzir na onda 3 | Invariância sob mudança de base; comparação com "base" numérica |
| 4 | 9 | `agent-cap-09` | virgem | Caps. 1–8 fechados | Reabre a porta da retificação (postulado de convexidade do Cap. 1) |
| 5 | 10 | `agent-cap-10` | virgem | Cap. 9 fechado | Julga as conjecturas C4/C5 do Cap. 1 (o fator 1/4); reabre e^{iθ} do Cap. 7; 0⁰ como interlúdio (E19) |
| 6 | 11 | `agent-cap-11` | virgem | Caps. 5, 7, 8, 9, 10 fechados | Classe suave por partes declarada (E10); sem Lebesgue |
| 7 | 12 | `agent-cap-12` | virgem | todos os anteriores fechados | Critério E16: nenhuma dependência fora do grafo de `claims.yml` |

**Infraestrutura (sessão-coordenadora, gatilhos do §1.7):**

| Gatilho | Entregável |
|---|---|
| 2º capítulo fechado | `schemas/claims.schema.json` + `tools/verify-claims.mjs` (gate v1) |
| 3º capítulo fechado | `tools/bundle.mjs` + `tools/validate-release.mjs` (gate v2) |
| endurecimento de gate | reauditoria dos capítulos fechados sob gate anterior (E9) |

## 5. Protocolo de handoff para cada agente

Todo agente de capítulo recebe, como primeiro comando da sua sessão:

1. Ler `MATH3us.md` integralmente — é a constituição; o contrato do seu
   capítulo está na §3.
2. Ler `models.md` (este arquivo) — sua linha na tabela da §4 define
   branch, pré-condições e portas.
3. Ler os `claims.yml` dos capítulos dos quais depende.
4. Seguir o protocolo de sessão (§9 do manual) do início ao fim.
5. Ferramentas prontas: `tools/oracle.py` (padrão de oráculo triplo — cada
   capítulo escreve o seu, com invariantes próprios) e `tools/audit.mjs`
   (auditoria de gate v0, parametrizada por diretório de capítulo).
6. Encerrar declarando o que ficou incompleto. "Praticamente pronto" é
   proibido pelo §9.

## 6. Regras de colisão

- Dois agentes nunca trabalham no mesmo capítulo.
- Agente não edita capítulo alheio; se encontrar erro em capítulo de outro
  agente, registra issue/nota para a coordenadora — correção de capítulo
  fechado exige commit, changelog e release próprios (E9).
- Dependência apontando para claim inexistente bloqueia o PR (E13).
- O portal da raiz (`index.html`) muda de estado (`previsto` → `aberto` →
  fechado com tag) apenas via sessão-coordenadora, no merge de cada PR.

## 7. Estado corrente

| Cap. | Estado | Branch | Última auditoria |
|---|---|---|---|
| 0 | **integrado** (PR #8) — prólogo criado por E21; auditado v0 (oráculo 12/12, auditoria 31/31); gate v1 validado na integração; aguarda tag (Decisão D1, `AUDIT.md`) | claude/chapter-1-geometric-rebuild-uf3z1f → main | 28/07/2026 |
| 1 | **fechado** — release cap-01-gate0-r1 (manifest em `releases/manifests/`; tag remota a criar pelo proprietário); revisão r2 pendente pelas correções pós-release (Decisão D2′, `AUDIT.md`) | coordenadora | 28/07/2026 — oráculo 8/8, auditoria 25/25 por viewport; re-executado pós-merge PR #8 |
| 2 | **fechado** — release cap-02-gate2-r1 (manifest, E23/D6) | wave1/cap-02 → coordenadora | 28/07/2026 |
| 3 | **fechado** — release cap-03-gate2-r1 (manifest, E23/D6) | wave1/cap-03 → coordenadora | 28/07/2026 |
| 4 | **fechado** — release cap-04-gate2-r1 (manifest, E23/D6) | wave1/cap-04 → coordenadora | 28/07/2026 |
| 5 | previsto — Onda 3 (após 6 e 7, §5) | — | — |
| 6 | **integrado** — auditado v0 (oráculo 8/8 + adversariais, auditoria 41/41); C5 do pré-registro refutada com autópsia; gate v1: 26 claims, zero achados | wave2/cap-06 → coordenadora | 29/07/2026 |
| 7 | **integrado** — auditado v0 (oráculo 10/10; dois-quadrados exaustivo p < 50000; contenção de e^{iθ} auditada); gate v1: 24 claims, portas door:true para o Cap. 2 | wave2/cap-07 → coordenadora | 29/07/2026 |
| 8–12 | previstos | — | — |

**Onda 1 concluída em 28/07/2026:** três agentes paralelos em worktrees,
dois commits por capítulo (pré-registro isolado antes do build, §1.3),
integração por cherry-pick na coordenadora, cada ledger validado pelo
`verify-claims.mjs` (gate v1 antecipado) com zero achados. Incidentes dos
agentes registrados nos próprios capítulos, não apagados. Onda 2 (Caps. 6 e 7) disparada em 28/07/2026 pela palavra do autor,
sob a arbitragem da Decisão D4 (pré-condições lógicas satisfeitas).

**Nota de coordenação (28/07/2026, pós-reconciliação):** pela tabela da §4,
as pré-condições **lógicas** da Onda 2 já estão satisfeitas — Cap. 6 exige
Cap. 1 fechado (veredito dado, D2 exercida) e Cap. 7 exige claims do Cap. 2
na `main` (PR #9). O condicionamento ao fechamento formal de 2–4, acima, é
critério mais estrito adotado pela coordenadora da Onda 1; a arbitragem
entre os dois está registrada na Decisão D4 do `AUDIT.md`, junto com as
tags pendentes (nenhuma tag remota existe, nem a do Cap. 1). O fechamento
do 3º capítulo arma o gate v2 (tabela de gatilhos, §4).

**Gate v1 pronto (antecipado):** `schemas/claims.schema.json` e
`tools/verify-claims.mjs` já existem e validam o Cap. 1; tornam-se
obrigatórios a partir do fechamento do segundo capítulo (§1.7).
Dependência do validador: `js-yaml` (obrigatória) e `ajv` (opcional),
resolvidas via `node_modules` ou `NODE_PATH`.

**Gate v2 pronto (antecipado, 28/07/2026):** `tools/bundle.mjs`
(empacotamento; bundles regeneráveis em `releases/bundles/`, ignorados
pelo git; identidade registrada em `caps/*/audit/bundle-report.json`) e
`tools/validate-release.mjs` (autocontenção estática + dinâmica).
Executados sobre os Caps. 0–4: aprovados, com reauditoria E9 dos
capítulos fechados sob gate anterior. Dependência: `playwright` via
`NODE_PATH` (navegador em `/opt/pw-browsers/chromium` ou `PW_CHROMIUM`).
