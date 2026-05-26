# Plano de Implementação Revisado (v3): AcolheMente Escolar PB

## Revisão v3 — 2026-05-26
Ampliação controlada de 5 para 7 variáveis proposicionais (5 nucleares + 2 contextuais),
incorporação de C (contexto comportamental) e I (insuficiência institucional),
adição de R5 e R6, e atualização de todos os artefatos de governança.

---

## 0. Decisão Central Obrigatória

**Técnica central:** Lógica Proposicional aplicada a Sistema Baseado em Conhecimento
com Inferência por Resolução (CNF + prova por contradição).

**O grafo de conhecimento** é apenas camada de explicabilidade e visualização.
Nunca substitui o motor lógico, nunca depende de IA generativa, nunca classifica estudantes.

---

## 1. Deliberação sobre Ampliação Controlada de 5 para 7 Variáveis Proposicionais

### Motivação
A versão-base com 5 variáveis (E, B, V, S, A) preservava máxima parcimônia e
alinhamento direto com o notebook exemplar da Trilha I (`Resposta_Trabalho_Trilha_I.ipynb`).
A evolução para 7 variáveis foi adotada de forma cautelosa para incorporar dois elementos
essenciais no contexto escolar:

1. **Contexto comportamental (C):** Fatores como tempo de tela, sedentarismo e qualidade
   de sono modulam a gravidade dos indicadores nucleares, permitindo ação preventiva sem
   diagnóstico.
2. **Capacidade institucional (I):** A presença ou ausência de apoio psicológico, fluxo
   PSE ativo e protocolos de acolhimento na escola desloca a análise do aluno individual
   para a responsabilidade organizacional da instituição.

### Riscos Identificados
| Risco | Controle |
|-------|----------|
| Complexidade excessiva para avaliador Trilha I | C e I são apresentadas como extensão natural, não como ruptura |
| C ser confundida com variável diagnóstica | Descrição explícita: "contextual, não isolada, não diagnóstica" |
| I ser confundida com atributo do aluno | Descrição explícita: "atributo da escola e não do corpo discente" |
| C ou I inferirem A isoladamente | Nenhuma regra permite C→A ou I→A; R5 exige E∧B∧C; R6 exige V∧I |
| Perda de explicabilidade | Grafo determinístico atualizado mostra todas as 7 variáveis e 6 regras |

### Controles Implementados
- C e I são classificadas como "contextuais de modulação", separadas das 5 nucleares
- Nenhuma regra permite C ou I inferirem A isoladamente (testes CI)
- Descrições contêm disclaimers explícitos de não-diagnóstico
- Budget test atualizado para 7 variáveis (com assert de 5+2)
- Grafo de explicabilidade atualizado com visualização das novas variáveis

### Justificativa de Preservação da Simplicidade
As 2 variáveis contextuais seguem o mesmo padrão formal das 5 nucleares (mesma classe
Entity, mesmo pipeline CNF, mesmo motor de resolução). A adição de 2 regras (R5, R6)
não altera a arquitetura do motor — apenas amplia a base de conhecimento. O notebook
permanece compreensível para avaliador da Trilha I, com seção explícita justificando
a evolução de 5 para 7.

---

## 2. Deliberação sobre o Novo Dataset (`mental_health_analysis.csv`)
**Decisão:** O dataset NÃO substitui os dados oficiais da PeNSE 2024, NÃO deve ser
misturado linha a linha com a PeNSE, NÃO será usado para calibrar o risco de adolescentes
brasileiros e NÃO sustentará conclusões sobre o contexto escolar brasileiro.
**Uso Permitido:** TIER_C_EXTERNAL_EXPLORATORY — benchmark metodológico apenas.

## 3. Matriz de Proveniência (Tiers Arquiteturais)

| Tier | Fonte | Papel |
|------|-------|-------|
| **TIER_A_OFFICIAL_BR** | PeNSE 2024 (IBGE) | Única fonte inferencial para Brasil/NE/PB |
| **TIER_B_SYNTHETIC_SCHOOL** | Dados escolares fictícios | Demonstração operacional |
| **TIER_C_EXTERNAL_EXPLORATORY** | `mental_health_analysis.csv` | Benchmark metodológico |

