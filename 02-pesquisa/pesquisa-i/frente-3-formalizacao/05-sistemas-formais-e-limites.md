---
titulo: Sistemas formais e seus limites
tipo: pesquisa
camada: mundo
status: rascunho
fonte: pesquisa
atualizado: 2026-11-07
---

# Sistemas formais e seus limites

Responde a §7.4: como sistemas simbólicos fechados produzem conhecimento **e** pontos cegos; e a diferença entre demonstrar, calcular, observar, realizar e representar. Etiquetas `[H]` `[I]` `[A]` `[R]` `[C]`.

Princípio do documento-mãe a guardar: **consistência lógica não equivale a verdade ontológica**.

---

## 1. O que é um sistema formal

`[I]` Um sistema formal é um jogo de símbolos com três partes:
1. **Alfabeto**: os sinais permitidos.
2. **Axiomas**: frases aceitas sem demonstração (o ponto de partida).
3. **Regras de inferência**: como passar de frases aceitas a novas frases.

Um **teorema** é qualquer frase que se alcança a partir dos axiomas seguindo as regras. O ponto decisivo: **o jogo pode ser jogado sem saber o que os símbolos significam**. David Hilbert teria dito que nos fundamentos da geometria deveria ser possível dizer "mesas, cadeiras e canecas de cerveja" em vez de "pontos, retas e planos" `[H]` (anedota relatada por Blumenthal, biógrafo de Hilbert; SEP, "Hilbert's Program"). A verdade do teorema, dentro do sistema, depende só da forma.

**Distinções essenciais** `[H]` (SEP, "Gödel's Incompleteness Theorems"; "Model Theory"):
- **Consistência**: o sistema não prova ao mesmo tempo uma frase e sua negação. Em lógica clássica, um sistema inconsistente prova *tudo* — e por isso não serve para nada.
- **Completude** (no sentido relevante aqui): para toda frase da linguagem, o sistema prova ela ou sua negação.
- **Correção / adequação**: o que o sistema prova é verdadeiro **no domínio que se pretende descrever**. Isso não é propriedade interna — depende da relação com algo fora do sistema.
- **Modelo**: uma interpretação dos símbolos em que os axiomas ficam verdadeiros. Um mesmo sistema pode ter **vários modelos muito diferentes** (a geometria hiperbólica tem modelos dentro da euclidiana — arquivo 03).

## 2. Axiomas: começar de algum lugar

`[H]`/`[I]`: Euclides tratava axiomas como verdades evidentes. Depois das geometrias não euclidianas (arquivo 03), axiomas passaram a ser vistos como **escolhas**: ponto de partida cujas consequências se exploram. Mudar um axioma não "corrige" o sistema; gera **outro** sistema, igualmente consistente.

- **Lição** `[I]`: dentro de um sistema, o axioma é inquestionável por definição; fora dele, é a parte mais questionável de todas. Toda tradição que formaliza precisa de algo que não demonstra.
- **Axiomas independentes** `[H]`: o axioma da escolha e a hipótese do contínuo são independentes dos axiomas usuais da teoria dos conjuntos (ZF): Gödel (1938/1940) mostrou que não se pode refutá-los; Cohen (1963) mostrou que não se pode prová-los (SEP, "The Continuum Hypothesis"). `[I]` Há perguntas bem formuladas que o sistema-padrão da matemática simplesmente **não decide** — e a comunidade matemática não tem consenso sobre se elas "têm resposta" fora de algum sistema.

## 3. O projeto de Hilbert e Gödel

**O projeto** `[H]`: no início do séc. XX, após paradoxos na teoria dos conjuntos (paradoxo de Russell, 1901–02), Hilbert propôs formalizar toda a matemática e **provar, por métodos finitos e seguros, que o sistema era consistente** (SEP, "Hilbert's Program").

**Gödel (1931)** `[H]` — "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I" (SEP, "Gödel's Incompleteness Theorems"):
1. **Primeiro teorema**: qualquer sistema formal consistente, com regras mecanicamente verificáveis, e forte o suficiente para fazer aritmética básica, contém frases **que ele não consegue provar nem refutar**.
2. **Segundo teorema**: tal sistema, se consistente, **não consegue provar a própria consistência**.

**A ideia, sem fórmulas** `[I]`: Gödel codificou frases e provas como números, de modo que a aritmética pudesse "falar" sobre suas próprias provas. Então construiu uma frase que, decodificada, diz algo como "esta frase não é demonstrável neste sistema". Se o sistema a provasse, provaria algo falso (inconsistente). Logo, se é consistente, não a prova — e então ela é verdadeira (no modelo padrão dos números) e indemonstrável.

