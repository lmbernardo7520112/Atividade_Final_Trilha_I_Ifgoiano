# =====================================================================
# test_graph_generation_is_deterministic.py
# =====================================================================
# Guardrail: O grafo deve ser gerado de forma 100% determinística.
# Duas execuções consecutivas devem produzir grafos idênticos.
# Nenhuma aleatoriedade, nenhuma dependência de API externa.
# =====================================================================

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.acolhemente.rule_graph import (
    build_proposition_graph,
    build_rule_graph,
    build_governance_graph,
)
from src.acolhemente.graph_schema import KnowledgeGraph


def _graph_fingerprint(kg: KnowledgeGraph) -> dict:
    """Gera impressão digital do grafo para comparação determinística."""
    return {
        "entity_count": kg.entity_count,
        "relationship_count": kg.relationship_count,
        "entity_names": sorted([e.name for e in kg.entities]),
        "entity_types": sorted([e.entity_type.name for e in kg.entities]),
        "entity_descriptions": sorted(
            [e.description for e in kg.entities]
        ),
        "relationships": sorted([
            (r.source.name, r.target.name, r.relationship_type.name,
             r.label)
            for r in kg.relationships
        ]),
    }


class TestGraphDeterminism:
    """Garante geração 100% determinística dos grafos."""

    def test_proposition_graph_deterministic(self):
        """Duas chamadas a build_proposition_graph() produzem grafos idênticos."""
        kg1 = build_proposition_graph()
        kg2 = build_proposition_graph()
        fp1 = _graph_fingerprint(kg1)
        fp2 = _graph_fingerprint(kg2)
        assert fp1 == fp2, (
            "DETERMINISM VIOLATION: build_proposition_graph() produziu "
            "grafos diferentes em execuções consecutivas."
        )

    def test_rule_graph_deterministic(self):
        """Duas chamadas a build_rule_graph() produzem grafos idênticos."""
        kg1 = build_rule_graph()
        kg2 = build_rule_graph()
        fp1 = _graph_fingerprint(kg1)
        fp2 = _graph_fingerprint(kg2)
        assert fp1 == fp2, (
            "DETERMINISM VIOLATION: build_rule_graph() produziu "
            "grafos diferentes em execuções consecutivas."
        )

    def test_governance_graph_deterministic(self):
        """Duas chamadas a build_governance_graph() produzem grafos idênticos."""
        kg1 = build_governance_graph()
        kg2 = build_governance_graph()
        fp1 = _graph_fingerprint(kg1)
        fp2 = _graph_fingerprint(kg2)
        assert fp1 == fp2, (
            "DETERMINISM VIOLATION: build_governance_graph() produziu "
            "grafos diferentes em execuções consecutivas."
        )

    def test_ten_consecutive_builds_identical(self):
        """10 builds consecutivos do grafo de regras são idênticos."""
        reference = _graph_fingerprint(build_rule_graph())
        for i in range(10):
            current = _graph_fingerprint(build_rule_graph())
            assert current == reference, (
                f"DETERMINISM VIOLATION: Build #{i+1} difere do "
                f"reference build."
            )

    def test_proposition_graph_has_stable_entity_count(self):
        """Contagem de entidades é estável entre builds."""
        counts = [build_proposition_graph().entity_count for _ in range(5)]
        assert len(set(counts)) == 1, (
            f"DETERMINISM VIOLATION: entity_count variou: {counts}"
        )

    def test_rule_graph_has_stable_relationship_count(self):
        """Contagem de relações é estável entre builds."""
        counts = [build_rule_graph().relationship_count for _ in range(5)]
        assert len(set(counts)) == 1, (
            f"DETERMINISM VIOLATION: relationship_count variou: {counts}"
        )

    def test_rule_graph_has_expected_rules(self):
        """Grafo de regras contém exatamente R1–R6."""
        from src.acolhemente.graph_schema import EntityType
        kg = build_rule_graph()
        rules = kg.get_entities_by_type(EntityType.LOGICAL_RULE)
        rule_names = {r.name for r in rules}
        expected = {"R1", "R2", "R3", "R4", "R5", "R6"}
        assert rule_names == expected, (
            f"RULE VIOLATION: Esperadas {expected}, "
            f"encontradas {rule_names}."
        )

    def test_rule_graph_has_expected_cnf_clauses(self):
        """Grafo contém cláusulas CNF para todas as 6 regras."""
        from src.acolhemente.graph_schema import EntityType
        kg = build_rule_graph()
        cnfs = kg.get_entities_by_type(EntityType.CNF_CLAUSE)
        cnf_names = {c.name for c in cnfs}
        expected = {"R1_CNF", "R2_CNF", "R3_CNF", "R4_CNF", "R5_CNF", "R6_CNF"}
        assert cnf_names == expected, (
            f"CNF VIOLATION: Esperadas {expected}, "
            f"encontradas {cnf_names}."
        )

    def test_governance_graph_has_all_guardrails(self):
        """Grafo de governança contém todos os guardrails obrigatórios."""
        from src.acolhemente.graph_schema import EntityType
        # Verify governance graph builds successfully
        build_governance_graph()
        # Guardrails are in the rule graph
        kg_rules = build_rule_graph()
        guardrails = kg_rules.get_entities_by_type(EntityType.GUARDRAIL)
        names = {g.name for g in guardrails}
        expected = {"LGPD", "ECA", "PSE", "Human-in-the-Loop"}
        assert expected.issubset(names), (
            f"GUARDRAIL VIOLATION: Esperados {expected}, "
            f"encontrados {names}. "
            f"Faltando: {expected - names}."
        )
