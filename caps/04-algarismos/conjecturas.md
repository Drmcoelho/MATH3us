# Capítulo 4 — Os Algarismos Repetidos · Pré-registro de conjecturas

**Tipo declarado:** escavação.
**Data do pré-registro:** 28/07/2026.
**Sítio:** 8, 80, 44, 0,142857̄ — o fascínio antigo pelos algarismos que se
repetem: nos números "redondos" e espelhados, e na dízima do sete.
**Estatuto (§1.3, E2):** o sítio **ainda não foi minerado**. Nenhum
fragmento verbatim, anotação ou conversa original foi localizado ou
commitado até esta data; `sources.md` registra a lacuna. Ela **não** será
preenchida com memória apresentada como fato. O conteúdo matemático fixado
no MATH3us.md §3 para este capítulo (o critério d | b^k, as consequências
por base, o sete como caso de estudo) tem estatuto de **contrato
editorial**, não de conjectura pré-registrada — reivindicar anterioridade
probatória para ele seria desonesto. As conjecturas abaixo referem-se ao
desenvolvimento que o capítulo fará a partir de agora; para elas o
pré-registro vale com força probatória plena.

---

## Pergunta central (registrada antes do desenvolvimento)

> Por que 1/7 vira 0,142857142857… — para sempre — enquanto 1/8 acaba em
> três casas? A culpa é do sete, do dez, ou da nossa maneira de escrever?
> E existe base em que **nenhuma** fração precise repetir algarismos?

Contexto: a fascinação original do sítio era por algarismos repetidos como
*aparência* (8, 80, 44; depois a dízima do sete). A obrigação do capítulo
(contrato §3) é substituir a aparência pela teoria que a torna inevitável:
valor posicional → congruências → critério de terminação → ordem
multiplicativa → primos full-reptend.

---

## Conjecturas

Exemplos citados abaixo foram computados em 28/07/2026 (python3, divisão
longa e ordem multiplicativa, execução exploratória pré-desenvolvimento;
o oráculo canônico com artefatos virá com o capítulo, E12).

### C1 — O critério de terminação é uma equivalência completa
**Enunciado:** para a/d **reduzida** (gcd(a,d) = 1, d ≥ 1) e base inteira
b ≥ 2: a expansão de a/d na base b é finita ⟺ existe k ∈ ℕ com d | b^k ⟺
todo fator primo de d divide b. As três condições são equivalentes e a
prova das duas direções cabe no aparato do capítulo (valor posicional +
fatoração única).
**Confiança inicial:** alta (é o contrato editorial; a conjectura própria
está na forma: *ambas* as direções saem sem teoria além do TFA).
**Exemplos disponíveis:** 1/8 = 0,125 (8 | 10³); 7/40 = 0,175; 1/7
infinita na base 10; 1/6 na base 12 = 0,2 (finita: 6 | 12).
**Refutadores possíveis:** uma fração reduzida com d contendo primo p ∤ b
e expansão finita; ou d | b^k com expansão infinita; ou uma lacuna na
prova da recíproca que exija teoria fora do capítulo.

### C2 — A hipótese de redução carrega peso real
**Enunciado:** sem a hipótese gcd(a,d) = 1 o critério é falso como teste
sobre d: 3/6 tem expansão finita na base 10 (= 0,5) embora 6 tenha o fator
3 ∤ 10; e 2/6 tem expansão infinita (= 1/3 = 0,3̄). O mesmo denominador 6
produz os dois comportamentos — logo qualquer enunciado honesto do
critério fala da fração **reduzida**, e a expansão só depende do valor
a/d, não do par (a, d).
**Confiança inicial:** alta.
**Refutadores possíveis:** nenhum caso em que denominadores não reduzidos
divirjam do comportamento da forma reduzida (aí a hipótese seria
decorativa, não estrutural — o que refutaria a *necessidade* alegada).

### C3 — Período = ordem multiplicativa (caso coprimo)
**Enunciado:** se gcd(d, b) = 1 e d > 1, a expansão de a/d na base b é
puramente periódica (pré-período zero) e o comprimento do período mínimo é
exatamente ord_d(b) — a ordem multiplicativa de b módulo d — **para todo**
a com gcd(a, d) = 1, independentemente de a.
**Confiança inicial:** alta.
**Exemplos disponíveis:** 1/7 base 10: período 6 = ord₇(10); 1/13 base 10:
período 6 = ord₁₃(10); 1/17: período 16 = ord₁₇(10); 1/7 base 16: período
3 = ord₇(16); 1/7 base 60: período 3 = ord₇(60); 1/3 base 2: período 2 =
ord₃(2).
**Refutadores possíveis:** fração coprima com pré-período não nulo; ou
período mínimo ≠ ord_d(b) para algum a coprimo (por exemplo, período
dependendo de a).

