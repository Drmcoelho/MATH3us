# Capítulo 2 — As Ternas do Ímpar · Pré-registro de conjecturas

**Tipo declarado:** escavação.
**Data do pré-registro:** 28/07/2026.
**Estatuto (§1.3, E2):** este é o registro *prospectivo* do desenvolvimento do
capítulo. O sítio arqueológico — o contato anterior do autor com 3-4-5,
5-12-13, 7-24-25 e a intuição de que "todo ímpar gera uma terna" — **ainda
não foi minerado**: nenhum fragmento verbatim foi localizado ou commitado até
esta data, e `sources.md` registrará o estado documental. Lacunas documentais
não serão preenchidas com memória apresentada como fato.

**Estatuto do contrato (E2, E15):** os sete itens do contrato editorial do
capítulo (MATH3us.md §3 — direta, recíproca e classificação, primitividade,
estrutura modular, medidas, raios, leitura euclidiana) têm estatuto de
**contrato editorial**, não de conjectura pré-registrada. Reivindicar
anterioridade probatória sobre eles seria a primeira desonestidade do
projeto. O que se pré-registra abaixo, com força probatória plena, são as
conjecturas *novas* — surgidas ao planejar o desenvolvimento e que o contrato
não fixa.

**Proveniência declarada (E12):** em 28/07/2026 foi executada uma verificação
**exploratória não canônica** dos itens do contrato (ímpares n ∈ {3, …, 20001},
Python, implementação única, sem artefato versionado, sem pares adversariais).
Ela foi rebaixada pelo manual e informa apenas confiança de trabalho. O
**oráculo canônico** — script próprio, hash de commit, domínio declarado,
pares adversariais recusados, relatório em `audit/` — é o que este capítulo
executa agora, como o manual prometeu na abertura do diretório.

---

## Pergunta central (registrada antes do desenvolvimento)

> Todo ímpar gera uma terna — mas gera **a** terna? A regra que fabrica
> 3-4-5, 5-12-13, 7-24-25 produz exemplos ou **classifica** um fenômeno?
> O que exatamente a consecutividade de cateto e hipotenusa força?

Contexto: as três ternas do sítio têm o cateto maior e a hipotenusa
consecutivos, e 4+5 = 9 = 3², 12+13 = 25 = 5², 24+25 = 49 = 7². A falha
prevista pelo manual é reconhecer o padrão sem provar universalidade,
unicidade ou primitividade — este capítulo existe para não cometê-la.

---

## Conjecturas (prospectivas, além do contrato)

### C1 — Coprimalidade dois a dois
**Enunciado:** na família (n, L, R) com L = (n²−1)/2 e R = (n²+1)/2, os três
lados são coprimos **dois a dois** — não apenas gcd(n, L) = 1 (que o contrato
exige), mas também gcd(n, R) = 1 e gcd(L, R) = 1.
**Confiança inicial:** alta.
**Exemplos disponíveis:** (3,4,5), (5,12,13), (7,24,25) — dois a dois coprimos.
**Justificativa intuitiva:** R − L = 1 já força gcd(L, R) = 1; e um divisor
comum de n e um dos outros dois deveria dividir combinações que colapsam em 1.
**Refutadores possíveis:** qualquer n ímpar ≥ 3 com gcd(n, R) > 1 ou
gcd(L, R) > 1 no domínio do oráculo.

### C2 — A parábola discreta: segundas diferenças constantes
**Enunciado:** sobre os ímpares consecutivos n, n+2, os saltos de L obedecem
L(n+2) − L(n) = 2n + 2; portanto as **segundas diferenças** de L (e de R) ao
longo dos ímpares são constantes e iguais a 4 — a assinatura aritmética de uma
parábola, visível antes de qualquer gráfico.
**Confiança inicial:** alta.
**Exemplos disponíveis:** L = 4, 12, 24, 40 → primeiras diferenças 8, 12, 16 →
segundas diferenças 4, 4.
**Refutadores possíveis:** um único par de ímpares consecutivos com segunda
diferença ≠ 4.

### C3 — A família espelho da diferença 2
**Enunciado:** as ternas em que hipotenusa e cateto maior diferem de **2**
formam família análoga gerada pelos pares: (2m, m²−1, m²+1), m ≥ 2; e essa
família é primitiva **se e somente se m é par**.
**Confiança inicial:** média-alta.
**Exemplos disponíveis:** m = 2 → (4,3,5) primitiva; m = 3 → (6,8,10) não
primitiva; m = 4 → (8,15,17) primitiva.
**Justificativa intuitiva:** a consecutividade (folga 1) força primitividade;
folga 2 deveria deixar exatamente um fator 2 de sobra quando m é ímpar.
**Refutadores possíveis:** m par com terna não primitiva; m ímpar com terna
primitiva; terna de folga 2 fora da forma (2m, m²−1, m²+1).

### C4 — A área é múltipla de 6
**Enunciado:** K = n(n²−1)/4 é sempre divisível por **6** — mais forte que o
"inteiro e par" do contrato.
**Confiança inicial:** alta.
**Exemplos disponíveis:** K = 6, 30, 84, 180 — todos múltiplos de 6.
**Justificativa intuitiva:** (n−1)·n·(n+1) é produto de três consecutivos,
logo múltiplo de 3; a paridade já dá o resto.
**Refutadores possíveis:** qualquer n ímpar ≥ 3 com K mod 6 ≠ 0.

### C5 — O ex-raio da hipotenusa é o semiperímetro
**Enunciado:** na família, o ex-raio oposto à hipotenusa vale exatamente s
(r_R = s) e o ex-raio oposto ao cateto L vale s − n; e a primeira identidade
não é privilégio da família — vale para **todo** triângulo retângulo.
**Confiança inicial:** alta para a família; média-alta para a generalização.
**Exemplos disponíveis:** n = 3: K = 6, s = 6, s − R = 1, K/(s−R) = 6 = s.
**Justificativa intuitiva:** r = s − R no triângulo retângulo (comprimento de
tangência do ângulo reto); K = r·s então fecha K = s·(s−R), que é a identidade.
**Refutadores possíveis:** um triângulo retângulo inteiro (gerado por Euclides
com u > v ≥ 1 quaisquer) em que K ≠ s·(s − hipotenusa).

---

## Condições gerais de refutação

Qualquer contraexemplo numérico reproduzível pelo oráculo do capítulo, ou
falha lógica apontada nas demonstrações, obriga autópsia nos termos da §1.3 —
a conjectura ferida permanece no registro. Se um item do **contrato** se
revelar falso, aplica-se E15: refutação no capítulo e proposta de emenda ao
manual via sessão-coordenadora.

## O que este pré-registro não é

Não é reivindicação de prioridade. A parametrização de Euclides é clássica
(Elementos, lema de X.28–29); a família do ímpar é redescoberta pessoal de
resultado conhecido; a síntese organizacional dos consecutivos (n±1)/2 —
parâmetros de Euclides, inraio e ex-raio — entrará no ledger como
`kind: synthesis`, `provenance: authorial`, com a nota obrigatória:
*Síntese autoral no âmbito deste tratado; prioridade histórica não
estabelecida.*
