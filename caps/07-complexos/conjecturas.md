# Capítulo 7 — ℂ · Pré-registro de conjecturas

**Tipo declarado:** território virgem.
**Data do pré-registro:** 28/07/2026.
**Estatuto (§1.3, E2):** território virgem — não existe descoberta pessoal
anterior suficientemente formada para ser escavada, e a assimetria fica
declarada (§1.2): este capítulo não fingirá redescoberta. Por ser virgem,
**o pré-registro tem força probatória plena**: tudo o que está abaixo foi
escrito e commitado antes de qualquer linha de `index.html`.

**Estatuto do contrato (E2, E15):** as obrigações do capítulo fixadas no
manual (MATH3us.md §3, Cap. 7, e emenda E11 — construção de ℂ, forma polar,
rotação-escala, raízes n-ésimas, argumento multivalorado e escolha de ramo,
ℤ[i], soma de dois quadrados; exponencial em porta fechada) têm estatuto de
**contrato editorial**, não de conjectura pré-registrada. O que se
pré-registra abaixo, com força plena, são as conjecturas *além* do contrato —
apostas que o desenvolvimento e o oráculo podem confirmar ou destruir.

**Restrição E11 (aceita como lei do capítulo):** a notação e^{iθ} aparecerá
exclusivamente em caixa de porta fechada; o operador de rotação será
cos θ + i·sen θ com estatuto geométrico; o logaritmo complexo, se mencionado,
apenas como relação formal adiada. Nenhuma conjectura abaixo depende da
exponencial.

---

## Pergunta central (registrada antes do desenvolvimento)

> A raiz quadrada devolve **um** número — ou eu sempre acreditei nisso porque
> só extraí raízes de números positivos? Se existir um plano onde todo número
> tem raiz, quantas raízes ele devolve — e o que acontece com a porta que o
> Capítulo 2 deixou trancada: **quais primos são soma de dois quadrados?**

Contexto: o Capítulo 2 provou a metade barata (hipotenusas primitivas são
u² + v² e satisfazem ≡ 1 mod 4) e trancou a porta da volta, apontando para
ℤ[i]. A falha prevista pelo manual para este capítulo é **presumir que toda
operação inversa devolve um único valor** — e a aposta editorial de E11 é que
as raízes n-ésimas destroem essa presunção sem precisar de exponencial
nenhuma.

---

## Conjecturas (prospectivas, com força plena)

### C1 — Unicidade da decomposição em dois quadrados para primos
**Enunciado:** todo primo p ≡ 1 (mod 4) escreve-se como a² + b² com
0 < a < b de **exatamente uma** maneira (unicidade além da existência que o
contrato exige provar). Para compostos a unicidade falha em geral.
**Confiança inicial:** média. A existência é o teorema de Fermat; a
unicidade é aposta minha — não estava na porta do Cap. 2.
**Exemplos disponíveis (verificados em 28/07/2026, Python exato):**
5 = 1²+2² (única); 13 = 2²+3²; 17 = 1²+4²; 29 = 2²+5²; 997 = 6²+31² —
uma decomposição cada. Composto 65 = 1²+8² = 4²+7² tem duas: a unicidade é
mesmo privilégio dos primos, se sobreviver.
**Refutadores possíveis:** um único primo p ≡ 1 (mod 4) no domínio do
oráculo (p < 50000, exaustivo) com duas decomposições distintas, ou com
nenhuma.

