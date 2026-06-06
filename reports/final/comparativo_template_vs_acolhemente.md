# Comparativo Template vs AcolheMente — Tabela Detalhada

> **Data:** 2026-06-06

---

| Aspecto | `Resposta_Trabalho_Trilha_I.ipynb` (Template) | `Trabalho_Trilha_I_AcolheMente_PB.ipynb` (v3_3) | Comentário para apresentação |
|---------|-----------------------------------------------|--------------------------------------------------|------------------------------|
| **Finalidade** | Modelo pedagógico da Trilha I | Trabalho final aplicado (AcolheMente Escolar PB) | "Segui a estrutura do template, aplicando ao meu domínio." |
| **Capa institucional** | ✅ LaTeX com logo IF Goiano | ✅ LaTeX com logo IF Goiano | Idêntica em espírito: capa, nome, curso, título. |
| **Logo IF Goiano** | ✅ `logo_urutai.png` | ✅ `logo_urutai.png` | Mesma logomarca em ambos. |
| **Texto acadêmico** | ✅ Seções: Introdução, Metodologia, Implementação, Resultados, Evolução | ✅ Seções equivalentes + Governança, Proveniência, Explicabilidade | AcolheMente adiciona seções de governança LGPD/ECA/PSE. |
| **Células de código** | 21 (genéricas/demonstrativas) | 16 (motor, regras, validação exaustiva) | AcolheMente: código é a implementação real do SBC. |
| **Scripts de apêndice** | ✅ `%%writefile` para auxiliares | ✅ `%%writefile` para 6 módulos Python | Mesma técnica; AcolheMente tem mais apêndices e mais especializados. |
| **Bibliografia** | ✅ `%%writefile referencias.bib` | ✅ `%%writefile referencias.bib` | Ambos escrevem `.bib` via notebook. |
| **Geração de gráficos** | ✅ (demonstrativa) | ✅ (grafos de regras, governança, proveniência, cenários) | AcolheMente: 8 figuras com significado acadêmico real. |
| **Geração de tabelas** | ✅ (demonstrativa) | ✅ (3 tabelas LaTeX: variáveis, regras, cenários) | AcolheMente: tabelas formais do motor de inferência. |
| **Método de IA** | Genérico (exemplo) | SBC com lógica proposicional e resolução | AcolheMente: técnica específica com R1–R6, CNF, 64 cenários. |
| **Geração de PDF** | ✅ Direto no Colab (nbconvert → xelatex) | ⚠️ `nbconvert --to html` como alternativa; PDF final via pipeline LaTeX separada | "O notebook exporta HTML para preview; o PDF final é gerado por pdflatex no repositório." |
| **Uso de nbconvert** | ✅ `--to latex` (etapa central da pipeline) | ✅ `--to html` (exportação auxiliar) | Template: nbconvert é core. AcolheMente: nbconvert é auxiliar. |
| **Uso de LaTeX** | ✅ xelatex (compilação no Colab) | ✅ pdflatex (compilação no repositório) | AcolheMente: pipeline controlada, não no Colab. |
| **Uso de abnTeX2** | ❌ Usa `article` (nbconvert padrão) | ✅ `\documentclass{abntex2}` no .tex canônico | "O template aproxima ABNT; o AcolheMente usa abnTeX2 nativo." |
| **Robustez tipográfica** | Média (article + pacotes ABNT via sed) | Alta (abnTeX2 nativo, 72 pp, capa, sumário, ref ABNT) | AcolheMente: qualidade tipográfica profissional. |
| **Adequação para banca** | ✅ (modelo aprovado pelo curso) | ✅ (segue o modelo + robustecimento) | "Segui o padrão aprovado; robusteci o acabamento." |
| **Reprodutibilidade** | ✅ (executa no Colab) | ✅ (notebook executa no Colab; PDF reproduz no repositório) | Ambos reprodutíveis; AcolheMente em dois caminhos complementares. |
| **Limitações** | Pipeline frágil se Colab mudar | PDF não é gerado pelo notebook sozinho | "A separação é intencional, não uma limitação." |

---

## Resumo visual

```
Template:  Notebook ──→ nbconvert --to latex ──→ .tex (article) ──→ xelatex ──→ PDF
                                      ↑ tudo dentro do Colab ↑

AcolheMente:  Notebook ──→ nbconvert --to html ──→ HTML (preview)
              .tex (abntex2) ──→ pdflatex + bibtex ──→ PDF (72 pp)
                                ↑ repositório local ↑
```

---

*Tabela preparada em 2026-06-06. Nenhum artefato consolidado foi modificado.*
