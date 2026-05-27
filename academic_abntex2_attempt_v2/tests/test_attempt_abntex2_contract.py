"""
Test 1: Contrato abnTeX2 do documento LaTeX.
Verifica conformidade com abnTeX2 v2.1.
"""
import os
import re
import pytest

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
LATEX_DIR = os.path.join(BASE_DIR, "latex")


@pytest.fixture
def tex_content():
    path = os.path.join(LATEX_DIR, "main_acolhemente_abntex2.tex")
    assert os.path.exists(path), ".tex não encontrado"
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


@pytest.fixture
def bib_content():
    path = os.path.join(LATEX_DIR, "referencias.bib")
    assert os.path.exists(path), ".bib não encontrado"
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


class TestAbnTeX2Contract:
    def test_tex_exists(self):
        assert os.path.exists(os.path.join(LATEX_DIR, "main_acolhemente_abntex2.tex"))

    def test_uses_abntex2_class(self, tex_content):
        assert r"\documentclass" in tex_content
        assert "abntex2}" in tex_content

    def test_not_abntex2_package(self, tex_content):
        assert r"\usepackage{abntex2}" not in tex_content

    def test_uses_abntex2cite(self, tex_content):
        assert r"\usepackage[alf]{abntex2cite}" in tex_content

    def test_uses_abntex2_alf_style(self, tex_content):
        assert r"\bibliographystyle{abntex2-alf}" in tex_content

    def test_has_bibliography(self, tex_content):
        assert r"\bibliography{referencias}" in tex_content

    def test_at_least_10_citations(self, tex_content):
        cites = re.findall(r"\\cite\w*\{[^}]+\}", tex_content)
        assert len(cites) >= 10, f"Apenas {len(cites)} citações"

    def test_bib_at_least_10_entries(self, bib_content):
        entries = re.findall(r"@\w+\{", bib_content)
        assert len(entries) >= 10, f"Apenas {len(entries)} entradas"

    def test_has_titlepage(self, tex_content):
        # memoir/abntex2 uses thispagestyle{empty} instead of titlepage env
        assert (r"\begin{titlepage}" in tex_content or
                r"\thispagestyle{empty}" in tex_content)

    def test_has_tableofcontents(self, tex_content):
        assert r"\tableofcontents" in tex_content

    def test_has_instituto_federal(self, tex_content):
        assert "INSTITUTO FEDERAL GOIANO" in tex_content

    def test_has_logo(self, tex_content):
        assert "logo_urutai.png" in tex_content

    # --- v2.1: chapter-level structure ---
    def test_uses_chapter_not_section_for_main(self, tex_content):
        """TEX deve usar \\chapter para seções principais, não \\section."""
        assert r"\chapter{Apresentação do Aluno e Contexto}" in tex_content
        assert r"\section{Apresentação do Aluno e Contexto}" not in tex_content

    def test_uses_apendicesenv(self, tex_content):
        """TEX deve usar \\begin{apendicesenv} para apêndices."""
        assert r"\begin{apendicesenv}" in tex_content

    def test_uses_partapendices(self, tex_content):
        """TEX deve usar \\partapendices dentro de apendicesenv."""
        assert r"\partapendices" in tex_content

    def test_no_bare_appendix(self, tex_content):
        """TEX não deve usar \\appendix diretamente (deve usar apendicesenv)."""
        # Only check outside of comments
        lines = tex_content.split("\n")
        for line in lines:
            stripped = line.strip()
            if stripped == r"\appendix":
                pytest.fail("Usa \\appendix diretamente em vez de apendicesenv")
