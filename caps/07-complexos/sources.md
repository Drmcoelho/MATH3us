# Capítulo 7 — ℂ · Registro de fontes

Estado em 28/07/2026.

## Estatuto do território (§1.2 — assimetria declarada)

Este capítulo é **território virgem**: não existe sítio pessoal — nenhuma
anotação, conversa ou tentativa anterior do autor sobre números complexos
suficientemente formada para escavação. A ausência não é lacuna a preencher:
é o próprio registro. Nada no capítulo é apresentado como redescoberta; o
pré-registro (`conjecturas.md`, commit próprio anterior ao desenvolvimento)
carrega força probatória plena exatamente porque o território é virgem (E2).

## Materiais clássicos utilizados (proveniência `classical`)

| Material | Uso no capítulo | Estado |
|---|---|---|
| Bombelli, *L'Algebra* (1572) — operação com quantidades "più di meno" | Seção 10 (camadas): história do nome "imaginário" | Citado como contexto histórico; nenhum resultado importado |
| Wessel (1797), Argand (1806), Gauss (1831) — o plano complexo | A construção por pares ordenados da seção 3 é a leitura moderna consolidada (formalizada por Hamilton, 1837) | Reconstruída integralmente no texto; a atribuição histórica é citada, não usada |
| Identidade de Brahmagupta–Fibonacci (dois quadrados) | Teorema 2, provado por expansão e pela rota estrutural | Provada no texto |
| Fórmulas de adição de seno e cosseno | Teorema 5 — **derivadas geometricamente** no texto (composição de rotações), não importadas; os fatos importados são os de congruência do plano (rotação preserva comprimentos/ângulos; composição soma ângulos), declarados no Lema 3 e na seção 5.3 | Derivadas aqui, com importação geométrica declarada |
| De Moivre (1707/1730) | Teorema 7, provado por indução | Provado no texto |
| Wilson–Lagrange (enunciado por Waring/Wilson 1770; provado por Lagrange 1771) | Teorema 14, provado por emparelhamento | Provado no texto |
| Fermat (1640, carta a Mersenne; provado por Euler 1749) — soma de dois quadrados | Teorema 16, provado via ℤ[i] | Provado no texto |
| Gauss, *Disquisitiones* e teoria de ℤ[i] (1832) — inteiros gaussianos, norma, divisão, primos | Seção 9 inteira: definições e Teoremas 12, 13, 17 | Reconstruídos e provados no texto |
| Euclides, *Elementos* — algoritmo do mdc; parametrização de ternas (via Cap. 2) | Elo 1 da seção 9.3 (subida para ℤ[i]); E3.2 usa a parametrização citada no Cap. 2 | Algoritmo provado aqui em ℤ[i]; parametrização citada via ledger do Cap. 2 |
| Princípio do supremo (Cap. 1 do tratado) | Lema 8 (existência da raiz n-ésima real) | Dependência interna: `chapter-01.supremum-principle` (capítulo fechado) |
| Problema do fosso gaussiano (Gordon, 1962) | Exercício N4 E4.2 | Citado como problema aberto; nada é usado |

## Distinções (protocolo §9)

- **Reconstrução atual:** todo o texto de `index.html` é reconstrução
  redigida em 28/07/2026; não há transcrição de material pessoal, porque
  não há material pessoal.
- **Registro:** `conjecturas.md` (pré-registro de 28/07/2026, commit
  anterior ao desenvolvimento — força plena, território virgem).
- **Memória:** nenhuma alegação baseada em memória foi incluída.
- **Proveniência executável (E12):** os artefatos canônicos deste capítulo
  estão em `audit/`, registrados em `claims.yml` (oracle_run, audit_run);
  todo número citado no texto foi verificado por computação antes da
  redação e reverificado pelo oráculo.

## Pendências

1. Fixar edições de referência dos materiais clássicos (Bombelli; Wessel/
   Argand/Gauss; Gauss sobre resíduos bicuadráticos/ℤ[i]; correspondência
   de Fermat; Lagrange sobre Wilson) — a fixar na release.
2. Se algum dia surgir material pessoal anterior sobre complexos, ele entra
   aqui com data e distinção explícita — e o estatuto de território virgem
   deste capítulo é revisto por emenda, nunca sobrescrito.
