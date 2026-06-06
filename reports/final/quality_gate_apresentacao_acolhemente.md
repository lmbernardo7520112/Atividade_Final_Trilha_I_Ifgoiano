# Quality Gate — Preparação de Apresentação AcolheMente Escolar PB

> **Data:** 2026-06-06

---

## Checklist de qualidade

| # | Critério | Status | Evidência |
|---|----------|:------:|-----------|
| 1 | Versão do notebook identificada com evidência material | ✅ | SHA256 HASH-B idêntico em `v3_3/notebooks` e `v3_3/outputs`; 29 células; menção v3_3; oráculo presente |
| 2 | PDF rastreado com evidência | ✅ | Dois PDFs distintos identificados: nbconvert (17pp, reports/pdf) vs abnTeX2 (72pp, v3_3/latex); SHA256 computados |
| 3 | Nenhum arquivo consolidado foi alterado | ✅ | Tarefa exclusivamente de auditoria; nenhum notebook, PDF, motor ou script modificado |
| 4 | Roadmap cobre dados, motor, regras, cenários, governança e limites | ✅ | 16 seções cobrindo todos os tópicos obrigatórios |
| 5 | Explicação de anonimização vs pseudonimização | ✅ | Roadmap §12, Perguntas #2 e #25 |
| 6 | Respostas para perguntas críticas | ✅ | 25 perguntas com respostas curtas e tecnicamente corretas |
| 7 | Caminho claro para apresentação acadêmica | ✅ | Roteiro oral em duas versões (10 min e 25 min) com timing e evidências |
| 8 | PeNSE vs cenários sintéticos vs dataset externo diferenciados | ✅ | Roadmap §3 (três tiers); Perguntas #15 e #16 |
| 9 | Tese de não-diagnóstico presente | ✅ | Roadmap §12; Perguntas #3, #11 |
| 10 | Human-in-the-loop documentado | ✅ | Roadmap §6, §12; Perguntas #11 |
| 11 | Geração do PDF explicada | ✅ | `pdf_generation_trace.md` com pipeline detalhado |
| 12 | Notebook final localizado | ✅ | `v3_3/notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb` (HASH-B) |
| 13 | Não há afirmação sem caminho de arquivo | ✅ | Todos os arquivos citados foram verificados com `ls`, `sha256sum`, `grep` |
| 14 | v3_3 não declarada sem justificativa | ✅ | Classificação por hash, conteúdo estrutural e localização canônica |
| 15 | Inconsistência reports/pdf vs v3_3/latex documentada | ✅ | `pdf_generation_trace.md` e `v3_3_lineage_and_artifact_map.md` §10 |

---

## Inconsistências encontradas e status

| # | Inconsistência | Severidade | Documentada em |
|---|---------------|------------|----------------|
| 1 | PDF em `reports/pdf/` (17pp, nbconvert) ≠ PDF v3_3 (72pp, abnTeX2) | CRÍTICA | `pdf_generation_trace.md` |
| 2 | Notebook em `./notebooks/` (raiz) ≠ notebook v3_3 | ALTA | `notebook_version_identity_report.md` §3.1 |
| 3 | Notebook HASH-D idêntico entre v3_1 e v3_2 | INFORMATIVA | `notebook_version_identity_report.md` §3.4 |
| 4 | `v3_3/scripts/notebooks/` contém versão intermediária | BAIXA | `notebook_version_identity_report.md` §3.3 |

## Recomendações

1. **Para apresentação:** usar o PDF abnTeX2 de 72 páginas (`v3_3/latex/main_acolhemente_abntex2.pdf`), não o de `reports/pdf/`.
2. **Notebook:** referenciar `v3_3/notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb` como canônico.
3. **Considerar:** copiar o PDF abnTeX2 para `reports/pdf/` se desejado, mas apenas como ação consciente do autor.

---

## Veredito

> **APROVADO.** Todos os critérios de qualidade foram atendidos. As inconsistências encontradas foram documentadas com evidências e não impedem a apresentação. O autor deve apenas estar ciente de que o PDF em `reports/pdf/` não é o PDF acadêmico final da v3_3.

---

*Quality gate executado em 2026-06-06.*
