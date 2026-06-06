# Notebook / PDF Pipeline — Resumo Executivo

> **Data:** 2026-06-06
> **Projeto:** AcolheMente Escolar PB — Trilha I IF Goiano, v3.3

---

## 1. O notebook AcolheMente faz exatamente o mesmo que o template?

**Segue a metodologia e o espírito do template, mas não replica literalmente sua pipeline técnica simplificada.**

## 2. Explicação em 5 linhas

O template da Trilha I organiza o trabalho em notebook executável e gera PDF diretamente no Colab via `nbconvert → article → xelatex`. O AcolheMente preserva a mesma estrutura pedagógica no notebook — capa, texto, código, apêndices, referências — mas produz o PDF final por pipeline LaTeX abnTeX2 nativa no repositório. A razão é técnica: abnTeX2 exige `\documentclass{abntex2}`, que o nbconvert não oferece. A separação não é limitação — é escolha de engenharia para garantir robustez tipográfica sem fragilizar o notebook executável.

## 3. O que o notebook faz

- Artefato acadêmico executável no Google Colab
- 29 células (13 markdown + 16 code)
- Capa institucional, texto acadêmico, 6 apêndices Python (`%%writefile`)
- Motor de inferência com R1–R6, validação exaustiva de 64 cenários, oráculo independente
- Grafos de regras, governança e proveniência
- Referências bibliográficas (`%%writefile referencias.bib`)
- Exportação alternativa via `nbconvert --to html` para preview

## 4. O que o PDF faz

- Documento acadêmico formal de 72 páginas
- Classe `\documentclass{abntex2}` — abnTeX2 nativo
- Compilado com pdflatex + bibtex sobre `main_acolhemente_abntex2.tex`
- Inclui: capa, folha de rosto, sumário, 24 seções, 8 figuras, 3 tabelas, referências, 8 apêndices
- Citações ABNT via `abntex2cite`
- Qualidade tipográfica profissional NBR 14724

## 5. Por que abnTeX2 foi tratado fora do Colab

- abnTeX2 é classe de documento (`\documentclass{abntex2}`), não pacote
- nbconvert sempre gera `\documentclass{article}` — incompatível com abnTeX2
- Instalação completa de TeX/abnTeX2 no Colab é pesada (4–5 GB), lenta e efêmera
- Compilação de 72 páginas com figuras, tabelas e apêndices no Colab seria frágil
- Separação intencional: notebook leve para avaliação + PDF robusto para formalidade

## 6. Houve PDF→HTML? O que significa?

- **Não houve PDF→HTML.** Houve notebook→HTML (`nbconvert --to html`).
- É exportação alternativa leve para preview no Colab.
- **Nenhuma relação** com a geração do PDF abnTeX2.
- O PDF é gerado exclusivamente por pdflatex + bibtex sobre o `.tex` nativo.

## 7. Versão recomendada para defesa

| Artefato | Caminho | Usar para |
|----------|---------|-----------|
| **PDF abnTeX2** | `academic_abntex2_attempt_v3_3/latex/main_acolhemente_abntex2.pdf` | Documento formal de referência (72 pp) |
| **Notebook Colab** | `academic_abntex2_attempt_v3_3/notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb` | Demonstração executável do motor |
| **CSV validação** | `academic_abntex2_attempt_v3_3/outputs/validacao_exaustiva_64.csv` | Prova de validação exaustiva |

**NÃO usar:** `reports/pdf/Trabalho_Trilha_I_AcolheMente_PB.pdf` (17 pp, artefato legado nbconvert).

## 8. Frase pronta para a apresentação

> "Eu segui o padrão pedagógico do template da Trilha I, que organiza o trabalho em notebook com células textuais, código, apêndices e geração de artefatos. Contudo, para alcançar um acabamento acadêmico mais robusto, especialmente com abnTeX2, a versão final separou o notebook executável da composição tipográfica do PDF. O notebook demonstra a lógica e a reprodutibilidade; o PDF abnTeX2 consolida o relatório formal. A robustez foi obtida separando execução didática e composição tipográfica final."

---

*Resumo executivo preparado em 2026-06-06. Nenhum artefato consolidado foi modificado.*
