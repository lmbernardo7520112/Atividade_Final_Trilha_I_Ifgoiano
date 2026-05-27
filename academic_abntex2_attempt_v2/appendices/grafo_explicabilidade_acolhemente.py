# =====================================================================
# APENDICE E: Grafo de Explicabilidade
# =====================================================================
# Gera visualizacao do grafo de regras usando NetworkX e Matplotlib.
# ADR-009: 100% deterministico, sem LLM, sem API externa.
# =====================================================================

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx


def construir_grafo():
    """Constroi grafo dirigido das regras do AcolheMente."""
    G = nx.DiGraph()

    # Variaveis nucleares
    for v in ["E", "B", "V", "S"]:
        G.add_node(v, tipo="nuclear")
    G.add_node("A", tipo="saida")

    # Variaveis contextuais
    for v in ["C", "I"]:
        G.add_node(v, tipo="contextual")

    # Regras
    for r in ["R1", "R2", "R3", "R4", "R5", "R6"]:
        G.add_node(r, tipo="regra")

    # Guardrails
    for g in ["LGPD", "ECA", "PSE", "HITL"]:
        G.add_node(g, tipo="guardrail")

    # Arestas: antecedentes -> regras
    G.add_edge("S", "R1", label="antecedente")
    G.add_edge("V", "R2", label="antecedente")
    G.add_edge("E", "R2", label="antecedente")
    G.add_edge("E", "R3", label="antecedente")
    G.add_edge("B", "R3", label="antecedente")
    G.add_edge("V", "R4", label="antecedente")
    G.add_edge("B", "R4", label="antecedente")
    G.add_edge("E", "R5", label="antecedente")
    G.add_edge("B", "R5", label="antecedente")
    G.add_edge("C", "R5", label="modula")
    G.add_edge("V", "R6", label="antecedente")
    G.add_edge("I", "R6", label="modula")

    # Arestas: regras -> A
    for r in ["R1", "R2", "R3", "R4", "R5", "R6"]:
        G.add_edge(r, "A", label="infere")

    # Arestas: A -> guardrails
    for g in ["LGPD", "ECA", "PSE", "HITL"]:
        G.add_edge("A", g, label="regulado por")

    return G


def exportar_grafo(G, caminho="figures/grafo_explicabilidade.png"):
    """Exporta grafo como PNG de alta resolucao."""
    cores = {
        "nuclear": "#4FC3F7",
        "contextual": "#A5D6A7",
        "saida": "#EF5350",
        "regra": "#FFB74D",
        "guardrail": "#CE93D8",
    }

    node_colors = [cores.get(G.nodes[n].get("tipo", ""), "#BDBDBD") for n in G.nodes()]

    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_title(
        "Grafo de Explicabilidade - AcolheMente Escolar PB",
        fontsize=14, fontweight="bold", pad=15
    )

    pos = nx.spring_layout(G, seed=42, k=2.0, iterations=80)

    nx.draw_networkx_nodes(G, pos, ax=ax, node_color=node_colors,
                           node_size=1800, edgecolors="#424242", linewidths=1.2)
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=9, font_weight="bold")
    nx.draw_networkx_edges(G, pos, ax=ax, edge_color="#757575",
                           arrows=True, arrowsize=12, width=1.2,
                           connectionstyle="arc3,rad=0.08", alpha=0.7)

    edge_labels = nx.get_edge_attributes(G, "label")
    nx.draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=edge_labels,
                                 font_size=6, font_color="#616161")

    legend = [mpatches.Patch(color=c, label=t.title()) for t, c in cores.items()]
    ax.legend(handles=legend, loc="upper left", fontsize=8, title="Tipo")
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(caminho, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Grafo exportado: {caminho}")
    return caminho


if __name__ == "__main__":
    G = construir_grafo()
    exportar_grafo(G)
    print(f"Nos: {G.number_of_nodes()}, Arestas: {G.number_of_edges()}")
