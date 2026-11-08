---
titulo: Estruturas relacionais — grafos, dinâmica, informação, simetria
tipo: pesquisa
camada: mundo
status: rascunho
fonte: pesquisa
atualizado: 2026-11-07
---

# Estruturas relacionais

Quatro ferramentas modernas que **não descrevem coisas, mas padrões de relação**: quem se liga a quem (grafos), como um estado se transforma em outro (sistemas dinâmicos), quanto uma mensagem reduz a incerteza (informação), o que permanece igual sob transformação (simetria). Etiquetas `[H]` `[I]` `[A]` `[R]` `[C]`.

Nota de método `[I]`: estas são ferramentas dos séculos XVIII–XX. Usá-las como matéria-prima de tradições ficcionais pré-modernas é **recombinação** `[R]`. Não se afirma que alguma tradição histórica as possuísse.

---

## 1. Grafos

**O que é** `[H]`/`[I]`: um grafo é só **pontos (nós) e ligações (arestas)**. Nada mais: sem distância, sem forma. Nasceu com Euler e as pontes de Königsberg (arquivo 03). Pode representar cidades e estradas, pessoas e parentescos, reações químicas, rotas de contágio, dependências entre tarefas.

**O que permite calcular** `[H]` (resultados-padrão; Britannica, "graph theory"; Barabási, *Network Science*, 2016, acesso aberto em networksciencebook.com):
- **Caminhos**: existe trajeto de A a B? Qual o mais curto?
- **Centralidade**: quais nós estão em mais caminhos (pontes, gargalos)? Um nó pequeno pode ser crucial se é o único elo entre dois grupos.
- **Conectividade e cortes**: quantas ligações é preciso cortar para separar a rede? Onde está o ponto frágil?
- **Ciclos**: há retornos (realimentação)?
- **Coloração**: o teorema das quatro cores (todo mapa plano se colore com 4 cores sem vizinhos iguais), provado por Appel e Haken (1976) com auxílio massivo de computador — primeira grande prova que nenhum humano verificou inteira à mão `[H]` (MacTutor, "The four colour theorem"). Ponte para o arquivo 05: o que é uma prova que ninguém consegue ler?

**Achados de rede com cara de lei social** `[H]`:
- **Mundo pequeno**: em muitas redes reais, poucos passos separam quaisquer dois nós (Milgram, 1967, cartas encaminhadas; Watts & Strogatz, *Nature*, 1998, modelo formal).
- **Hubs**: muitas redes têm poucos nós com enorme número de ligações (Barabási & Albert, *Science*, 1999). Tais redes resistem a falhas aleatórias e são **frágeis a ataques dirigidos aos hubs**. (O alcance da universalidade dessas "redes sem escala" é **debatido**: Broido & Clauset, *Nature Communications*, 2019.)

**O que oculta** `[I]`: intensidade e qualidade da relação (uma aresta é uma aresta), o que acontece *dentro* do nó, a história que formou a rede. E o maior risco: **o mapa de ligações escolhido define o que se vê** — quem decide quais relações contam como aresta já decidiu metade da conclusão.

## 2. Sistemas dinâmicos

**O que é** `[I]`: um sistema dinâmico é uma **regra que diz como o estado atual vira o próximo estado**. O "estado" pode ser posição e velocidade de planetas, populações de presas e predadores, temperatura e pressão. Em vez de perguntar "onde estará em tal dia", a teoria pergunta **que tipos de comportamento são possíveis no longo prazo** — imagina-se o espaço de todos os estados possíveis (espaço de fase) e olha-se o desenho das trajetórias.

**Conceitos centrais**:
- **Ponto fixo / equilíbrio**: estado que não muda. Pode ser *estável* (perturbado, volta) ou *instável* (perturbado, foge) — uma bola no fundo de uma tigela vs. no topo de uma colina `[H]`.
- **Ciclo limite**: o sistema cai num ritmo que se repete sozinho, independentemente de onde começou (batimentos, alguns ciclos populacionais) `[H]`.
- **Atrator**: a região para onde trajetórias convergem. Pode ser ponto, ciclo, ou **atrator estranho** (forma fractal, como o atrator de Lorenz em forma de asas de borboleta) `[H]`.
- **Bacia de atração**: o conjunto de estados iniciais que levam a um certo atrator. Duas bacias vizinhas podem ter fronteira intrincadíssima `[H]`.
- **Bifurcação**: ao mudar lentamente um parâmetro (temperatura, taxa de crescimento), o comportamento muda **de tipo** de repente — um equilíbrio vira oscilação, uma oscilação vira caos. Pequena causa contínua, efeito qualitativo descontínuo `[H]`.
- **Histerese**: depois de uma bifurcação, desfazer a mudança do parâmetro nem sempre traz o sistema de volta; o caminho de ida difere do de volta `[H]` (ex.: modelos de lagos que viram turvos e não voltam a ficar limpos só reduzindo poluente; Scheffer et al., *Nature*, 2001 — citado de memória).

