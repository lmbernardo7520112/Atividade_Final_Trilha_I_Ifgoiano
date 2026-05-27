# 🧠 AcolheMente Escolar PB 📊

**Motor de Inferência Lógico para Acolhimento em Saúde Mental Escolar — Paraíba.**

<div align="center">

<!-- Badges -->
[![CI](https://img.shields.io/badge/tests-107%20passed-brightgreen)]()
[![Coverage](https://img.shields.io/badge/coverage-88%25-brightgreen)]()
[![Ruff](https://img.shields.io/badge/lint-ruff%20passed-brightgreen)]()
[![Variables](https://img.shields.io/badge/propositional%20variables-7-blue)]()
[![Rules](https://img.shields.io/badge/logical%20rules-6-orange)]()
[![Version](https://img.shields.io/badge/version-v1.0.0-brightgreen)]()

*Desenvolvido por: Leonardo Maximino Bernardo*

</div>

<!-- Accordion Navigation -->
<details open>
<summary>📜 Tabela de Conteúdos</summary>
<ol>
  <li><a href="#-sobre-o-projeto">Sobre o Projeto</a></li>
  <li><a href="#-variáveis-proposicionais">Variáveis Proposicionais (7 Variáveis)</a></li>
  <li><a href="#-regras-lógicas">Regras Lógicas (CNF)</a></li>
  <li><a href="#-governança-de-dados">Governança de Dados & Proibições</a></li>
  <li><a href="#-estrutura-do-projeto">Estrutura do Projeto</a></li>
  <li><a href="#-como-executar">Como Executar</a></li>
  <li><a href="#-compliance-e-referências">Compliance e Referências</a></li>
</ol>
</details>

---

## 📖 Sobre o Projeto

O **AcolheMente Escolar PB** é um Sistema Baseado em Conhecimento (SBC) que utiliza **Lógica Proposicional com Inferência por Resolução** para identificar cenários de acolhimento prioritário em saúde mental escolar.

Diferente de abordagens baseadas em Machine Learning ou IA Generativa (como LLMs), este projeto foca em **explicabilidade e determinismo absoluto**:
* **Técnica central:** Lógica proposicional determinística. Não há "caixas pretas", predições probabilísticas ou dependência de APIs externas (como OpenAI ou Gemini).
* **Domínio:** Saúde mental escolar, ancorado nos dados da **PeNSE 2024 (IBGE)**, com foco específico no estado da **Paraíba**.
* **Complexidade Controlada:** O motor lógico foi intencionalmente "congelado" (conforme ADR-011) em exatas **7 variáveis proposicionais** e **6 regras lógicas** para garantir máxima governança e interpretabilidade humana.

---

## 🧮 Variáveis Proposicionais

O modelo opera com 7 variáveis, divididas entre **5 variáveis nucleares** (que definem o estado do estudante) e **2 variáveis contextuais** (que modulam a resposta da escola).

### 5 Nucleares
| Var | Semântica | Fontes PeNSE |
|:---:|-----------|-------------|
| **E** | Sofrimento emocional recorrente | B12004, B12005, B12007 |
| **B** | Baixo apoio socioafetivo percebido | B12003, B07004 |
| **V** | Indicador crítico de desvalor da vida | B12008 |
| **S** | Sinal autorreferido de autoagressão | B12009 |
| **A** | Acolhimento humano prioritário | *Saída do motor* |

### 2 Contextuais de Modulação
| Var | Semântica | Fontes PeNSE |
|:---:|-----------|-------------|
| **C** | Contexto comportamental agravante | B03010C, B03006B |
| **I** | Insuficiência institucional de resposta | E01P60, E01P117 |

> **Nota:** `C` e `I` são variáveis contextuais de modulação e **nunca** inferem `A` isoladamente. `C` requer a presença de `E ∧ B`; `I` requer a presença de `V`.

---

## ⚖️ Regras Lógicas

A inferência é feita convertendo o conhecimento humano em Forma Normal Conjuntiva (CNF):

| Regra | Natural | CNF |
|:-----:|---------|-----|
| **R1** | S → A | ¬S ∨ A |
| **R2** | V ∧ E → A | ¬V ∨ ¬E ∨ A |
| **R3** | E ∧ B → A | ¬E ∨ ¬B ∨ A |
| **R4** | V ∧ B → A | ¬V ∨ ¬B ∨ A |
| **R5** | E ∧ B ∧ C → A | ¬E ∨ ¬B ∨ ¬C ∨ A |
| **R6** | V ∧ I → A | ¬V ∨ ¬I ∨ A |

---

## 🛡️ Governança de Dados

Para garantir a segurança, ética e eficácia do projeto, estabelecemos uma arquitetura rigorosa de proveniência de dados dividida em 3 camadas:

| Tier | Fonte | Finalidade |
|------|-------|------------|
| **TIER_A** | PeNSE 2024 (IBGE) | Inferência oficial para Brasil/NE/PB |
| **TIER_B** | Escola sintética | Demonstração operacional e validação |
| **TIER_C** | Dataset externo | Benchmark metodológico (sem inferência BR) |

⚠️ **Merge entre tiers distintos é estritamente PROIBIDO.**

### 🛑 Proibições Absolutas no Motor
- ❌ Linguagem diagnóstica clínica (depressão, TDAH, autismo, TOC, transtorno).
- ❌ Ranking ou escore comparativo de estudantes.
- ❌ Classificação de qualquer aluno individual real.
- ❌ Presença de dados identificáveis (nome, CPF, matrícula).
- ❌ Dependência de APIs de IA Generativa.
- ❌ Inferência regional a partir do dataset externo (TIER_C).

---

## 📂 Estrutura do Projeto

```text
├── docs/                           # ADRs e documentação de governança
├── implementation_plans/           # Planos de arquitetura e implementação
├── notebooks/                      # Notebook Jupyter final da entrega
├── reports/
│   ├── figures/                    # Grafos de explicabilidade determinística
│   ├── pdf/                        # PDF final gerado (abnTeX2/xelatex)
│   └── tex/                        # LaTeX gerado
├── scripts/                        # Scripts de compilação de PDF
├── src/acolhemente/                # Módulos Python (Motor, Grafos, EDA)
├── templates/abntex2/              # Templates de formatação LaTeX
└── tests/                          # 107 testes automatizados (Pytest)
```

---

## 🚀 Como Executar

### Testes e Validação (CI)
```bash
# Criar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependências
pip install pytest pytest-cov ruff networkx matplotlib

# Validar com Linter (Ruff)
ruff check .

# Executar suíte de testes e cobertura
python -m pytest tests/ --cov=src/acolhemente --cov-report=term-missing
```

### Notebook e Grafos
```bash
# Executar notebook programaticamente
pip install jupyter nbconvert ipykernel
jupyter nbconvert --execute --to notebook notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb

# Exportar grafos de regras manualmente
python -c "from src.acolhemente.rule_graph import build_rule_graph, export_graph_png; export_graph_png(build_rule_graph(), 'reports/figures/grafo_regras.png')"
```

### Compilar PDF Final
```bash
# Pipeline completo: gera .tex, aplica correções, compila com xelatex+bibtex
bash scripts/build_academic_pdf.sh
```

---

## ⚖️ Compliance e Referências

| Framework | Status | Detalhamento |
|-----------|:------:|--------------|
| **LGPD** | ✅ | Total ausência de dados identificáveis no motor. |
| **ECA** | ✅ | Sem classificação ou rotulagem limitante de menores. |
| **PSE** | ✅ | Integrado ao fluxo como guardrail institucional. |
| **HITL** | ✅ | *Human-in-the-Loop* obrigatório em toda decisão final. |

* **Russell, S.; Norvig, P.** *Inteligência Artificial: uma abordagem moderna*. 4ª ed. GEN LTC, 2022.
* **IBGE.** PeNSE 2024 — Pesquisa Nacional de Saúde do Escolar. 2024.
* **Brasil.** Lei nº 13.709/2018 (LGPD).
* **Brasil.** Lei nº 8.069/1990 (ECA).
