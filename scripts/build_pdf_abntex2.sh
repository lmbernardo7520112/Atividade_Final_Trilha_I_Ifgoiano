#!/usr/bin/env bash
# =====================================================================
# build_pdf_abntex2.sh — Compila o PDF do trabalho
# =====================================================================
# Uso: bash scripts/build_pdf_abntex2.sh
#
# Estratégia:
#   1. Tenta nbconvert --to pdf (usa xelatex internamente)
#   2. Fallback: pdflatex manual com triple-pass + bibtex
#
# Pré-requisitos: texlive ou TinyTeX + pandoc/pypandoc
# Saída: reports/pdf/Trabalho_Trilha_I_AcolheMente_PB.pdf
# =====================================================================

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PDF_DIR="${PROJECT_ROOT}/reports/pdf"
TEX_DIR="${PROJECT_ROOT}/reports/tex"
NOTEBOOK="${PROJECT_ROOT}/notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb"

echo "=== AcolheMente Escolar PB — Build PDF ==="
echo "Project root: ${PROJECT_ROOT}"

# Ativar venv se existir
source "${PROJECT_ROOT}/.venv/bin/activate" 2>/dev/null || true

# Adicionar TinyTeX ao PATH se existir
export PATH="$HOME/bin:$HOME/.TinyTeX/bin/x86_64-linux:$PATH"

mkdir -p "${PDF_DIR}" "${TEX_DIR}"

# ==== ESTRATÉGIA 1: nbconvert --to pdf (recomendado) ====
if command -v jupyter &> /dev/null; then
    echo "Tentando: jupyter nbconvert --to pdf..."
    if jupyter nbconvert --to pdf \
        --output-dir="${PDF_DIR}" \
        "${NOTEBOOK}" 2>&1; then

        if [ -f "${PDF_DIR}/Trabalho_Trilha_I_AcolheMente_PB.pdf" ]; then
            SIZE=$(stat -c%s "${PDF_DIR}/Trabalho_Trilha_I_AcolheMente_PB.pdf" 2>/dev/null || echo "0")
            echo ""
            echo "✅ PDF gerado: ${PDF_DIR}/Trabalho_Trilha_I_AcolheMente_PB.pdf (${SIZE} bytes)"

            # Gerar .tex também para referência
            jupyter nbconvert --to latex \
                --output-dir="${TEX_DIR}" \
                "${NOTEBOOK}" 2>/dev/null || true

            echo "=== Build concluído com sucesso ==="
            exit 0
        fi
    fi
    echo "⚠️  nbconvert --to pdf falhou. Tentando fallback..."
fi

# ==== ESTRATÉGIA 2: pdflatex manual ====
if ! command -v pdflatex &> /dev/null; then
    echo "❌ Nem jupyter nbconvert nem pdflatex estão disponíveis."
    echo ""
    echo "Instale um dos seguintes:"
    echo "  1. TinyTeX: wget -qO- https://yihui.org/tinytex/install-bin-unix.sh | sh"
    echo "  2. texlive: sudo apt install texlive-full"
    echo "  3. Colab: bash scripts/install_tex_colab.sh"
    exit 1
fi

# Gerar .tex via nbconvert se não existir
if [ ! -f "${TEX_DIR}/Trabalho_Trilha_I_AcolheMente_PB.tex" ]; then
    echo "Gerando .tex via nbconvert..."
    jupyter nbconvert --to latex \
        --output-dir="${TEX_DIR}" "${NOTEBOOK}"
fi

# Copiar referências e figuras
cp "${PROJECT_ROOT}/templates/abntex2/referencias.bib" "${TEX_DIR}/" 2>/dev/null || true
cp "${PROJECT_ROOT}/reports/figures/"*.png "${TEX_DIR}/" 2>/dev/null || true

# Compilar
cd "${TEX_DIR}"
echo "Compilando pdflatex (1/3)..."
pdflatex -interaction=nonstopmode Trabalho_Trilha_I_AcolheMente_PB.tex || true

echo "Compilando bibtex..."
bibtex Trabalho_Trilha_I_AcolheMente_PB || true

echo "Compilando pdflatex (2/3)..."
pdflatex -interaction=nonstopmode Trabalho_Trilha_I_AcolheMente_PB.tex || true

echo "Compilando pdflatex (3/3)..."
pdflatex -interaction=nonstopmode Trabalho_Trilha_I_AcolheMente_PB.tex || true

# Mover PDF para destino
if [ -f "Trabalho_Trilha_I_AcolheMente_PB.pdf" ]; then
    mv Trabalho_Trilha_I_AcolheMente_PB.pdf "${PDF_DIR}/"
    echo ""
    echo "✅ PDF gerado: ${PDF_DIR}/Trabalho_Trilha_I_AcolheMente_PB.pdf"
else
    echo ""
    echo "❌ PDF não foi gerado. Verifique os logs acima."
    exit 1
fi

# Limpar auxiliares
rm -f *.aux *.log *.bbl *.blg *.out *.toc *.lof *.lot 2>/dev/null || true

echo "=== Build concluído ==="
