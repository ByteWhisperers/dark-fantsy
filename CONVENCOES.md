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
status: ideia | rascunho | canone | descartado
fonte: conto | pre-worldbuild | sessao AAAA-MM-DD | inventado
atualizado: AAAA-MM-DD
---
```

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
