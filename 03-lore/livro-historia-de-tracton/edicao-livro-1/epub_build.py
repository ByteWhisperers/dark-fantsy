import re,pathlib
SRC=pathlib.Path("/mnt/project-files/darck-fantasy/03-lore/livro-historia-de-tracton/piloto-livro-1")
fs=sorted(SRC.glob("0*.md"))
out=[]
for i,f in enumerate(fs):
    t=re.sub(r"\A---\n.*?\n---\n","",f.read_text(),flags=re.S).strip()+"\n"
    if i==0:
        t=re.sub(r"\A# Livro dos Juramentos\n+\*de Odran.*?\*\n+","",t,flags=re.S)
        t=t.replace("## Prólogo","# Prólogo",1); t=re.sub(r"^### ","## ",t,flags=re.M)
    elif i==8:
        t=re.sub(r"^---\s*$","* * *",t,flags=re.M)
    else:
        if i==1: t=t.replace("# Livro I · As Décadas de Sangue","# Livro I · As Décadas de Sangue {.parte}",1)
        else: t=re.sub(r"^# Livro I · As Décadas de Sangue\n+","",t,flags=re.M)
        t=re.sub(r"^## Cap","# Cap",t,flags=re.M); t=re.sub(r"^### ","## ",t,flags=re.M)
    out.append(t.strip())
pathlib.Path("epub.md").write_text("\n\n".join(out)+"\n")
