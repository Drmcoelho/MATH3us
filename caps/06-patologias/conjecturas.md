# Capítulo 6 — As Patologias · Pré-registro de conjecturas

**Tipo declarado:** território virgem.
**Data do pré-registro:** 28/07/2026.
**Estatuto (§1.3, E2):** para território virgem, o pré-registro tem **força
probatória plena** — não existe sítio arqueológico a minerar. A assimetria
exigida pela §1.2 fica declarada sem disfarce: o conteúdo clássico deste
capítulo (Dirichlet, Thomae, Takagi, TVI, completude de ℝ) **não** provém de
redescoberta pessoal. Não haverá narrativa falsa de descoberta; `sources.md`
registra os materiais clássicos e a ausência — que é o registro honesto — de
qualquer sítio pessoal.

**Estatuto do contrato (E15):** as obrigações de cobertura fixadas no manual
(MATH3us.md §3, Capítulo 6: descontinuidade total de Dirichlet; continuidade
de Thomae exatamente nos irracionais; contínua em toda parte e diferenciável
em nenhuma; TVI a partir do princípio do supremo; densidade sem completude
em ℚ) são **contrato editorial**, não conjectura: são teoremas clássicos
conhecidos, e fingir risco sobre eles seria desonestidade. O que se
pré-registra abaixo, com força plena, é o que o contrato **não** fixa: as
conjecturas quantitativas sobre o que a camada de observação (§2.1) vai
mostrar e esconder quando essas funções forem postas na tela.

**Proveniência declarada (E12):** em 28/07/2026, durante o planejamento desta
sessão, foi executada verificação **exploratória não canônica** (Python,
implementação única, sem artefato versionado) dos itens marcados abaixo com
[E]. Ela informa confiança de trabalho e é declarada — não apagada; o oráculo
canônico do capítulo re-executa tudo com implementações independentes,
artefatos em `audit/` e hash de commit. As conjecturas C1b e C5 **não**
receberam verificação exploratória de espécie alguma: são apostas genuínas.

---

## Pergunta central (registrada antes do desenvolvimento)

> Quanto do que "se vê" num gráfico sobrevive à formalização? Mais
> precisamente: existe função cujo gráfico computacional oculte **exatamente
> a propriedade investigada** — e, se existe, o que resta da frase
> "dá para ver"?

Contexto: o Capítulo 1 mostrou os olhos desistindo antes dos números (a
convergência visual em n ≈ 48, dezenas de linhas antes da tabela). A falha
prevista pelo manual para este capítulo é a confiança excessiva na imagem e
na intuição de regularidade. Este capítulo existe para destruir proposições
visualmente plausíveis — com teoremas, não com retórica.

---

## Conjecturas (prospectivas, além do contrato)

### C1 — A cegueira float: o traçador honesto de Dirichlet desenha UMA reta
**Enunciado:** amostrando a função de Dirichlet (indicadora de ℚ) em
qualquer conjunto de valores IEEE-754 de precisão dupla — em qualquer
resolução, janela ou zoom — 100% das amostras retornam 1, porque todo float
finito é um racional p/2^k. O gráfico computacional honesto é **uma** reta
na altura 1; a figura folclórica de "duas retas" já é uma idealização que
máquina nenhuma produz por amostragem.
**Confiança inicial:** alta (o argumento é estrutural). [E: não executada
como varredura; a estrutura p/2^k é conhecimento prévio.]
**Exemplos disponíveis:** 0,5 = 1/2; 0,1 em float é 3602879701896397/2^55 —
racional, apesar do nome.
**Refutadores possíveis:** um único float finito x com D(x) = 0, isto é, um
float irracional exibido pelo oráculo.

### C1b — E nenhuma janela escapa
**Enunciado:** no traçador do capítulo, para **todas** as janelas testadas
(centro √2/2, larguras 2⁰ a 2⁻²⁰, 640 colunas de pixel), toda coluna de
pixel conterá simultaneamente um racional e um irracional do objeto — de
modo que o gráfico *idealizado* de Dirichlet pinta as duas retas inteiras em
toda resolução, enquanto o gráfico *amostrado* pinta uma só. As duas imagens
discordam em toda janela; nenhuma das duas é o objeto.
**Confiança inicial:** alta (densidades de ℚ e de ℝ∖ℚ, a provar no
capítulo). **Sem verificação exploratória.**
**Refutadores possíveis:** uma coluna de pixel (um intervalo de largura
> 0) sem racional ou sem irracional — o que refutaria a densidade provada,
não apenas a conjectura.

