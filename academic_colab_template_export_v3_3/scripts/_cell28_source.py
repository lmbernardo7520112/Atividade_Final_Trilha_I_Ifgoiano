import json
import os
import re
import shutil
from datetime import datetime

# =====================================================================
# PIPELINE DE EXPORTACAO PARA PDF VIA ARTICLE (PADRAO DO TEMPLATE)
# =====================================================================
# Segue a logica funcional do template Resposta_Trabalho_Trilha_I.ipynb
# Gera PDF via: nbconvert -> article -> xelatex + bibtex
# =====================================================================

nb_name = "Trabalho_Trilha_I_AcolheMente_PB_TemplateExport"
nb_file = f"/content/{nb_name}.ipynb"
build_dir = "/content/acolhemente_article_build"

# 0. Cria diretorio de build limpo
if os.path.exists(build_dir):
    shutil.rmtree(build_dir)
os.makedirs(build_dir, exist_ok=True)

# 1. Copia assets para o build dir
shutil.copy2(nb_file, f"{build_dir}/{nb_name}.ipynb")
if os.path.exists("/content/logo_urutai.png"):
    shutil.copy2("/content/logo_urutai.png", f"{build_dir}/logo_urutai.png")
if os.path.exists("/content/referencias.bib"):
    shutil.copy2("/content/referencias.bib", f"{build_dir}/referencias.bib")

# 2. Verifica e copia os .py dos apendices
py_files = [
    "simbolos_acolhemente.py",
    "regras_acolhemente.py",
    "motor_resolucao_acolhemente.py",
    "cenarios_sinteticos_acolhemente.py",
    "grafo_explicabilidade_acolhemente.py",
    "gerar_tabelas_resultados.py",
]
for py in py_files:
    src = f"/content/{py}"
    if not os.path.exists(src):
        print(f"ERRO: {py} nao encontrado. Execute as celulas %%writefile primeiro.")
        raise FileNotFoundError(f"Arquivo obrigatorio ausente: {py}")
    shutil.copy2(src, f"{build_dir}/{py}")
    print(f"  Copiado: {py}")

# 3. Sanitiza caracteres acentuados nos .py para compatibilidade com listings/xelatex
for py in py_files:
    path = f"{build_dir}/{py}"
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    # listings com xelatex lida bem com UTF-8, mas garantimos
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# 4. Data atual
meses = {1:"janeiro",2:"fevereiro",3:"marco",4:"abril",5:"maio",6:"junho",
         7:"julho",8:"agosto",9:"setembro",10:"outubro",11:"novembro",12:"dezembro"}
hoje = datetime.now()
data_formatada = f"{hoje.day} de {meses[hoje.month]} de {hoje.year}"

# 5. Carrega e limpa notebook
with open(f"{build_dir}/{nb_name}.ipynb", 'r', encoding='utf-8') as f:
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
clean_nb = f"{build_dir}/temp_limpo.ipynb"
with open(clean_nb, 'w', encoding='utf-8') as f:
    json.dump(nb_data, f, ensure_ascii=False, indent=2)
print(f"Celulas filtradas: {len(celulas_filtradas)}")

# 6. nbconvert
print("Convertendo notebook para LaTeX...")
os.system(f'cd {build_dir} && jupyter nbconvert --to latex temp_limpo.ipynb --no-input --output={nb_name}')

tex_path = f"{build_dir}/{nb_name}.tex"
if not os.path.exists(tex_path):
    raise RuntimeError("nbconvert falhou: .tex nao gerado")

with open(tex_path, 'r', encoding='utf-8') as f:
    conteudo = f.read()

# =====================================================================
# POS-PROCESSAMENTO LATEX
# =====================================================================

# A) Remover titulo automatico do nbconvert ("temp_limpo")
conteudo = re.sub(r'\\title\{[^}]*\}', '', conteudo)
conteudo = re.sub(r'\\author\{[^}]*\}', '', conteudo)
conteudo = re.sub(r'\\date\{[^}]*\}', '', conteudo)
conteudo = conteudo.replace('\\maketitle', '')

# Remover qualquer referencia residual a "temp_limpo"
conteudo = conteudo.replace('temp_limpo', '')
conteudo = conteudo.replace('temp\\_limpo', '')

# Remover nocaption
conteudo = re.sub(r'.*nocaption.*\n?', '', conteudo)

# Data dinamica
if '\\today' in conteudo:
    conteudo = conteudo.replace('\\today', data_formatada)

# B) Injeta pacotes e traducoes ANTES de \begin{document}
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
        '    tabsize=4,\n'
        '    inputencoding=utf8,\n'
        '    extendedchars=true,\n'
        '    literate=\n'
        '      {á}{{\\\'a}}1 {à}{{\\`a}}1 {â}{{\\^a}}1 {ã}{{\\~a}}1\n'
        '      {é}{{\\\'e}}1 {ê}{{\\^e}}1\n'
        '      {í}{{\\\'i}}1\n'
        '      {ó}{{\\\'o}}1 {ô}{{\\^o}}1 {õ}{{\\~o}}1\n'
        '      {ú}{{\\\'u}}1\n'
        '      {ç}{{\\c{c}}}1\n'
        '      {Á}{{\\\'A}}1 {É}{{\\\'E}}1 {Í}{{\\\'I}}1 {Ó}{{\\\'O}}1 {Ú}{{\\\'U}}1\n'
        '      {Ç}{{\\c{C}}}1\n'
        '      {ã}{{\\~a}}1 {õ}{{\\~o}}1\n'
        '}\n'
        '\\renewcommand{\\familydefault}{\\sfdefault}\n'
        '\\renewcommand{\\contentsname}{Sumário}\n'
        '\\renewcommand{\\figurename}{Figura}\n'
        '\\renewcommand{\\tablename}{Tabela}\n'
        '\\renewcommand{\\refname}{Referências}\n'
        '\\begin{document}'
    )
    conteudo = conteudo.replace('\\begin{document}', traducoes)

