# =====================================================================
# test_no_regression_vs_v3_2_contract.py (v3.3)
# =====================================================================
# Teste automatizado de não regressão: v3.3 vs v3.2.
# =====================================================================
from pathlib import Path
import json
import pytest

ROOT = Path(__file__).resolve().parents[2]
V32 = ROOT / "academic_abntex2_attempt_v3_2"
V33 = ROOT / "academic_abntex2_attempt_v3_3"


def files_under(path, suffix=None):
    if not path.exists():
        return set()
    files = {p.relative_to(path) for p in path.rglob("*") if p.is_file()}
    if suffix:
        files = {p for p in files if str(p).endswith(suffix)}
    return files


def test_v32_baseline_exists():
    assert V32.exists(), "Baseline v3_2 não encontrada"
    assert V33.exists(), "Versão v3_3 não encontrada"


def test_v33_preserves_essential_directories():
    for d in ["appendices", "audits", "_build", "figures", "latex",
              "notebooks", "outputs", "scripts", "tests"]:
        assert (V33 / d).exists(), f"Diretório essencial ausente na v3_3: {d}"


def test_v33_does_not_remove_existing_tests():
    v32_tests = {p.name for p in (V32 / "tests").glob("test_*.py")}
    v33_tests = {p.name for p in (V33 / "tests").glob("test_*.py")}
    missing = v32_tests - v33_tests
    assert not missing, f"Testes da v3_2 removidos na v3_3: {missing}"


def test_v33_preserves_or_expands_appendix_python_files():
    v32_py = {p.name for p in (V32 / "appendices").glob("*.py")}
    v33_py = {p.name for p in (V33 / "appendices").glob("*.py")}
    missing = v32_py - v33_py
    assert not missing, f"Apêndices Python da v3_2 removidos na v3_3: {missing}"


def test_v33_preserves_figures_or_documents_replacement():
    v32_figs = {p.name for p in (V32 / "figures").glob("*")}
    v33_figs = {p.name for p in (V33 / "figures").glob("*")}
    missing = v32_figs - v33_figs
    assert not missing, (
        f"Figuras da v3_2 removidas na v3_3 sem substituição: {missing}"
    )


def test_v33_required_new_artifacts_exist():
    required = [
        "outputs/validacao_exaustiva_64.csv",
        "docs/specs/v3_3_acolhemente_excellence_closure_sdd.md",
        "docs/adr/ADR-v3_3-r5-subsuncao-e-validacao-exaustiva.md",
        "audits/v3_3_excellence_closure_report.md",
        "outputs/main_acolhemente_abntex2.pdf",
        "outputs/Trabalho_Trilha_I_AcolheMente_PB.ipynb",
    ]
    for rel in required:
        p = V33 / rel
        assert p.exists(), f"Artefato obrigatório ausente: {rel}"
        assert p.stat().st_size > 0, f"Artefato obrigatório vazio: {rel}"


def test_v33_notebook_executed_without_errors():
    p = V33 / "outputs/Trabalho_Trilha_I_AcolheMente_PB.ipynb"
    nb = json.loads(p.read_text(encoding="utf-8"))
    executed = 0
    errors = []
    for c in nb.get("cells", []):
        if c.get("cell_type") == "code" and c.get("execution_count") is not None:
            executed += 1
        for out in c.get("outputs", []):
            if out.get("output_type") == "error":
                errors.append(out)
    assert executed > 0, "Notebook v3_3 não possui células executadas"
    assert not errors, f"Notebook v3_3 contém erros: {errors[:2]}"


def test_v33_csv_has_64_rows():
    import csv
    p = V33 / "outputs" / "validacao_exaustiva_64.csv"
    with open(p, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    assert len(rows) == 64, f"CSV tem {len(rows)} linhas, esperado 64"
    assert "A_motor" in rows[0], "CSV não tem coluna A_motor"
    assert "A_esperado" in rows[0], "CSV não tem coluna A_esperado"
    assert "ok" in rows[0], "CSV não tem coluna ok"
    assert "regras_acionadas" in rows[0], "CSV não tem coluna regras_acionadas"
    # Verify oracle agreement
    assert all(
        str(r["ok"]).lower() in {"true", "1"} for r in rows
    ), "Oráculo discorda do motor em algum cenário"


def test_v33_r5_subsumption_confirmed_in_csv():
    import csv
    p = V33 / "outputs" / "validacao_exaustiva_64.csv"
    with open(p, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    r5_only = [
        r for r in rows
        if "R5" in r["regras_acionadas"] and "R3" not in r["regras_acionadas"]
    ]
    assert len(r5_only) == 0, f"R5 sem R3 encontrado: {r5_only}"


def test_v33_preserves_privacy_content():
    tex = (V33 / "latex" / "main_acolhemente_abntex2.tex").read_text(
        encoding="utf-8"
    )
    assert "pseudonimiza" in tex.lower()
    assert "reidentifica" in tex.lower()
    assert "tab:perfis_acesso" in tex
    assert "fluxo_pseudonimizacao_acolhimento" in tex
    assert "LGPD" in tex
    assert "ECA" in tex


def test_v33_tex_has_r5_subsumption():
    tex = (V33 / "latex" / "main_acolhemente_abntex2.tex").read_text(
        encoding="utf-8"
    )
    assert "subsumida" in tex or "subsun" in tex.lower()
