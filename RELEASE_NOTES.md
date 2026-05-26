# Release Notes — v1.0.0

## AcolheMente Escolar PB — Motor de Inferência Lógico para Acolhimento em Saúde Mental Escolar

**Data de release:** 2026-05-26
**Status:** ✅ FINAL (v1.0.0)
**Promovido de:** v0.3.0-rc1

---

## Resumo

Motor lógico determinístico com **7 variáveis proposicionais** (5 nucleares + 2 contextuais)
e **6 regras lógicas** em CNF, congelado por ADR-011. Entrega final da Trilha I do curso
de Pós-Graduação em Inteligência Artificial Aplicada — IF Goiano.

## Métricas de Qualidade

| Métrica | Resultado |
|---------|-----------|
| Testes | **80 passed**, 0 failed |
| Coverage | **88%** |
| Lint (ruff) | **All checks passed** |
| Notebook | **Executa do início ao fim** |
| PDF | **✅ 71 KB** (`reports/pdf/Trabalho_Trilha_I_AcolheMente_PB.pdf`) |
| Caminhos locais | **0** (nenhum `.gemini` ou `file:///home`) |

## Compilação do PDF

```
$ jupyter nbconvert --to pdf notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb
[NbConvertApp] PDF successfully created
[NbConvertApp] Writing 71838 bytes to reports/pdf/Trabalho_Trilha_I_AcolheMente_PB.pdf
```

**Motor TeX:** TinyTeX (TeX Live 2026) + xelatex via nbconvert
**Tamanho do PDF:** 71 KB
**Comando:** `jupyter nbconvert --to pdf --output-dir=reports/pdf notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb`

## Artefatos da Entrega

| Artefato | Caminho | Tamanho |
|----------|---------|---------|
| Notebook final | `notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb` | 23 KB |
| PDF final | `reports/pdf/Trabalho_Trilha_I_AcolheMente_PB.pdf` | 71 KB |
| LaTeX gerado | `reports/tex/Trabalho_Trilha_I_AcolheMente_PB.tex` | 60 KB |
| Grafo de regras | `reports/figures/grafo_regras_7vars.png` | 2.0 MB |
| Grafo de governança | `reports/figures/grafo_governanca_7vars.png` | 985 KB |
| BibTeX | `templates/abntex2/referencias.bib` | 1.9 KB |

## Proibições que permanecem

- ❌ Nenhuma variável adicional (motor congelado por ADR-011)
- ❌ Nenhuma regra adicional (R1–R6 são o teto)
- ❌ Nenhum diagnóstico automatizado
- ❌ Nenhum ranking de estudantes
- ❌ Nenhum merge entre tiers
- ❌ Nenhum dado identificável
- ❌ Nenhuma API externa (Gemini, OpenAI)