### Política de Merge
| Operação | Regra |
|----------|-------|
| TIER_A × TIER_A | ✅ Permitido |
| TIER_B × TIER_B | ✅ Permitido |
| TIER_C × TIER_C | ✅ Permitido |
| TIER_A × TIER_B | ❌ Proibido |
| **TIER_A × TIER_C** | **❌ Bloqueio Absoluto** |
| TIER_B × TIER_C | ❌ Proibido |

## 4. Variáveis Proposicionais Aprovadas (Orçamento: 7 = 5 nucleares + 2 contextuais)

### 5 Variáveis Nucleares

| Var | Semântica | Fonte PeNSE | Papel |
|-----|-----------|-------------|-------|
| **E** | Sofrimento emocional recorrente | B12004, B12005, B12007 | Consolida preocupação, tristeza ou irritabilidade |
| **B** | Baixo apoio socioafetivo percebido | B12003, B07004 | Fragilidade de apoio social/familiar |
| **V** | Indicador crítico de desvalor da vida | B12008 | Sinal sensível de desesperança |
| **S** | Sinal autorreferido de autoagressão | B12009 | Aciona protocolo humano obrigatório |
| **A** | Acolhimento humano prioritário | Saída do motor | Conclusão operacional, não clínica |

### 2 Variáveis Contextuais de Modulação

| Var | Semântica | Fontes | Papel |
|-----|-----------|--------|-------|
| **C** | Contexto comportamental agravante | PeNSE: B03010C, B03006B; externo: Screen_Time_Hours etc. (benchmark) | Modula gravidade; não isolada; não diagnóstica |
| **I** | Insuficiência institucional de resposta | PeNSE: E01P60, E01P117; escola sintética | Atributo da escola, não do discente |

## 5. Regras Lógicas Aprovadas (6 regras)

### Forma natural:
- **R1:** S → A
- **R2:** V ∧ E → A
- **R3:** E ∧ B → A
- **R4:** V ∧ B → A
- **R5:** E ∧ B ∧ C → A *(contextual: C modula, não infere isoladamente)*
- **R6:** V ∧ I → A *(contextual: I é institucional, não do discente)*

### CNF obrigatória:
- **R1:** ¬S ∨ A
- **R2:** ¬V ∨ ¬E ∨ A
- **R3:** ¬E ∨ ¬B ∨ A
- **R4:** ¬V ∨ ¬B ∨ A
- **R5:** ¬E ∨ ¬B ∨ ¬C ∨ A
- **R6:** ¬V ∨ ¬I ∨ A

## 6. Proibições Absolutas

| Categoria | Proibição |
|-----------|-----------|
| **Linguagem** | Não criar variável "depressão", "TDAH", "autismo", "TOC", "transtorno" |
| **Classificação** | Não criar ranking; não classificar aluno individual real |
| **Dados pessoais** | Não usar nomes, matrículas, CPF, telefone, e-mail |
| **Inferência** | Não usar dataset externo para conclusão sobre Brasil/NE/PB |
| **Merge** | Não fazer merge entre tiers distintos |
| **API** | Não depender de Gemini, OpenAI ou API externa no notebook final |
| **Isolamento C/I** | C nunca infere A sozinha; I nunca infere A sozinha |

## 7. Uso do knowledge_graph_generation.ipynb como Camada Determinística

### Matriz de Aproveitamento
| Camada | Status |
|--------|--------|
| EDA estatística PeNSE (PB vs NE vs BR) | ✅ Aprovado |
| EDA exploratória dataset externo (TIER_C com disclaimers) | ✅ Aprovado |
| KG explicável: variáveis → proposições → regras → acolhimento | ✅ Aprovado |
| KG governança: fontes → tiers → crosswalks | ✅ Aprovado |
| Visualização networkx + matplotlib | ✅ Aprovado |
| ⛔ Grafo de alunos | ❌ Bloqueado |
| ⛔ Grafo de diagnóstico | ❌ Bloqueado |
| ⛔ Grafo extraído por LLM | ❌ Bloqueado |

## 8. Arquitetura de Módulos (`src/acolhemente/`)