**O que Gödel NÃO diz** `[H]`/`[I]` (fonte de muito abuso; ver Franzén, *Gödel's Theorem: An Incomplete Guide to Its Use and Abuse*, 2005):
- Não diz que "toda verdade é relativa", nem que "a razão é limitada em geral", nem que "a mente humana supera máquinas" (essa última é tese de Lucas e Penrose, **fortemente contestada**).
- Não se aplica a qualquer sistema: exige força aritmética. Sistemas mais fracos (a geometria euclidiana elementar, na formalização de Tarski) **são completos e decidíveis** `[H]` (SEP, "Tarski's Truth Definitions" / literatura sobre geometria de Tarski).
- A frase indecidível pode ser acrescentada como novo axioma — mas o novo sistema terá sua própria frase indecidível. **O limite não se remove ampliando o sistema; ele se desloca**.

**Tarski (1933/1936)** `[H]`: a verdade aritmética não é definível dentro da própria aritmética (teorema da indefinibilidade). `[I]` Um sistema não consegue conter o conceito completo de "verdadeiro" sobre si mesmo; precisa de uma metalinguagem mais forte.

## 4. Indecidibilidade e computação

`[H]` Turing (1936, "On Computable Numbers...") e Church (1936): não existe procedimento mecânico geral que decida, para toda afirmação matemática, se ela é demonstrável. Em particular, o **problema da parada**: não existe programa que, dado qualquer programa, diga sempre se ele vai terminar ou rodar para sempre (SEP, "The Church-Turing Thesis"; "Computability and Complexity").

`[I]` Traduzindo: há perguntas perfeitamente claras sobre procedimentos para as quais nenhum procedimento dá resposta garantida. O único jeito de saber se um ritual (ou cálculo) termina pode ser **executá-lo** — e se ele não terminou ainda, nunca se sabe se vai terminar.

**Além disso, o caro e o impossível** `[H]`/`[I]`: muitas coisas são decidíveis em princípio mas exigem tempo astronômico (complexidade computacional). E sistemas caóticos (arquivo 04) são deterministas e imprevisíveis na prática. São três limites diferentes: **não demonstrável**, **não computável**, **não praticável**.

## 5. Modelo versus realidade

**Box** `[H]`: o estatístico George E. P. Box escreveu "all models are wrong" em "Science and Statistics" (*Journal of the American Statistical Association* 71, 1976); a forma completa "Essentially, all models are wrong, but some are useful" aparece em Box & Draper, *Empirical Model-Building and Response Surfaces* (1987, p. 424) (Wikipedia, "All models are wrong": https://en.wikipedia.org/wiki/All_models_are_wrong; SAS blog: https://blogs.sas.com/content/iml/2025/04/02/all-models-are-wrong.html). No contexto de 1976 a frase **não é ceticismo**: é defesa de modelos **parcimoniosos** e crítica a quem sofistica demais o modelo (sobreajuste) `[H]` (SAS blog).

**Wigner** `[H]`: "The Unreasonable Effectiveness of Mathematics in the Natural Sciences" (1960), sobre o mistério de estruturas criadas por motivos internos à matemática (números complexos, geometria de Riemann) se encaixarem depois na física (Wigner, *Communications on Pure and Applied Mathematics* 13, 1960 — referência padrão). `[I]` O mistério tem contrapartida pouco lembrada: a matemática que **não** se aplica a nada não é contada; há viés de sobrevivência no espanto.

**Modos de um modelo errar** `[I]`:
- **Domínio**: certo dentro de condições, falso fora (mecânica newtoniana a velocidades próximas à da luz).
- **Flexibilidade excessiva**: encaixa qualquer dado (epiciclos com círculos suficientes — arquivo 01) e por isso não arrisca nada.
- **Variáveis omitidas**: o que ficou fora volta como "ruído" ou "anomalia".
- **Reificação**: tomar a entidade do modelo pelo mundo (o éter, o calórico; "a média" como pessoa real).
- **Autoconfirmação**: o modelo orienta quais dados se coletam, e os dados confirmam o modelo (liga com §3.1, validação interna).

## 6. As cinco coisas de §7.4 — por que não são a mesma

| | Pergunta | Juiz | Exemplo onde se separa das outras |
|---|---|---|---|
| **1. Demonstrável** | Segue dos axiomas pelas regras? | o próprio sistema | Teoremas de geometria hiperbólica são demonstráveis e (por séculos) não pareciam "verdade do espaço" `[H]` |
| **2. Calculável / previsível** | Existe procedimento que gere o número/previsão? | procedimento + tempo | Efemérides babilônicas previam sem nada demonstrar; Lorenz: regras exatas, previsão impossível além do horizonte `[H]` |
| **3. Observável** | Pode ser registrado por percepção ou instrumento? | instrumento + observador | Curvatura do espaço: invisível em pequena escala; anomalias de órbita de Mercúrio observadas antes de explicadas (Le Verrier, 1859; explicada por Einstein, 1915) `[H]` |
| **4. Realizável tecnicamente** | Pode ser feito? | materiais, mãos, custo | Ondas de rádio previstas por Maxwell (1860s), produzidas por Hertz (1887–88) — duas décadas entre previsão e realização `[H]`. O inverso: técnicas (metalurgia, fermentação) realizadas milênios antes de qualquer cálculo `[H]` (cf. Frente 2) |
| **5. Representado sobre a realidade** | O que o sistema diz que o mundo **é**? | ninguém de forma definitiva | Maxwell dentro do éter: equações sobrevivem, ontologia cai `[H]`. Bombelli usava imaginários e negava que existissem `[H]` (arquivo 01) |

`[I]` Cada par pode se separar:
- **Demonstrável sem ser observável** (frase de Gödel; teoremas sobre infinitos).
- **Calculável sem ser demonstrado** (tabelas empíricas, receitas egípcias com verificação).
- **Observável sem ser calculável** (fenômenos caóticos; doenças reconhecidas por padrão clínico sem modelo).
- **Realizável sem ser representado** (conhecimento tácito do artesão, §8).
- **Representado sem ser realizável** (um modelo correto de algo que não se consegue fazer).

A ilusão típica de uma tradição formal: **deslizar de 1 para 5** — "provamos, logo é assim que o mundo é". A ilusão típica de uma tradição técnica: **deslizar de 4 para 5** — "funciona, logo nossa explicação é a verdadeira" (é exatamente a "passagem problemática" de §3.1 do documento-mãe) `[I]`.

## 7. Como sistemas fechados produzem pontos cegos

`[I]` Quatro mecanismos:
1. **O que não tem símbolo não pode ser perguntado.** Uma álgebra sem negativos (al-Khwarizmi) não "esconde" soluções negativas; ela não tem como formulá-las.
2. **Consistência protege o erro.** Um sistema coerente tem resposta para tudo dentro de si; a anomalia é reinterpretada em vez de aceita.
3. **Indecidíveis internos.** Mesmo um sistema perfeito tem perguntas que ele não fecha (Gödel), e a tradição pode tratá-las como sem sentido.
4. **Mudança exige alteração estrutural.** Alguns fenômenos só se representam mudando axiomas (paralelas), alfabeto (zero, imaginários) ou o tipo de objeto (de grandeza para relação). Isso não é ajuste: é ruptura — e quem rompe parece herege para o sistema anterior.

---

## Potencial ficcional

- **Uma tradição que sabe que é incompleta** `[R]` (Gödel/Tarski): sua doutrina central é que todo sistema de saber suficientemente rico contém verdades que ele mesmo não alcança. Em vez de desespero, gera uma **ética de axiomas**: cada geração acrescenta um novo princípio indemonstrável, sabendo que outro faltará. **Percebe**: os limites de qualquer sistema rival com precisão cirúrgica. **Ponto cego**: risco de usar a incompletude como desculpa para não decidir nada — e de abusar de Gödel exatamente como Franzén descreve (tudo vira "indecidível" quando convém).
- **Escolas de axiomas rivais** `[R]` (não euclidianas + independência): duas escolas que partilham tudo exceto um princípio inicial e, por isso, constroem mundos internamente impecáveis e incompatíveis. Nenhuma refuta a outra por lógica. O conflito só se resolve — se resolver — por observação, técnica ou utilidade. Argon fica no meio e precisa decidir o que contaria como teste.
- **Rituais que não se sabe se terminam** `[C]` (problema da parada): procedimentos longos cujo término não pode ser previsto por nenhuma análise; a única maneira é executá-los. Tradições que mantêm processos em curso por gerações sem saber se acabam. Fantasia sombria pura sem nenhuma magia: a angústia é lógica.
- **O deslizamento 1→5 como pecado intelectual** `[C]`: uma tradição formal de prestígio que confunde provar com saber o que o mundo é. Seus membros são brilhantes e, em certos domínios, sistematicamente errados — porque seus teoremas descrevem um modelo, não o território.
- **Os parcimoniosos de Box** `[R]`: uma tradição prática que desconfia de modelos sofisticados demais e prefere o mais simples que funciona. **Percebe** quando outros encaixam tudo e não preveem nada (epiciclos). **Ponto cego**: pode rejeitar a complexidade real quando ela existe.
- **Para Argon** `[C]`: ele experimenta antes de julgar (§9) — o que o põe naturalmente do lado de 3 e 4 (observar, realizar). O risco dele é o oposto do formalista: deslizar de 4 para 5. Um encontro produtivo é com alguém que lhe mostra uma impossibilidade **demonstrada** que ele estava tentando realizar por esforço.

## Questões em aberto
- Anedota de Hilbert ("canecas de cerveja"): relatada por Blumenthal; texto exato não conferido.
- Se a frase completa de Box aparece já em 1976: fontes secundárias divergem.
- Interpretação filosófica de Gödel sobre mente/máquina: aberta e contestada; não usar como fato.
- Wigner 1960: referência padrão, não refetchada.

## Fontes consultadas
- Wikipedia, "All models are wrong": https://en.wikipedia.org/wiki/All_models_are_wrong
- SAS blog (Rick Wicklin), 2025: https://blogs.sas.com/content/iml/2025/04/02/all-models-are-wrong.html
- Referências sem fetch: SEP ("Gödel's Incompleteness Theorems", "Hilbert's Program", "The Continuum Hypothesis", "The Church-Turing Thesis", "Model Theory", "Tarski's Truth Definitions"); T. Franzén, *Gödel's Theorem* (2005); Gödel 1931; Turing 1936; Wigner 1960; Box 1976; Box & Draper 1987.
