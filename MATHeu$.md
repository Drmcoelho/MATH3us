# MATHeu$.md — Constituição do Braço Geométrico-Experimental

> **A matemática entra pelos olhos, é interrogada pelas mãos e só sai pela prova.**  
> Leitor primário: Matheus M. Coelho. Autor: o mesmo. Testemunha: o artefato renderizado.

---

## 0. Identidade

- **Nome do braço:** `MATHeu$`.
- **Nome público do artefato inicial:** *O Triângulo que Exaure o Círculo*.
- **Relação com MATH3us:** braço alternativo e adversarial. Não corrige silenciosamente o outro; demonstra, por implementação concorrente, como o mesmo sítio pode ser reconstruído com maior densidade geométrica, visual e didática.
- **Símbolo `$`:** não representa dinheiro. É o sinal de que o projeto deve entregar valor observável: figura que explica, cálculo que responde, exercício que testa, prova que fecha.
- **Unidade de entrega:** um laboratório-capítulo autocontido, visto no navegador real, com matemática, visualização, boxes, exercícios e auditoria semântica.
- **Formato canônico:** HTML único, sem CDN, sem dependência remota, baseado prioritariamente em SVG vetorial acessível. Canvas só entra quando oferecer vantagem real e após teste específico em Safari/iOS.

---

## 1. Tese editorial

O primeiro braço reduziu o método de exaustão a duas sequências de semiperímetros. `MATHeu$` parte de uma tese mais forte:

> **O método de exaustão não é uma tabela que converge. É uma máquina geométrica composta por um triângulo retângulo fundamental, dois cercos, quatro erros e uma cadeia de identidades que o leitor pode manipular.**

A página não deverá apenas dizer que os polígonos convergem. Deverá permitir ao leitor ver, medir, comparar e provar:

1. o triângulo retângulo `R–r–L/2`;
2. a passagem do triângulo para o polígono;
3. o polígono inscrito e o circunscrito como duas normalizações do mesmo triângulo;
4. a evolução dos semiperímetros;
5. a evolução das áreas;
6. a diferença entre erro interno e externo;
7. a diferença entre erro de perímetro e erro de área;
8. a ordem quadrática de convergência em relação ao número de lados;
9. a razão assintótica de contração `1/4`;
10. o ponto exato em que observação, inferência e prova deixam de ser a mesma coisa.

---

## 2. Critério de inclusão

Uma seção entra quando cumpre ao menos uma destas funções:

- expõe um objeto geométrico que gera uma fórmula;
- transforma uma fórmula em experiência manipulável;
- separa duas grandezas que poderiam ser confundidas;
- fornece um exercício que detecta falsa compreensão;
- produz uma prova, uma recíproca ou um limite;
- mostra um erro de representação ou de implementação;
- conecta uma etapa ao capítulo posterior.

Curiosidade sem função vira nota lateral. Derivação central nunca vira nota lateral.

---

## 3. Objeto central: o triângulo fundamental

Para um polígono regular de lado `L`, raio circunscrito `R` e apótema `r`, o centro `O`, o ponto médio `M` de um lado e um vértice `V` formam um triângulo retângulo:

\[
OV=R,\qquad OM=r,\qquad MV=\frac L2,
\]

\[
\boxed{R^2=r^2+\left(\frac L2\right)^2}.
\]

Esse triângulo é o átomo do capítulo. Toda visualização poligonal deve poder ser retraída a ele; toda fórmula de perímetro ou área deve poder ser reconstruída a partir dele.

### 3.1 Normalização inscrita

No círculo unitário:

\[
R=1,\qquad r=\cos\theta,\qquad \frac L2=\sin\theta,
\qquad \theta=\frac{\pi}{n}.
\]

### 3.2 Normalização circunscrita

No mesmo círculo:

\[
r=1,\qquad R=\sec\theta,\qquad \frac L2=\tan\theta.
\]

A página deverá mostrar os dois triângulos lado a lado e permitir alternar entre valores absolutos, razões normalizadas e diferenças em relação à unidade.

---

## 4. Contrato matemático do laboratório inicial

Definem-se os semiperímetros do círculo unitário:

\[
a_n=n\sin\left(\frac{\pi}{n}\right),
\qquad
b_n=n\tan\left(\frac{\pi}{n}\right).
\]

