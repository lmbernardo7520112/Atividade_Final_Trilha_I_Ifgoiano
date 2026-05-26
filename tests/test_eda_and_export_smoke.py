# =====================================================================
# test_eda_and_export_smoke.py
# =====================================================================
# Smoke tests for EDA plots and graph PNG export.
# Ensures coverage of eda_plots.py and export_graph_png.
# All outputs go to a temporary directory.
# =====================================================================

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.acolhemente.rule_graph import (
    build_rule_graph,
    build_governance_graph,
    export_graph_png,
)
from src.acolhemente.eda_plots import (
    plot_pense_pb_vs_ne_br,
    plot_rule_activation_summary,
    COLORS,
)


class TestExportGraphPng:
    """Smoke tests for graph PNG export."""

    def test_export_rule_graph_png(self, tmp_path):
        """Rule graph exports PNG without error."""
        kg = build_rule_graph()
        path = export_graph_png(
            kg, str(tmp_path / "test_rules.png"),
            title="Test Rule Graph"
        )
        assert os.path.exists(path)
        assert os.path.getsize(path) > 1000  # Should be non-trivial PNG

    def test_export_governance_graph_png(self, tmp_path):
        """Governance graph exports PNG without error."""
        kg = build_governance_graph()
        path = export_graph_png(
            kg, str(tmp_path / "test_gov.png"),
            title="Test Governance Graph",
            figsize=(14, 8)
        )
        assert os.path.exists(path)
        assert os.path.getsize(path) > 1000

    def test_export_creates_parent_dirs(self, tmp_path):
        """Export creates parent directories if they don't exist."""
        kg = build_rule_graph()
        path = export_graph_png(
            kg, str(tmp_path / "subdir" / "nested" / "test.png"),
            title="Nested Test"
        )
        assert os.path.exists(path)


class TestEDAPlots:
    """Smoke tests for EDA plotting functions."""

    def test_plot_pense_comparison(self, tmp_path):
        """PeNSE comparison plot generates without error."""
        data = {
            "Sofrimento Emocional": {"PB": 45.2, "NE": 42.1, "BR": 40.5},
            "Baixo Apoio": {"PB": 32.1, "NE": 30.5, "BR": 28.3},
        }
        out = str(tmp_path / "pense_test.png")
        plot_pense_pb_vs_ne_br(data, output_path=out)
        assert os.path.exists(out)
        assert os.path.getsize(out) > 1000

    def test_plot_pense_without_save(self):
        """PeNSE comparison plot works without saving."""
        data = {
            "Indicador A": {"PB": 10, "NE": 20, "BR": 30},
        }
        # Should not raise
        plot_pense_pb_vs_ne_br(data)

    def test_plot_rule_activation(self, tmp_path):
        """Rule activation summary generates without error."""
        results = [
            {"cenario": "Cenário 1", "acolhimento": False, "regras_ativadas": []},
            {"cenario": "Cenário 2", "acolhimento": True, "regras_ativadas": ["R1"]},
            {"cenario": "Cenário 3", "acolhimento": True, "regras_ativadas": ["R3", "R5"]},
        ]
        out = str(tmp_path / "rules_test.png")
        plot_rule_activation_summary(results, output_path=out)
        assert os.path.exists(out)

    def test_plot_rule_activation_without_save(self):
        """Rule activation summary works without saving."""
        results = [
            {"cenario": "Test", "acolhimento": True, "regras_ativadas": ["R1"]},
        ]
        plot_rule_activation_summary(results)

    def test_colors_palette_exists(self):
        """COLORS palette has all required keys."""
        required = {"pb", "ne", "br", "external", "alert", "safe"}
        assert required.issubset(COLORS.keys())
