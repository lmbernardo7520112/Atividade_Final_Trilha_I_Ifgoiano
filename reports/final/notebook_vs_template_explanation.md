# Notebook vs Template — Explicação Completa

> **Data:** 2026-06-06
> **Escopo:** Comparação entre `Resposta_Trabalho_Trilha_I.ipynb` (template) e `Trabalho_Trilha_I_AcolheMente_PB.ipynb` (AcolheMente v3_3)

---

## Tarefa 1 — Inventário comparativo dos notebooks

### Dados forenses

| Atributo | Template | AcolheMente v3_3 |
|----------|----------|------------------|
| **Caminho** | `./Resposta_Trabalho_Trilha_I.ipynb` | `academic_abntex2_attempt_v3_3/outputs/Trabalho_Trilha_I_AcolheMente_PB.ipynb` |
| **SHA256** (16) | `95e7c2be157caed4` | `d266fe637ff50e1d` |
| **Tamanho** | 85.586 bytes | 73.188 bytes |
| **Células** | 39 (18 md + 21 code) | 29 (13 md + 16 code) |
| Colab metadata | ✅ | ✅ |
| Capa LaTeX | ✅ (`\Large`, `\maketitle`) | ✅ (`\Large`, capa institucional) |
| logo_urutai | ✅ | ✅ |
| `%%writefile` | ✅ | ✅ |
| Scripts apêndice | ✅ | ✅ (6 scripts Python) |
| Bibliografia `.bib` | ✅ | ✅ |
| **nbconvert** | ✅ (`--to latex`) | ✅ (`--to html`, alternativa) |
| **xelatex** | ✅ (executa xelatex 3×) | ❌ |
| **bibtex** | ✅ (executa bibtex) | ❌ |
| **apt-get texlive** | ✅ | ✅ (presente mas para contexto) |
| **abnTeX2** | ❌ | ❌ (no notebook) |
| **documentclass abnTeX2** | ❌ | ❌ (no notebook) |
| Conversão para HTML | ❌ | ✅ (`nbconvert --to html`) |
| Conversão para PDF | ✅ (via xelatex) | ✅ (alternativa comentada) |
| Exportação LaTeX | ✅ (`nbconvert --to latex`) | ✅ (alternativa) |
| Outputs executados | ✅ | ✅ |
| Oráculo | ❌ | ✅ |
| `inferir_acolhimento` | ❌ | ✅ |
| R1–R6 | ❌ | ✅ |
| 64 cenários | ✅ | ✅ |
| LGPD/ECA/PSE | ❌/❌/❌ | ✅/✅/✅ |

---

## Tarefa 2 — O notebook AcolheMente faz exatamente o que o template faz?

### 2.1. Em que sentido ele segue o template

1. **Usa notebook como artefato acadêmico:** o notebook é o veículo principal de entrega executável da Trilha I, contendo texto, código, resultados e referências.
2. **Organiza seções acadêmicas:** Apresentação, Introdução/Problema, Metodologia, Implementação, Resultados, Evolução Futura, Conclusão — mesma lógica do template.
3. **Mantém células de código didáticas:** mostra implementação ao vivo, não apenas texto.
4. **Usa `%%writefile` para scripts auxiliares:** 6 apêndices Python (simbolos, regras, motor, cenários, grafos, tabelas) escritos via `%%writefile`, exatamente como o template faz com seus auxiliares.
5. **Mantém capa institucional com logo IF Goiano:** `logo_urutai.png` em LaTeX dentro de célula markdown.
6. **Inclui referências bibliográficas:** arquivo `referencias.bib` escrito via `%%writefile`, exatamente como no template.
7. **Mantém a lógica "notebook executável + relatório acadêmico":** o notebook pode ser aberto no Colab e executado de ponta a ponta.

### 2.2. Em que sentido ele NÃO faz exatamente a mesma coisa

1. **O template gera PDF diretamente dentro do Colab:**
   - Instala texlive via `apt-get`
   - Usa `jupyter nbconvert --to latex` para gerar `.tex` intermediário
   - Edita o `.tex` com Python/sed para inserir pacotes, traduções, sumário
   - Compila com `xelatex` 3 vezes + `bibtex` 1 vez
   - Produz PDF final sem sair do Colab

2. **O AcolheMente v3_3 separa notebook e PDF final:**
   - O notebook contém `nbconvert --to html` como alternativa leve de exportação/preview
   - O PDF abnTeX2 final (72 páginas) foi gerado por pipeline separada no repositório (`scripts/build_abntex2_from_colab.py` → pdflatex + bibtex sobre `main_acolhemente_abntex2.tex`)
   - O notebook é fonte acadêmica e evidência de implementação; o PDF é artefato de composição tipográfica final

