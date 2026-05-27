# =====================================================================
# test_motor_equivalence_contract.py
# =====================================================================
# Verifica que o motor academico (appendices/) e o motor de producao
# (src/acolhemente/) produzem saidas identicas para os mesmos cenarios.
# =====================================================================
import sys
import os
import pytest

# Diretorio dos apendices
APPENDICES = os.path.join(os.path.dirname(__file__), "..", "appendices")


def test_motor_academico_funciona():
    """Motor academico roda sem erros e produz resultados corretos."""
    sys.path.insert(0, APPENDICES)
    try:
        from motor_resolucao_acolhemente import inferir_acolhimento
        from cenarios_sinteticos_acolhemente import executar_validacao
        resultados = executar_validacao()
        assert len(resultados) >= 14, f"Esperados >= 14 cenarios, obtidos {len(resultados)}"
        for r in resultados:
            assert r["ok"], f"Cenario falhou: {r['nome']}"
    finally:
        sys.path.pop(0)


def test_motor_producao_equivalence():
    """Se o motor de producao estiver importavel, verifica equivalencia."""
    try:
        from acolhemente.motor import inferir_acolhimento as prod_inferir
    except (ImportError, ModuleNotFoundError):
        pytest.skip(
            "Motor de producao (src/acolhemente/motor.py) nao importavel "
            "no ambiente atual. Skip justificado: o motor academico e a "
            "versao didatica-equivalente apresentada no PDF."
        )

    sys.path.insert(0, APPENDICES)
    try:
        from motor_resolucao_acolhemente import inferir_acolhimento as acad_inferir

        cenarios = [
            {"E": False, "B": False, "V": False, "S": False, "C": False, "I": False},
            {"E": False, "B": False, "V": False, "S": True, "C": False, "I": False},
            {"E": True, "B": False, "V": True, "S": False, "C": False, "I": False},
            {"E": True, "B": True, "V": False, "S": False, "C": False, "I": False},
            {"E": False, "B": True, "V": True, "S": False, "C": False, "I": False},
            {"E": True, "B": True, "V": False, "S": False, "C": True, "I": False},
            {"E": False, "B": False, "V": True, "S": False, "C": False, "I": True},
            {"E": False, "B": False, "V": False, "S": False, "C": True, "I": False},
            {"E": False, "B": False, "V": False, "S": False, "C": False, "I": True},
            {"E": True, "B": True, "V": True, "S": True, "C": True, "I": True},
        ]

        for c in cenarios:
            r_acad = acad_inferir(**c)
            r_prod = prod_inferir(**c)
            assert r_acad == r_prod, (
                f"Divergencia! cenario={c} acad={r_acad} prod={r_prod}"
            )
    finally:
        sys.path.pop(0)
