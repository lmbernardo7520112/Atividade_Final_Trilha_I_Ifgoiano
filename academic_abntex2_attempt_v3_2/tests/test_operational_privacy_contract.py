# =====================================================================
# test_operational_privacy_contract.py (v3.2)
# =====================================================================
# Verifica que o .tex contem discussao sobre anonimizacao,
# pseudonimizacao, reidentificacao restrita e perfis de acesso.
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


# --- Presenca obrigatoria ---
def test_contains_anonimizacao(tex_content):
    assert "anonimiza" in tex_content.lower()


def test_contains_pseudonimizacao(tex_content):
    assert "pseudonimiza" in tex_content.lower()


def test_contains_reidentificacao_restrita(tex_content):
    assert "reidentifica" in tex_content.lower()
    assert "restrita" in tex_content.lower()


def test_contains_case_id(tex_content):
    assert "case" in tex_content.lower() and (
        "case\\_id" in tex_content or
        "case-2026" in tex_content.lower() or
        "identificador de caso" in tex_content.lower()
    )


def test_contains_equipe_autorizada(tex_content):
    assert "equipe" in tex_content.lower() and "autorizada" in tex_content.lower()


def test_contains_chave_reidentificacao(tex_content):
    assert "chave" in tex_content.lower() and "reidentifica" in tex_content.lower()


def test_professores_not_broad_access(tex_content):
    # professores + "nao devem ter acesso" or equivalent
    lower = tex_content.lower()
    assert "professor" in lower
    assert (
        "n~ao devem ter acesso" in tex_content or
        "nao devem ter acesso" in lower or
        "n\\~ao devem ter acesso" in tex_content
    )


def test_contains_pse_ubs_caps(tex_content):
    assert "PSE" in tex_content
    assert "UBS" in tex_content
    assert "CAPS" in tex_content


def test_contains_painel_analitico(tex_content):
    assert "painel" in tex_content.lower() and "anal" in tex_content.lower()


def test_contains_dados_agregados(tex_content):
    assert "dados agregados" in tex_content.lower() or "agregados" in tex_content.lower()


def test_contains_supressao_grupos(tex_content):
    assert "supress" in tex_content.lower() and "grupo" in tex_content.lower()


def test_nao_exibir_nome(tex_content):
    lower = tex_content.lower()
    assert ("exibir nome" in lower or
            "exibe nome" in lower or
            "nunca devem exibir nome" in lower or
            "n~ao deve" in tex_content and "nome" in lower)


def test_nao_exibir_matricula(tex_content):
    lower = tex_content.lower()
    assert ("matr" in lower and
            ("exibir" in lower or "exibe" in lower or
             "n~ao pode" in tex_content or "nunca" in lower))


def test_logs_acesso(tex_content):
    lower = tex_content.lower()
    assert ("logs de acesso" in lower or
            "registro audit" in lower or
            "log" in lower and "acesso" in lower)


def test_cite_lgpd(tex_content):
    assert "brasil_lgpd_2018" in tex_content


def test_cite_eca(tex_content):
    assert "brasil_eca_1990" in tex_content


def test_cite_pse(tex_content):
    assert "brasil_pse_2007" in tex_content


# --- Ausencia de formulacoes perigosas ---
def test_no_anonimizacao_permite_acolher(tex_content):
    lower = tex_content.lower()
    assert "anonimiza" not in lower or "permite acolher o aluno" not in lower


def test_no_gestao_inteira_acessa(tex_content):
    lower = tex_content.lower()
    assert "gest~ao inteira pode acessar" not in tex_content
    assert "gestao inteira" not in lower


def test_no_professores_podem_ver_score(tex_content):
    lower = tex_content.lower()
    assert "professores podem ver score" not in lower


def test_no_ranking_de_alunos_afirmativo(tex_content):
    """Nao pode conter 'ranking de alunos' em sentido afirmativo."""
    lower = tex_content.lower()
    # OK to have "proibicao de ranking" or "nunca ranking"
    # Not OK: "produz ranking de alunos"
    assert "produz ranking de alunos" not in lower
    assert "gera ranking de alunos" not in lower


def test_no_diagnostico_automatizado_afirmativo(tex_content):
    lower = tex_content.lower()
    assert "realiza diagn" not in lower or "n~ao" in tex_content
    assert "produz diagn" not in lower or "n~ao" in tex_content


# --- Tabela de perfis de acesso ---
def test_tabela_perfis_acesso(tex_content):
    assert "tab:perfis_acesso" in tex_content


# --- Figura pseudonimizacao ---
def test_figura_pseudonimizacao(tex_content):
    assert "fluxo_pseudonimizacao_acolhimento" in tex_content


# --- DPIA/RIPD mencionado ---
def test_dpia_ripd(tex_content):
    assert "DPIA" in tex_content or "RIPD" in tex_content


# --- Politica de retencao ---
def test_politica_retencao(tex_content):
    lower = tex_content.lower()
    assert "reten" in lower and "descarte" in lower
