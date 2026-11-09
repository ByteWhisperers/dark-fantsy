---
titulo: P1 · Tracton — arquitetura institucional e casos de teste
tipo: faccao
camada: mundo
status: ideia
fonte: conto + adendo autoral (2026-11-09) + inventado (propostas marcadas)
atualizado: 2026-11-09
---

# Tracton — arquitetura institucional (entregável B)

Pedido do [adendo](../../00-fontes/adendo-autoral-tracton-p1.txt), §17: para cada instituição, origem, legitimidade, competências, capacidade efetiva, financiamento, relações, diferenças regionais, conflitos internos, ambições e efeitos; **distinguir o poder que reivindica do poder que executa**; testar com três casos.

**Tudo aqui é proposta** (`💡`), exceto o que vem marcado do conto (📜) ou do adendo (📜 Adendo). Onde há escolha estrutural, dou **alternativas com consequências** e uma recomendação; nada é canonizado.

---

## 1. Escolhas estruturais (alternativas)

### 1.1 O que é o Círculo de Estudos Arcanos?
📜 Conto: tem Quatro Câmaras, Magísteres com títulos ("Magíster Titular da Quarta Câmara"), matrículas e registros de famílias de sangue desperto; responde a um "Conselho" que manda Caldris com a Guarda de Prata e escribas juramentados.

