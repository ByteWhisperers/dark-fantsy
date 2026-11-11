# Edição diagramada do Livro I

PDF (14 x 21 cm) e EPUB do *Livro dos Juramentos*, Livro I, gerados a partir de `../piloto-livro-1/` sem mudar o texto.

Para gerar de novo: `pip install weasyprint`, depois `python3 build.py` (cria `livro.html`) e
`python3 -c "from weasyprint import HTML; HTML('livro.html', base_url='.').write_pdf('livro.pdf')"`.
O EPUB sai de `python3 epub_build.py` e `pandoc epub.md --metadata-file=meta.yaml -f markdown+smart --split-level=1 --toc --toc-depth=1 --css epub.css --epub-embed-font=fontes/EBG-400.ttf --epub-embed-font=fontes/EBGI-400.ttf --epub-embed-font=fontes/fell.ttf -o livro.epub`.
Os scripts leem o texto da pasta do projeto; ajuste `SRC` se rodar dentro do repositório.

Fontes: EB Garamond e IM Fell English (licença SIL OFL).
