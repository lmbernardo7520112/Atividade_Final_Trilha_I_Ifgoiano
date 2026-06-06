# Notebook Version Identity Report — Auditoria Forense

> **Data:** 2026-06-06
> **Escopo:** Todas as cópias de `Trabalho_Trilha_I_AcolheMente_PB.ipynb` no repositório

---

## 1. Inventário completo de notebooks

| # | Caminho | SHA256 (primeiros 16) | Bytes | Células | Grupo de hash |
|---|---------|----------------------|-------|---------|---------------|
| 1 | `./notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb` | `86cd5603459e0d6f` | 53910 | 20 | **HASH-A** (único) |
| 2 | `./academic_abntex2_attempt_v3_3/notebooks/...ipynb` | `d266fe637ff50e1d` | 73188 | 29 | **HASH-B** |
| 3 | `./academic_abntex2_attempt_v3_3/outputs/...ipynb` | `d266fe637ff50e1d` | 73188 | 29 | **HASH-B** |
| 4 | `./academic_abntex2_attempt_v3_3/scripts/notebooks/...ipynb` | `af9043777ff9e41a` | 62784 | 26 | **HASH-C** (único) |
| 5 | `./academic_abntex2_attempt_v3_2/notebooks/...ipynb` | `22e8db2b8597a12e` | 62673 | 26 | **HASH-D** |
| 6 | `./academic_abntex2_attempt_v3_2/outputs/...ipynb` | `22e8db2b8597a12e` | 62673 | 26 | **HASH-D** |
| 7 | `./academic_abntex2_attempt_v3_2/scripts/notebooks/...ipynb` | `22e8db2b8597a12e` | 62673 | 26 | **HASH-D** |
| 8 | `./academic_abntex2_attempt_v3_1/notebooks/...ipynb` | `22e8db2b8597a12e` | 62673 | 26 | **HASH-D** |
| 9 | `./academic_abntex2_attempt_v3_1/outputs/...ipynb` | `22e8db2b8597a12e` | 62673 | 26 | **HASH-D** |
| 10 | `./academic_abntex2_attempt_v3_1/scripts/notebooks/...ipynb` | `22e8db2b8597a12e` | 62673 | 26 | **HASH-D** |
| 11 | `./academic_abntex2_attempt_v2/notebooks/...ipynb` | `b8d8bea2f6488447` | 61447 | 26 | **HASH-E** (único) |

### Grupos de hash identificados

| Grupo | Ocorrências | Versão | Observações |
|-------|-------------|--------|-------------|
| **HASH-A** | 1 | pré-v2 ou derivado independente | 20 células, 53.9KB, sem Colab, sem oráculo, sem menção a versões |
| **HASH-B** | 2 | **v3_3 canônico** | 29 células, 73.2KB, Colab, oráculo, menção v3_3, outputs presentes |
| **HASH-C** | 1 | intermediário v3_3 | 26 células, 62.8KB, Colab, sem oráculo, sem outputs — versão de template |
| **HASH-D** | 6 | **v3_1/v3_2 congelado** | 26 células, 62.7KB, Colab, sem oráculo, sem outputs |
| **HASH-E** | 1 | **v2** | 26 células, 61.4KB, Colab, sem oráculo |

---

## 2. Análise diferencial por capacidade

| Capacidade | HASH-A (raiz) | HASH-B (v3_3) | HASH-C (scripts) | HASH-D (v3_1/v3_2) | HASH-E (v2) |
|------------|:---:|:---:|:---:|:---:|:---:|
| Colab metadata | ❌ | ✅ | ✅ | ✅ | ✅ |
| logo_urutai | ✅ | ✅ | ✅ | ✅ | ✅ |
| R1–R6 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 64 cenários | ✅ | ✅ | ✅ | ✅ | ✅ |
| Oráculo | ❌ | ✅ | ❌ | ❌ | ❌ |
| LGPD/ECA/PSE | ✅/✅/✅ | ✅/✅/✅ | ✅/✅/✅ | ✅/✅/✅ | ✅/✅/✅ |
| Governança | ✅ | ✅ | ✅ | ✅ | ✅ |
| Outputs executados | ✅ | ✅ | ❌ | ❌ | ❌ |
| Menção v3_3 | ❌ | ✅ | ❌ | ❌ | ❌ |
| `inferir_acolhimento` | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## 3. Classificação de cada notebook

