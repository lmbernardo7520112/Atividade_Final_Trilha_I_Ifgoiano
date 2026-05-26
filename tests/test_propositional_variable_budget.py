# =====================================================================
# test_propositional_variable_budget.py
# =====================================================================
# Guardrail: Exatamente 7 variáveis proposicionais
# (5 nucleares + 2 contextuais).
# Variáveis aprovadas: E, B, V, S, A (nucleares), C, I (contextuais)
# =====================================================================

import re
import pytest
import sys
import os

# Ajustar path para importar src/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.acolhemente.rule_graph import (
    PROPOSITIONAL_VARIABLES,
    NUCLEAR_VARIABLES,
    CONTEXTUAL_VARIABLES,
    ALL_RULES,
    ALL_CNFS,
    E, B, V, S, A, C, I,
)
from src.acolhemente.graph_schema import EntityType


class TestPropositionalVariableBudget:
    """Garante que o orçamento de variáveis proposicionais é respeitado."""

    # ---------------------------------------------------------------
    # BUDGET: contagem e nomes
    # ---------------------------------------------------------------

    def test_exactly_seven_variables(self):
        """BUDGET: Deve haver exatamente 7 variáveis proposicionais."""
        assert len(PROPOSITIONAL_VARIABLES) == 7, (
            f"BUDGET VIOLATION: Esperadas 7 variáveis, "
            f"encontradas {len(PROPOSITIONAL_VARIABLES)}: "
            f"{[v.name for v in PROPOSITIONAL_VARIABLES]}"
        )

    def test_five_nuclear_variables(self):
        """BUDGET: Deve haver exatamente 5 variáveis nucleares."""
        assert len(NUCLEAR_VARIABLES) == 5, (
            f"BUDGET VIOLATION: Esperadas 5 nucleares, "
            f"encontradas {len(NUCLEAR_VARIABLES)}"
        )

    def test_two_contextual_variables(self):
        """BUDGET: Deve haver exatamente 2 variáveis contextuais."""
        assert len(CONTEXTUAL_VARIABLES) == 2, (
            f"BUDGET VIOLATION: Esperadas 2 contextuais, "
            f"encontradas {len(CONTEXTUAL_VARIABLES)}"
        )

    def test_variable_names_match_approved(self):
        """BUDGET: Os nomes devem ser exatamente E, B, V, S, A, C, I."""
        expected = {"E", "B", "V", "S", "A", "C", "I"}
        actual = {v.name for v in PROPOSITIONAL_VARIABLES}
        assert actual == expected, (
            f"BUDGET VIOLATION: Nomes esperados {expected}, "
            f"encontrados {actual}. "
            f"Extras: {actual - expected}. "
            f"Faltando: {expected - actual}."
        )

    def test_nuclear_names(self):
        """Nucleares devem ser E, B, V, S, A."""
        expected = {"E", "B", "V", "S", "A"}
        actual = {v.name for v in NUCLEAR_VARIABLES}
        assert actual == expected

    def test_contextual_names(self):
        """Contextuais devem ser C e I."""
        expected = {"C", "I"}
        actual = {v.name for v in CONTEXTUAL_VARIABLES}
        assert actual == expected

    def test_all_variables_are_propositional_type(self):
        """Todas as variáveis devem ser do tipo PROPOSITIONAL_VARIABLE."""
        for var in PROPOSITIONAL_VARIABLES:
            assert var.entity_type == EntityType.PROPOSITIONAL_VARIABLE, (
                f"Variable '{var.name}' tem tipo {var.entity_type}, "
                f"esperado PROPOSITIONAL_VARIABLE."
            )

    # ---------------------------------------------------------------
    # FONTES PeNSE nas variáveis nucleares
    # ---------------------------------------------------------------

    def test_e_description_references_pense(self):
        """E deve referenciar B12004, B12005, B12007."""
        desc = E.description.upper()
        for code in ["B12004", "B12005", "B12007"]:
            assert code in desc, f"E.description deve referenciar {code}"

    def test_b_description_references_pense(self):
        """B deve referenciar B12003, B07004."""
        desc = B.description.upper()
        for code in ["B12003", "B07004"]:
            assert code in desc, f"B.description deve referenciar {code}"

    def test_v_description_references_pense(self):
        """V deve referenciar B12008."""
        assert "B12008" in V.description.upper()

    def test_s_description_references_pense(self):
        """S deve referenciar B12009."""
        assert "B12009" in S.description.upper()

    # ---------------------------------------------------------------
    # VARIÁVEL A: saída operacional
    # ---------------------------------------------------------------

    def test_a_is_output_variable(self):
        """A deve ser variável de saída do motor."""
        desc_lower = A.description.lower()
        assert "saída" in desc_lower or "motor" in desc_lower, (
            f"A.description deve indicar que é saída do motor: "
            f"'{A.description}'"
        )

    def test_a_is_only_output(self):
        """A é a ÚNICA conclusão operacional — nenhuma outra variável é saída."""
        output_markers = {"saída", "conclusão", "output"}
        for var in PROPOSITIONAL_VARIABLES:
            if var.name == "A":
                continue
            desc_lower = var.description.lower()
            for marker in output_markers:
                assert marker not in desc_lower, (
                    f"VIOLATION: Variável '{var.name}' parece ser saída "
                    f"('{marker}' em '{var.description}'). "
                    f"Apenas A pode ser saída operacional."
                )

    # ---------------------------------------------------------------
    # VARIÁVEL C: contextual comportamental
    # ---------------------------------------------------------------

    def test_c_is_contextual(self):
        """C deve ser descrita como contextual."""
        desc = C.description.lower()
        assert "contextual" in desc, (
            f"C.description deve conter 'contextual': '{C.description}'"
        )

    def test_c_is_not_diagnostic(self):
        """C não pode ser diagnóstica."""
        desc = C.description.lower()
        assert "não diagnóstica" in desc or "não isolada" in desc, (
            f"C.description deve conter 'não diagnóstica' ou "
            f"'não isolada': '{C.description}'"
        )

    # ---------------------------------------------------------------
    # VARIÁVEL I: contextual institucional
    # ---------------------------------------------------------------

    def test_i_is_contextual(self):
        """I deve ser descrita como contextual."""
        desc = I.description.lower()
        assert "contextual" in desc, (
            f"I.description deve conter 'contextual': '{I.description}'"
        )

    def test_i_is_institutional_not_student(self):
        """I deve ser atributo da escola, não do corpo discente."""
        desc = I.description.lower()
        assert "escola" in desc or "institucional" in desc, (
            f"I.description deve referenciar escola/instituição: "
            f"'{I.description}'"
        )
        assert ("não do corpo discente" in desc
                or "atributo da escola" in desc
                or "não do aluno" in desc), (
            f"I.description deve indicar que NÃO é atributo do aluno: "
            f"'{I.description}'"
        )

    # ---------------------------------------------------------------
    # REGRAS: R1–R6
    # ---------------------------------------------------------------

    def test_exactly_six_rules(self):
        """Deve haver exatamente 6 regras lógicas."""
        assert len(ALL_RULES) == 6, (
            f"RULE BUDGET: Esperadas 6 regras, encontradas {len(ALL_RULES)}"
        )

    def test_exactly_six_cnf_clauses(self):
        """Deve haver exatamente 6 cláusulas CNF."""
        assert len(ALL_CNFS) == 6, (
            f"CNF BUDGET: Esperadas 6 CNFs, encontradas {len(ALL_CNFS)}"
        )

    def test_c_never_infers_a_alone(self):
        """C NUNCA deve inferir A isoladamente (nenhuma regra C → A)."""
        for rule in ALL_RULES:
            desc = rule.description.strip()
            # Regra seria "C → A" se for apenas C no antecedente
            if desc in ("C → A", "C -> A"):
                pytest.fail(
                    f"ISOLATION VIOLATION: Regra '{rule.name}' ({desc}) "
                    f"usa C isoladamente para inferir A. "
                    f"C é contextual e nunca infere A sozinha."
                )

    def test_i_never_infers_a_alone(self):
        """I NUNCA deve inferir A isoladamente (nenhuma regra I → A)."""
        for rule in ALL_RULES:
            desc = rule.description.strip()
            if desc in ("I → A", "I -> A"):
                pytest.fail(
                    f"ISOLATION VIOLATION: Regra '{rule.name}' ({desc}) "
                    f"usa I isoladamente para inferir A. "
                    f"I é contextual e nunca infere A sozinha."
                )

    # ---------------------------------------------------------------
    # GUARDRAILS: sem diagnóstico, sem ranking
    # ---------------------------------------------------------------

    def test_no_variable_has_diagnostic_name(self):
        """Nenhuma variável pode ter nome diagnóstico."""
        forbidden_pattern = re.compile(
            r"\b(depressão|tdah|autismo|toc|transtorno)\b",
            re.IGNORECASE
        )
        for var in PROPOSITIONAL_VARIABLES:
            for text in (var.name, var.description):
                match = forbidden_pattern.search(text)
                assert match is None, (
                    f"DIAGNOSTIC VIOLATION: Variável '{var.name}' contém "
                    f"termo proibido '{match.group()}'"
                )

    def test_no_ranking_language(self):
        """Nenhuma variável contém linguagem de ranking."""
        ranking_pattern = re.compile(
            r"\b(ranking|rank|posição|classificar|nota|score individual)\b",
            re.IGNORECASE
        )
        for var in PROPOSITIONAL_VARIABLES:
            for text in (var.name, var.description):
                match = ranking_pattern.search(text)
                assert match is None, (
                    f"RANKING VIOLATION: '{var.name}' contém '{match.group()}'"
                )

    # ---------------------------------------------------------------
    # GRAFO: contagem no grafo construído
    # ---------------------------------------------------------------

    def test_proposition_graph_has_seven_variables(self):
        """O grafo de proposições deve conter exatamente 7 vars."""
        from src.acolhemente.rule_graph import build_proposition_graph
        kg = build_proposition_graph()
        count = kg.propositional_variable_count()
        assert count == 7, (
            f"BUDGET VIOLATION no grafo: Esperadas 7 variáveis "
            f"proposicionais, encontradas {count}"
        )

    def test_dataset_externo_not_used_for_br_conclusion(self):
        """Dataset externo não é usado para conclusão sobre Brasil."""
        from src.acolhemente.rule_graph import build_governance_graph
        kg = build_governance_graph()
        # Variáveis externas devem pertencer apenas a TIER_C
        for rel in kg.relationships:
            if rel.source.entity_type == EntityType.EXTERNAL_VARIABLE:
                assert rel.target.name != "TIER_A_OFFICIAL_BR", (
                    f"TIER VIOLATION: Variável externa "
                    f"'{rel.source.name}' vinculada a TIER_A."
                )
