# =====================================================================
# graph_schema.py — Schema Determinístico de Grafo de Conhecimento
# =====================================================================
# Inspirado em knowledge_graph_generation.ipynb (Google/Gemini),
# porém 100% determinístico, sem dependência de LLM/API externa.
#
# ADR-009: Grafo Determinístico de Conhecimento para Explicabilidade
# =====================================================================

import re
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Optional


class EntityType(Enum):
    """Tipos de entidade permitidos no grafo de explicabilidade."""
    PROPOSITIONAL_VARIABLE = auto()   # E, B, V, S, A
    PENSE_SOURCE = auto()             # Variáveis PeNSE (B12004, B12003, etc.)
    LOGICAL_RULE = auto()             # R1, R2, R3, R4
    CNF_CLAUSE = auto()               # Cláusulas em CNF
    ACTION = auto()                   # Acolhimento humano prioritário
    GUARDRAIL = auto()                # LGPD, ECA, PSE, Human-in-the-loop
    TIER = auto()                     # TIER_A, TIER_B, TIER_C
    EXTERNAL_VARIABLE = auto()        # Variáveis do dataset externo (benchmark)


class RelationshipType(Enum):
    """Tipos de relação permitidos no grafo."""
    FEEDS_INTO = auto()               # Fonte PeNSE → Variável proposicional
    IMPLIES = auto()                  # Antecedente → Consequente (regra)
    CONVERTS_TO = auto()              # Regra → CNF
    TRIGGERS = auto()                 # Resolução → Ação de acolhimento
    GOVERNED_BY = auto()              # Ação → Guardrail ético/legal
    BENCHMARKS_AGAINST = auto()       # Variável TIER_C → Crosswalk semântico
    BELONGS_TO_TIER = auto()          # Fonte → Tier de proveniência


# =====================================================================
# RÓTULOS PROIBIDOS — Termos clínicos/diagnósticos vetados
# Validação usa word boundaries (\b) para evitar falsos positivos
# (ex: "protocolo" não deve acionar "toc").
# =====================================================================
FORBIDDEN_LABELS = frozenset({
    "depressão", "depression",
    "tdah", "adhd",
    "autismo", "autism",
    "toc", "ocd",
    "transtorno", "disorder",
    "paciente", "patient",
    "diagnóstico", "diagnosis",
})

# Regex pré-compilado com word boundaries para cada termo proibido
_FORBIDDEN_PATTERNS = {
    term: re.compile(r"\b" + re.escape(term) + r"\b", re.IGNORECASE)
    for term in FORBIDDEN_LABELS
}


def _contains_forbidden_label(text: str) -> Optional[str]:
    """
    Verifica se texto contém termo diagnóstico proibido como palavra inteira.

    Usa word boundaries (\b) para evitar falsos positivos:
    - "protocolo" NÃO aciona "toc" ✓
    - "toc" isolado ACIONA "toc" ✓
    - "diagnóstico" ACIONA "diagnóstico" ✓

    Retorna o termo proibido encontrado ou None.
    """
    for term, pattern in _FORBIDDEN_PATTERNS.items():
        if pattern.search(text):
            return term
    return None


@dataclass(frozen=True)
class Entity:
    """
    Entidade do grafo de conhecimento.

    Representação determinística — não extraída por LLM.
    Nenhum nó pode representar um estudante individual (ADR-008/009).
    """
    name: str
    entity_type: EntityType
    description: str = ""

    def __post_init__(self):
        # Guardrail: bloquear rótulos diagnósticos (word boundary match)
        for text in (self.name, self.description):
            found = _contains_forbidden_label(text)
            if found:
                raise ValueError(
                    f"GUARDRAIL VIOLATION: Rótulo diagnóstico proibido "
                    f"detectado: '{found}' em Entity(name='{self.name}'). "
                    f"ADR-008/ADR-009 proíbem linguagem diagnóstica."
                )


@dataclass(frozen=True)
class Relationship:
    """
    Relação dirigida entre duas entidades do grafo.

    Todas as relações são definidas programaticamente no código,
    nunca extraídas por IA generativa.
    """
    source: Entity
    target: Entity
    relationship_type: RelationshipType
    label: str = ""


@dataclass
class KnowledgeGraph:
    """
    Grafo de Conhecimento Determinístico.

    Armazena entidades e relações definidas explicitamente no código.
    Não possui nenhum mecanismo de extração automática por LLM.

    Guardrails integrados:
    - Nenhum nó pode representar estudante individual
    - Nenhum rótulo pode conter termos diagnósticos
    - O grafo é 100% reproduzível (determinístico)
    """
    entities: List[Entity] = field(default_factory=list)
    relationships: List[Relationship] = field(default_factory=list)

    def add_entity(self, entity: Entity) -> None:
        """Adiciona entidade com validação de guardrails."""
        if entity not in self.entities:
            self.entities.append(entity)

    def add_relationship(self, relationship: Relationship) -> None:
        """Adiciona relação garantindo que ambas as entidades existem."""
        self.add_entity(relationship.source)
        self.add_entity(relationship.target)
        if relationship not in self.relationships:
            self.relationships.append(relationship)

    def get_entities_by_type(self, entity_type: EntityType) -> List[Entity]:
        """Filtra entidades por tipo."""
        return [e for e in self.entities if e.entity_type == entity_type]

    def get_relationships_by_type(
        self, rel_type: RelationshipType
    ) -> List[Relationship]:
        """Filtra relações por tipo."""
        return [r for r in self.relationships
                if r.relationship_type == rel_type]

    def validate_no_student_nodes(self) -> bool:
        """
        Guardrail: verifica que nenhum nó IDENTIFICA estudante individual.

        Verifica apenas NOMES de entidades (não descrições), pois descrições
        podem conter vocabulário educacional legítimo como 'aluno', 'estudante',
        'discente', 'acolhimento humano'.

        Bloqueia padrões de nós identificáveis como:
        - "Aluno João", "Estudante 123", "Paciente Z"
        - Nomes com CPF, matrícula, e-mail, telefone
        """
        # Patterns que indicam nó representando indivíduo identificável
        _STUDENT_NODE_PATTERNS = [
            # Nó que nomeia aluno individual: "Aluno X", "Estudante Y"
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
        for entity in self.entities:
            for pattern in _STUDENT_NODE_PATTERNS:
                match = pattern.search(entity.name)
                if match:
                    raise ValueError(
                        f"GUARDRAIL VIOLATION: Nó com identificador de "
                        f"estudante detectado: '{entity.name}' "
                        f"(match: '{match.group()}'). "
                        f"ADR-008 proíbe classificação de aluno individual."
                    )
        return True

    def validate_no_diagnostic_labels(self) -> bool:
        """
        Guardrail: verifica que nenhum rótulo contém termos diagnósticos.
        Usa word boundaries para evitar falsos positivos.
        """
        for entity in self.entities:
            # A validação já acontece no __post_init__ de Entity,
            # mas rodamos de novo para segurança adicional.
            for text in (entity.name, entity.description):
                found = _contains_forbidden_label(text)
                if found:
                    raise ValueError(
                        f"GUARDRAIL VIOLATION: Rótulo diagnóstico "
                        f"'{found}' em '{entity.name}'."
                    )
        return True

    @property
    def entity_count(self) -> int:
        return len(self.entities)

    @property
    def relationship_count(self) -> int:
        return len(self.relationships)

    def propositional_variable_count(self) -> int:
        """Conta variáveis proposicionais no grafo."""
        return len(self.get_entities_by_type(
            EntityType.PROPOSITIONAL_VARIABLE
        ))
