# =====================================================================
# test_data_usage_explanation_contract.py (v3.1)
# =====================================================================
# Adapted for v3.1 chapter titles (no "Grafos de Explicabilidade",
# now "Explicabilidade e Grafos").
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


# --- Capitulos obrigatorios ---
def test_cap_arquitetura_dados(tex_content):
    chapters = re.findall(r"\\chapter\{([^}]+)\}", tex_content)
    found = any("Arquitetura" in c and "Dados" in c for c in chapters)
    assert found, f"Cap Arquitetura de Dados not found. Chapters: {chapters}"


def test_cap_eda(tex_content):
    assert "Explorat" in tex_content


def test_cap_cenarios_sinteticos(tex_content):
    assert "Sint" in tex_content


def test_cap_resultados_guardrail(tex_content):
    assert "Guardrail" in tex_content or "guardrail" in tex_content


def test_cap_explicabilidade(tex_content):
    chapters = re.findall(r"\\chapter\{([^}]+)\}", tex_content)
    found = any("Explicabilidade" in c for c in chapters)
    assert found, f"Cap Explicabilidade not found. Chapters: {chapters}"


# --- Formulacao correta ---
def test_6_variaveis_entrada_1_saida(tex_content):
    assert "6 vari" in tex_content and "entrada" in tex_content


def test_2_elevado_a_6_igual_64(tex_content):
    assert "2^6 = 64" in tex_content


# --- Explicacoes obrigatorias ---
def test_pense_nao_alimenta_motor(tex_content):
    assert "alimenta" in tex_content and "diretamente" in tex_content and "motor" in tex_content


def test_cenarios_nao_representam_alunos(tex_content):
    assert "representam alunos reais" in tex_content


def test_tier_a_explicado(tex_content):
    assert "TIER" in tex_content and "PeNSE" in tex_content


def test_tier_b_explicado(tex_content):
    assert "TIER" in tex_content


def test_tier_c_explicado(tex_content):
    assert "externo" in tex_content.lower()


def test_dataset_externo_benchmark(tex_content):
    assert "benchmark" in tex_content.lower()


def test_motor_producao_explicado(tex_content):
    assert "motor.py" in tex_content


def test_motor_academico_explicado(tex_content):
    assert "motor_resolucao_acolhemente" in tex_content


# --- Figuras ---
def test_figura_proveniencia(tex_content):
    assert "fluxo_proveniencia_dados" in tex_content


def test_figura_grafo_regras(tex_content):
    assert "grafo_regras_7vars" in tex_content


def test_figura_grafo_governanca(tex_content):
    assert "grafo_governanca_acolhemente" in tex_content


def test_figura_cenarios(tex_content):
    assert "cenarios_ativacao_regras" in tex_content or "resultado_cenarios" in tex_content


def test_figura_baseline(tex_content):
    assert "comparacao_baseline_motor" in tex_content
