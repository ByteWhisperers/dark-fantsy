"""Diagrama o Livro dos Juramentos (Livros I a V) em PDF (WeasyPrint) e EPUB (pandoc).

O texto vem intacto dos .md em ../piloto-livro-N/; só a forma muda.

Uso:  python3 build.py            -> volume único + um PDF por Livro, em ./saida/
"""
import re, subprocess, pathlib, html, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = HERE / "saida"

ROMANOS = ["I", "II", "III", "IV", "V"]
FLEURON = '<p class="fleuron" aria-hidden="true">❦</p>'
ORD = {"primeiro": "I", "segundo": "II", "terceiro": "III", "quarto": "IV", "quinto": "V",
       "sexto": "VI", "sétimo": "VII", "oitavo": "VIII", "nono": "IX", "décimo": "X",
       "vigésimo": "XX", "trigésimo": "XXX"}


def roman_from_label(label):
    """'Capítulo décimo terceiro' -> 'XIII'."""
    words = label.split()[1:]
    out = "".join(ORD.get(w, "") for w in words)
    # décimo + terceiro = X + III ; vigésimo + primeiro = XX + I
    return out or label


def strip_frontmatter(t):
    return re.sub(r"\A---\n.*?\n---\n", "", t, flags=re.S).strip() + "\n"


def md2html(md):
    return subprocess.run(
        ["pandoc", "-f", "markdown-auto_identifiers+smart+hard_line_breaks", "-t", "html5", "--wrap=none"],
        input=md, capture_output=True, text=True, check=True).stdout


def split_heading(h):
    label, _, title = h.partition(" · ")
    return label.strip(), title.strip()


def abertura(frag):
    """Capitular + versalete nas primeiras palavras do primeiro parágrafo."""
    def rep(m):
        txt = m.group(1)
        if txt.startswith("<"):           # parágrafo começa com marcação (itálico, negrito): sem capitular
            return m.group(0)
        words = txt.split(" ")
        first, rest = words[0], words[1:]
        # letra inicial; aspas vão junto
        k = 2 if first[0] in "“\"'‘«" else 1
        lead = " ".join([first[k:]] + rest[:2])
        tail = " ".join(rest[2:])
        cauda = " cauda" if first[k - 1] in "QJ" else ""
        return (f'<p class="abertura"><span class="capitular{cauda}">{first[:k]}</span>'
                f'<span class="versalete">{lead}</span> {tail}</p>')
    return re.sub(r"<p>(.*?)</p>", rep, frag, count=1, flags=re.S)


def section_breaks(frag):
    return re.sub(r"<h3>", FLEURON + "<h3>", frag)


# ---------- leitura das fontes ----------

def ler_livros():
    """Devolve lista de blocos: ('parte'|'cap'|'intermedio'|'epilogo'|'apendices'|'prologo', dados)."""
    blocos = []
    for n in range(1, 6):
        pasta = ROOT / f"piloto-livro-{n}"
        for f in sorted(pasta.glob("[0-9]*.md")):
            md = strip_frontmatter(f.read_text(encoding="utf-8"))
            blocos.extend(ler_arquivo(md, n))
    return blocos