E as áreas dos polígonos inscrito e circunscrito:

\[
A_n^- = n\sin\theta\cos\theta,
\qquad
A_n^+ = n\tan\theta.
\]

O laboratório deverá tornar visíveis e demonstráveis as identidades:

\[
\boxed{A_n^- = \frac{a_n^2}{b_n}},
\qquad
\boxed{A_n^+ = b_n},
\]

\[
\boxed{A_{2n}^- = a_n},
\]

\[
\boxed{
A_n^- < A_{2n}^- = a_n < \pi < b_{2n}=A_{2n}^+ < A_n^+
}.
\]

A diferença das áreas é:

\[
\Delta A_n=A_n^+-A_n^-
=\frac{(b_n-a_n)(b_n+a_n)}{b_n}.
\]

Logo:

\[
\frac{\Delta A_n}{b_n-a_n}\longrightarrow 2.
\]

As assíntotas a serem distinguidas são:

\[
\pi-a_n\sim\frac{\pi^3}{6n^2},
\qquad
b_n-\pi\sim\frac{\pi^3}{3n^2},
\]

\[
\pi-A_n^-\sim\frac{2\pi^3}{3n^2},
\qquad
A_n^+-\pi\sim\frac{\pi^3}{3n^2},
\]

\[
\boxed{b_n-a_n\sim\frac{\pi^3}{2n^2}},
\qquad
\boxed{A_n^+-A_n^-\sim\frac{\pi^3}{n^2}}.
\]

O fator `2` não pode migrar clandestinamente de uma grandeza para outra.

---

## 5. Arquitetura da página

### 5.1 Abertura

A página abre com o triângulo fundamental, não com três contornos sobrepostos. O leitor primeiro reconhece `R`, `r` e `L/2`; depois vê a repetição radial que cria o polígono.

### 5.2 Laboratório I — triângulo

Controles:

- número de lados `n`;
- alternância inscrito/circunscrito/ambos;
- exibição de medidas absolutas ou normalizadas;
- marcação de ângulo reto e semiângulo central;
- botão “mostrar Pitágoras”.

Saídas:

- desenho SVG vetorial;
- valores de `R`, `r`, `L/2`, `L`, `θ`;
- verificação numérica de `R² = r² + (L/2)²`;
- área do triângulo e contribuição para a área poligonal.

### 5.3 Laboratório II — dois cercos

A vista geral deve mostrar inequivocamente:

- círculo;
- vértices do inscrito sobre o círculo;
- pontos de tangência do circunscrito;
- raio normal escolhido;
- uma cunha destacada que corresponde ao triângulo fundamental.

A lupa não será uma câmera cega. Será uma **vista local normalizada**, construída diretamente a partir das três distâncias radiais relevantes. Todos os traços permanecem em campo em qualquer estado permitido.

### 5.4 Laboratório III — perímetros e áreas

O leitor poderá alternar entre:

- semiperímetros `aₙ`, `π`, `bₙ`;
- áreas `Aₙ⁻`, `π`, `Aₙ⁺`;
- erros absolutos;
- erros multiplicados por `n²`;
- diferenças totais;
- razões de contração na duplicação.

Cada gráfico deve ter:

- legenda direta;
- tabela equivalente;
- descrição textual do estado;
- escala automática;
- destaque do valor selecionado;
- zero dependência exclusiva de cor.

### 5.5 Laboratório IV — cadeia de identidades

Uma sequência visual conecta:

\[
\text{triângulo}
\rightarrow
\text{lado}
\rightarrow
\text{perímetro}
\rightarrow
\text{área}
\rightarrow
\text{erro}
\rightarrow
\text{limite}.
\]

Nenhuma fórmula central aparece sem que o objeto de onde ela vem esteja disponível na tela.

---

## 6. Sistema de boxes

Os boxes não são decoração. Cada tipo possui função epistemológica e aparência estável.

### BOX — Intuição

Registra a pergunta ou o padrão antes da prova.

### BOX — Traduza o objeto

Obriga o leitor a dizer em palavras o que cada símbolo mede.

### BOX — Não confunda

Separa objetos semelhantes: semiperímetro versus área; lupa física versus amplificação didática; observação versus prova.

### BOX — Descoberta

Destaca uma identidade que nasce da combinação de resultados, por exemplo:

\[
A_{2n}^-=a_n.
\]

### BOX — Prova

Contém hipóteses, cadeia dedutiva e conclusão. Não contém saltos “óbvios”.

### BOX — Autópsia

Preserva um erro real e mostra por que parecia plausível. O erro da constante assintótica por fator `2` é candidato obrigatório.

### BOX — Porta fechada

Declara uma dependência futura sem utilizá-la clandestinamente.

### BOX — Exercício

Exige ação do leitor e oferece dica, tentativa, feedback e resolução separada.

---

## 7. Exercícios como parte do argumento

Todo laboratório inicial terá exercícios em quatro níveis.

### Nível 1 — leitura geométrica

Identificar `R`, `r`, `L/2`, pontos de tangência, vértices e ângulo reto.

### Nível 2 — reconstrução algébrica

Derivar `L`, perímetro e área a partir do triângulo.

### Nível 3 — identidade estrutural

Demonstrar `A_n^- = a_n²/b_n` e `A_{2n}^- = a_n`.

### Nível 4 — erro e assíntota

Distinguir qual constante pertence à diferença de semiperímetros e qual pertence à diferença de áreas.

Regras:

- resposta não aparece automaticamente;
- dica não entrega a conclusão;
- feedback explica o erro, não apenas marca vermelho;
- resolução completa permanece recolhida até solicitação;
- exercícios numéricos aceitam tolerância explícita;
- todo exercício possui alternativa textual para leitores sem interação visual.

---

## 8. Invariantes visuais

Uma release é bloqueada se qualquer um destes invariantes falhar:

1. o círculo passa visualmente pelos vértices marcados do inscrito;
2. o círculo é tangente aos lados marcados do circunscrito;
3. os dois conjuntos de pontos de contato não são confundidos;
4. a vista local nunca fica vazia;
5. a vista local sempre contém os três referentes ou os representa por guias explícitas;
6. `R`, `r` e `L/2` permanecem identificáveis em celular;
7. nenhum gráfico usa apenas cor para distinguir séries;
8. o estado numérico exibido corresponde ao desenho;
9. toda figura analítica possui descrição textual equivalente;
10. screenshots reais são vistas pelo leitor primário antes de qualquer tag.

O teste “há pixels pintados” não satisfaz nenhum desses invariantes sozinho.

---

## 9. Invariantes matemáticos

O oráculo do braço deve testar, para cada `n` admissível:

- identidade pitagórica do triângulo inscrito;
- identidade pitagórica do triângulo circunscrito;
- `A_n^- = a_n²/b_n`;
- `A_n^+ = b_n`;
- `A_{2n}^- = a_n`;
- cadeia de aprisionamento;
- monotonicidade dos quatro cercos;
- positividade dos erros;
- razão de diferença de áreas por diferença de semiperímetros tendendo a `2`;
- razão de contração tendendo a `1/4`;
- constantes assintóticas separadas;
- rejeição de `n < 3`, não inteiro e valores não finitos.

A implementação visual e a implementação do oráculo não podem compartilhar a mesma função de cálculo.

---

## 10. Estado epistemológico da primeira versão

O primeiro site do braço é um **protótipo canônico aberto**. Ele deve implementar imediatamente:

- triângulo fundamental;
- dois cercos;
- tabela de áreas e perímetros;
- gráficos comparativos;
- boxes centrais;
- exercícios autocorrigíveis;
- responsividade;
- acessibilidade estrutural;
- funcionamento offline.

Ainda não reivindica release até que:

- a prova textual completa seja revisada;
- o oráculo independente seja anexado;
- screenshots desktop e iPhone sejam inspecionadas;
- os exercícios sejam tentados por leitor real;
- nenhuma fórmula dependa de notação circular não declarada.

---

## 11. Estrutura do braço

```text
MATHeu$.md
arms/
└── matheus-dollar/
    ├── index.html
    ├── conjecturas.md
    ├── claims.yml
    └── audit/
```

O HTML é autocontido. O branch de trabalho é separado da `main`. A integração, se ocorrer, será por PR revisada e nunca por substituição silenciosa do outro braço.

---

## 12. Divisa

> **A figura deve confessar a fórmula. A fórmula deve sobreviver à prova. O exercício deve descobrir se o leitor realmente entendeu.**
