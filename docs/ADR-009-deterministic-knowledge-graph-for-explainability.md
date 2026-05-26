# ADR-009: Grafo Determinístico de Conhecimento para Explicabilidade

## Status
**Aprovado** — 2026-05-26

## Contexto
O projeto AcolheMente Escolar PB utiliza Lógica Proposicional com Inferência por Resolução
como técnica central de IA. O notebook `knowledge_graph_generation.ipynb` (Google/Gemini)
demonstra como construir Knowledge Graphs a partir de documentos usando LLMs. O projeto
precisa de uma camada de explicabilidade visual, porém não pode depender de APIs externas
(Gemini, OpenAI) nem gerar diagnósticos automatizados.

## Decisão
O projeto adotará um **grafo determinístico de conhecimento** construído programaticamente
com `networkx` para visualizar as relações entre:
- Variáveis proposicionais (E, B, V, S, A)
- Proposições da base de conhecimento
- Regras lógicas em CNF (R1–R4)
- Ações humanas de acolhimento
- Guardrails éticos e legais (LGPD, ECA, PSE)

### O que o grafo FAZ:
1. Visualiza o fluxo lógico: variáveis → proposições → regras → acolhimento.
2. Permite auditoria visual de cada decisão do motor lógico.
3. Gera diagramas estáticos exportáveis como PNG para inclusão no notebook/PDF.
4. Usa métricas de centralidade e comunidades apenas como recurso visual de EDA.
5. É gerado de forma 100% determinística, sem qualquer aleatoriedade ou dependência externa.

### O que o grafo NÃO faz:
1. **Não classifica estudantes** — nenhum nó do grafo representa um aluno individual.
2. **Não gera diagnóstico** — nenhum rótulo contém termos clínicos proibidos.
3. **Não substitui o motor lógico** — a inferência por resolução é a técnica central.
4. **Não depende de LLM/API externa** — zero chamadas a google.genai, openai ou similares.
5. **Não é usado para inferência epidemiológica** — não produz conclusões populacionais.
6. **Não extrai entidades por IA generativa** — todas as entidades são definidas no código.

## Aproveitamento do knowledge_graph_generation.ipynb

### Aproveitado (padrões de design):
| Elemento | Uso |
|----------|-----|
| Classes Entity, Relationship, KnowledgeGraph | Adaptadas como schema determinístico |
| Construção de grafo dirigido com networkx | Reutilizado integralmente |
| Visualização de nós e arestas com matplotlib | Reutilizado integralmente |
| Centralidade e comunidades | Apenas como recurso visual |
| Exportação de grafo para PNG | Reutilizado integralmente |

### NÃO aproveitado (dependências de LLM):
| Elemento | Motivo da exclusão |
|----------|--------------------|
| Extração automática por LLM | Cria dependência de API externa |
| Chamada obrigatória ao Gemini | Inviabiliza execução offline |
| Análise de documentos por IA generativa | Fora do escopo da técnica central |
| Prompts abertos para inferência sensível | Risco ético inaceitável em saúde mental |

## Consequências
- O notebook final executa do início ao fim sem conexão à internet.
- Toda decisão do motor lógico é rastreável visualmente no grafo.
- A equipe pedagógica pode auditar as regras sem conhecimento técnico.
- Nenhum dado sensível de estudante transita pelo grafo.

## Referências
- ADR-005: Data Provenance Separation
- ADR-006: No Cross-Dataset Inferential Mixing
- ADR-007: External Dataset as Benchmark Only
- ADR-008: Sensitive Alert Human Protocol
- Russell, S.; Norvig, P. Inteligência Artificial: uma abordagem moderna. 4ª ed. GEN LTC, 2022.
