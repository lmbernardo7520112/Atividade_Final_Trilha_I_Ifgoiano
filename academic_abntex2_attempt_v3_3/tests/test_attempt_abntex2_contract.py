# =====================================================================
# test_attempt_abntex2_contract.py (v3.1)
# =====================================================================
# Adapted for v3.1: verifies abnTeX2 compliance without checking for
# specific section counts (v3.1 uses no numbered sections).
# =====================================================================
import os
import re
import pytest

TEX_PATH = os.path.join(
    os.path.dirname(__file__), "..", "latex", "main_acolhemente_abntex2.tex"
)


@pytest.fixture
def tex_content():
    with open(TEX_PATH, "r", encoding="utf-8") as f:
        return f.read()


class TestAbnTeX2Contract:
    def test_uses_abntex2_class(self, tex_content):
        assert "abntex2" in tex_content

    def test_uses_abntex2_cite(self, tex_content):
        assert "abntex2cite" in tex_content or "abntex2-alf" in tex_content

    def test_has_bibliography(self, tex_content):
        assert "\\bibliography{" in tex_content

    def test_has_appendices(self, tex_content):
        assert "\\begin{apendicesenv}" in tex_content

    def test_has_tableofcontents(self, tex_content):
        assert "\\tableofcontents" in tex_content

    def test_uses_chapter_for_main(self, tex_content):
        """v3.1 uses \\chapter{} and zero \\section{} in body."""
        body = tex_content.split("\\begin{apendicesenv}")[0]
        chapters = re.findall(r"\\chapter\{", body)
        sections = re.findall(r"\\section\{", body)
        assert len(chapters) >= 10, f"Too few chapters: {len(chapters)}"
        assert len(sections) <= 3, f"Too many sections: {len(sections)}"

    def test_has_lstinputlisting(self, tex_content):
        assert "\\lstinputlisting" in tex_content

    def test_no_unicode_dashes(self, tex_content):
        """No raw unicode em-dashes that could cause extraction issues."""
        assert "\u2014" not in tex_content, "Raw unicode em-dash found; use ---"
        assert "\u2013" not in tex_content, "Raw unicode en-dash found; use --"

    def test_has_lmodern(self, tex_content):
        """lmodern package required for clean text extraction."""
        assert "\\usepackage{lmodern}" in tex_content