3. **O template usa `documentclass article` (via nbconvert):**
   - O nbconvert gera `.tex` com `\documentclass[11pt]{article}`
   - O template adiciona pacotes ABNT (babel, float, caption) via sed/Python
   - Mas **não** usa `\documentclass{abntex2}` — apenas aproxima o formato

4. **O AcolheMente usa abnTeX2 nativo:**
   - O `.tex` da v3_3 declara `\documentclass[12pt,openright,oneside,a4paper,english,brazil]{abntex2}`
   - Usa `\usepackage[alf]{abntex2cite}` e `\bibliographystyle{abntex2-alf}`
   - Isso é abnTeX2 genuíno, não aproximação

### 2.3. Conclusão

> **O notebook AcolheMente segue a metodologia e o espírito do template da Trilha I, mas não replica literalmente sua pipeline técnica simplificada.** O template gera PDF inteiramente dentro do Colab via nbconvert → article → xelatex. O AcolheMente mantém o notebook como artefato executável e acadêmico, mas produz o PDF final via pipeline abnTeX2 nativa controlada no repositório.

---

## Tarefa 3 — O que o template Resposta_Trabalho_Trilha_I.ipynb faz

### Pipeline passo a passo do template

| Passo | O que faz | Como faz |
|-------|-----------|----------|
| 1 | Capa/folha de rosto | LaTeX em célula markdown (`\Large`, `\includegraphics{logo_urutai.png}`) |
| 2 | Seções acadêmicas | Markdown/LaTeX: Introdução, Metodologia, Implementação, Resultados, Evolução |
| 3 | Scripts auxiliares | `%%writefile` para Python/auxiliares |
| 4 | Execução de código | Gera resultados, tabelas, gráficos |
| 5 | Logomarca | Baixa `logo_urutai.png` do Google Drive |
| 6 | Bibliografia | `%%writefile referencias.bib` |
| 7 | **Instala TeX** | `apt-get install texlive texlive-xetex texlive-latex-extra pandoc` |
| 8 | **Copia notebook** | `cp` para `/content/` |
| 9 | **Limpa células técnicas** | Remove células com "nbconvert", "xelatex", "referencias.bib" do JSON |
| 10 | **nbconvert → LaTeX** | `jupyter nbconvert --to latex temp_limpo.ipynb --no-input` |
| 11 | **Edita .tex** | Python/sed para inserir: babel, float, booktabs, caption, listings, xcolor, traduções, sumário, lista de figuras/tabelas |
| 12 | **1ª compilação** | `xelatex -interaction=batchmode` |
| 13 | **bibtex** | `bibtex Resposta_Trabalho_Trilha-I` |
| 14 | **2ª compilação** | `xelatex` (atualiza sumário e referências) |
| 15 | **3ª compilação** | `xelatex` (resolve referências cruzadas) |
| 16 | **PDF final** | Produzido no Colab |

### Modelo conceitual do template

```
Notebook (.ipynb)
    ↓ [limpa células técnicas]
    ↓ [jupyter nbconvert --to latex]
.tex intermediário (article)
    ↓ [Python/sed: pacotes, traduções, sumário]
.tex ajustado
    ↓ [xelatex × 3 + bibtex × 1]
PDF final
```

**Observação crucial:** a `documentclass` gerada pelo nbconvert é `article`, não `abntex2`. O template aproxima o resultado visual do padrão ABNT injetando pacotes, mas **não produz documento abnTeX2 nativo**.

---

## Tarefa 4 — Episódio de confusão sobre abnTeX2

### O que é abnTeX2

abnTeX2 não é um pacote LaTeX — é uma **classe de documento** (`\documentclass{abntex2}`). A diferença é fundamental:

| Abordagem | Comando | O que produz |
|-----------|---------|-------------|
| **Incorreta** | `\usepackage{abntex2}` | Erro de compilação ou efeito nulo |
| **Correta** | `\documentclass{abntex2}` | Documento nativo ABNT NBR 14724 |

### O que o template faz (e o que NÃO é abnTeX2)

O template usa `nbconvert --to latex`, que gera `.tex` com `\documentclass[11pt]{article}`. Depois injeta pacotes como `babel`, `caption`, `listings` para **aproximar** o visual do padrão ABNT. Mas isso **não é abnTeX2**.

### O que o AcolheMente v3_3 faz (e o que É abnTeX2)

O `.tex` da v3_3 declara:

```latex
\documentclass[12pt,openright,oneside,a4paper,english,brazil]{abntex2}
```

Com:
- `\usepackage[alf]{abntex2cite}` — citações autor-data ABNT
- `\bibliographystyle{abntex2-alf}` — estilo bibliográfico ABNT
- `\imprimircapa`, `\imprimirfolhaderosto` — comandos nativos abnTeX2

