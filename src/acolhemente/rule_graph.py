# =====================================================================
# rule_graph.py — Construtor Determinístico de Grafos de Regras
# =====================================================================
# Constrói grafos de conhecimento a partir das 7 variáveis proposicionais
# (5 nucleares + 2 contextuais) e 6 regras lógicas aprovadas para o
# AcolheMente Escolar PB.
#
# Dependências: networkx, matplotlib (ambas offline, sem API externa).
# ADR-009: Grafo determinístico, sem LLM, sem diagnóstico.
# =====================================================================

from __future__ import annotations

from pathlib import Path
from typing import Dict, Tuple

import matplotlib
matplotlib.use("Agg")  # Backend não-interativo para exportação
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx

from .graph_schema import (
    Entity,
    EntityType,
    KnowledgeGraph,
    Relationship,
    RelationshipType,
)


# =====================================================================
# VARIÁVEIS PROPOSICIONAIS APROVADAS
# 7 variáveis: 5 nucleares + 2 contextuais
# =====================================================================

# --- 5 VARIÁVEIS NUCLEARES ---
E = Entity(
    name="E",
    entity_type=EntityType.PROPOSITIONAL_VARIABLE,
    description="Sofrimento emocional recorrente (B12004, B12005, B12007)"
)
B = Entity(
    name="B",
    entity_type=EntityType.PROPOSITIONAL_VARIABLE,
    description="Baixo apoio socioafetivo percebido (B12003, B07004)"
)
V = Entity(
    name="V",
    entity_type=EntityType.PROPOSITIONAL_VARIABLE,
    description="Indicador crítico de desvalor da vida (B12008)"
)
S = Entity(
    name="S",
    entity_type=EntityType.PROPOSITIONAL_VARIABLE,
    description="Sinal autorreferido de autoagressão (B12009)"
)
A = Entity(
    name="A",
    entity_type=EntityType.PROPOSITIONAL_VARIABLE,
    description="Acolhimento humano prioritário (saída do motor)"
)

NUCLEAR_VARIABLES = [E, B, V, S, A]

# --- 2 VARIÁVEIS CONTEXTUAIS DE MODULAÇÃO ---
C = Entity(
    name="C",
    entity_type=EntityType.PROPOSITIONAL_VARIABLE,
    description=(
        "Contexto comportamental agravante — contextual, não isolada, "
        "não diagnóstica (tempo de tela, atividade física, sono)"
    )
)
I = Entity(  # noqa: E741 — single-char propositional variable name is deliberate
    name="I",
    entity_type=EntityType.PROPOSITIONAL_VARIABLE,
    description=(
        "Insuficiência institucional de resposta — contextual, atributo "
        "da escola e não do corpo discente (E01P60, E01P117, E01P118xx)"
    )
)

CONTEXTUAL_VARIABLES = [C, I]

# --- LISTA COMPLETA: 7 VARIÁVEIS ---
PROPOSITIONAL_VARIABLES = NUCLEAR_VARIABLES + CONTEXTUAL_VARIABLES
assert len(PROPOSITIONAL_VARIABLES) == 7, (
    f"BUDGET VIOLATION: Exatamente 7 variáveis proposicionais exigidas "
    f"(5 nucleares + 2 contextuais), "
    f"encontradas {len(PROPOSITIONAL_VARIABLES)}."
)


# =====================================================================
# FONTES PeNSE (TIER_A_OFFICIAL_BR)
# =====================================================================
_PENSE_SOURCES = {
    # Fontes nucleares (E, B, V, S)
    "B12004": Entity("B12004", EntityType.PENSE_SOURCE,
                     "Frequência de preocupação excessiva"),
    "B12005": Entity("B12005", EntityType.PENSE_SOURCE,
                     "Frequência de tristeza"),
    "B12007": Entity("B12007", EntityType.PENSE_SOURCE,
                     "Frequência de irritabilidade"),
    "B12003": Entity("B12003", EntityType.PENSE_SOURCE,
                     "Percepção de apoio familiar"),
    "B07004": Entity("B07004", EntityType.PENSE_SOURCE,
                     "Percepção de apoio escolar"),
    "B12008": Entity("B12008", EntityType.PENSE_SOURCE,
                     "Pensamento de que a vida não vale a pena"),
    "B12009": Entity("B12009", EntityType.PENSE_SOURCE,
                     "Autoagressão autorreferida"),
    # Fontes contextuais (C)
    "B03010C": Entity("B03010C", EntityType.PENSE_SOURCE,
                      "Tempo de tela em dias de semana"),
    "B03006B": Entity("B03006B", EntityType.PENSE_SOURCE,
                      "Prática de atividade física"),
    # Fontes contextuais (I) — variáveis institucionais
    "E01P60": Entity("E01P60", EntityType.PENSE_SOURCE,
                     "Escola oferece apoio psicológico"),
    "E01P117": Entity("E01P117", EntityType.PENSE_SOURCE,
                      "Escola possui fluxo PSE ativo"),
}


