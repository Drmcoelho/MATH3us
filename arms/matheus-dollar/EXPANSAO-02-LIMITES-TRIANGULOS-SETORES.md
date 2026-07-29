# MATHeu$ — Expansão 02
## Círculo fixo, limites, triângulos locais, setores, coordenadas e rotação

> Documento canônico de especificação matemática e visual.
> Estado: contrato prospectivo para implementação no braço `MATHeu$`.
> Data de registro: 29/07/2026.

---

## 0. Pergunta geradora

O laboratório inicial já reconstrói o método de exaustão a partir do triângulo retângulo fundamental `R–r–L/2`. A expansão seguinte deverá responder uma pergunta mais ampla:

> **O que acontece quando mantemos uma circunferência de referência fixa, fazemos `n` crescer e acompanhamos, simultaneamente, os polígonos, seus perímetros, suas áreas, os triângulos locais, os setores circulares e os erros de aproximação?**

O objetivo não é acrescentar figuras independentes. É revelar que todos esses objetos são projeções locais ou globais da mesma estrutura.

---

## 1. Dois regimes geométricos, explicitamente separados

O site terá dois regimes. Eles não podem ser confundidos nem combinados silenciosamente.

### 1.1 Regime A — circunferência circunscrita fixa

Escolhe-se um círculo de referência de raio `ρ > 0`. Para todo `n ≥ 3`, os `n` vértices do polígono regular pertencem à mesma circunferência.

O raio circunscrito permanece:

\[
R=\rho.
\]

Definindo

\[
\theta=\frac{\pi}{n},
\]

o apótema, o meio-lado e o lado valem:

\[
r=\rho\cos\theta,
\qquad
\frac L2=\rho\sin\theta,
\qquad
L=2\rho\sin\theta.
\]

O triângulo fundamental satisfaz:

\[
\rho^2=(\rho\cos\theta)^2+(\rho\sin\theta)^2.
\]

Neste regime:

- o círculo-base nunca muda;
- os vértices permanecem sobre ele;
- o apótema cresce com `n` e tende a `ρ`;
- o lado diminui e tende a zero;
- o perímetro e a área do polígono convergem para os valores do círculo fixo.

### 1.2 Regime B — incircunferência fixa

Escolhe-se um círculo de raio `ρ > 0` tangente aos lados do polígono circunscrito. O mesmo círculo pode funcionar como referência entre um cerco interno e um cerco externo.

Neste regime:

\[
r=\rho,
\qquad
R=\rho\sec\theta,
\qquad
\frac L2=\rho\tan\theta.
\]

Este é o regime adequado para:

- comparação entre aproximação interna e externa;
- cadeias de aprisionamento;
- recorrências harmônica e geométrica;
- diferença entre erros de perímetro e de área.

### 1.3 Regra de interface

Um seletor visível deverá oferecer:

- `circunferência circunscrita fixa`;
- `incircunferência fixa`.

A interface deve informar, em cada estado, qual grandeza permanece invariável e quais mudam com `n`.

---

## 2. Escolha do raio e normalizações especiais

O raio não ficará ocultamente fixado em `1`. O leitor poderá escolher `ρ` e alternar entre presets matematicamente significativos.

### 2.1 Preset unitário

\[
\rho=1.
\]

Então:

\[
C=2\pi,
\qquad
A=\pi.
\]

É a normalização mais conveniente para comparar com a formulação clássica.

### 2.2 Preset de circunferência inteira

\[
\rho=\frac1\pi.
\]

Então:

\[
C=2\pi\rho=2,
\qquad
A=\pi\rho^2=\frac1\pi.
\]

Este preset elimina `π` do comprimento da circunferência e permite estudar a convergência do perímetro para o inteiro `2`.

### 2.3 Preset de área unitária

Para obter área do círculo igual a `1`, o raio correto é:

\[
\rho=\frac1{\sqrt\pi}.
\]

Então:

\[
A=\pi\rho^2=1,
\qquad
C=2\sqrt\pi.
\]

### 2.4 Preset exploratório `1/π²`

O valor

\[
\rho=\frac1{\pi^2}
\]

poderá existir como entrada livre, mas não será descrito como normalização inteira, pois:

\[
C=\frac2\pi,
\qquad
A=\frac1{\pi^3}.
\]

### 2.5 Escala livre

O controle aceitará `ρ > 0`, com validação de:

- valores finitos;
- ausência de zero;
- ausência de valores negativos;
- tolerância numérica declarada.

### 2.6 Grandezas adimensionais

Para comparar raios diferentes, o laboratório exibirá também:

