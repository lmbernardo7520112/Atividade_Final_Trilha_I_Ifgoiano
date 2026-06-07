# Quality Gate — Exportação Article do Notebook (Corrigida)

> **Data:** 2026-06-07  
> **Versão:** v3.3 template export — pós-correção

---

- [x] Notebook demonstrativo abre no Colab
- [x] Célula de exportação roda sem ajuste manual
- [x] PDF é gerado (23 páginas, 145 KB)
- [x] PDF não tem página "temp_limpo"
- [x] PDF não tem listas vazias
- [x] PDF não tem referências duplicadas
- [x] PDF não tem página de referências em branco
- [x] Seção 8 Referências Bibliográficas permanece
- [x] Apêndices A–F renderizam código completo
- [x] Apêndices não aparecem como ".1, .2"
- [x] Nenhum arquivo da v3_3 formal foi alterado
- [x] O PDF article é claramente classificado como demonstrativo
- [x] O PDF abnTeX2 continua sendo o formal

---

## Evidências

### Verificação do .tex

```
documentclass: \documentclass[11pt]{article}
temp_limpo:    0 ocorrências
listoffigures: 0 ocorrências
listoftables:  0 ocorrências
bibliography:  0 ocorrências
maketitle:     0 ocorrências
\title{}:      0 ocorrências
lstinputlisting: 6 ocorrências (A-F)
```

### Verificação do PDF

```
temp_limpo:           0 ocorrências
Lista de Figuras:     0 ocorrências
Lista de Tabelas:     0 ocorrências
Seção 8 Referências:  presente (linha 77)
Apêndice A:           presente (linha 809)
def inferir:          1 ocorrência
REGRAS_CNF:           7 ocorrências
Páginas:              23
```

### Integridade v3_3

| Artefato | Modificado? |
|----------|:-----------:|
| `main_acolhemente_abntex2.pdf` | ❌ Não |
| `main_acolhemente_abntex2.tex` | ❌ Não |
| `appendices/*` | ❌ Não |
| `figures/*` | ❌ Não |
| `src/acolhemente/*` | ❌ Não |
| Motor lógico | ❌ Não |
| Variáveis | ❌ Não |
| Regras R1–R6 | ❌ Não |
| CNF | ❌ Não |

---

*Quality gate aprovado em 2026-06-07.*
