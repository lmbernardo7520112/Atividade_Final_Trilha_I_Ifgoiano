import json
import os
import re
from datetime import datetime

# =====================================================================
# PIPELINE DE EXPORTACAO PARA PDF VIA ARTICLE (PADRAO DO TEMPLATE)
# =====================================================================

nb_name = "Trabalho_Trilha_I_AcolheMente_PB_TemplateExport"
nb_file = f"/content/{nb_name}.ipynb"

# 1. Data atual
meses = {1:"janeiro",2:"fevereiro",3:"marco",4:"abril",5:"maio",6:"junho",
         7:"julho",8:"agosto",9:"setembro",10:"outubro",11:"novembro",12:"dezembro"}
hoje = datetime.now()
data_formatada = f"{hoje.day} de {meses[hoje.month]} de {hoje.year}"

# 2. Carrega e limpa notebook
with open(nb_file, 'r', encoding='utf-8') as f:
    nb_data = json.load(f)

celulas_filtradas = []
for c in nb_data['cells']:
    src = ''.join(c.get('source', []))
    src_lower = src.lower()
    if any(kw in src_lower for kw in ['nbconvert','xelatex','bibtex']): continue
    if 'apt-get' in src_lower and 'texlive' in src_lower: continue
    if 'drive.mount' in src_lower: continue
    if 'get_ipynb' in src_lower or '_message' in src_lower: continue
    if 'referencias.bib' in src and '%%capture' in src and c['cell_type']=='code': continue
    celulas_filtradas.append(c)

