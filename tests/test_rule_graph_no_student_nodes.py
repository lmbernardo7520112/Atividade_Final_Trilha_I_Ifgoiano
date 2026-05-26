# =====================================================================
# test_rule_graph_no_student_nodes.py
# =====================================================================
# Guardrail: Nenhum nó do grafo pode IDENTIFICAR estudante real.
# ADR-008: Proibido classificar aluno individual.
# ADR-009: Grafo determinístico sem identificadores pessoais.
#
# IMPORTANTE: Este teste distingue:
#   - Nós que IDENTIFICAM indivíduos → PROIBIDOS ("Aluno João")
#   - Texto acadêmico legítimo → PERMITIDO ("não do aluno")
# =====================================================================

import re
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.acolhemente.rule_graph import (
    build_proposition_graph,
    build_rule_graph,
    build_governance_graph,
)
from src.acolhemente.graph_schema import Entity, EntityType, KnowledgeGraph


# Padrões que indicam nó representando indivíduo identificável
# (verifica NOMES de entidades, não descrições)
_STUDENT_NODE_PATTERNS = [
    # Nó que nomeia aluno individual: "Aluno João", "Estudante 123"
    re.compile(
        r"\b(aluno|aluna|estudante|student|paciente)\s+\S+",
        re.IGNORECASE
    ),
    # Dados identificáveis no nome do nó
    re.compile(
        r"\b(cpf|matrícula|matricula|e-?mail|telefone|phone|"
        r"celular|endereço|endereco|address)\b",
        re.IGNORECASE
    ),
]

# Nomes próprios (word-boundary regex, ≥4 chars para evitar falsos positivos)
_INDIVIDUAL_NAMES_PATTERN = re.compile(
    r"\b(joão|maria|pedro|josé|silva|santos|oliveira|"
    r"fernanda|lucas|gabriel|beatriz|rafael)\b",
    re.IGNORECASE
)


class TestNoStudentNodes:
    """Garante que nenhum nó do grafo identifica estudante real."""

    def _check_graph_entity_names(self, kg: KnowledgeGraph):
        """Verifica NOMES de entidades contra padrões de identificação."""
        for entity in kg.entities:
            for pattern in _STUDENT_NODE_PATTERNS:
                match = pattern.search(entity.name)
                assert match is None, (
                    f"STUDENT NODE VIOLATION: Nó '{entity.name}' contém "
                    f"padrão de identificação de estudante: "
                    f"'{match.group()}'."
                )

    def test_proposition_graph_no_students(self):
        """Grafo de proposições não tem nós de estudante."""
        kg = build_proposition_graph()
        self._check_graph_entity_names(kg)

    def test_rule_graph_no_students(self):
        """Grafo de regras não tem nós de estudante."""
        kg = build_rule_graph()
        self._check_graph_entity_names(kg)

    def test_governance_graph_no_students(self):
        """Grafo de governança não tem nós de estudante."""
        kg = build_governance_graph()
        self._check_graph_entity_names(kg)

    def test_validate_no_student_nodes_method(self):
        """Método validate_no_student_nodes() funciona corretamente."""
        kg = build_rule_graph()
        # Deve passar sem exceção
        assert kg.validate_no_student_nodes() is True

    def test_validate_no_student_nodes_catches_violation(self):
        """Método validate_no_student_nodes() detecta violação."""
        kg = KnowledgeGraph()
        # Tentar adicionar nó com nome de aluno individual
        bad_entity = Entity(
            name="Aluno João",
            entity_type=EntityType.PROPOSITIONAL_VARIABLE,
            description="teste"
        )
        kg.add_entity(bad_entity)
        with pytest.raises(ValueError, match="GUARDRAIL VIOLATION"):
            kg.validate_no_student_nodes()

    def test_no_entity_represents_individual(self):
        """Nenhuma entidade em nenhum grafo representa um indivíduo."""
        for builder in [build_proposition_graph, build_rule_graph,
                        build_governance_graph]:
            kg = builder()
            for entity in kg.entities:
                match = _INDIVIDUAL_NAMES_PATTERN.search(entity.name)
                assert match is None, (
                    f"INDIVIDUAL VIOLATION: Nó '{entity.name}' parece "
                    f"representar pessoa individual ('{match.group()}')."
                )

    def test_legitimate_educational_text_allowed(self):
        """Texto educacional legítimo NÃO é bloqueado em descrições."""
        # Estes devem funcionar sem erro (texto acadêmico legítimo)
        legitimate = [
            Entity("I", EntityType.PROPOSITIONAL_VARIABLE,
                   "atributo da escola e não do corpo discente"),
            Entity("Revisão Humana", EntityType.ACTION,
                   "Revisão obrigatória por profissional habilitado"),
            Entity("Sem Ranking", EntityType.ACTION,
                   "Nenhum ranking ou ordenação de indivíduos gerado"),
        ]
        kg = KnowledgeGraph()
        for e in legitimate:
            kg.add_entity(e)
        # Não deve levantar exceção
        assert kg.validate_no_student_nodes() is True
