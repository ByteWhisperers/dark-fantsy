---
titulo: P1 · Reino de Tracton — dossiê principal
tipo: povo
camada: mundo
status: rascunho
fonte: conto + adendo autoral (2026-11-09) + inventado (propostas marcadas)
atualizado: 2026-11-09
---

# P1 · Reino de Tracton — dossiê principal

Primeira sociedade-piloto do [ciclo piloto](../00-ciclo-piloto-proposta.md), no formato do §5.2 do [protocolo](../../00-fontes/protocolo-povos-continente.pdf). Revisado com o [adendo autoral](../../00-fontes/adendo-autoral-tracton-p1.txt) (entregável A).

**Como ler:**
- `> 📜 Adendo` = decisão do Hermes, registrada no CANONE (#14–#21). Vale como cânone de trabalho.
- `> 📜 Conto` = o que o conto diz, com a linha de `00-fontes/conto-cronicas-de-argon.txt`. É evidência narrativa, não cânone automático (pergunta #4).
- `> 💡` = proposta do Claude. Pode morrer.
- `> ❓` = lacuna ou contradição (vai para `PERGUNTAS-ABERTAS.md`).

**Documentos deste piloto:**
| # | Documento | Entregável do adendo |
|---|---|---|
| 00 | este dossiê | A |
| 01 | [arquitetura institucional e casos de teste](01-arquitetura-institucional.md) | B |
| 02 | [matriz de diversidade interna](02-matriz-diversidade-interna.md) | C |
| 03 | [esboço histórico](03-esboco-historico.md) | D |
| 04 | [relações locais do Tier 1](04-relacoes-locais-tier1.md) | E |
| 05 | [registro de status](05-registro-de-status.md) | F |
| 06 | [relações regionais do Tier 2](06-relacoes-regionais-tier2.md) | extra, pedido pelo CANONE #30–#31 |

**Recorte de tempo (CANONE #29):** três momentos: **formação**, **primeira vida de Argon** (primeiro conto) e **início do segundo conto**, ~300 anos depois (CANONE #10). Este dossiê descreve sobretudo Tracton **no tempo do primeiro conto**; o que mudou ao longo dos séculos, e o reino do segundo conto (o mesmo, maior e mais estruturado, CANONE #25), está no [esboço histórico](03-esboco-historico.md). Nada da primeira vida se presume inalterado na segunda. **Escalas (CANONE #30):** 1ª vida do Tier 1 ao Tier 2; 2ª vida começa no Tier 1 e termina em ponto indefinido.

---

## Resumo em uma frase
> Tracton é um reino humano medieval, feudal e culturalmente heterogêneo, cuja Coroa e cuja Igreja monoteísta aspiram à expansão, mas esbarram em limites administrativos, territoriais e políticos. A magia é capacidade real com peso militar, controlada por instituições que também reproduzem privilégio aristocrático; pólvora anã, tráfico, mercados clandestinos, magia irregular e cultos minoritários persistem apesar das restrições. (Síntese do adendo.)

---

## A. Identidade e delimitação

> 📜 Adendo (CANONE #14): **Reino de Tracton**, nome de trabalho. Predominantemente humano, medieval e feudal, extenso, com senhorios subordinados. **Não é império**, mas a Coroa tem **aspirações imperiais**. A população é heterogênea; **súdito do rei ≠ identidade tractoniana**. Categorias analíticas a investigar: territórios de **formação tractoniana**, territórios **incorporados** e senhorios de **fidelidade instável**.

> 📜 Conto: Coroa, rei, **Alta Capital**; "grandes cidades portuárias" no plural (l. 1147); Vallenar "no norte" (l. 1418); "Diocese do Norte" (l. 1859). A cidade portuária de Argon segue **sem nome** (pergunta #7).

> 📜 Adendo (CANONE #18, #19): **anões** fornecem pólvora e metalurgia, com origem e política opacas; **Altos Elfos** vivem num arquipélago distante. Ambos aparecem em Tracton como estrangeiros.

> 💡 Três identidades que não coincidem, a testar na [matriz de diversidade](02-matriz-diversidade-interna.md): a **política** (súdito da Coroa), a **cultural** (tractoniano do núcleo × regiões incorporadas) e a **religiosa** (fiel da Igreja × cultos locais). Ex.: um camponês de um senhorio incorporado pode ser súdito, não se dizer tractoniano e ir à missa por obrigação enquanto mantém o culto doméstico dos avós.

## B. Condições materiais e ambientais

> 📜 Conto: porto com docas, baleeiros do norte que compram meninos órfãos (l. 37–39), caravelas para as **colônias do sul** (vinho; Maren), tráfico de ópio e lótus. Cidade com granito branco, pedreira, moinho. **Fronteira**: Vallenar, "terras frias e lamacentas", serra, **minas de ferro e pedágios de rio** disputados por barões (l. 1147–1150), mina de sal na divisa sul. Vallenar fica a **300 léguas da costa**.

> 📜 Adendo (CANONE #14, §4): a capacidade de governar **varia entre regiões e matérias**; fiscalização desigual não é necessariamente incompetência ou indiferença do rei.

> 💡 **Distância como custo de governo.** Uma légua tem ~5 a ~6,6 km conforme o padrão (`[M]`, a conferir). 300 léguas ≈ 1.500–2.000 km, ou **50 a 65 dias a pé** a ~30 km/dia (h/01, transversal #20). A Coroa governa barato onde há rio navegável, porto e estrada; na serra, governa por intermédio dos senhores. A Alta Capital soube do cerco de Oakhaven com **três anos** de atraso (l. 1412). O monopólio arcano segue a mesma geografia (ver [casos de teste](01-arquitetura-institucional.md#3-os-tres-casos-de-teste)).

> 💡 **Cadeia de suprimento arcano.** As Academias compram insumos de alquimistas, ferreiros e herboristas marginais (l. 215–254); o foco de cristal custa "um navio de guerra" e é rastreado (l. 769); elixires de infância usam lótus branco (l. 1409). O controle recai sobre **treino, certificação e uso**, menos sobre **materiais**. Quem fornece entende a parte material e fica fora da teoria: foi a brecha de Argon.

> 📜 Adendo (CANONE #20): há **tráfico de substâncias** com usos recreativos, medicinais, alquímicos e talvez arcanos, sem organização única. A investigar: origem, extração, refino, rotas, mercados legais e ilegais, autoridades, dependência econômica. 💡 O lótus é o caso-piloto: o **lótus branco** entra nos elixires da elite (legal?) e o **lótus azul** vicia no porto (ilegal?). Mesma planta ou família de plantas, dois mercados. ❓ Pergunta #27.

## C. Organização social

> 📜 Conto: nobreza (Cidade Alta, liteiras; aprendizes nobres, l. 345), **famílias de sangue desperto** registradas há pelo menos 80 anos (l. 1444), diplomados, guildas (Guilda Real dos alquimistas), plebe portuária, submundo (gangues, cortiços), camponeses de fronteira, soldados e mercenários, clero.

> 📜 Adendo (CANONE #16): vida civil **familiar às sociedades medievais europeias de matriz judaico-cristã**: família, casamento, herança, obrigações religiosas, festas, reputação, autoridade comunitária. Tracton **não é permanentemente miserável**: há trabalho, comércio, afeto, prosperidade e instituições úteis.

> 📜 Adendo (CANONE #20): **a escravidão não é instituição jurídica** em Tracton, mas há **tráfico de pessoas**, inclusive de súditos capturados no próprio reino: crianças pobres, estrangeiros, vulneráveis. A venda de meninos aos baleeiros e o cativeiro de Lyra são parte disso. Distinguir proibição jurídica, prática clandestina, tolerância, fiscalização, corrupção e coerção real; **não fixar uma política uniforme de cumplicidade**.

> 📜 Conto: outras dependências visíveis: corpos de **condenados à forca** entregues por contrato a uso privado (Henrik e Argon, l. 1229, 1371); trabalho assalariado precário (Marta, lavadeira, morta aos 26).

> 💡 **Linhagem arcana como estrato dentro da nobreza.** Nem todo nobre é conjurador; o registro de nascimento das famílias de sangue desperto é documento de pertencimento. Nobres sem dom **compram** serviço arcano (Henrik e o Mestre Julian), o que cria hierarquia entre casas. Pelo adendo (CANONE #17), isto **não** pressupõe que a hereditariedade seja irrelevante: as linhagens podem de fato importar e, ainda assim, a teoria oficial ser insuficiente.

> ❓ Gênero: o conto não mostra maga, sacerdotisa nem nobre mulher em posição de poder. Lacuna, não conclusão.

## D. Organização política

> 📜 Adendo (CANONE #14, §2 e §4): **autoridade fragmentada**. Um barão obedece em umas matérias e resiste em outras; senhorios entraram por conquista, herança, casamento ou acordo; lealdade não é permanente nem nacional. A Coroa **quer** centralizar, mas não tem capacidade administrativa para impor-se em todo lugar. Mecanismos possíveis (registros, fisco, padronização jurídica, forças régias, controle de tecnologias estratégicas, representantes da Coroa) **não** são instituições consolidadas por padrão.

> 📜 Conto: Coroa, **Conselho** (l. 1442), **interdito real** (l. 1421), **Círculo de Estudos Arcanos** com **Quatro Câmaras**, **quatro Academias Reais** (l. 1414), **Guarda de Prata**, **caçadores da Coroa** (l. 1147), nobreza com tribunais próprios (l. 1229) e guerras privadas, Igreja com **Inquisição**, templários e Bispo Inquisidor.

> 📜 Conto, a lei da magia (Caldris, l. 1454–1457): conjuração **acima do primeiro círculo** por indivíduo **não auditado pela Coroa** é "**crime de risco público e heresia contra a Ordem da Trama**". Saídas legais: provar **mutação tardia de linhagem nobre** ou entregar **artefato da Era Antiga**, e "regularizar".

> 📜 Adendo (CANONE #17): a regulação tem origem **bélica, política e aristocrática**; um conjurador de baixa posição pode ameaçar tropas ou decidir conflitos. A Igreja pode apoiar o controle em nome da ordem. A lei do conto se mantém, **sem inferir** que o 1º círculo seja livre em toda localidade.

> 💡 O que a lei revela:
> 1. **O alvo é o poder de guerra.** O limite está no círculo que dá magia ofensiva de escala, não na magia em si (transversal #14, b/05). Localmente, o 1º círculo pode ser restringido por senhores, cidades ou Igreja.
> 2. **Irregular, não falso** (c/04). O conjurador sem registro não é negado: é irregular, e a primeira resposta oficial é **regularizar e absorver**.
> 3. **Dupla jurisdição.** O mesmo ato é **crime** (Coroa) e **heresia** (Igreja). Duas instituições têm motivo e direito de agir, e podem disputar quem julga.
> 4. **As saídas legais favorecem a nobreza.** "Mutação tardia de linhagem" é porta aberta para casas nobres e fechada para o plebeu (caso C dos [testes](01-arquitetura-institucional.md#3-os-tres-casos-de-teste)).

A distribuição de autoridade entre essas instituições, com alternativas, está na [arquitetura institucional](01-arquitetura-institucional.md).

## E. Identidade cultural

> 📜 Adendo (CANONE #16): família, casamento, herança, festas, reputação e costumes locais familiares ao medievo europeu judaico-cristão, com Igreja de identidade própria.

> 📜 Conto: veludo azul-real e foco de safira (Caldris); "manto azul" dos magos (l. 226); reverência de grau devida a um Magíster (l. 1425); escribas juramentados, atas, selos de cera, contratos.

> 💡 **Cultura de documento.** A elite se legitima por **registro escrito** (genealogia verificável, atas, matrículas; transversal #13); o submundo e a fronteira operam por **palavra, reputação e força**. É eixo de identidade, não estética, e dá ao Tier 1 uma textura concreta: quem tem papel e quem não tem.

> ❓ Lacunas: línguas, calendário (o conto usa meses do nosso calendário), comida, festas, arquitetura, educação fora das Academias.

## F. Organização religiosa e espiritual

> 📜 Adendo (CANONE #15): a Igreja dominante é **monoteísta**: divindade de **ordem, justiça, autoridade, disciplina, estratégia, organização social e exercício legítimo da força**, guerreira mais próxima de Atena que de Ares, sem copiar. Sem nome, iconografia nem doutrina ainda. **Universalizante**: uma ordem justa pode ou deve alcançar outras comunidades. A crença **não prova** que seja a única entidade divina. Igreja e Coroa **cooperam e competem** (jurisdições, propriedades, nomeações, receitas, legitimidade).

> 📜 Adendo (§15): existem cultos locais, tradições familiares, práticas domésticas, dissidências, especialistas independentes e grupos clandestinos. Alguns antecedem o reino; nem todos são políticos. O **Culto da Medula** é caso particular, não modelo. **Não inventar seitas** para povoar o cenário de antagonistas.

> 📜 Conto: Inquisição que **pericia relatórios** (l. 1414); templários; óleo e sal bentos; Igreja que tinha **anatomistas** (Orel, l. 794) e que **apagou o nome de Malakor**. Lyra jura "pelos Antigos" (l. 584), outra religião.

> 💡 **Uma divindade da força legítima explica a aliança com o controle arcano.** Se a deidade abençoa *o uso legítimo* da força, o problema teológico da magia irregular não é ser magia: é ser **força sem legitimidade**. Isso dá à Igreja motivo próprio para apoiar o registro, e também motivo para disputar com a Coroa **quem define o legítimo**. ❓ A "heresia contra a Ordem da Trama" (pergunta #25) pode ser o ponto em que as duas linguagens se encontram.

> 📜 **Capilaridade × poder (CANONE #26).** A Igreja está em quase todo o território (igrejas, paróquias, sacerdotes, sedes maiores), com capilaridade inspirada na Igreja medieval sem copiá-la. Mas **presença não é controle**: a paróquia influencia a comunidade sem força armada nem poder sobre o senhor; certos bispados e grandes sedes concentram patrimônio, diplomacia, jurisdição e, às vezes, poder político ou militar. Ver a tabela de níveis na [arquitetura institucional](01-arquitetura-institucional.md).

> 💡 **A Igreja produz conhecimento.** Anatomistas e peritos inquisitoriais sugerem uma instituição de **investigação** do corpo e do arcano, rival intelectual das Academias. Quem reprime arquiva o reprimido (b/05): o arquivo da Igreja pode guardar o que ela destruiu.

> 💡 **Apagar o nome** de uma entidade que depende de nome (transversal #2, a/03) é uma **técnica**, não só censura. Foi isso que reduziu Malakor (l. 1854). A Igreja sabe que funciona?

## G. Relação com a realidade arcana

> 📜 Conto, teorias do dom em disputa:
> | Quem | Teoria | Fonte |
> |---|---|---|
> | Círculo (Caldris) | linhagem, "harmonia sináptica", décadas de meditação guiada e elixires; plebeu tem "canais fechados" | l. 1474–1477 |
> | Argon | fisiologia e química dos nervos, que se pode forçar | l. 481 |
> | Lyra | dom de raça ("não foi feito pra sua raça") | l. 512–513 |
> | Igreja (inferido) | heresia "contra a Ordem da Trama"; Argon nega de antemão a explicação por "espírito de demônio" | l. 1456, 1470 |
> | Culto da Medula | dor e carne como via para a "Permanência" de Malakor | l. 800–857 |

> 📜 Adendo (CANONE #17): a teoria das linhagens pode legitimar privilégio, mas **não declarar a hereditariedade irrelevante** porque a teoria oficial é insuficiente. Evitar "eugenia" sem política reprodutiva deliberada. (Obs.: o narrador do conto usa "séculos de eugenia aristocrática", l. 1409; fica como voz do narrador, não como fato.)

> 💡 **Ontologia ≠ eficácia (§12 do protocolo).** A teoria do Círculo **funciona** (forma magos) e é **incompleta** (não explica Argon). A hereditariedade pode ter peso real, e a teoria pode ainda assim servir sobretudo a quem a ensina (§2.6).

> 💡 **Perfil arcano pelo §2.4** (provisório):
> | Dimensão | Avaliação |
> |---|---|
> | Amplitude | média: evocação, proteção, contenção, levitação; pouco sobre consciência e alma |
> | Precisão | alta dentro do currículo |
> | Transmissão | escolar, escrita, filtrada por genealogia; ao lado, ensino clandestino (adendo §8) |
> | Acesso social | muito restrito no oficial; desigual no irregular |
> | Infraestrutura | cara: focos, elixires, academias |
> | Escala | baixa: poucos magos, cada um muito caro |
> | Compreensão ontológica | baixa, com teoria forte |
> | Inovação | baixa no oficial; o irregular inova por necessidade |

> 📜 Adendo (CANONE #18): **pólvora** com uso militar: bacamartes, pistolas de um tiro, artilharia, explosivos, armas de cerco. Cara, lenta (≈30 s de recarga), não substitui espada, lança ou arco. Anões podem ter armas melhores que as vendidas.

> 📜 **Pólvora (CANONE #28):** é **mais barata** que formar um mago e, em certas condições, pode superar o guerreiro convencional. **Preços e custos completos estão em aberto** (pergunta #34). Limites: recarga lenta, dependência de recursos e conhecimento técnico. **Não é sempre superior à magia.**

> 💡 **Pólvora × mago de guerra, sem números.** Ambos permitem a poucos matar à distância. O mago se **forma** (sangue, escola, registro, tempo); a pólvora se **adquire** (com acesso aos anões). Para a Coroa, controlar um é controlar treino e certificação; controlar o outro é controlar **abastecimento** de fornecedores opacos. Qual compensa depende do objetivo militar e das condições (cerco, campo aberto, abastecimento), não de uma tabela de preços que ainda não existe.

> ⚙️ 5e: círculos ≈ níveis de magia. Magíster da Quarta Câmara e mago de batalha parecem estar na faixa de nível ~7–10 (leitura, não decisão). A **escala baixa** é o que torna um feiticeiro de nível 10 um rei (CANONE #12). Pistolas e bacamartes: o SRD 5.1 **não** tem armas de fogo (elas estavam só no Guia do Mestre de 2014). De memória (`[M]`, conferir no SRD antes de usar), o livro de 2024 e o SRD 5.2 trazem **Mosquete** e **Pistola** com a propriedade de recarga. A recarga de ~30 s do adendo é bem mais lenta que a regra do 5e (um disparo por turno, ~6 s); se for mantida, vai para `08-sistema/adaptacoes.md`.

## H. História resumida

Ver o [esboço histórico](03-esboco-historico.md), com três processos: formação, consolidação e aspiração imperial, transformações pós-Argon.

> 📜 Conto: Primeira Era / Era Antiga; época de Argon; nas décadas após a morte dele, **Consórcio dos Mantos, Sacerdócio do Glifo e Ordem do Selo de Chumbo**, "máquina inquisitorial **continental**" (l. 1530–1533).
> 📜 Adendo (§9, §18): causalidade multifatorial, não só Caldris; recuos e reformas fracassadas possíveis; **não assumir que Tracton alcança a hegemonia**.

---

## Matriz de transformação (§3.4)

| Mecanismo | Fonte na Etapa I | O que se toma | O que se descarta | Como aparece em Tracton (💡) |
|---|---|---|---|---|
| Prebenda | b/01 | cargo ritual como renda herdável e vendável | templo babilônico | cadeira de Câmara como patrimônio de família |
| Licenciamento de deuses | c/04 | o Estado certifica por eficácia; o não titulado é irregular | burocracia chinesa | registro e auditoria de conjuradores; "regularizar" |
| Controlar não é proibir | b/05, transv. #14 | o alvo é o poder organizado | Roma, Bacanais | lei mira o círculo de guerra |
| Juristas não nomeados pelo governante (Mihna) | b/03 | quem detém o saber limita o poder | islã abássida | Coroa × Círculo × Igreja sobre quem define o dom |
| Querela das Investiduras | b/03 | quem nomeia o clérigo que também é senhor | Europa latina | quem nomeia bispos, Magísteres e inquisidores |
| Centro cético; quem reprime arquiva | b/05, d/02 | perícia procedimental, arquivo do reprimido | Inquisição espanhola | Inquisição pericial; arquivo da Igreja |
| Custo de distância | h/01, transv. #20 | dias e preço | ORBIS romano | Coroa forte na costa e nos rios, fraca na serra |

O vocabulário europeu (conde, barão, Igreja, Inquisição) é decisão do autor (CANONE #16). A matriz não troca os nomes; dá **mecanismos** de várias regiões ao que está por trás deles.

---

## ⚙️ Notas de sistema (5e)
- Humanos (SRD) majoritários; elfos e anões estrangeiros. Elfos com ~1000 anos (CANONE #19): registrar em `adaptacoes.md`.
- Tracton pede **regras de acesso** (quem aprende), **custos** (foco, elixires) e **armas de fogo**, não traços de espécie novos.

## Causas no mundo / usos na narrativa
- Camada mundo. O Tier 1 do **primeiro conto** (CANONE #21 e #29) encontra Tracton pelas autoridades locais: ver [relações locais](04-relacoes-locais-tier1.md). O reino é descrito pelo que é, não para servir a Argon.

## Revisão rápida contra o protocolo (§16, §17)
- **Homogeneização:** reduzida pelo adendo (núcleo, incorporados, fidelidade instável) e pela [matriz](02-matriz-diversidade-interna.md). Ainda falta a voz camponesa e a do clero comum em primeira mão.
- **Causa única:** a virada pós-Argon tem várias hipóteses, nenhuma escolhida.
- **Instituição funcional demais:** a teoria das linhagens é tratada como insuficiente e útil a quem a ensina, sem negar a hereditariedade.
- **Miséria permanente:** corrigido pelo CANONE #16; os blocos C e E ainda pendem para o porto e o crime, porque é o que o conto mostra.
- **Quantidade ≠ profundidade:** E e F seguem rasos.
