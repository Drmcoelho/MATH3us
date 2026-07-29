# ROADMAP.md — Roteiro multiagentes

Documento operacional da sessão-coordenadora, subordinado ao MATH3us.md e ao
models.md (em conflito, o manual vence; em operação, este arquivo detalha).
Atualizado em 28/07/2026. A coordenação vigente é a sessão da branch
`claude/repo-analysis-chapters-b8h2df`, por mandato do autor.

O objetivo deste roteiro é único: **nenhuma sobreposição de tarefa, nenhum
PR concorrente sobre os mesmos arquivos, nenhum conflito com a `main`.**

---

## 1. Disciplina de fila de PRs (anti-conflito)

A colisão E20/E20 e os conflitos do PR #8 tiveram a mesma causa: branch
antiga demais e dois PRs tocando os mesmos arquivos. Regras vigentes:

1. **Um PR aberto por vez entra na fila de merge.** Agentes podem trabalhar
   em paralelo, mas o merge é serializado pela coordenadora, na ordem da
   fila (§4). Nenhum agente mescla o próprio PR.
2. **Rebase antes de abrir PR:** todo agente parte de `origin/main` do dia e
   re-sincroniza (`git fetch origin main && git merge origin/main`) antes de
   abrir o PR. PR com `mergeable_state: dirty` volta para o agente.
3. **Escopo de arquivos declarado no título do PR** e conferido contra a
   matriz da §2. PR que toca arquivo fora do seu escopo é bloqueado.
4. **Emendas nunca nascem numeradas em branch de agente.** O agente propõe
   a emenda no corpo do PR; a coordenadora atribui o número E na integração
   (lição da colisão E20).
5. **Publicar cedo:** worktree local não publicado é trabalho inexistente.
   Push da branch do agente ao fim de cada sessão de trabalho, sempre.

## 2. Matriz de propriedade de arquivos

| Caminho | Dono | Mais ninguém toca |
|---|---|---|
| `caps/NN-*/` | agente do capítulo NN (um por capítulo, §6 do models.md) | correção de capítulo alheio = nota para a coordenadora |
| `MATH3us.md`, `models.md`, `ROADMAP.md`, `AUDIT.md`, `index.html` (raiz), `tools/`, `schemas/`, `releases/` | coordenadora | agentes propõem via corpo do PR ou nota |
| `arms/matheus-dollar/`, `MATHeu$.md` | braço MATHeu$ (sessão própria) | não referencia nem é referenciado pelos `claims.yml` dos capítulos |
| tags e releases GitHub | leitor primário (ato humano, indelegável) | — |

## 3. Estado e fila corrente (28/07/2026)

- **Integrado na `main`:** Caps. 0, 1, 2, 3, 4 (auditados v0; ledgers
  validados pelo gate v1).
- **Fila de merge:** vazia. PR #6 (MATHeu$) aguarda veredito do leitor
  primário — política na §6.
- **Bloqueio externo:** nenhuma tag remota existe (D1, D2′, D4 do
  `AUDIT.md`). As tags destravam o fechamento formal e o critério estrito
  da Onda 2.
- **Gate v2 entregue e executado (28/07/2026):** `tools/bundle.mjs` +
  `tools/validate-release.mjs`, aprovados nos Caps. 0–4 com reauditoria
  E9 (relatórios em `caps/*/audit/`). A D4 está destravada do lado da
  infraestrutura — pende apenas do ato humano das tags (D1 primeiro,
  depois Caps. 2–4 como `cap-0N-gate2-r1`).

## 4. Ondas restantes — atribuição e sequência

Uma sessão-agente = um capítulo = uma branch = um PR. Pré-condições da
tabela §4 do models.md; fila de merge na ordem abaixo.

