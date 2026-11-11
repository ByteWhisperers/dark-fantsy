"""Diagrama o Livro I do Livro dos Juramentos: HTML -> PDF (WeasyPrint) e EPUB (pandoc).
O texto vem intacto dos .md; só a forma muda."""
import re, subprocess, pathlib, html

SRC = pathlib.Path("/mnt/project-files/darck-fantasy/03-lore/livro-historia-de-tracton/piloto-livro-1")
HERE = pathlib.Path(__file__).parent

FILES = ["00-prologo.md", "01-as-terras-sem-nome.md", "02-inimigos-que-comerciam.md",
         "03-a-guerra-que-nao-acabava-na-colheita.md", "04-a-gente-da-coluna.md",
         "05-o-ano-em-que-as-cidades-nao-pagaram.md", "06-o-que-se-tomava.md",
         "07-a-terra-nao-da-duas-vezes.md", "08-intermedio-rol-de-uma-venda.md"]

FLEURON = '<p class="fleuron" aria-hidden="true">❦</p>'


def body_of(name):
    t = (SRC / name).read_text(encoding="utf-8")
    t = re.sub(r"\A---\n.*?\n---\n", "", t, flags=re.S)          # frontmatter
    return t


def md2html(md):
    return subprocess.run(["pandoc", "-f", "markdown-auto_identifiers+smart", "-t", "html5", "--wrap=none"],
                          input=md, capture_output=True, text=True, check=True).stdout


def split_heading(h):
    label, _, title = h.partition(" · ")
    return label.strip(), title.strip()


def first_para_classes(frag):
    # capitular no primeiro parágrafo: letra em destaque + primeiras palavras em versalete
    def rep(m):
        txt = m.group(1)
        words = txt.split(" ")
        first, rest = words[0], words[1:]
        lead = " ".join([first[1:]] + rest[:2])
        tail = " ".join(rest[2:])
        return (f'<p class="abertura"><span class="capitular{' cauda' if first[0] in 'QJ' else ''}">{first[0]}</span>'
                f'<span class="versalete">{lead}</span> {tail}</p>')
    return re.sub(r"<p>(.*?)</p>", rep, frag, count=1, flags=re.S)


def section_breaks(frag):
    # vinheta antes de cada intertítulo, exceto se for o primeiro bloco
    return re.sub(r"<h3>", FLEURON + "<h3>", frag)


chapters = []   # (id, label, title, html, kind)

# Prólogo
md = body_of(FILES[0])
md = re.sub(r"^# Livro dos Juramentos\n+\*de Odran.*?\*\n+", "", md, flags=re.S)
m = re.search(r"^## (.+)$", md, flags=re.M)
label, title = split_heading(m.group(1))
frag = md2html(md[m.end():])
chapters.append(("prologo", label, title, section_breaks(first_para_classes(frag)), "prologo"))

# Capítulos 1-7
for i, f in enumerate(FILES[1:8], start=1):
    md = body_of(f)
    md = re.sub(r"^# Livro I · As Décadas de Sangue\n+", "", md, flags=re.M)
    m = re.search(r"^## (.+)$", md, flags=re.M)
    label, title = split_heading(m.group(1))
    frag = md2html(md[m.end():])
    chapters.append((f"cap{i}", label, title, section_breaks(first_para_classes(frag)), "capitulo"))

# Intermédio
md = body_of(FILES[8])
m = re.search(r"^# (.+)$", md, flags=re.M)
label, title = split_heading(m.group(1))
rest = md[m.end():]
parts = [p.strip() for p in re.split(r"^---\s*$", rest, flags=re.M)]
# parts: [nota de abertura, rol, nota à margem, comentário]
nota, rol, margem, coment = parts
rol_html = md2html(rol)
rol_html = rol_html.replace("<ol>", '<ol class="rol">')
inter = (f'<div class="nota-copista">{md2html(nota)}</div>'
         f'<div class="documento">{rol_html}'
         f'<div class="margem">{md2html(margem)}</div></div>'
         f'{FLEURON}<div class="comentario">{md2html(coment)}</div>')
chapters.append(("intermedio", label, title, inter, "intermedio"))


def ordinal_label(label):
    return label


# ---------- HTML do livro ----------
toc_rows = []
for cid, label, title, _, kind in chapters:
    if kind == "capitulo" and cid == "cap1":
        toc_rows.append('<li class="toc-parte"><a href="#livro1">Livro I · As Décadas de Sangue</a></li>')
    ROM = {"primeiro":"I","segundo":"II","terceiro":"III","quarto":"IV","quinto":"V","sexto":"VI","sétimo":"VII"}
    tl = ROM.get(label.split()[-1], label) if kind == "capitulo" else label
    toc_rows.append(f'<li class="toc-{kind}"><a href="#{cid}"><span class="toc-label">{html.escape(tl)}</span>'
                    f'<span class="toc-title">{html.escape(title)}</span></a></li>')

mapa = (HERE / "mapa.svg").read_text(encoding="utf-8")

body = []
body.append("""
<section class="falso-rosto"><p>Livro dos Juramentos</p></section>
<section class="mapa-pagina">
  <figure>__MAPA__</figure>
</section>
<section class="rosto">
  <p class="rosto-ornamento">❦</p>
  <h1 class="rosto-titulo">Livro dos<br/>Juramentos</h1>
  <p class="rosto-filete"></p>
  <p class="rosto-sub">Livro I · As Décadas de Sangue</p>
  <p class="rosto-autor">de Odran de Vessane<br/><span>cônego e guarda das cartas</span></p>
  <p class="rosto-casa">Darck Fantasy</p>
</section>
<section class="colofao-pagina">
  <p>Livro dos Juramentos. Livro I, <em>As Décadas de Sangue</em>.</p>
  <p>Texto em rascunho. Edição de trabalho.</p>
  <p>Composto em EB Garamond, com capitulares e títulos em IM Fell English.</p>
</section>
<section class="sumario">
  <h2 class="sumario-titulo">Sumário</h2>
  <ul class="toc">""" + "\n".join(toc_rows) + """</ul>
</section>
""")
body[-1] = body[-1].replace("__MAPA__", mapa)

for cid, label, title, frag, kind in chapters:
    if cid == "cap1":
        body.append('<section class="parte" id="livro1"><p class="parte-label">Livro I</p>'
                    '<p class="rosto-filete"></p><h1 class="parte-titulo">As Décadas de Sangue</h1></section>')
    body.append(f'<section class="cap {kind}" id="{cid}">'
                f'<header><p class="cap-label">{html.escape(label)}</p>'
                f'<h2 class="cap-titulo">{html.escape(title)}</h2>'
                f'<p class="cap-ornamento">⁓ ❦ ⁓</p></header>{frag}</section>')

doc = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"/>
<title>Livro dos Juramentos — Livro I</title>
<meta name="author" content="Odran de Vessane"/>
<link rel="stylesheet" href="livro.css"/></head>
<body>{''.join(body)}</body></html>"""
(HERE / "livro.html").write_text(doc, encoding="utf-8")
print("ok", len(doc))
