#!/usr/bin/env python3
"""
Build script para compilação do documento abnTeX2 do AcolheMente.
Uso: python scripts/build_abntex2_from_colab.py
"""
import os
import shutil
import subprocess
import sys
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LATEX_DIR = os.path.join(BASE_DIR, "latex")
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")
AUDITS_DIR = os.path.join(BASE_DIR, "audits")
FIGURES_DIR = os.path.join(BASE_DIR, "figures")
APPENDICES_DIR = os.path.join(BASE_DIR, "appendices")

TEX_FILE = "main_acolhemente_abntex2"
LOG_LINES = []


def log(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    LOG_LINES.append(line)


def run(cmd, cwd=None):
    """Executa comando e retorna (returncode, stdout, stderr)."""
    result = subprocess.run(
        cmd, shell=True, cwd=cwd,
        capture_output=True, text=True, timeout=120
    )
    return result.returncode, result.stdout, result.stderr


def check_prerequisites():
    """Verifica pré-requisitos."""
    log("=== Verificação de pré-requisitos ===")

    # Logo
    logo = os.path.join(FIGURES_DIR, "logo_urutai.png")
    assert os.path.exists(logo), f"Logo não encontrado: {logo}"
    log(f"  ✅ Logo: {logo}")

    # .tex
    tex = os.path.join(LATEX_DIR, f"{TEX_FILE}.tex")
    assert os.path.exists(tex), f".tex não encontrado: {tex}"
    log(f"  ✅ .tex: {tex}")

    # .bib
    bib = os.path.join(LATEX_DIR, "referencias.bib")
    assert os.path.exists(bib), f".bib não encontrado: {bib}"
    log(f"  ✅ .bib: {bib}")

    # Apêndices
    appendices = [
        "simbolos_acolhemente.py",
        "regras_acolhemente.py",
        "motor_resolucao_acolhemente.py",
        "cenarios_sinteticos_acolhemente.py",
        "grafo_explicabilidade_acolhemente.py",
        "gerar_tabelas_resultados.py",
    ]
    for a in appendices:
        path = os.path.join(APPENDICES_DIR, a)
        assert os.path.exists(path), f"Apêndice não encontrado: {path}"
        log(f"  ✅ Apêndice: {a}")

    # xelatex
    rc, _, _ = run("which xelatex")
    if rc != 0:
        log("  ⚠️ xelatex não encontrado no PATH")
        return False
    log("  ✅ xelatex disponível")

    # bibtex
    rc, _, _ = run("which bibtex")
    if rc != 0:
        log("  ⚠️ bibtex não encontrado no PATH")
        return False
    log("  ✅ bibtex disponível")

    return True


def prepare_build_dir():
    """Prepara diretório de build com links simbólicos."""
    log("=== Preparação do diretório de build ===")
    build_dir = os.path.join(BASE_DIR, "_build")
    os.makedirs(build_dir, exist_ok=True)

    # Copiar .tex e .bib
    for f in [f"{TEX_FILE}.tex", "referencias.bib"]:
        src = os.path.join(LATEX_DIR, f)
        dst = os.path.join(build_dir, f)
        shutil.copy2(src, dst)
        log(f"  Copiado: {f}")

    # Link simbólico para figures/
    figures_link = os.path.join(build_dir, "figures")
    if os.path.exists(figures_link):
        os.remove(figures_link)
    os.symlink(FIGURES_DIR, figures_link)
    log("  Link: figures/")

    # Link simbólico para appendices/
    appendices_link = os.path.join(build_dir, "appendices")
    if os.path.exists(appendices_link):
        os.remove(appendices_link)
    os.symlink(APPENDICES_DIR, appendices_link)
    log("  Link: appendices/")

    # Gerar tabelas LaTeX
    log("  Gerando tabelas LaTeX...")
    sys.path.insert(0, APPENDICES_DIR)
    from gerar_tabelas_resultados import (
        gerar_tabela_variaveis_latex,
        gerar_tabela_regras_latex,
        gerar_tabela_cenarios_latex,
    )
    with open(os.path.join(build_dir, "tabela_variaveis.tex"), "w") as f:
        f.write(gerar_tabela_variaveis_latex())
    with open(os.path.join(build_dir, "tabela_regras.tex"), "w") as f:
        f.write(gerar_tabela_regras_latex())
    with open(os.path.join(build_dir, "tabela_cenarios.tex"), "w") as f:
        f.write(gerar_tabela_cenarios_latex())
    log("  ✅ Tabelas LaTeX geradas")

    return build_dir


def compile_latex(build_dir):
    """Compila com xelatex + bibtex."""
    log("=== Compilação LaTeX ===")

    steps = [
        ("xelatex (1/3)", f"xelatex -interaction=nonstopmode {TEX_FILE}.tex"),
        ("bibtex",        f"bibtex {TEX_FILE}"),
        ("xelatex (2/3)", f"xelatex -interaction=nonstopmode {TEX_FILE}.tex"),
        ("xelatex (3/3)", f"xelatex -interaction=nonstopmode {TEX_FILE}.tex"),
    ]

    for name, cmd in steps:
        log(f"  Executando: {name}...")
        rc, stdout, stderr = run(cmd, cwd=build_dir)
        if rc != 0 and "bibtex" not in name:
            log(f"  ⚠️ {name} retornou código {rc}")
        else:
            log(f"  ✅ {name} concluído")

    pdf_path = os.path.join(build_dir, f"{TEX_FILE}.pdf")
    return pdf_path


def collect_outputs(build_dir):
    """Copia outputs para o diretório final."""
    log("=== Coleta de outputs ===")
    os.makedirs(OUTPUTS_DIR, exist_ok=True)

    for ext in ["pdf", "tex", "log", "bbl"]:
        src = os.path.join(build_dir, f"{TEX_FILE}.{ext}")
        dst = os.path.join(OUTPUTS_DIR, f"{TEX_FILE}.{ext}")
        if os.path.exists(src):
            shutil.copy2(src, dst)
            size = os.path.getsize(dst)
            log(f"  ✅ {TEX_FILE}.{ext} ({size} bytes)")
        else:
            log(f"  ⚠️ {TEX_FILE}.{ext} não encontrado")


def write_build_report():
    """Salva relatório de build."""
    os.makedirs(AUDITS_DIR, exist_ok=True)
    report_path = os.path.join(AUDITS_DIR, "abntex2_build_report.md")

    pdf_path = os.path.join(OUTPUTS_DIR, f"{TEX_FILE}.pdf")
    pdf_exists = os.path.exists(pdf_path)
    pdf_size = os.path.getsize(pdf_path) if pdf_exists else 0

    with open(report_path, "w") as f:
        f.write("# Relatório de Build abnTeX2\n\n")
        f.write(f"**Data:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**PDF gerado:** {'SIM' if pdf_exists else 'NÃO'}\n")
        f.write(f"**Tamanho:** {pdf_size} bytes\n\n")
        f.write("## Log de execução\n\n```\n")
        for line in LOG_LINES:
            f.write(line + "\n")
        f.write("```\n")

    log(f"  Relatório: {report_path}")


def main():
    log("=" * 60)
    log("AcolheMente Escolar PB — Build abnTeX2")
    log("=" * 60)

    if not check_prerequisites():
        log("❌ Pré-requisitos não atendidos. Compilação não realizada.")
        write_build_report()
        sys.exit(1)

    build_dir = prepare_build_dir()
    pdf_path = compile_latex(build_dir)

    if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 1000:
        log(f"✅ PDF gerado: {pdf_path}")
        collect_outputs(build_dir)
    else:
        log("❌ PDF não gerado ou corrompido")

    write_build_report()
    log("=== Build concluído ===")


if __name__ == "__main__":
    main()
