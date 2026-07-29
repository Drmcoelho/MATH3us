# CLAUDE.md

Orientação para instâncias do Claude Code trabalhando neste repositório.

## O que é este repositório

MATH3us é um tratado matemático auditável, em português, publicado como páginas
estáticas (GitHub Pages / Vercel). Não há aplicação, build nem `package.json`:
a unidade de entrega é o **capítulo fechado** — um diretório `caps/NN-slug/`
cujo `index.html` é **100% autocontido** (zero requisições de rede, zero CDN,
zero fonte remota; invariante desde o gate v0). A constituição do projeto é o
[MATH3us.md](MATH3us.md); em conflito com qualquer outro documento, o manual vence.

Convenção de idioma: prosa em português; código, commits e branches em inglês.

## Comandos de verificação (os "testes" do projeto)

Dependências Node instaladas ad hoc (não vendoradas):
`npm install --no-save js-yaml ajv playwright`, resolvidas via `node_modules`
ou `NODE_PATH`. O Chromium do Playwright pode ser apontado por `PW_CHROMIUM`
(em ambientes remotos, `/opt/pw-browsers/chromium` é detectado automaticamente).

```bash
# Gate v1 — validação do ledger (schema, ids, dependências, ciclos,
# âncoras de prova, artefatos, compatibilidade kind/status/proof_mode)
node tools/verify-claims.mjs caps/02-ternas

# Oráculo numérico triplo (stdlib Python; regrava artefatos em audit/)
python3 caps/02-ternas/oracle.py     # caps 2–4
python3 tools/oracle.py              # cap 1
python3 tools/oracle-ch00.py         # cap 0

# Gate v0 — auditoria de página com Playwright (interação, teclado,
# overflow, canvas pintado, autocontenção; screenshots em audit/)
node caps/02-ternas/audit.mjs        # caps 2–4 (script próprio por capítulo)
node tools/audit.mjs caps/01-exaustao   # cap 1
node tools/audit-ch00.mjs            # cap 0

# Gate v2 — empacotamento e validação de release
node tools/bundle.mjs caps/02-ternas
node tools/validate-release.mjs caps/02-ternas
```

O CI (`.github/workflows/coordination-sweep.yml`) roda diariamente os gates
v1 e v2 sobre todos os capítulos e abre issue em caso de falha. Os oráculos e
o gate v0 não rodam no CI — são executados pelo agente do capítulo, que comita
os artefatos.

Atenção: oráculos e auditorias **regravam** artefatos versionados em
`caps/NN-*/audit/` (com data e commit novos). Rodá-los para conferência é
bem-vindo, mas não comite artefatos regenerados por acidente — restaure com
`git checkout -- caps/` se a execução foi só verificação.

## Estrutura

- `caps/NN-slug/` — capítulo autocontido: `index.html`, `conjecturas.md`
  (pré-registro), `claims.yml` (ledger, namespace `chapter-NN.*`),
  `sources.md` (dossiê), `audit/` (artefatos), e opcionalmente `oracle.py`
  e `audit.mjs` próprios.
- `schemas/claims.schema.json` — schema do ledger (gate v1).
- `releases/manifests/` — capítulo fechado ⇔ manifest presente; dependência
  entre capítulos só é válida para capítulo fechado ou marcada `door: true`.
- `tools/` — validadores e oráculos compartilhados.
- `arms/matheus-dollar/` + `MATHeu$.md` — braço separado do tratado; não
  referencia nem é referenciado pelos `claims.yml` dos capítulos.
- `AUDIT.md` — estado de auditoria e decisões do leitor primário;
  `ROADMAP.md` — fila de PRs e matriz de propriedade; `models.md` — divisão
  entre sessões-agente.

## Regras operacionais (doutrina — não violar)

1. **Matriz de propriedade de arquivos** (ROADMAP.md §2): agente de capítulo
   só toca `caps/NN-*/` do seu capítulo. `MATH3us.md`, `models.md`,
   `ROADMAP.md`, `AUDIT.md`, `index.html` da raiz, `tools/`, `schemas/` e
   `releases/` pertencem à sessão-coordenadora — agentes propõem mudanças no
   corpo do PR, não as fazem.
2. **Pré-registro**: `conjecturas.md` nasce em commit separado, antes de
   qualquer linha do `index.html` do capítulo.
3. **Sem reescrita silenciosa pós-release**: tags são imutáveis; correção
   após release gera revisão explícita (rN) com commit, changelog e
   reauditoria próprios.
4. **Emendas ao manual nunca nascem numeradas em branch de agente** — o
   agente propõe; a numeração E é atribuída na integração.
5. **Um PR por capítulo**, branch `claude/cap-NN-<slug>`, escopo de arquivos
   declarado no título; sincronizar com `origin/main` antes de abrir o PR.
6. **Acessibilidade mínima** (E4/E14): fórmulas com representação textual ou
   MathML (nunca imagem), controles operáveis por teclado, contraste AA,
   nenhuma informação transmitida só por cor.
