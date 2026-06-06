# v3_3 Lineage and Artifact Map

> **Data:** 2026-06-06

---

## 1. O que mudou da v3_2 para a v3_3?

| Categoria | Mudança |
|-----------|---------|
| **Notebook** | Evoluiu de HASH-D (26 células, sem oráculo) para HASH-B (29 células, com oráculo, com outputs, com menção v3_3) |
| **notebooks/** | Adicionados 6 apêndices Python + `validacao_exaustiva_64.csv` como suporte local ao notebook |
| **outputs/** | Adicionado `validacao_exaustiva_64.csv` + `preparacao_banca_acolhemente_pb.md` |
| **tests/** | Adicionado `test_no_regression_vs_v3_2_contract.py` |
| **audits/** | Adicionados: `v3_3_excellence_closure_report.md`, `v3_3_1_semantic_gate_closure_report.md`, `v3_3_2_final_sync_closure_report.md`, `v3_3_banca_preparation_report.md`, `v3_3_code_traceability_preparation_report.md`, `v3_3_symbols_taxonomy_fix_report.md` |
| **docs/** | Adicionados: `preparacao_banca_acolhemente_pb.md`, ADR de R5/subsunção, SDD de excellence closure |
| **LaTeX** | PDF recompilado (72 páginas, 1.6MB) com correções de taxonomia, SBC sigla, R5 subsunção |
| **Apêndices** | `simbolos_acolhemente.py` corrigido: A tipo `"nuclear"` → `"saida_inferida"` |
| **Apêndices** | `gerar_tabelas_resultados.py` corrigido: A "Nuclear" → "Saída inferida" |

## 2. O notebook final pertence à v3_3?

**Sim.** O notebook canônico da v3_3 é:

```
academic_abntex2_attempt_v3_3/notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb
SHA256: d266fe637ff50e1d680b9db35ef81fdf89f7b786370eea670140f05133628ac5
```

Evidências: hash idêntico em `notebooks/` e `outputs/`, 29 células, oráculo presente, menção v3_3.

O notebook em `./notebooks/` (raiz) **NÃO** pertence à v3_3 — é artefato legado.

## 3. O PDF final em `reports/pdf/` foi produzido a partir de qual notebook?

O PDF em `reports/pdf/Trabalho_Trilha_I_AcolheMente_PB.pdf` (17 páginas, 144KB) **NÃO** foi produzido a partir do pipeline abnTeX2 da v3_3.

Ele foi produzido via **nbconvert** (notebook → LaTeX article → PDF), evidenciado por:
- `\documentclass[11pt]{article}` (não abnTeX2)
- `\usepackage[breakable]{tcolorbox}` (característico de nbconvert)
- 17 páginas (vs 72 do abnTeX2)
- Fonte LaTeX em `reports/tex/Trabalho_Trilha_I_AcolheMente_PB.tex` (1481 linhas)

**O PDF acadêmico final da v3_3** é:

```
academic_abntex2_attempt_v3_3/latex/main_acolhemente_abntex2.pdf
72 páginas, 1.6MB, abnTeX2
```

## 4. Qual script ou pipeline gerou o PDF?

### PDF abnTeX2 (v3_3, 72 páginas):
- **Pipeline:** `scripts/build_abntex2_local.sh` → chama `build_abntex2_from_colab.py` + `validate_abntex2_outputs.py`
- **Compilação:** pdflatex + bibtex sobre `latex/main_acolhemente_abntex2.tex`
- **Referências:** `latex/referencias.bib`

### PDF nbconvert (reports/pdf, 17 páginas):
- **Pipeline:** nbconvert (jupyter notebook → LaTeX → PDF)
- **Fonte:** `reports/tex/Trabalho_Trilha_I_AcolheMente_PB.tex` (gerado por nbconvert)
- **Observação:** pipeline anterior, provavelmente da versão legada do notebook em `./notebooks/`

## 5. Quais figuras, tabelas e apêndices entraram no PDF abnTeX2?

### Figuras (8):
- `cenarios_ativacao_regras.png`
- `comparacao_baseline_motor.png`
- `fluxo_proveniencia_dados.png`
- `fluxo_pseudonimizacao_acolhimento.png`
- `grafo_governanca_acolhemente.png`
- `grafo_regras_7vars.png`
- `logo_urutai.png`
- `resultado_cenarios_sinteticos.png`

### Tabelas LaTeX (3):
- `_build/tabela_variaveis.tex`
- `_build/tabela_regras.tex`
- `_build/tabela_cenarios.tex`

### Apêndices Python (8):
- `simbolos_acolhemente.py`
- `regras_acolhemente.py`
- `motor_resolucao_acolhemente.py`
- `cenarios_sinteticos_acolhemente.py`
- `gerar_tabelas_resultados.py`
- `grafo_explicabilidade_acolhemente.py`
- `grafo_pseudonimizacao_acolhimento.py`
- `grafos_governanca_proveniencia.py`

## 6. Quais testes validaram a entrega?

8 módulos de teste (136 passed, 1 skipped):
- `test_motor_equivalence_contract.py` — equivalência dos motores
- `test_academic_flow_contract.py` — fluxo acadêmico
- `test_attempt_abntex2_contract.py` — estrutura abnTeX2
- `test_attempt_academic_structure.py` — estrutura acadêmica
- `test_attempt_pdf_quality.py` — qualidade do PDF
- `test_data_usage_explanation_contract.py` — uso de dados
- `test_no_regression_vs_v3_2_contract.py` — anti-regressão
- `test_operational_privacy_contract.py` — privacidade

## 7. Artefatos canônicos

| Artefato | Caminho canônico |
|----------|------------------|
| PDF abnTeX2 | `academic_abntex2_attempt_v3_3/latex/main_acolhemente_abntex2.pdf` |
| Notebook | `academic_abntex2_attempt_v3_3/notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb` |
| CSV validação | `academic_abntex2_attempt_v3_3/outputs/validacao_exaustiva_64.csv` |
| Motor pedagógico | `academic_abntex2_attempt_v3_3/appendices/motor_resolucao_acolhemente.py` |
| Motor modular | `src/acolhemente/motor.py` |

## 8. Artefatos derivados

| Artefato | Derivado de |
|----------|-------------|
| `v3_3/outputs/Trabalho_Trilha_I_AcolheMente_PB.ipynb` | Cópia de `v3_3/notebooks/` (HASH-B idêntico) |
| `v3_3/outputs/main_acolhemente_abntex2.pdf` | Cópia de `v3_3/latex/` (tamanho idêntico) |
| `reports/pdf/Trabalho_Trilha_I_AcolheMente_PB.pdf` | Gerado via nbconvert, **NÃO** derivado da v3_3 |

## 9. Cópias redundantes

- 6 cópias do notebook HASH-D (v3_1/v3_2) — todas idênticas
- 2 cópias do notebook HASH-B (v3_3) — notebooks/ e outputs/
- 3 cópias do PDF nbconvert — reports/pdf/, reports/tex/, raiz

## 10. Inconsistências

| # | Inconsistência | Severidade |
|---|---------------|------------|
| 1 | O PDF em `reports/pdf/` (17 pp, nbconvert) **não é** o PDF acadêmico final da v3_3 (72 pp, abnTeX2) | **CRÍTICA** |
| 2 | O notebook em `./notebooks/` (raiz) **não é** o notebook da v3_3 | **ALTA** |
| 3 | O notebook HASH-D não evoluiu entre v3_1 e v3_2 (hashes idênticos) | INFORMATIVA |
| 4 | `v3_3/scripts/notebooks/` contém versão intermediária (HASH-C), não a final | BAIXA |

---

*Relatório gerado em 2026-06-06.*