def ler_arquivo(md, livro):
    out = []
    # Prólogo (abre com o título do livro e a linha do autor)
    if md.startswith("# Livro dos Juramentos"):
        md = re.sub(r"\A# Livro dos Juramentos\n+\*de Odran.*?\*\n+", "", md, flags=re.S)
        m = re.search(r"^## (.+)$", md, flags=re.M)
        label, title = split_heading(m.group(1))
        frag = md2html(md[m.end():])
        return [("prologo", dict(id="prologo", label=label, title=title, html=section_breaks(abertura(frag)), livro=0))]

    m1 = re.match(r"# (.+)\n", md)
    h1 = m1.group(1) if m1 else ""
    rest = md[m1.end():] if m1 else md

    if h1.startswith("Livro "):
        m2 = re.search(r"^## (.+)$", rest, flags=re.M)
        epigrafe = rest[:m2.start()].strip()
        label, title = split_heading(h1)
        parte = dict(id=f"livro{livro}", label=label, title=title, epigrafe=md2html(epigrafe) if epigrafe else "", livro=livro)
        clabel, ctitle = split_heading(m2.group(1))
        frag = md2html(rest[m2.end():])
        cap = dict(id=None, label=clabel, title=ctitle, html=section_breaks(abertura(frag)), livro=livro)
        return [("parte?", parte), ("cap", cap)]

    if h1.startswith("Intermédio"):
        label, title = split_heading(h1)
        segs = [s.strip() for s in re.split(r"^---\s*$", rest, flags=re.M)]
        nota, doc, extra = segs[0], segs[1], segs[2:]
        margem, comentario = [], []
        for i, s in enumerate(extra):
            last = i == len(extra) - 1
            if s.startswith("*") and not last:
                margem.append(s)
            elif s.startswith("*") and last and len(extra) == 1:
                margem.append(s)
            else:
                comentario.append(s)
        doc_html = md2html(doc).replace("<ol>", '<ol class="rol">')
        h = f'<div class="nota-copista">{md2html(nota)}</div><div class="documento">{doc_html}'
        for s in margem:
            h += f'<div class="margem">{md2html(s)}</div>'
        h += "</div>"
        for s in comentario:
            ch = md2html(s)
            if ch.lstrip().startswith("<h3>"):
                h += f'<div class="comentario">{section_breaks(ch)}</div>'
            else:
                h += f'{FLEURON}<div class="comentario">{ch}</div>'
        return [("intermedio", dict(id=None, label=label, title=title, html=h, livro=livro))]

    if h1.startswith("Epílogo"):
        label, title = split_heading(h1)
        return [("epilogo", dict(id="epilogo", label=label, title=title,
                                 html=section_breaks(abertura(md2html(rest))), livro=livro))]

    if h1.startswith("Apêndices"):
        # ## I · Das fontes -> intertítulos de apêndice
        frag = md2html(rest)
        frag = re.sub(r"<h2>(.*?)</h2>", lambda m: '<h3 class="apendice">' + m.group(1) + "</h3>", frag)
        frag = re.sub(r'<h3 class="apendice">', FLEURON + '<h3 class="apendice">', frag)
        frag = frag.replace(FLEURON, "", 1)  # sem vinheta antes do primeiro
        return [("apendices", dict(id="apendices", label="", title="Apêndices", html=frag, livro=livro))]

    raise SystemExit(f"estrutura inesperada: {h1!r}")


def normalizar(blocos):
    """Uma página de parte por Livro; ids únicos."""
    vistos, out, n = set(), [], 0
    for kind, d in blocos:
        if kind == "parte?":
            if d["livro"] in vistos:
                continue
            vistos.add(d["livro"])
            out.append(("parte", d))
            continue
        n += 1
        if d["id"] is None:
            d["id"] = f"c{n}"
        out.append((kind, d))
    return out


# ---------- HTML ----------

def html_livro(blocos, titulo_sub, mapa_svg, com_mapa=True):
    toc = []
    for kind, d in blocos:
        if kind == "parte":
            toc.append(f'<li class="toc-parte"><a href="#{d["id"]}">{html.escape(d["label"])} · {html.escape(d["title"])}</a></li>')
        elif kind == "cap":
            toc.append(f'<li class="toc-capitulo"><a href="#{d["id"]}"><span class="toc-label">{roman_from_label(d["label"])}</span>'
                       f'<span class="toc-title">{html.escape(d["title"])}</span></a></li>')
        else:
            lab = html.escape(d["label"]) + " · " if d["label"] else ""
            toc.append(f'<li class="toc-{kind}"><a href="#{d["id"]}"><span class="toc-label">{lab}</span>'
                       f'<span class="toc-title">{html.escape(d["title"])}</span></a></li>')

    corpo = [f"""
<section class="falso-rosto"><p>Livro dos Juramentos</p></section>
{'<section class="mapa-pagina"><figure>' + mapa_svg + '</figure></section>' if com_mapa else ''}
<section class="rosto">
  <p class="rosto-ornamento">❦</p>
  <h1 class="rosto-titulo">Livro dos<br/>Juramentos</h1>
  <p class="rosto-filete"></p>
  <p class="rosto-sub">{titulo_sub}</p>
  <p class="rosto-autor">de Odran de Vessane<br/><span>cônego e guarda das cartas</span></p>
  <p class="rosto-casa">Darck Fantasy</p>
</section>
<section class="colofao-pagina">
  <p>Livro dos Juramentos. {titulo_sub}.</p>
  <p>Texto em rascunho. Edição de trabalho.</p>
  <p>Composto em EB Garamond, com capitulares e títulos em IM Fell English.</p>
</section>
<section class="sumario">
  <h2 class="sumario-titulo">Sumário</h2>
  <ul class="toc">{''.join(toc)}</ul>
</section>"""]

    for kind, d in blocos:
        if kind == "parte":
            corpo.append(f'<section class="parte" id="{d["id"]}" data-c="{html.escape(d["label"])} · {html.escape(d["title"])}"><p class="parte-label">{html.escape(d["label"])}</p>'
                         f'<p class="rosto-filete"></p><h1 class="parte-titulo">{html.escape(d["title"])}</h1>'
                         f'{"<div class=epigrafe>" + d["epigrafe"] + "</div>" if d["epigrafe"] else ""}</section>')
            continue
        label = f'<p class="cap-label">{html.escape(d["label"])}</p>' if d["label"] else ""
        corpo.append(f'<section class="cap {kind}" id="{d["id"]}"><header>{label}'
                     f'<h2 class="cap-titulo">{html.escape(d["title"])}</h2>'
                     f'<p class="cap-ornamento">⁓ ❦ ⁓</p></header>{d["html"]}</section>')

    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"/>
