# Engenharia Reversa do Template — Resposta_Trabalho_Trilha_I.ipynb

> **Data:** 2026-06-07

---

## Estrutura do template

| Célula | Tipo | Função |
|--------|------|--------|
| 0 | markdown | Capa/titlepage com logo IF Goiano (`logo_urutai.png`) |
| 1 | markdown | Folha de rosto (segundo titlepage) |
| 2–5 | markdown | Seções acadêmicas: Apresentação, Introdução, Metodologia, Implementação |
| 6–7 | code | `%%writefile` para scripts auxiliares |
| 8–26 | misto | Resultados, gráficos, tabelas, evolução, conclusões |
| 27–28 | code | Células vazias (espaço reservado) |
| 29 | code | `drive.mount('/content/drive')` (Google Drive) |
| 30 | code | `apt-get install texlive texlive-xetex texlive-latex-extra pandoc` |
| 31 | code | `wget logo_urutai.png` do site do IF Goiano |
| 32 | code | `%%writefile referencias.bib` — referências BibTeX |
| 33 | markdown | `\newpage` — separador |
| 34 | code | Copia notebook para `/content/` |
| 35 | code | **Pipeline completa de geração de PDF** (ver abaixo) |
| 36–38 | code | Células vazias |

---

## Pipeline de geração de PDF (célula 35)

### Passo a passo

1. **Configuração de data:** monta string com data em português
2. **Limpeza do notebook:** remove células que contenham `nbconvert`, `xelatex`, `referencias.bib`
3. **Salva notebook limpo:** `temp_limpo.ipynb`
4. **nbconvert → LaTeX:** `jupyter nbconvert --to latex temp_limpo.ipynb --no-input --output=Resposta_Trabalho_Trilha-I`
5. **Remove `\maketitle`:** evita capa duplicada (capa é do notebook)
6. **Remove `nocaption`:** permite legendas em figuras/tabelas
7. **Substitui `\today`:** por data formatada em português
8. **Injeta pacotes antes de `\begin{document}`:**
   - `babel[brazil]` — tradução automática
   - `float`, `url`, `booktabs` — formatação
   - `caption` — legendas ABNT (tabela topo, figura embaixo)
   - `listings`, `xcolor` — blocos de código coloridos
   - Traduções: Sumário, Lista de Figuras/Tabelas, Figura, Tabela, Referências
   - `\renewcommand{\familydefault}{\sfdefault}` — fonte sans-serif global
9. **Injeta sumário e listas:** `\tableofcontents`, `\listoffigures`, `\listoftables` após a segunda `\end{titlepage}`
10. **Ordena referências antes de apêndices:** separa `\appendix`, injeta `\bibliographystyle{plain}` + `\bibliography{referencias}` antes
11. **Salva `.tex` final**
12. **Limpa auxiliares antigos:** `.aux`, `.bbl`, `.blg`, `.pdf`, `.toc`, `.lof`
13. **Compila:**
    - `xelatex -interaction=batchmode` (1ª passagem)
    - `bibtex` (referências)
    - `xelatex -interaction=batchmode` (2ª passagem)
    - `xelatex -interaction=batchmode` (3ª passagem)
14. **Resultado:** PDF final gerado

### Características chave

- **Classe LaTeX:** `article` (gerada pelo nbconvert, mantida)
- **Compilador:** xelatex (suporte nativo a UTF-8)
- **NÃO usa abnTeX2:** nenhum `\documentclass{abntex2}` ou `abntex2cite`
- **Tradução manual:** via `\renewcommand`
- **Capa:** LaTeX raw em célula markdown do notebook (2 titlepages)
- **Logo:** baixada do site do IF Goiano via wget
- **Bibliografia:** escrita via `%%writefile` no notebook

### Modelo conceitual

```
Notebook (.ipynb)
    ↓ [remove células técnicas]
    ↓ [jupyter nbconvert --to latex --no-input]
.tex intermediário (article)
    ↓ [Python/sed: pacotes, traduções, sumário, bib]
.tex ajustado
    ↓ [xelatex × 3 + bibtex × 1]
PDF final
```

---

*Relatório gerado em 2026-06-07. Nenhum artefato consolidado foi modificado.*
