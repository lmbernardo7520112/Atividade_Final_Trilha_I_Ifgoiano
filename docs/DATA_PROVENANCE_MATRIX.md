# DATA_PROVENANCE_MATRIX.md — Matriz de Proveniência de Dados

## Tiers de Proveniência

| Tier | Fonte | Papel | Merge Permitido |
|------|-------|-------|----------------|
| **TIER_A_OFFICIAL_BR** | PeNSE 2024 (IBGE) | Única fonte inferencial para Brasil/NE/PB | Apenas intra-tier |
| **TIER_B_SYNTHETIC_SCHOOL** | Dados escolares fictícios | Demonstração operacional | Apenas intra-tier |
| **TIER_C_EXTERNAL_EXPLORATORY** | `mental_health_analysis.csv` (Kaggle) | Benchmark metodológico | Apenas intra-tier |

## Variáveis PeNSE Utilizadas (TIER_A)

### Nucleares
| Código | Tema | Variável Proposicional | Descrição |
|--------|------|----------------------|-----------|
| B12004 | Saúde Mental | E | Frequência de preocupação excessiva |
| B12005 | Saúde Mental | E | Frequência de tristeza |
| B12007 | Saúde Mental | E | Frequência de irritabilidade |
| B12003 | Saúde Mental | B | Percepção de apoio familiar |
| B07004 | Convivência | B | Percepção de apoio escolar |
| B12008 | Saúde Mental | V | Pensamento de que a vida não vale a pena |
| B12009 | Saúde Mental | S | Autoagressão autorreferida |

### Contextuais
| Código | Tema | Variável Proposicional | Descrição |
|--------|------|----------------------|-----------|
| B03010C | Alimentação/Comportamento | C | Tempo de tela em dias de semana |
| B03006B | Atividade Física | C | Prática de atividade física |
| E01P60 | Escola | I | Escola oferece apoio psicológico |
| E01P117 | Escola | I | Escola possui fluxo PSE ativo |

## Variáveis do Dataset Externo (TIER_C)

| Variável | Crosswalk PeNSE | Uso Permitido |
|----------|----------------|---------------|
| Support_System | B12003, B07004 | Benchmark apenas |
| Screen_Time_Hours | B03010C | Benchmark apenas |
| Exercise_Hours | B03006B | Benchmark apenas |
| Social_Media_Hours | — | Benchmark apenas |
| Sleep_Hours | — | Benchmark apenas |
| Survey_Stress_Score | B12004 | Benchmark apenas |
| Wearable_Stress_Score | — | Benchmark apenas |

## Bloqueios de Merge

| Operação | Status | Justificativa |
|----------|--------|---------------|
| TIER_A × TIER_A | ✅ Permitido | Dados oficiais da mesma fonte |
| TIER_B × TIER_B | ✅ Permitido | Dados sintéticos da mesma origem |
| TIER_C × TIER_C | ✅ Permitido | Dados exploratórios da mesma fonte |
| TIER_A × TIER_B | ❌ Proibido | Contaminação de inferência oficial |
| **TIER_A × TIER_C** | **❌ Bloqueio Absoluto** | Calibragem indevida de risco BR |
| TIER_B × TIER_C | ❌ Proibido | Contaminação da simulação operacional |

## Compliance

- **LGPD:** Nenhum dado identificável processado
- **ECA:** Nenhuma classificação de menor individual
- **PSE:** Integrado como guardrail e encaminhamento
- **Human-in-the-Loop:** Obrigatório antes de qualquer ação
