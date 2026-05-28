# v3.3 Code Traceability Preparation Report

> **Data:** 2026-05-28
> **Versão base:** academic_abntex2_attempt_v3_3 (v3.3.2)

## 1. Objetivo

Adicionar ao documento de preparação para banca um mapa de rastreabilidade texto ↔ código, permitindo que o autor conecte cada afirmação acadêmica a arquivos, funções, testes e evidências concretas do repositório.

## 2. Arquivos inspecionados

| Arquivo | Linhas | Conteúdo verificado |
|---------|--------|---------------------|
| `appendices/simbolos_acolhemente.py` | 40 | Definição de 7 variáveis com tipo e fontes PeNSE |
| `appendices/regras_acolhemente.py` | 54 | 6 regras implicativas + CNF + antecedentes |
| `appendices/motor_resolucao_acolhemente.py` | 102 | Motor pedagógico: `_resolve`, `inferir_por_resolucao`, `inferir_acolhimento`, `explicar_decisao` |
| `appendices/cenarios_sinteticos_acolhemente.py` | ~60 | 14 cenários representativos com resultado esperado |
| `appendices/grafo_explicabilidade_acolhemente.py` | — | Gerador de `grafo_regras_7vars.png` |
| `appendices/grafo_pseudonimizacao_acolhimento.py` | — | Gerador de `fluxo_pseudonimizacao_acolhimento.png` |
| `appendices/grafos_governanca_proveniencia.py` | — | Gerador de 5 figuras: proveniência, governança, cenários, baseline |
| `src/acolhemente/motor.py` | 147 | Motor modular: mesma assinatura `inferir_acolhimento()` |
| `src/acolhemente/rule_graph.py` | — | Grafo de regras modular |
| `src/acolhemente/eda_plots.py` | — | EDA com `plot_pense_pb_vs_ne_br()` |
| `_build/tabela_variaveis.tex` | — | A marcada como "Saída inferida" |
| `_build/tabela_regras.tex` | — | R1–R6 em forma implicativa e CNF |
| `_build/tabela_cenarios.tex` | — | 10 cenários com guardrails C e I |
| `tests/test_motor_equivalence_contract.py` | — | Equivalência acadêmico/modular |
| `outputs/validacao_exaustiva_64.csv` | 65 | 64 linhas, oráculo, 0 falhas |
| `notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb` | — | Todos os termos obrigatórios presentes |

## 3. Seções adicionadas

| # | Seção | Conteúdo |
|---|-------|----------|
| 18 | Mapa de Rastreabilidade Texto ↔ Código | Inventário + 15 itens mapeados |
| 19 | Guia rápido: onde apontar no código | 10 perguntas → arquivo → função → mensagem |
| 20 | Trechos de código essenciais comentados | 6 blocos: motor, regras, oráculo, validação, CSV, teste |
| 21 | Mapa de evidência para 10 minutos | 10 blocos cronometrados com evidência textual e de código |
| 22 | Checklist de domínio técnico | 15 itens verificáveis sobre código |

## 4. Itens mapeados na matriz

15 itens: SBC, variáveis, R1–R6, CNF, motor pedagógico, motor modular, validação 64, oráculo, R5 subsumida, guardrails, baseline, PeNSE, pseudonimização, grafos, testes.

## 5. Comandos executados

- `find . -maxdepth 3 -type f | sort` — inventário completo
- `ls appendices/ scripts/ tests/ notebooks/ outputs/ figures/ _build/`
- `ls src/acolhemente/` — motor modular confirmado
- `view_file` em 4 arquivos Python completos
- `head` em 3 arquivos adicionais
- `python -m pytest tests/ -q` → 136 passed, 1 skipped

## 6. Evidências verificadas

| Evidência | Resultado |
|-----------|-----------|
| Motor pedagógico existe e tem `inferir_acolhimento()` (L49) | ✅ |
| Motor modular existe e tem `inferir_acolhimento()` (L77) | ✅ |
| Mesma assinatura em ambos os motores | ✅ |
| `REGRAS_CNF` idêntica em ambos (6 frozensets) | ✅ |
| CSV com 64 linhas, colunas A_motor/A_esperado/ok | ✅ |
| Notebook com oráculo e nota metodológica | ✅ |
| 8 figuras em `figures/` | ✅ |
| 3 tabelas LaTeX em `_build/` | ✅ |
| 8 módulos de teste em `tests/` | ✅ |
| 136 passed, 1 skipped, 0 failed | ✅ |

## 7. Limitações

- O campo `tipo` de A em `simbolos_acolhemente.py` (L26) ainda diz `"nuclear"` (legado). A tabela LaTeX (`_build/tabela_variaveis.tex`) já está correta ("Saída inferida"). Essa divergência foi documentada no Item 2 do mapa.
- Não há pipeline Markdown→DOCX no projeto. Documento disponível apenas em Markdown.
- Não há pipeline Markdown→PDF separado. O PDF acadêmico é compilado via LaTeX.

## 8. Veredito

> O documento de preparação para banca agora permite defender o trabalho conectando cada afirmação acadêmica a código, testes e outputs verificáveis. 15 itens mapeados, 10 perguntas respondidas com localização exata no código, 6 trechos comentados para estudo, e 15 itens de checklist técnico.
