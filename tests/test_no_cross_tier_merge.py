# =====================================================================
# test_no_cross_tier_merge.py
# =====================================================================
# Guardrail: Nenhuma operação de merge entre tiers distintos.
# TIER_A (PeNSE 2024) nunca deve ser unida linha a linha com TIER_C.
# TIER_C nunca deve sustentar conclusão sobre Brasil/NE/PB.
# TIER_B nunca deve ser tratada como dado real.
# ADR-005/006/007: Proveniência estrita por tiers.
# =====================================================================

import re
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.acolhemente.rule_graph import (
    build_governance_graph,
    CONTEXTUAL_VARIABLES,
)
from src.acolhemente.graph_schema import (
    EntityType,
    RelationshipType,
)


class TestNoCrossTierMerge:
    """Garante isolamento absoluto entre tiers de proveniência."""

    # ---------------------------------------------------------------
    # TIER_A × TIER_C: Bloqueio Absoluto
    # ---------------------------------------------------------------

    def test_no_external_variable_in_tier_a(self):
        """Nenhuma variável externa deve pertencer ao TIER_A."""
        kg = build_governance_graph()
        for rel in kg.relationships:
            if rel.relationship_type == RelationshipType.BELONGS_TO_TIER:
                if rel.source.entity_type == EntityType.EXTERNAL_VARIABLE:
                    assert rel.target.name != "TIER_A_OFFICIAL_BR", (
                        f"CROSS-TIER VIOLATION: Variável externa "
                        f"'{rel.source.name}' vinculada a TIER_A. "
                        f"Merge TIER_A × TIER_C é PROIBIDO."
                    )

    def test_no_pense_source_in_tier_c(self):
        """Nenhuma fonte PeNSE deve pertencer ao TIER_C."""
        kg = build_governance_graph()
        for rel in kg.relationships:
            if rel.relationship_type == RelationshipType.BELONGS_TO_TIER:
                if rel.source.entity_type == EntityType.PENSE_SOURCE:
                    assert rel.target.name != "TIER_C_EXTERNAL_EXPLORATORY", (
                        f"CROSS-TIER VIOLATION: Fonte PeNSE "
                        f"'{rel.source.name}' vinculada a TIER_C. "
                        f"Merge TIER_A × TIER_C é PROIBIDO."
                    )

    def test_crosswalks_are_semantic_not_physical(self):
        """Crosswalks entre tiers devem ser semânticos (sem merge físico)."""
        kg = build_governance_graph()
        crosswalks = kg.get_relationships_by_type(
            RelationshipType.BENCHMARKS_AGAINST
        )
        for cw in crosswalks:
            label_lower = cw.label.lower()
            assert "sem merge" in label_lower, (
                f"CROSSWALK VIOLATION: Crosswalk entre "
                f"'{cw.source.name}' e '{cw.target.name}' "
                f"não declara 'sem merge' no label: '{cw.label}'. "
                f"Todos os crosswalks devem ser semânticos."
            )

    # ---------------------------------------------------------------
    # TIER_C: sem conclusão regional
    # ---------------------------------------------------------------

    def test_external_variables_have_benchmark_disclaimer(self):
        """Todas as variáveis externas (TIER_C) devem ter disclaimer."""
        kg = build_governance_graph()
        ext_vars = kg.get_entities_by_type(EntityType.EXTERNAL_VARIABLE)
        assert len(ext_vars) > 0, "Nenhuma variável externa encontrada."
        for ext in ext_vars:
            desc_lower = ext.description.lower()
            assert "benchmark" in desc_lower or "sem inferência" in desc_lower, (
                f"DISCLAIMER VIOLATION: Variável externa "
                f"'{ext.name}' não tem disclaimer de benchmark: "
                f"'{ext.description}'"
            )

    def test_no_regional_inference_from_external(self):
        """Nenhuma variável externa pode gerar conclusão regional BR."""
        # Padrão: termos regionais brasileiros
        regional_pattern = re.compile(
            r"\b(brasil|nordeste|paraíba|paraiba|escola pública|"
            r"escola publica|rede estadual|rede municipal|ibge)\b",
            re.IGNORECASE
        )
        kg = build_governance_graph()
        ext_vars = kg.get_entities_by_type(EntityType.EXTERNAL_VARIABLE)
        for ext in ext_vars:
            for text in (ext.name, ext.description):
                match = regional_pattern.search(text)
                assert match is None, (
                    f"REGIONAL INFERENCE VIOLATION: Variável externa "
                    f"'{ext.name}' contém referência regional "
                    f"'{match.group()}': '{text}'. "
                    f"TIER_C não pode gerar conclusão sobre Brasil."
                )

    # ---------------------------------------------------------------
    # TIER_B: não é dado real
    # ---------------------------------------------------------------

    def test_tier_b_is_synthetic_if_present(self):
        """TIER_B, se presente no grafo, deve ser sintética/demonstração."""
        kg = build_governance_graph()
        tiers = kg.get_entities_by_type(EntityType.TIER)
        tier_b = [t for t in tiers if "TIER_B" in t.name]
        # TIER_B é opcional no grafo de governança (sem fontes wired)
        if len(tier_b) == 1:
            desc_lower = tier_b[0].description.lower()
            assert "sintétic" in desc_lower or "demonstração" in desc_lower, (
                f"TIER_B deve ser declarada como sintética: "
                f"'{tier_b[0].description}'"
            )

    # ---------------------------------------------------------------
    # Contagem e completude dos tiers
    # ---------------------------------------------------------------

    def test_governance_graph_has_required_tiers(self):
        """Grafo de governança deve ter ao menos TIER_A e TIER_C."""
        kg = build_governance_graph()
        tiers = kg.get_entities_by_type(EntityType.TIER)
        tier_names = {t.name for t in tiers}
        required = {
            "TIER_A_OFFICIAL_BR",
            "TIER_C_EXTERNAL_EXPLORATORY",
        }
        assert required.issubset(tier_names), (
            f"TIER VIOLATION: Tiers obrigatórios {required} não encontrados "
            f"em {tier_names}. Faltando: {required - tier_names}."
        )

    def test_contextual_variables_not_diagnostic(self):
        """Variáveis contextuais C e I nunca geram diagnóstico."""
        for var in CONTEXTUAL_VARIABLES:
            desc_lower = var.description.lower()
            assert "contextual" in desc_lower, (
                f"Variável '{var.name}' deve ser descrita como contextual."
            )

    def test_no_merge_between_distinct_tiers_in_relationships(self):
        """Nenhuma relação do grafo conecta entidades de tiers distintos
        diretamente (exceto crosswalks semânticos declarados)."""
        kg = build_governance_graph()
        for rel in kg.relationships:
            # Crosswalks semânticos são permitidos (BENCHMARKS_AGAINST)
            if rel.relationship_type == RelationshipType.BENCHMARKS_AGAINST:
                continue
            # Verifica se source e target pertencem a tiers diferentes
            # via ligação direta de BELONGS_TO_TIER
            source_type = rel.source.entity_type
            target_type = rel.target.entity_type
            # Variáveis externas não devem ter relação direta com fontes PeNSE
            if (source_type == EntityType.EXTERNAL_VARIABLE
                    and target_type == EntityType.PENSE_SOURCE):
                pytest.fail(
                    f"MERGE VIOLATION: Relação direta entre "
                    f"variável externa '{rel.source.name}' e "
                    f"fonte PeNSE '{rel.target.name}'."
                )
            if (source_type == EntityType.PENSE_SOURCE
                    and target_type == EntityType.EXTERNAL_VARIABLE):
                pytest.fail(
                    f"MERGE VIOLATION: Relação direta entre "
                    f"fonte PeNSE '{rel.source.name}' e "
                    f"variável externa '{rel.target.name}' "
                    f"sem crosswalk semântico declarado."
                )