**Caos** `[H]`:
- Poincaré, ao estudar o problema dos três corpos (prêmio do rei Oscar II, 1889–1890), percebeu que trajetórias podem ser extremamente sensíveis às condições iniciais; a primeira versão premiada continha um erro, corrigido na versão impressa — e foi a correção que revelou o comportamento caótico (Barrow-Green, *Poincaré and the Three Body Problem*, 1997; MacTutor, "Poincaré").
- Lorenz (1963, "Deterministic Nonperiodic Flow", *Journal of the Atmospheric Sciences*) achou, num modelo simplificado de convecção, que arredondar um número de 6 para 3 casas decimais mudava completamente a previsão a médio prazo. Palestra de 1972: "Does the flap of a butterfly's wings in Brazil set off a tornado in Texas?" `[H]` (MacTutor/Britannica, "Lorenz"; título da palestra amplamente citado).
- May (1976, *Nature*, "Simple mathematical models with very complicated dynamics"): a equação logística, um modelo de população com uma linha só, produz equilíbrio, ciclos de 2, 4, 8... e caos ao aumentar a taxa de crescimento. Feigenbaum (1978) mostrou que a razão entre intervalos sucessivos dessas duplicações converge para uma constante universal (~4,669) que vale para uma classe enorme de sistemas diferentes `[H]`.

**O que isso significa** `[I]`:
1. **Determinismo ≠ previsibilidade.** Um sistema pode seguir regras exatas sem acaso nenhum e, mesmo assim, ser imprevisível na prática além de um horizonte, porque nenhum instrumento mede o estado inicial com precisão infinita.
2. **Mas há previsão de outro tipo.** Não se sabe *onde* a trajetória estará, mas sabe-se *em que forma* ela vive (o atrator), com que frequência visita cada região (estatística), e que transições são possíveis. Previsão qualitativa e estatística sobrevive à perda da previsão pontual. (O clima é previsível em médias; o tempo, só por dias.)
3. **Universalidade.** Sistemas físicos totalmente diferentes podem compartilhar a mesma estrutura de transição (constante de Feigenbaum). `[A]` Semelhança de comportamento **sem** identidade de mecanismo — exatamente o critério 2 de §13 do documento-mãe, mas com um giro: às vezes a semelhança de forma **é** real e profunda, embora os mecanismos difiram.

**O que oculta** `[I]`: o modelo dinâmico pressupõe que se escolheram as variáveis certas; variáveis omitidas viram "ruído". Bifurcações só são reconhecíveis se o modelo tem o parâmetro certo.

## 3. Teoria da informação

**Origem** `[H]`: Claude Shannon, "A Mathematical Theory of Communication", *Bell System Technical Journal* (1948). Shannon separou explicitamente o **significado** da mensagem do problema técnico de transmiti-la: "os aspectos semânticos da comunicação são irrelevantes para o problema de engenharia" (paráfrase de passagem da introdução) `[H]` (SEP, "Information"; Britannica, "information theory").

**Entropia, em palavras** `[I]`: a informação de uma mensagem mede **quanta incerteza ela elimina**. Se você já sabe o que vem, a mensagem não informa nada. Uma moeda honesta: cada lançamento dá 1 *bit* (uma pergunta sim/não). Uma moeda viciada que dá cara 99% das vezes: cada lançamento informa muito pouco em média — você já quase sabia. A **entropia** de uma fonte é essa média: quanto, em média, cada símbolo surpreende. (Fórmula, para quem quiser: H = −Σ p·log₂ p, a soma, sobre cada resultado possível, da probabilidade vezes o logaritmo dela, com sinal trocado.)

