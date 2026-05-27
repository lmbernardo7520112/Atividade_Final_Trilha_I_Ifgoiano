"""
Test 2: Estrutura acadêmica do documento LaTeX.
Verifica conformidade com Template_Trabalho_Trilha_I.
"""
import os
import re
import pytest

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
LATEX_DIR = os.path.join(BASE_DIR, "latex")


@pytest.fixture
def tex_content():
    path = os.path.join(LATEX_DIR, "main_acolhemente_abntex2.tex")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


REQUIRED_CHAPTERS = [
    "Apresentação do Aluno e Contexto",
    "Introdução",
    "Definição do Problema e Objetivos",
    "Fundamentação Metodológica",
    "Dados e Governança",
    "Representação do Conhecimento",
    "Base de Conhecimento e Regras",
    "Conversão para Forma Normal Conjuntiva",
    "Inferência por Resolução",
    "Implementação Computacional",
    "Resultados e Comparações",
    "Explicabilidade",
    "Discussão Crítica",
    "Perspectiva de Evolução do Trabalho",
    "Conclusão",
]


class TestAcademicStructure:
    @pytest.mark.parametrize("chapter_title", REQUIRED_CHAPTERS)
    def test_chapter_exists(self, tex_content, chapter_title):
        # Must exist as \chapter{...}, not \section{...}
        pattern = re.compile(r"\\chapter\{[^}]*" + re.escape(chapter_title[:20]))
        assert pattern.search(tex_content), (
            f"\\chapter{{{chapter_title}}} não encontrado no .tex"
        )

    def test_has_appendix(self, tex_content):
        assert r"\begin{apendicesenv}" in tex_content

    def test_has_appendices_a_to_f(self, tex_content):
        appendices = [
            "Símbolos Proposicionais",
            "Regras Lógicas",
            "Motor de Inferência",
            "Cenários Sintéticos",
            "Grafo de Explicabilidade",
            "Gerador de Tabelas",
        ]
        for a in appendices:
            assert a in tex_content, f"Apêndice '{a}' não encontrado"

    def test_no_manual_numbering(self, tex_content):
        """Nenhum \\chapter com numeração manual como \\chapter{1. ...}"""
        manual = re.findall(r"\\chapter\{\d+\.\s", tex_content)
        assert len(manual) == 0, f"Numeração manual encontrada: {manual}"

    def test_no_duplicate_heading_numbers(self, tex_content):
        """Sem números de seção duplicados."""
        chapter_titles = re.findall(r"\\chapter\{([^}]+)\}", tex_content)
        seen = set()
        for t in chapter_titles:
            assert t not in seen, f"Capítulo duplicado: {t}"
            seen.add(t)

    def test_apresentacao_aluno(self, tex_content):
        assert "Leonardo Maximino Bernardo" in tex_content

    def test_has_lstinputlisting(self, tex_content):
        lst = re.findall(r"\\lstinputlisting", tex_content)
        assert len(lst) >= 6, f"Apenas {len(lst)} \\lstinputlisting"

    # --- v2.1: Perspectiva de Evolução sem subsections ---
    def test_perspectiva_no_subsections(self, tex_content):
        """A seção 'Perspectiva de Evolução' não deve ter \\section ou \\subsection internas."""
        # Find the Perspectiva chapter and the next chapter
        persp_match = re.search(
            r"\\chapter\{Perspectiva de Evolução do Trabalho\}",
            tex_content,
        )
        assert persp_match, "Capítulo 'Perspectiva de Evolução' não encontrado"
        start_pos = persp_match.end()

        # Find the next \chapter
        next_chapter = re.search(r"\\chapter\{", tex_content[start_pos:])
        if next_chapter:
            end_pos = start_pos + next_chapter.start()
        else:
            end_pos = len(tex_content)

        persp_body = tex_content[start_pos:end_pos]
        subsections = re.findall(r"\\(?:sub)?section\{", persp_body)
        assert len(subsections) == 0, (
            f"Perspectiva de Evolução contém {len(subsections)} subseções"
        )

    # --- v2.1: chapter-level structure validation ---
    def test_main_sections_are_chapters(self, tex_content):
        """As seções principais devem ser \\chapter, não \\section."""
        # Check that there are no top-level \\section before \\begin{apendicesenv}
        apendices_start = tex_content.find(r"\begin{apendicesenv}")
        if apendices_start == -1:
            apendices_start = len(tex_content)
        main_body = tex_content[:apendices_start]
        # Sections should not exist in main body (only chapters)
        sections = re.findall(r"\\section\{", main_body)
        assert len(sections) == 0, (
            f"Encontrados {len(sections)} \\section no corpo principal "
            f"(devem ser \\chapter)"
        )

    def test_no_107_tests_claim(self, tex_content):
        """O documento não deve afirmar '107 testes'."""
        assert "107 testes" not in tex_content