nb_data['cells'] = celulas_filtradas
with open('/content/temp_limpo.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb_data, f, ensure_ascii=False, indent=2)
print(f"Celulas filtradas: {len(celulas_filtradas)}")

# 3. nbconvert
print("Convertendo notebook para LaTeX...")
!jupyter nbconvert --to latex /content/temp_limpo.ipynb --no-input --output=$nb_name

# 4. Carrega .tex
tex_path = f'/content/{nb_name}.tex'
with open(tex_path, 'r', encoding='utf-8') as f:
    conteudo = f.read()

# 5. Remove \maketitle
conteudo = conteudo.replace('\\maketitle', '')

# 6. Remove nocaption
!sed -i '/nocaption/d' /content/$nb_name.tex

# Recarrega apos sed
with open(tex_path, 'r', encoding='utf-8') as f:
    conteudo = f.read()

# 7. Data dinamica
if '\\today' in conteudo:
    conteudo = conteudo.replace('\\today', data_formatada)

# 8. Injeta pacotes e traducoes
if '\\begin{document}' in conteudo:
    traducoes = (
        '\\usepackage[brazil]{babel}\n'
        '\\usepackage{float}\n'
        '\\usepackage{url}\n'
        '\\usepackage{booktabs}\n'
        '\\usepackage[aboveskip=6pt,position=top]{caption}\n'
        '\\captionsetup[table]{position=top}\n'
        '\\captionsetup[figure]{position=bottom}\n'
        '\\usepackage{listings}\n'
        '\\usepackage{xcolor}\n'
        '\\definecolor{codegreen}{rgb}{0,0.6,0}\n'
        '\\definecolor{codegray}{rgb}{0.5,0.5,0.5}\n'
        '\\definecolor{codepurple}{rgb}{0.58,0,0.82}\n'
        '\\definecolor{backcolour}{rgb}{0.95,0.95,0.92}\n'
        '\\lstset{\n'
        '    backgroundcolor=\\color{backcolour},\n'
        '    commentstyle=\\color{codegreen},\n'
        '    keywordstyle=\\color{magenta},\n'
        '    numberstyle=\\small\\color{codegray},\n'
        '    stringstyle=\\color{codepurple},\n'
        '    basicstyle=\\ttfamily\\small,\n'
        '    breakatwhitespace=false,\n'
        '    breaklines=true,\n'
        '    captionpos=t,\n'
        '    keepspaces=true,\n'
        '    numbers=left,\n'
        '    numbersep=5pt,\n'
        '    showspaces=false,\n'
        '    showstringspaces=false,\n'
        '    showtabs=false,\n'
        '    tabsize=4\n'
        '}\n'
        '\\renewcommand{\\familydefault}{\\sfdefault}\n'
        '\\renewcommand{\\contentsname}{Sumário}\n'
        '\\renewcommand{\\listfigurename}{Lista de Figuras}\n'
        '\\renewcommand{\\listtablename}{Lista de Tabelas}\n'
        '\\renewcommand{\\figurename}{Figura}\n'
        '\\renewcommand{\\tablename}{Tabela}\n'
        '\\renewcommand{\\refname}{Referências}\n'
        '\\begin{document}'
    )
    conteudo = conteudo.replace('\\begin{document}', traducoes)

# 9. Sumario e listas apos capa
partes_titlepage = conteudo.split('\\end{titlepage}')
if len(partes_titlepage) >= 3:
    bloco_preambulo = (
        '\n\\tableofcontents\n\\newpage\n'
        '\\listoffigures\n\\newpage\n'
        '\\listoftables\n\\newpage\n'
    )
    conteudo = (partes_titlepage[0] + '\\end{titlepage}' +
                partes_titlepage[1] + '\\end{titlepage}\n' +
                bloco_preambulo +
                '\\end{titlepage}'.join(partes_titlepage[2:]))

# 10. Bibliografia
if '\\appendix' in conteudo:
    partes_apendice = conteudo.split('\\appendix')
    conteudo_principal = partes_apendice[0].replace('\\end{document}', '')
    conteudo_apendice = '\\appendix' + partes_apendice[1].replace('\\end{document}', '')
    conteudo = (
        conteudo_principal +
        '\n\\newpage\n\\addcontentsline{toc}{section}{Referências}\n\\bibliographystyle{plain}\n\\bibliography{referencias}\n' +
        '\n\\clearpage\n' + conteudo_apendice +
        '\n\\end{document}'
    )
else:
    bloco_bibtex = (
        '\n\\newpage\n'
        '\\addcontentsline{toc}{section}{Referências}\n'
        '\\bibliographystyle{plain}\n'
        '\\bibliography{referencias}\n'
        '\\end{document}'
    )
    if '\\end{document}' in conteudo:
        conteudo = conteudo.replace('\\end{document}', bloco_bibtex)

with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(conteudo)

# 11. Limpa auxiliares
for ext in ['.aux','.bbl','.blg','.pdf','.toc','.lof','.lot']:
    arq = f'/content/{nb_name}{ext}'
    if os.path.exists(arq): os.remove(arq)

# 12. Compila
print("Compilando 1/4 (processando referencias internas)...")
!cd /content && xelatex -interaction=nonstopmode $nb_name.tex > /dev/null 2>&1
print("Compilando 2/4 (ligando arquivo referencias.bib)...")
!cd /content && bibtex $nb_name > /dev/null 2>&1
print("Compilando 3/4 (sincronizando indices e sumarios)...")
!cd /content && xelatex -interaction=nonstopmode $nb_name.tex > /dev/null 2>&1
print("Compilando 4/4 (resolucao final de referencias cruzadas)...")
!cd /content && xelatex -interaction=nonstopmode $nb_name.tex > /dev/null 2>&1

# 13. Verifica resultado
pdf_path = f'/content/{nb_name}.pdf'
if os.path.exists(pdf_path):
    size_mb = os.path.getsize(pdf_path) / (1024*1024)
    print(f"\n{'='*60}")
    print(f"PDF demonstrativo gerado: {pdf_path} ({size_mb:.1f} MB)")
    print(f"Este PDF NAO substitui o PDF formal abnTeX2 v3.3.")
    print(f"{'='*60}")
else:
    print(f"\nPDF nao gerado. Verifique o log:")
    print(f"  !cat /content/{nb_name}.log | tail -30")