**Resultados com consequência prática** `[H]`:
- **Compressão**: não se pode comprimir uma fonte, sem perda, abaixo de sua entropia. Linguagens naturais são muito redundantes (Shannon estimou para o inglês algo em torno de 1 bit por letra em textos longos, muito menos que o máximo possível — estimativa de 1951, de memória).
- **Canal com ruído**: para qualquer canal com ruído há uma **capacidade**; abaixo dela, é possível transmitir com erro tão pequeno quanto se queira **adicionando redundância bem planejada** (códigos corretores de erros). Acima dela, não há truque.
- **Redundância protege**: repetição, padrões de verificação, rima e métrica numa tradição oral funcionam `[A]` como códigos corretores: permitem detectar e corrigir erros de transmissão. (Analogia, não identidade.)

**O que oculta** `[I]`: o **significado**, por construção. Uma tradição pode transmitir a mensagem perfeitamente e perder o que ela queria dizer. E a entropia depende de um modelo de expectativa: o que surpreende um observador não surpreende outro — **informação é relativa a quem já sabe o quê**.

**Ponte com termodinâmica** `[H]`: a fórmula de Shannon tem forma idêntica à entropia estatística de Boltzmann/Gibbs; a relação conceitual foi explorada por Jaynes (1957) e Landauer (1961: apagar informação tem custo energético mínimo). A profundidade dessa ligação ainda é discutida (SEP, "Information Processing and Thermodynamic Entropy").

## 4. Simetria, grupos e o teorema de Noether

**Simetria, em palavras** `[I]`: uma simetria é uma **transformação que deixa algo igual**. Girar um quadrado 90° o deixa igual; girar 45° não. O conjunto de todas as transformações que deixam algo igual tem estrutura própria: fazer duas seguidas dá outra do conjunto, cada uma tem desfazer. Essa estrutura chama-se **grupo**.

**Origem** `[H]`: Galois (morto em 1832, aos 20 anos) usou grupos de permutações das raízes de uma equação para explicar **por que** equações de grau 5 ou mais não têm, em geral, fórmula de solução por radicais (resultado de impossibilidade de Abel–Ruffini, explicado estruturalmente por Galois) (MacTutor, "Galois"). `[I]` Outra impossibilidade estrutural: séculos procurando uma fórmula que não pode existir.

**Ornamentos** `[H]`: existem exatamente 17 tipos de simetria para padrões planos que se repetem em duas direções (grupos de papel de parede; Fedorov 1891, Pólya 1924). Afirma-se com frequência que os azulejos da Alhambra exibem todos os 17; isso é **disputado** (depende de critérios de contagem) `[H]` com ressalva (Grünbaum, "What symmetry groups are present in the Alhambra?", *Notices AMS*, 2006 — citado de memória). `[I]` Artesãos produziram estruturas que só seriam classificadas séculos depois.

**Teorema de Noether** `[H]`: Emmy Noether, "Invariante Variationsprobleme" (1918). Em sistemas físicos descritos por um princípio de ação (a forma padrão da física moderna), **a cada simetria contínua corresponde uma quantidade conservada** (MacTutor, "Noether"; SEP, "Symmetry and Symmetry Breaking"):
- As leis não mudam de um instante para outro (simetria no tempo) ↔ conserva-se a **energia**.
- As leis não mudam de um lugar para outro (simetria no espaço) ↔ conserva-se o **momento linear**.
- As leis não mudam com a direção (simetria de rotação) ↔ conserva-se o **momento angular**.

**Por que isso importa para o mundo** `[I]`: Noether transforma uma pergunta sobre *o que se conserva* (quantidades, "substâncias") em uma pergunta sobre *o que é indiferente* (simetrias, "relações"). A conservação de energia deixa de ser um fato bruto sobre uma "coisa" e vira consequência de o mundo não distinguir um momento de outro. **Uma ontologia de substâncias e uma ontologia de relações dão, aqui, o mesmo resultado por caminhos diferentes** — e quando uma simetria se quebra, a conservação correspondente deixa de valer. Em escalas cosmológicas, com a expansão do universo, a conservação global de energia é sutil e debatida pelos físicos `[H]` (discussão padrão em cosmologia; não detalhada aqui).

**Quebra de simetria** `[H]`/`[I]`: muitos fenômenos surgem quando um sistema simétrico "escolhe" um estado não simétrico (lápis em pé cai numa direção; ímã escolhe um polo ao esfriar). A lei é simétrica; o resultado não.

