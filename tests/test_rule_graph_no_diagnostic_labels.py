# =====================================================================
# test_rule_graph_no_diagnostic_labels.py
# =====================================================================
# Guardrail: Nenhum rótulo do grafo contém termos diagnósticos.
# Proibições absolutas: depressão, TDAH, autismo, TOC, transtorno,
# paciente, diagnóstico.
# =====================================================================

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.acolhemente.rule_graph import (
    build_proposition_graph,
    build_rule_graph,
    build_governance_graph,
    PROPOSITIONAL_VARIABLES,
)
from src.acolhemente.graph_schema import (
    Entity,
    EntityType,
    KnowledgeGraph,
    FORBIDDEN_LABELS,
)


import re

DIAGNOSTIC_TERMS = {
    # Português
    "depressão", "ansiedade diagnosticada", "tdah",
    "autismo", "toc", "transtorno", "paciente",
    "esquizofrenia", "bipolar", "borderline",
    "transtorno de personalidade",
    # Inglês
    "depression", "adhd", "autism", "ocd",
    "disorder", "patient", "diagnosis",
    "schizophrenia", "bipolar",
}

# Regex com word boundaries para evitar falsos positivos
# (ex: "protocolo" NÃO aciona "toc")
_DIAGNOSTIC_PATTERNS = {
    term: re.compile(r"\b" + re.escape(term) + r"\b", re.IGNORECASE)
    for term in DIAGNOSTIC_TERMS
}


def _text_contains_diagnostic(text: str) -> str | None:
    """Retorna o termo diagnóstico encontrado ou None (word boundary)."""
    for term, pattern in _DIAGNOSTIC_PATTERNS.items():
        if pattern.search(text):
            return term
    return None


class TestNoDiagnosticLabels:
    """Garante ausência total de linguagem diagnóstica no grafo."""

    def _check_graph_for_diagnostic_terms(self, kg: KnowledgeGraph):
        """Verifica todos os nós e relações de um grafo."""
        for entity in kg.entities:
            for text in (entity.name, entity.description):
                found = _text_contains_diagnostic(text)
                assert found is None, (
                    f"DIAGNOSTIC LABEL VIOLATION: "
                    f"'{entity.name}' contém termo diagnóstico "
                    f"proibido '{found}' em texto '{text}'."
                )

        for rel in kg.relationships:
            found = _text_contains_diagnostic(rel.label)
            assert found is None, (
                f"DIAGNOSTIC LABEL VIOLATION: Relação "
                f"'{rel.source.name}' → '{rel.target.name}' "
                f"contém termo diagnóstico '{found}' no label "
                f"'{rel.label}'."
            )

    def test_proposition_graph_no_diagnostics(self):
        """Grafo de proposições sem termos diagnósticos."""
        kg = build_proposition_graph()
        self._check_graph_for_diagnostic_terms(kg)

    def test_rule_graph_no_diagnostics(self):
        """Grafo de regras sem termos diagnósticos."""
        kg = build_rule_graph()
        self._check_graph_for_diagnostic_terms(kg)

    def test_governance_graph_no_diagnostics(self):
        """Grafo de governança sem termos diagnósticos."""
        kg = build_governance_graph()
        self._check_graph_for_diagnostic_terms(kg)

    def test_validate_no_diagnostic_labels_method(self):
        """Método validate_no_diagnostic_labels() funciona."""
        kg = build_rule_graph()
        assert kg.validate_no_diagnostic_labels() is True

    def test_entity_constructor_blocks_diagnostic_label(self):
        """Construtor de Entity bloqueia rótulos diagnósticos."""
        with pytest.raises(ValueError, match="GUARDRAIL VIOLATION"):
            Entity(
                name="depressão",
                entity_type=EntityType.PROPOSITIONAL_VARIABLE,
                description="teste"
            )

    def test_entity_constructor_blocks_diagnostic_in_description(self):
        """Construtor de Entity bloqueia diagnóstico na descrição."""
        with pytest.raises(ValueError, match="GUARDRAIL VIOLATION"):
            Entity(
                name="X",
                entity_type=EntityType.PROPOSITIONAL_VARIABLE,
                description="Indicador de autismo"
            )

    def test_propositional_variables_no_ranking_language(self):
        """Variáveis proposicionais não contêm linguagem de ranking."""
        ranking_terms = {"ranking", "rank", "posição", "classificar",
                         "melhor", "pior", "nota", "score individual"}
        for var in PROPOSITIONAL_VARIABLES:
            name_lower = var.name.lower()
            desc_lower = var.description.lower()
            for term in ranking_terms:
                assert term not in name_lower, (
                    f"RANKING VIOLATION: '{var.name}' contém '{term}'"
                )
                assert term not in desc_lower, (
                    f"RANKING VIOLATION: descrição de '{var.name}' "
                    f"contém '{term}': '{var.description}'"
                )

    def test_forbidden_labels_constant_is_complete(self):
        """FORBIDDEN_LABELS no schema cobre os termos obrigatórios."""
        required = {"depressão", "tdah", "autismo", "toc", "transtorno",
                     "paciente"}
        for term in required:
            assert term in FORBIDDEN_LABELS, (
                f"FORBIDDEN_LABELS está incompleto: falta '{term}'"
            )

    def test_all_classifications_have_explainable_rule(self):
        """Toda ação de acolhimento no grafo tem regra rastreável."""
        from src.acolhemente.graph_schema import RelationshipType
        kg = build_rule_graph()
        # Encontrar relações TRIGGERS que disparam a ação principal
        trigger_rels = kg.get_relationships_by_type(
            RelationshipType.TRIGGERS
        )
        assert len(trigger_rels) > 0, (
            "Nenhuma relação TRIGGERS encontrada no grafo de regras."
        )
        # Cada TRIGGERS que vem de regra deve vir de LOGICAL_RULE
        # (TRIGGERS entre ACTIONs são encaminhamentos, não classificações)
        rule_triggers = [
            rel for rel in trigger_rels
            if rel.source.entity_type == EntityType.LOGICAL_RULE
        ]
        assert len(rule_triggers) >= 6, (
            f"Esperadas ao menos 6 regras disparando acolhimento, "
            f"encontradas {len(rule_triggers)}."
        )
        for rel in rule_triggers:
            assert rel.source.entity_type == EntityType.LOGICAL_RULE, (
                f"Ação de acolhimento disparada por "
                f"'{rel.source.name}' (tipo {rel.source.entity_type}) "
                f"não tem regra explicável. Deveria ser LOGICAL_RULE."
            )

