# Resumo Executivo — Exportação Article do Notebook

> **Data:** 2026-06-07

---

## 1. Por que a nova variante foi criada

O template da Trilha I (`Resposta_Trabalho_Trilha_I.ipynb`) gera PDF diretamente no Colab via `nbconvert → article → xelatex`. Para demonstrar que o notebook AcolheMente também é capaz de gerar PDF no padrão do template, criou-se uma variante isolada com essa pipeline.

## 2. Como se relaciona ao template do professor

A variante reproduz **exatamente** a mesma lógica funcional: limpa células técnicas, converte para LaTeX com `nbconvert --to latex --no-input`, injeta pacotes e traduções, compila com `xelatex + bibtex`. A classe é `article` — idêntica ao template.

## 3. Como gera PDF via article

```
Notebook → limpa células → nbconvert --to latex → .tex (article)
→ injeta pacotes/traduções → xelatex × 3 + bibtex → PDF
```

## 4. Por que não usa abnTeX2

Porque o objetivo é reproduzir a pipeline do template, que usa `article`. O PDF abnTeX2 é artefato separado com controle tipográfico mais profundo.

## 5. Qual PDF é "gerado pelo notebook"

`Trabalho_Trilha_I_AcolheMente_PB_TemplateExport_article.pdf` — 16 páginas, classe `article`, gerado via `nbconvert + xelatex`.

## 6. Qual PDF é o formal

`main_acolhemente_abntex2.pdf` — 72 páginas, classe `abntex2`, gerado via pipeline LaTeX nativa. **Este é o documento de submissão.**

## 7. Como explicar na apresentação

> "O notebook gera seu próprio PDF via nbconvert e xelatex, seguindo a mesma lógica do template da Trilha I. Esse PDF demonstra que o notebook é funcional e exportável. Em paralelo, o PDF formal em abnTeX2 preserva o acabamento acadêmico completo."

## 8. Arquivos criados

| Arquivo | Descrição |
|---------|-----------|
| `notebooks/Trabalho_Trilha_I_AcolheMente_PB_TemplateExport.ipynb` | Notebook demonstrativo com pipeline de exportação |
| `scripts/build_article_pdf_from_notebook.py` | Script local para reproduzir a compilação |
| `outputs/...article.pdf` | PDF demonstrativo (16 pp, article, 116 KB) |
| `outputs/...article.tex` | .tex intermediário |
| `outputs/build_article_pdf.log` | Log de compilação |
| `audits/template_pipeline_reverse_engineering.md` | Engenharia reversa do template |
| `audits/article_export_quality_gate.md` | Quality gate (15 critérios) |
| `audits/fala_oral_notebook_template_export.md` | Fala oral (1 min) |
| `audits/template_export_executive_summary.md` | Este resumo |
| `README.md` | Documentação da pasta |

## 9. Arquivos que permaneceram intocados

- `academic_abntex2_attempt_v3_3/latex/main_acolhemente_abntex2.pdf` ✅
- `academic_abntex2_attempt_v3_3/latex/main_acolhemente_abntex2.tex` ✅
- `academic_abntex2_attempt_v3_3/notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb` ✅
- `academic_abntex2_attempt_v3_3/appendices/*` ✅
- `src/acolhemente/*` ✅
- `tests/*` ✅

## 10. Como reproduzir o build

**No Colab:** abrir o notebook, executar todas as células (incluindo a final de exportação).

**Localmente:**
```bash
cd academic_colab_template_export_v3_3
python3 scripts/build_article_pdf_from_notebook.py
```

Requer: `xelatex`, `bibtex`, `jupyter`, `nbconvert`.

---

*Resumo executivo preparado em 2026-06-07.*