**O que oculta** `[I]`: só vale para simetrias contínuas e sistemas com formulação variacional; sistemas com atrito/dissipação escapam à forma simples. E a simetria pode ser aproximada — o pensamento por simetria tende a idealizar.

---

## Potencial ficcional

- **Tecelões de redes** `[R]` (grafos): uma tradição que mapeia parentesco, dívida, juramento e comércio como grafos. Percebe gargalos, pontes, quem é indispensável apesar de parecer pequeno; prevê que um reino com poucos hubs cai se os hubs caírem. **Ponto cego**: trata toda ligação como igual; não vê ódio dentro do parentesco, nem a qualidade do vínculo. E quem desenha o mapa decide o que vê — conflito político perfeito.
- **Leitores de bacias** `[R]` (dinâmica): sabem que não podem prever o detalhe, mas conhecem o "relevo" de possibilidades: onde uma sociedade, uma doença, um clima tende a cair; quando um pequeno empurrão contínuo vai provocar uma virada súbita (bifurcação) e por que desfazer a causa não desfaz o efeito (histerese). Percebem limiares que tradições lineares não veem. **Ponto cego**: dependem de ter escolhido as variáveis certas; tudo fora delas é "ruído" — e o desastre vem do ruído. Também: podem parecer fatalistas ou charlatães porque recusam previsões precisas.
- **Determinismo sem profecia** `[C]`: uma escola convencida de que o mundo é inteiramente regido por regras e, mesmo assim, de que nenhuma profecia é possível além de um horizonte. Choca-se com uma tradição oracular que faz previsões pontuais e às vezes acerta. Argon precisa distinguir acerto por estrutura de acerto por sorte.
- **Guardiões da redundância** `[R]` (informação): uma tradição oral que sabe exatamente quanta repetição, rima e verificação um texto precisa para sobreviver N gerações. Transmite com fidelidade espantosa a **forma**; perde o **significado** (os versos chegam intactos e ninguém sabe o que querem dizer). `[C]` Seu oposto: uma tradição que transmite o sentido e muda as palavras a cada geração.
- **Informação relativa ao observador** `[C]`: o mesmo sinal é revelação para um e ruído para outro. Uma tradição que mede o valor de um sinal pela surpresa que causa entra em conflito com outra que o mede pela autoridade de quem fala.
- **Teólogos da indiferença** `[R]` (Noether): uma tradição que explica a permanência das coisas não por uma substância eterna, mas pelo fato de o mundo não distinguir certos lugares, tempos ou direções. Para ela, se um lugar *passa a ser diferente dos outros*, algo que se conservava ali deixa de se conservar. **Percebe** ligações entre "o que é igual" e "o que dura" que tradições de substância não veem. **Ponto cego**: dissipação, atrito, desgaste — o mundo real nunca é perfeitamente simétrico, e a tradição idealiza demais. Uma tradição assim *interpretaria* um lugar estranho como "assimétrico" — `[C]`, como leitura possível dessa tradição, não como propriedade das leis do mundo (que o autor ainda não definiu; pergunta aberta #20).
- **Artesãos antes da teoria** `[R]` (ornamentos/Alhambra): mestres que produzem padrões cuja estrutura um sistema formal posterior só classificará depois — e que talvez tenham esgotado possibilidades que a teoria declara finitas. Ótimo para o tema de §8: saber fazer sem saber formalizar.

## Questões em aberto
- Universalidade de redes sem escala: debatida (Broido & Clauset 2019).
- Alhambra com os 17 grupos: disputado.
- Detalhes de Scheffer 2001, estimativa de Shannon 1951, artigo de Grünbaum 2006: citados de memória, não conferidos online.
- Estatuto da ligação entropia de Shannon ↔ termodinâmica: debatido.

## Fontes
Referências de conhecimento padrão, não refeitas online nesta rodada (verificar antes de uso canônico): Shannon 1948 (BSTJ 27); Noether 1918 (*Nachr. Ges. Wiss. Göttingen*); Lorenz 1963 (*J. Atmos. Sci.* 20); May 1976 (*Nature* 261); Watts & Strogatz 1998; Barabási & Albert 1999; Broido & Clauset 2019; Barrow-Green 1997; MacTutor (Noether, Galois, Poincaré, "The four colour theorem"); SEP ("Information", "Symmetry and Symmetry Breaking", "Information Processing and Thermodynamic Entropy"); Britannica ("graph theory", "information theory"); Barabási, *Network Science* (https://networksciencebook.com).