### A confusão

A confusão surgiu porque o conceito de "usar abnTeX2" foi inicialmente interpretado como "adicionar pacotes ABNT ao .tex gerado pelo nbconvert". Mas abnTeX2 exige controle da `documentclass` desde o início. O nbconvert não oferece esse controle — ele sempre gera `article`. Para usar abnTeX2 genuíno, é necessário escrever ou gerar o `.tex` independentemente do nbconvert.

---

## Tarefa 5 — Por que NÃO rodar abnTeX2 completo diretamente no Colab?

### Razões técnicas

1. **Ambiente temporário:** o Colab descarta tudo ao desconectar. Uma instalação completa de TeX/abnTeX2 precisa ser refeita a cada sessão.
2. **Instalação pesada e lenta:** `texlive-full` pode ter 4–5 GB. Mesmo `texlive-xetex` demora vários minutos.
3. **abnTeX2 não pré-instalado:** o pacote abnTeX2 e seus estilos (`abntex2cite`, fontes, classes) frequentemente não estão disponíveis nos repositórios padrão do Colab.
4. **Falhas silenciosas:** compilações complexas com xelatex/bibtex + figuras + listings + apêndices podem falhar por codificação UTF-8, fontes ausentes, caminhos quebrados ou permissões.
5. **Fragilidade acumulada:** cada etapa da pipeline (limpar notebook → nbconvert → sed → xelatex × 3 → bibtex) é um ponto de falha. No template simples funciona; para 72 páginas com abnTeX2 nativo, a probabilidade de falha é alta.

### Razões pedagógicas

6. **Notebook deve permanecer leve:** o notebook é avaliado como artefato executável e didático. Se a compilação LaTeX complexa falhar, o avaliador pode ficar sem notebook E sem PDF.
7. **Separação de responsabilidades:** o notebook demonstra a lógica e a reprodutibilidade; o PDF demonstra a qualidade formal. Misturar os dois num único processo frágil é arriscado.

### Solução adotada

> "O notebook preserva a lógica de entrega executável da Trilha I; o PDF abnTeX2 preserva a qualidade formal acadêmica. A robustez foi obtida separando execução didática e composição tipográfica final."

---

## Tarefa 6 — Como o AcolheMente evitou o problema

### Pipeline real da v3_3

| # | Pergunta | Resposta | Evidência |
|---|----------|---------|-----------|
| 1 | O notebook final foi gerado por script? | **Sim** | `scripts/generate_notebook.py` gera o `.ipynb` |
| 2 | Qual script gerou o notebook? | `generate_notebook.py` | Lê apêndices de `appendices/`, monta células, salva `.ipynb` |
| 3 | O PDF final foi gerado a partir do notebook ou do .tex? | **A partir do .tex canônico** | `latex/main_acolhemente_abntex2.tex` (72 páginas) |
| 4 | Qual .tex foi usado? | `latex/main_acolhemente_abntex2.tex` | `\documentclass{abntex2}`, header "v3.3" |
| 5 | Qual .bib foi usado? | `latex/referencias.bib` | Confirmado em `build_abntex2_from_colab.py` |
| 6 | Qual script executou a compilação? | `scripts/build_abntex2_from_colab.py` orquestrado por `scripts/build_abntex2_local.sh` | Chama pdflatex + bibtex |
| 7 | O PDF final foi gerado com abnTeX2 real? | **Sim** | `\documentclass[12pt,...]{abntex2}`, `\usepackage[alf]{abntex2cite}` |
| 8 | Houve xelatex/bibtex? | **pdflatex + bibtex** (não xelatex) | Log: "pdfTeX, Version 3.141592653" |
| 9 | O PDF final de 72 páginas corresponde ao main_acolhemente_abntex2.pdf? | **Sim** | `latex/main_acolhemente_abntex2.pdf` = 72 pp, 1.6MB |
| 10 | O notebook gera diretamente o PDF final? | **Não** | O notebook é artefato acadêmico/fonte; o PDF é gerado por pipeline LaTeX separada |

### Diagrama da pipeline real

```
appendices/*.py ──┐
                  ├──→ generate_notebook.py ──→ notebook (.ipynb)
                  │         ↓ [preview/entrega Colab]
                  │    nbconvert --to html (alternativa leve)
                  │
figures/*.png ────┤
_build/*.tex ─────┼──→ main_acolhemente_abntex2.tex
latex/referencias.bib ┘         ↓
                          pdflatex + bibtex
                               ↓
                    main_acolhemente_abntex2.pdf (72 pp, abnTeX2)
```

---

## Tarefa 7 — O que o notebook final faz, passo a passo

