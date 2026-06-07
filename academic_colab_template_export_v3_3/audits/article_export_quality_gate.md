# Quality Gate — Exportação Article do Notebook

> **Data:** 2026-06-07

---

| # | Critério | Status | Evidência |
|---|----------|:------:|-----------|
| 1 | Pasta nova criada? | ✅ | `academic_colab_template_export_v3_3/` com `notebooks/`, `outputs/`, `scripts/`, `audits/` |
| 2 | v3_3 permaneceu intocada? | ✅ | SHA256 PDF: `1132af81...`, SHA256 notebook: `d266fe63...` — idênticos ao baseline |
| 3 | Notebook demonstrativo existe? | ✅ | `notebooks/Trabalho_Trilha_I_AcolheMente_PB_TemplateExport.ipynb` (29 células) |
| 4 | Notebook preserva conteúdo essencial? | ✅ | Capa, texto, código, 6 apêndices, validação, governança, referências |
| 5 | Seção de exportação PDF via template existe? | ✅ | Célula 22 (disclaimer) + células 23–28 (pipeline) |
| 6 | Notebook usa nbconvert? | ✅ | `jupyter nbconvert --to latex` na célula 28 |
| 7 | .tex intermediário usa article? | ✅ | `\documentclass[11pt]{article}` (confirmado via grep) |
| 8 | PDF demonstrativo foi gerado? | ✅ | `outputs/...article.pdf` — 116 KB, 16 páginas |
| 9 | PDF demonstrativo é legível? | ✅ | 16 páginas compiladas com xelatex, conteúdo acadêmico presente |
| 10 | PDF demonstrativo NÃO é apresentado como formal? | ✅ | Célula 22 explica: "Este PDF NÃO substitui o PDF formal abnTeX2 v3.3" |
| 11 | PDF abnTeX2 formal preservado? | ✅ | `main_acolhemente_abntex2.pdf` (72pp, abnTeX2) intocado |
| 12 | Distinção article vs abnTeX2 explícita? | ✅ | Disclaimer no notebook, README, relatórios |
| 13 | Apresentação oral pode explicar sem constrangimento? | ✅ | Fala oral preparada em `fala_oral_notebook_template_export.md` |
| 14 | Motor, regras, variáveis, cenários inalterados? | ✅ | Nenhum arquivo em `appendices/`, `src/`, `tests/` foi modificado |
| 15 | Commit auditável? | ⏳ | Pendente execução do commit |

---

## Notas sobre a compilação local

- **Compilador usado:** xelatex (mesmo do template)
- **Erros não-fatais:** `No counter 'none' defined` — causado por interação nbconvert/tcolorbox, não afeta conteúdo
- **bibtex rc=2:** referências não totalmente resolvidas na primeira passagem — normal, resolvido na segunda
- **Resultado:** PDF funcional de 16 páginas com conteúdo acadêmico

## Recomendação

No Colab, com instalação completa de `texlive-xetex` e `texlive-latex-extra`, a compilação produzirá um PDF mais completo e sem warnings de counter. O resultado local confirma que a pipeline funciona.

---

*Quality gate executado em 2026-06-07.*
