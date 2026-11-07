---
titulo: Geometria e topologia — do objeto à relação
tipo: pesquisa
camada: mundo
status: rascunho
fonte: pesquisa
atualizado: 2026-11-07
---

# Geometria e topologia

Responde a §7.3. Pergunta-guia: **o que muda quando se vê o mundo como relações, conexões, superfícies e transformações — e não como objetos com medidas?** Etiquetas `[H]` `[I]` `[A]` `[R]` `[C]`. Por exigência de §7.3 e §15, nada aqui é subordinado a círculos mágicos ou regras.

Uma ideia unificadora `[H]`/`[I]`: Felix Klein, no *Programa de Erlangen* (1872), propôs que **cada geometria se define pelo que permanece invariante sob um grupo de transformações** (MacTutor, "Klein"; Britannica, "Erlangen program"). Euclidiana: o que não muda quando se move e gira uma figura (distâncias, ângulos). Projetiva: o que não muda quando se projeta uma sombra (retas continuam retas, mas distâncias não). Topologia: o que não muda quando se **estica e deforma sem rasgar nem colar**. Cada passo **esquece** mais coisas — e por isso enxerga coisas mais gerais. É a melhor chave para este arquivo: **cada geometria é uma decisão sobre o que importa**.

---

## 1. Geometria euclidiana: o mundo como medida e forma

**O que é** `[H]`: sistema dos *Elementos* (c. 300 a.C.). Cinco postulados; o quinto (das paralelas) diz, na formulação equivalente de Playfair, que por um ponto fora de uma reta passa **exatamente uma** paralela (MacTutor, "Non-Euclidean geometry"; SEP, "Nineteenth Century Geometry").

**O que permite** `[I]`: comparar e transportar medidas; semelhança (figuras do mesmo formato em escalas diferentes), o que permite medir o inacessível por modelo reduzido; construção (com régua e compasso) como forma de existência — na tradição euclidiana, **mostrar que algo pode ser construído é mostrar que existe** `[H]` (SEP, "Euclid" — título aproximado).

**Ontologia implícita** `[I]`: um espaço homogêneo, igual em toda parte, infinito, em que figuras podem ser movidas sem se deformar. O espaço é **palco neutro**; os objetos é que têm propriedades.

**O que oculta** `[I]`: curvatura do próprio espaço; qualquer propriedade que dependa de "onde" se está; as conexões de longo alcance (que partes se comunicam com quais).

## 2. Geometrias não euclidianas: o palco tem forma

**A história** `[H]`: por dois mil anos tentou-se provar o quinto postulado a partir dos outros. Saccheri (1733) tentou por absurdo e derivou teoremas "estranhos" que julgou contraditórios. Gauss, Bolyai (publicado 1832) e Lobachevsky (1829) aceitaram negar o postulado e obtiveram geometrias consistentes (hiperbólica: infinitas paralelas por um ponto). Riemann (palestra de habilitação, 1854) generalizou para espaços cuja curvatura pode variar de ponto a ponto. Beltrami (1868) construiu modelos da geometria hiperbólica dentro da euclidiana, mostrando que, se a euclidiana é consistente, a hiperbólica também é (MacTutor, "Non-Euclidean geometry"; SEP, "Nineteenth Century Geometry").

