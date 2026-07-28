# Capítulo 0 — Análise de prioridade e novidade

Data: 28/07/2026. Executa (parcialmente) a pendência 1 do `sources.md`:
busca bibliográfica de prioridade para os resultados do capítulo, mais o
material do documento fundador destinado à reconstrução do Capítulo 1 (D3
em `AUDIT.md`).

**Método e limites.** Buscas na web aberta em 28/07/2026 (consultas dirigidas
por resultado; URLs na seção final). A busca **não é exaustiva**: não cobre
bases fechadas, literatura em outras línguas, nem o acervo completo de
revistas de desigualdades (RGMIA, JIPAM etc.), que é vasto. Portanto:
*ausência de resultado nas buscas não estabelece ineditismo* — apenas
qualifica o grau de confiança da classificação abaixo, nos termos da §1.12
do manual ("síntese autoral; prioridade histórica não estabelecida").

---

## Camada A — clássico consolidado (confirmado pelas buscas)

| Resultado do capítulo | Situação na literatura |
|---|---|
| Triângulo fundamental; r/R = cos(π/n) (Enunciados A, D–E, substância) | Material de referência corrente (MathWorld: Inradius, Polygon Inscribing; calculadoras e textos didáticos). Nenhuma novidade, como o `claims.yml` já declarava. |
| **Identidade da coroa** (Enunciado B) | É exatamente o **exemplo fundador do cálculo visual de Mamikon** (1959): a área da coroa depende só da corda tangente à circunferência interna — "independe dos raios". Documentado em Mamikon/Apostol (*Visual Calculus*, Caltech; cut-the-knot; Wikipedia "Visual calculus"). A citação de Mamikon que o capítulo fazia "como imagem" fica confirmada como a fonte canônica do resultado. Proveniência `classical` correta. |
| Desigualdade da cunha sen θ < θ < tg θ (Enunciado F) | Clássica (é a base geométrica do limite sen x/x em todo texto rigoroso). |
| **Medida do ângulo pela área** (convenção da seção 3) | Tem precedente direto e nobre: **Apostol** (*Calculus*, vol. 1) define seno e cosseno pelo ponto do círculo unitário que delimita setor de área θ/2 — exatamente a convenção do capítulo; tratamentos recentes (Results in Mathematics, 2025) seguem o mesmo caminho para evitar a dependência do comprimento de arco. A escolha do capítulo não é excentricidade autoral: é uma tradição rigorosa, adotada pelo mesmo motivo (adiar comprimento de arco). |
| **1 − cos x vs 2 sen²(x/2)** (§8, primeira mentira do computador) | É **o** exemplo de manual de cancelamento catastrófico (Wikipedia "Catastrophic cancellation"; Goldberg, *What Every Computer Scientist Should Know About Floating-Point Arithmetic*; notas de cursos de análise numérica). O fenômeno é pedagogia clássica; o que é do tratado é apenas a encenação específica ("o instrumento declara círculo" em n ≈ 3·10⁸) e sua promoção a invariante de oráculo. |

## Camada B — família clássica conhecida; empacotamento do tratado

**Sanduíches G e H** (déficit e folga). As desigualdades usadas
(sen y < y; y·cos y < sen y) e o gênero inteiro de resultado pertencem à
família **Jordan–Kober–Cusa-Huygens**, com literatura de refinamentos ampla e
ativa (survey de Qi–Niu–Guo, *Refinements, Generalizations, and Applications
of Jordan's Inequality*; refinamentos de Cusa-Huygens, arXiv:2009.01688;
arXiv:1405.0934). As buscas **não localizaram** os empacotamentos específicos
do capítulo — o fator de autorreferência ρ₂ₙ² no déficit, o fator ρₙ na
folga, e a identidade do meio cos α·cos β = (ρₙ + ρₙ₊₁)/2 — mas, dado o
volume dessa literatura, a classificação honesta permanece a que o
`claims.yml` já registra: substância elementar, quase certamente
redescobrível ou redescoberta; **prioridade não estabelecida**, agora com a
família vizinha identificada.

**Assintótica quadrática polígono-vs-círculo.** Bem trilhada: tratamentos
correntes de "quantos lados até parecer círculo" usam exatamente critérios
em n⁻² (desvio radial ∼ π²/2n², erro de perímetro ∼ π²/6n²; ex.: SAS/IML
blog, Quora/recreativa). O Enunciado G está nessa tradição.

## Camada C — síntese autoral; possível novidade de organização

