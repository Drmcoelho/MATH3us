# Capítulo 4 — Os Algarismos Repetidos · Registro de fontes

Estado em 28/07/2026.

## Estado documental do sítio (escavação — cláusula E2)

O sítio pessoal deste capítulo (o fascínio original por algarismos
repetidos — 8, 80, 44 — e pela dízima 0,142857̄ do sete: anotações,
conversas, tentativas) **ainda não foi minerado**. Nenhum fragmento
verbatim foi localizado ou commitado até esta data. Nos termos da §1.3 do
manual, esta lacuna fica declarada — e não será preenchida com memória
apresentada como fato. Quando a mineração ocorrer, cada fragmento entrará
aqui com origem, data e distinção explícita entre fala original,
transcrição, resumo posterior e reconstrução atual. Os quatro marcadores
do sítio (8, 80, 44, 0,142857̄) constam do contrato editorial do
MATH3us.md §3 e são usados no capítulo apenas como marcadores, sem
qualquer narrativa reconstruída de memória em torno deles.

## Materiais clássicos utilizados (proveniência `classical`)

| Material | Uso no capítulo | Estado |
|---|---|---|
| Algoritmo da divisão longa (aritmética elementar consolidada) | Enunciado A: a expansão como máquina de restos; motor do experimento | Conteúdo clássico; a formulação como máquina de estados com o invariante r_k = a·b^k mod d é redação do tratado, declarada como tal |
| Critério de terminação de fração em base b (teoria elementar dos números, consolidada) | Enunciado B; provado integralmente no capítulo (`proof_mode: proved_here`) | Clássico; nenhuma reivindicação de prioridade |
| Lema de Euclides–Gauss (d \| a·m, gcd(a,d)=1 ⟹ d \| m) | Passo da recíproca do critério; prova curta via TFA incluída | Clássico (Elementos VII / Disquisitiones); citado com prova curta |
| Teorema Fundamental da Aritmética (fatoração única) | Base do lema acima, da equivalência (ii)⟺(iii) e da cisão d = d_b·d′ | Clássico; importado e declarado, não provado aqui |
| Euclides, *Elementos*, IX.20 (infinitude dos primos) | Corolário "nenhuma base incorpora todos os primos" | Clássico; prova curta reproduzida no capítulo (`#euclides`) |
| Período = ordem multiplicativa; primos full-reptend; permutações cíclicas de 1/p | Enunciados D/E e seção 6; provas completas no capítulo | Teoria clássica consolidada (Gauss, Disquisitiones, art. 315–318, trata os períodos de frações decimais); o termo *full-reptend* é da literatura recreativa/clássica em inglês, declarado como termo importado |
| Conjectura de Artin sobre raízes primitivas (1927); Hooley 1967 (condicional à GRH); Heath-Brown 1986 | Porta fechada e exercício E4.1 — problema declarado aberto | Citados como estado da arte; nenhum destes resultados é usado em prova do capítulo |
| Borel 1909 (quase todo real é normal); Champernowne 1933 (0,123456789101112… é normal na base 10) | Porta fechada e exercício E4.3 | Citados; fora do primeiro ciclo (teoria da medida) |

## Verificações computacionais próprias

Todos os valores numéricos citados no texto (períodos, ordens, expansões,
os múltiplos de 142857, os dois ciclos do 13, ord de 998001 e 9801, a
lista de full-reptend < 100) foram verificados em 28/07/2026 com python3
antes da redação; a verificação canônica com artefatos é a do oráculo
(`oracle.py` → `audit/numeric-check.json`, `audit/edge-cases.md`), nos
termos de E12.

## Distinções (protocolo §9)

- **Reconstrução atual:** todo o texto de `index.html` é reconstrução
  redigida em 28/07/2026; nada nele é transcrição de material do sítio.
- **Registro:** `conjecturas.md` (pré-registro de 28/07/2026, commit
  próprio anterior ao desenvolvimento).
- **Memória:** nenhuma alegação baseada em memória foi incluída.

## Pendências

1. Minerar o sítio pessoal e povoar este arquivo com os fragmentos
   (8, 80, 44 e a história pessoal com o 142857).
2. Fixar edições de referência (Euclides IX.20; Gauss, Disquisitiones,
   artigos sobre períodos decimais) na release.