### C2 — A contagem dos visíveis de Thomae (conjectura de calibração, arriscada)
**Enunciado:** os pontos do gráfico de Thomae com altura ≥ 1/Q em [0, 1]
são as frações reduzidas p/q com q ≤ Q; sua contagem Φ(Q) = Σ_{q≤Q} φ(q)
satisfaz **|Φ(1000)/(3·1000²/π²) − 1| < 1%**, e — parte igualmente
arriscada — em Q = 10 o desvio é **maior que 3%**: a assintótica clássica
ainda não governa a primeira década. Consequência visual: dobrar a precisão
vertical (Q → 2Q) quadruplica os pontos visíveis, mas os pontos de
continuidade (irracionais, altura 0) permanecem 0% dos pixels acesos em
todo Q.
**Confiança inicial:** média-alta. [E: executada — Φ(1000) = 304192 contra
303963,55 (desvio ≈ 0,075%); Φ(10) = 32 contra 30,396 (desvio ≈ 5,3%);
o oráculo canônico re-verifica com peneira de totientes E contagem direta
por gcd, independentes.]
**Refutadores possíveis:** contagem exata fora de qualquer uma das duas
margens.

### C3 — O declive diádico de Takagi em 0 diverge linearmente
**Enunciado:** para a função de Takagi T(x) = Σ_{k≥0} s(2^k x)/2^k, com
s = distância ao inteiro mais próximo, o quociente de diferenças sobre o
passo diádico h = 2⁻^m em x = 0 vale **exatamente m**:
[T(2⁻^m) − T(0)]/2⁻^m = m, para todo m ≥ 1. Divergência linear, prevista e
exata — não "cresce sem cota" genérico: cresce **como m**.
**Confiança inicial:** alta. [E: executada para m ≤ 20 em aritmética exata
de frações; o oráculo canônico verifica por duas rotas independentes —
avaliação direta da soma parcial exata e fórmula combinatória dos ±1.]
**Refutadores possíveis:** um único m com quociente ≠ m em aritmética
exata.

### C4 — A rugosidade não se dilui: as metades diferem por exatamente 2
**Enunciado:** em **qualquer** intervalo diádico [j/2^m, (j+1)/2^m], os
declives de T sobre as duas metades do intervalo diferem por exatamente 2
(o filho esquerdo ganha +1, o direito −1, sobre o declive do pai). Logo o
zoom nunca encontra escala em que T se alise — enquanto a soma parcial T_N
é **linear por partes** em cada intervalo diádico de comprimento 2⁻^N, e
portanto, sob zoom mais fundo que 2⁻^N, parece (e É, enquanto soma parcial)
um segmento de reta. O gráfico da soma parcial mente sobre T precisamente
na propriedade investigada: a rugosidade.
**Confiança inicial:** alta. [E: não executada como varredura; decorre da
estrutura binária de s, a provar no capítulo.]
**Refutadores possíveis:** um intervalo diádico cujas metades tenham
declives com diferença ≠ 2, em aritmética exata.

### C5 — Os bits de √2/2 como passeio quase equilibrado (aposta genuína)
**Enunciado:** tomando x* = float(√2/2) = 6369051672525773/2⁵³ (o racional
que a máquina realmente segura quando se digita √2/2) e S_m = soma dos ±1
dos m primeiros bits binários de x*, a sequência S_1, …, S_52 muda de sinal
pelo menos 3 vezes e satisfaz max |S_m| ≤ 12. Em palavras: os bits da
mantissa se comportam como passeio aleatório quase equilibrado — o declive
diádico de T em x* oscila sem convergir, em vez de divergir como em 0.
**Confiança inicial:** média (√(52) ≈ 7,2 é a escala esperada de um passeio
justo; 12 dá folga, mas bits de constantes não devem lealdade a passeios).
**Sem verificação exploratória de qualquer espécie — este número não foi
computado antes deste registro.**
**Refutadores possíveis:** menos de 3 mudanças de sinal, ou algum
|S_m| > 12, no oráculo canônico.

---

## Condições gerais de refutação

Qualquer contraexemplo numérico reproduzível pelo oráculo do capítulo, ou
falha lógica apontada nas demonstrações, obriga autópsia nos termos da §1.3
— a conjectura ferida permanece no registro, com as cinco perguntas
respondidas em apêndice a este arquivo (nunca por edição do registro acima).
Se uma obrigação do **contrato** se revelar falsa ou mal formulada,
aplica-se E15: refutação no capítulo e proposta de emenda ao manual via
sessão-coordenadora.

## O que este pré-registro não é

Não é reivindicação de prioridade nem de descoberta. Dirichlet (1829),
Thomae (1875), Weierstrass (1872), Takagi (1901) e van der Waerden (1930)
chegaram muito antes; o TVI é de Bolzano (1817) e Cauchy; a incompletude de
ℚ é socrática. O capítulo importa esse conhecimento declaradamente e o
demonstra ou cita item a item (`claims.yml`). A única coisa nova que este
registro protege é a honestidade do experimento: o que foi previsto sobre a
tela, antes de a tela existir.