**O que muda conceitualmente** `[I]`:
- Soma dos ângulos de um triângulo: =180° (plano), >180° (esfera: um triângulo do Polo Norte a dois pontos do Equador pode ter três ângulos retos), <180° (hiperbólico).
- **A geometria vira questão empírica.** Se há várias geometrias consistentes, qual é a do mundo é algo a medir. Gauss teria medido o triângulo entre três montanhas (Brocken, Hohehagen, Inselsberg) — se para testar isso é debatido `[H]` (MacTutor; tema controverso entre historiadores).
- Poincaré defendeu que a escolha da geometria é em parte **convenção** (a mais conveniente), não fato (*La Science et l'hypothèse*, 1902) `[H]` (SEP, "Poincaré" / "Conventionalism").
- Einstein (relatividade geral, 1915) usou a geometria de Riemann: gravidade como curvatura do espaço-tempo `[H]`.

**Lição para o mundo** `[I]`: **a consistência de um sistema não decide se ele descreve o mundo** (ponte para o arquivo 05). Durante séculos, a euclidiana foi considerada *a* verdade sobre o espaço (Kant a tratou como forma a priori da intuição) `[H]` (SEP, "Kant's Views on Space and Time"). Isso é um caso histórico perfeito de §4 do documento-mãe: o pressuposto "evidente" de uma época.

**Ponto de percepção** `[I]`: pequenas regiões de um espaço curvo parecem planas. Um ser que só mede localmente nunca descobre a curvatura — precisa de **triângulos grandes**, de dar a volta, ou de comparar o que acontece com uma direção transportada ao longo de um caminho fechado (na esfera, uma seta transportada "paralelamente" ao redor de um triângulo volta girada; chama-se *holonomia*) `[H]` conceito padrão.

## 3. Topologia: o que sobrevive à deformação

**Definição acessível** `[I]`: a topologia estuda as propriedades de uma forma que **não mudam** quando ela é esticada, torcida, amassada — desde que não se rasgue nem se cole partes. Para um topólogo, uma xícara com alça e uma rosca (toro) são "a mesma coisa": ambas têm um buraco. Uma bola e um cubo também são a mesma coisa. Distância, ângulo, tamanho, reto/curvo — tudo isso desaparece. O que fica:

- **Conexão**: a coisa é uma peça só ou várias? Dá para ir de qualquer ponto a qualquer outro sem sair dela?
- **Buracos** (*genus*): quantos "furos de alça" a superfície tem. Esfera: 0; toro: 1; pretzel de dois furos: 2.
- **Orientabilidade**: a superfície tem dois lados distintos?
- **Continuidade**: pontos vizinhos continuam vizinhos depois da transformação.
- **Fronteira**: a superfície tem borda?

**Origens** `[H]`: Leibniz já desejava uma *analysis situs* ("análise da posição"), um cálculo de relações de lugar distinto do cálculo de grandezas (carta a Huygens, 1679) (SEP, "Leibniz's Philosophy of Mathematics" — referência à *analysis situs*; MacTutor, "Topology enters mathematics"). Euler cita explicitamente essa "geometria da posição" no artigo das pontes.

### 3.1. As pontes de Königsberg (Euler)

`[H]` Königsberg tinha sete pontes ligando duas margens e duas ilhas do rio Pregel. Pergunta popular: é possível passear atravessando cada ponte exatamente uma vez? Euler apresentou a solução à Academia de São Petersburgo em 26 de agosto de 1735; o artigo *Solutio problematis ad geometriam situs pertinentis* saiu no volume dos *Commentarii* datado de 1736, impresso em 1741 (Wikipedia, "Seven Bridges of Königsberg": https://en.wikipedia.org/wiki/Seven_Bridges_of_K%C3%B6nigsberg; historyofinformation.com).

**O gesto decisivo** `[I]`: Euler **jogou fora** tudo o que parecia importante — o formato das ilhas, o comprimento das pontes, a largura do rio — e ficou só com: *quais massas de terra se ligam a quais, por quantas pontes*. Nisto, a resposta fica evidente: cada vez que se entra numa região, é preciso sair por outra ponte; logo, toda região que não seja início ou fim do passeio precisa de número **par** de pontes. Em Königsberg, as quatro regiões tinham número ímpar (5, 3, 3, 3). Impossível.
- A impossibilidade **não é empírica**: não se testou nenhuma rota. É estrutural. Nenhuma quantidade de tentativas teria "descoberto" isso — mas uma pessoa insistente poderia passar a vida tentando.
- Isto inaugura a teoria dos grafos (arquivo 04).

### 3.2. A fita de Möbius

`[H]` Descrita independentemente por Möbius e Listing em 1858 (MacTutor, "Möbius"; "Listing" — Listing também cunhou o termo "Topologie", 1847). Pegue uma tira de papel, dê meia-volta numa ponta e cole: a superfície resultante tem **um só lado e uma só borda**. Uma formiga andando pelo "meio" volta ao ponto de partida do "outro lado" sem cruzar a borda.
- **Não orientável** `[I]`: na fita, não existe distinção global entre "direita" e "esquerda". Uma mão direita desenhada que dê a volta completa retorna como mão esquerda. Localmente, em cada pedaço, existe direita e esquerda; **globalmente, não**.
- Cortar a fita ao meio pelo comprimento não produz duas fitas, mas uma fita mais longa com duas meias-voltas (e dois lados) `[H]`. Ou seja: a intuição de "cortar em dois" falha.

### 3.3. Invariantes: a fórmula de Euler e o genus

`[H]` Para qualquer poliedro convexo (cubo, pirâmide, dodecaedro), vértices − arestas + faces = 2 (Euler, carta a Goldbach de 1750, publicação 1758). O cubo: 8 − 12 + 6 = 2. Esse número (a *característica de Euler*) não depende do formato, só da topologia: para uma superfície com *g* buracos, vale 2 − 2g (MacTutor; Richeson, *Euler's Gem*, 2008).
- **O que é um invariante** `[I]`: um número ou propriedade que se calcula de várias maneiras e dá sempre o mesmo resultado, **por mais que se deforme o objeto**. Serve para provar que duas coisas são diferentes sem precisar examiná-las por completo: se os invariantes divergem, não há deformação que leve uma à outra.
- Limite: invariantes iguais **não** garantem que as coisas sejam iguais (há nós distintos com invariantes simples iguais) `[H]`.

### 3.4. Outros resultados com cara de lei do mundo

- **Teorema da bola cabeluda** `[H]`: não há como pentear os pelos de uma esfera sem deixar pelo menos um redemoinho/ponto calvo (Poincaré–Brouwer). Consequência popular: em qualquer momento, há pelo menos um ponto da Terra sem vento horizontal (idealização). No toro (rosca) é possível pentear sem redemoinho.
- **Teorema do ponto fixo de Brouwer** `[H]`: mexa o café numa xícara sem derramar (transformação contínua do disco em si mesmo): algum ponto acaba exatamente onde começou.
- **Teorema de Borsuk–Ulam** `[H]`: há sempre dois pontos antípodas na Terra com a mesma temperatura e pressão (idealização).
- **Teorema da curva de Jordan** `[H]`: uma curva fechada simples no plano divide-o em dentro e fora. Parece óbvio; a prova rigorosa é difícil — e **numa superfície como o toro, uma curva fechada pode não separar nada** (um círculo dando a volta no tubo do toro).

(Fontes gerais: Britannica, "topology"; MacTutor, "Topology enters mathematics". Enunciados padrão.)

## 4. O que muda quando se vê o mundo como relações

`[I]` em todo este bloco.

1. **A pergunta muda de "quanto?" para "o que se liga a quê?"** Uma tradição métrica pergunta tamanho, distância, peso; uma tradição topológica pergunta acesso, separação, vizinhança, laço. São perguntas diferentes e nenhuma reduz-se à outra.
2. **Impossibilidades estruturais ficam visíveis.** Königsberg e a bola cabeluda mostram coisas que não dá para fazer *por mais que se tente* — e não por falta de força ou habilidade. Uma tradição relacional sabe dizer "não adianta"; uma tradição métrica tende a tentar mais forte.
3. **Garantias de existência sem localização.** Brouwer garante que há um ponto fixo, mas não diz onde. Isto é um tipo estranho de conhecimento: saber que algo **está** sem saber **onde**.
4. **Local × global.** Na fita de Möbius e na esfera curva, o que vale em toda vizinhança pequena (há direita/esquerda; o espaço parece plano) **falha no todo**. Ver o mundo topologicamente é desconfiar de que o que é verdade em cada lugar seja verdade do conjunto.
5. **Robustez.** Propriedades topológicas sobrevivem a erros de medida e deformações. São boas para conhecimento transmitido mal, por mapas tortos, de memória — um mapa de metrô (o de Londres, Harry Beck, 1931–33 `[H]`) é topológico: mente sobre distâncias, acerta sobre conexões, e é por isso que funciona.
6. **O preço.** A topologia não sabe quão longe, quão grande, quão forte. Uma tradição puramente topológica saberia que dois lugares se ligam, não se a viagem dura uma hora ou um ano. Saberia que algo tem um buraco, não se cabe uma agulha ou um exército.
7. **Objetos viram classes de equivalência.** Para a topologia, "uma coisa" é tudo o que se pode deformar nela. A identidade passa do material e da forma para a estrutura de conexão. `[A]` Isso tem parentesco (apenas analógico, não identidade) com doutrinas que dizem que a identidade de algo é seu padrão de relações (Leibniz sobre relações; budismo sobre originação dependente — essas aproximações precisam ser tratadas com cautela, cf. decisão metodológica 2).

---

## Potencial ficcional

Todos `[C]` ou `[R]`. Nenhum destes é magia; são **maneiras de perceber e operar**.

- **Uma tradição de topólogos** `[R]` (Euler + Möbius + Leibniz *analysis situs*): pensa lugares, corpos e comunidades como tecidos de conexões. **Percebe** quando uma tarefa é estruturalmente impossível ("nenhum caminho atravessa cada ponte uma vez"), detecta onde há "buracos" que não se fecham por esforço local, e confia em mapas grosseiros. **Não percebe** magnitude, intensidade, perigo proporcional, custo. Pode concluir corretamente que dois reinos "estão ligados" e não saber que a ligação é um fio. Conflito natural com uma tradição métrica (agrimensores, engenheiros) que os acha vagos.
- **O problema local/global como experiência dramática** `[C]`: um viajante segue regras que valem em cada passo ("sempre mantenha o rio à direita") e retorna ao ponto de partida "espelhado" — o que era direita virou esquerda. Num mundo de fantasia sombria, uma região com propriedade de tipo Möbius não precisa de explicação sobrenatural: basta que o mundo (ou um lugar) tenha uma estrutura global que nenhuma observação local revela. **Cuidado**: é recurso de criação, não afirmação sobre o mundo real nem sobre as leis do mundo ficcional, que o autor ainda não definiu (pergunta aberta #20).
- **Curvatura invisível de dentro** `[R]` (Gauss/Riemann): um povo que mede com triângulos pequenos e jura que seu espaço é plano; outro, nômade, que percorre triângulos imensos e sabe que não é. Ambos têm evidência. Excelente para §4 (pressupostos evidentes de uma época).
- **Convenção × fato** `[R]` (Poincaré): uma escola que defende que a escolha de geometria é convenção — e por isso não pode ser refutada por nenhum experimento, porque sempre ajusta a física. Argon esbarra no limite: uma tradição que nunca erra porque nunca se arrisca.
- **Garantias sem localização** `[C]`: uma tradição que sabe provar que "há um ponto que não se move" ou "há um lugar sem vento" mas não sabe achá-lo. Seu saber é ao mesmo tempo seguro e inútil na prática — o que gera conflito com caçadores práticos que encontram o ponto por tentativa e não sabem que ele tinha de existir.
- **Invariantes como teste de identidade** `[C]`: em vez de perguntar "isto é o mesmo objeto?" pelo aspecto, perguntar "quantos buracos, quantos lados, quantas peças". Uma tradição assim reconhece o mesmo ser sob formas diferentes — e confunde seres diferentes que compartilham invariantes. **Ponto cego explícito**: invariantes iguais não garantem identidade.
- **Para Argon** `[C]`: aprender a esquecer de propósito. O gesto de Euler — jogar fora o que parece importante — é uma habilidade que se ensina e que vai contra a formação de qualquer tradição de substâncias e propriedades locais.

## Questões em aberto
- Se Gauss mediu o triângulo Brocken–Hohehagen–Inselsberg para testar a geometria do espaço: controverso.
- Datas do artigo de Euler (1735 apresentação / 1736 volume / 1741 impressão): fontes divergem só em qual data citar.
- Atribuições exatas de citações de Leibniz sobre *analysis situs*: não conferidas em fonte primária nesta rodada.

## Fontes consultadas
- Wikipedia, "Seven Bridges of Königsberg": https://en.wikipedia.org/wiki/Seven_Bridges_of_K%C3%B6nigsberg
- historyofinformation.com, Euler/Königsberg: https://historyofinformation.com/detail.php?id=3406
- Referências sem fetch: MacTutor ("Non-Euclidean geometry", "Topology enters mathematics", Möbius, Listing, Klein); SEP ("Nineteenth Century Geometry", "Poincaré", "Kant's Views on Space and Time", "Leibniz's Philosophy of Mathematics"); Britannica ("topology", "Erlangen program"); D. Richeson, *Euler's Gem* (2008).
