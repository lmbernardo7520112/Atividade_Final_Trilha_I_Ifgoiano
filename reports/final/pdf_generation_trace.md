# PDF Generation Trace — Rastreamento da Geração do PDF Final

> **Data:** 2026-06-06

---

## 1. Dois PDFs distintos no repositório

O repositório contém **dois PDFs com nomes e origens diferentes**:

| PDF | Páginas | Bytes | SHA256 (16) | Pipeline |
|-----|---------|-------|-------------|----------|
| `reports/pdf/Trabalho_Trilha_I_AcolheMente_PB.pdf` | 17 | 144.779 | `fee230ff7a9fdfb3` | nbconvert |
| `academic_abntex2_attempt_v3_3/latex/main_acolhemente_abntex2.pdf` | 72 | 1.610.400 | `9702f1b0ab5b0a69` | pdflatex+bibtex (abnTeX2) |

### PDF em `reports/pdf/` — Via nbconvert

**Fonte LaTeX:** `reports/tex/Trabalho_Trilha_I_AcolheMente_PB.tex` (1481 linhas)

**Evidências de nbconvert:**
- `\documentclass[11pt]{article}` — classe article, não abnTeX2
- `\usepackage[breakable]{tcolorbox}` — pacote de nbconvert
- Estrutura de células notebook convertidas para LaTeX
- 17 páginas — compatível com conversão de notebook curto

**Notebook fonte provável:** `./notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb` (HASH-A, 20 células, 53.9KB), baseado na correspondência de tamanho e ausência de metadata Colab.

**Figuras incluídas:**
- `reports/tex/grafo_governanca_7vars.png`
- `reports/tex/grafo_regras_7vars.png`
- `reports/tex/logo_urutai.png`

**Referências:** `reports/tex/referencias.bib`

**Cópias idênticas (SHA256):**
- `reports/tex/Trabalho_Trilha_I_AcolheMente_PB.pdf` (mesmo hash)
- `./Trabalho_Trilha_I_AcolheMente_PB.pdf` (raiz do projeto, mesmo hash)

### PDF abnTeX2 da v3_3 — Via pdflatex+bibtex

**Fonte LaTeX:** `academic_abntex2_attempt_v3_3/latex/main_acolhemente_abntex2.tex`

**Evidências:**
- `\documentclass[12pt, openright, oneside, a4paper, ...]` — abnTeX2
- Header: "AcolheMente Escolar PB --- Documento Academico Final v3.3"
- 72 páginas — documento acadêmico completo
- 1.6MB — inclui todas as figuras e tabelas

**Pipeline de build:**
1. `scripts/build_abntex2_local.sh` — script shell orquestrador
2. → chama `scripts/build_abntex2_from_colab.py` — gera/valida artefatos
3. → chama `scripts/validate_abntex2_outputs.py` — validação
4. Compilação: `pdflatex` + `bibtex` sobre `main_acolhemente_abntex2.tex`

**Figuras incorporadas (8):**
- `figures/cenarios_ativacao_regras.png`
- `figures/comparacao_baseline_motor.png`
- `figures/fluxo_proveniencia_dados.png`
- `figures/fluxo_pseudonimizacao_acolhimento.png`
- `figures/grafo_governanca_acolhemente.png`
- `figures/grafo_regras_7vars.png`
- `figures/logo_urutai.png`
- `figures/resultado_cenarios_sinteticos.png`

**Tabelas incorporadas (3):**
- `_build/tabela_variaveis.tex`
- `_build/tabela_regras.tex`
- `_build/tabela_cenarios.tex`

**Referências:** `latex/referencias.bib`

**Cópia derivada:**
- `academic_abntex2_attempt_v3_3/outputs/main_acolhemente_abntex2.pdf` (tamanho idêntico: 1.610.400 bytes, hash diferente — provável recompilação menor)

---

## 2. Qual é o PDF acadêmico final?

> O PDF acadêmico final para apresentação à banca é:
>
> **`academic_abntex2_attempt_v3_3/latex/main_acolhemente_abntex2.pdf`**
>
> 72 páginas, abnTeX2, com todas as figuras, tabelas, apêndices e referências.

O PDF em `reports/pdf/` é um artefato anterior gerado via nbconvert, com 17 páginas — **não é o PDF final da v3_3**.

---

## 3. Elos comprovados e não comprovados

| Elo | Status |
|-----|--------|
| `main_acolhemente_abntex2.tex` → `main_acolhemente_abntex2.pdf` | ✅ Comprovado (auxiliares .aux/.bbl/.log presentes) |
| `build_abntex2_local.sh` → compilação | ✅ Comprovado (script lê e invoca pdflatex) |
| `generate_notebook.py` → notebook | ✅ Comprovado (gera .ipynb a partir dos apêndices) |
| nbconvert → `reports/pdf/` | ✅ Comprovado (tcolorbox no .tex fonte) |
| Notebook raiz → PDF nbconvert | ⚠️ Provável mas não comprovado com certeza (não há log de nbconvert) |
| PDF `reports/pdf/` como cópia de `reports/tex/` | ✅ Comprovado (SHA256 idêntico) |

---

*Relatório gerado em 2026-06-06.*
