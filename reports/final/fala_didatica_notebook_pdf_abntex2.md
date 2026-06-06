# Fala Didática — Notebook, PDF e abnTeX2 para Apresentação

> **Duração estimada:** 3–5 minutos
> **Momento:** quando a banca perguntar sobre a relação entre notebook e PDF, ou durante a seção de reprodutibilidade/metodologia

---

## Fala completa (versão para treinar em voz alta)

---

**[Início — 30 segundos]**

"Antes de detalhar os resultados, quero explicar brevemente como o trabalho está organizado entre o notebook e o PDF, porque essa decisão foi técnica e deliberada."

---

**[Contexto do template — 45 segundos]**

"Eu segui o padrão pedagógico do template da Trilha I, que organiza o trabalho em notebook com células textuais, código, apêndices e geração de artefatos. O template original inclusive gera o PDF diretamente dentro do Colab: ele instala o LaTeX no ambiente temporário, converte o notebook para um arquivo `.tex` intermediário usando nbconvert, ajusta formatação e compila com xelatex e bibtex. Tudo dentro do próprio notebook."

---

**[O que o AcolheMente preserva — 30 segundos]**

"O notebook AcolheMente preserva essa mesma lógica: ele tem capa institucional, texto acadêmico, células de código executáveis, apêndices salvos com `%%writefile`, referências bibliográficas — e pode ser aberto e executado de ponta a ponta no Colab. Ele demonstra a lógica, a implementação e a reprodutibilidade do motor de inferência."

---

**[O que mudou e por quê — 60 segundos]**

"Contudo, para alcançar um acabamento acadêmico mais robusto, especialmente com abnTeX2, a versão final separou o notebook executável da composição tipográfica do PDF."

"O motivo é técnico: o abnTeX2 não é apenas um pacote LaTeX — é uma classe de documento. O correto é declarar `documentclass abntex2`, não simplesmente `usepackage`. E o nbconvert, que é a ferramenta que converte notebook para LaTeX, sempre gera a classe `article`. Ou seja, para usar abnTeX2 genuíno, eu precisaria de um arquivo `.tex` escrito ou gerado independentemente do nbconvert."

"Além disso, o Colab é um ambiente temporário. Uma instalação completa do abnTeX2 com todos os estilos de citação, fontes e pacotes é pesada, demorada e pode falhar a cada sessão. Para um documento de 72 páginas com 8 figuras, 3 tabelas, 8 apêndices e referências bibliográficas, a compilação no Colab seria frágil demais."

---

**[Solução adotada — 45 segundos]**

"A solução que adotei foi separar as responsabilidades:"

"Primeiro: o notebook é o artefato executável e didático — ele demonstra que o motor funciona, que os cenários estão corretos, que a validação é exaustiva."

"Segundo: o arquivo `.tex` abnTeX2 foi escrito e mantido no repositório como documento acadêmico nativo, compilado com pdflatex e bibtex. É ele que produz o PDF final de 72 páginas."

"Terceiro: o repositório tem um script de build que orquestra essa compilação, verifica pré-requisitos e valida a saída."

---

**[Resumo — 30 segundos]**

"O notebook demonstra a lógica e a reprodutibilidade; o PDF abnTeX2 consolida o relatório formal. Não são redundantes — são complementares. O notebook mostra *que funciona*; o PDF mostra *como se reporta academicamente*."

---

**[Frase de fechamento]**

"A robustez foi obtida separando execução didática e composição tipográfica final."

---

## Versão ultracompacta (1 minuto — para se a banca não perguntar muito)

"O notebook segue o modelo pedagógico da Trilha I: capa, texto acadêmico, código, apêndices e referências, tudo executável no Colab. Mas o PDF final de 72 páginas foi gerado por um arquivo LaTeX abnTeX2 nativo, compilado com pdflatex e bibtex no repositório — não pelo notebook diretamente. A razão é técnica: o abnTeX2 exige controle da classe de documento que o nbconvert não oferece. A separação foi intencional: o notebook demonstra a lógica; o PDF consolida o relatório formal."

---

## Perguntas prováveis e respostas curtas

**"Por que não gerar o PDF direto do notebook, como no template?"**
> "O template gera PDF com classe `article` via nbconvert. Para usar abnTeX2 genuíno — com `documentclass abntex2`, citações `abntex2cite` e formatação ABNT nativa — o `.tex` precisa ser escrito independentemente do nbconvert."

**"Então o notebook não gera o PDF?"**
> "O notebook é fonte acadêmica e evidência de implementação. Ele pode gerar uma versão HTML para preview. Mas o PDF final de 72 páginas é compilado a partir de um `.tex` abnTeX2 nativo no repositório."

**"Isso é uma limitação?"**
> "É uma escolha de engenharia. A alternativa — tentar forçar abnTeX2 dentro do Colab — seria mais frágil e menos reprodutível. A separação garante que o notebook permaneça leve e executável, e que o PDF tenha qualidade tipográfica profissional."

**"O que tem a ver HTML com o PDF?"**
> "Não tem. O notebook oferece `nbconvert --to html` como alternativa leve de exportação no Colab. É para preview, não para geração do PDF acadêmico. O PDF é compilado por pdflatex + bibtex sobre o `.tex` abnTeX2."

---

*Fala preparada em 2026-06-06. Baseada na versão v3.3 do AcolheMente Escolar PB.*
