# Capítulo 3 — A Singularidade do Quatro · Pré-registro de conjecturas

**Tipo declarado:** escavação.
**Data do pré-registro:** 28/07/2026.
**Estatuto (§1.3, E2):** o sítio pessoal — o contato original do autor com a
observação 2+2 = 2·2 = 2² — **ainda não foi minerado**: nenhum fragmento
verbatim foi localizado ou commitado até esta data. A lacuna fica declarada
e não será preenchida com memória apresentada como fato; `sources.md`
registrará o estado documental. A observação em si tem estatuto de
**contrato editorial** (MATH3us.md §3, Capítulo 3), não de conjectura
pré-registrada. As conjecturas abaixo referem-se ao desenvolvimento que o
capítulo fará a partir de agora — para elas o pré-registro vale com força
probatória plena.

**Declaração de exploração prévia (E12, honestidade):** antes deste
registro, em 28/07/2026, foi executada exploração numérica **não canônica**
(python3, implementação única, sem artefato versionado) para calibrar as
confianças abaixo. Ela é declarada, não escondida: os exemplos citados vêm
dela. O oráculo canônico, com script e artefatos em `audit/`, será
executado no desenvolvimento.

---

## Pergunta central (registrada antes do desenvolvimento)

> Para quais números positivos x as três regras — somar consigo (x+x),
> multiplicar por si (x·x), elevar a si (x^x) — produzem **o mesmo
> resultado**? A coincidência 2+2 = 2·2 = 2² = 4 é acidente de notação ou
> singularidade estrutural?

---

## Conjecturas

### C1 — Os conjuntos par a par não coincidem
**Enunciado:** em ℝ⁺, o conjunto solução de x+x = x² é {2}; o de
x² = x^x é {1, 2}. Os dois conjuntos são diferentes — a solução extra
x = 1 aparece porque ln 1 = 0 anula o fator logarítmico, não porque 1
"quase" satisfaça a outra equação.
**Confiança inicial:** alta.
**Exemplos disponíveis:** k = 1: (2, 1, 1); k = 2: (4, 4, 4); k = 3:
(6, 9, 27); varredura exploratória de inteiros não achou outras soluções.
**Refutadores possíveis:** qualquer outra solução real positiva de uma das
duas equações; falha do caso x = 1 na fatoração (x−2)·ln x = 0.

### C2 — A terceira equação esconde uma raiz não óbvia
**Enunciado:** x+x = x^x (isto é, 2x = x^x) tem em ℝ⁺ **exatamente duas**
soluções: x = 2 e uma segunda raiz r no intervalo (0, 1), com
r ≈ 0,3463 (exploração numérica). A existência sairá do teorema do valor
intermediário com troca de sinal exibida; a unicidade em cada ramo, da
monotonia de (x−1)·ln x. A forma fechada de r não será alcançável com o
aparato do capítulo (ver C4).
**Confiança inicial:** média-alta (existência e valor aproximado já
observados na exploração; a *unicidade* é o que o desenvolvimento deve
provar e ainda pode surpreender).
**Refutadores possíveis:** uma terceira raiz positiva encontrada
numericamente; não monotonia de (x−1)·ln x em (0,1) ou em (1,∞).

### C3 — A coincidência tripla é só o 2
**Enunciado:** a interseção dos três conjuntos solução em ℝ⁺ é {2}, com
valor comum 4. Em particular x = 1, que satisfaz x² = x^x, falha em
x+x = x² (1+1 = 2 ≠ 1). Corolário inteiro: 4 é o único número expressável
como k+k = k·k = k^k com k inteiro positivo.
**Confiança inicial:** alta.
**Refutadores possíveis:** qualquer x > 0 com as três igualdades além
de 2 — bastaria um.

### C4 — A porta de Lambert
**Enunciado:** a raiz r de C2 não possui forma fechada nas operações e
funções que este capítulo declara (aritmética, raízes, ln importado);
expressá-la exige a função W de Lambert, cuja construção pertence ao
Capítulo 10. No capítulo, r entrará como raiz **localizada numericamente**
com certificado de troca de sinal — porta fechada, não derrota disfarçada.
**Confiança inicial:** média (a redutibilidade a W é clássica; a
inexpressabilidade elementar estrita é crença informada, não teorema que o
capítulo provará).
**Refutadores possíveis:** forma fechada elementar de r encontrada dentro
do aparato declarado — exigiria autópsia e reclassificação.

### C5 — A lição da variação de regras
**Enunciado:** comparadas as três equações par a par, as coincidências
duplas serão **comuns e desarrumadas** — {2}, {1, 2}, {r, 2}, três
conjuntos diferentes — e só a coincidência **tripla** isola o 2. A
singularidade do quatro é estrutural (sobrevive a mudança de base e de
notação); o algarismo "4" é figurino decimal.
**Confiança inicial:** alta para a parte matemática; a parte final é
síntese organizacional (tipagem `synthesis` no ledger, prioridade
histórica não estabelecida — a observação 2+2 = 2·2 é folclore clássico).
**Refutadores possíveis:** os conjuntos par a par colapsarem no mesmo
conjunto (refutaria "desarrumadas"); a coincidência tripla admitir outra
solução (refutaria a singularidade).

---

## Condições gerais de refutação

Qualquer contraexemplo numérico reprodutível no experimento ou no oráculo
do capítulo, ou falha lógica apontada nas demonstrações, obriga autópsia
nos termos da §1.3 — a conjectura ferida permanece no registro.

## O que este pré-registro não é

Não é reivindicação de prioridade: a observação-sítio é folclore
matemático clássico, e a teoria usada (fatoração, logaritmo, valor
intermediário) é clássica. O que o capítulo reivindica é o **caminho de
reconstrução** — e a honestidade sobre qual parte é teorema, qual é
estimativa numérica e qual é porta fechada.