\[
\frac{P_n}{2\pi\rho},
\qquad
\frac{A_n}{\pi\rho^2},
\qquad
\frac{r}{\rho},
\qquad
\frac{L}{\rho}.
\]

Essas razões removem a escala e expõem apenas a geometria dependente de `n`.

---

## 3. Perímetro e área com circunferência fixa

No Regime A, o polígono regular inscrito possui:

### 3.1 Perímetro

\[
P_n=2n\rho\sin\left(\frac\pi n\right).
\]

E:

\[
\boxed{\lim_{n\to\infty}P_n=2\pi\rho}.
\]

### 3.2 Área

O polígono é a reunião de `n` triângulos isósceles de lados `ρ,ρ` e ângulo central `2π/n`:

\[
A_n
=n\cdot\frac12\rho^2\sin\left(\frac{2\pi}{n}\right).
\]

Equivalentemente:

\[
A_n
=n\rho^2\sin\left(\frac\pi n\right)
\cos\left(\frac\pi n\right).
\]

E:

\[
\boxed{\lim_{n\to\infty}A_n=\pi\rho^2}.
\]

### 3.3 Apótema e lado

\[
r_n=\rho\cos\left(\frac\pi n\right)
\longrightarrow\rho,
\]

\[
L_n=2\rho\sin\left(\frac\pi n\right)
\longrightarrow0.
\]

### 3.4 Leitura geométrica

O polígono não cresce indefinidamente. Ele muda de forma sob uma borda fixa:

- mais vértices;
- lados menores;
- apótema maior;
- perímetro maior e limitado;
- área maior e limitada.

---

## 4. Limites e velocidade de convergência

### 4.1 Erro do perímetro

Defina:

\[
E_P(n)=2\pi\rho-P_n.
\]

Pela expansão de `sen x` em torno de zero:

\[
P_n
=2\pi\rho-\frac{\pi^3\rho}{3n^2}+O(n^{-4}).
\]

Portanto:

\[
\boxed{E_P(n)\sim\frac{\pi^3\rho}{3n^2}}.
\]

Consequentemente:

\[
\boxed{n^2E_P(n)\longrightarrow\frac{\pi^3\rho}{3}}.
\]

### 4.2 Erro da área

Defina:

\[
E_A(n)=\pi\rho^2-A_n.
\]

Então:

\[
A_n
=\pi\rho^2-\frac{2\pi^3\rho^2}{3n^2}+O(n^{-4}),
\]

logo:

\[
\boxed{E_A(n)\sim\frac{2\pi^3\rho^2}{3n^2}}.
\]

E:

\[
\boxed{n^2E_A(n)\longrightarrow\frac{2\pi^3\rho^2}{3}}.
\]

### 4.3 Relação entre os erros

\[
\frac{E_A(n)}{E_P(n)}\longrightarrow 2\rho.
\]

Essa relação deve ser visualizada para múltiplos raios.

### 4.4 Forma adimensional dos erros

\[
\varepsilon_P(n)
=1-\frac{P_n}{2\pi\rho},
\]

\[
\varepsilon_A(n)
=1-\frac{A_n}{\pi\rho^2}.
\]

Essas grandezas não dependem da escala absoluta de `ρ`.

### 4.5 Gráficos obrigatórios

O laboratório deverá oferecer:

1. `P_n` e `2πρ`;
2. `A_n` e `πρ²`;
3. `E_P(n)` e `E_A(n)`;
4. erros em escala logarítmica;
5. `n²E_P(n)` e sua constante-limite;
6. `n²E_A(n)` e sua constante-limite;
7. `E_A/E_P` e o limite `2ρ`;
8. grandezas adimensionais para diferentes raios.

Cada gráfico terá tabela equivalente e descrição textual do comportamento.

---

## 5. Três triângulos locais

A geometria local será apresentada por três triângulos relacionados, não por uma única figura.

### 5.1 Triângulo retângulo fundamental

Pontos:

- `O`: centro;
- `M`: ponto médio de um lado;
- `V`: vértice.

Lados:

\[
OV=R,
\qquad
OM=r,
\qquad
MV=\frac L2.
\]

Identidade:

\[
R^2=r^2+\left(\frac L2\right)^2.
\]

### 5.2 Triângulo isósceles dos vértices

Pontos:

- centro `O`;
- dois vértices consecutivos `V_k,V_{k+1}`.

No Regime A:

\[
OV_k=OV_{k+1}=\rho,
\]

\[
V_kV_{k+1}=2\rho\sin\theta.
\]

Perímetro:

\[
p_V=2\rho+2\rho\sin\theta
=2\rho(1+\sin\theta).
\]