### 3.1 `./notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb` (HASH-A)

**Classificação: NÃO corresponde à v3_3.**

Evidências:
- Hash único, não aparece em nenhuma versão acadêmica
- 20 células (v3_3 tem 29)
- Sem metadata Colab
- Sem oráculo independente
- Sem menção a v3_3
- 53.9KB (v3_3 = 73.2KB)
- Sem pseudonimização

Provável origem: versão anterior independente, possivelmente gerada manualmente antes do pipeline `generate_notebook.py`.

### 3.2 `v3_3/notebooks/` e `v3_3/outputs/` (HASH-B)

**Classificação: NOTEBOOK CANÔNICO DA V3_3.**

Evidências:
- Hash idêntico entre `notebooks/` e `outputs/` dentro da v3_3
- 29 células (mais evoluído)
- Contém oráculo independente (`oraculo_acolhimento`)
- Contém menção explícita a v3_3
- Contém outputs executados
- 73.2KB (maior e mais completo)
- Metadata Colab presente

### 3.3 `v3_3/scripts/notebooks/` (HASH-C)

**Classificação: Template intermediário da v3_3.**

Evidências:
- Hash único, diferente de notebooks/ e outputs/
- 26 células (3 a menos que canônico)
- Sem oráculo
- Sem outputs executados
- Provável: versão gerada por `generate_notebook.py` antes de execução/enriquecimento

### 3.4 v3_1 e v3_2 (HASH-D)

**Classificação: Notebook congelado da v3_1/v3_2.**

Evidência: hash idêntico em 6 locais diferentes (notebooks/, outputs/, scripts/notebooks/ de v3_1 e v3_2). Não evoluiu da v3_1 para a v3_2.

### 3.5 v2 (HASH-E)

**Classificação: Notebook da v2, anterior.**

Hash único, ligeiramente menor (61.4KB vs 62.7KB da v3_1/v3_2).

---

## 4. Notebook canônico final

> **O notebook canônico da v3_3 está em:**
>
> `academic_abntex2_attempt_v3_3/notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb`
>
> (idêntico a `academic_abntex2_attempt_v3_3/outputs/Trabalho_Trilha_I_AcolheMente_PB.ipynb`)
>
> **SHA256:** `d266fe637ff50e1d680b9db35ef81fdf89f7b786370eea670140f05133628ac5`
>
> **Grau de confiança:** ALTO — evidência material por hash, conteúdo estrutural (oráculo, 29 células, menção v3_3) e localização canônica.

---

## 5. O notebook em `./notebooks/` (raiz do projeto)

> **NÃO pertence à v3_3.**
>
> É uma versão anterior independente (20 células, sem oráculo, sem Colab, sem menção a versões).
>
> Classificação: **artefato legado, provavelmente anterior à v2**.

---

## 6. Cópias redundantes

| Par | Status |
|-----|--------|
| v3_3/notebooks ↔ v3_3/outputs | ✅ Idênticos (HASH-B) |
| v3_2/notebooks ↔ v3_2/outputs ↔ v3_2/scripts/notebooks | ✅ Idênticos (HASH-D) |
| v3_1/notebooks ↔ v3_1/outputs ↔ v3_1/scripts/notebooks | ✅ Idênticos (HASH-D) |
| v3_1 ↔ v3_2 | ✅ Idênticos (HASH-D) — notebook não evoluiu entre v3_1 e v3_2 |

---

*Relatório gerado em 2026-06-06 via auditoria forense com SHA256, nbformat e inspeção estrutural.*
