#!/usr/bin/env bash
# =====================================================================
# install_tex_colab.sh — Instala TeX mínimo no Google Colab
# =====================================================================
# Uso: bash scripts/install_tex_colab.sh
#
# Para execução no Google Colab:
#   !bash scripts/install_tex_colab.sh
#
# Após instalação, executar:
#   !bash scripts/build_pdf_abntex2.sh
# =====================================================================

set -euo pipefail

echo "=== Instalando TeX mínimo para Colab ==="

# Instalar texlive mínimo + abntex2
apt-get update -qq
apt-get install -y -qq \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-lang-portuguese \
    texlive-publishers \
    texlive-bibtex-extra \
    latexmk \
    2>/dev/null

# Verificar
echo ""
echo "Verificando instalação:"
pdflatex --version | head -1
bibtex --version | head -1

echo ""
echo "✅ TeX instalado com sucesso."
echo "   Execute: bash scripts/build_pdf_abntex2.sh"