Área:

\[
T_V=\frac12\rho^2\sin(2\theta)
=\rho^2\sin\theta\cos\theta.
\]

### 5.3 Triângulo isósceles dos pontos de tangência

Os pontos de tangência consecutivos `T_k,T_{k+1}` pertencem à incircunferência do polígono, de raio:

\[
r=\rho\cos\theta.
\]

Então:

\[
OT_k=OT_{k+1}=r,
\]

\[
T_kT_{k+1}=2r\sin\theta.
\]

Perímetro:

\[
p_T=2r(1+\sin\theta).
\]

Área:

\[
T_T=r^2\sin\theta\cos\theta.
\]

### 5.4 Comparação exata

\[
\boxed{\frac{p_T}{p_V}=\frac r\rho=\cos\theta},
\]

\[
\boxed{\frac{T_T}{T_V}=\frac{r^2}{\rho^2}=\cos^2\theta}.
\]

Quando `n→∞`:

\[
\cos\theta\to1,
\qquad
\cos^2\theta\to1.
\]

A comparação deverá mostrar o efeito linear da escala nos perímetros e o efeito quadrático nas áreas.

---

## 6. O “sorvete”: setores e segmentos circulares

O termo informal “sorvete” será preservado como recurso didático, acompanhado da nomenclatura correta.

### 6.1 Setor circular dos vértices

O setor do círculo de raio `ρ` entre dois vértices consecutivos possui ângulo central:

\[
2\theta=\frac{2\pi}{n}.
\]

Área do setor:

\[
S_V=\rho^2\theta.
\]

Comprimento do arco:

\[
\ell_V=2\rho\theta.
\]

Perímetro da figura formada por dois raios e o arco:

\[
q_V=2\rho+2\rho\theta=2\rho(1+\theta).
\]

Segmento circular entre arco e corda:

\[
\Sigma_V=S_V-T_V
=\rho^2\left(\theta-\sin\theta\cos\theta\right).
\]

### 6.2 Setor da incircunferência

Para o raio `r=ρcosθ`:

\[
S_T=r^2\theta,
\]

\[
\ell_T=2r\theta,
\]

\[
q_T=2r(1+\theta),
\]

\[
\Sigma_T=r^2\left(\theta-\sin\theta\cos\theta\right).
\]

### 6.3 Razões estruturais

\[
\boxed{\frac{S_T}{S_V}=\cos^2\theta},
\]

\[
\boxed{\frac{\Sigma_T}{\Sigma_V}=\cos^2\theta},
\]

\[
\boxed{\frac{q_T}{q_V}=\cos\theta}.
\]

O mesmo padrão linear/quadrático reaparece:

- comprimentos e perímetros escalam como `cos θ`;
- áreas escalam como `cos² θ`.

### 6.4 Visualização obrigatória

Um seletor deverá alternar entre:

- triângulo isósceles;
- setor circular;
- segmento circular;
- sobreposição dos três.

O arco nunca será substituído visualmente pela corda.

---

## 7. Plano cartesiano

### 7.1 Rotação global

Introduz-se um ângulo de orientação `φ`, sem alterar a geometria intrínseca.

Os vértices são:

\[
V_k=
\left(
\rho\cos\left(\varphi+\frac{2\pi k}{n}\right),
\rho\sin\left(\varphi+\frac{2\pi k}{n}\right)
\right).
\]

Os pontos de tangência são:

\[
T_k=
\left(
r\cos\left(\varphi+\frac{(2k+1)\pi}{n}\right),
r\sin\left(\varphi+\frac{(2k+1)\pi}{n}\right)
\right).
\]

### 7.2 O que a camada cartesiana deverá ensinar

- vértice como ponto, não apenas encontro de segmentos;
- tangência como normal radial;
- corda entre dois pontos;
- distância euclidiana;
- inclinação da tangente;
- área pelo determinante ou fórmula do cadarço;
- equivalência entre cálculo coordenado e cálculo trigonométrico.

### 7.3 Verificação independente

A área do polígono deverá ser calculada por duas rotas independentes:

1. decomposição em triângulos;
2. fórmula do cadarço sobre os vértices.

Uma divergência acima da tolerância bloqueia a visualização.

---

## 8. Números complexos

A camada complexa é pertinente porque rotação e simetria são centrais. Não deve ser usada apenas como ornamento notacional.

### 8.1 Vértices complexos

\[
z_k=\rho\,e^{i(\varphi+2\pi k/n)}.
\]

A passagem ao vértice seguinte ocorre por multiplicação:

\[
z_{k+1}=z_k\,e^{2\pi i/n}.
\]

### 8.2 Pontos de tangência

\[
t_k=r\,e^{i(\varphi+(2k+1)\pi/n)}.
\]

### 8.3 Funções didáticas

A aba complexa deverá permitir:

- alternar entre forma cartesiana e polar;
- mostrar módulo e argumento;
- aplicar rotação `φ`;
- destacar a raiz da unidade `e^{2πi/n}`;
- reconstruir os vértices por multiplicações sucessivas;
- comparar a órbita complexa com o polígono desenhado.

### 8.4 Porta fechada

A igualdade

\[
e^{i\theta}=\cos\theta+i\sin\theta
\]

poderá ser usada apenas com estatuto declarado. Se a fórmula de Euler ainda não tiver sido construída no ciclo principal, a interface deverá marcá-la como representação importada ou porta futura.

---

## 9. Coordenada `z` e 3D

A coordenada `z` não pertence ao núcleo desta expansão.

Ela poderá entrar posteriormente em uma extensão opcional para:

- empilhar polígonos de diferentes `n` em alturas diferentes;
- construir uma superfície de convergência;
- representar `n` ou o erro no eixo vertical;
- extrudar setores para comparação volumétrica.

Regra de corte:

> Nenhuma visualização 3D entra se não revelar uma relação invisível nos gráficos 2D.

Rotação plana e números complexos têm prioridade sobre espetáculo tridimensional.

---

## 10. Arquitetura de interface

### 10.1 Controles globais

- regime geométrico;
- número de lados `n`;
- raio `ρ`;
- presets `1`, `1/π`, `1/√π`;
- orientação `φ`;
- escala absoluta ou adimensional;
- objeto local selecionado;
- grandeza gráfica;
- modo cartesiano/trigonométrico/complexo.

### 10.2 Painéis

1. **Círculo fixo e polígono** — visão global.
2. **Triângulo retângulo fundamental**.
3. **Triângulo dos vértices**.
4. **Triângulo dos pontos de tangência**.
5. **Setores e segmentos**.
6. **Tabela de grandezas globais**.
7. **Tabela de grandezas locais**.
8. **Gráficos de limite**.
9. **Coordenadas dos pontos**.
10. **Representação complexa**.

### 10.3 Regra de sincronização

Mudar `n`, `ρ`, `φ` ou regime atualiza todos os painéis a partir do mesmo estado imutável. Nenhum painel mantém estado matemático paralelo.

---

## 11. Boxes obrigatórios desta expansão

### BOX — O que ficou fixo?

Identifica a circunferência de referência e evita que o leitor atribua a convergência a uma mudança clandestina de escala.

### BOX — Normalização não é realidade

Explica que `ρ=1`, `1/π` e `1/√π` são escolhas de escala, não círculos geometricamente diferentes em estrutura.

### BOX — Limite

Separa:

- valor para `n` finito;
- tendência observada;
- limite demonstrado;
- termo assintótico.

### BOX — Linear versus quadrático

Compara:

\[
\frac{p_T}{p_V}=\cos\theta
\]

e

\[
\frac{T_T}{T_V}=\cos^2\theta.
\]

### BOX — O sorvete não é um triângulo

Distingue:

- triângulo;
- setor;
- segmento circular;
- perímetro com arco;
- perímetro com corda.

### BOX — Cartesiano e complexo dizem a mesma coisa?

Exige que o leitor traduza entre coordenadas e forma polar.

### BOX — Porta 3D

Explica por que a terceira dimensão foi adiada.

---

## 12. Exercícios

### N0 — socrático

1. O que permanece fixo quando `n` aumenta no Regime A?
2. Por que os lados diminuem enquanto o perímetro aumenta?
3. Por que o apótema tende ao raio?
4. O arco e a corda têm o mesmo comprimento para `n` finito?

### N1 — leitura geométrica

1. Marcar `V_k`, `V_{k+1}`, `T_k`, `T_{k+1}`, `O` e `M`.
2. Identificar qual círculo contém os vértices e qual contém as tangências.
3. Diferenciar triângulo, setor e segmento circular.

### N2 — cálculo direto

1. Calcular `P_n` e `A_n` para um `ρ` e `n` escolhidos.
2. Demonstrar `p_T/p_V=cosθ`.
3. Demonstrar `T_T/T_V=cos²θ`.
4. Mostrar que `ρ=1/π` produz circunferência `2`.
5. Determinar o raio que produz área unitária.

### N3 — limites e assíntotas