**A moldura inferencial completa**: a razão r/R como estatística suficiente
da forma; a regra de decisão com erro δ; o **limiar cúbico** de identificação
(distinguir n de n+1 custa ∼ π²/n³, Enunciados H–J); a **janela crepuscular**
(a década inferencial entre o quadrático "é polígono" e o cúbico "qual
polígono", Enunciado K); e a regra editorial "desigualdades sem linguagem de
limite".

As buscas não encontraram tratamento equivalente. O adjacente mais próximo é
a **metrologia de circularidade** (roundness/lobing): lá também se pergunta
"quantos lóbulos tem esta peça quase-circular?", mas o método é análise
harmônica do perfil (UPR — undulations per revolution) e detecção por
V-block, não a razão inradius/circunradius; e o fato de que medições a dois
pontos *não detectam* lóbulos ímpares é um parente industrial da nossa janela
crepuscular ("o instrumento certifica desvio sem identificar a forma").
Nenhuma fonte localizada enuncia o contraste quadrático-vs-cúbico como
estrutura, nem a janela [(π²/2δ)^{1/3}, δ^{-1/2}].

**Classificação:** síntese autoral no âmbito deste tratado; a substância é
elementar e o ineditismo, se houver, é de organização e ênfase — não de
técnica. Prioridade histórica não estabelecida (busca não exaustiva; campos
candidatos a busca futura: metrologia dimensional, inverse problems
didáticos, psicofísica de formas).

## Material do D3 (documento fundador; ainda não implementado)

| Item | Situação |
|---|---|
| Recorrências HM/GM dos semiperímetros | Clássico e **bem estudado como algoritmo**: Phillips, *Archimedes the Numerical Analyst* (Amer. Math. Monthly 88(3), 1981, 165–169) e literatura subsequente do "algoritmo arquimediano" (meios harmônico-geométricos, conexões com Borchardt). O Capítulo 1 já cita a substância; a referência de Phillips deve entrar no `sources.md` do Cap. 1 quando D3 abrir. |
| A = ½·apótema·perímetro | Pré-arquimediano (documentado na literatura didática). |
| A⁺ₙ = bₙ e **A⁻₂ₙ = aₙ** (área do 2n-inscrito = semiperímetro do n-inscrito) | Consequência imediata do anterior; as buscas desta data **não localizaram** a identidade A⁻₂ₙ = aₙ enunciada e explorada como tal (a cadeia A⁻ₙ < A⁻₂ₙ = aₙ < π < b₂ₙ = A⁺₂ₙ < A⁺ₙ). Presumivelmente conhecida na literatura dos algoritmos de π; classificar, ao implementar D3, como redescoberta com prioridade não estabelecida — e repetir a busca antes de qualquer reivindicação. |
| Dualidade assintótica dos erros (π³/6, π³/3; 2π³/3, π³/3; a dominância troca de lado entre perímetro e área) | Substância: expansões de Taylor padrão. A *observação organizada* da troca de dominância é do documento fundador; mesma classificação de síntese autoral. |

## Consequências para o ledger

- Nenhuma proveniência do `claims.yml` precisa mudar: as classificações já
  eram conservadoras e as buscas as confirmaram (em particular, os
  `priority_note` dos sanduíches e da síntese inferencial permanecem).
- A caixa da seção 3 do capítulo ganha respaldo explícito (Apostol) — fica
  registrado aqui; o texto do capítulo não precisa de emenda.
- Pendência 1 do `sources.md`: **parcialmente executada** — família das
  desigualdades identificada, Mamikon confirmado como fonte canônica da
  coroa, precedente de Apostol localizado; permanece aberta para bases
  fechadas e literatura de metrologia antes de qualquer reivindicação de
  ineditismo.

## Referências das buscas (28/07/2026)

- Qi, Niu, Guo — *Refinements, Generalizations, and Applications of
  Jordan's Inequality and Related Problems* (survey; rgmia.org/papers/v11n2/refine-jordan-kober.pdf)
- *New Refinements of Cusa-Huygens inequality* — arXiv:2009.01688
- *On classical inequalities of trigonometric and hyperbolic functions* — arXiv:1405.0934
- Wikipedia — *Catastrophic cancellation*; Goldberg — *What Every Computer
  Scientist Should Know About Floating-Point Arithmetic* (docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html)
- Mamikon/Apostol — *Visual Calculus* (its.caltech.edu/~mamikon/VisualCalc.html);
  Wikipedia — *Visual calculus*; cut-the-knot — *Invariant Area Sweep Implies
  Pythagorean Theorem*
- MathWorld — *Inradius*, *Polygon Inscribing*
- Springer, Results in Mathematics (2025) — *How to Define Sine and Cosine…
  Rigorously and with Minimal Prerequisites* (link.springer.com/article/10.1007/s00025-025-02569-1)
- Taylor Hobson — *Roundness Measurement Errors and Effects*;
  what-when-how — *Measurement of Circularity (Metrology)*
- Phillips — *Archimedes the Numerical Analyst*, Amer. Math. Monthly 88(3)
  (1981) 165–169 (sites.math.rutgers.edu/~zeilberg/EM22/archimedes.pdf)
- SAS/IML blog — *Polygons, pi, and linear approximations*
  (blogs.sas.com/content/iml/2020/03/11/polygons-pi-linear-approx.html)
