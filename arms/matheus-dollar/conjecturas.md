# MATHeu$ — Pré-registro do laboratório inicial

**Data:** 28/07/2026  
**Tipo:** reconstrução concorrente do sítio geométrico da exaustão.

## Pergunta central

Como reconstruir o método de exaustão a partir do triângulo retângulo fundamental `R–r–L/2`, de modo que perímetros, áreas, diferenças, gráficos e exercícios façam parte do argumento — e não sejam adereços posteriores?

## Conjecturas de implementação

- **C1:** SVG vetorial e uma vista local normalizada eliminarão a tela branca e a ambiguidade de contatos observadas no braço anterior.
- **C2:** o triângulo fundamental permitirá ao leitor reconstruir as fórmulas de perímetro e área sem recebê-las prontas.
- **C3:** a identidade `A⁻₂ₙ = aₙ` será didaticamente mais reveladora que a simples monotonicidade de duas colunas.
- **C4:** comparar simultaneamente áreas e semiperímetros impedirá a troca indevida do fator assintótico `2`.
- **C5:** exercícios interativos revelarão compreensões falsas que a leitura passiva não detecta.

## Refutadores

- qualquer estado em que os três referentes da vista local não estejam representados;
- desenho incompatível com os valores numéricos;
- exercício que aceite resposta errada ou rejeite resposta correta dentro da tolerância;
- gráfico cuja série não possa ser identificada sem cor;
- fórmula central que não possa ser reconstruída a partir dos objetos exibidos.

---

# Pré-registro da Expansão 02

**Data:** 29/07/2026  
**Documento contratual:** `EXPANSAO-02-LIMITES-TRIANGULOS-SETORES.md`.

## Pergunta central E02

Mantendo fixa uma circunferência de raio `ρ`, como perímetro, área, apótema, lados, triângulos locais, setores e segmentos se comportam quando `n` aumenta — e quais relações sobrevivem à mudança de escala, rotação e representação?

## Conjecturas prospectivas

- **E02-C1 — referência fixa:** manter a circunferência circunscrita fixa tornará visualmente inequívoco que os vértices pertencem ao mesmo círculo para todo `n`.
- **E02-C2 — normalização:** os presets `ρ=1`, `ρ=1/π` e `ρ=1/√π` permitirão separar estrutura geométrica de escolha de escala sem produzir confusão dimensional.
- **E02-C3 — velocidade:** os gráficos de `n²E_P` e `n²E_A` revelarão patamares distintos, correspondentes a `π³ρ/3` e `2π³ρ²/3`.
- **E02-C4 — razão de erros:** `E_A/E_P` tenderá a `2ρ`, e a forma adimensional dessa comparação permanecerá estável sob mudança de escala.
- **E02-C5 — triângulos locais:** o triângulo dos pontos de tangência será uma cópia homotética do triângulo dos vértices, com razão linear `cos θ` e razão de áreas `cos² θ`.
- **E02-C6 — setores:** setores e segmentos associados aos dois círculos repetirão a mesma distinção linear/quadrática.
- **E02-C7 — coordenadas:** a área calculada por decomposição trigonométrica coincidirá, dentro da tolerância, com a área calculada pela fórmula do cadarço.
- **E02-C8 — rotação:** variar `φ` alterará apenas a representação; distâncias, perímetros, áreas e erros permanecerão invariantes.
- **E02-C9 — complexos:** a órbita `z_{k+1}=z_k e^{2πi/n}` reconstruirá o mesmo polígono sem adicionar hipótese geométrica clandestina.
- **E02-C10 — 3D adiado:** uma camada tridimensional não acrescentará valor suficiente antes de as relações 2D estarem fechadas e auditadas.

## Refutadores E02

- qualquer vértice com distância ao centro diferente de `ρ` além da tolerância;
- qualquer tangência cuja reta não seja ortogonal ao raio correspondente;
- divergência entre área trigonométrica e área pelo cadarço;
- gráfico normalizado que mude indevidamente ao alterar `ρ`;
- rotação `φ` que altere uma grandeza intrínseca;
- setor visualmente indistinguível de triângulo ou segmento;
- desaparecimento de arco, corda ou tangente em qualquer estado admissível;
- uso de `1/π²` como normalização inteira sem demonstração;
- uso de números complexos como mera decoração, sem tradução verificável para coordenadas reais;
- introdução de `z`/3D sem uma pergunta matemática que não possa ser respondida no plano.

## Estatuto

As proposições matemáticas listadas no contrato são resultados a demonstrar e auditar. As conjecturas acima dizem respeito à eficácia didática, semântica e computacional da implementação. Nenhuma recebe promoção automática a `proved` pela simples publicação do documento.
