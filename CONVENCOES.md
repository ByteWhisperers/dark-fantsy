# Convenções

## Idioma e tom
- Tudo em português do Brasil. Termos de D&D podem aparecer em inglês entre parênteses na primeira menção: *Classe de Armadura (Armor Class)*.
- Textos de lore com tom de fantasia sombria; notas de trabalho em linguagem direta.

## Nomes de arquivo
- minúsculas, sem acento, palavras separadas por hífen: `reino-de-exemplo.md`.
- Sessões: `01-notas/sessoes/AAAA-MM-DD.md`.

## Cabeçalho de todo documento
```
---
titulo: Nome
tipo: lugar | povo | faccao | personagem | evento | conceito | pesquisa | nota
camada: mundo | narrativa
status: ideia | rascunho | canone | descartado
fonte: conto | pre-worldbuild | sessao AAAA-MM-DD | inventado
atualizado: AAAA-MM-DD
---
```

## Duas camadas (decisão do autor, 2026-11-07)
- **Camada do mundo:** o que existe independentemente de Argon e da história. Lugares, povos, facções, religiões, regras da magia, história geral. Uma facção pode existir sem nunca aparecer na aventura.
- **Camada narrativa:** o que acontece com Argon, Malakor e os demais personagens dentro desse mundo. Eventos, arcos, cenas, escolhas.
- **Regra:** todo elemento narrativo precisa ter **relações causais** com o mundo (campo "Causas no mundo" nos modelos). Elemento do mundo não precisa de uso narrativo.
- **Objetivo:** evitar que o cenário vire uma coleção de fichas interessantes sem estrutura narrativa que as use. Antes de detalhar um elemento do mundo, perguntar: "a narrativa pede isso, ou é só ficha?" Se for só ficha, fica no mínimo (rascunho curto).
- Cada documento declara sua `camada` no cabeçalho. Pasta `09-narrativa/` guarda a camada narrativa; as pastas 03–08 guardam o mundo. Personagens: mundo se existem independentes da trama (ex.: Caldris como figura do Círculo), narrativa se só existem por causa dela.

## Status (o mais importante)
- **ideia** — hipótese solta, pode morrer.
- **rascunho** — em desenvolvimento, pode mudar.
- **canone** — aprovado pelo autor e listado em `CANONE.md`. Só muda com nova decisão registrada.
- **descartado** — mantido para histórico, com o motivo.

## Marcações no texto
- `[[nome-do-arquivo]]` — liga a outro documento.
- `> ❓ ...` — dúvida em aberto (copiar para `PERGUNTAS-ABERTAS.md`).
- `> 📜 Fonte: ...` — trecho tirado do conto ou do pré-worldbuild.
- `> ⚙️ 5e: ...` — nota de como algo se traduz no sistema.
- `> 💡 ...` — sugestão do Claude, ainda não aprovada pelo autor.

## Regras de trabalho
1. O material do autor (`00-fontes/`) manda. O Claude propõe, o autor decide.
2. O D&D 5e é **norte, não jaula**: usamos a linguagem e as estruturas do sistema como referência, mas o mundo pode quebrá-las quando a história pedir. Quebras ficam anotadas em `08-sistema/adaptacoes.md`.
3. Uma coisa por vez. Nada de gerar regiões, panteões ou povos inteiros de uma vez.
4. Contradição encontrada → vira pergunta aberta, não se resolve sozinha.
