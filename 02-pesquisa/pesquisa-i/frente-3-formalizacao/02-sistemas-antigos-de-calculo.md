---
titulo: Sistemas antigos de cálculo — como cada um permitia operar sobre o mundo
tipo: pesquisa
camada: mundo
status: rascunho
fonte: pesquisa
atualizado: 2026-11-07
---

# Sistemas antigos de cálculo

Foco de §7.2: não "quem descobriu o quê primeiro", mas **o que cada sistema tornava fácil, o que tornava difícil, e que tipo de mundo ele deixava operar**. Etiquetas `[H]` `[I]` `[A]` `[R]` `[C]`.

Aviso de §6.2: "babilônios", "egípcios", "indianos" aqui são atalhos. Cada item indica período e tipo de praticante (escriba, astrônomo, funcionário). A maior parte dessa matemática era de **especialistas administrativos**, não de filósofos.

---

## 1. Mesopotâmia: base 60 posicional e tabelas

**O sistema** `[H]`. Desde o período paleobabilônico (c. 2000–1600 a.C.), escribas usavam numeração **sexagesimal posicional**: só dois sinais em cunha (um para 1, um para 10), combinados até 59; a posição dava o peso (×60, ×3600...). Durante muito tempo não houve zero, nem marca da "vírgula": o mesmo registro podia significar 2, 120 ou 2/60, e o contexto decidia. Um sinal de lugar vazio aparece só no período selêucida (fim do 1º milênio a.C.) e não ao final do número (MacTutor, "Babylonian numerals"; Robson, *Mathematics in Ancient Iraq*, 2008).

**O que a base 60 facilitava** `[H]`/`[I]`:
- 60 tem muitos divisores (2, 3, 4, 5, 6, 10, 12, 15, 20, 30). Divisões por esses números dão "frações redondas". Isso importa para partilhas, rações, salários.
- **Dividir = multiplicar pelo recíproco**: os escribas tinham tabelas-padrão de recíprocos dos números "regulares" (os que só têm 2, 3 e 5 como fatores). Dividir por 7 era um problema; não existe recíproco finito — e as tabelas simplesmente o omitiam ou anotavam como impossível `[H]` (Robson 2008).
- A ausência de vírgula é uma **vantagem operacional**: trabalha-se com a mantissa e decide-se a magnitude no fim (como uma régua de cálculo) `[I]`.

