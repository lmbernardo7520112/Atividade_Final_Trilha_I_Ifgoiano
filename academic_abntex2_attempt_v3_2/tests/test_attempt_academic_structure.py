# =====================================================================
# test_attempt_academic_structure.py (v3.1)
# =====================================================================
# Adapted for the v3.1 chapter structure (15 chapters, no numbered sections).
# =====================================================================
import os
import pytest

TEX_PATH = os.path.join(
    os.path.dirname(__file__), "..", "latex", "main_acolhemente_abntex2.tex"
)


@pytest.fixture
def tex_content():
    with open(TEX_PATH, "r", encoding="utf-8") as f:
        return f.read()


class TestAcademicStructure:
    EXPECTED_CHAPTERS_FRAGMENTS = [
        "Apresenta",      # Cap 1
        "Introdu",         # Cap 2
        "Defini",          # Cap 3
        "Fundamenta",      # Cap 4
        "Arquitetura de Dados",  # Cap 5
        "Explorat",        # Cap 6
        "Representa",      # Cap 7
        "Base de Conhecimento",  # Cap 8
        "Implementa",      # Cap 9
        "Sint",            # Cap 10
        "Guardrails",      # Cap 11
        "Explicabilidade", # Cap 12
        "Discuss",         # Cap 13
        "Perspectiva",     # Cap 14
        "Conclus",         # Cap 15
    ]

    @pytest.mark.parametrize("fragment", EXPECTED_CHAPTERS_FRAGMENTS)
    def test_chapter_exists(self, tex_content, fragment):
        """Each expected chapter fragment must appear in a \\chapter{} command."""
        import re
        chapters = re.findall(r"\\chapter\{([^}]+)\}", tex_content)
        found = any(fragment in ch for ch in chapters)
        assert found, f"Chapter with '{fragment}' not found. Chapters: {chapters}"

    def test_has_appendices_a_to_h(self, tex_content):
        body_after = tex_content.split("\\begin{apendicesenv}")
        assert len(body_after) == 2, "apendicesenv not found"
        appendices = body_after[1]
        import re
        ap_chapters = re.findall(r"\\chapter\{", appendices)
        assert len(ap_chapters) >= 7, f"Expected >= 7 appendix chapters, found {len(ap_chapters)}"

    def test_perspectiva_no_subsections(self, tex_content):
        import re
        match = re.search(r"\\chapter\{[^}]*Perspectiva[^}]*\}", tex_content)
        assert match, "Cap Perspectiva not found"
        start = match.end()
        next_ch = re.search(r"\\chapter\{", tex_content[start:])
        end = start + next_ch.start() if next_ch else len(tex_content)
        body = tex_content[start:end]
        sections = re.findall(r"\\section\{", body)
        assert len(sections) == 0, f"Perspectiva has {len(sections)} sections (expected 0)"