1. Demonstrar `P_n→2πρ`.
2. Demonstrar `A_n→πρ²`.
3. Identificar numericamente os limites de `n²E_P` e `n²E_A`.
4. Demonstrar `E_A/E_P→2ρ`.
5. Comparar os limites dos triângulos de vértices e de tangência.

### N4 — impossível por enquanto

1. Reconstruir rigorosamente a fórmula de Euler sem importá-la.
2. Formular uma superfície 3D cuja altura represente o erro e provar uma propriedade geométrica não visível em 2D.
3. Generalizar a construção para polígonos em geometrias de curvatura não nula.

Cada N4 deverá indicar a porta futura correspondente.

---

## 13. Claims planejadas

O ledger deverá incluir, após prova e auditoria:

- `dollar.fixed-circle-perimeter-limit`;
- `dollar.fixed-circle-area-limit`;
- `dollar.fixed-circle-perimeter-asymptotic`;
- `dollar.fixed-circle-area-asymptotic`;
- `dollar.area-error-perimeter-error-ratio`;
- `dollar.vertex-tangent-triangle-perimeter-ratio`;
- `dollar.vertex-tangent-triangle-area-ratio`;
- `dollar.sector-area-ratio`;
- `dollar.segment-area-ratio`;
- `dollar.cartesian-trigonometric-area-equivalence`;
- `dollar.complex-rotation-orbit`;
- `dollar.fixed-reference-visual-integrity`.

Nenhuma claim recebe `proved` antes de artefato simbólico, numérico e adversarial.

---

## 14. Invariantes do oráculo

O oráculo independente deverá testar:

1. todos os vértices satisfazem `|V_k|=ρ`;
2. todos os pontos de tangência satisfazem `|T_k|=r`;
3. cada tangente é ortogonal ao raio correspondente;
4. `R²=r²+(L/2)²`;
5. fórmula trigonométrica e cadarço fornecem a mesma área;
6. `P_n<2πρ` e cresce com `n`;
7. `A_n<πρ²` e cresce com `n`;
8. erros permanecem positivos;
9. `n²E_P` aproxima `π³ρ/3`;
10. `n²E_A` aproxima `2π³ρ²/3`;
11. `E_A/E_P` aproxima `2ρ`;
12. razões dos triângulos são `cosθ` e `cos²θ`;
13. razões dos setores e segmentos são coerentes;
14. rotação `φ` não altera distâncias, perímetros ou áreas;
15. presets de raio produzem os valores declarados;
16. entradas inválidas são recusadas.

---

## 15. Invariantes visuais

Uma release será bloqueada se:

- os vértices parecerem sair da circunferência fixa;
- os pontos de tangência não puderem ser distinguidos dos vértices;
- o arco for confundido com a corda;
- o setor for apresentado como triângulo;
- mudar `ρ` deformar razões adimensionais;
- mudar `φ` alterar métricas invariantes;
- qualquer série gráfica depender apenas de cor;
- qualquer objeto desaparecer sob zoom ou mudança de `n`;
- a representação complexa não corresponder à cartesiana;
- a vista móvel ocultar rótulos centrais.

---

## 16. Plano de implementação

### Fase D2.1 — estado e raio

- estado único `{regime,n,rho,phi}`;
- presets de raio;
- grandezas globais;
- valores adimensionais.

### Fase D2.2 — limites e gráficos

- perímetro;
- área;
- erros;
- erros normalizados por `n²`;
- constante-limite;
- tabelas acessíveis.

### Fase D2.3 — triângulos comparados

- retângulo fundamental;
- isósceles dos vértices;
- isósceles das tangências;
- razões lineares e quadráticas.

### Fase D2.4 — setores e segmentos

- arco;
- corda;
- setor;
- segmento;
- comparações interna e externa.

### Fase D2.5 — cartesiano e complexo

- coordenadas;
- rotação `φ`;
- cadarço;
- órbita complexa;
- tradução entre formas.

### Fase D2.6 — exercícios e auditoria

- exercícios N0–N4;
- oráculo independente;
- Safari/iOS;
- screenshots;
- revisão adversarial.

---

## 17. Critério de fechamento

Esta expansão só poderá ser declarada fechada quando o leitor conseguir percorrer, em ambos os regimes, a cadeia:

\[
\boxed{
\text{círculo fixo}
\to
\text{pontos}
\to
\text{triângulos}
\to
\text{polígono}
\to
\text{perímetro e área}
\to
\text{erro}
\to
\text{limite}
\to
\text{coordenadas}
\to
\text{rotação complexa}
}
\]

sem que nenhuma mudança de escala, objeto ou estatuto epistemológico ocorra de forma implícita.
