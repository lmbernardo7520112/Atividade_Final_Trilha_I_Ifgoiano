# Diff: Versão Repo vs Versão Colab Funcional

> **Data:** 2026-06-07

---

## Resumo

Comparação entre a versão original do repositório e o notebook funcional uploadado pelo usuário após testes no Google Colab.

## Células alteradas

| Célula | Tipo | Alteração |
|--------|------|-----------|
| 0–26 | todas | ✅ Idênticas — nenhuma alteração no conteúdo acadêmico |
| 27 | code | ❌ Diferente — adicionado `import os` no topo |
| 28 | code | ❌ Diferente — `sed` com aspas corrigidas, detalhes de escaping |

### Cell 27: Captura do notebook

**Repo:** `import os` dentro do bloco `except` (escopo limitado)
**Upload:** `import os` movido para o topo do script (escopo global)

**Justificativa:** Necessário porque `os.path.exists()` é chamado fora do bloco `except` na verificação final.

### Cell 28: Pipeline de exportação

**Diferenças do upload vs repo:**
- `sed` com aspas corrigidas: `!sed -i '/nocaption/d' "{tex_path}"` (com aspas em torno do path)
- Resto da lógica idêntico

## Problemas observados no PDF uploadado

1. **Página "temp_limpo"** na primeira página — `\title{temp_limpo}` gerado pelo nbconvert
2. **Lista de Figuras vazia** — `\listoffigures` sem entradas reais
3. **Lista de Tabelas vazia** — `\listoftables` sem entradas reais
4. **Referências duplicadas** — seção 8 manual + `\bibliography{}` automática
5. **Apêndices sem código** — apenas placeholders "Código-fonte completo no arquivo..."
6. **Numeração dos apêndices errada** — ".1", ".2" em vez de "Apêndice A", "Apêndice B"

## Correções incorporadas

Todas as 6 correções acima foram aplicadas na versão corrigida. Ver `template_export_pdf_correction_report.md`.

---

*Relatório gerado em 2026-06-07.*
