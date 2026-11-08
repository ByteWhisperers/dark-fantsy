---
titulo: Repertório de estruturas matemáticas e simbólicas (Frente 3)
tipo: pesquisa
camada: mundo
status: rascunho
fonte: pesquisa
atualizado: 2026-11-07
---

# Repertório de estruturas matemáticas e simbólicas

Entregável 3 da Pesquisa I (Frente 3 — Matemática, símbolos e formalização). Nada aqui é cânone; é matéria-prima. Etiquetas: `[H]` histórico (com fonte), `[I]` interpretação, `[A]` analogia, `[R]` recombinação, `[C]` criação original.

## Por que este repertório existe

Decisão metodológica 3 do documento-mãe: **matemática não pode entrar como decoração arcana**. A pergunta útil não é "que símbolo fica bonito", mas: *que operações esta formalização torna possíveis, quais torna impossíveis, e o que ela esconde de quem a usa?* `[I]` Escolher uma formalização é escolher uma percepção — com capacidades e cegueiras próprias.

## Índice

| Arquivo | Conteúdo |
|---|---|
| `01-signos-e-representacao.md` | §7.1: o que a notação torna perceptível, manipulável, o que perde; notações que "sabiam" mais que seus criadores (imaginários, Leibniz, zero, pauta musical, mapas) |
| `02-sistemas-antigos-de-calculo.md` | §7.2: base 60 babilônica, frações unitárias egípcias, Euclides/Eudoxo, varas chinesas, Índia (zero, Madhava), al-Khwarizmi |
| `03-geometria-e-topologia.md` | §7.3: euclidiana, não euclidiana, topologia (Königsberg, Möbius, genus, invariantes); objeto vs relação |
| `04-estruturas-relacionais.md` | grafos, sistemas dinâmicos e caos, teoria da informação, simetria/grupos/Noether |
| `05-sistemas-formais-e-limites.md` | §7.4: axiomas, Gödel, indecidibilidade, modelo vs realidade (Box), as 5 distinções |

## Tabela-repertório

Legenda de colunas: **representa** = o que a estrutura deixa ver; **calcula/transforma** = o que deixa fazer; **oculta** = o que não alcança ou distorce. As células "oculta" são `[I]`; os exemplos históricos são `[H]` (fontes nos arquivos indicados).

| Estrutura | O que permite representar | O que permite calcular/transformar | O que oculta ou não alcança | Exemplo histórico | Arq. |
|---|---|---|---|---|---|
| Notação posicional com zero | quantidades de qualquer tamanho com poucos sinais; o "nada" num lugar | algoritmos escritos de soma/multiplicação/divisão sem ábaco; perícia vira rotina | magnitude intuitiva (dígitos parecem iguais); o infinito das dízimas fica implícito | Brahmagupta (628) regras do zero; Bakhshali (datação disputada) | 01, 02 |
| Base 60 + tabelas de recíprocos | partilhas em muitos divisores; tempo e ângulo | dividir multiplicando pelo recíproco; aproximações de alta precisão (√2) | números "irregulares" (1/7); magnitude ambígua sem vírgula; prova geral | YBC 7289; efemérides selêucidas | 02 |
| Frações unitárias + duplicação | quantidades como porções entregáveis | partilha justa, verificação passo a passo | razão contínua abstrata; cálculo longo eficiente; generalização | Papiro Rhind, tabela 2/n (c. 1550 a.C.) | 02 |
| Proporção de Eudoxo / demonstração euclidiana | razões entre grandezas, inclusive incomensuráveis | provar que algo vale *sempre*; medir o inacessível por semelhança | negativos, álgebra numérica, dimensões > 3; separa número de grandeza | *Elementos* V; retomado por Dedekind (1872) | 02, 03 |
| Varas de contagem / prancha | coeficientes em colunas; positivo/negativo por cor | eliminação em sistemas lineares (*fangcheng*) | o estado do cálculo é efêmero; saber fica nas mãos | *Nove Capítulos*, cap. 8; Liu Hui (263) | 02 |
| Séries infinitas versificadas | funções (seno, arco-tangente) como somas sem fim | tabelas astronômicas de alta precisão | teoria geral de funções; difusão fora da linhagem | Madhava (c. 1340–1425) via *Yuktibhāṣā* | 02 |
| Álgebra retórica (al-jabr) | a equação como balança; problemas classificados por tipo | restaurar/balancear; resolver as 6 formas | soluções negativas; cúbicas; generalidade simbólica | al-Khwarizmi (c. 820) | 02 |
| Notação de Leibniz (dx, ∫) | taxa de mudança e acumulação como "frações" e "somas" | regra da cadeia e mudança de variável quase automáticas | o que um infinitesimal *é* (ficou obscuro ~150 anos) | ∫ em manuscrito de 29/10/1675 | 01 |
| Números imaginários/complexos | raízes "impossíveis"; depois, rotações no plano | atravessar o impossível para chegar a resultados reais | por 250 anos, o próprio referente | Cardano 1545; Bombelli 1572; Argand 1806 | 01 |
| Coordenadas cartesianas | curvas como equações | traduzir problemas visuais em cálculo e vice-versa | qualidades não numéricas; escolha de origem/eixos é arbitrária | Descartes, *La Géométrie* (1637) | 01 |
| Mapas e projeções | território em plano reduzido | rumos constantes (Mercator), áreas iguais (outras) — nunca tudo | toda projeção distorce algo (teorema de Gauss) | Mercator (1569); mapa do metrô de Londres (1931–33) | 01, 03 |
| Notação musical (pauta) | altura e duração com precisão | reproduzir música a distância, sem mestre presente | timbre, ornamentos, microtons, prática corporal | Guido d'Arezzo (c. 1025) | 01 |
| Tabelas e diários astronômicos | séculos de observação lado a lado | prever por periodicidade sem modelo causal | fenômenos raros; mudanças de regime; o "porquê" | Diários babilônicos (652 a.C.–séc. I a.C.) | 01 |
| Geometria não euclidiana | espaço com forma própria (curvatura) | geometrias consistentes alternativas; espaço como questão empírica | invisível em pequena escala; exige grandes triângulos ou laços | Lobachevsky 1829, Bolyai 1832, Riemann 1854 | 03 |
| Topologia | conexão, buracos, lados, vizinhança | provar impossibilidades e existências estruturais; invariantes | distância, tamanho, intensidade, custo | Euler, Königsberg (1735/36); Möbius/Listing (1858) | 03 |
| Invariantes (característica de Euler, genus) | o que sobrevive à deformação | distinguir formas sem examiná-las inteiras | invariantes iguais não garantem identidade | V − A + F = 2 (Euler, 1750/58) | 03 |
| Grafos e redes | quem se liga a quem | caminhos, gargalos, pontos frágeis, hubs | qualidade/intensidade do vínculo; quem escolhe as arestas decide | Euler; Milgram (1967); Barabási–Albert (1999) | 04 |
| Sistemas dinâmicos / caos | estados e regras de transição; o "relevo" do possível | atratores, bifurcações, histerese; previsão qualitativa e estatística | previsão pontual de longo prazo; variáveis omitidas | Poincaré (1890); Lorenz (1963); May (1976) | 04 |
| Teoria da informação | incerteza e surpresa como quantidade | compressão; transmissão confiável com ruído via redundância | significado (por construção); relatividade ao observador | Shannon (1948) | 04 |
| Simetria e grupos | o que fica igual sob transformação | classificar padrões; explicar impossibilidades (Galois); simetria ↔ conservação | dissipação, assimetrias reais; idealização | Galois (†1832); Noether (1918); 17 grupos de padrões planos | 04 |
| Sistema formal axiomático | conhecimento como derivação a partir de princípios | provas mecânicas; vários modelos de um mesmo sistema | os próprios axiomas; adequação ao mundo | Euclides; Hilbert | 05 |
| Incompletude / indecidibilidade | os limites internos de qualquer sistema rico | saber o que *não* pode ser provado ou decidido | não diz nada sobre "razão em geral" (abuso comum) | Gödel (1931); Tarski; Turing (1936) | 05 |
| Modelo estatístico/científico | a realidade aproximada por estrutura simplificada | previsão; teste de hipóteses; parcimônia | o que ficou fora vira "ruído"; reificação | Box (1976; 1987) | 05 |

