# Final Presentation Preparation Summary — Relatório Executivo

> **Data:** 2026-06-06
> **Projeto:** AcolheMente Escolar PB — Trilha I IF Goiano
> **Versão:** v3.3

---

## 1. Versão identificada do notebook

**Notebook canônico da v3_3:**

```
academic_abntex2_attempt_v3_3/notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb
```

SHA256: `d266fe637ff50e1d680b9db35ef81fdf89f7b786370eea670140f05133628ac5`

## 2. Grau de confiança da identificação

**ALTO.** Baseado em evidência material múltipla:
- Hash SHA256 idêntico entre `notebooks/` e `outputs/` dentro da v3_3
- Conteúdo estrutural exclusivo: 29 células, oráculo independente, menção explícita a v3_3
- Maior e mais completo que todas as versões anteriores (73.2KB vs 62.7KB)
- Metadata Colab presente com outputs executados

## 3. Evidências usadas

- SHA256 de 11 notebooks e 3 PDFs
- Análise nbformat: contagem de células, tipos, headings, outputs
- Verificação de 16 capacidades por notebook (Colab, oráculo, LGPD, etc.)
- Inspeção de `\documentclass` nos .tex para identificar pipelines
- Inventário completo de `reports/` e `academic_abntex2_attempt_v3_3/`

## 4. Caminho do notebook canônico

```
academic_abntex2_attempt_v3_3/notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb
```

**Nota:** O notebook em `./notebooks/` (raiz do projeto) **NÃO** é o notebook da v3_3 — é artefato legado (HASH-A, 20 células, sem oráculo).

## 5. Caminho do PDF final

**PDF acadêmico (para banca):**
```
academic_abntex2_attempt_v3_3/latex/main_acolhemente_abntex2.pdf
```
72 páginas, 1.6MB, abnTeX2.

**PDF nbconvert (artefato anterior):**
```
reports/pdf/Trabalho_Trilha_I_AcolheMente_PB.pdf
```
17 páginas, 144KB. NÃO é o PDF final da v3_3.

## 6. Explicação curta da geração do PDF

O PDF acadêmico foi gerado via `pdflatex + bibtex` sobre `main_acolhemente_abntex2.tex`, usando a classe abnTeX2, 8 figuras, 3 tabelas LaTeX e referências bibliográficas. O pipeline é orquestrado por `scripts/build_abntex2_local.sh`.

O PDF em `reports/pdf/` foi gerado via `nbconvert` (notebook → LaTeX article → PDF), provavelmente a partir do notebook legado em `./notebooks/`.

## 7. Artefatos principais

| Artefato | Caminho | Papel |
|----------|---------|-------|
| PDF abnTeX2 | `v3_3/latex/main_acolhemente_abntex2.pdf` | Documento acadêmico final |
| Notebook canônico | `v3_3/notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb` | Notebook Colab executável |
| Motor pedagógico | `v3_3/appendices/motor_resolucao_acolhemente.py` | Implementação didática |
| Motor modular | `src/acolhemente/motor.py` | Implementação de engenharia |
| CSV validação | `v3_3/outputs/validacao_exaustiva_64.csv` | 64 cenários, 0 falhas |
| Símbolos | `v3_3/appendices/simbolos_acolhemente.py` | Variáveis com taxonomia 4-2-1 |
| Regras | `v3_3/appendices/regras_acolhemente.py` | R1–R6 implicativa e CNF |
| 8 figuras | `v3_3/figures/` | Grafos de regras, governança, proveniência, etc. |
| 8 testes | `v3_3/tests/` | 136 passed, 1 skipped |

## 8. Roadmap gerado

```
reports/final/roadmap_apresentacao_academica_acolhemente.md
```

16 seções cobrindo: abertura, justificativa, arquitetura de dados, técnica de IA, variáveis, regras, CNF, implementação, validação, resultados, explicabilidade, governança, reprodutibilidade, limitações, evolução e fechamento.

## 9. Roteiro oral gerado

```
reports/final/roteiro_oral_apresentacao_acolhemente.md
```

Duas versões:
- **Curta:** 10–12 min, 7 blocos cronometrados
- **Completa:** 20–25 min, 11 blocos cronometrados

Cada bloco com: fala sugerida, evidência visual, pergunta provável e resposta.

## 10. Perguntas da banca geradas

```
reports/final/perguntas_banca_respostas_acolhemente.md
```

25 perguntas com respostas curtas e tecnicamente corretas, cobrindo: dados reais, diagnóstico, ML, LGPD, ECA, PSE, variáveis, CNF, guardrails, oráculo, R5, baseline, limitações, evolução.

## 11. Recomendações finais para apresentação

1. **Usar o PDF abnTeX2** (72 pp) como documento de referência, não o de `reports/pdf/` (17 pp).
2. **Abrir o notebook Colab** durante a apresentação para demonstrar execução interativa.
3. **Ter o CSV** `validacao_exaustiva_64.csv` pronto para mostrar se perguntado sobre validação.
4. **Treinar o roteiro** com cronômetro em voz alta — o documento prepara o conteúdo, não substitui o treino oral.
5. **Memorizar as 3 frases-chave:**
   - "O motor sinaliza; o profissional decide."
   - "Em domínio sensível, transparência vale mais que complexidade."
   - "Pseudonimizar, não anonimizar — porque anonimizar impede acolher."
6. **Estar preparado para mostrar código** se perguntado — usar `regras_acolhemente.py` e `motor_resolucao_acolhemente.py` como demonstração de SBC.

---

## Relatórios produzidos nesta sessão

| # | Relatório | Caminho |
|---|-----------|---------|
| 1 | Notebook Version Identity Report | `reports/audits/notebook_version_identity_report.md` |
| 2 | Notebook Version Identity JSON | `reports/audits/notebook_version_identity.json` |
| 3 | v3_3 Lineage and Artifact Map | `reports/audits/v3_3_lineage_and_artifact_map.md` |
| 4 | PDF Generation Trace | `reports/final/pdf_generation_trace.md` |
| 5 | Roadmap Acadêmico | `reports/final/roadmap_apresentacao_academica_acolhemente.md` |
| 6 | Roteiro Oral | `reports/final/roteiro_oral_apresentacao_acolhemente.md` |
| 7 | Perguntas da Banca | `reports/final/perguntas_banca_respostas_acolhemente.md` |
| 8 | Quality Gate | `reports/final/quality_gate_apresentacao_acolhemente.md` |
| 9 | Este resumo executivo | `reports/final/final_presentation_preparation_summary.md` |

---

*Relatório executivo preparado em 2026-06-06. Nenhum artefato consolidado foi modificado.*
