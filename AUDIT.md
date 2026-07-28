# AUDIT.md — Estado de auditoria e decisões pendentes

> Registro vivo, na raiz do repositório, do estado de auditoria de cada
> capítulo e das **decisões reservadas ao leitor primário**. Complementa —
> não substitui — a definição de capítulo fechado (MATH3us.md §10), a
> convenção de releases (§1.7) e os artefatos por capítulo em `caps/*/audit/`.
> Atualizado em toda sessão que altera estado de auditoria; a fotografia
> abaixo vale para o commit indicado.

**Fotografia:** 28/07/2026 · integração do merge main ↔ prólogo (PR #8) · branch
`claude/chapter-1-geometric-rebuild-uf3z1f`.

---

## 1. Estado por capítulo

| Cap. | Título | Pré-registro | Oráculo triplo | Gate v0 | Ledger | Release |
|---|---|---|---|---|---|---|
| 0 | A Inferência | `conjecturas.md` commitado antes do desenvolvimento (`9f46b8f`) | 12/12 invariantes, 3 implementações independentes (`31bc78c`; artefatos em `caps/00-inferencia/audit/`) | 31/31 checks, desktop + iPhone, screenshots inspecionados (`c8221c7`) | `claims.yml` válido, campos ortogonais, registro E12 | **nenhuma — aguarda Decisão D1** |
| 1 | A Exaustão | `conjecturas.md` (pré-desenvolvimento; C5 refutada com autópsia) | invariantes + adversariais; ¼ promovido a teorema via fatoração exata (main, `f770cc9`) | Re-executado pós-merge sobre o conteúdo integrado | `claims.yml` válido; `correction_log` do fator 2 mesclado à promoção | **cap-01-gate0-r1** (`085e494`); correções pós-release neste merge — **aguarda Decisão D2′ (r2)** |
| 2–12 | — | contrato editorial no manual | — | — | — | previstos |

Nenhum item vigente do §10 está pendente para os Capítulos 0 e 1 **exceto a
tag de release** — que o manual reserva, deliberadamente, a um ato humano.

---

## 2. Decisões pendentes do leitor primário

### D1 — Tag de release do Capítulo 0: `cap-00-gate0-r1`

**O que é.** O ato que fecha o capítulo (§1.7, §10): uma tag Git **imutável**
apontando para o commit auditado. Depois dela, qualquer correção de conteúdo
gera revisão explícita (`cap-00-gate0-r2`), com commit, changelog e
reauditoria próprios — nunca reescrita silenciosa.

**Estado que a tag congelaria.** O commit de merge do PR #8 (estado
integrado): Enunciados A–K demonstrados por desigualdades sem linguagem de
limite; oráculo 12/12; gate v0 31/31; incidente n = 170 registrado (ver §4).
Nota de gate: com o Cap. 1 fechado, o Cap. 0 será o **segundo** capítulo
fechado — o gate v1 (§1.7) passa a valer, e `tools/verify-claims.mjs` foi
executado sobre o ledger na integração.

**Execução, quando decidida:**

```
git tag -a cap-00-gate0-r1 <commit-de-merge> -m "chapter 0 release: gate v1, content revision 1"
git push origin cap-00-gate0-r1
```

acompanhada do manifest em `releases/manifests/` (§1.7):

```yaml
chapter: 0
content_revision: 1
gate_version: 1
commit: <commit-de-merge>
previous_release: null
```

**Por que é sua.** Tag imutável é compromisso público do tratado; o manual
não delega compromisso a agente.

### D2 — Tag de release do Capítulo 1 — **EXERCIDA no main** (28/07/2026)

A tag `cap-01-gate0-r1` foi criada no main (`085e494`, manifest em
`releases/manifests/cap-01-gate0-r1.yml`), junto com a promoção do ¼ a
teorema, a refutação de C5 (autópsia em `conjecturas.md`) e o tooling de
gate v1. Decisão registrada; nada mais pendente sob este número.

### D2′ — Revisão r2 do Capítulo 1: `cap-01-gate0-r2`