# =====================================================================
# REGRAS LÓGICAS APROVADAS (6 regras)
# =====================================================================
R1 = Entity("R1", EntityType.LOGICAL_RULE, "S → A")
R2 = Entity("R2", EntityType.LOGICAL_RULE, "V ∧ E → A")
R3 = Entity("R3", EntityType.LOGICAL_RULE, "E ∧ B → A")
R4 = Entity("R4", EntityType.LOGICAL_RULE, "V ∧ B → A")
R5 = Entity("R5", EntityType.LOGICAL_RULE, "E ∧ B ∧ C → A")
R6 = Entity("R6", EntityType.LOGICAL_RULE, "V ∧ I → A")

R1_CNF = Entity("R1_CNF", EntityType.CNF_CLAUSE, "¬S ∨ A")
R2_CNF = Entity("R2_CNF", EntityType.CNF_CLAUSE, "¬V ∨ ¬E ∨ A")
R3_CNF = Entity("R3_CNF", EntityType.CNF_CLAUSE, "¬E ∨ ¬B ∨ A")
R4_CNF = Entity("R4_CNF", EntityType.CNF_CLAUSE, "¬V ∨ ¬B ∨ A")
R5_CNF = Entity("R5_CNF", EntityType.CNF_CLAUSE, "¬E ∨ ¬B ∨ ¬C ∨ A")
R6_CNF = Entity("R6_CNF", EntityType.CNF_CLAUSE, "¬V ∨ ¬I ∨ A")

ALL_RULES = [R1, R2, R3, R4, R5, R6]
ALL_CNFS = [R1_CNF, R2_CNF, R3_CNF, R4_CNF, R5_CNF, R6_CNF]


# =====================================================================
# AÇÃO E GUARDRAILS
# =====================================================================
ACAO_ACOLHIMENTO = Entity(
    "Acolhimento Humano",
    EntityType.ACTION,
    "Protocolo de escuta ativa com profissional habilitado"
)

GUARDRAILS = [
    Entity("LGPD", EntityType.GUARDRAIL,
           "Lei Geral de Proteção de Dados Pessoais"),
    Entity("ECA", EntityType.GUARDRAIL,
           "Estatuto da Criança e do Adolescente"),
    Entity("PSE", EntityType.GUARDRAIL,
           "Programa Saúde na Escola"),
    Entity("Human-in-the-Loop", EntityType.GUARDRAIL,
           "Intervenção humana obrigatória antes de qualquer ação"),
]

# Ações de encaminhamento vinculadas a A
ENCAMINHAMENTOS = [
    Entity("Revisão Humana", EntityType.ACTION,
           "Revisão obrigatória por profissional habilitado"),
    Entity("Sem Ranking", EntityType.ACTION,
           "Nenhum ranking ou ordenação de indivíduos gerado"),
    Entity("PSE/UBS/CAPS", EntityType.ACTION,
           "Encaminhamento para rede de saúde quando aplicável"),
]


# =====================================================================
# CORES POR TIPO DE ENTIDADE
# =====================================================================
_ENTITY_COLORS: Dict[EntityType, str] = {
    EntityType.PROPOSITIONAL_VARIABLE: "#4FC3F7",  # Azul claro
    EntityType.PENSE_SOURCE: "#81C784",             # Verde
    EntityType.LOGICAL_RULE: "#FFB74D",             # Laranja
    EntityType.CNF_CLAUSE: "#FF8A65",               # Laranja escuro
    EntityType.ACTION: "#E57373",                    # Vermelho suave
    EntityType.GUARDRAIL: "#CE93D8",                # Roxo
    EntityType.TIER: "#90A4AE",                      # Cinza azulado
    EntityType.EXTERNAL_VARIABLE: "#A5D6A7",         # Verde claro
}


