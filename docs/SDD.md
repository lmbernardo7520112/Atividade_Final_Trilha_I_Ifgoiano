# SDD.md — Software Design Document: AcolheMente Escolar PB

## 1. Visão Geral da Arquitetura

```
┌──────────────────────────────────────────────────────────────────┐
│                    NOTEBOOK FINAL (.ipynb)                       │
│  ┌─────────┐  ┌──────────┐  ┌────────────┐  ┌───────────────┐  │
│  │ EDA     │  │ Motor    │  │ Grafo      │  │ Resultados    │  │
│  │ Governada│  │ Lógico   │  │ Explicável │  │ & Comparações │  │
│  │ (Tiers) │  │ (CNF)    │  │ (NetworkX) │  │               │  │
│  └────┬────┘  └────┬─────┘  └─────┬──────┘  └───────────────┘  │
│       │            │               │                             │
│  ┌────▼────────────▼───────────────▼──────────────────────────┐  │
│  │              src/acolhemente/                               │  │
│  │  graph_schema.py │ rule_graph.py │ eda_plots.py            │  │
│  │  provenance.py   │ external_loader.py │ semantic_crosswalk  │  │
│  └────────────────────────────────────────────────────────────┘  │
│       │                                                          │
│  ┌────▼──────────────────────────────────────────────────────┐  │
│  │                    DADOS                                   │  │
│  │  TIER_A: PeNSE 2024   │  TIER_B: Sintéticos  │  TIER_C   │  │
│  └────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
         │                    │                     │
    ┌────▼────┐         ┌────▼────┐           ┌────▼────┐
    │ GUARDRAILS │       │ TESTES  │           │  ADRs   │
    │ LGPD/ECA  │       │ 62 CI   │           │ 005-009 │
    │ PSE/HitL  │       │ gates   │           │         │
    └───────────┘       └─────────┘           └─────────┘
```

## 2. Motor Lógico

### Variáveis Proposicionais (7 = 5N + 2C)
- **Nucleares (5):** E, B, V, S, A
- **Contextuais (2):** C, I
- **Saída:** A (única conclusão operacional)

### Base de Conhecimento (6 regras em CNF)
```
R1_CNF: {¬S, A}
R2_CNF: {¬V, ¬E, A}
R3_CNF: {¬E, ¬B, A}
R4_CNF: {¬V, ¬B, A}
R5_CNF: {¬E, ¬B, ¬C, A}
R6_CNF: {¬V, ¬I, A}
```

### Método de Inferência
Resolução por refutação:
1. Adicionar ¬A (negação da query) à KB
2. Converter tudo para CNF (já está)
3. Aplicar resolução binária repetidamente
4. Se cláusula vazia (⊥) derivada → A é consequência lógica da KB
5. Se saturação sem ⊥ → A não é inferível

## 3. Grafo de Explicabilidade

### Tipos de Entidade
| Tipo | Cor | Exemplo |
|------|-----|---------|
| PROPOSITIONAL_VARIABLE | #4FC3F7 (azul) | E, B, V, S, A, C, I |
| PENSE_SOURCE | #81C784 (verde) | B12004, E01P60 |
| LOGICAL_RULE | #FFB74D (laranja) | R1, R2, ..., R6 |
| CNF_CLAUSE | #FF8A65 (laranja escuro) | R1_CNF, ..., R6_CNF |
| ACTION | #E57373 (vermelho) | Acolhimento Humano |
| GUARDRAIL | #CE93D8 (roxo) | LGPD, ECA, PSE |
| TIER | #90A4AE (cinza) | TIER_A, TIER_B, TIER_C |
| EXTERNAL_VARIABLE | #A5D6A7 (verde claro) | Screen_Time_Hours |

### Tipos de Relação
| Tipo | Significado |
|------|-------------|
| FEEDS_INTO | Fonte PeNSE → Variável proposicional |
| IMPLIES | Antecedente → Regra lógica |
| CONVERTS_TO | Regra → Cláusula CNF |
| TRIGGERS | Regra → Ação de acolhimento |
| GOVERNED_BY | Ação → Guardrail ético/legal |
| BENCHMARKS_AGAINST | TIER_A ↔ TIER_C (crosswalk semântico) |
| BELONGS_TO_TIER | Fonte → Tier de proveniência |

## 4. Camada de Testes (CI Gates)

62 testes organizados em 5 suítes:
1. **Budget (27 testes):** 7 variáveis, 5+2 split, C/I contextual, isolamento
2. **Student nodes (6 testes):** Nenhum nó com dados pessoais
3. **Diagnostic labels (10 testes):** Nenhum rótulo clínico
4. **Determinism (9 testes):** Reprodutibilidade do grafo
5. **GenAI dependency (10 testes):** Zero imports de LLM/API

## 5. Decisões Arquiteturais (ADRs)

| ADR | Decisão |
|-----|---------|
| 005 | Separação de proveniência por tiers |
| 006 | Proibição de mistura inferencial entre tiers |
| 007 | Dataset externo como benchmark apenas |
| 008 | Protocolo humano para alertas sensíveis |
| 009 | Grafo determinístico sem dependência de LLM |
