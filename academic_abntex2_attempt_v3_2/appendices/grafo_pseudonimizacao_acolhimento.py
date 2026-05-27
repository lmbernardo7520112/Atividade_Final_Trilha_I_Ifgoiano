#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
grafo_pseudonimizacao_acolhimento.py
Gera figura do fluxo operacional pseudonimizado do AcolheMente.
Usa apenas ASCII seguro e matplotlib/networkx.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# =====================================================================
# Layout manual do fluxo
# =====================================================================
# Posicoes (x, y)
NODES = {
    "Observacao/\nindicadores\nminimos": (0.5, 0.95),
    "Geracao de\ncase_id\npseudo-\nnimizado": (0.5, 0.82),
    "Motor logico\nprocessa\nE,B,V,S,C,I": (0.5, 0.67),
    "Saida A +\nregras\nacionadas": (0.5, 0.54),
    "Revisao humana\nautorizada": (0.5, 0.41),
    "Reidentificacao\nrestrita\n(equipe designada)": (0.5, 0.28),
    "Acolhimento/\nencaminhamento\nPSE/UBS/CAPS": (0.5, 0.15),
    "Registro\nauditavel": (0.5, 0.03),
}

PROHIBITIONS = {
    "Motor NAO\nve nome": (0.13, 0.67),
    "Painel NAO\nmostra ranking": (0.87, 0.54),
    "Professores NAO\nacessam chave": (0.13, 0.28),
    "GitHub NAO\nrecebe dados\nreais": (0.87, 0.82),
}


def draw_flow(output_path):
    fig, ax = plt.subplots(figsize=(10, 14))
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.02, 1.02)
    ax.axis("off")
    fig.patch.set_facecolor("white")

    # Draw main flow boxes
    positions = list(NODES.items())
    box_w, box_h = 0.28, 0.08

    for i, (label, (x, y)) in enumerate(positions):
        color = "#2196F3"  # blue default
        if "Motor" in label:
            color = "#4CAF50"  # green
        elif "Revisao" in label:
            color = "#FF9800"  # orange
        elif "Reidentificacao" in label:
            color = "#9C27B0"  # purple
        elif "Acolhimento" in label:
            color = "#E91E63"  # pink
        elif "Registro" in label:
            color = "#607D8B"  # grey
        elif "case_id" in label:
            color = "#00BCD4"  # cyan

        rect = mpatches.FancyBboxPatch(
            (x - box_w / 2, y - box_h / 2),
            box_w, box_h,
            boxstyle="round,pad=0.01",
            facecolor=color, edgecolor="white",
            linewidth=1.5, alpha=0.9
        )
        ax.add_patch(rect)
        ax.text(x, y, label, ha="center", va="center",
                fontsize=8.5, fontweight="bold", color="white",
                linespacing=1.1)

        # Arrow to next node
        if i < len(positions) - 1:
            next_y = positions[i + 1][1][1]
            ax.annotate(
                "", xy=(x, next_y + box_h / 2 + 0.005),
                xytext=(x, y - box_h / 2 - 0.005),
                arrowprops=dict(arrowstyle="->", color="#333333",
                                lw=2, connectionstyle="arc3")
            )

    # Draw prohibition nodes
    for label, (x, y) in PROHIBITIONS.items():
        rect = mpatches.FancyBboxPatch(
            (x - 0.11, y - 0.035),
            0.22, 0.07,
            boxstyle="round,pad=0.01",
            facecolor="#F44336", edgecolor="#B71C1C",
            linewidth=2, alpha=0.85
        )
        ax.add_patch(rect)
        ax.text(x, y, label, ha="center", va="center",
                fontsize=7.5, fontweight="bold", color="white",
                linespacing=1.1)

        # Dashed line to nearest main node
        target_y = y
        ax.plot(
            [x + (0.11 if x < 0.5 else -0.11), 0.5 - box_w / 2 if x < 0.5 else 0.5 + box_w / 2],
            [y, target_y],
            linestyle="--", color="#F44336", lw=1.5, alpha=0.6
        )

    # Title
    ax.text(0.5, 1.01,
            "Fluxo Operacional Pseudonimizado do AcolheMente",
            ha="center", va="bottom", fontsize=13, fontweight="bold",
            color="#1a1a1a")

    # Legend
    legend_items = [
        mpatches.Patch(facecolor="#2196F3", label="Etapa principal"),
        mpatches.Patch(facecolor="#4CAF50", label="Motor logico"),
        mpatches.Patch(facecolor="#FF9800", label="Revisao humana"),
        mpatches.Patch(facecolor="#9C27B0", label="Reidentificacao restrita"),
        mpatches.Patch(facecolor="#F44336", label="Proibicao"),
    ]
    ax.legend(handles=legend_items, loc="lower right",
              fontsize=7.5, framealpha=0.9, edgecolor="#ccc")

    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=200, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    plt.close()
    print(f"Figura gerada: {output_path}")


if __name__ == "__main__":
    base = os.path.dirname(os.path.dirname(__file__))
    out = os.path.join(base, "figures",
                       "fluxo_pseudonimizacao_acolhimento.png")
    draw_flow(out)
