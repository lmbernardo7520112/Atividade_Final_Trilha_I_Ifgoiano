# v3.3 Symbols Taxonomy Fix Report

> **Data:** 2026-05-29
> **Versão base:** academic_abntex2_attempt_v3_3 (v3.3.2)

## 1. Objetivo

Corrigir divergência residual no campo `tipo` da variável A em `appendices/simbolos_acolhemente.py`, alinhando-o à taxonomia final do PDF e da tabela LaTeX: A = Saída inferida.

## 2. Problema identificado

O relatório de rastreabilidade (`audits/v3_3_code_traceability_preparation_report.md`) indicou que `A` ainda aparecia como `"nuclear"` em estrutura legada no código-fonte, embora o PDF e `_build/tabela_variaveis.tex` já apresentassem `A` como "Saída inferida".

Taxonomia anterior no código:
- E, B, V, S, **A** → `"nuclear"` (5 nucleares)
- C, I → `"contextual"` (2 contextuais)

Taxonomia correta (PDF/LaTeX):
- E, B, V, S → entrada nuclear (4)
- C, I → entrada contextual (2)
- A → saída inferida (1)

## 3. Correção executada

### `appendices/simbolos_acolhemente.py`
- L9: comentário `# --- 5 Variaveis Nucleares ---` → `# --- 4 Variaveis Nucleares de Entrada ---`
- L26: `"tipo": "nuclear"` → `"tipo": "saida_inferida"` (apenas para chave `"A"`)
- L32: assert `== 5` → `== 4`
- L33 (nova): `assert sum(... "saida_inferida") == 1`

### `appendices/gerar_tabelas_resultados.py`
- L22: `A & Nuclear` → `A & Saída inferida`

### `notebooks/simbolos_acolhemente.py`
- Copiado de `appendices/simbolos_acolhemente.py` para sincronizar

## 4. Arquivos alterados

| Arquivo | Alteração |
|---------|-----------|
| `appendices/simbolos_acolhemente.py` | Tipo de A: `"nuclear"` → `"saida_inferida"`, asserts ajustados |
| `appendices/gerar_tabelas_resultados.py` | LaTeX hardcoded: `Nuclear` → `Saída inferida` para A |
| `notebooks/simbolos_acolhemente.py` | Cópia sincronizada |

## 5. Arquivos NÃO alterados

| Arquivo | Razão |
|---------|-------|
| `_build/tabela_variaveis.tex` | Já estava correto (`Sa\'ida inferida`) |
| `appendices/regras_acolhemente.py` | Não referencia tipos de variáveis |
| `appendices/motor_resolucao_acolhemente.py` | Não referencia tipos de variáveis |
| `src/acolhemente/motor.py` | Não referencia tipos de variáveis |
| `outputs/validacao_exaustiva_64.csv` | Não afetado (A é coluna de resultado, não tipo) |

## 6. Gates executados

| Gate | Resultado |
|------|-----------|
| Symbol taxonomy gate (Python) | ✅ PASSED |
| pytest (`tests/` — 8 módulos) | ✅ 136 passed, 1 skipped, 0 failed |
| CSV validation (64 linhas) | ✅ PASSED |

## 7. Resultado

- A aparece como `"saida_inferida"` no código-fonte
- A tabela `_build/tabela_variaveis.tex` continua correta (já era)
- O gerador `gerar_tabelas_resultados.py` agora também diz "Saída inferida"
- Testes passam sem alteração de expectativas
- CSV 64 permanece válido (64/64 ok=True)
- Lógica do motor preservada (nenhuma alteração em `inferir_acolhimento`, regras ou resolução)

## 8. Veredito

Correção fechada. Divergência residual eliminada sem alteração da lógica do motor. A taxonomia 4-2-1 (4 entradas nucleares, 2 contextuais, 1 saída inferida) está agora consistente entre código-fonte, tabela LaTeX, PDF e documento de defesa.
