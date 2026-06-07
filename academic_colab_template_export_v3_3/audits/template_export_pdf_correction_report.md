# Relatório de Correção do PDF Article Demonstrativo

> **Data:** 2026-06-07  
> **Versão:** v3.3 template export corrigida

---

## Problemas corrigidos

### 1. Página "temp_limpo" ✅ CORRIGIDO

**Causa:** `nbconvert` gera `\title{temp_limpo}` a partir do nome do notebook limpo.

**Correção:** Remoção via regex de `\title{...}`, `\author{...}`, `\date{...}` e `\maketitle` do `.tex` gerado. Também remove qualquer ocorrência textual de "temp_limpo".

**Verificação:** `pdftotext ... | grep "temp_limpo"` → 0 ocorrências.

### 2. Lista de Figuras vazia ✅ CORRIGIDO

**Causa:** `\listoffigures` inserida sem figuras com `\caption`.

**Correção:** Removida completamente. O PDF article demonstrativo não inclui lista de figuras.

**Verificação:** `grep "listoffigures" .tex` → 0 ocorrências. `pdftotext ... | grep "Lista de Figuras"` → 0.

### 3. Lista de Tabelas vazia ✅ CORRIGIDO

**Causa:** `\listoftables` inserida sem tabelas com `\caption`.

**Correção:** Removida completamente.

**Verificação:** `grep "listoftables" .tex` → 0 ocorrências.

### 4. Referências duplicadas ✅ CORRIGIDO

**Causa:** `\bibliography{referencias}` + `\bibliographystyle{plain}` geravam página "Referências" em branco, duplicando a seção 8 manual.

**Correção:** Removidas todas as diretivas de bibliografia automática. A seção 8 "Referências Bibliográficas" (manual, no corpo do notebook) permanece como única fonte de referências.

**Verificação:** `grep "bibliography" .tex` → 0 ocorrências. Seção 8 presente no PDF (linha 77).

### 5. Apêndices sem código ✅ CORRIGIDO

**Causa:** `nbconvert` convertia os apêndices do notebook como texto Markdown, gerando apenas placeholders.

**Correção:** Substituição completa do bloco de apêndices por `\lstinputlisting` nativo, que inclui o código-fonte dos 6 arquivos `.py` diretamente no PDF.

**Arquivos renderizados:**
- `simbolos_acolhemente.py` → Apêndice A
- `regras_acolhemente.py` → Apêndice B
- `motor_resolucao_acolhemente.py` → Apêndice C
- `cenarios_sinteticos_acolhemente.py` → Apêndice D
- `grafo_explicabilidade_acolhemente.py` → Apêndice E
- `gerar_tabelas_resultados.py` → Apêndice F

**Verificação:** `pdftotext | grep "def inferir_acolhimento"` → 1 ocorrência. `pdftotext | grep "REGRAS_CNF"` → 7 ocorrências.

### 6. Numeração dos apêndices ✅ CORRIGIDO

**Causa:** Sem `\renewcommand{\thesection}`, os apêndices apareciam como ".1", ".2".

**Correção:** Adicionado `\renewcommand{\thesection}{Apêndice \Alph{section}}` após `\appendix`.

**Verificação:** PDF mostra "Apêndice A", "Apêndice B", ..., "Apêndice F".

---

## Checklist de integridade

| # | Critério | Status |
|---|----------|--------|
| 1 | Sem "temp_limpo" no PDF | ✅ |
| 2 | Sem Lista de Figuras vazia | ✅ |
| 3 | Sem Lista de Tabelas vazia | ✅ |
| 4 | Seção 8 "Referências Bibliográficas" presente | ✅ |
| 5 | Sem página "Referências" em branco | ✅ |
| 6 | Apêndices A–F com código completo | ✅ |
| 7 | Numeração correta dos apêndices | ✅ |
| 8 | PDF via article/nbconvert/xelatex | ✅ `\documentclass[11pt]{article}` |
| 9 | PDF abnTeX2 intocado | ✅ SHA256 preservado |
| 10 | Notebook funcional anexado usado como referência | ✅ Diff report criado |
| 11 | PDF abre e tem conteúdo legível | ✅ 23 páginas, 145 KB |

---

## Métricas do PDF

- **Classe:** `article`
- **Compilador:** xelatex
- **Páginas:** 23
- **Tamanho:** 145 KB
- **Apêndices:** 6 (A–F) com código-fonte completo

---

*Relatório gerado em 2026-06-07.*