### C4 — A cisão d = d_b · d′ decide tudo no caso geral
**Enunciado:** escreva d = d_b · d′, onde d_b agrega os fatores primos de
d que dividem b e gcd(d′, b) = 1. Então, para a/d reduzida: o pré-período
mínimo é ν = max_p ⌈v_p(d)/v_p(b)⌉ sobre os primos p | d_b (o menor k com
d_b | b^k), e o período mínimo é ord_{d′}(b) (com a convenção período 0
quando d′ = 1). Ambos independem de a.
**Confiança inicial:** média-alta — a fórmula do pré-período via valuações
é a parte que o autor menos vezes viu enunciada com prova completa; é onde
uma surpresa poderia morar.
**Exemplos disponíveis:** 1/12 base 10 (d_b = 4, d′ = 3): pré 2, período
1 → 0,083̄; 5/12 idem (0,416̄); 1/60 base 10 (d_b = 20, d′ = 3): pré 2,
período 1; 1/10 base 2 (d_b = 2, d′ = 5): pré 1, período 4; 1/22 base 10:
pré 1, período 2 = ord₁₁(10).
**Refutadores possíveis:** pré-período observado ≠ ν para alguma fração
reduzida; período do caso geral ≠ ord_{d′}(b); dependência em a.

### C5 — As permutações cíclicas de 142857 são estruturais, não numerológicas
**Enunciado:** o fato de 142857·{1,…,6} percorrer exatamente as rotações
cíclicas de 142857 é consequência estrutural de 7 ser full-reptend na base
10 (ord₇(10) = 6 = 7 − 1): o ciclo de restos da divisão longa visita
**todos** os resíduos 1,…,6, logo começar a divisão em m/7 é entrar no
mesmo ciclo em outro ponto. Previsão geral: para todo primo p full-reptend
na base b, os múltiplos m·(b^{p−1} − 1)/p, m = 1,…,p−1, são precisamente
as rotações cíclicas do bloco fundamental de p na base b.
**Confiança inicial:** média-alta.
**Exemplos disponíveis:** p = 7, b = 10: {142857, 285714, 428571, 571428,
714285, 857142} = rotações de 142857 (verificado 28/07/2026); 999999/7 =
142857 exato.
**Refutadores possíveis:** um primo full-reptend cujo bloco fundamental
tenha múltiplo que não seja rotação; múltiplos repetindo rotação (colisão)
em vez de esgotá-las.

### C6 — A patologia é do numeral, nunca do número
**Enunciado:** todo comportamento deste capítulo (terminar, repetir,
comprimento do período) é propriedade do **par** (número, base) — um
artefato representacional no sentido da §2.3 — e nunca do número sozinho:
para toda fração a/d existe base b em que a expansão é finita (por
exemplo, b = d, ou qualquer múltiplo de d), e para toda base b existem
infinitas frações de expansão infinita (os inversos dos infinitos primos
p ∤ b, via Euclides). Em particular 1/7 = 0,1 exata na base 7.
**Confiança inicial:** alta.
**Refutadores possíveis:** uma fração sem base finita alguma que a
termine; ou uma base finita que termine todas as frações (exigiria base
divisível por todos os primos — impossível se há infinitos).

---

## Condições gerais de refutação

Qualquer contraexemplo numérico reprodutível no experimento do capítulo ou
no oráculo, ou falha lógica apontada nas demonstrações, obriga autópsia
nos termos da §1.3 — a conjectura ferida permanece no registro, datada.

## O que este pré-registro não é

Não é reivindicação de prioridade: C1, C3 e C4 são teoria clássica
(critério de terminação; período como ordem multiplicativa; cisão
pré-período/período), cuja *escavação* — o caminho do fascínio pelos
algarismos até a teoria — é o objeto do capítulo. C5 é consequência
conhecida da teoria dos primos full-reptend. A tipagem no `claims.yml`
seguirá §1.4: proveniência `classical` onde couber; síntese apenas onde
for síntese; nenhuma identidade será chamada de inédita por ter sido
encontrada sem consulta.
