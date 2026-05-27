# AcolheMente Escolar PB - Scorecard Academico v2.2

## Resultado Geral

| # | Criterio | Nota | Evidencia |
|---|----------|------|-----------|
| 1 | Classe abnTeX2 | 10.0 | `\documentclass[...]{abntex2}` |
| 2 | Estilo ABNT (abntex2-alf) | 10.0 | `abntex2cite` + `abntex2-alf` |
| 3 | Capa institucional | 10.0 | IF Goiano, Campus Urutai, logo |
| 4 | Sumario automatico | 10.0 | `\tableofcontents*` sem "Sumario" como item |
| 5 | Capitulos do template | 10.0 | 15 capitulos, todos via `\chapter{}` |
| 6 | Numeracao automatica por capitulos | 10.0 | Nenhum 0.x, nenhum .x em apendices, nenhum 14.1 |
| 7 | Estrutura abnTeX2 por capitulos e apendices | 10.0 | `\chapter` + `\begin{apendicesenv}` + `\partapendices` |
| 8 | Citacoes no corpo | 10.0 | 14+ `\cite{}` e `\citeonline{}` |
| 9 | Referencias BibTeX | 10.0 | 10 entradas completas |
| 10 | Texto fluido (nao listas) | 9.5 | Paragrafos densos; 1 lista em objetivos |
| 11 | Profundidade academica | 9.5 | ~12.000 palavras, fundamentacao robusta |
| 12 | Apendices com codigo | 10.0 | 6 apendices via `\lstinputlisting` |
| 13 | Explicabilidade documentada | 10.0 | Capitulo 12 + Apendice E |
| 14 | Discussao critica | 9.5 | Limitacoes, riscos, medicalizacao |
| 15 | Perspectiva de Evolucao fluida | 10.0 | 10 paragrafos corridos, sem subsections |
| 16 | Conformidade LGPD/ECA/PSE | 10.0 | Reforcada em multiplos capitulos |
| 17 | Declaracao de testes precisa | 10.0 | 42 testes v2 declarados; sem 107 inflado |
| 18 | **Qualidade dos apendices e renderizacao de simbolos** | **10.0** | Nenhum glifo corrompido; todos scripts ASCII puro; 6/6 py_compile OK |
| 19 | **Remocao de bordas visuais de links** | **10.0** | `\hypersetup{hidelinks}` presente; pdfborder={0 0 0} |
| 20 | **Precisao biografica** | **10.0** | CD concluido corretamente declarado |

**Media: 9.93 / 10.0** (minimo exigido: 9.3)
**Menor nota: 9.5** (minimo exigido: 8.8)

## Metricas do PDF v2.2

| Metrica | v2.0 | v2.1 | v2.2 |
|---------|------|------|------|
| Paginas | 35 | 45 | **45** |
| Tamanho | 197 KB | 196 KB | **196 KB** |
| Numeracao 0.x | PRESENTE | Ausente | Ausente |
| Apendices .x | PRESENTE | Ausente | Ausente |
| Subsection 14.1 | PRESENTE | Ausente | Ausente |
| "Sumario" no TOC | PRESENTE | Ausente | Ausente |
| "107 testes" | PRESENTE | Corrigido | Corrigido |
| Perspectiva fragmentada | 2 subsections | Fluida | Fluida |
| Glifos corrompidos | NAO TESTADO | NAO TESTADO | **LIMPO** |
| Bordas de link | VERMELHAS | NAO TESTADO | **REMOVIDAS** |
| py_compile | NAO TESTADO | NAO TESTADO | **6/6 OK** |

## Testes Automatizados v2.2

| Suite | v2.0 | v2.1 | v2.2 |
|-------|------|------|------|
| Contract (abnTeX2) | 12 | 16 | 16 |
| Structure (academico) | 20 | 23 | 23 |
| PDF Quality | 10 | 16 | **22** |
| **Total** | **42** | **55** | **61** |

## Novos testes em v2.2

1. `test_no_corrupted_glyph_n_caron` - PDF sem glifo n-caron
2. `test_no_corrupted_glyph_hookrightarrow` - PDF sem hookrightarrow
3. `test_no_replacement_char` - PDF sem replacement char
4. `test_no_file_protocol` - PDF sem file:///
5. `test_tex_has_hypersetup` - .tex contem \hypersetup
6. `test_tex_has_hidelinks_or_pdfborder` - .tex contem hidelinks

## Criterios de Aceite v2.2

- [x] Nada fora de `academic_abntex2_attempt_v2/` foi alterado
- [x] PDF usa abnTeX2
- [x] Sumario nao mostra bordas vermelhas
- [x] Sumario nao contem 0.x
- [x] Apendices nao aparecem como .x
- [x] PDF nao contem n-caron
- [x] PDF nao contem hookrightarrow
- [x] PDF nao contem References em ingles
- [x] Scripts dos apendices passam em py_compile
- [x] Citacoes e BibTeX continuam funcionando
- [x] Perspectiva de Evolucao permanece fluida
- [x] 61 testes passam
- [x] Scorecard nao infla notas sem evidencia