**Exemplo: YBC 7289** `[H]`. Pequena tábua escolar paleobabilônica com um quadrado e suas diagonais; na diagonal, 1;24,51,10 (= 1 + 24/60 + 51/3600 + 10/216000 ≈ 1,41421296), aproximação de √2 com erro na ordem de 6 milionésimos; ao lado, 30 e 42;25,35 (a diagonal de um quadrado de lado 30). O método de cálculo é desconhecido (CDLI wiki, "80. square root of two": https://cdli.ox.ac.uk/wiki/80._square_root_of_two; Fowler & Robson, *Historia Mathematica* 25, 1998). `[I]` Note: o valor é tratado como coeficiente utilizável (multiplica-se pelo lado), não como objeto metafísico — nada aqui indica a noção grega de "incomensurável".

**Plimpton 322** `[H]`: tábua com colunas de números que correspondem a ternos pitagóricos. A interpretação é disputada: Robson (2001/2002) lê como exercício de professor gerado a partir de pares de recíprocos; Mansfield & Wildberger (*Historia Mathematica*, 2017) leem como tabela trigonométrica baseada em razões, o que outros historiadores criticam por depender de reconstrução da parte quebrada (Discover/Smithsonian, cobertura; resumo via busca). **Controvérsia aberta.** Lição `[I]`: o mesmo artefato pode ser lido como sala de aula ou como instrumento sofisticado — o leitor moderno projeta sua matemática.

**Astronomia matemática selêucida** `[H]`: calculavam posições lunares e planetárias com **funções em zigue-zague e em degraus** (sequências aritméticas que sobem e descem), sem modelo geométrico do céu (Neugebauer 1957; Britannica, "Babylonian astronomy"). Um estudo de 2016 (Ossendrijver, *Science*) mostrou que tábuas babilônicas calculavam a posição de Júpiter pela área sob uma curva velocidade×tempo, um procedimento trapezoidal `[H]` (verificação por memória; não refeita online nesta rodada).

**Como operava sobre o mundo** `[I]`: o mundo é **tabela + procedimento**. Não se pergunta "por que", pergunta-se "qual a sequência de passos que dá o número". Isso gera previsões impressionantes sem ontologia geométrica — e liga-se aos presságios: o céu é texto a ser lido.

**Pontos cegos**: números não regulares; problemas sem procedimento-modelo; demonstração geral (o conhecimento vem em exemplos resolvidos, não em teoremas) `[I]`.

## 2. Egito: frações unitárias e duplicação

**O sistema** `[H]`. Numeração hieroglífica/hierática decimal **não posicional** (um sinal para 1, 10, 100...). Multiplicação por **duplicação sucessiva** e soma: para 13 × 7, duplica-se 7 (7, 14, 28, 56), escolhem-se as linhas que somam 13 (1+4+8) e soma-se 7+28+56 = 91. Frações, salvo 2/3 (e em alguns contextos 3/4), eram expressas como **soma de frações unitárias distintas** (1/n) (MacTutor, "Egyptian mathematics"; Imhausen, *Mathematics in Ancient Egypt*, 2016).

**Papiro Rhind** `[H]`: copiado pelo escriba Ahmes c. 1550 a.C. a partir de original mais antigo (Reino Médio, segundo o próprio colofão); começa com a **tabela 2/n** para n ímpar de 3 a 101, decompondo cada 2/n em no máximo 4 frações unitárias (ex.: 2/5 = 1/3 + 1/15). Os critérios de escolha das decomposições permanecem sem explicação consensual (Joyce, Clark Univ.: https://mathcs.clarku.edu/~djoyce/ma105/2byn.html; Wikipedia, "Rhind Mathematical Papyrus").

**O que isso facilitava** `[I]`: **partilha física**. "Divida 9 pães entre 10 homens" (problema do Rhind): cada um recebe 2/3 + 1/5 + 1/30 de pão — o que pode ser *cortado e entregue* literalmente. As frações unitárias são uma matemática de **porções**, não de razões abstratas. Também a duplicação só exige saber dobrar e somar: robusta, verificável, ensinável.

**Geometria aplicada** `[H]`: área do círculo como (8/9 do diâmetro)², equivalente a π ≈ 3,16; volume do tronco de pirâmide exato no Papiro de Moscou (problema 14). Unidades como o *seked* (inclinação de pirâmide: deslocamento horizontal por côvado de altura) (MacTutor; Imhausen 2016).

**Como operava sobre o mundo**: rações, impostos, construção, celeiros. O conhecimento é **receita com verificação** ("faça assim; confira assim") `[H]` — os papiros trazem provas reais de que a resposta funciona, não demonstrações gerais.

**Pontos cegos** `[I]`: generalização (cada problema é um caso); razões como objetos; complexidade crescente — frações unitárias ficam penosas em cálculos longos (astronomia egípcia não desenvolveu a predição numérica babilônica; isso é comparação comum, mas a causa é interpretação).

## 3. Grécia: geometria demonstrativa e a teoria das proporções de Eudoxo

**A virada** `[H]`/`[I]`: nos *Elementos* de Euclides (c. 300 a.C.), conhecimento matemático = **demonstração a partir de definições, postulados e noções comuns**. Não basta funcionar; é preciso *provar que deve funcionar sempre*.

**A crise da incomensurabilidade** `[H]`: em algum momento antes de Platão, descobriu-se que a diagonal e o lado de um quadrado não têm medida comum (não há unidade, por menor que seja, que caiba um número inteiro de vezes em ambos). A atribuição a Hipaso e as lendas de punição são tardias e duvidosas (SEP, "Pythagoreanism"; MacTutor, "Hippasus"). Contraste com YBC 7289: o babilônio *usa* um valor aproximado; o grego descobre que **nenhum** valor exato em razão de inteiros existe — e isso vira problema filosófico `[I]`.

**Eudoxo de Cnido** (séc. IV a.C.) `[H]`: teoria das proporções preservada no Livro V dos *Elementos*. Em linguagem acessível: duas razões a:b e c:d são "a mesma" se, **para quaisquer múltiplos** que se tome, a comparação (maior/igual/menor) entre os múltiplos de a e b for sempre a mesma que entre os de c e d. Isso define igualdade de razões **sem precisar de um número** que as meça — funciona para incomensuráveis. Richard Dedekind (1872) reconheceu que sua construção dos números reais ("cortes") retomava essa ideia `[H]` (MacTutor, "Eudoxus"; SEP, "Dedekind's Contributions to the Foundations of Mathematics"). Eudoxo também deu o "método da exaustão" para áreas e volumes, usado por Arquimedes `[H]`.

**O preço** `[I]`: para contornar o incomensurável, a matemática grega clássica separou **número** (inteiros, discretos) de **grandeza** (contínua, geométrica). Álgebra foi feita como geometria (o "produto" de dois segmentos é um retângulo; três segmentos, um sólido; quatro, nada). Isso tornou tudo rigoroso e, ao mesmo tempo, travou a álgebra numérica geral por séculos. O rigor tem custo.

**Como operava sobre o mundo**: arquitetura, astronomia geométrica (esferas e epiciclos), óptica, mecânica de Arquimedes (alavanca, flutuação). O mundo é **forma e proporção**.

**Pontos cegos** `[I]`: quantidades sem forma (dívida, negativos), dimensões acima de 3, cálculo numérico rotineiro (gregos usavam sexagesimal babilônico na astronomia — Ptolomeu o faz `[H]`).

## 4. China: varas de contagem, posição na prancha e matrizes

**O sistema** `[H]`: **varas de contagem** (bambu, osso) dispostas numa superfície em colunas posicionais decimais, com orientação alternada vertical/horizontal entre posições vizinhas para evitar confusão; casa vazia = espaço em branco. Varas **vermelhas para positivos, pretas para negativos** (Wikipedia, "Counting rods"; Martzloff, *A History of Chinese Mathematics*, 1997).

**Os Nove Capítulos sobre a Arte Matemática** (*Jiuzhang suanshu*), compilação de camadas com redação principal em torno do séc. I d.C., comentada por Liu Hui (263 d.C.) `[H]` (Wikipedia, "The Nine Chapters..."; Chemla & Guo Shuchun, *Les neuf chapitres*, 2004). O capítulo 8, *fangcheng*, resolve sistemas de várias equações lineares dispondo os coeficientes em **colunas na prancha** e eliminando por operações entre colunas — essencialmente o que no Ocidente se chamou eliminação de Gauss `[H]`. É também o primeiro texto com **regras explícitas de sinais** (somar e subtrair "quantidades de cores diferentes") `[H]` (Retrospect Journal, "Fangcheng Procedure Revisited": https://retrospectjournal.com/?p=2906).

**O que a prancha permitia** `[I]`: a notação **não é escrita: é um arranjo físico manipulável**. O cálculo é uma coreografia de mãos; o texto descreve o procedimento, a prancha guarda o estado. Isso torna natural pensar em **tabelas de coeficientes como objeto** (a matriz) muito antes da álgebra simbólica. E números negativos aparecem não por especulação ontológica, mas porque o procedimento os produz no meio do caminho e é preciso continuar `[I]`.

**Como operava sobre o mundo**: problemas de administração imperial — agrimensura, impostos proporcionais, trabalho em obras, misturas de grãos `[H]`.

**Pontos cegos** `[I]`: o estado do cálculo é efêmero (desfeito ao terminar); conhecimento fica nos procedimentos e nos comentadores; ênfase em algoritmo correto e generalizável (Liu Hui justifica procedimentos), mas não no estilo axiomático euclidiano — o que **não** significa ausência de prova (Chemla insiste nisso) `[H]`.

## 5. Índia: zero, notação decimal e séries infinitas

**Zero e posição** `[H]`: a notação decimal posicional com zero se consolida na Índia na segunda metade do 1º milênio d.C.; Brahmagupta (628) dá regras de operação com zero e com "fortunas" (positivos) e "dívidas" (negativos) — algumas delas (divisão por zero) problemáticas `[H]` (MacTutor, "Brahmagupta"). Esse sistema chega ao mundo islâmico (al-Khwarizmi escreveu sobre ele) e daí à Europa (Fibonacci, *Liber Abaci*, 1202) `[H]`.

**Madhava de Sangamagrama** (c. 1340–1425) e a escola de Kerala `[H]`: séries infinitas para arco-tangente, seno e cosseno, e uma série para π (π/4 = 1 − 1/3 + 1/5 − 1/7 + ...), com termos de correção para acelerar a convergência. Nenhuma obra matemática de Madhava sobrevive com esses resultados; eles são conhecidos via discípulos, especialmente o *Yuktibhāṣā* de Jyeṣṭhadeva (c. 1530, em malaiala), que traz derivações em prosa (Wikipedia, "Kerala school"; Plofker, *Mathematics in India*, 2009). A série do arco-tangente é hoje chamada às vezes de Madhava–Gregory `[H]`. Transmissão a Europa: **sem evidência sólida** `[H]` (consenso cauteloso; propostas de transmissão via jesuítas são especulativas).

**O que isso permitia** `[I]`: cálculo de tabelas de senos de altíssima precisão para astronomia. A tradição é **versificada**: resultados em sânscrito métrico, números em sistemas como *bhūtasaṃkhyā* (palavras-objeto valem dígitos: "olhos" = 2, "lua" = 1) `[H]` (Plofker 2009). A memória poética é parte do aparato de cálculo.

**Pontos cegos** `[I]`: a ênfase astronômica e o meio de transmissão (comentário, linhagem de mestres) mantiveram o resultado local; não houve generalização para uma teoria de funções.

## 6. Al-Khwarizmi: álgebra como procedimento de equilíbrio

**A obra** `[H]`: *al-Kitāb al-mukhtaṣar fī ḥisāb al-jabr wa'l-muqābala* (c. 820, Bagdá, Casa da Sabedoria). Todo o texto é **retórico**: sem símbolos, números escritos por extenso, incógnita como "coisa" (*shay'*), seu quadrado como "riqueza/bem" (*māl*). Reduz todos os problemas lineares e quadráticos a **seis formas-padrão** (ex.: "quadrados iguais a raízes", "quadrados e raízes iguais a números") e resolve cada uma com procedimento e **justificativa geométrica** (completar o quadrado desenhado) (DSB, verbete "Al-Khwārizmī", hospedado no MacTutor: https://mathshistory.st-andrews.ac.uk/DSB/Al-Khwarizmi.pdf).
- *al-jabr* = "restauração": tirar um termo subtraído de um lado e somá-lo ao outro; *al-muqābala* = "balanceamento": cancelar termos iguais dos dois lados `[H]`. O nome "algoritmo" deriva de seu nome latinizado `[H]`.
- Por que seis formas? Porque não havia coeficientes negativos nem zero como coeficiente: "x² + 10 = 7x" e "x² = 7x + 10" são **problemas diferentes**, não o mesmo com sinais trocados `[I]`.

**O que isso permitia** `[I]`/`[H]`: resolver problemas de herança islâmica (partilha legal com frações complexas), comércio, agrimensura — boa parte do livro é aplicação jurídica. A grande novidade conceitual: a **equação** como objeto, classificável por tipo, sobre o qual se age por transformações que preservam o equilíbrio.

**Pontos cegos**: soluções negativas descartadas; raízes de cúbicas fora de alcance (Omar Khayyam, séc. XI, resolve cúbicas geometricamente por interseção de cônicas) `[H]`.

---

## Síntese comparativa `[I]`

| Sistema | Unidade de pensamento | Força | Cegueira |
|---|---|---|---|
| Babilônico | tabela + procedimento | previsão numérica, aproximação | demonstração geral, números "irregulares" |
| Egípcio | porção partilhável | verificação, justiça distributiva | generalização, razão abstrata |
| Grego (Euclides/Eudoxo) | grandeza e prova | rigor, incomensurável | álgebra numérica, negativos |
| Chinês (varas) | arranjo manipulável | sistemas lineares, negativos | registro permanente do estado |
| Indiano (Kerala) | série e verso | precisão astronômica, infinito | difusão, teoria geral |
| al-Khwarizmi | equação como balança | classificação de problemas | soluções negativas, cúbicas |

---

## Potencial ficcional

- **A ordem dos recíprocos** `[R]` (Babilônia): uma tradição que só sabe dividir por "números regulares". Para ela certas partilhas são literalmente **impossíveis** e por isso tabu — há números "impuros" (os primos 7, 11, 13...). Percebe muito bem ciclos e ritmos comensuráveis; falha diante de qualquer fenômeno cujo período seja "irregular". `[C]` Uma heresia: um calculista que aproxima 1/7 e mostra que funciona "bem o suficiente".
- **Cortadores de pão** `[R]` (frações unitárias): uma tradição em que toda quantidade se pensa como soma de porções entregáveis. Excelente em justiça distributiva e em verificar; incapaz de pensar uma razão contínua (uma grandeza "entre" porções lhe parece inexistente).
- **Geômetras do incomensurável** `[R]` (Eudoxo): um grupo para quem a descoberta de que certas razões não têm medida comum foi trauma fundador. Tratam o incomensurável com rigor (definem igualdade sem número) e por isso desprezam calculistas aproximadores — e perdem a eficácia prática destes. Conflito clássico rigor × uso.
- **A prancha vermelha e preta** `[R]` (varas chinesas): conhecimento que existe só *durante* a operação, como arranjo físico. Os mestres sabem fazer o que não sabem escrever. Quando a prancha é desfeita, o saber some. Argon pode aprender olhando as mãos, não lendo — conecta-se a §8 (conhecimento tácito).
- **Versos que calculam** `[R]` (Kerala): números codificados em palavras-imagem; um poema é também uma tabela. Um estrangeiro lê como poesia religiosa e não percebe que está diante de uma tabela de senos — ótimo para mal-entendidos de tradução (§5.1 e decisão metodológica 2).
- **Restauração e balanceamento** `[R]` (al-jabr): uma tradição jurídica que vê todo conflito como desequilíbrio a restaurar movendo termos de um lado para o outro. Seis tipos canônicos de disputa; o que não se reduz a um deles "não é caso".

## Questões em aberto
- Plimpton 322: leitura disputada.
- Datação dos Nove Capítulos (camadas de séc. X a.C.–II d.C. segundo diferentes fontes): imprecisa.
- Ossendrijver 2016 (Júpiter, área sob curva): citado de memória.
- Transmissão Kerala → Europa: especulativa, não usar como fato.

## Fontes consultadas
- CDLI, YBC 7289: https://cdli.ox.ac.uk/wiki/80._square_root_of_two
- Wikipedia, "YBC 7289": https://en.wikipedia.org/wiki/YBC_7289
- Joyce, "The Egyptian 2/n table": https://mathcs.clarku.edu/~djoyce/ma105/2byn.html
- DSB "Al-Khwārizmī" (MacTutor): https://mathshistory.st-andrews.ac.uk/DSB/Al-Khwarizmi.pdf
- Retrospect Journal, fangcheng: https://retrospectjournal.com/?p=2906
- Wikipedia, "Nine Chapters", "Counting rods", "Kerala school", "Rhind Mathematical Papyrus" (secundárias)
- Cobertura de Plimpton 322: https://www.smithsonianmag.com/smart-news/origins-trigonometry-may-lie-ancient-tablet-180964640/
- Referências sem fetch: Robson 2008; Imhausen 2016; Martzloff 1997; Chemla & Guo 2004; Plofker 2009; Neugebauer 1957; MacTutor (Eudoxus, Brahmagupta, Babylonian numerals, Egyptian mathematics); SEP (Pythagoreanism; Dedekind).
