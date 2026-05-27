#!/bin/bash
# build_academic_pdf.sh — Pipeline de geração do PDF acadêmico
set -e

PROJ_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJ_DIR"

echo "=== Etapa 1: Gerar .tex a partir do notebook ==="
./.venv/bin/jupyter nbconvert \
    --to latex \
    --output-dir=reports/tex \
    notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb

TEX_FILE="reports/tex/Trabalho_Trilha_I_AcolheMente_PB.tex"
echo "  → $TEX_FILE gerado"

echo "=== Etapa 2: Copiar recursos ==="
cp templates/abntex2/referencias.bib reports/tex/referencias.bib
if [ -f "logo_urutai.png" ]; then
    cp logo_urutai.png reports/tex/logo_urutai.png
fi

echo "=== Etapa 3: Inserir bibliography no .tex ==="
if ! grep -q 'bibliographystyle' "$TEX_FILE"; then
    sed -i 's/\\end{document}/\\bibliographystyle{plain}\n\\bibliography{referencias}\n\\end{document}/' "$TEX_FILE"
fi

echo "=== Etapa 4: Fix tabular issues ==="
./.venv/bin/python scripts/fix_latex_tables.py "$TEX_FILE"

echo "=== Etapa 5: Compilar com xelatex ==="
cd reports/tex
xelatex -interaction=nonstopmode \
    Trabalho_Trilha_I_AcolheMente_PB.tex > /dev/null 2>&1 || true

echo "=== Etapa 6: Executar bibtex ==="
bibtex Trabalho_Trilha_I_AcolheMente_PB > /dev/null 2>&1 || true

echo "=== Etapa 7: Recompilar (2x) ==="
xelatex -interaction=nonstopmode \
    Trabalho_Trilha_I_AcolheMente_PB.tex > /dev/null 2>&1 || true
xelatex -interaction=nonstopmode \
    Trabalho_Trilha_I_AcolheMente_PB.tex > /dev/null 2>&1 || true

echo "=== Etapa 8: Mover PDF ==="
cd "$PROJ_DIR"
mkdir -p reports/pdf
cp reports/tex/Trabalho_Trilha_I_AcolheMente_PB.pdf \
    reports/pdf/Trabalho_Trilha_I_AcolheMente_PB.pdf

PDF="reports/pdf/Trabalho_Trilha_I_AcolheMente_PB.pdf"
if [ -f "$PDF" ]; then
    SIZE=$(stat -c%s "$PDF")
    PAGES=$(./.venv/bin/python -c "import PyPDF2; r=PyPDF2.PdfReader(open('$PDF','rb')); print(len(r.pages))")
    echo "✅ PDF gerado: $PDF ($SIZE bytes, $PAGES páginas)"
else
    echo "❌ PDF NÃO gerado!"
    exit 1
fi
