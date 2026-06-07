#!/usr/bin/env python3
"""
Build script para gerar PDF article a partir do notebook demonstrativo.
Simula localmente a pipeline do template Resposta_Trabalho_Trilha_I.ipynb.

Uso: python3 scripts/build_article_pdf_from_notebook.py

Saídas:
  outputs/Trabalho_Trilha_I_AcolheMente_PB_TemplateExport_article.pdf
  outputs/Trabalho_Trilha_I_AcolheMente_PB_TemplateExport_article.tex
  outputs/build_article_pdf.log
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NB_DIR = os.path.join(BASE_DIR, "notebooks")
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")
V3_3_DIR = os.path.join(os.path.dirname(BASE_DIR), "academic_abntex2_attempt_v3_3")

NB_NAME = "Trabalho_Trilha_I_AcolheMente_PB_TemplateExport"
NB_FILE = os.path.join(NB_DIR, f"{NB_NAME}.ipynb")
OUT_PREFIX = "Trabalho_Trilha_I_AcolheMente_PB_TemplateExport_article"

LOG = []

def log(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    LOG.append(line)

def run(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, cwd=cwd,
                            capture_output=True, text=True, timeout=180)
    return result.returncode, result.stdout, result.stderr

def main():
    log("=== Build Article PDF from Notebook ===")
    log(f"Base: {BASE_DIR}")
    log(f"Notebook: {NB_FILE}")

    assert os.path.exists(NB_FILE), f"Notebook não encontrado: {NB_FILE}"
    os.makedirs(OUTPUTS_DIR, exist_ok=True)

    # Check xelatex
    rc, _, _ = run("which xelatex")
    if rc != 0:
        log("⚠️ xelatex não encontrado. Tentando pdflatex...")
        rc2, _, _ = run("which pdflatex")
        if rc2 != 0:
            log("❌ Nenhum compilador LaTeX disponível. PDF não será gerado.")
            log("   Instale: apt-get install texlive texlive-xetex texlive-latex-extra")
            save_log()
            return False
        latex_cmd = "pdflatex"
    else:
        latex_cmd = "xelatex"
    log(f"  ✅ Compilador: {latex_cmd}")

    # Check bibtex
    rc, _, _ = run("which bibtex")
    has_bibtex = rc == 0
    log(f"  {'✅' if has_bibtex else '⚠️'} bibtex: {'disponível' if has_bibtex else 'não disponível'}")

    # Work in temp dir
    with tempfile.TemporaryDirectory() as tmpdir:
        log(f"  Temp dir: {tmpdir}")

        # 1. Load and clean notebook
        log("1. Carregando e limpando notebook...")
        with open(NB_FILE, "r", encoding="utf-8") as f:
            nb_data = json.load(f)

        celulas_filtradas = []
        for c in nb_data["cells"]:
            src = "".join(c.get("source", []))
            sl = src.lower()
            if any(kw in sl for kw in ["nbconvert", "xelatex", "bibtex"]):
                continue
            if "apt-get" in sl and "texlive" in sl:
                continue
            if "drive.mount" in sl:
                continue
            if "referencias.bib" in sl and "%%capture" in sl and c["cell_type"] == "code":
                continue
            celulas_filtradas.append(c)

        nb_data["cells"] = celulas_filtradas
        clean_nb = os.path.join(tmpdir, "temp_limpo.ipynb")
        with open(clean_nb, "w", encoding="utf-8") as f:
            json.dump(nb_data, f, ensure_ascii=False, indent=2)
        log(f"  Células filtradas: {len(celulas_filtradas)} (de {len(json.load(open(NB_FILE))['cells'])})")

        # 2. Copy supporting files
        log("2. Copiando arquivos de suporte...")
        logo = os.path.join(V3_3_DIR, "figures", "logo_urutai.png")
        if os.path.exists(logo):
            shutil.copy2(logo, os.path.join(tmpdir, "logo_urutai.png"))
            log("  ✅ logo_urutai.png")

        # Copy figures
        figs_dir = os.path.join(V3_3_DIR, "figures")
        for fig in os.listdir(figs_dir):
            if fig.endswith(".png"):
                shutil.copy2(os.path.join(figs_dir, fig), os.path.join(tmpdir, fig))

        bib = os.path.join(V3_3_DIR, "latex", "referencias.bib")
        if os.path.exists(bib):
            shutil.copy2(bib, os.path.join(tmpdir, "referencias.bib"))
            log("  ✅ referencias.bib")

        # 3. nbconvert
        log("3. Executando nbconvert --to latex...")
        rc, stdout, stderr = run(
            f"jupyter nbconvert --to latex {clean_nb} --no-input --output={OUT_PREFIX}",
            cwd=tmpdir
        )
        tex_path = os.path.join(tmpdir, f"{OUT_PREFIX}.tex")
        if not os.path.exists(tex_path):
            log(f"❌ nbconvert falhou (rc={rc})")
            log(f"   stderr: {stderr[:500]}")
            save_log()
            return False
        log(f"  ✅ .tex gerado: {os.path.getsize(tex_path)} bytes")

        # 4. Edit .tex
        log("4. Ajustando .tex...")
        with open(tex_path, "r", encoding="utf-8") as f:
            conteudo = f.read()

        # Remove \maketitle
        conteudo = conteudo.replace("\\maketitle", "")
        # Remove nocaption
        conteudo = re.sub(r".*nocaption.*\n?", "", conteudo)

        # Date
        meses = {1:"janeiro",2:"fevereiro",3:"março",4:"abril",5:"maio",6:"junho",
                 7:"julho",8:"agosto",9:"setembro",10:"outubro",11:"novembro",12:"dezembro"}
        hoje = datetime.now()
        data_fmt = f"{hoje.day} de {meses[hoje.month]} de {hoje.year}"
        conteudo = conteudo.replace("\\today", data_fmt)

        # Inject packages
        if "\\begin{document}" in conteudo:
            pacotes = (
                "\\usepackage[brazil]{babel}\n"
                "\\usepackage{float}\n"
                "\\usepackage{url}\n"
                "\\usepackage{booktabs}\n"
                "\\usepackage[aboveskip=6pt,position=top]{caption}\n"
                "\\captionsetup[table]{position=top}\n"
                "\\captionsetup[figure]{position=bottom}\n"
                "\\usepackage{listings}\n"
                "\\usepackage{xcolor}\n"
                "\\definecolor{codegreen}{rgb}{0,0.6,0}\n"
                "\\definecolor{codegray}{rgb}{0.5,0.5,0.5}\n"
                "\\definecolor{codepurple}{rgb}{0.58,0,0.82}\n"
                "\\definecolor{backcolour}{rgb}{0.95,0.95,0.92}\n"
                "\\lstset{\n"
                "    backgroundcolor=\\color{backcolour},\n"
                "    commentstyle=\\color{codegreen},\n"
                "    keywordstyle=\\color{magenta},\n"
                "    numberstyle=\\small\\color{codegray},\n"
                "    stringstyle=\\color{codepurple},\n"
                "    basicstyle=\\ttfamily\\small,\n"
                "    breakatwhitespace=false,\n"
                "    breaklines=true,\n"
                "    captionpos=t,\n"
                "    keepspaces=true,\n"
                "    numbers=left,\n"
                "    numbersep=5pt,\n"
                "    showspaces=false,\n"
                "    showstringspaces=false,\n"
                "    showtabs=false,\n"
                "    tabsize=4\n"
                "}\n"
                "\\renewcommand{\\familydefault}{\\sfdefault}\n"
                "\\renewcommand{\\contentsname}{Sumário}\n"
                "\\renewcommand{\\listfigurename}{Lista de Figuras}\n"
                "\\renewcommand{\\listtablename}{Lista de Tabelas}\n"
                "\\renewcommand{\\figurename}{Figura}\n"
                "\\renewcommand{\\tablename}{Tabela}\n"
                "\\renewcommand{\\refname}{Referências}\n"
                "\\begin{document}"
            )
            conteudo = conteudo.replace("\\begin{document}", pacotes)

        # TOC after titlepage
        partes = conteudo.split("\\end{titlepage}")
        if len(partes) >= 3:
            bloco = "\n\\tableofcontents\n\\newpage\n\\listoffigures\n\\newpage\n\\listoftables\n\\newpage\n"
            conteudo = (partes[0] + "\\end{titlepage}" +
                        partes[1] + "\\end{titlepage}\n" +
                        bloco + "\\end{titlepage}".join(partes[2:]))

        # Bibliography
        if "\\appendix" in conteudo:
            p = conteudo.split("\\appendix")
            main_part = p[0].replace("\\end{document}", "")
            appendix = "\\appendix" + p[1].replace("\\end{document}", "")
            conteudo = (main_part +
                        "\n\\newpage\n\\addcontentsline{toc}{section}{Referências}\n"
                        "\\bibliographystyle{plain}\n\\bibliography{referencias}\n" +
                        "\n\\clearpage\n" + appendix + "\n\\end{document}")
        else:
            bloco_bib = ("\n\\newpage\n\\addcontentsline{toc}{section}{Referências}\n"
                         "\\bibliographystyle{plain}\n\\bibliography{referencias}\n"
                         "\\end{document}")
            conteudo = conteudo.replace("\\end{document}", bloco_bib)

        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(conteudo)
        log(f"  ✅ .tex ajustado: {len(conteudo)} chars")

        # 5. Compile
        log("5. Compilando...")
        for ext in [".aux", ".bbl", ".blg", ".pdf", ".toc", ".lof", ".lot"]:
            p = os.path.join(tmpdir, f"{OUT_PREFIX}{ext}")
            if os.path.exists(p):
                os.remove(p)

        log("  Passo 1/4: xelatex (processando referencias internas)...")
        rc, _, stderr = run(f"{latex_cmd} -interaction=nonstopmode {OUT_PREFIX}.tex", cwd=tmpdir)
        log(f"    rc={rc}")

        if has_bibtex:
            log("  Passo 2/4: bibtex (ligando referencias.bib)...")
            rc, _, _ = run(f"bibtex {OUT_PREFIX}", cwd=tmpdir)
            log(f"    rc={rc}")

        log("  Passo 3/4: xelatex (sincronizando indices)...")
        run(f"{latex_cmd} -interaction=nonstopmode {OUT_PREFIX}.tex", cwd=tmpdir)

        log("  Passo 4/4: xelatex (resolucao final)...")
        run(f"{latex_cmd} -interaction=nonstopmode {OUT_PREFIX}.tex", cwd=tmpdir)

        # 6. Collect outputs
        pdf_path = os.path.join(tmpdir, f"{OUT_PREFIX}.pdf")
        if os.path.exists(pdf_path):
            out_pdf = os.path.join(OUTPUTS_DIR, f"{OUT_PREFIX}.pdf")
            shutil.copy2(pdf_path, out_pdf)
            size_kb = os.path.getsize(out_pdf) / 1024
            log(f"✅ PDF gerado: {out_pdf} ({size_kb:.0f} KB)")
        else:
            log("❌ PDF não gerado. Verifique o log.")
            # Copy log
            tex_log = os.path.join(tmpdir, f"{OUT_PREFIX}.log")
            if os.path.exists(tex_log):
                with open(tex_log, "r", errors="replace") as f:
                    log_content = f.read()
                # Find errors
                for line in log_content.split("\n"):
                    if line.startswith("!") or "Fatal" in line:
                        log(f"  LaTeX: {line[:200]}")

        # Copy .tex
        out_tex = os.path.join(OUTPUTS_DIR, f"{OUT_PREFIX}.tex")
        shutil.copy2(tex_path, out_tex)
        log(f"✅ .tex copiado: {out_tex}")

    save_log()
    return os.path.exists(os.path.join(OUTPUTS_DIR, f"{OUT_PREFIX}.pdf"))

def save_log():
    os.makedirs(OUTPUTS_DIR, exist_ok=True)
    log_path = os.path.join(OUTPUTS_DIR, "build_article_pdf.log")
    with open(log_path, "w", encoding="utf-8") as f:
        f.write("\n".join(LOG))
    print(f"Log salvo: {log_path}")

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