**Por que existe.** A integração do merge (PR #8) trouxe ao Capítulo 1
correções de conteúdo **posteriores à tag r1**: a constante da folga de
semiperímetros — escrita como π³/n² também na redação paralela da promoção
e no gabarito do exercício E4.2 — foi corrigida para π³/(2n²), com nota de
registro na seção 6. Pela E9, correção de conteúdo pós-release recebe
revisão explícita: `cap-01-gate0-r2`, com manifest apontando
`previous_release: cap-01-gate0-r1`. Gate v0 re-executado sobre o conteúdo
integrado (artefatos em `audit/`).

**Execução, quando decidida:** tag `cap-01-gate0-r2` no commit de merge +
manifest com `content_revision: 2`.

**Interação com a D3.** Inalterada: a reconstrução geométrica futura seria
r3 (ou a r2 pode esperar a reconstrução, a critério editorial).

### D3 — Reabertura do Capítulo 1: a reconstrução geométrica sobre a cunha

**O que é.** Pendência editorial registrada em E21 (MATH3us.md §3, §13; emenda nascida "E20" em branch paralela e renumerada na integração pela colisão com a E20 dos exercícios) e no
`sources.md` do Capítulo 0: reconstruir o Capítulo 1 em torno do triângulo
fundamental R, r, L/2 e dos **dois cercos** — por perímetro e por área.
Escopo fixado pelo documento fundador de 28/07/2026 (crítica do leitor
primário, verbatim em `caps/00-inferencia/sources.md`):

- a cunha fundamental antecedendo a_n = n·sen θ e b_n = n·tg θ;
- as áreas: A⁻_n = a_n²/b_n, A⁺_n = b_n, e a identidade A⁻_{2n} = a_n;
- a cadeia A⁻_n < A⁻_{2n} = a_n < π < b_{2n} = A⁺_{2n} < A⁺_n;
- a diferença de áreas ΔA_n = (b_n − a_n)(b_n + a_n)/b_n ∼ 2(b_n − a_n);
- a dualidade assintótica dos erros (π³/6n², π³/3n² para semiperímetros;
  2π³/3n², π³/3n² para áreas — o erro dominante troca de lado);
- os quatro laboratórios gráficos (perímetros, áreas, perímetro × área,
  evolução da cunha com zoom normalizado);
- ~~reavaliação da conjectura C4/C5~~ — **resolvida no main em 28/07/2026**,
  antes desta reconstrução: C5 refutada (autópsia em `conjecturas.md` do
  Cap. 1) e o ¼ promovido a teorema via fatoração exata da folga, achada no
  desenho do exercício E3.1. O item sai do escopo de D3.

**Estado.** Não iniciada. O Capítulo 0 já fornece o átomo (a cunha) e o zoom
normalizado legítimo; a reconstrução os importa em vez de recriá-los.

**Opções em aberto:** (a) reconstruir já; (b) taggear D1 e D2′ primeiro e
reconstruir como revisão seguinte; (c) adiar com prioridade explícita para a
ordem de produção (§5: os Capítulos 2–4 já estão em produção no main).

---

## 3. Pendências declaradas, não bloqueantes

| Pendência | Onde está declarada | Bloqueia release? |
|---|---|---|
| Mineração do sítio pessoal do Cap. 1 (fragmentos verbatim) | `caps/01-exaustao/sources.md` | Não (lacuna declarada, E2) |
| Dedução euclidiana pura das recorrências (dossiê) | `caps/01-exaustao/sources.md` | Não |
| Edição de referência de *A Medida do Círculo* | `caps/01-exaustao/sources.md` | A fixar na release |
| Busca bibliográfica de prioridade dos sanduíches G–H e da formulação inferencial | `caps/00-inferencia/sources.md` → **parcialmente executada**, análise em `caps/00-inferencia/prioridade.md` (28/07/2026): substância clássica confirmada onde já declarada; nenhum equivalente localizado para o limiar cúbico e a janela crepuscular; permanece "prioridade não estabelecida" | Não (§1.12) |

---

## 4. Registro consolidado de incidentes de auditoria

Os incidentes são dados (§12 do manual). Detalhes nos artefatos citados.

| Data | Cap. | Incidente | Desfecho | Registro |
|---|---|---|---|---|
| 28/07/2026 | 1 | Cota de erro enunciada com `<` estrito, falsa em k = 0 | Corrigida antes do run aprovado | `claims.yml` (I6), §5.2 do capítulo |
| 28/07/2026 | 1 | Lupa em branco em zoom alto + famílias de contato coincidentes (relato iOS do leitor primário) | Render refeito; novo invariante | rodapé do capítulo, `audit_run.history` |
| 28/07/2026 | 1 | Falso positivo do invariante da lupa por amostragem esparsa (aliasing) | Leitura de todos os pixels | `audit_run.history`, comentário em `tools/audit.mjs` |
| 28/07/2026 | 1 | **Troca de constante**: π³/n² atribuída à folga de semiperímetros (pertence à folga de áreas); detectada pelo leitor primário | Corrigida (π³/(2n²)); verificação numérica no commit `2950338`; re-audit `be998ae` | §6 do capítulo, `correction_log` em `claims.yml` |
| 28/07/2026 | 0 | **Exemplo trabalhado refutado**: texto afirmava n = 170 identificável em δ = 10⁻⁶; oráculo mediu g₁₇₀/2 = 9,956·10⁻⁷ < δ | Corrigido (commit `31bc78c`); nota de auditoria no §6 | invariante I10, `correction_log` em `claims.yml`, `edge-cases.md` |
| 28/07/2026 | 0 | Folga afogada em cancelamento: forma direta cos−cos "violou" o sanduíche 174.477 vezes | Forma de produto adotada; falha da forma ingênua promovida a invariante obrigatório (I6b) | §8 do capítulo, `edge-cases.md` |
| 28/07/2026 | 0 | Colapso float64: 1 − cos(π/n) = 0 exato em n = 3·10⁸ | Documentado como imperfeição computacional (C0.8 confirmada, I11) | §8 do capítulo, `edge-cases.md` |
| 28/07/2026 | 1 | **A constante trocada reapareceu**: a redação paralela da promoção do ¼ (main, pós-release r1) reescreveu π³/n² para a folga de semiperímetros — no texto, no gabarito de E4.2 e no ledger — sem absorver a correção que corria em branch paralela | Corrigida na integração do merge (PR #8); motiva a decisão D2′ (r2) | §6 do capítulo, `correction_log` mesclado em `claims.yml` |
| 28/07/2026 | — | **Colisão de emendas**: duas branches usaram "E20" (exercícios, pr-05; Capítulo 0) | E20 dos exercícios mantida (primeira no main); Capítulo 0 renumerado E21 com nota de integração na própria linha da emenda | MATH3us.md §13 |

---

## 5. Histórico de execuções canônicas

| Data | Script | Cap. | Commit do código | Resultado | Artefato |
|---|---|---|---|---|---|
| 28/07/2026 | `tools/oracle.py` | 1 | `d8dc136` | run 1: falha I6 → correção → run 2: aprovado | `caps/01-exaustao/audit/numeric-check.json` |
| 28/07/2026 | `tools/audit.mjs` | 1 | `34d28c4` | aprovado (pós-correção de render) | `caps/01-exaustao/audit/interaction-report.json` |
| 28/07/2026 | `tools/oracle-ch00.py` | 0 | `31bc78c` | run 1: falha I10 → correção → run 2: 12/12 | `caps/00-inferencia/audit/numeric-check.json` |
| 28/07/2026 | `tools/audit-ch00.mjs` | 0 | `c8221c7` | aprovado, 31/31 | `caps/00-inferencia/audit/interaction-report.json` |
| 28/07/2026 | `tools/audit.mjs` | 1 | `be998ae` | re-run sobre conteúdo corrigido: aprovado | `caps/01-exaustao/audit/interaction-report.json` |
| 28/07/2026 | `tools/oracle.py` + `tools/audit.mjs` | 1 | pós-merge PR #8 | re-execução sobre o conteúdo integrado (promoção do ¼ + correção da constante) | `caps/01-exaustao/audit/` |
| 28/07/2026 | `tools/verify-claims.mjs` (gate v1) | 0 e 1 | pós-merge PR #8 | validação de schema e dependências dos dois ledgers | saída registrada no commit de merge |

---

## 6. Como registrar uma decisão

Uma decisão do leitor primário entra no repositório, nunca só na conversa:

1. **Tag (D1/D2):** executar os comandos da decisão; commitar o manifest em
   `releases/manifests/`; atualizar a linha correspondente do §1 deste
   arquivo e o rodapé do capítulo ("release: cap-0X-gate0-r1").
2. **Reabertura (D3):** commit de abertura declarando escopo (este arquivo,
   §D3, serve de contrato inicial); novas conjecturas que surgirem recebem
   pré-registro com força plena (§1.3).
3. **Adiamento explícito:** também é decisão — registrar aqui com data e
   motivo, para que o adiamento não se disfarce de esquecimento.