## Achados transversais `[I]`

1. **A regra muitas vezes vem antes da ontologia.** Imaginários, infinitesimais, equações de Maxwell dentro do éter: o formalismo funcionou décadas ou séculos antes de alguém saber "o que" ele denotava. É a premissa central da Pesquisa I vista do lado matemático.
2. **Toda formalização escolhe o que esquecer.** Euler resolveu Königsberg jogando fora formas e distâncias; Mercator salva ângulos e perde áreas; Shannon descarta o significado. A potência vem do esquecimento — e a cegueira também.
3. **Impossibilidades estruturais são um tipo de conhecimento.** Königsberg, quíntica (Galois), bola cabeluda, Gödel, problema da parada: saber que *não adianta tentar* é algo que só a formalização dá — e que tradições puramente técnicas não alcançam.
4. **Local ≠ global.** Curvatura e não orientabilidade são invisíveis de perto. Uma tradição que só verifica localmente pode estar certa em todo lugar e errada sobre o todo.
5. **Determinismo ≠ previsibilidade**; **consistência ≠ verdade**; **provar ≠ observar ≠ realizar**. As cinco distinções de §7.4 se separam em casos históricos concretos (tabela no arquivo 05).
6. **O meio de cálculo molda o saber.** Prancha (efêmera, gestual), tabela (agregada, sem porquê), verso (memorizável, opaco a estrangeiros), papel posicional (democratizante). A forma física da notação define quem pode saber e como o saber se perde.
7. **Semelhança de forma às vezes é profunda, às vezes é ilusória.** Universalidade de Feigenbaum (formas iguais, mecanismos diferentes, semelhança real) vs. epiciclos ≈ Fourier (analogia que não autoriza dizer que Ptolomeu "fazia Fourier").

## Limites desta entrega
- Foco ocidental-erudito nos séculos XVIII–XX nos arquivos 03–05; matemáticas de tradições orais, africanas e ameríndias (ex.: quipus andinos, padrões de *sona* angolanos, calendário maia) **não foram cobertas** — lacuna a preencher numa rodada futura.
- Várias referências foram citadas a partir de conhecimento de referência sem refetch online; cada arquivo lista o que foi e o que não foi verificado.
- Nada aqui define magia, círculos ou regras (§15). Ligação a círculos mágicos fica para a Pesquisa II.