| Ordem | Agente | Branch | Capítulo | Pode iniciar quando | Observação anti-conflito |
|---|---|---|---|---|---|
| 1 | `agent-cap-06` | `claude/cap-06-patologias` | 6 — As Patologias | tag `cap-01-gate0-r1` criada — pelo §10 do manual, capítulo só fecha com a tag; veredito e manifest não a substituem (correção aceita de revisão externa) | não toca `caps/01-exaustao/`; usa claims do Cap. 1 por referência |
| 2 | `agent-cap-07` | `claude/cap-07-complexos` | 7 — ℂ | claims do Cap. 2 na `main` ✓ (pré-condição da §4 do models.md é claims, não fechamento) | reabre porta do Cap. 2 **por referência**, sem editar o Cap. 2; sem exponencial (E11) |
| 3 | `agent-cap-02r2` | `claude/cap-02-r2-density` | 2 — revisão r2 (W1, §5) | tag `cap-02-gate0-r1` criada (E9: correção/extensão pós-release exige revisão própria) | mesmo diretório do Cap. 2; **não pode correr em paralelo com outro trabalho no Cap. 2** |
| ~~4~~ | ~~`agent-cap-01r`~~ | — | 1 — reconstrução geométrica — **CONCLUÍDA** (D3 exercida; PR #17, release r3 em `947aa80`; primeira aresta inter-capítulos do grafo: cunha do Cap. 1 → Cap. 0) | — | vaga liberada para a política da §8 |
| 5 | `agent-cap-05` | `claude/cap-05-consonancia` | 5 — A Consonância | Caps. 6 e 7 na `main` | — |
| 5 | `agent-cap-08` | `claude/cap-08-algebra-linear` | 8 — Álgebra Linear | nenhuma lógica; produzir na onda do 5 | paralelo seguro com o 5 (diretórios disjuntos) |
| 6 | `agent-cap-09` | `claude/cap-09-integral` | 9 — A Integral | Caps. 1–8 fechados | reabre retificação por referência |
| 7 | `agent-cap-10` | `claude/cap-10-fabrica` | 10 — A Fábrica de Funções | Cap. 9 fechado | julga C4 do Cap. 1; reabre e^{iθ} |
| 8 | `agent-cap-11` | `claude/cap-11-fourier` | 11 — Fourier | Caps. 5, 7, 8, 9, 10 fechados | — |
| 9 | `agent-cap-12` | `claude/cap-12-sintese` | 12 — Síntese | todos fechados | critério E16 |

**Infraestrutura (coordenadora):** gate v2 (`tools/bundle.mjs` +
`tools/validate-release.mjs`) no fechamento formal do 3º capítulo;
reauditoria E9 dos fechados a cada endurecimento; aplicação retroativa da
E22 (§5, W2) como pendência editorial auditável.

## 4.1 Política de alocação de paralelismo

Quantos agentes produtores rodar ao mesmo tempo. O teto estrutural em cada
momento é o número de frentes **logicamente destravadas** com diretórios
disjuntos (§2); o número recomendado fica abaixo do teto, por três razões
operacionais comprovadas em 28/07/2026:

1. a fila de merge é serializada (§1) — cada produtor a mais envelhece as
   branches dos outros (causa raiz da colisão E20 e dos conflitos do PR #8);
2. o gargalo real é o leitor primário — capítulo produzido além da
   capacidade de veredito vira estoque, não progresso;
3. revisões de capítulo em avaliação (tags em emissão) criam alvo móvel —
   no máximo **uma revisão** em curso por vez.

| Fase | Frentes destravadas | Recomendado | Composição |
|---|---|---|---|
| **Atual (pós-tags D1/D2′/D4/D5)** | 6, 7, 8, 2-r2 | **4 + coordenadora** | `agent-cap-06` ∥ `agent-cap-07` ∥ `agent-cap-08` ∥ `agent-cap-02r2` |
| Após fechar 6 e 7 | 5 (+ revisão pendente) | 2 + coordenadora | `agent-cap-05` ∥ revisão remanescente |
| Cauda (9 → 10 → 11 → 12) | cadeia estritamente sequencial | 1 + coordenadora | um agente por vez; paralelismo extra não acelera a lógica |

A curva do projeto é 4 → 2 → 1. Aumentar além do recomendado só é
justificável se o leitor primário estiver com a fila de vereditos vazia; o
teto estrutural nunca pode ser excedido. A coordenadora não produz capítulo
enquanto houver ≥ 2 produtores ativos (integração vira o trabalho dela).

## 5. Trabalhos registrados pelo autor em 28/07/2026

### W1 — Cap. 2, revisão r2: a fração canônica das ternas primitivas

Registro da proposta do autor (leitor primário), para pré-registro formal
pelo agente da revisão (§1.3 — o pré-registro pertence ao agente, este
parágrafo é o contrato editorial):

O Cap. 2 já prova a regra canônica do autor nas duas direções
(`chapter-02.odd-triple-forward` e `chapter-02.consecutive-classification`):
todo ímpar n ≥ 3 como menor cateto forma a terna (n, (n²−1)/2, (n²+1)/2),
com perímetro n(n+1), e toda terna com hipotenusa e cateto maior
consecutivos é desta família. **O que falta — e é o acréscimo do autor — é
a contagem:** entre os triângulos retângulos inteiros *primitivos* (já
reduzidos por divisores comuns, portanto não múltiplos 2x, 3x de um
inicial), qual fração obedece à regra canônica? Duas contagens honestas a
desenvolver: (a) fixado o cateto ímpar n, quantas ternas primitivas o têm
como cateto e qual delas é a canônica (a resposta envolve o número de
fatores primos distintos de n); (b) ordenando por hipotenusa ≤ H, o
comportamento assintótico da fração (a família canônica cresce como √H
enquanto o total primitivo cresce linearmente — a fração tende a zero, e a
taxa é o conteúdo). Porta com a densidade de Lehmer H/(2π) declarável como
`cited`.

### W2 — E22: fundação geométrica visual (aplicação retroativa)

Emenda E22 comitada (MATH3us.md §6.1 item 11, registro §13): todo uso de
trigonometria precedido da figura do triângulo retângulo com as definições
escolares formais — sen θ = cateto oposto/hipotenusa, cos θ = cateto
adjacente/hipotenusa, tg θ = oposto/adjacente — figura e razão juntas.
Aplicação retroativa: auditoria editorial dos Caps. 0–4 (onde a
trigonometria comparece sem o preâmbulo visual) como pendência não
bloqueante; a reconstrução D3 do Cap. 1 é o veículo natural da correção no
capítulo mais afetado.

## 6. Braço MATHeu$ (PR #6) — política

Braço **complementar**, por decisão do autor: não substitui capítulo, não
corrige capítulo, não entra no grafo de `claims.yml` do tratado. Análise da
coordenadora (28/07/2026): conteúdo real e autocontido (~30 KB, sem
dependência externa); ledger próprio com claims corretos; auditoria
**exploratória apenas** — o próprio branch declara que faltam oráculo
versionado, auditoria semântica automática, screenshots commitados e teste
real em iOS antes de qualquer release. Mescla limpa contra a `main` (só
arquivos novos). Política: pode ser mesclado como braço a qualquer momento
(decisão do leitor primário), ficando `arms/` fora dos gates do tratado até
que o braço adote gates próprios; ou permanecer aberto como laboratório.

## 7. Registro de handoff

Todo agente novo recebe, além do protocolo §5 do models.md: (i) este
ROADMAP.md; (ii) a instrução de rebase da §1; (iii) seu escopo de arquivos
da §2; (iv) a E22 como obrigação de template desde já.
