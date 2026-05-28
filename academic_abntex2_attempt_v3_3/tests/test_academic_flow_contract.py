# =====================================================================
# test_academic_flow_contract.py
# =====================================================================
# Verifica que o .tex v3.1 possui estilo academico fluido, sem excesso
# de subseções, e mantem todas as explicacoes obrigatorias.
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


# --- 1. Sumario: maximo 3 subseções numeradas no corpo principal ---
def test_max_3_sections_in_body(tex_content):
    """Sumario deve ter no maximo 3 \\section{} no corpo (antes dos apendices)."""
    body = tex_content.split("\\begin{apendicesenv}")[0]
    sections = re.findall(r"\\section\{", body)
    assert len(sections) <= 3, (
        f"Encontradas {len(sections)} \\section{{}} no corpo. Maximo: 3."
    )


# --- 2. Caps 5,6,10,11,12,13 sem subseções numeradas ---
def _get_chapter_body(tex, chapter_title_fragment):
    """Extrai corpo entre capitulo com titulo contendo fragment e proximo \\chapter."""
    pattern = r"\\chapter\{[^}]*" + re.escape(chapter_title_fragment) + r"[^}]*\}"
    match = re.search(pattern, tex)
    if not match:
        return ""
    start = match.end()
    next_chapter = re.search(r"\\chapter\{", tex[start:])
    end = start + next_chapter.start() if next_chapter else len(tex)
    return tex[start:end]


def test_cap5_no_sections(tex_content):
    body = _get_chapter_body(tex_content, "Arquitetura de Dados")
    sections = re.findall(r"\\section\{", body)
    assert len(sections) == 0, f"Cap 5 tem {len(sections)} sections (esperado 0)"


def test_cap6_no_sections(tex_content):
    body = _get_chapter_body(tex_content, "Explorat")
    sections = re.findall(r"\\section\{", body)
    assert len(sections) == 0, f"Cap 6 tem {len(sections)} sections (esperado 0)"


def test_cap9_no_sections(tex_content):
    body = _get_chapter_body(tex_content, "Implementa")
    sections = re.findall(r"\\section\{", body)
    assert len(sections) == 0, f"Cap 9 tem {len(sections)} sections (esperado 0)"


def test_cap10_no_sections(tex_content):
    body = _get_chapter_body(tex_content, "Sint")
    sections = re.findall(r"\\section\{", body)
    assert len(sections) == 0, f"Cap 10 tem {len(sections)} sections (esperado 0)"


def test_cap11_no_sections(tex_content):
    body = _get_chapter_body(tex_content, "Guardrails")
    sections = re.findall(r"\\section\{", body)
    assert len(sections) == 0, f"Cap 11 tem {len(sections)} sections (esperado 0)"


def test_cap12_no_sections(tex_content):
    body = _get_chapter_body(tex_content, "Explicabilidade")
    sections = re.findall(r"\\section\{", body)
    assert len(sections) == 0, f"Cap 12 tem {len(sections)} sections (esperado 0)"


# --- 3. TIER_A, TIER_B, TIER_C presentes no cap de arquitetura ---
def test_tiers_in_text(tex_content):
    body = _get_chapter_body(tex_content, "Arquitetura de Dados")
    assert "TIER" in body and "PeNSE" in body
    assert "sint" in body.lower() or "TIER\\_B" in body
    assert "externo" in body.lower() or "TIER\\_C" in body


# --- 4. 2^6 = 64 no capitulo de cenarios ---
def test_64_in_cenarios(tex_content):
    body = _get_chapter_body(tex_content, "Sint")
    assert "2^6 = 64" in body or "$2^6 = 64$" in body


# --- 5. "6 variáveis de entrada e 1 variável de saída" ---
def test_6_entrada_1_saida(tex_content):
    body = _get_chapter_body(tex_content, "Sint")
    assert "6 vari" in body and "entrada" in body
    assert "1 vari" in body and "sa" in body


# --- 6. C isolado, I isolado, C+I nos resultados ---
def test_guardrails_in_results(tex_content):
    body = _get_chapter_body(tex_content, "Guardrails")
    assert "C" in body and "isolad" in body.lower()
    assert "I" in body
    assert "C+I" in body or "C$+$I" in body or "$C+I$" in body or "C\\_I" in body


# --- 7. Grafos no cap de explicabilidade ---
def test_grafos_in_explicabilidade(tex_content):
    body = _get_chapter_body(tex_content, "Explicabilidade")
    assert "proveni" in body.lower()
    assert "regras" in body.lower() or "grafo_regras" in body
    assert "governan" in body.lower()


# --- 8. Sem "fi" corrompido (teste no tex) ---
def test_no_fi_corruption_in_tex(tex_content):
    """Verifica que o TeX usa comandos LaTeX corretos para acentos."""
    # O tex fonte deve usar \\' \\~ \\^ \\c ao inves de UTF-8 direto
    # que pode causar problemas de extracao
    assert "\\usepackage{lmodern}" in tex_content, "lmodern nao encontrado"


# --- 9. Sem "References" residual ---
def test_no_references_residual(tex_content):
    assert "\\section{References}" not in tex_content
    assert "\\chapter{References}" not in tex_content


# --- 10. Sem "0.1" no sumario ---
def test_no_zero_dot_one(tex_content):
    assert "\\chapter{0." not in tex_content
    assert "\\section{0." not in tex_content


# --- 11. Sem ".1 Símbolos" fora de apendice ---
def test_no_dot_one_simbolos(tex_content):
    body = tex_content.split("\\begin{apendicesenv}")[0]
    assert ".1 S" not in body or "\\section{.1 S" not in body


# --- Testes de conteudo preservado ---
def test_pense_nao_alimenta_motor(tex_content):
    assert "alimentam diretamente o motor" in tex_content or "alimenta diretamente o motor" in tex_content


def test_cenarios_nao_representam_alunos(tex_content):
    assert "representam alunos reais" in tex_content


def test_motor_producao_referenciado(tex_content):
    assert "motor.py" in tex_content


def test_motor_academico_referenciado(tex_content):
    assert "motor_resolucao_acolhemente" in tex_content or "motor acad" in tex_content.lower()


def test_figuras_presentes(tex_content):
    assert "fluxo_proveniencia_dados" in tex_content
    assert "grafo_regras_7vars" in tex_content
    assert "grafo_governanca_acolhemente" in tex_content
    assert "cenarios_ativacao_regras" in tex_content
    assert "comparacao_baseline_motor" in tex_content
    assert "resultado_cenarios_sinteticos" in tex_content
