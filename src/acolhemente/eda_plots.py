# =====================================================================
# eda_plots.py — Funções de EDA Governada por Tiers de Proveniência
# =====================================================================
# Funções de visualização para Análise Exploratória de Dados (EDA)
# com separação estrita entre TIER_A (PeNSE) e TIER_C (externo).
#
# Nenhuma função desta biblioteca:
# - Gera diagnóstico clínico
# - Classifica aluno individual
# - Mistura dados de tiers distintos
# - Depende de LLM/API externa
# =====================================================================

from __future__ import annotations

from typing import Dict, List, Optional, Tuple

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Tentar importar pandas e seaborn; se não disponíveis, falhar gracefully
try:
    import pandas as pd
    import seaborn as sns
    _HAS_PANDAS = True
except ImportError:
    _HAS_PANDAS = False


# =====================================================================
# PALETA DE CORES PADRONIZADA
# =====================================================================
COLORS = {
    "pb": "#1565C0",       # Paraíba — Azul escuro
    "ne": "#42A5F5",       # Nordeste — Azul médio
    "br": "#90CAF9",       # Brasil — Azul claro
    "external": "#FFA726",  # Dataset externo — Laranja
    "alert": "#E53935",     # Acolhimento — Vermelho
    "safe": "#43A047",      # Seguro — Verde
}


def _require_pandas():
    """Verifica disponibilidade de pandas/seaborn."""
    if not _HAS_PANDAS:
        raise ImportError(
            "pandas e seaborn são necessários para EDA. "
            "Instale com: pip install pandas seaborn"
        )


# =====================================================================
# EDA GOVERNADA — TIER_A (PeNSE 2024)
# =====================================================================

def plot_pense_pb_vs_ne_br(
    data: Dict[str, Dict[str, float]],
    title: str = "Indicadores de Saúde Mental — PeNSE 2024",
    ylabel: str = "Prevalência (%)",
    output_path: Optional[str] = None,
    figsize: Tuple[int, int] = (12, 6),
) -> None:
    """
    Gráfico de barras agrupadas comparando Paraíba, Nordeste e Brasil.

    TIER_A exclusivo — nenhum dado externo é plotado aqui.

    Parâmetros:
    - data: dicionário {indicador: {PB: %, NE: %, BR: %}}
      Exemplo: {"Sofrimento Emocional": {"PB": 45.2, "NE": 42.1, "BR": 40.5}}
    - title: título do gráfico
    - output_path: se fornecido, salva PNG em alta resolução
    """
    indicadores = list(data.keys())
    n = len(indicadores)
    x = np.arange(n)
    width = 0.25

    fig, ax = plt.subplots(figsize=figsize)

    pb_vals = [data[ind].get("PB", 0) for ind in indicadores]
    ne_vals = [data[ind].get("NE", 0) for ind in indicadores]
    br_vals = [data[ind].get("BR", 0) for ind in indicadores]

    bars_pb = ax.bar(x - width, pb_vals, width, label="Paraíba",
                     color=COLORS["pb"], edgecolor="white", linewidth=0.5)
    bars_ne = ax.bar(x, ne_vals, width, label="Nordeste",
                     color=COLORS["ne"], edgecolor="white", linewidth=0.5)
    bars_br = ax.bar(x + width, br_vals, width, label="Brasil",
                     color=COLORS["br"], edgecolor="white", linewidth=0.5)

    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_ylabel(ylabel, fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels(indicadores, rotation=15, ha="right", fontsize=9)
    ax.legend(fontsize=10)
    ax.grid(axis="y", alpha=0.3, linestyle="--")
    ax.set_ylim(0, max(max(pb_vals), max(ne_vals), max(br_vals)) * 1.2)

    # Anotações de valor nas barras
    for bars in [bars_pb, bars_ne, bars_br]:
        for bar in bars:
            height = bar.get_height()
            if height > 0:
                ax.annotate(
                    f"{height:.1f}%",
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha="center", va="bottom", fontsize=7,
                )

    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches="tight",
                    facecolor="white")
    plt.close(fig)


# =====================================================================
# EDA EXPLORATÓRIA — TIER_C (Dataset Externo)
# =====================================================================

