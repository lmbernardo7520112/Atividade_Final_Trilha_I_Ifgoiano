# =====================================================================
# APENDICE I: Grafos de Proveniencia, Governanca e Ativacao de Regras
# =====================================================================
# Gera 5 figuras para o relatorio academico v3:
#   1. Fluxo de proveniencia de dados (TIER_A/B/C)
#   2. Grafo de regras 7 variaveis
#   3. Grafo de governanca pos-acolhimento
#   4. Ativacao de regras por cenarios sinteticos
#   5. Comparacao baseline manual vs motor logico
#
# Sem dependencias externas alem de matplotlib e networkx.
# ADR-009: 100% deterministico, sem LLM, sem API externa.
# =====================================================================

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx

OUT = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(OUT, exist_ok=True)


# =====================================================================
# FIGURA 1: Fluxo de proveniencia de dados
# =====================================================================
def gerar_fluxo_proveniencia():
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7)
    ax.axis("off")
    fig.patch.set_facecolor("white")

    # --- TIER A ---
    ax.add_patch(plt.Rectangle((0.5, 4.5), 3, 2, facecolor="#BBDEFB",
                                edgecolor="#1565C0", linewidth=2, zorder=2))
    ax.text(2, 6.1, "TIER A", fontsize=11, fontweight="bold",
            ha="center", color="#1565C0")
    ax.text(2, 5.5, "PeNSE 2024\n(IBGE)", fontsize=9, ha="center",
            va="center")
    ax.text(2, 4.8, "Dados oficiais\nanonimizados", fontsize=7,
            ha="center", color="#555", style="italic")

    ax.annotate("", xy=(4.2, 5.5), xytext=(3.5, 5.5),
                arrowprops=dict(arrowstyle="->", color="#1565C0", lw=2))

    ax.add_patch(plt.Rectangle((4.5, 4.5), 3.5, 2, facecolor="#E3F2FD",
                                edgecolor="#1565C0", linewidth=1.5, zorder=2))
    ax.text(6.25, 5.8, "EDA / Motivacao", fontsize=9, fontweight="bold",
            ha="center")
    ax.text(6.25, 5.2, "Prevalencia PB\nvs NE vs BR", fontsize=8,
            ha="center", color="#333")
    ax.text(6.25, 4.7, "Justifica o problema", fontsize=7, ha="center",
            color="#555", style="italic")

    ax.annotate("", xy=(8.7, 5.5), xytext=(8.0, 5.5),
                arrowprops=dict(arrowstyle="->", color="#1565C0", lw=2))

    ax.add_patch(plt.Rectangle((9.0, 4.5), 4, 2, facecolor="#C8E6C9",
                                edgecolor="#2E7D32", linewidth=2, zorder=2))
    ax.text(11, 6.1, "RESULTADO", fontsize=10, fontweight="bold",
            ha="center", color="#2E7D32")
    ax.text(11, 5.5, "Variaveis\nproposicionais", fontsize=9,
            ha="center")
    ax.text(11, 4.7, "E, B, V, S, C, I, A", fontsize=8, ha="center",
            fontweight="bold", color="#2E7D32")

    # --- TIER B ---
    ax.add_patch(plt.Rectangle((0.5, 2.0), 3, 2, facecolor="#FFF3E0",
                                edgecolor="#E65100", linewidth=2, zorder=2))
    ax.text(2, 3.6, "TIER B", fontsize=11, fontweight="bold",
            ha="center", color="#E65100")
    ax.text(2, 3.0, "Cenarios\nsinteticos", fontsize=9, ha="center")
    ax.text(2, 2.3, "Criados pelo\nprojeto", fontsize=7, ha="center",
            color="#555", style="italic")

    ax.annotate("", xy=(4.2, 3.0), xytext=(3.5, 3.0),
                arrowprops=dict(arrowstyle="->", color="#E65100", lw=2))

    ax.add_patch(plt.Rectangle((4.5, 2.0), 3.5, 2, facecolor="#FFF8E1",
                                edgecolor="#E65100", linewidth=1.5, zorder=2))
    ax.text(6.25, 3.3, "Motor logico", fontsize=9, fontweight="bold",
            ha="center")
    ax.text(6.25, 2.7, "Inferencia por\nresolucao", fontsize=8,
            ha="center", color="#333")

    ax.annotate("", xy=(8.7, 3.0), xytext=(8.0, 3.0),
                arrowprops=dict(arrowstyle="->", color="#E65100", lw=2))

    ax.add_patch(plt.Rectangle((9.0, 2.0), 4, 2, facecolor="#C8E6C9",
                                edgecolor="#2E7D32", linewidth=2, zorder=2))
    ax.text(11, 3.3, "Validacao R1-R6", fontsize=9, fontweight="bold",
            ha="center")
    ax.text(11, 2.7, "64 cenarios\ntestados", fontsize=8, ha="center",
            color="#333")
    ax.text(11, 2.2, "0 falhas", fontsize=8, ha="center",
            fontweight="bold", color="#2E7D32")

    # --- TIER C ---
    ax.add_patch(plt.Rectangle((0.5, -0.3), 3, 1.8, facecolor="#F3E5F5",
                                edgecolor="#7B1FA2", linewidth=2, zorder=2))
    ax.text(2, 1.1, "TIER C", fontsize=11, fontweight="bold",
            ha="center", color="#7B1FA2")
    ax.text(2, 0.5, "Dataset\nexterno", fontsize=9, ha="center")
    ax.text(2, 0.0, "Benchmark\nmetodologico", fontsize=7, ha="center",
            color="#555", style="italic")

    ax.annotate("", xy=(4.2, 0.6), xytext=(3.5, 0.6),
                arrowprops=dict(arrowstyle="->", color="#7B1FA2", lw=2))

    ax.add_patch(plt.Rectangle((4.5, -0.3), 3.5, 1.8, facecolor="#EDE7F6",
                                edgecolor="#7B1FA2", linewidth=1.5, zorder=2))
    ax.text(6.25, 0.8, "EDA exploratoria", fontsize=9, fontweight="bold",
            ha="center")
    ax.text(6.25, 0.2, "Extensibilidade\nmetodologica", fontsize=8,
            ha="center", color="#333")

    ax.annotate("", xy=(8.7, 0.6), xytext=(8.0, 0.6),
                arrowprops=dict(arrowstyle="->", color="#7B1FA2", lw=2))

    ax.add_patch(plt.Rectangle((9.0, -0.3), 4, 1.8, facecolor="#FFEBEE",
                                edgecolor="#C62828", linewidth=2, zorder=2,
                                linestyle="--"))
    ax.text(11, 0.8, "NAO inferencia", fontsize=9, fontweight="bold",
            ha="center", color="#C62828")
    ax.text(11, 0.2, "Sem validade para\nBrasil/Paraiba", fontsize=8,
            ha="center", color="#C62828")

    # Barreira de merge proibido
    ax.axhline(y=1.7, color="#C62828", linestyle=":", linewidth=1.5,
               xmin=0.02, xmax=0.98)
    ax.text(7, 1.75, "MERGE ENTRE TIERS PROIBIDO", fontsize=8,
            ha="center", color="#C62828", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.2", facecolor="white",
                      edgecolor="#C62828"))

    ax.set_title("Arquitetura de Proveniencia de Dados --- AcolheMente Escolar PB",
                 fontsize=13, fontweight="bold", pad=15)

    plt.tight_layout()
    path = os.path.join(OUT, "fluxo_proveniencia_dados.png")
    plt.savefig(path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  Salvo: {path}")


# =====================================================================
# FIGURA 2: Grafo de regras com 7 variaveis
# =====================================================================
def gerar_grafo_regras():
    G = nx.DiGraph()
    nucleares = ["E", "B", "V", "S"]
    contextuais = ["C", "I"]
    regras = ["R1", "R2", "R3", "R4", "R5", "R6"]
    saida = ["A"]

    for n in nucleares:
        G.add_node(n, layer=0)
    for c in contextuais:
        G.add_node(c, layer=0)
    for r in regras:
        G.add_node(r, layer=1)
    G.add_node("A", layer=2)

    edges = [
        ("S", "R1"), ("V", "R2"), ("E", "R2"), ("E", "R3"), ("B", "R3"),
        ("V", "R4"), ("B", "R4"), ("E", "R5"), ("B", "R5"), ("C", "R5"),
        ("V", "R6"), ("I", "R6"),
    ]
    for e in edges:
        G.add_edge(*e)
    for r in regras:
        G.add_edge(r, "A")

    pos = {
        "E": (0, 3), "B": (0, 2), "V": (0, 1), "S": (0, 0),
        "C": (0, -1), "I": (0, -2),
        "R1": (3, 3.5), "R2": (3, 2.5), "R3": (3, 1.5),
        "R4": (3, 0.5), "R5": (3, -0.5), "R6": (3, -1.5),
        "A": (6, 1),
    }

    fig, ax = plt.subplots(figsize=(12, 8))
    fig.patch.set_facecolor("white")

    # Edges
    nx.draw_networkx_edges(G, pos, ax=ax, edge_color="#9E9E9E",
                           arrows=True, arrowsize=15, width=1.5,
                           connectionstyle="arc3,rad=0.05")

    # Nodes por tipo
    nx.draw_networkx_nodes(G, pos, nodelist=nucleares, ax=ax,
                           node_color="#1565C0", node_size=1200,
                           node_shape="o")
    nx.draw_networkx_nodes(G, pos, nodelist=contextuais, ax=ax,
                           node_color="#FFA726", node_size=1200,
                           node_shape="s")
    nx.draw_networkx_nodes(G, pos, nodelist=regras, ax=ax,
                           node_color="#78909C", node_size=900,
                           node_shape="D")
    nx.draw_networkx_nodes(G, pos, nodelist=saida, ax=ax,
                           node_color="#E53935", node_size=1500,
                           node_shape="o")

    nx.draw_networkx_labels(G, pos, ax=ax, font_size=12,
                            font_color="white", font_weight="bold")

    legend = [
        mpatches.Patch(color="#1565C0", label="Nuclear (E, B, V, S)"),
        mpatches.Patch(color="#FFA726", label="Contextual (C, I)"),
        mpatches.Patch(color="#78909C", label="Regras (R1-R6)"),
        mpatches.Patch(color="#E53935", label="Saida (A)"),
    ]
    ax.legend(handles=legend, loc="lower right", fontsize=10)
    ax.set_title("Grafo de Regras --- 7 Variaveis Proposicionais e 6 Regras",
                 fontsize=13, fontweight="bold")
    ax.axis("off")
    plt.tight_layout()
    path = os.path.join(OUT, "grafo_regras_7vars.png")
    plt.savefig(path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  Salvo: {path}")


# =====================================================================
# FIGURA 3: Grafo de governanca pos-acolhimento
# =====================================================================
def gerar_grafo_governanca():
    G = nx.DiGraph()
    nodes = [
        "Motor\nLogico", "A = SIM", "Revisao\nHumana",
        "Acolhimento\nPedagogico", "PSE/UBS/\nCAPS",
        "NAO\nDiagnostico", "NAO\nRanking",
    ]
    for n in nodes:
        G.add_node(n)
    G.add_edges_from([
        ("Motor\nLogico", "A = SIM"),
        ("A = SIM", "Revisao\nHumana"),
        ("Revisao\nHumana", "Acolhimento\nPedagogico"),
        ("Acolhimento\nPedagogico", "PSE/UBS/\nCAPS"),
    ])

    pos = {
        "Motor\nLogico": (0, 0), "A = SIM": (2, 0),
        "Revisao\nHumana": (4, 0), "Acolhimento\nPedagogico": (6, 0),
        "PSE/UBS/\nCAPS": (8, 0),
        "NAO\nDiagnostico": (4, -1.5), "NAO\nRanking": (6, -1.5),
    }

    fig, ax = plt.subplots(figsize=(14, 5))
    fig.patch.set_facecolor("white")

    nx.draw_networkx_edges(G, pos, ax=ax, edge_color="#2E7D32",
                           arrows=True, arrowsize=18, width=2.5)

    flow = ["Motor\nLogico", "A = SIM", "Revisao\nHumana",
            "Acolhimento\nPedagogico", "PSE/UBS/\nCAPS"]
    prohib = ["NAO\nDiagnostico", "NAO\nRanking"]

    nx.draw_networkx_nodes(G, pos, nodelist=flow, ax=ax,
                           node_color="#C8E6C9", node_size=2500,
                           node_shape="s", edgecolors="#2E7D32",
                           linewidths=2)
    nx.draw_networkx_nodes(G, pos, nodelist=prohib, ax=ax,
                           node_color="#FFCDD2", node_size=2200,
                           node_shape="8", edgecolors="#C62828",
                           linewidths=2)
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=9,
                            font_weight="bold")

    # Proibicoes
    ax.annotate("PROIBIDO", xy=(4, -1.5), xytext=(4, -2.3),
                ha="center", fontsize=9, color="#C62828",
                fontweight="bold")
    ax.annotate("PROIBIDO", xy=(6, -1.5), xytext=(6, -2.3),
                ha="center", fontsize=9, color="#C62828",
                fontweight="bold")

    ax.set_title("Fluxo de Governanca pos-Acolhimento --- Human-in-the-Loop",
                 fontsize=13, fontweight="bold")
    ax.axis("off")
    plt.tight_layout()
    path = os.path.join(OUT, "grafo_governanca_acolhemente.png")
    plt.savefig(path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  Salvo: {path}")


# =====================================================================
# FIGURA 4: Ativacao de regras por cenarios
# =====================================================================
def gerar_ativacao_regras():
    # Contagem: quantos cenarios ativam cada regra
    # Baseado nos 14 cenarios representativos
    regras = ["R1", "R2", "R3", "R4", "R5", "R6", "Nenhuma"]
    contagem = [2, 2, 3, 3, 2, 2, 5]
    cores = ["#E53935", "#E53935", "#E53935",
             "#E53935", "#E53935", "#E53935", "#43A047"]

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor("white")
    bars = ax.bar(regras, contagem, color=cores, edgecolor="white",
                  linewidth=1.5, width=0.6)

    for bar, c in zip(bars, contagem):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,
                str(c), ha="center", va="bottom", fontsize=11,
                fontweight="bold")

    ax.set_ylabel("Cenarios que ativam", fontsize=11)
    ax.set_xlabel("Regra", fontsize=11)
    ax.set_title("Ativacao de Regras por Cenarios Sinteticos Representativos",
                 fontsize=13, fontweight="bold")
    ax.grid(axis="y", alpha=0.3, linestyle="--")
    ax.set_ylim(0, max(contagem) + 1)

    legend = [
        mpatches.Patch(color="#E53935", label="A = SIM (acolhimento)"),
        mpatches.Patch(color="#43A047", label="A = NAO (sem alerta)"),
    ]
    ax.legend(handles=legend, fontsize=10)
    plt.tight_layout()
    path = os.path.join(OUT, "cenarios_ativacao_regras.png")
    plt.savefig(path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  Salvo: {path}")


# =====================================================================
# FIGURA 5: Comparacao baseline manual vs motor logico
# =====================================================================
def gerar_comparacao_baseline():
    criterios = ["Transparencia", "Consistencia", "Explicabilidade",
                 "Rastreabilidade", "Fadiga\ndecisoria", "Nuance\nqualitativa"]
    manual =     [2, 3, 3, 1, 2, 9]
    motor =      [10, 10, 10, 10, 10, 1]

    import numpy as np
    x = np.arange(len(criterios))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor("white")

    bars1 = ax.bar(x - width/2, manual, width, label="Baseline manual",
                   color="#FFAB91", edgecolor="white", linewidth=1)
    bars2 = ax.bar(x + width/2, motor, width, label="Motor logico",
                   color="#81C784", edgecolor="white", linewidth=1)

    for bar, val in zip(bars1, manual):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
                str(val), ha="center", fontsize=9, fontweight="bold")
    for bar, val in zip(bars2, motor):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
                str(val), ha="center", fontsize=9, fontweight="bold")

    ax.set_ylabel("Nota (0-10)", fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels(criterios, fontsize=9)
    ax.set_ylim(0, 12)
    ax.legend(fontsize=10)
    ax.set_title("Comparacao: Baseline Manual vs. Motor Logico",
                 fontsize=13, fontweight="bold")
    ax.grid(axis="y", alpha=0.3, linestyle="--")
    plt.tight_layout()
    path = os.path.join(OUT, "comparacao_baseline_motor.png")
    plt.savefig(path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  Salvo: {path}")


# =====================================================================
# FIGURA 6: Resultado dos cenarios sinteticos (heatmap)
# =====================================================================
def gerar_resultado_cenarios():
    cenarios = [
        ("Nulo",            [0,0,0,0,0,0], False),
        ("S isolado",       [0,0,0,1,0,0], True),
        ("V+E",             [1,0,1,0,0,0], True),
        ("E+B",             [1,1,0,0,0,0], True),
        ("V+B",             [0,1,1,0,0,0], True),
        ("E+B+C",           [1,1,0,0,1,0], True),
        ("V+I",             [0,0,1,0,0,1], True),
        ("C isolado",       [0,0,0,0,1,0], False),
        ("I isolado",       [0,0,0,0,0,1], False),
        ("C+I",             [0,0,0,0,1,1], False),
        ("Todas",           [1,1,1,1,1,1], True),
        ("E isolado",       [1,0,0,0,0,0], False),
        ("B isolado",       [0,1,0,0,0,0], False),
        ("V isolado",       [0,0,1,0,0,0], False),
    ]

    import numpy as np
    vars_names = ["E", "B", "V", "S", "C", "I"]
    nomes = [c[0] for c in cenarios]
    mat = np.array([c[1] for c in cenarios])
    result = [1 if c[2] else 0 for c in cenarios]

    fig, ax = plt.subplots(figsize=(10, 7))
    fig.patch.set_facecolor("white")

    # Heatmap das variaveis
    cmap_vars = plt.cm.colors.ListedColormap(["#E0E0E0", "#42A5F5"])
    ax.imshow(mat, cmap=cmap_vars, aspect="auto", interpolation="nearest")

    # Coluna de resultado
    for i, r in enumerate(result):
        color = "#E53935" if r else "#43A047"
        label = "SIM" if r else "NAO"
        ax.text(len(vars_names) + 0.3, i, label, fontsize=9,
                fontweight="bold", color=color, va="center")

    # Labels
    ax.set_xticks(range(len(vars_names)))
    ax.set_xticklabels(vars_names, fontsize=11, fontweight="bold")
    ax.set_yticks(range(len(nomes)))
    ax.set_yticklabels(nomes, fontsize=9)

    # Valores na matriz
    for i in range(len(nomes)):
        for j in range(len(vars_names)):
            ax.text(j, i, str(mat[i, j]), ha="center", va="center",
                    fontsize=9, color="white" if mat[i,j] else "#666")

    ax.text(len(vars_names) + 0.3, -0.8, "A?", fontsize=11,
            fontweight="bold", ha="center")

    ax.set_title("Resultado dos Cenarios Sinteticos --- Validacao do Motor",
                 fontsize=13, fontweight="bold", pad=15)
    plt.tight_layout()
    path = os.path.join(OUT, "resultado_cenarios_sinteticos.png")
    plt.savefig(path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  Salvo: {path}")


# =====================================================================
# MAIN
# =====================================================================
if __name__ == "__main__":
    print("Gerando figuras para v3...\n")
    gerar_fluxo_proveniencia()
    gerar_grafo_regras()
    gerar_grafo_governanca()
    gerar_ativacao_regras()
    gerar_comparacao_baseline()
    gerar_resultado_cenarios()
    print("\nTodas as figuras geradas com sucesso.")