def build_proposition_graph() -> KnowledgeGraph:
    """
    Constrói o grafo de proposições: fontes PeNSE → variáveis proposicionais.

    Inclui as 7 variáveis (5 nucleares + 2 contextuais).
    Retorna um KnowledgeGraph 100% determinístico.
    """
    kg = KnowledgeGraph()

    # Mapeamento: fonte PeNSE → variável proposicional
    source_to_var = {
        "B12004": E, "B12005": E, "B12007": E,  # → E (nuclear)
        "B12003": B, "B07004": B,                 # → B (nuclear)
        "B12008": V,                               # → V (nuclear)
        "B12009": S,                               # → S (nuclear)
        "B03010C": C, "B03006B": C,               # → C (contextual)
        "E01P60": I, "E01P117": I,                 # → I (contextual)
    }

    for source_code, var in source_to_var.items():
        source_entity = _PENSE_SOURCES[source_code]
        kg.add_relationship(Relationship(
            source=source_entity,
            target=var,
            relationship_type=RelationshipType.FEEDS_INTO,
            label="alimenta"
        ))

    # Adiciona A como variável de saída
    kg.add_entity(A)

    return kg


def build_rule_graph() -> KnowledgeGraph:
    """
    Constrói o grafo completo: proposições + 6 regras + CNF + ação + guardrails.

    Inclui:
    - Fontes PeNSE → 7 variáveis proposicionais
    - Variáveis → Regras lógicas (R1–R6)
    - Regras → CNF
    - Regras → Ação de acolhimento
    - Ação → Guardrails
    - Ação → Encaminhamentos
    """
    kg = build_proposition_graph()

    # R1: S → A
    kg.add_relationship(Relationship(S, R1, RelationshipType.IMPLIES, "antecedente"))
    kg.add_relationship(Relationship(R1, ACAO_ACOLHIMENTO, RelationshipType.TRIGGERS, "dispara"))
    kg.add_relationship(Relationship(R1, R1_CNF, RelationshipType.CONVERTS_TO, "CNF"))

    # R2: V ∧ E → A
    kg.add_relationship(Relationship(V, R2, RelationshipType.IMPLIES, "antecedente"))
    kg.add_relationship(Relationship(E, R2, RelationshipType.IMPLIES, "antecedente"))
    kg.add_relationship(Relationship(R2, ACAO_ACOLHIMENTO, RelationshipType.TRIGGERS, "dispara"))
    kg.add_relationship(Relationship(R2, R2_CNF, RelationshipType.CONVERTS_TO, "CNF"))

    # R3: E ∧ B → A
    kg.add_relationship(Relationship(E, R3, RelationshipType.IMPLIES, "antecedente"))
    kg.add_relationship(Relationship(B, R3, RelationshipType.IMPLIES, "antecedente"))
    kg.add_relationship(Relationship(R3, ACAO_ACOLHIMENTO, RelationshipType.TRIGGERS, "dispara"))
    kg.add_relationship(Relationship(R3, R3_CNF, RelationshipType.CONVERTS_TO, "CNF"))

    # R4: V ∧ B → A
    kg.add_relationship(Relationship(V, R4, RelationshipType.IMPLIES, "antecedente"))
    kg.add_relationship(Relationship(B, R4, RelationshipType.IMPLIES, "antecedente"))
    kg.add_relationship(Relationship(R4, ACAO_ACOLHIMENTO, RelationshipType.TRIGGERS, "dispara"))
    kg.add_relationship(Relationship(R4, R4_CNF, RelationshipType.CONVERTS_TO, "CNF"))

    # R5: E ∧ B ∧ C → A (contextual: C modula, não infere isoladamente)
    kg.add_relationship(Relationship(E, R5, RelationshipType.IMPLIES, "antecedente"))
    kg.add_relationship(Relationship(B, R5, RelationshipType.IMPLIES, "antecedente"))
    kg.add_relationship(Relationship(C, R5, RelationshipType.IMPLIES, "modula"))
    kg.add_relationship(Relationship(R5, ACAO_ACOLHIMENTO, RelationshipType.TRIGGERS, "dispara"))
    kg.add_relationship(Relationship(R5, R5_CNF, RelationshipType.CONVERTS_TO, "CNF"))

    # R6: V ∧ I → A (contextual: I é institucional, não do aluno)
    kg.add_relationship(Relationship(V, R6, RelationshipType.IMPLIES, "antecedente"))
    kg.add_relationship(Relationship(I, R6, RelationshipType.IMPLIES, "modula"))
    kg.add_relationship(Relationship(R6, ACAO_ACOLHIMENTO, RelationshipType.TRIGGERS, "dispara"))
    kg.add_relationship(Relationship(R6, R6_CNF, RelationshipType.CONVERTS_TO, "CNF"))

    # Guardrails sobre a ação de acolhimento
    for guardrail in GUARDRAILS:
        kg.add_relationship(Relationship(
            ACAO_ACOLHIMENTO, guardrail,
            RelationshipType.GOVERNED_BY, "regulado por"
        ))

    # Encaminhamentos vinculados a A
    for encaminhamento in ENCAMINHAMENTOS:
        kg.add_relationship(Relationship(
            ACAO_ACOLHIMENTO, encaminhamento,
            RelationshipType.TRIGGERS, "encaminha"
        ))

    # Validações finais
    kg.validate_no_student_nodes()
    kg.validate_no_diagnostic_labels()

    return kg