| Módulo | Responsabilidade |
|--------|-----------------|
| `__init__.py` | Package init |
| `provenance.py` | Enums de Tiers |
| `external_loader.py` | Carga isolada TIER_C |
| `semantic_crosswalk.py` | Compatibilidade semântica TIER_A ↔ TIER_C |
| `graph_schema.py` | Entity, Relationship, KnowledgeGraph + guardrails |
| `rule_graph.py` | 7 variáveis, 6 regras, 3 builders, export PNG |
| `eda_plots.py` | EDA governada por tiers |

## 9. ADRs

| ADR | Descrição |
|-----|-----------|
| ADR-005 | Data Provenance Separation |
| ADR-006 | No Cross-Dataset Inferential Mixing |
| ADR-007 | External Dataset as Benchmark Only |
| ADR-008 | Sensitive Alert Human Protocol |
| ADR-009 | Deterministic Knowledge Graph for Explainability |

## 10. Testes Automatizados (CI Gates) — 62 testes

| Teste | Critérios |
|-------|-----------|
| `test_propositional_variable_budget.py` | 7 vars (5+2), C contextual, I institucional, C/I não isoladas, 6 regras |
| `test_rule_graph_no_student_nodes.py` | Sem nós de aluno, sem identificadores pessoais |
| `test_rule_graph_no_diagnostic_labels.py` | Sem rótulos diagnósticos, regras explicáveis |
| `test_graph_generation_is_deterministic.py` | Grafo reproduzível, R1-R6, CNFs, guardrails |
| `test_no_genai_dependency_in_core_notebook.py` | Zero imports de google.genai/openai/anthropic |

## 11. Estrutura do Notebook Final

```
1. Apresentação do aluno e contexto
2. Introdução e definição do problema
3. Metodologia e escolha da técnica de IA
   3.1 Lógica proposicional
   3.2 Inferência por resolução
   3.3 Justificativa de não usar diagnóstico automatizado
   3.4 Por que avançar de 5 para 7 variáveis?
4. Implementação da solução
   4.1 Carregamento e governança dos dados
   4.2 EDA governada PeNSE (TIER_A)
   4.3 EDA exploratória dataset externo (TIER_C, com disclaimers)
   4.4 Formalização das 7 variáveis proposicionais (5 nucleares + 2 contextuais)
   4.5 Base de conhecimento e regras em CNF (R1–R6)
   4.6 Inferência por resolução
   4.7 Grafo determinístico de explicabilidade
   4.8 Cenários sintéticos de validação (TIER_B)
5. Resultados e comparações
   5.1 Baseline manual
   5.2 Motor lógico
   5.3 Rastreabilidade por grafo
6. Perspectiva de evolução com deep learning
   6.1 Apenas teórica
   6.2 Com governança, LGPD, ECA, PSE e human-in-the-loop
7. Conclusões
8. Referências
```

## 12. Plano de Commits (Conventional Commits)

1. `docs: deliberate controlled expansion to seven propositional variables`
2. `feat(logic): add contextual variables C and I to rule base`
3. `feat(graph): update explainability graph for seven-variable model`
4. `test: enforce seven-variable budget and contextual guardrails`
5. `notebook: document seven-variable logic in final Trilha I narrative`
6. `docs: update governance artifacts for contextual variables`

## 13. Critérios de Aceite (v3)

- [ ] Exatamente 7 variáveis proposicionais (5 nucleares + 2 contextuais)
- [ ] Máximo de 6 regras lógicas (R1–R6)
- [ ] A é a única conclusão operacional
- [ ] C e I não inferem A isoladamente
- [ ] Motor lógico por regras explícitas em CNF
- [ ] Grafo determinístico sem API externa
- [ ] EDA PeNSE separada da EDA externa
- [ ] Nenhuma mistura inferencial de tiers
- [ ] Nenhuma linguagem diagnóstica
- [ ] Nenhum ranking de aluno
- [ ] Nenhum dado identificável
- [ ] Dataset externo apenas como benchmark
- [ ] Notebook executa do início ao fim
- [ ] PDF abnTeX2 compila
- [ ] CI verde (62+ testes passando)