# C) Sumario apos segunda titlepage — SEM Lista de Figuras/Tabelas
partes_titlepage = conteudo.split('\\end{titlepage}')
if len(partes_titlepage) >= 3:
    bloco_preambulo = (
        '\n\\tableofcontents\n\\newpage\n'
    )
    conteudo = (partes_titlepage[0] + '\\end{titlepage}' +
                partes_titlepage[1] + '\\end{titlepage}\n' +
                bloco_preambulo +
                '\\end{titlepage}'.join(partes_titlepage[2:]))

# D) Remover \listoffigures e \listoftables residuais
conteudo = re.sub(r'\\listoffigures\s*', '', conteudo)
conteudo = re.sub(r'\\listoftables\s*', '', conteudo)

# E) APENDICES: Substituir placeholders por lstinputlisting
# Primeiro, remover o bloco de apendices gerado pelo nbconvert (placeholders)
apendices_info = [
    ("simbolos_acolhemente.py", "Símbolos Proposicionais do AcolheMente", "lst:simbolos"),
    ("regras_acolhemente.py", "Regras Lógicas e CNF", "lst:regras"),
    ("motor_resolucao_acolhemente.py", "Motor de Inferência por Resolução", "lst:motor"),
    ("cenarios_sinteticos_acolhemente.py", "Cenários Sintéticos de Validação", "lst:cenarios"),
    ("grafo_explicabilidade_acolhemente.py", "Grafo de Explicabilidade", "lst:grafo"),
    ("gerar_tabelas_resultados.py", "Gerador de Tabelas de Resultados", "lst:tabelas"),
]

# Construir bloco de apendices nativo
bloco_apendices = (
    '\n\\clearpage\n'
    '\\appendix\n'
    '\\renewcommand{\\thesection}{Apêndice \\Alph{section}}\n\n'
)
for py_file, titulo, label in apendices_info:
    bloco_apendices += (
        f'\\section{{{titulo}}}\n'
        f'\\lstinputlisting[language=Python, caption={{{titulo}.}}, label={{{label}}}]{{{py_file}}}\n\n'
    )

# Remover bloco de apendices existente (gerado pelo nbconvert)
if '\\appendix' in conteudo:
    # Tudo entre \appendix e \end{document}
    partes = conteudo.split('\\appendix')
    conteudo_principal = partes[0]
    # Remover \end{document} do principal
    conteudo_principal = conteudo_principal.replace('\\end{document}', '')
    conteudo = conteudo_principal + bloco_apendices + '\n\\end{document}'
else:
    # Nao ha \appendix, inserir antes de \end{document}
    conteudo = conteudo.replace('\\end{document}', bloco_apendices + '\n\\end{document}')

# F) Bibliografia: NAO inserir \bibliography se ja tem secao manual
# A secao 8 "Referencias Bibliograficas" ja esta no corpo do notebook
# Remover qualquer \bibliography{...} residual
conteudo = re.sub(r'\\addcontentsline\{toc\}\{section\}\{Refer[êe]ncias\}', '', conteudo)
conteudo = re.sub(r'\\bibliographystyle\{[^}]*\}', '', conteudo)
conteudo = re.sub(r'\\bibliography\{[^}]*\}', '', conteudo)

# Limpar newpages orfaos antes de \end{document}
conteudo = re.sub(r'(\\newpage\s*)+\\end\{document\}', '\\end{document}', conteudo)

# Salvar .tex final
with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(conteudo)

print(f"LaTeX processado: {len(conteudo)} chars")

# =====================================================================
# COMPILACAO
# =====================================================================

# Limpa auxiliares
for ext in ['.aux','.bbl','.blg','.pdf','.toc','.lof','.lot','.out']:
    arq = f"{build_dir}/{nb_name}{ext}"
    if os.path.exists(arq): os.remove(arq)

print("Compilando 1/3 (processando referencias internas)...")
os.system(f'cd {build_dir} && xelatex -interaction=nonstopmode {nb_name}.tex > /dev/null 2>&1')
print("Compilando 2/3 (sincronizando indices e sumarios)...")
os.system(f'cd {build_dir} && xelatex -interaction=nonstopmode {nb_name}.tex > /dev/null 2>&1')
print("Compilando 3/3 (resolucao final de referencias cruzadas)...")
os.system(f'cd {build_dir} && xelatex -interaction=nonstopmode {nb_name}.tex > /dev/null 2>&1')

# Resultado
pdf_path = f"{build_dir}/{nb_name}.pdf"
if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 1000:
    size_mb = os.path.getsize(pdf_path) / (1024*1024)
    # Copia para /content/ para facil download
    shutil.copy2(pdf_path, f"/content/{nb_name}.pdf")
    print(f"\n{'='*60}")
    print(f"PDF demonstrativo gerado: /content/{nb_name}.pdf ({size_mb:.1f} MB)")
    print(f"Este PDF NAO substitui o PDF formal abnTeX2 v3.3.")
    print(f"{'='*60}")
else:
    print(f"\nPDF nao gerado. Verifique o log:")
    print(f"  !cat {build_dir}/{nb_name}.log | tail -30")
