# Capítulo 6 — As Patologias · Registro de fontes

Estado em 28/07/2026.

## Estado documental (território virgem — declaração de assimetria, §1.2)

**Não existe sítio pessoal para este capítulo, e essa ausência é o registro
honesto.** Nenhuma das funções, teoremas ou construções aqui tratados foi
intuída, conjecturada ou redescoberta pelo autor antes do tratado; nenhuma
anotação, conversa ou tentativa anterior foi localizada — porque não há o que
localizar. Nos termos da E2, o mecanismo de honestidade deste capítulo é o
**pré-registro prospectivo com força plena** (`conjecturas.md`, commit próprio
anterior ao desenvolvimento), não uma cadeia de proveniência de dossiê. O
capítulo não fingirá redescoberta: todo o conteúdo clássico entra importado e
declarado, demonstrado ou citado item a item no `claims.yml`.

## Materiais clássicos utilizados (proveniência `classical`)

| Material | Uso no capítulo | Estado |
|---|---|---|
| P. G. L. Dirichlet, memória sobre séries de Fourier (1829) — origem histórica da função indicadora de ℚ como exemplo-limite | Definição na seção 4; teorema da descontinuidade total demonstrado na seção 5.5 | Atribuição histórica de conhecimento consolidado; **edição de referência não consultada em original** — a fixar na release |
| J. Thomae, *Einleitung in die Theorie der bestimmten Integrale* (1875) — a função "pipoca" | Definição na seção 4; teorema completo (ε-δ, finitude dos denominadores pequenos) demonstrado na seção 5.6 | Idem — atribuição consolidada; original não consultado |
| K. Weierstrass, comunicação à Academia de Berlim (1872) — primeira função contínua sem derivada publicada | **Somente contexto citado** na seção 5.7; nenhuma propriedade sua é usada; prova completa = exercício N4 E4.3, porta → Cap. 10 | Citada sem prova e sem uso; original não consultado |
| T. Takagi, *A simple example of the continuous function without derivative* (1901); B. L. van der Waerden (1930), redescoberta com base 10 | Objeto central das seções 5.7–5.10; continuidade via importação declarada; não diferenciabilidade **demonstrada integralmente** pelo argumento combinatório diádico | A construção é clássica; as provas das seções 5.8–5.10 foram redigidas para este tratado na forma dos declives inteiros S_m; originais não consultados |
| Teste M de Weierstrass + continuidade do limite uniforme | Importação declarada (caixa de porta na seção 5.7); única dependência demonstrativa externa do capítulo | `proof_mode: cited`; porta fechada → Capítulo 10 |
| B. Bolzano (1817) / A.-L. Cauchy — Teorema do Valor Intermediário | Demonstrado na seção 5.11 a partir do princípio do supremo (Cap. 1) | Resultado clássico com prova própria no texto |
| G. Darboux (1875) — derivadas têm a propriedade do valor intermediário | Nota citada na seção 5.11, sem prova e sem uso | `proof_mode: cited`; teoria fina de derivadas fora deste ciclo |
| Irracionalidade de √2 (tradição pitagórica; Euclides, *Elementos* X) | Demonstrada na seção 5.1 (paridade); cunha de metade do capítulo | Clássico com prova própria no texto |
| Assintótica de Farey/totientes Φ(Q) ~ 3Q²/π² (Mertens, 1874) | Calibração da conjectura C2 (tabela da seção 2 + oráculo I5) | **Não demonstrada** (exigiria teoria analítica, fora do ciclo — §11); registrada como `estimate` com verificação `computational_only` |
| Princípio da boa ordenação (ℤ limitado inferiormente tem menor elemento) | Usado declaradamente na prova da densidade (5.3) | Princípio aritmético básico, mesmo estatuto da divisão euclidiana nos Caps. 2–4 |

## Distinções (protocolo §9)

- **Reconstrução atual:** todo o texto de `index.html` é redação de
  28/07/2026 para este tratado; as provas seguem caminhos clássicos, mas a
  organização (declives inteiros S_m pela janela de m dígitos; testemunhas
  explícitas r′ e t no buraco de ℚ; o traçador mentiroso como experimento
  central) é edição própria.
- **Registro:** `conjecturas.md` (pré-registro de 28/07/2026, commit
  anterior ao desenvolvimento — força plena, E2).
- **Memória:** nenhuma alegação baseada em memória foi incluída; não há
  memória a incluir.
- **Proveniência executável (E12):** os artefatos canônicos estão em
  `audit/` e registrados em `claims.yml`; a verificação exploratória de
  planejamento (28/07/2026) está declarada em `conjecturas.md`, item a item.

## Pendências

1. Fixar edições de referência dos originais (Dirichlet 1829, Thomae 1875,
   Weierstrass 1872, Takagi 1901, van der Waerden 1930) — nenhum original
   foi consultado nesta sessão; as atribuições são de conhecimento
   consolidado e estão declaradas como tal.
2. Se alguma edição consultada divergir da atribuição consolidada (data,
   enunciado, prioridade), registrar a divergência aqui e no capítulo —
   nunca sobrescrever.
