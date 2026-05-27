# Engenharia Reversa: Template e Resposta da Trilha I

## 1. Estrutura do Template (16 células)

| # | Tipo | Conteúdo |
|---|------|----------|
| 0–2 | markdown | Capas LaTeX (titlepage) com logo IF Goiano |
| 3 | markdown | Apresentação do Aluno e Contexto |
| 4 | markdown | Introdução e Definição do Problema |
| 5 | markdown | Metodologia e Escolha da Técnica de IA |
| 6 | markdown | Implementação (placeholder) |
| 7 | markdown | Resultados e Comparações |
| 8 | markdown | Perspectiva de Evolução |
| 9 | markdown | Conclusão |
| 10 | markdown | Apêndices (appendix LaTeX) |
| 11–12 | code | Referências BibTeX e build |
| 13–15 | code | Cópia, instalação, conversão |

**Padrões observados no Template:**
- Capa em LaTeX puro (`\begin{titlepage}`)
- Logo via `\includegraphics` apontando para `/content/logo_urutai.png`
- Texto em markdown com citações `\cite{}`
- Seções sem numeração manual
- Apêndices com `\appendix` e `\lstinputlisting`
- BibTeX gerado via `%%capture` + `open()` Python
- Build via `xelatex` + `bibtex` + `xelatex` + `xelatex`

## 2. Estrutura da Resposta (39 células)

| # | Tipo | Conteúdo |
|---|------|----------|
| 0–1 | markdown | Duas versões de capa LaTeX |
| 2 | markdown | Apresentação do Aluno (blockquote) |
| 3 | markdown | Introdução e Definição do Problema |
| 4 | markdown | Metodologia e Escolha da Técnica |
| 5 | markdown | Implementação da Solução |
| 6 | code | `%%writefile logica_proposicional.py` (Apêndice A) |
| 7 | code | `%%writefile inferencia_por_resolucao.py` (Apêndice B) |
| 8 | markdown | Resultados e Comparações |
| 9 | code | `%%writefile simbolos_consultorio.py` (Apêndice C) |
| 10 | markdown | Avaliação Larga Escala |
| 11 | code | `%%writefile avaliacao_larga_escala.py` (Apêndice D) |
| 12 | markdown | Geração de Gráficos |
| 13 | code | `%%writefile grafico_matrizes_confusao.py` (Apêndice E) |
| 14 | code | Execução local do gráfico |
| 15 | markdown | Figura: Matrizes de confusão |
| 16 | markdown | Eficiência operacional |
| 17 | code | `%%writefile grafico_eficiencia.py` (Apêndice F) |
| 18 | code | Execução local do gráfico |
| 19 | markdown | Figura: Tempo de execução |
| 20 | markdown | Tabela de métricas |
| 21 | code | `%%writefile tabela_metricas.py` (Apêndice G) |
| 22 | code | Execução local de métricas |
| 23 | markdown | Tabela LaTeX |
| 24 | markdown | Análise Crítica |
| 25 | markdown | Perspectiva de Evolução |
| 26 | markdown | Conclusões |
| 27–28 | code | Vazias |
| 29 | code | Google Drive mount |
| 30 | code | Instalação TeX |
| 31 | code | Download da logomarca |
| 32 | code | Geração do .bib |
| 33 | markdown | Apêndices com `\appendix` + `\lstinputlisting` |
| 34 | code | Cópia do notebook |
| 35 | code | Build script completo (Python + sed + xelatex) |
| 36–38 | code | Vazias |

## 3. Padrões-Chave Extraídos

### 3.1 Uso de `%%writefile`
- Cada script Python é salvo via `%%writefile nome.py`
- Precedido por `%%capture` para ocultar output
- Scripts ficam em `/content/` (Colab)

### 3.2 Capa LaTeX
- `\begin{titlepage}` com `\centering`
- Logo: `\includegraphics[width=0.15\textwidth]{logo_urutai.png}`
- Hierarquia: IF Goiano → Campus Urutaí → Núcleo → Especialização
- Nome do aluno em `\MakeUppercase`
- Título em bold uppercase
- Data com `\today`

### 3.3 Apêndices
- `\appendix` seguido de `\section{Título}`
- `\lstinputlisting[language=Python]{arquivo.py}`
- `\clearpage` entre apêndices
- Legendas em cabeçalho

### 3.4 Build Script
- Filtra células técnicas do notebook
- Converte para LaTeX via `jupyter nbconvert --to latex --no-input`
- Injeta pacotes (babel, float, booktabs, caption, listings, xcolor)
- Define `\lstset{}` com cores e formatação
- Renomeia Figure→Figura, Table→Tabela, References→Referências
- Compila com xelatex 3x + bibtex 1x

### 3.5 BibTeX
- Gerado via Python `open()` + `f.write(r"""...""")`
- Estilo não explicitado no Resposta (usa abntex2-alf no Template)

## 4. Lacunas do PDF Atual (Consolidado)

1. Usa `nbconvert --to pdf` direto, não abnTeX2
2. Não tem `\documentclass{abntex2}`
3. Não tem `abntex2cite`
4. Não tem `\bibliographystyle{abntex2-alf}`
5. Tabelas longtable quebravam com `\real{}`
6. Numeração de seções manual + automática = duplicada
7. Código extenso no corpo principal
8. Seção de Evolução fragmentada em muitas subseções
9. Capa não segue fielmente o modelo institucional

## 5. Plano Célula por Célula da Nova Tentativa

| # | Tipo | Conteúdo |
|---|------|----------|
| 0 | code | Google Drive mount (Colab) |
| 1 | code | Instalação TeX (apt-get texlive + abntex2) |
| 2 | code | Download logomarca |
| 3 | code | `%%writefile latex/referencias.bib` |
| 4 | code | `%%writefile appendices/simbolos_acolhemente.py` |
| 5 | code | `%%writefile appendices/regras_acolhemente.py` |
| 6 | code | `%%writefile appendices/motor_resolucao_acolhemente.py` |
| 7 | code | `%%writefile appendices/cenarios_sinteticos_acolhemente.py` |
| 8 | code | `%%writefile appendices/grafo_explicabilidade_acolhemente.py` |
| 9 | code | `%%writefile appendices/gerar_tabelas_resultados.py` |
| 10 | markdown | Capa LaTeX (titlepage) |
| 11 | markdown | Apresentação do Aluno |
| 12 | markdown | Introdução |
| 13 | markdown | Definição do Problema e Objetivos |
| 14 | markdown | Fundamentação Metodológica |
| 15 | markdown | Dados e Governança |
| 16 | markdown | Representação do Conhecimento |
| 17 | markdown | Base de Conhecimento e Regras |
| 18 | markdown | Conversão CNF |
| 19 | markdown | Inferência por Resolução |
| 20 | markdown | Implementação Computacional |
| 21 | markdown | Resultados e Comparações |
| 22 | markdown | Explicabilidade |
| 23 | markdown | Discussão Crítica |
| 24 | markdown | Perspectiva de Evolução |
| 25 | markdown | Conclusão |
| 26 | markdown | Apêndices (LaTeX) |
| 27 | code | `%%writefile latex/main_acolhemente_abntex2.tex` |
| 28 | code | `%%writefile scripts/build_abntex2_from_colab.py` |
| 29 | code | `%%writefile scripts/validate_abntex2_outputs.py` |
| 30 | code | Execução do build |
| 31 | code | Execução da validação |