def build_governance_graph() -> KnowledgeGraph:
    """
    Constrói grafo de governança de dados: Tiers + fontes + crosswalks.
    Inclui fontes para variáveis contextuais C e I.
    """
    kg = KnowledgeGraph()

    tier_a = Entity("TIER_A_OFFICIAL_BR", EntityType.TIER,
                    "PeNSE 2024 (IBGE) — única fonte inferencial para Brasil")
    tier_b = Entity("TIER_B_SYNTHETIC_SCHOOL", EntityType.TIER,
                    "Dados escolares sintéticos para demonstração")
    tier_c = Entity("TIER_C_EXTERNAL_EXPLORATORY", EntityType.TIER,
                    "Dataset externo — apenas benchmark metodológico")

    # Registrar todos os 3 tiers no grafo
    kg.add_entity(tier_a)
    kg.add_entity(tier_b)
    kg.add_entity(tier_c)

    # Fontes PeNSE → TIER_A
    for code, source in _PENSE_SOURCES.items():
        kg.add_relationship(Relationship(
            source, tier_a,
            RelationshipType.BELONGS_TO_TIER, "pertence a"
        ))

    # Variáveis externas → TIER_C (benchmark apenas)
    ext_vars = [
        Entity("Support_System", EntityType.EXTERNAL_VARIABLE,
               "Benchmark externo — sem inferência brasileira"),
        Entity("Screen_Time_Hours", EntityType.EXTERNAL_VARIABLE,
               "Benchmark externo — sem inferência brasileira"),
        Entity("Exercise_Hours", EntityType.EXTERNAL_VARIABLE,
               "Benchmark externo — sem inferência brasileira"),
        Entity("Social_Media_Hours", EntityType.EXTERNAL_VARIABLE,
               "Benchmark externo — sem inferência brasileira"),
        Entity("Sleep_Hours", EntityType.EXTERNAL_VARIABLE,
               "Benchmark externo — sem inferência brasileira"),
    ]
    for ext in ext_vars:
        kg.add_relationship(Relationship(
            ext, tier_c,
            RelationshipType.BELONGS_TO_TIER, "pertence a"
        ))

    # Crosswalks semânticos (sem merge físico)
    crosswalks = [
        (_PENSE_SOURCES["B12003"], ext_vars[0]),   # B12003 ↔ Support_System
        (_PENSE_SOURCES["B07004"], ext_vars[0]),    # B07004 ↔ Support_System
        (_PENSE_SOURCES["B03010C"], ext_vars[1]),   # B03010C ↔ Screen_Time_Hours
        (_PENSE_SOURCES["B03006B"], ext_vars[2]),   # B03006B ↔ Exercise_Hours
    ]
    for pense, ext in crosswalks:
        kg.add_relationship(Relationship(
            pense, ext,
            RelationshipType.BENCHMARKS_AGAINST,
            "crosswalk semântico (sem merge)"
        ))

    kg.validate_no_student_nodes()
    kg.validate_no_diagnostic_labels()

    return kg


