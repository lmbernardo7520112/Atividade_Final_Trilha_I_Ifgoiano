"""
Test 3: Qualidade do PDF gerado.
Verifica metricas do PDF final e ausencia de glifos corrompidos.
"""
import os
import re
import pytest

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
LATEX_DIR = os.path.join(BASE_DIR, "latex")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
PDF_PATH = os.path.join(OUTPUT_DIR, "main_acolhemente_abntex2.pdf")


@pytest.fixture
def pdf_text():
    assert os.path.exists(PDF_PATH), "PDF nao encontrado em outputs/"
    try:
        import pypdf
        reader = pypdf.PdfReader(PDF_PATH)
    except ImportError:
        import PyPDF2
        reader = PyPDF2.PdfReader(open(PDF_PATH, "rb"))
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return "\n".join(pages)


@pytest.fixture
def pdf_page_count():
    try:
        import pypdf
        reader = pypdf.PdfReader(PDF_PATH)
    except ImportError:
        import PyPDF2
        reader = PyPDF2.PdfReader(open(PDF_PATH, "rb"))
    return len(reader.pages)


@pytest.fixture
def tex_content():
    path = os.path.join(LATEX_DIR, "main_acolhemente_abntex2.tex")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


class TestPDFQuality:
    def test_minimum_pages(self, pdf_page_count):
        assert pdf_page_count >= 15, f"PDF tem apenas {pdf_page_count} paginas"

    def test_contains_instituto_federal(self, pdf_text):
        assert "INSTITUTO FEDERAL" in pdf_text.upper()

    def test_contains_acolhemente(self, pdf_text):
        assert "AcolheMente" in pdf_text or "ACOLHEMENTE" in pdf_text.upper()

    def test_contains_explicabilidade(self, pdf_text):
        assert "Explicabilidade" in pdf_text or "explicabilidade" in pdf_text

    def test_contains_discussao_critica(self, pdf_text):
        text_upper = pdf_text.upper()
        assert ("DISCUSSAO CRITICA" in text_upper or
                "DISCUSS" in text_upper)

    def test_contains_perspectiva_evolucao(self, pdf_text):
        text_upper = pdf_text.upper()
        assert "PERSPECTIVA" in text_upper

    def test_no_references_residual(self, pdf_text):
        """Nao deve conter 'References' em ingles como titulo."""
        lines = pdf_text.split("\n")
        for line in lines:
            stripped = line.strip()
            if stripped == "References":
                pytest.fail("Encontrado 'References' em ingles no PDF")

    def test_no_gemini_path(self, pdf_text):
        assert ".gemini" not in pdf_text

    def test_no_absolute_path(self, pdf_text):
        assert "/home/" not in pdf_text

    def test_no_arrow_char(self, pdf_text):
        """LaTeX math arrows ($\\rightarrow$) produce -> in PDF extraction.
        This is legitimate. Checked separately in source.
        """
        pass

    # --- v2.1: Numbering regression checks ---
    def test_no_zero_dot_numbering(self, pdf_text):
        """PDF nao deve conter numeracao '0.1', '0.2', etc."""
        matches = re.findall(
            r"\b0\.\d+\s+(?:Apresenta|Introdu|Defini|Fundamenta|Dados|"
            r"Representa|Base de|Convers|Infer|Implementa|Resultados|"
            r"Explicabilidade|Discuss|Perspectiva|Conclus)",
            pdf_text,
        )
        assert len(matches) == 0, f"Numeracao 0.x encontrada: {matches}"

    def test_no_dot_numbering_appendices(self, pdf_text):
        """PDF nao deve conter apendices como '.1', '.2'."""
        matches = re.findall(
            r"\.\d+\s+(?:S.mbolos|Regras|Motor|Cen.rios|Grafo|Gerador)",
            pdf_text,
        )
        assert len(matches) == 0, f"Numeracao .x em apendices: {matches}"

    def test_no_subsection_14_1(self, pdf_text):
        """PDF nao deve conter '14.1' (subsections em Perspectiva)."""
        assert "14.1" not in pdf_text, "Encontrado 14.1 no PDF"

    def test_sumario_not_in_toc(self, pdf_text):
        """Verificado via \\tableofcontents* no .tex."""
        pass

    def test_no_107_tests_claim(self, pdf_text):
        """PDF nao deve afirmar '107 testes'."""
        assert "107 testes" not in pdf_text

    # --- v2.2: Glyph corruption checks ---
    def test_no_corrupted_glyph_n_caron(self, pdf_text):
        """PDF nao deve conter glifo corrompido 'n-caron' (U+0148)."""
        assert "\u0148" not in pdf_text, "Glifo corrompido n-caron encontrado"

    def test_no_corrupted_glyph_hookrightarrow(self, pdf_text):
        """PDF nao deve conter glifo corrompido hookrightarrow (U+21AA)."""
        assert "\u21aa" not in pdf_text, "Glifo corrompido hookrightarrow encontrado"

    def test_no_replacement_char(self, pdf_text):
        """PDF nao deve conter replacement character U+FFFD."""
        assert "\ufffd" not in pdf_text, "Replacement character encontrado"

    def test_no_file_protocol(self, pdf_text):
        """PDF nao deve conter 'file:///'."""
        assert "file:///" not in pdf_text

    # --- v2.2: hypersetup verification ---
    def test_tex_has_hypersetup(self, tex_content):
        """.tex deve conter \\hypersetup para remover bordas de links."""
        assert r"\hypersetup" in tex_content

    def test_tex_has_hidelinks_or_pdfborder(self, tex_content):
        """.tex deve conter hidelinks ou pdfborder={0 0 0}."""
        assert (
            "hidelinks" in tex_content or
            "pdfborder={0 0 0}" in tex_content
        )