### Bloco 1 — Apresentação institucional (célula 0)
- Capa com logo IF Goiano (logo_urutai.png)
- Nome do aluno, curso, turma
- Título do trabalho: "AcolheMente Escolar PB"

### Bloco 2 — Problema e justificativa (células 1–2)
- Saúde mental adolescente no Brasil
- Dados da PeNSE/IBGE
- Escola pública da Paraíba como primeiro contato institucional
- Necessidade de fluxo formal e governado de acolhimento

### Bloco 3 — Metodologia (células 3–4)
- Sistema Baseado em Conhecimento (SBC)
- Lógica proposicional e inferência por resolução
- Por que não ML/DL neste contexto
- Arquitetura de dados: TIER_A (PeNSE), TIER_B (sintéticos), TIER_C (benchmark)

### Bloco 4 — Representação do conhecimento (células 5–8)
- 7 variáveis: E, B, V, S, C, I, A
- 6 entradas (4 nucleares + 2 contextuais) + 1 saída inferida
- 2^6 = 64 cenários
- `%%writefile simbolos_acolhemente.py`
- `%%writefile regras_acolhemente.py`

### Bloco 5 — Implementação (células 9–14)
- `%%writefile motor_resolucao_acolhemente.py` — motor pedagógico
- Regras R1–R6 em forma implicativa e CNF
- Resolução por `_resolve()` e `inferir_por_resolucao()`
- Geração de tabelas LaTeX
- Geração de grafos de explicabilidade

### Bloco 6 — Validação (células 15–18)
- `%%writefile cenarios_sinteticos_acolhemente.py`
- Loop exaustivo `itertools.product([0,1], repeat=6)`
- Oráculo independente `oraculo_acolhimento()`
- CSV `validacao_exaustiva_64.csv`: 64 linhas, 0 falhas
- Guardrails verificados: C e I isolados → NÃO

### Bloco 7 — Resultados (células 19–22)
- Gráficos de ativação de regras
- Baseline comparativo
- 50/64 acionam A, 14/64 não acionam

### Bloco 8 — Governança e explicabilidade (células 23–25)
- LGPD, ECA, PSE
- Não-diagnóstico, não-ranking, human-in-the-loop
- Grafos de proveniência e governança
- Pseudonimização projetada para piloto futuro

### Bloco 9 — Conclusão e evolução (célula 20 — markdown)
- Limites do trabalho
- Perspectivas futuras
- Piloto institucional governado

### Bloco 10 — Referências e exportação (células 26–28)
- `%%writefile referencias.bib` — referências em BibTeX
- Cópia do notebook para `/content/` (Colab)
- `jupyter nbconvert --to html` — alternativa leve para preview

---

## Tarefa 8 — Elucidação do PDF → HTML

### O que foi encontrado

As únicas menções a "html" no projeto são:

| Local | Conteúdo | Função |
|-------|----------|--------|
| Notebook célula 28 | `!jupyter nbconvert --to html "Trabalho_Trilha_I_AcolheMente_PB.ipynb"` | Exportação alternativa leve para preview/entrega Colab |
| Referências bibliográficas | URLs do IBGE (`.html`) | Endereços web em citações |
| `generate_notebook.py` L611 | Gera célula com `nbconvert --to html` | Script que monta o notebook |

### Respostas

| # | Pergunta | Resposta |
|---|----------|---------|
| 1 | Existe conversão PDF→HTML? | **Não.** Existe conversão notebook→HTML (`nbconvert --to html`), que é diferente. |
| 2 | Onde ela aparece? | Célula 28 do notebook AcolheMente (e no `generate_notebook.py` que gera essa célula) |
| 3 | Para que foi usada? | **Preview/entrega alternativa leve.** Gera versão HTML do notebook para visualização rápida no Colab. |
| 4 | Foi usada para gerar o PDF final? | **Não.** O PDF final foi gerado por pdflatex + bibtex sobre `main_acolhemente_abntex2.tex`. |
| 5 | Relação com nbconvert? | **Sim** — é nbconvert `--to html`, não `--to latex`. Diferente da pipeline do template (que usa `--to latex`). |
| 6 | Relação com abnTeX2? | **Nenhuma.** abnTeX2 é compilado por pdflatex; o HTML é gerado por nbconvert separadamente. |

> **Conclusão:** `nbconvert --to html`, quando aparece, é etapa auxiliar de exportação/preview no Colab. Não é a etapa que gera o PDF final acadêmico. A geração do PDF abnTeX2 ocorre pela compilação do `.tex` com pdflatex + bibtex, em pipeline completamente independente.

---

*Relatório gerado em 2026-06-06. Nenhum artefato consolidado foi modificado.*