def _get_node_color(kg: KnowledgeGraph, node_name: str) -> str:
    """Retorna cor baseada no tipo de entidade."""
    for entity in kg.entities:
        if entity.name == node_name:
            return _ENTITY_COLORS.get(entity.entity_type, "#BDBDBD")
    return "#BDBDBD"


def _get_node_labels(kg: KnowledgeGraph) -> Dict[str, str]:
    """Gera labels com nome + descrição curta."""
    labels = {}
    for entity in kg.entities:
        if entity.description and len(entity.description) <= 40:
            labels[entity.name] = f"{entity.name}\n{entity.description}"
        else:
            labels[entity.name] = entity.name
    return labels


def export_graph_png(
    kg: KnowledgeGraph,
    output_path: str | Path,
    title: str = "Grafo de Conhecimento — AcolheMente Escolar PB",
    figsize: Tuple[int, int] = (20, 14),
    seed: int = 42,
) -> Path:
    """
    Exporta o grafo como imagem PNG de alta resolução.

    Parâmetros:
    - kg: KnowledgeGraph determinístico
    - output_path: caminho de saída do PNG
    - title: título do gráfico
    - figsize: dimensão da figura
    - seed: semente para layout determinístico

    Retorna:
    - Path do arquivo gerado
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Constrói grafo networkx dirigido
    G = nx.DiGraph()

    for entity in kg.entities:
        G.add_node(entity.name, entity_type=entity.entity_type.name)

    for rel in kg.relationships:
        G.add_edge(
            rel.source.name,
            rel.target.name,
            label=rel.label,
            rel_type=rel.relationship_type.name
        )

    # Layout determinístico (semente fixa)
    pos = nx.spring_layout(G, seed=seed, k=2.5, iterations=100)

    # Cores por tipo de entidade
    node_colors = [_get_node_color(kg, node) for node in G.nodes()]

    # Labels
    labels = _get_node_labels(kg)

    fig, ax = plt.subplots(1, 1, figsize=figsize)
    ax.set_title(title, fontsize=16, fontweight="bold", pad=20)

    # Desenha nós
    nx.draw_networkx_nodes(
        G, pos, ax=ax,
        node_color=node_colors,
        node_size=2000,
        edgecolors="#424242",
        linewidths=1.5,
        alpha=0.9,
    )

    # Desenha labels dos nós
    nx.draw_networkx_labels(
        G, pos, ax=ax,
        labels=labels,
        font_size=7,
        font_weight="bold",
    )

    # Desenha arestas
    nx.draw_networkx_edges(
        G, pos, ax=ax,
        edge_color="#757575",
        arrows=True,
        arrowsize=15,
        width=1.5,
        connectionstyle="arc3,rad=0.1",
        alpha=0.7,
    )

    # Labels das arestas
    edge_labels = nx.get_edge_attributes(G, "label")
    nx.draw_networkx_edge_labels(
        G, pos, ax=ax,
        edge_labels=edge_labels,
        font_size=6,
        font_color="#616161",
    )

    # Legenda de cores
    legend_patches = []
    seen_types = set()
    for entity in kg.entities:
        if entity.entity_type not in seen_types:
            seen_types.add(entity.entity_type)
            color = _ENTITY_COLORS.get(entity.entity_type, "#BDBDBD")
            label = entity.entity_type.name.replace("_", " ").title()
            legend_patches.append(mpatches.Patch(color=color, label=label))

    ax.legend(
        handles=legend_patches,
        loc="upper left",
        fontsize=8,
        framealpha=0.9,
        title="Tipo de Entidade",
        title_fontsize=9,
    )

    ax.axis("off")
    plt.tight_layout()
    plt.savefig(str(output_path), dpi=300, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    plt.close(fig)

    return output_path
