# =====================================================================
# test_no_genai_dependency_in_core_notebook.py
# =====================================================================
# Guardrail: O notebook final e os módulos core NÃO podem ter
# dependência obrigatória de google.genai, openai ou qualquer API
# externa de IA generativa.
#
# O grafo é determinístico. O motor lógico é determinístico.
# Zero dependência de LLM para execução do notebook final.
# =====================================================================

import pytest
import sys
import os
import ast
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


# Módulos core que NÃO podem importar APIs de IA generativa
CORE_MODULES = [
    "src/acolhemente/__init__.py",
    "src/acolhemente/graph_schema.py",
    "src/acolhemente/rule_graph.py",
    "src/acolhemente/eda_plots.py",
]

# Imports proibidos nos módulos core
FORBIDDEN_IMPORTS = {
    "google.genai",
    "google.generativeai",
    "openai",
    "anthropic",
    "langchain",
    "langchain_core",
    "langchain_google_genai",
    "vertexai",
    "vertexai.generative_models",
}

# Strings proibidas que indicam dependência de API
FORBIDDEN_STRINGS = {
    "genai.Client",
    "GenerativeModel",
    "openai.ChatCompletion",
    "openai.Completion",
    "anthropic.Anthropic",
    "GOOGLE_API_KEY",
    "OPENAI_API_KEY",
    "ANTHROPIC_API_KEY",
}

# Caminho base do projeto
BASE_DIR = Path(__file__).parent.parent


class TestNoGenAIDependency:
    """Garante zero dependência de LLM/API externa nos módulos core."""

    def _get_imports_from_file(self, filepath: Path) -> set:
        """Extrai todos os imports de um arquivo Python via AST."""
        if not filepath.exists():
            return set()

        source = filepath.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(filepath))
        imports = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module)

        return imports

    def _check_file_for_forbidden_strings(self, filepath: Path) -> list:
        """Verifica se arquivo contém strings proibidas."""
        if not filepath.exists():
            return []

        content = filepath.read_text(encoding="utf-8")
        violations = []
        for forbidden in FORBIDDEN_STRINGS:
            if forbidden in content:
                violations.append(forbidden)
        return violations

    @pytest.mark.parametrize("module_path", CORE_MODULES)
    def test_no_forbidden_imports(self, module_path):
        """Módulo core não importa APIs de IA generativa."""
        filepath = BASE_DIR / module_path
        if not filepath.exists():
            pytest.skip(f"Arquivo {module_path} não encontrado")

        imports = self._get_imports_from_file(filepath)
        violations = imports & FORBIDDEN_IMPORTS
        assert len(violations) == 0, (
            f"GENAI DEPENDENCY VIOLATION em {module_path}: "
            f"Imports proibidos encontrados: {violations}. "
            f"O notebook final deve executar sem API externa."
        )

    @pytest.mark.parametrize("module_path", CORE_MODULES)
    def test_no_forbidden_strings(self, module_path):
        """Módulo core não contém strings de API generativa."""
        filepath = BASE_DIR / module_path
        if not filepath.exists():
            pytest.skip(f"Arquivo {module_path} não encontrado")

        violations = self._check_file_for_forbidden_strings(filepath)
        assert len(violations) == 0, (
            f"GENAI STRING VIOLATION em {module_path}: "
            f"Strings proibidas encontradas: {violations}. "
            f"ADR-009 proíbe dependência de LLM no core."
        )

    def test_graph_schema_importable_without_genai(self):
        """graph_schema.py importa sem google.genai instalado."""
        # Se importou até aqui, já funciona
        from src.acolhemente.graph_schema import (
            Entity, Relationship, KnowledgeGraph,
        )
        assert Entity is not None
        assert Relationship is not None
        assert KnowledgeGraph is not None

    def test_rule_graph_importable_without_genai(self):
        """rule_graph.py importa sem google.genai instalado."""
        from src.acolhemente.rule_graph import (
            build_proposition_graph,
            build_rule_graph,
        )
        assert build_proposition_graph is not None
        assert build_rule_graph is not None

    def test_rule_graph_builds_without_network(self):
        """Grafo de regras constrói sem acesso à rede."""
        from src.acolhemente.rule_graph import build_rule_graph
        # Se esta função depender de API externa, falhará aqui
        kg = build_rule_graph()
        assert kg.entity_count > 0
        assert kg.relationship_count > 0

    def test_eda_plots_no_genai_import(self):
        """eda_plots.py não importa APIs de IA generativa."""
        filepath = BASE_DIR / "src/acolhemente/eda_plots.py"
        if not filepath.exists():
            pytest.skip("eda_plots.py não encontrado")

        imports = self._get_imports_from_file(filepath)
        violations = imports & FORBIDDEN_IMPORTS
        assert len(violations) == 0, (
            f"GENAI DEPENDENCY em eda_plots.py: {violations}"
        )

    def test_no_genai_in_any_src_file(self):
        """Nenhum arquivo em src/acolhemente/ importa GenAI."""
        src_dir = BASE_DIR / "src" / "acolhemente"
        if not src_dir.exists():
            pytest.skip("src/acolhemente/ não encontrado")

        all_violations = {}
        for py_file in src_dir.glob("*.py"):
            imports = self._get_imports_from_file(py_file)
            violations = imports & FORBIDDEN_IMPORTS
            if violations:
                all_violations[py_file.name] = violations

        assert len(all_violations) == 0, (
            f"GENAI DEPENDENCY encontrada em: {all_violations}"
        )
