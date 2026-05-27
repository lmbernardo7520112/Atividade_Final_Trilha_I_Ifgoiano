"""
Tests para o motor de inferência por resolução (motor.py).

Verifica:
- Correção de todas as 6 regras
- Guardrails (C e I isolados)
- Cenário nulo
- Cenário completo
- Explicabilidade
- Propriedades da KB
"""
import pytest
from src.acolhemente.motor import (
    REGRAS_CNF,
    REGRAS_NATURAIS,
    VARIAVEIS,
    inferir_acolhimento,
    explicar_decisao,
    inferir_por_resolucao,
)


class TestRegrasCNF:
    """Testa a estrutura da base de conhecimento."""

    def test_existem_6_regras(self):
        assert len(REGRAS_CNF) == 6

    def test_nomes_regras(self):
        expected = {"R1", "R2", "R3", "R4", "R5", "R6"}
        assert set(REGRAS_CNF.keys()) == expected

    def test_regras_sao_frozensets(self):
        for nome, clausula in REGRAS_CNF.items():
            assert isinstance(clausula, frozenset), f"{nome} não é frozenset"

    def test_todas_regras_contem_A(self):
        """Todas as regras devem ter A como consequente."""
        for nome, clausula in REGRAS_CNF.items():
            assert "A" in clausula, f"{nome} não contém A"

    def test_regras_naturais_existem(self):
        assert len(REGRAS_NATURAIS) == 6
        for r in REGRAS_CNF:
            assert r in REGRAS_NATURAIS

    def test_variaveis_entrada(self):
        assert set(VARIAVEIS) == {"E", "B", "V", "S", "C", "I"}


class TestInferirAcolhimento:
    """Testa inferência para cada regra e cenários."""

    def test_cenario_nulo(self):
        """Nenhuma variável → A não inferido."""
        assert inferir_acolhimento() is False

    def test_R1_S_isolado(self):
        """S → A (R1)."""
        assert inferir_acolhimento(S=True) is True

    def test_R2_V_E(self):
        """V ∧ E → A (R2)."""
        assert inferir_acolhimento(V=True, E=True) is True

    def test_R3_E_B(self):
        """E ∧ B → A (R3)."""
        assert inferir_acolhimento(E=True, B=True) is True

    def test_R4_V_B(self):
        """V ∧ B → A (R4)."""
        assert inferir_acolhimento(V=True, B=True) is True

    def test_R5_E_B_C(self):
        """E ∧ B ∧ C → A (R5)."""
        assert inferir_acolhimento(E=True, B=True, C=True) is True

    def test_R6_V_I(self):
        """V ∧ I → A (R6)."""
        assert inferir_acolhimento(V=True, I=True) is True

    def test_todas_verdadeiras(self):
        """Todas → A inferido."""
        assert inferir_acolhimento(
            E=True, B=True, V=True, S=True, C=True, I=True
        ) is True


class TestGuardrails:
    """Testa que variáveis contextuais não inferem A isoladamente."""

    def test_C_isolado(self):
        """C isolado NÃO infere A."""
        assert inferir_acolhimento(C=True) is False

    def test_I_isolado(self):
        """I isolado NÃO infere A."""
        assert inferir_acolhimento(I=True) is False

    def test_C_I_combinados(self):
        """C + I NÃO inferem A."""
        assert inferir_acolhimento(C=True, I=True) is False

    def test_E_isolado(self):
        """E isolado NÃO infere A."""
        assert inferir_acolhimento(E=True) is False

    def test_B_isolado(self):
        """B isolado NÃO infere A."""
        assert inferir_acolhimento(B=True) is False

    def test_V_isolado(self):
        """V isolado NÃO infere A."""
        assert inferir_acolhimento(V=True) is False


class TestExplicarDecisao:
    """Testa a explicabilidade do motor."""

    def test_explicacao_R1(self):
        result = explicar_decisao(S=True)
        assert result["resultado"] is True
        assert "R1" in result["regras_acionadas"]

    def test_explicacao_R3(self):
        result = explicar_decisao(E=True, B=True)
        assert result["resultado"] is True
        assert "R3" in result["regras_acionadas"]

    def test_explicacao_nenhuma(self):
        result = explicar_decisao()
        assert result["resultado"] is False
        assert len(result["regras_acionadas"]) == 0

    def test_explicacao_multiplas_regras(self):
        result = explicar_decisao(
            E=True, B=True, V=True, S=True, C=True, I=True
        )
        assert result["resultado"] is True
        assert len(result["regras_acionadas"]) >= 3

    def test_explicacao_contem_texto(self):
        result = explicar_decisao(V=True, E=True)
        assert "explicacao" in result
        assert isinstance(result["explicacao"], str)
        assert len(result["explicacao"]) > 0
