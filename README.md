# MATH3us — Do Número ao Contínuo

*Reconstrução formal de uma matemática já vivida*: um tratado auditável, cuja testemunha é o próprio repositório.

**Site publicado:** https://drmcoelho.github.io/MATH3us/

## O que é

Não é um curso, uma enciclopédia nem um currículo — é uma biografia intelectual em andamento: o registro da distância entre o que foi intuído, o que foi afirmado, o que era demonstrável e o que precisou ser reconstruído. A unidade de entrega é o **capítulo fechado** — cada capítulo se declara *escavação* de uma descoberta anterior ou *território virgem* —, e nenhum resultado entra sem que sua proveniência, sua prova e seus limites estejam no ledger. A cultura do projeto é de prova e auditoria: *o experimento sugere; a demonstração obriga.*

## Como o repositório se organiza

- **[MATH3us.md](MATH3us.md)** — o manual operacional, constituição do tratado: doutrina, contratos editoriais dos capítulos, template, definição de capítulo fechado, registro de emendas.
- **[AUDIT.md](AUDIT.md)** — estado de auditoria por capítulo e decisões reservadas ao leitor primário (tags de release, reaberturas).
- **[ROADMAP.md](ROADMAP.md)** — roteiro operacional da produção multiagentes: fila de PRs, matriz de propriedade de arquivos, ondas restantes.
- **[models.md](models.md)** — divisão da produção entre sessões-agente paralelas: ondas, pré-condições, protocolo de handoff.
- **[index.html](index.html)** — portal do tratado (índice publicado dos capítulos).
- **[caps/](caps/)** — um diretório autocontido por capítulo: `index.html`, `conjecturas.md` (pré-registro), `claims.yml` (ledger), `sources.md` (dossiê) e `audit/` (artefatos de verificação).
- **[releases/manifests/](releases/manifests/)** — manifests de release: capítulo, revisão de conteúdo, versão de gate, commit.
- **[schemas/](schemas/)** — `claims.schema.json`, validação automática do ledger a partir do gate v1.
- **[tools/](tools/)** — oráculos numéricos (`oracle.py`, `oracle-ch00.py`) e auditorias de gate (`audit.mjs`, `audit-ch00.mjs`, `verify-claims.mjs`).

## Doutrina em cinco linhas

1. **Ledger de afirmações:** todo resultado relevante vive no `claims.yml` do capítulo, com campos ortogonais (`kind`, `status`, `provenance`, `proof_mode`) e dependências resolvíveis.
2. **Oráculo triplo:** derivação simbólica, verificação numérica independente e caso extremo/adversarial — com artefatos versionados em `audit/`.
3. **Gates versionados:** v0 → v1 → v2, endurecidos a cada capítulo fechado; autocontenção e funcionamento sem rede são invariantes desde o v0.
4. **Sem reescrita silenciosa pós-fechamento:** tags são imutáveis; correção de conteúdo após release gera revisão explícita, com commit, changelog e reauditoria próprios (E9).
5. **Emendas numeradas no manual:** atômicas, nunca reescritas retroativamente — uma nova emenda revoga ou corrige a antiga (§13 do MATH3us.md).

## Estado dos capítulos

Fotografia conforme o [AUDIT.md](AUDIT.md) (28/07/2026):

| Cap. | Título | Estado |
|---|---|---|
| 0 | A Inferência | **Fechado** — release `cap-00-gate0-r2` (r2: exercícios E20 + retrofit editorial, reauditados) |
| 1 | A Exaustão | **Fechado** — release `cap-01-gate0-r4` (r2: correção do fator 2; r3: reconstrução geométrica D3; r4: retrofit editorial reauditado) |
| 2 | As Ternas do Ímpar | Auditado (oráculo 10/10; gate v0 29/29; gate v1 zero achados) — aguarda tag (Decisão D4) |
| 3 | A Singularidade do Quatro | Auditado (oráculo 7/7; gate v0 31/31; gate v1 zero achados) — aguarda tag (Decisão D4) |
| 4 | Os Algarismos Repetidos | Auditado (oráculo 9/9; gate v0 41/41; gate v1 zero achados) — aguarda tag (Decisão D4) |

Capítulos 5–12: previstos — contrato editorial fixado no manual, desenvolvimento não iniciado.

## Template de capítulo

Elementos obrigatórios (§6.1 do manual): declaração de tipo; pergunta e conjecturas pré-registradas (`conjecturas.md` antes do desenvolvimento); dossiê do sítio; ledger de afirmações; demonstração canônica; experimento computacional inline; gate de verificação vigente; horizonte (portas fechadas declaradas); **exercícios em cinco níveis** (E20: do N0 socrático ao N4 "impossível por enquanto", com gabarito robusto como parte do argumento); **fundação geométrica visual** (E22: figura e razão trigonométrica juntas, objetos desenhados antes de entrarem em fórmula); **regime visual do "gibi rigoroso"** (E23: capítulo conduzido pela imagem, fórmulas em destaque, caixas de curiosidade e de segredo oculto).

## Invariantes técnicos

- `index.html` de release **100% autocontido**, funcionando sem rede — invariante desde o gate v0 (E9);
- nenhuma dependência de CDN, fonte remota, API externa ou biblioteca de renderização carregada em runtime;
- acessibilidade funcional mínima (E4/E14): fórmulas com representação textual ou MathML, controles operáveis por teclado, contraste AA, nenhuma informação transmitida apenas por cor.

## Contribuição

O fluxo de trabalho é regido pelo [ROADMAP.md](ROADMAP.md): um PR por vez na fila de merge, com escopo de arquivos declarado no título e conferido contra a matriz de propriedade. Emendas ao manual nunca nascem numeradas em branch de agente — o agente propõe no corpo do PR e a numeração é atribuída na integração.
