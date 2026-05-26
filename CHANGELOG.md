# CHANGELOG

Todas as mudanças notáveis do projeto AcolheMente Escolar PB.

## [v1.0.0] — 2026-05-26

### Promovido de v0.3.0-rc1
- PDF compilado com sucesso via `jupyter nbconvert --to pdf` + xelatex (TinyTeX)
- Arquivo: `reports/pdf/Trabalho_Trilha_I_AcolheMente_PB.pdf` (71 KB)
- LaTeX: `reports/tex/Trabalho_Trilha_I_AcolheMente_PB.tex` (60 KB)
- VERSION.txt atualizado para v1.0.0
- RELEASE_NOTES.md atualizado com evidência de compilação
- `build_pdf_abntex2.sh` atualizado com fallback `nbconvert --to pdf`
- README.md com badges de versão v1.0.0

### Verificação final
- Ruff: All checks passed
- Pytest: 80 passed, 0 failed
- Coverage: 88%
- Notebook: executa do início ao fim
- Caminhos locais: 0 (grep -R retorna vazio)

## [v0.3.0-rc1] — 2026-05-26

### Adicionado
- **ADR-011:** Congelamento do motor lógico de 7 variáveis para entrega da Trilha I
- **test_no_cross_tier_merge.py:** 9 testes de proveniência explícita
- **test_eda_and_export_smoke.py:** 8 smoke tests para EDA e exportação PNG
- **test_legitimate_educational_text_allowed:** Valida que texto acadêmico não é bloqueado
- **scripts/install_tex_colab.sh:** Script de instalação TeX para Google Colab
- **RELEASE_NOTES.md:** Notas de release v0.3.0-rc1
- **VERSION.txt:** Arquivo de versão (v0.3.0-rc1)
- **pyproject.toml:** Configuração ruff (line-length=100, E741 ignorado)
- TIER_B adicionado ao grafo de governança como entidade explícita

### Alterado
- **graph_schema.py:** `validate_no_student_nodes()` migrado para word-boundary regex
  - Verifica apenas NOMES de entidades, não descrições
  - Texto educacional legítimo não é mais bloqueado
- **eda_plots.py:** Removida variável `bars` não utilizada
- **rule_graph.py:** Adicionado `noqa: E741` para variável `I`
- Ruff: 12 fixes automáticos + 4 manuais → All checks passed
- Coverage: 55% → 88%
- Testes: 72 → 80

### Corrigido
- Imports não utilizados em 6 arquivos de teste
- Variável `kg` não utilizada em test_graph_generation_is_deterministic.py

## [v0.3.0] — 2026-05-26

### Adicionado
- **Variáveis contextuais C e I** — ampliação controlada de 5 para 7 variáveis
- **Regras R5 e R6** — E∧B∧C→A e V∧I→A
- **Encaminhamentos no grafo** — Revisão Humana, Sem Ranking, PSE/UBS/CAPS
- **Notebook final** — 26 células, executa do início ao fim
- **Pipeline abnTeX2** — build_pdf_abntex2.sh + referencias.bib
- README.md, SDD.md, MODEL_CARD.md, DATA_PROVENANCE_MATRIX.md, CHANGELOG.md

### Alterado
- `rule_graph.py` reescrito para 7 variáveis e 6 regras
- Grafo de regras: 38 entidades, 42 relações
- Grafo de governança: 18→19 entidades (com TIER_B), 20 relações

### Corrigido
- Falso positivo "aluno" na descrição de I (→ "corpo discente")
- Falso positivo "estudante" na descrição de "Sem Ranking"
- Falso positivo "ana" em "Revisão Humana" (word boundary regex)

## [v0.2.0] — 2026-05-26

### Adicionado
- ADR-009: Grafo Determinístico de Conhecimento para Explicabilidade
- `graph_schema.py` — Entity, Relationship, KnowledgeGraph com guardrails
- `rule_graph.py` — 5 variáveis, 4 regras, 3 builders de grafos
- `eda_plots.py` — 4 funções de EDA governada por tiers
- 5 suítes de teste (47 testes totais)

## [v0.1.0] — 2026-05-26

### Adicionado
- Plano de implementação inicial com arquitetura de tiers
- Deliberação sobre dataset externo (`mental_health_analysis.csv`)
- Política de merge entre tiers (TIER_A × TIER_C: Bloqueio Absoluto)
