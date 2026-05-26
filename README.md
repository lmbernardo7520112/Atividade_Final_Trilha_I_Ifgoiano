# AcolheMente Escolar PB

> Motor de Inferência Lógico para Acolhimento em Saúde Mental Escolar — Paraíba

[![CI](https://img.shields.io/badge/tests-80%20passed-brightgreen)]()
[![Coverage](https://img.shields.io/badge/coverage-88%25-brightgreen)]()
[![Ruff](https://img.shields.io/badge/lint-ruff%20passed-brightgreen)]()
[![Variables](https://img.shields.io/badge/propositional%20variables-7-blue)]()
[![Rules](https://img.shields.io/badge/logical%20rules-6-orange)]()
[![Version](https://img.shields.io/badge/version-v1.0.0-brightgreen)]()

## Visão Geral

Sistema Baseado em Conhecimento que utiliza **Lógica Proposicional com Inferência por
Resolução** para identificar cenários de acolhimento prioritário em saúde mental escolar.

**Técnica central:** Lógica proposicional determinística — não utiliza machine learning,
deep learning, IA generativa ou qualquer API externa.

**Domínio:** Saúde mental escolar no contexto da PeNSE 2024 (IBGE) com foco na Paraíba.

**Motor congelado:** ADR-011 declara 7 variáveis e 6 regras como teto de complexidade.

## Variáveis Proposicionais (7 = 5 nucleares + 2 contextuais)

### 5 Nucleares
| Var | Semântica | Fontes PeNSE |
|-----|-----------|-------------|
| **E** | Sofrimento emocional recorrente | B12004, B12005, B12007 |
| **B** | Baixo apoio socioafetivo percebido | B12003, B07004 |
| **V** | Indicador crítico de desvalor da vida | B12008 |
| **S** | Sinal autorreferido de autoagressão | B12009 |
| **A** | Acolhimento humano prioritário | Saída do motor |

### 2 Contextuais de Modulação
| Var | Semântica | Fontes |
|-----|-----------|--------|
| **C** | Contexto comportamental agravante | B03010C, B03006B |
| **I** | Insuficiência institucional de resposta | E01P60, E01P117 |

## Regras Lógicas (CNF)

| Regra | Natural | CNF |
|-------|---------|-----|
| R1 | S → A | ¬S ∨ A |
| R2 | V ∧ E → A | ¬V ∨ ¬E ∨ A |
| R3 | E ∧ B → A | ¬E ∨ ¬B ∨ A |
| R4 | V ∧ B → A | ¬V ∨ ¬B ∨ A |
| R5 | E ∧ B ∧ C → A | ¬E ∨ ¬B ∨ ¬C ∨ A |
| R6 | V ∧ I → A | ¬V ∨ ¬I ∨ A |

> **Nota:** C e I são variáveis contextuais de modulação.
> Nenhuma delas infere A isoladamente. C requer E∧B; I requer V.

## Governança de Dados

| Tier | Fonte | Uso |
|------|-------|-----|
| TIER_A | PeNSE 2024 (IBGE) | Inferência para Brasil/NE/PB |
| TIER_B | Escola sintética | Demonstração operacional |
| TIER_C | Dataset externo | Benchmark metodológico (sem inferência BR) |

**Merge entre tiers distintos: PROIBIDO.**

## Proibições Absolutas

- ❌ Linguagem diagnóstica (depressão, TDAH, autismo, TOC, transtorno)
- ❌ Ranking de estudantes
- ❌ Classificação de aluno individual real
- ❌ Dados identificáveis (nome, CPF, matrícula)
- ❌ Dependência de API externa (Gemini, OpenAI)
- ❌ Inferência regional a partir do dataset externo

## Estrutura do Projeto

```
├── docs/                           # ADRs e documentação de governança
│   ├── ADR-009-deterministic-knowledge-graph-for-explainability.md
│   ├── ADR-011-freeze-seven-variable-logic-core.md
│   ├── SDD.md
│   ├── MODEL_CARD.md
│   └── DATA_PROVENANCE_MATRIX.md
├── implementation_plans/           # Plano de implementação v3
├── notebooks/                      # Notebook final
│   └── Trabalho_Trilha_I_AcolheMente_PB.ipynb
├── reports/
│   ├── figures/                    # Grafos de explicabilidade
│   ├── tex/                        # LaTeX gerado
│   └── pdf/                        # PDF abnTeX2
├── scripts/
│   ├── build_pdf_abntex2.sh        # Compilação PDF
│   └── install_tex_colab.sh        # Instalação TeX no Colab
├── src/acolhemente/                # Módulos Python
│   ├── graph_schema.py
│   ├── rule_graph.py
│   └── eda_plots.py
├── templates/abntex2/              # Template LaTeX + referências
│   └── referencias.bib
├── tests/                          # 80 testes automatizados (7 suítes)
│   ├── test_propositional_variable_budget.py     (25)
│   ├── test_no_genai_dependency_in_core_notebook.py (13)
│   ├── test_graph_generation_is_deterministic.py  (9)
│   ├── test_no_cross_tier_merge.py               (9)
│   ├── test_rule_graph_no_diagnostic_labels.py   (9)
│   ├── test_eda_and_export_smoke.py              (8)
│   └── test_rule_graph_no_student_nodes.py       (7)
├── CHANGELOG.md
├── RELEASE_NOTES.md
├── VERSION.txt
└── pyproject.toml
```

## Como Executar

### Testes e CI
```bash
# Criar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependências
pip install pytest pytest-cov ruff networkx matplotlib

# Lint
ruff check .

# Testes
python -m pytest tests/ -v

# Coverage
python -m pytest tests/ --cov=src/acolhemente --cov-report=term-missing
```

### Notebook
```bash
pip install jupyter nbconvert ipykernel
jupyter nbconvert --execute --to notebook notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb
```

### Grafos
```bash
python -c "
from src.acolhemente.rule_graph import build_rule_graph, export_graph_png
kg = build_rule_graph()
export_graph_png(kg, 'reports/figures/grafo_regras_7vars.png')
"
```

### PDF abnTeX2

**Opção 1 — Local (requer texlive):**
```bash
sudo apt install texlive-full
bash scripts/build_pdf_abntex2.sh
```

**Opção 2 — Google Colab:**
```python
!bash scripts/install_tex_colab.sh
!bash scripts/build_pdf_abntex2.sh
```

## Compliance

| Framework | Status |
|-----------|--------|
| LGPD | ✅ Sem dados identificáveis |
| ECA | ✅ Sem classificação de menor |
| PSE | ✅ Integrado como guardrail |
| Human-in-the-Loop | ✅ Obrigatório em toda decisão |

## Referências

- Russell, S.; Norvig, P. *Inteligência Artificial: uma abordagem moderna*. 4ª ed. GEN LTC, 2022.
- PeNSE 2024 — Pesquisa Nacional de Saúde do Escolar. IBGE, 2024.
- Brasil. Lei nº 13.709/2018 (LGPD).
- Brasil. Lei nº 8.069/1990 (ECA).
