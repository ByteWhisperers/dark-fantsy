# Edição diagramada do Livro dos Juramentos

PDF (14 x 21 cm) e EPUB dos Livros I a V, com prólogo, intermédios, epílogo e apêndices. O texto vem sem mudança de `../piloto-livro-N/`; só a forma é desta pasta.

Em `saida/`:
- `Livro-dos-Juramentos.pdf`: volume único.
- `Livro-dos-Juramentos-Livro-I.pdf` a `-Livro-V.pdf`: um por Livro (o I leva o prólogo; o V, o epílogo e os apêndices).
- `Livro-dos-Juramentos.epub`: volume único para leitor digital.

Para gerar de novo depois de mexer no texto: `pip install weasyprint` (e ter o `pandoc`), depois `python3 build.py`.

Projeto gráfico: EB Garamond no texto, IM Fell English nos títulos e capitulares (as duas com licença SIL OFL, em `fontes/`); capitular em vermelho e versalete na abertura de cada capítulo; cabeçalho com o Livro à esquerda e o capítulo à direita; ornamento ❦ entre seções; documentos dos intermédios em quadro cor de pergaminho; mapa em página deitada (`mapa.svg`, cópia de `05-geografia/` sem a nota de bastidor).