<title>Livro dos Juramentos — {titulo_sub}</title>
<meta name="author" content="Odran de Vessane"/>
<link rel="stylesheet" href="livro.css"/></head>
<body>{''.join(corpo)}</body></html>"""


def html_epub(blocos):
    """HTML simples para o pandoc: h1 por capítulo, h2 por intertítulo."""
    partes = []
    for kind, d in blocos:
        if kind == "parte":
            partes.append(f'<h1 class="parte">{html.escape(d["label"])} · {html.escape(d["title"])}</h1>'
                          f'<div class="epigrafe">{d["epigrafe"]}</div>')
            continue
        t = (d["label"] + " · " if d["label"] else "") + d["title"]
        h = d["html"]
        h = re.sub(r'<p class="fleuron"[^>]*>❦</p>', "", h)
        h = re.sub(r'<span class="capitular[^"]*">(.*?)</span><span class="versalete">(.*?)</span>',
                   r'<span class="capitular">\1</span><span class="versalete">\2</span>', h)
        h = h.replace("<h3", "<h2").replace("</h3>", "</h2>")
        partes.append(f'<h1 class="{kind}">{html.escape(t)}</h1>{h}')
    return '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Livro dos Juramentos</title></head><body>' + "".join(partes) + "</body></html>"


def main():
    from weasyprint import HTML
    OUT.mkdir(exist_ok=True)
    mapa = (HERE / "mapa.svg").read_text(encoding="utf-8")
    todos = normalizar(ler_livros())

    def gerar(blocos, sub, nome, com_mapa=True):
        doc = html_livro(blocos, sub, mapa, com_mapa)
        p = HERE / f"_{nome}.html"
        p.write_text(doc, encoding="utf-8")
        d = HTML(str(p), base_url=str(HERE)).render()
        d.write_pdf(OUT / f"{nome}.pdf")
        p.unlink()
        print(nome, len(d.pages), "páginas")

    gerar(todos, "Livros I a V", "Livro-dos-Juramentos")

    # um PDF por Livro: o I leva o prólogo; o V leva epílogo e apêndices
    por_livro = {n: [] for n in range(1, 6)}
    for kind, d in todos:
        por_livro[max(d["livro"], 1)].append((kind, d))
    if "--so-volume" not in sys.argv:
        for n, bl in por_livro.items():
            sub = f'Livro {ROMANOS[n-1]} · {next(d["title"] for k, d in bl if k == "parte")}'
            gerar(bl, sub, f"Livro-dos-Juramentos-Livro-{ROMANOS[n-1]}", com_mapa=True)

    # EPUB do volume
    (HERE / "_epub.html").write_text(html_epub(todos), encoding="utf-8")
    subprocess.run(["pandoc", "_epub.html", "-f", "html", "-o", str(OUT / "Livro-dos-Juramentos.epub"),
                    "--metadata", "title=Livro dos Juramentos", "--metadata", "subtitle=Livros I a V",
                    "--metadata", "author=Odran de Vessane", "--metadata", "lang=pt-BR",
                    "--split-level=1", "--toc", "--toc-depth=1", "--css", "epub.css",
                    "--epub-embed-font=fontes/EBG-400.ttf", "--epub-embed-font=fontes/EBGI-400.ttf",
                    "--epub-embed-font=fontes/fell.ttf"], cwd=HERE, check=True)
    (HERE / "_epub.html").unlink()
    print("epub ok")


if __name__ == "__main__":
    main()