| Alternativa | Como funciona | Consequências |
|---|---|---|
| **1a. Órgão régio** | A Coroa nomeia os Magísteres; o Círculo é um ministério do arcano. | Coroa forte no papel; mas a Coroa depende de quem entende de magia para fiscalizar magia, e o Círculo vira o lugar onde a nobreza disputa cargos. Pouca tensão Coroa × Círculo. |
| **1b. Corporação com carta régia** | O Círculo se autogoverna (elege, examina, diploma), e a Coroa lhe concede o **monopólio da certificação** em troca de serviço e lealdade. | Tensão produtiva: o Círculo tem interesse corporativo próprio (renda, prestígio, fechamento), a Coroa quer obediência. A carta pode ser revista, revogada ou disputada. Explica por que o Círculo **aluga** magos à nobreza. |
| **1c. Corpo híbrido com a Igreja** | Magísteres têm ordenação ou juramento religioso; a heresia arcana é julgada dentro dele. | Funde as duas jurisdições e apaga a tensão Coroa × Igreja sobre a magia, que o adendo pede para preservar (CANONE #15). |

> 💡 **Recomendo 1b.** Mantém três centros com interesses próprios (Coroa, Círculo, Igreja), que é o que o adendo pede, e cria a pergunta histórica certa: **quando e por que a Coroa concedeu esse monopólio**, e o que recebeu em troca (ver [esboço histórico](03-esboco-historico.md)).

### 1.2 Câmaras e Academias: o que é cada uma?
📜 Conto: "Quatro Câmaras" com grau ("Magíster da Segunda Câmara", l. 153; "Quarta Câmara", Caldris e Julian) e "círculo de contenção da **Terceira Câmara**" (l. 222); "quatro Academias Reais" com arquivos; aprendizes nobres nas "Academias da Cidade Alta". Caldris ensina "Teoria da Ressonância" na Quarta Câmara. Pergunta #8.

| Alternativa | Câmaras | Academias | Consequências |
|---|---|---|---|
| **2a. Câmaras = graus** | Escada de títulos (1ª a 4ª), cada uma ligada a uma faixa de círculos. | Escolas onde se aprende; cada uma pode ter mestres de várias Câmaras. | Simples e legível. "Quarta Câmara" = topo do que um mortal comum alcança no reino (~4º–5º círculo?). Nos casos de teste, a Câmara diz **quem tem autoridade** para julgar um conjurador. |
| **2b. Câmaras = funções** | Cada Câmara é um ramo: ensino, guerra, registro e auditoria, pesquisa. | Escolas regionais. | Mais burocrático; a Câmara de registro vira o centro do controle. Mas "círculo de contenção da Terceira Câmara" fica estranho. |
| **2c. Câmaras = órgãos de governo do Círculo** | Assembleias por nível que votam e julgam. | Escolas. | Cria política interna rica, mas pede detalhe que o Tier 1 não usa. |

> 💡 **Recomendo 2a**, com um detalhe: as **quatro Academias Reais** ficam em **cidades diferentes** (a capital e três grandes cidades, ao menos uma portuária). Assim, o registro existe onde há Academia, e o resto do reino depende de visitas, relatórios e denúncias. Isso dá geografia ao monopólio.

> ❓ Se as Câmaras são graus, o que está **acima** da Quarta? O Conselho? Os magos de 5º–6º círculo que o conto sugere na Alta Capital (pergunta #8)?

### 1.3 O que é o "Conselho"?
📜 Conto: "o Conselho me enviou até aqui" (Caldris, l. 1442); "um banho de sangue que o Conselho não autorizara" (l. 1509).

| Alternativa | Consequência |
|---|---|
| **3a. Conselho do rei** (conselho régio com nobres, clérigos e Magísteres) | O controle arcano é **política de Estado** decidida com a nobreza e a Igreja à mesa. Caldris é enviado do rei. |
| **3b. Conselho do Círculo** (órgão superior da corporação) | Caldris é enviado da corporação, e a Coroa só aparece pela escolta (Guarda de Prata). Tensão: quem paga a Guarda? |

> 💡 Sem recomendação forte. **3b** combina com 1b e torna a visita a Vallenar um ato do Círculo **com força emprestada da Coroa**, o que é bom para os casos de teste. Mas "armas reais" na carruagem (l. 1405) pende para 3a. Fica para o Hermes (pergunta #28).

---

## 2. Instituições: reivindica × executa

Leitura com as recomendações 1b, 2a e 3b. Se o Hermes escolher outra, a tabela muda.

### Coroa
| Campo | Proposta |
|---|---|
| Origem | 💡 Uma casa senhorial do núcleo que acumulou senhorios por conquista, casamento e herança (adendo §2). |
| Legitimidade | Sucessão dinástica, sagração pela Igreja (💡), vitória militar, costume. |
| **Reivindica** | Soberania sobre todo o reino; justiça alta (crimes de "risco público"); monopólio da certificação arcana (delegado ao Círculo); impostos; guerra e paz; interdito real. |
| **Executa** | Plenamente na capital, nos portos com Academia e ao longo dos rios. Na fronteira, por meio de barões, que obedecem em umas matérias e não em outras (adendo §2). Caçadores e Guarda de Prata chegam caro e devagar. |
| Financiamento | Domínio régio, pedágios e alfândegas dos portos, tributos negociados com senhores, 💡 taxas de registro arcano e de licença de pólvora. |
| Ambições | Centralizar e expandir (CANONE #14). Instrumentos possíveis, **não consolidados**: registros, fisco, padronização jurídica, forças régias, controle de tecnologias estratégicas (magia e pólvora), representantes locais. |
| Conflitos internos | Facções da corte; casas que querem o trono; sucessões. |
| Efeito sobre a população | Alto nos portos (imposto, alfândega, lei régia); distante na serra, onde "o rei" é um nome no selo do barão. |

### Aristocracia territorial (condes, barões e senhores)
| Campo | Proposta |
|---|---|
| Legitimidade | Linhagem, vassalagem jurada, posse da terra, força. |
| **Reivindica** | Justiça local (tribunais senhoriais; 📜 "tribunais de Vallenar", l. 1229), tributo dos camponeses, guerra privada contra vizinhos, privilégios locais. |
| **Executa** | Quase tudo dentro do senhorio, se tiver homens armados. 📜 Na fronteira, "a lei era escrita por quem tinha mais aço ou mais pólvora" (l. 1150). |
| Divisões | 💡 **Núcleo tractoniano** (mais leais, mais vigiados), **incorporados** (privilégios negociados na incorporação), **fidelidade instável** (podem trocar de lado). Categorias analíticas (adendo §2). |
| Relação com a magia | Precisa de força arcana para guerrear e **não pode formá-la**: compra do Círculo (aluguel de diplomados) ou contrata irregular (caso B). Casas com sangue desperto têm vantagem própria. |
| Conflitos | Entre vizinhos (Vallenar × Oakhaven por ferro e pedágio); com a Coroa (centralização); com a Igreja (terras, dízimos, nomeações). |

### Igreja
| Campo | Proposta |
|---|---|
| Legitimidade | A divindade da ordem e da força legítima (CANONE #15); antiguidade; rede paroquial. |
| **Reivindica** | Jurisdição sobre heresia, sacramentos, casamento e herança (💡, como no medievo), moral pública; universalidade além das fronteiras do reino (CANONE #15). |
| **Executa** | Onde há paróquia, diocese e tribunal eclesiástico. A rede paroquial chega **mais longe** que a Coroa: o pároco está em toda aldeia. 💡 Essa é a vantagem da Igreja sobre a Coroa na fronteira. |
| Braços | Clero secular (bispos, padres); **Inquisição** (perícia e julgamento de heresia; 📜 pericia relatórios, l. 1414); **templários** (força armada, 📜 queimam a mina da Medula); anatomistas (📜 Orel). |
| Financiamento | 💡 Dízimos, terras, doações, taxas sacramentais. |
| Relação com a magia | 💡 Uma divindade da **força legítima** tem motivo próprio para apoiar o controle: magia irregular é força sem legitimidade (ver dossiê, bloco F). Mas a Igreja também quer **definir** o legítimo, o que a põe em concorrência com o Círculo e a Coroa. |
| Conflitos internos | 💡 Bispos ligados a casas nobres × Inquisição centralizada; clero paroquial pobre × alto clero; correntes que veem a magia como dom da ordem divina × como usurpação. |
| Ambições | Universalizante e expansionista, com objetivos que não coincidem com os da Coroa (CANONE #15). |

### Círculo de Estudos Arcanos (com Câmaras e Academias)
| Campo | Proposta |
|---|---|
| Origem | 💡 Corporação de conjuradores que recebeu carta régia depois de guerras em que magia decidiu batalhas (CANONE #17; ver [esboço](03-esboco-historico.md)). |
| Legitimidade | Saber, exame, genealogia registrada, carta régia. |
| **Reivindica** | Monopólio de ensinar, examinar, diplomar e **auditar** conjuradores acima do 1º círculo em todo o reino; perícia sobre o que é ou não magia. |
| **Executa** | Onde há Academia. Fora delas, depende de **denúncia** e de escolta régia. 📜 Os arquivos levaram meses para confirmar que nenhum diplomado esteve perto de Vallenar (l. 1414). |
| Financiamento | 💡 Matrículas pagas pelas famílias, **aluguel de magos de guerra** às casas nobres, taxas de registro, patronato régio. Cadeiras de Câmara como **prebenda** (b/01): renda herdável, que tende a se fragmentar. |
| Conflitos internos | 💡 Famílias de sangue desperto antigas × novas; Magísteres que querem abrir o recrutamento (mais magos, mais renda) × os que querem fechar (mais valor para cada mago); Academias regionais × a da capital. |
| Efeito sobre a população | Quase nenhum direto. Indireto: quem fornece insumos; quem é denunciado; quem é contratado como "mago de batalha". |

### Guarda de Prata e caçadores da Coroa
| Campo | Proposta |
|---|---|
| 📜 Conto | Guarda de Prata escolta Caldris (l. 1406); caçadores da Coroa perseguem magos sem registro "na capital e nas grandes cidades portuárias" (l. 1147). |
| **Reivindica** | Alcance em todo o reino. |
| **Executa** | 💡 Poucos, caros, concentrados em cidades. Na fronteira, só com cooperação do senhor local ou com escolta grande. |
| 💡 Proposta de diferença | **Guarda de Prata** = força de escolta e proteção ligada ao Círculo ou ao Conselho (prata contra criaturas? a definir). **Caçadores da Coroa** = agentes régios de captura, pagos por cabeça ou por soldo, com fama ruim. Dois corpos, duas lealdades. |

### Tribunais e autoridades locais
| Campo | Proposta |
|---|---|
| Tipos | 💡 Tribunal senhorial; tribunal urbano (cidades com carta); tribunal eclesiástico; tribunal régio (itinerante ou na capital); justiça de fato do crime organizado (📜 a Ferradura Quebrada). |
| Regra geral 💡 | **Foro por condição**: nobre julgado por pares, clérigo pela Igreja, burguês pela cidade, camponês pelo senhor. A magia irregular é um dos raros crimes que **atravessa** essa regra (risco público + heresia), e por isso é campo de disputa. |

---

## 3. Os três casos de teste

Para cada caso: **quem investiga, prende, julga, concede exceção, executa e pode contestar**, e como muda entre **capital**, **porto** e **fronteira**.

### Caso A · Camponês não registrado usa magia ofensiva e mata alguém

| | Capital | Porto | Fronteira (ex.: Vallenar) |
|---|---|---|---|
| Quem fica sabendo | Guarda urbana, testemunhas | Guarda urbana, gangues, informantes | Aldeia, pároco, senhor |
| Investiga | Caçadores da Coroa + perícia do Círculo | Caçadores; perícia do Círculo se houver Academia | **Senhor local**; o pároco pode avisar a diocese |
| Prende | Caçadores | Caçadores ou guarda; gangue pode esconder ou entregar | Homens do senhor |
| Julga | Disputa: tribunal régio (crime de risco público) **×** tribunal eclesiástico (heresia) | Igual, com mais suborno | O **senhor**, como homicídio comum, **se quiser** |
| Exceção | Quase nenhuma: plebeu, sem linhagem a provar | Quase nenhuma | O senhor pode **recrutá-lo** em vez de julgá-lo |
| Executa | Coroa (forca ou fogueira, conforme quem ganhou a jurisdição) | Coroa | Senhor; ou ninguém |
| Contesta | Praticamente ninguém; um patrono raro | Um patrono do crime, se o camponês for útil | Um senhor rival pode **denunciar** o senhor que o protegeu |

> 💡 **O que o caso mostra:** o mesmo crime é **execução certa** na capital e **oportunidade de recrutamento** na fronteira. A Igreja é a instituição com mais chance de saber em qualquer lugar, porque o pároco está na aldeia. Para o camponês, o perigo não é "a lei": é **quem soube primeiro**.

### Caso B · Barão contrata conjurador independente para sua força militar
📜 É o caso de Henrik e Argon.

| | Capital | Porto | Fronteira |
|---|---|---|---|
| É viável? | Não: seria descoberto rápido | Difícil; possível com magos estrangeiros de passagem | Sim; é onde acontece |
| Quem fica sabendo | — | Rivais, Academia local | **Rivais** (os derrotados, vizinhos), sobreviventes, a Igreja |
| Investiga | — | Círculo | **Círculo com escolta régia**, meses ou anos depois (📜 três anos, Caldris) |
| Julga | — | Círculo / tribunal régio | Contra o conjurador: Círculo e Igreja. Contra o barão: **ninguém julga um barão facilmente**; a Coroa ameaça com **interdito real** (📜 l. 1421) |
| Exceção | — | Regularização do conjurador, se for absorvível | **Regularização** (o Círculo absorve o mago e seu método) ou **licença ex post** comprada pelo barão |
| Executa | — | Caçadores | Depende de força: 📜 Caldris recua porque um confronto "terminaria num banho de sangue que o Conselho não autorizara" (l. 1509) |
| Contesta | — | — | O barão, pelos seus suseranos, aliados, casamentos e a Igreja local |

> 💡 **O que o caso mostra:** a lei arcana é **arma entre nobres**. Quem denuncia é quase sempre o rival que perdeu. O Círculo prefere **absorver** a punir, porque punir um barão custa uma guerra. Isso dá ao Tier 1 um tipo de trama sem alta política: o mago contratado vira moeda numa disputa de vizinhos.

### Caso C · Família nobre esconde descendente com capacidade arcana fora dos critérios de registro
💡 "Fora dos critérios" pode ser: bastardo; capacidade surgida em casa sem sangue desperto registrado; capacidade tardia; criança cuja capacidade não cabe na teoria (ex.: manifestações estranhas, outro tipo de dom).

**Por que esconder?** (💡 hipóteses, não excludentes)
1. **Escândalo de legitimidade:** se o dom "vem do sangue", um dom inesperado sugere adultério ou bastardia.
2. **Obrigação de serviço:** o registro pode obrigar a criança a ir para a Academia (refém de fato) ou a servir a Coroa.
3. **Vantagem privada:** um mago não registrado é arma da casa, fora do aluguel do Círculo.
4. **Medo da Igreja:** se a capacidade não se parece com a ortodoxa, pode cair em heresia.

| | Capital | Porto | Fronteira |
|---|---|---|---|
| Quem descobre | Servos, tutores, rivais da corte, confessor | Servos, comerciantes, informantes | Quase ninguém; o pároco e os servos |
| Investiga | Círculo, com discrição | Círculo | Raramente alguém |
| Julga | **Negociação**, não tribunal: Círculo, família e talvez Coroa | Negociação | Ninguém, até um rival denunciar |
| Exceção | 📜 **"Mutação tardia de linhagem nobre"** (l. 1457–1460): a porta legal existe **para nobres** | A mesma | A mesma, se chegar a ser preciso |
| Executa | Registro tardio, multa, criança enviada à Academia | Idem | — |
| Contesta | A família, com seus aliados no Conselho | Idem | — |

> 💡 **O que o caso mostra:** o mesmo fato (capacidade não registrada) é **crime capital** para o plebeu (caso A) e **regularização negociada** para o nobre (caso C). A desigualdade não está no texto da lei, está nas **saídas** que a lei oferece. É aqui que, depois de Argon, a "coleira nobre" da Ordem do Selo de Chumbo faz sentido: o endurecimento recai sobre quem não tem porta de saída.

---

## 4. Perguntas novas
- **#28** O "Conselho" é conselho do rei ou órgão superior do Círculo? (1.3)
- **#29** O que está acima da Quarta Câmara? (1.2; liga à #8)
- **#30** A Guarda de Prata e os caçadores da Coroa são o mesmo corpo ou dois? A quem cada um responde?