def plot_external_behavioral_distributions(
    df: "pd.DataFrame",
    columns: List[str],
    title: str = "Distribuições Comportamentais — Dataset Externo (TIER_C)",
    subtitle: str = ("⚠ Dados exploratórios SEM aplicabilidade inferencial "
                     "para população brasileira"),
    output_path: Optional[str] = None,
    figsize: Tuple[int, int] = (14, 8),
) -> None:
    """
    Histogramas de variáveis comportamentais do dataset externo.

    TIER_C exclusivo — nenhuma conclusão sobre Brasil, Nordeste ou Paraíba.
    """
    _require_pandas()

    n_cols = min(len(columns), 3)
    n_rows = (len(columns) + n_cols - 1) // n_cols

    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    fig.suptitle(title, fontsize=14, fontweight="bold", y=1.02)
    fig.text(0.5, 0.99, subtitle, ha="center", fontsize=9,
             style="italic", color="#E53935")

    if n_rows == 1 and n_cols == 1:
        axes = np.array([axes])
    axes_flat = axes.flatten() if hasattr(axes, "flatten") else [axes]

    for i, col in enumerate(columns):
        if i < len(axes_flat) and col in df.columns:
            ax = axes_flat[i]
            sns.histplot(df[col].dropna(), ax=ax, kde=True,
                         color=COLORS["external"], edgecolor="white",
                         alpha=0.7)
            ax.set_title(col.replace("_", " ").title(), fontsize=10)
            ax.set_xlabel("")

    # Esconder eixos vazios
    for j in range(len(columns), len(axes_flat)):
        axes_flat[j].set_visible(False)

    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches="tight",
                    facecolor="white")
    plt.close(fig)


def plot_external_correlation_matrix(
    df: "pd.DataFrame",
    columns: List[str],
    title: str = "Matriz de Correlação — Dataset Externo (TIER_C)",
    subtitle: str = ("⚠ Correlações exploratórias SEM generalização para "
                     "escola pública brasileira"),
    output_path: Optional[str] = None,
    figsize: Tuple[int, int] = (10, 8),
) -> None:
    """
    Heatmap de correlação do dataset externo.

    TIER_C exclusivo — disclaimer obrigatório no título.
    """
    _require_pandas()

    valid_cols = [c for c in columns if c in df.columns]
    corr = df[valid_cols].corr()

    fig, ax = plt.subplots(figsize=figsize)
    fig.suptitle(title, fontsize=14, fontweight="bold", y=1.02)
    fig.text(0.5, 0.99, subtitle, ha="center", fontsize=9,
             style="italic", color="#E53935")

    mask = np.triu(np.ones_like(corr, dtype=bool))
    sns.heatmap(
        corr, mask=mask, annot=True, fmt=".2f",
        cmap="coolwarm", center=0, square=True,
        linewidths=0.5, ax=ax,
        vmin=-1, vmax=1,
    )

    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right",
                       fontsize=9)
    ax.set_yticklabels(ax.get_yticklabels(), fontsize=9)

    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches="tight",
                    facecolor="white")
    plt.close(fig)


# =====================================================================
# RESULTADOS — ATIVAÇÃO DE REGRAS (cenários sintéticos)
# =====================================================================

def plot_rule_activation_summary(
    results: List[Dict[str, object]],
    title: str = "Resumo de Ativação de Regras — Cenários Sintéticos",
    subtitle: str = "Dados fictícios para demonstração — nenhum aluno real",
    output_path: Optional[str] = None,
    figsize: Tuple[int, int] = (12, 6),
) -> None:
    """
    Gráfico de barras mostrando quais regras foram ativadas nos cenários.

    Usa apenas dados sintéticos (TIER_B).
    Cada resultado deve ter: {cenário, regras_ativadas, acolhimento}

    Parâmetros:
    - results: lista de dicionários com chaves:
        - "cenario": str (nome do cenário)
        - "acolhimento": bool (se A foi inferido)
        - "regras_ativadas": list[str] (ex: ["R1", "R3"])
    """
    cenarios = [r["cenario"] for r in results]
    acolhimento_flags = [r["acolhimento"] for r in results]

    fig, ax = plt.subplots(figsize=figsize)
    fig.suptitle(title, fontsize=14, fontweight="bold", y=1.02)
    fig.text(0.5, 0.99, subtitle, ha="center", fontsize=9,
             style="italic", color="#757575")

    colors = [COLORS["alert"] if a else COLORS["safe"]
              for a in acolhimento_flags]

    ax.barh(cenarios, [1] * len(cenarios), color=colors,
            edgecolor="white", linewidth=0.5)

    for i, result in enumerate(results):
        label = "ACOLHER" if result["acolhimento"] else "OK"
        regras = ", ".join(result.get("regras_ativadas", []))
        text = f"{label}"
        if regras:
            text += f" ({regras})"
        ax.text(0.5, i, text, va="center", ha="center",
                fontsize=9, fontweight="bold", color="white")

    ax.set_xlim(0, 1)
    ax.set_xlabel("")
    ax.xaxis.set_visible(False)
    ax.invert_yaxis()

    # Legenda
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=COLORS["alert"], label="Acolhimento Prioritário"),
        Patch(facecolor=COLORS["safe"], label="Sem Alerta"),
    ]
    ax.legend(handles=legend_elements, loc="lower right", fontsize=9)

    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches="tight",
                    facecolor="white")
    plt.close(fig)
