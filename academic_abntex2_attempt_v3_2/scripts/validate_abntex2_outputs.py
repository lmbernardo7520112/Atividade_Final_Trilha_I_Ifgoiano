#!/usr/bin/env python3
"""
Validação dos outputs do build abnTeX2.
Uso: python scripts/validate_abntex2_outputs.py
"""
import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")
LATEX_DIR = os.path.join(BASE_DIR, "latex")

errors = []
warnings = []


def check(condition, msg):
    if not condition:
        errors.append(f"ERRO: {msg}")
        return False
    return True


def warn(condition, msg):
    if not condition:
        warnings.append(f"AVISO: {msg}")


def validate_tex():
    """Valida o .tex mestre."""
    tex_path = os.path.join(LATEX_DIR, "main_acolhemente_abntex2.tex")
    if not check(os.path.exists(tex_path), ".tex não encontrado"):
        return

    with open(tex_path, "r", encoding="utf-8") as f:
        tex = f.read()

    # abnTeX2 como classe
    check(r"\documentclass" in tex and "abntex2" in tex,
          "Não usa abntex2 como classe")
    check(r"\usepackage{abntex2}" not in tex,
          "Usa abntex2 como pacote (proibido)")
    check(r"\usepackage[alf]{abntex2cite}" in tex,
          "Falta abntex2cite")
    check(r"\bibliographystyle{abntex2-alf}" in tex,
          "Falta abntex2-alf")
    check(r"\bibliography{referencias}" in tex,
          "Falta bibliography")

    # Citações
    cites = re.findall(r"\\cite\w*\{[^}]+\}", tex)
    check(len(cites) >= 10, f"Apenas {len(cites)} citações (mínimo 10)")

    # Capa
    check(r"\begin{titlepage}" in tex, "Falta capa LaTeX")
    check(r"\tableofcontents" in tex, "Falta sumário")

    # Numeração duplicada
    sections = re.findall(r"\\(?:section|subsection)\{(.+?)\}", tex)
    for s in sections:
        check(not re.match(r"^\d+[\.\s]", s),
              f"Numeração manual em título: '{s}'")

    # Apêndices
    check(r"\appendix" in tex, "Falta \\appendix")

    print(f"  .tex: {len(cites)} citações, {len(sections)} seções")


def validate_bib():
    """Valida o .bib."""
    bib_path = os.path.join(LATEX_DIR, "referencias.bib")
    if not check(os.path.exists(bib_path), ".bib não encontrado"):
        return

    with open(bib_path, "r", encoding="utf-8") as f:
        bib = f.read()

    entries = re.findall(r"@\w+\{(\w+),", bib)
    check(len(entries) >= 10, f"Apenas {len(entries)} entradas BibTeX (mínimo 10)")

    required = [
        "ibge_pense_2024", "brasil_lgpd_2018", "brasil_eca_1990",
        "brasil_pse_2007", "russell_norvig_2022", "brachman_levesque_2004",
        "genesereth_nilsson_1987", "ribeiro_lime_2016",
        "jobin_ai_ethics_2019", "who_mental_health_2022",
    ]
    for r in required:
        check(r in entries, f"Entrada BibTeX faltando: {r}")

    print(f"  .bib: {len(entries)} entradas")


def validate_pdf():
    """Valida o PDF se existir."""
    pdf_path = os.path.join(OUTPUTS_DIR, "main_acolhemente_abntex2.pdf")
    if not os.path.exists(pdf_path):
        warn(False, "PDF não encontrado (build pode não ter sido executado)")
        return

    size = os.path.getsize(pdf_path)
    check(size > 10000, f"PDF muito pequeno: {size} bytes")
    print(f"  PDF: {size} bytes")


def main():
    print("=" * 60)
    print("Validação de Outputs abnTeX2 — AcolheMente")
    print("=" * 60)

    validate_tex()
    validate_bib()
    validate_pdf()

    print()
    if warnings:
        print(f"⚠️  {len(warnings)} avisos:")
        for w in warnings:
            print(f"  {w}")

    if errors:
        print(f"❌ {len(errors)} erros:")
        for e in errors:
            print(f"  {e}")
        sys.exit(1)
    else:
        print("✅ Validação aprovada!")
        sys.exit(0)


if __name__ == "__main__":
    main()