### C2 — O fatorial-testemunha fabrica a decomposição
**Enunciado:** para p ≡ 1 (mod 4), a testemunha de Wilson
m = ((p−1)/2)! mod p satisfaz m² ≡ −1 (mod p), e o mdc gaussiano
mdc(m + i, p), computado pelo algoritmo de Euclides em ℤ[i] com divisão por
arredondamento, é um inteiro gaussiano a + bi com a² + b² = p — ou seja, a
**prova** (Wilson → resíduo quadrático → fator gaussiano) é também um
**algoritmo** que devolve a decomposição.
**Confiança inicial:** média-alta para m² ≡ −1; média para o mdc devolver
exatamente norma p (o algoritmo poderia devolver uma unidade se p
continuasse primo em ℤ[i] — a conjectura aposta que não continua).
**Exemplos disponíveis (verificados em 28/07/2026):** p = 5: m = 2,
m² ≡ 4 ≡ −1; mdc(2+i, 5) = 2+i, norma 5 ✓. p = 13: mdc = −2−3i, norma 13 ✓.
p = 997: mdc de norma 997 ✓. p = 4001: mdc de norma 4001 ✓.
**Refutadores possíveis:** primo p ≡ 1 (mod 4) com m² ≢ −1 (mod p); ou
mdc(m + i, p) com norma 1 ou p² no domínio amostrado do oráculo.

### C3 — A soma das n raízes é zero
**Enunciado:** para todo w ≠ 0 e todo n ≥ 2, as n raízes n-ésimas de w
somam **exatamente zero** (o centro do polígono regular é a origem, e o
"peso" das raízes se cancela).
**Confiança inicial:** alta — mas note que ela obriga as raízes a serem
exatamente n e igualmente espaçadas, o que ainda não está provado.
**Exemplos disponíveis (verificados em 28/07/2026, float):** raízes quartas
de 1, quintas de 2+3i, sétimas de 0,5−2i — somas com módulo < 10⁻¹⁴.
**Refutadores possíveis:** um par (w, n) com soma numericamente estável
longe de zero; ou uma prova de que a soma depende de w.

### C4 — O critério da norma para primos gaussianos "de verdade"
**Enunciado:** um inteiro gaussiano a + bi com a &gt; 0 e b &gt; 0 (fora dos
eixos) é primo em ℤ[i] **se e somente se** sua norma a² + b² é um primo
racional. (Nos eixos a regra é outra: 3 é primo gaussiano com norma 9
composta — a conjectura é sobre o interior do reticulado.)
**Confiança inicial:** média-alta.
**Exemplos disponíveis (verificados em 28/07/2026, busca bruta de divisores
até norma 400):** critério e irredutibilidade bruta coincidem em todos os
a, b ∈ {1, …, 14} — zero divergências.
**Refutadores possíveis:** a + bi fora dos eixos, irredutível por busca
exaustiva de divisores, com norma composta; ou redutível com norma prima.

### C5 — O custo exato do ramo
**Enunciado:** com Arg escolhido em (−π, π], o defeito
Arg(zw) − Arg z − Arg w pertence sempre a {−2π, 0, +2π} — a escolha de ramo
não erra por qualquer valor: erra por um múltiplo inteiro de volta, e no
produto de dois fatores a correção nunca passa de uma volta.
**Confiança inicial:** alta.
**Exemplos disponíveis:** z = w = −1 + 0,1i: Arg z + Arg w ≈ 6,08 > π, e
Arg(zw) ≈ 6,08 − 2π. z = w = 1: defeito 0.
**Refutadores possíveis:** par (z, w) com defeito fora do conjunto
{−2π, 0, 2π} (amostragem ampla do oráculo, incluindo pares colados no corte).

---

## Condições gerais de refutação

Qualquer contraexemplo numérico reproduzível pelo oráculo do capítulo, ou
falha lógica apontada nas demonstrações, obriga autópsia nos termos da §1.3 —
a conjectura ferida permanece no registro, com as cinco perguntas
respondidas. Se uma obrigação do **contrato** se revelar falsa, aplica-se
E15: refutação no capítulo e proposta de emenda via sessão-coordenadora.

## O que este pré-registro não é

Não é reivindicação de prioridade. Tudo o que está acima é matemática
clássica consolidada (Fermat, Euler, Gauss, Wilson); a força probatória do
pré-registro aqui é sobre a **honestidade do processo** — estas apostas
foram escritas antes do desenvolvimento e serão julgadas pelo oráculo — e
não sobre novidade matemática. `sources.md` registrará os materiais
clássicos; a ausência de sítio pessoal é o próprio registro (§1.2:
assimetria declarada).
