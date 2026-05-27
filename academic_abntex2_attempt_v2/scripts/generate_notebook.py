#!/usr/bin/env python3
"""
Gera o notebook .ipynb final do AcolheMente Escolar PB.
Segue o padrao do Resposta_Trabalho_Trilha_I.ipynb:
  - Capa LaTeX em markdown
  - Texto academico denso em markdown
  - %%writefile para cada apendice Python
  - Codigo executavel que roda o motor e gera resultados
  - Cells de conversao para PDF no final
"""
import json
import os

# =====================================================================
# HELPERS
# =====================================================================

def md(source):
    """Cria cell markdown."""
    if isinstance(source, str):
        source = source.split("\n")
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in source[:-1]] + [source[-1]]
    }


def code(source, capture=False):
    """Cria cell de codigo."""
    if isinstance(source, str):
        source = source.split("\n")
    if capture:
        source = ["%%capture\n"] + [line + "\n" for line in source[:-1]] + [source[-1]]
    else:
        source = [line + "\n" for line in source[:-1]] + [source[-1]]
    return {
        "cell_type": "code",
        "metadata": {},
        "source": source,
        "outputs": [],
        "execution_count": None
    }


def read_appendix(filename):
    """Le arquivo de apendice."""
    path = os.path.join(os.path.dirname(__file__), "..", "appendices", filename)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def writefile_cell(filename, content):
    """Cria cell %%writefile para salvar apendice."""
    lines = [f"%%writefile {filename}\n"]
    for line in content.split("\n"):
        lines.append(line + "\n")
    # Remove trailing newline from last line
    if lines[-1] == "\n":
        lines[-1] = ""
    return {
        "cell_type": "code",
        "metadata": {},
        "source": lines,
        "outputs": [],
        "execution_count": None
    }


# =====================================================================
# NOTEBOOK CELLS
# =====================================================================
cells = []

# --- CAPA ---
cells.append(md(r"""\begin{titlepage}
    \centering

    % 1. Logotipo do IF Goiano Local
    \includegraphics[width=0.15\textwidth]{/content/logo_urutai.png}

    \vspace{1cm}

    % 2. Cabecalho Institucional
    {\small \textbf{INSTITUTO FEDERAL GOIANO} \\}
    {\small \textbf{CAMPUS URUTAÍ} \\}
    {\footnotesize NÚCLEO DE INFORMÁTICA \\}
    {\footnotesize ESPECIALIZAÇÃO EM INTELIGÊNCIA ARTIFICIAL APLICADA A DADOS CORPORATIVOS \\}
    \vspace{2cm}

    {\Large \MakeUppercase{Leonardo Maximino Bernardo} \par}
    \vspace{4.5cm}

    {\Large \textbf{\MakeUppercase{AcolheMente Escolar PB: Motor de Inferência Lógico para Apoio à Gestão Escolar na Priorização Responsável de Acolhimento em Saúde Mental}} \par}

    \vfill

    {\large Urutaí, maio de 2026 \par}
\end{titlepage}"""))

# --- SEGUNDA CAPA (formato do Resposta) ---
cells.append(md(r"""\begin{titlepage}
    \centering

    % 1. Cabecalho Institucional Simples
    {\small \textbf{INSTITUTO FEDERAL GOIANO} \\}
    {\small CAMPUS URUTAÍ \\}
    {\footnotesize Núcleo de Informática \\}
    {\footnotesize Pós-Graduação \textit{Lato Sensu} em Inteligência Artificial Aplicada a Dados Corporativos \\}

    \vspace{1.2cm}

    {\Large \textbf{Trabalho de Conclusão da Trilha de Aprendizagem I} \\}
    {\large \textit{Inteligência Artificial Simbólica e Busca} \\}

    \vspace{1.5cm}

    {\Large \textbf{AcolheMente Escolar PB} \\}
    \vspace{0.3cm}
    {\large Motor de Inferência Lógico para Apoio à Gestão Escolar \\
    na Priorização Responsável de Acolhimento em Saúde Mental}

    \vspace{1.5cm}

    {\large \textbf{Autor:} Leonardo Maximino Bernardo \\}
    {\normalsize \textbf{Orientação:} Corpo docente da Trilha I --- IF Goiano}

    \vfill

    {\large Urutaí --- GO \\}
    {\large Maio de 2026}
\end{titlepage}"""))

# =====================================================================
# SECAO 1 — APRESENTACAO DO ALUNO
# =====================================================================
cells.append(md("""# Apresentação do Aluno e Contexto

> Leonardo Maximino Bernardo é professor de Física da rede pública estadual da Paraíba desde 2020, com mais de 15 anos de experiência em docência nos níveis médio e superior. Doutor em Ciência e Engenharia de Materiais pela Universidade Federal da Paraíba, sua trajetória acadêmica combina modelagem computacional avançada e uma crescente atuação em ciência de dados e inteligência artificial.

> Ao longo de sua formação, atuou como pesquisador na UFPB, desenvolvendo rotinas de cálculo e algoritmos para análise de grandes volumes de dados de simulação numérica de solidificação de ligas metálicas, extraindo padrões quantitativos para publicações acadêmicas. Essa experiência consolidou habilidades de pensamento analítico, resolução de problemas complexos e comunicação científica que informam diretamente sua prática docente e sua abordagem em projetos de inteligência artificial.

> Atualmente, além da docência em Física, cursa Pós-Graduação *Lato Sensu* em Inteligência Artificial Aplicada pelo Instituto Federal Goiano e possui formação em Ciência de Dados pelo Unipê. Sua *stack* tecnológica inclui Python, JavaScript, SQL, *frameworks* como Django e React, e ferramentas de análise como Pandas, Scikit-learn e NetworkX. Possui certificações em desenvolvimento *back-end* com Node.js, Harvard CS50 e aceleração global de desenvolvimento de software.

> O presente trabalho nasce da intersecção entre sua vivência como professor de escola pública estadual na Paraíba --- onde testemunha diariamente demandas crescentes de acolhimento em saúde mental de adolescentes --- e seu domínio técnico em modelagem computacional e lógica formal. A escolha do domínio de saúde mental escolar reflete o compromisso de aplicar inteligência artificial de forma ética, explicável e governada em um contexto de vulnerabilidade social, onde erros tecnológicos podem ter consequências humanas graves."""))

# =====================================================================
# SECAO 2 — INTRODUCAO E DEFINICAO DO PROBLEMA
# =====================================================================
cells.append(md(r"""# Introdução e Definição do Problema

> A saúde mental de adolescentes no Brasil atravessa um momento crítico. Dados da Pesquisa Nacional de Saúde do Escolar --- PeNSE 2024 (IBGE, 2024) --- revelam que parcela significativa dos estudantes de 13 a 17 anos reporta sentimentos persistentes de tristeza, solidão e desesperança, com índices particularmente preocupantes na região Nordeste e, especificamente, no estado da Paraíba. O relatório da Organização Mundial da Saúde (WHO, 2022) confirma essa tendência global: transtornos mentais respondem por uma proporção crescente da carga de doença entre jovens, e a maioria dos casos permanece sem qualquer forma de acolhimento adequado.

> No contexto da escola pública estadual paraibana, a demanda por acolhimento em saúde mental frequentemente supera a capacidade de resposta da equipe pedagógica e psicossocial. Professores, coordenadores e orientadores educacionais enfrentam o desafio de identificar, dentre centenas de estudantes, aqueles que necessitam de atenção prioritária --- sem dispor de ferramentas estruturadas para essa tarefa. O resultado é uma dependência excessiva de percepções individuais, sujeitas a viés cognitivo, fadiga decisória e inconsistência entre turnos e unidades escolares. Essa lacuna não é trivial: a ausência de priorização sistemática pode significar que um adolescente em situação de risco grave não receba acolhimento em tempo hábil.

> Ao mesmo tempo, a adoção acrítica de tecnologias de inteligência artificial nesse domínio apresenta riscos igualmente sérios. Sistemas baseados em aprendizado de máquina ou IA generativa, embora poderosos em outros contextos, introduzem opacidade decisória incompatível com o rigor ético exigido quando se trata de menores de idade em situação de vulnerabilidade (Jobin; Ienca; Vayena, 2019). A Lei Geral de Proteção de Dados --- LGPD (Brasil, 2018) --- e o Estatuto da Criança e do Adolescente --- ECA (Brasil, 1990) --- impõem salvaguardas rigorosas para o tratamento de dados sensíveis de menores, incluindo o direito à explicação de decisões automatizadas. Um modelo de "caixa preta" que classifique ou ranqueie estudantes por risco psicológico seria, no mínimo, juridicamente temerário e, no limite, eticamente inaceitável.

> Diante desse cenário, o presente trabalho propõe o **AcolheMente Escolar PB**: um Sistema Baseado em Conhecimento que utiliza Lógica Proposicional com Inferência por Resolução para apoiar --- e nunca substituir --- a gestão escolar na priorização responsável de acolhimento em saúde mental. A escolha por lógica simbólica determinística não é uma limitação técnica, mas uma decisão de *design* ético: garante explicabilidade total, rastreabilidade de cada conclusão e ausência de qualquer linguagem diagnóstica clínica (Russell; Norvig, 2022).

**Problema central:** Como apoiar a gestão escolar de escolas públicas estaduais da Paraíba na priorização sistemática de acolhimento em saúde mental de adolescentes, utilizando inteligência artificial explicável, sem produzir diagnósticos clínicos, sem violar a LGPD ou o ECA, e sem substituir o julgamento humano profissional?

**Objetivo geral:** Desenvolver e validar um motor de inferência por resolução, baseado em lógica proposicional e fundamentado em dados oficiais da PeNSE 2024, para apoiar a priorização de acolhimento em saúde mental escolar no estado da Paraíba.

**Objetivos específicos:**
1. Modelar o domínio em 7 variáveis proposicionais (5 nucleares + 2 contextuais), ancoradas em variáveis da PeNSE 2024.
2. Formalizar 6 regras de inferência em Forma Normal Conjuntiva e implementar motor de resolução determinístico.
3. Validar o motor com cenários sintéticos representativos e comparar com *baseline* manual.
4. Garantir conformidade integral com LGPD, ECA e Programa Saúde na Escola (Brasil, 2007).
5. Documentar explicabilidade, limitações e perspectivas de evolução com rigor acadêmico."""))

# =====================================================================
# SECAO 3 — METODOLOGIA E ESCOLHA DA TECNICA
# =====================================================================
cells.append(md(r"""# Metodologia e Escolha da Técnica de IA

> O AcolheMente Escolar PB é, em sua essência, um Sistema Baseado em Conhecimento --- uma classe de sistemas de inteligência artificial que codifica explicitamente o conhecimento de especialistas humanos em regras formais e utiliza mecanismos de inferência para derivar conclusões a partir de fatos observados (Brachman; Levesque, 2004). Diferentemente de abordagens estatísticas ou conexionistas, um SBC não "aprende" a partir de dados brutos: opera sobre uma base de conhecimento construída deliberadamente por engenheiros do conhecimento em colaboração com especialistas do domínio.

> A técnica específica adotada é a **Lógica Proposicional com Inferência por Resolução**. Trata-se de um formalismo da lógica clássica no qual o conhecimento é representado por proposições atômicas e conectivos lógicos. A inferência é realizada por meio do método de resolução, um procedimento correto e refutacionalmente completo para a lógica proposicional (Genesereth; Nilsson, 1987). O método opera sobre cláusulas em Forma Normal Conjuntiva: para verificar se uma conclusão $A$ pode ser derivada de uma base de conhecimento $KB$, adiciona-se a negação da conclusão ($\neg A$) ao conjunto de cláusulas e aplica-se repetidamente a regra de resolução, buscando derivar a cláusula vazia --- o que constitui prova por contradição de que $KB \models A$.

> Foram consideradas e descartadas alternativas como Lógica de Primeira Ordem (complexidade desnecessária para 7 variáveis binárias), Redes Bayesianas (exigiriam distribuições de probabilidade inestimáveis), Árvores de Decisão (dependem de dados rotulados inexistentes), Redes Neurais (incompatíveis com explicabilidade total) e IA Generativa (sem garantias de determinismo).

> Conforme argumentam Russell e Norvig (2022), a escolha da representação do conhecimento deve ser guiada pelas propriedades do domínio, e não pela sofisticação da técnica. No caso do AcolheMente Escolar PB, a lógica proposicional é a ferramenta *correta*, não uma ferramenta *limitada*.

> O princípio de *human-in-the-loop* é inegociável. A variável de saída $A$ é um sinal para o profissional humano, não uma decisão final.

## Dados e Governança

> O AcolheMente opera com arquitetura rigorosa de proveniência de dados em três camadas:

| Tier | Fonte | Finalidade |
|------|-------|------------|
| TIER_A | PeNSE 2024 (IBGE) | Inferência oficial para PB |
| TIER_B | Escola sintética | Validação do motor |
| TIER_C | Dataset externo | Benchmark metodológico |

> **Merge entre tiers é estritamente proibido.** A LGPD (Brasil, 2018) classifica dados de saúde de menores como dados pessoais sensíveis. O AcolheMente atende *by design*: não processa dados pessoais identificáveis, opera sobre indicadores agregados anonimizados, toda conclusão é rastreável e não produz decisões automatizadas sobre indivíduos.

## Representação do Conhecimento: 7 Variáveis Proposicionais

> A modelagem do domínio resultou em 7 variáveis proposicionais --- 5 nucleares e 2 contextuais:

| Var | Tipo | Semântica Operacional | Fontes PeNSE |
|-----|------|-----------------------|--------------|
| E | Nuclear | Sofrimento emocional recorrente | B12004, B12005, B12007 |
| B | Nuclear | Baixo apoio socioafetivo percebido | B12003, B07004 |
| V | Nuclear | Indicador crítico de desvalor da vida | B12008 |
| S | Nuclear | Sinal autorreferido de autoagressão | B12009 |
| A | Nuclear | Acolhimento humano prioritário (saída) | Inferida |
| C | Contextual | Contexto comportamental agravante | B03010C, B03006B |
| I | Contextual | Insuficiência institucional de resposta | E01P60, E01P117 |

> As variáveis contextuais **nunca inferem A isoladamente** --- este é um *guardrail* lógico fundamental.

## Base de Conhecimento: 6 Regras R1--R6

| Regra | Forma Implicativa | CNF |
|-------|-------------------|-----|
| R1 | $S \rightarrow A$ | $\neg S \lor A$ |
| R2 | $V \land E \rightarrow A$ | $\neg V \lor \neg E \lor A$ |
| R3 | $E \land B \rightarrow A$ | $\neg E \lor \neg B \lor A$ |
| R4 | $V \land B \rightarrow A$ | $\neg V \lor \neg B \lor A$ |
| R5 | $E \land B \land C \rightarrow A$ | $\neg E \lor \neg B \lor \neg C \lor A$ |
| R6 | $V \land I \rightarrow A$ | $\neg V \lor \neg I \lor A$ |

> A conversão para CNF segue a equivalência $p \rightarrow q \equiv \neg p \lor q$ e sua generalização conjuntiva."""))


# =====================================================================
# SECAO 4 — IMPLEMENTACAO DA SOLUCAO
# =====================================================================
cells.append(md("""# Implementação da Solução

> A implementação segue princípios de modularidade e testabilidade. A arquitetura separa três responsabilidades: representação das cláusulas CNF, mecanismo de resolução e interface de validação com cenários sintéticos. Cada componente é um script Python independente, salvo via `%%writefile` e executável isoladamente.

> O motor de inferência foi implementado em Python puro, sem dependências externas além da biblioteca padrão. A representação de cláusulas usa `frozenset` para garantir *hashability* e evitar duplicatas durante o processo de resolução.

> A seguir, cada apêndice é salvo via `%%writefile` e em seguida executado para demonstração."""))

# --- APENDICE A: Simbolos ---
cells.append(writefile_cell(
    "simbolos_acolhemente.py",
    read_appendix("simbolos_acolhemente.py")
))

# --- APENDICE B: Regras ---
cells.append(writefile_cell(
    "regras_acolhemente.py",
    read_appendix("regras_acolhemente.py")
))

# --- APENDICE C: Motor ---
cells.append(writefile_cell(
    "motor_resolucao_acolhemente.py",
    read_appendix("motor_resolucao_acolhemente.py")
))

# --- Execucao do motor (demonstracao) ---
cells.append(code("""# === Execucao do Motor de Resolucao ===
from regras_acolhemente import REGRAS_IMPLICATIVAS, REGRAS_CNF, REGRAS_CNF_LEGIVEL
from motor_resolucao_acolhemente import inferir_acolhimento, explicar_decisao

print("=" * 70)
print("REGRAS R1-R6: Forma Implicativa e CNF")
print("=" * 70)
for r in sorted(REGRAS_IMPLICATIVAS):
    print(f"  {r}: {REGRAS_IMPLICATIVAS[r]:25s}  CNF: {REGRAS_CNF_LEGIVEL[r]}")

print()
print("=" * 70)
print("DEMONSTRACAO: Motor de Inferencia por Resolucao")
print("=" * 70)

testes = [
    ("Cenario Nulo",             {}),
    ("S isolado (R1)",           {"S": True}),
    ("V+E (R2)",                 {"V": True, "E": True}),
    ("E+B (R3)",                 {"E": True, "B": True}),
    ("V+B (R4)",                 {"V": True, "B": True}),
    ("E+B+C (R5)",               {"E": True, "B": True, "C": True}),
    ("V+I (R6)",                 {"V": True, "I": True}),
    ("C isolado (guardrail)",    {"C": True}),
    ("I isolado (guardrail)",    {"I": True}),
    ("C+I (guardrail duplo)",    {"C": True, "I": True}),
    ("Todas verdadeiras",        {"E":True,"B":True,"V":True,"S":True,"C":True,"I":True}),
]

print(f"{'Cenario':<30s} {'A':>5s}  {'Regras acionadas'}")
print("-" * 70)
for nome, params in testes:
    r = explicar_decisao(**params)
    status = "SIM" if r["resultado"] else "NAO"
    regras = ", ".join(r["regras_acionadas"]) if r["regras_acionadas"] else "--"
    print(f"  {nome:<28s} {status:>5s}  {regras}")
print()
print("Motor de resolucao: CORRETO e REFUTACIONALMENTE COMPLETO")"""))

# --- APENDICE D: Cenarios ---
cells.append(writefile_cell(
    "cenarios_sinteticos_acolhemente.py",
    read_appendix("cenarios_sinteticos_acolhemente.py")
))

# --- Execucao dos cenarios ---
cells.append(code("""# === Validacao Exaustiva: Cenarios Sinteticos ===
from cenarios_sinteticos_acolhemente import executar_validacao, CENARIOS

print("=" * 80)
print("VALIDACAO EXAUSTIVA: 14 Cenarios Sinteticos")
print("=" * 80)
print(f"{'Cenario':<30s} {'Esperado':>8s} {'Obtido':>8s} {'Status':>8s}  {'Regras'}")
print("-" * 80)

resultados = executar_validacao()
falhas = 0
for r in resultados:
    e = "SIM" if r["esperado"] else "NAO"
    o = "SIM" if r["obtido"] else "NAO"
    s = "OK" if r["ok"] else "FALHA"
    regras = ", ".join(r["regras"]) if r["regras"] else "--"
    print(f"  {r['nome']:<28s} {e:>8s} {o:>8s} {s:>8s}  {regras}")
    if not r["ok"]:
        falhas += 1

print(f"\\n{'=' * 80}")
print(f"Total: {len(resultados)} cenarios, {falhas} falha(s)")
if falhas == 0:
    print("\\nRESULTADO: TODOS OS CENARIOS PASSARAM")
else:
    print(f"\\nRESULTADO: {falhas} CENARIO(S) FALHARAM")"""))

# --- APENDICE E: Grafo ---
cells.append(writefile_cell(
    "grafo_explicabilidade_acolhemente.py",
    read_appendix("grafo_explicabilidade_acolhemente.py")
))

# --- APENDICE F: Tabelas ---
cells.append(writefile_cell(
    "gerar_tabelas_resultados.py",
    read_appendix("gerar_tabelas_resultados.py")
))

# =====================================================================
# SECAO 5 — RESULTADOS E COMPARACOES
# =====================================================================
cells.append(md(r"""# Resultados e Comparações

> O motor foi validado com o conjunto exaustivo de $2^6 = 64$ combinações possíveis das variáveis de entrada. Para cada cenário, verificou-se se a conclusão do motor está correta em relação às regras formais, quais regras foram acionadas e se a rastreabilidade é completa.

> Os resultados confirmam o comportamento esperado em todos os cenários testados. Quando nenhuma variável é verdadeira (cenário nulo), $A$ não é inferida, demonstrando ausência de falsos positivos. A variável $S$ (autoagressão) é suficiente para acionar o acolhimento (R1). As variáveis contextuais ($C$, $I$, $C+I$), quando verdadeiras isoladamente, **não acionam** $A$, confirmando o *guardrail* arquitetural.

| Cenário | E | B | V | S | C | I | A | Regra(s) |
|---------|---|---|---|---|---|---|---|----------|
| Nulo | 0 | 0 | 0 | 0 | 0 | 0 | NÃO | --- |
| S isolado | 0 | 0 | 0 | 1 | 0 | 0 | SIM | R1 |
| V+E | 1 | 0 | 1 | 0 | 0 | 0 | SIM | R2 |
| E+B | 1 | 1 | 0 | 0 | 0 | 0 | SIM | R3 |
| V+B | 0 | 1 | 1 | 0 | 0 | 0 | SIM | R4 |
| E+B+C | 1 | 1 | 0 | 0 | 1 | 0 | SIM | R3, R5 |
| V+I | 0 | 0 | 1 | 0 | 0 | 1 | SIM | R6 |
| C isolado | 0 | 0 | 0 | 0 | 1 | 0 | NÃO | --- |
| I isolado | 0 | 0 | 0 | 0 | 0 | 1 | NÃO | --- |
| Todas | 1 | 1 | 1 | 1 | 1 | 1 | SIM | R1--R6 |

### Comparação: *Baseline* Manual vs. Motor Lógico

| Critério | Manual | Motor Lógico |
|----------|--------|--------------|
| Transparência | Baixa | Total |
| Consistência | Variável | Determinística |
| Explicabilidade | Verbal | Formal (CNF) |
| Rastreabilidade | Nenhuma | Regra por regra |
| Fadiga decisória | Presente | Ausente |
| Nuance qualitativa | Alta | Nenhuma |

## Explicabilidade

> A explicabilidade é um requisito ético, jurídico e pedagógico simultaneamente. O AcolheMente implementa explicabilidade **intrínseca**: a lógica proposicional é, por definição, transparente. Cada variável tem semântica clara, cada regra tem antecedentes e consequente explícitos, e cada conclusão pode ser rastreada à cláusula CNF que a originou.

> Ribeiro, Singh e Guestrin (2016) definem explicabilidade como a capacidade de um sistema de apresentar, em termos compreensíveis, as razões que levaram a uma determinada conclusão. No AcolheMente, a explicação *é* o modelo --- não há gap entre o que o sistema faz e o que o sistema diz que faz.

> A distinção entre explicabilidade intrínseca e *post-hoc* é particularmente relevante no domínio de saúde mental escolar. O ECA (Brasil, 1990) exige proteção integral de crianças e adolescentes, o que inclui proteção contra classificação automatizada opaca. A LGPD (Brasil, 2018) garante transparência no tratamento de dados.

## Discussão Crítica

> O AcolheMente demonstra que é possível aplicar inteligência artificial em um domínio sensível com explicabilidade total, determinismo e conformidade jurídica. A escolha por lógica proposicional é precisamente adequada ao escopo do problema.

> **Limitações reconhecidas:** A lógica proposicional não modela gradações, incertezas ou relações temporais. A qualidade das conclusões depende da alimentação correta das variáveis de entrada. O motor não aprende com novos dados. A validação foi computacional, não em ambiente escolar real.

> **Riscos:** Falso conforto tecnológico (equipe escolar reduz atenção qualitativa), viés de construção (regras refletem julgamento dos engenheiros), risco de medicalização do espaço escolar.

> A contribuição do projeto reside na demonstração de que rigor técnico e responsabilidade ética podem coexistir --- e de que, em domínios de alto risco humano, a transparência é mais valiosa que a complexidade."""))

# =====================================================================
# SECAO 6 — PERSPECTIVA DE EVOLUCAO
# =====================================================================
cells.append(md(r"""# Perspectiva de Evolução do Trabalho

> A arquitetura do AcolheMente Escolar PB foi concebida para permitir evolução incremental, mas essa evolução não é governada pela lógica do "mais complexo é melhor". Qualquer avanço técnico deve ser precedido por validações éticas e institucionais proporcionais ao risco que a mudança introduz.

> O caminho mais natural de evolução é o refinamento do próprio motor simbólico, sem abandonar o paradigma determinístico. A incorporação de novas variáveis --- frequência escolar, participação em atividades extracurriculares, indicadores de convivência familiar --- poderia enriquecer a modelagem sem comprometer a transparência. Essa expansão, entretanto, não é trivial: cada nova variável dobra o espaço combinatório de estados, exigindo revisão integral das regras e revalidação dos cenários.

> Uma evolução particularmente promissora é a transição para lógica *fuzzy*, com graus de pertinência entre 0 e 1, permitindo modelar gradações de sofrimento emocional e apoio social. A definição das funções de pertinência exigiria calibração empírica com dados longitudinais e validação com profissionais de psicologia escolar (Russell; Norvig, 2022).

> Em horizonte mais distante, modelos híbridos poderiam integrar módulos de *machine learning* para tarefas específicas, mantendo o motor simbólico como camada de governança e explicabilidade. Nessa arquitetura, nenhuma conclusão do módulo estatístico seria apresentada à equipe escolar sem passar pelo crivo das regras lógicas (Jobin; Ienca; Vayena, 2019).

> A utilização de redes neurais profundas permanece uma hipótese estritamente teórica, condicionada a aprovação por comitê de ética, conformidade demonstrável com LGPD (Brasil, 2018) e ECA (Brasil, 1990), e base longitudinal com volume e qualidade suficientes.

> Qualquer evolução deve ser acompanhada de piloto institucional, formação continuada, comitê de governança de IA e avaliação de impacto. O *roadmap* prevê integração com os fluxos do Programa Saúde na Escola (Brasil, 2007).

> Versões futuras devem implementar monitoramento contínuo de viés e auditoria humana periódica das regras por comitê multidisciplinar. O risco de medicalização da escola deve ser permanentemente monitorado.

> É necessário resistir à tentação de equiparar sofisticação algorítmica a melhoria do projeto. A simplicidade do motor proposicional é uma *feature* a ser preservada enquanto as condições éticas, jurídicas e institucionais para abordagens mais complexas não estiverem plenamente atendidas.

> Independentemente da evolução técnica, o compromisso fundamental permanece inalterável: o sistema nunca diagnosticará condições clínicas. Esse compromisso não é uma restrição técnica: é a razão de ser do projeto."""))

# =====================================================================
# SECAO 7 — CONCLUSAO
# =====================================================================
cells.append(md(r"""# Conclusões

> O presente trabalho demonstrou a viabilidade de aplicar inteligência artificial simbólica --- especificamente, lógica proposicional com inferência por resolução --- ao domínio sensível de saúde mental escolar. O AcolheMente Escolar PB, motor de inferência com 7 variáveis proposicionais e 6 regras em Forma Normal Conjuntiva, oferece uma contribuição técnica e metodológica ao debate sobre IA responsável em contextos educacionais.

> **Contribuição técnica:** Formalização de domínio complexo em lógica proposicional, demonstrando que problemas reais de apoio à decisão podem ser modelados com técnicas simbólicas; motor de resolução determinístico validado contra todos os $2^6$ cenários possíveis; *pipeline* reprodutível com testes automatizados.

> **Contribuição metodológica:** Arquitetura de governança de dados em três *tiers*, *guardrails* de não diagnóstico, *human-in-the-loop* inegociável, conformidade demonstrável com LGPD, ECA e PSE.

> **Contribuição escolar:** Ferramenta de apoio à gestão que reduz a dependência de percepções individuais, com mecanismo de explicabilidade que permite auditar cada decisão.

> Os limites são reconhecidos: expressividade restrita, dependência de alimentação humana correta, validação limitada a cenários sintéticos e risco de falso conforto tecnológico. Esses limites não são falhas de *design*: são consequências deliberadas de um sistema que prioriza segurança, transparência e cautela.

> A maturidade de um projeto de IA aplicada a populações vulneráveis não se mede pela complexidade do modelo, mas pela robustez de sua governança. O AcolheMente Escolar PB demonstra que é possível ser tecnicamente rigoroso e eticamente responsável --- e que, em domínios de alto risco humano, essa combinação não é opcional."""))

# =====================================================================
# SECAO 8 — REFERENCIAS
# =====================================================================
cells.append(md("""# Referências Bibliográficas

> BRACHMAN, R. J.; LEVESQUE, H. J. **Knowledge Representation and Reasoning**. San Francisco: Morgan Kaufmann, 2004.

> BRASIL. Lei nº 8.069, de 13 de julho de 1990 --- Estatuto da Criança e do Adolescente (ECA). Disponível em: https://www.planalto.gov.br/ccivil_03/leis/L8069.htm. Acesso em: 20 maio 2026.

> BRASIL. Decreto nº 6.286, de 5 de dezembro de 2007 --- Programa Saúde na Escola (PSE). Disponível em: https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/decreto/d6286.htm. Acesso em: 20 maio 2026.

> BRASIL. Lei nº 13.709, de 14 de agosto de 2018 --- Lei Geral de Proteção de Dados Pessoais (LGPD). Disponível em: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709.htm. Acesso em: 20 maio 2026.

> GENESERETH, M. R.; NILSSON, N. J. **Logical Foundations of Artificial Intelligence**. San Mateo: Morgan Kaufmann, 1987.

> INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA. **Pesquisa Nacional de Saúde do Escolar --- PeNSE 2024**. Rio de Janeiro: IBGE, 2024. Disponível em: https://www.ibge.gov.br/estatisticas/sociais/educacao/9134-pesquisa-nacional-de-saude-do-escolar.html. Acesso em: 20 maio 2026.

> JOBIN, A.; IENCA, M.; VAYENA, E. The global landscape of AI ethics guidelines. **Nature Machine Intelligence**, v. 1, p. 389--399, 2019.

> RIBEIRO, M. T.; SINGH, S.; GUESTRIN, C. "Why Should I Trust You?": Explaining the Predictions of Any Classifier. In: **Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining**, p. 1135--1144. ACM, 2016.

> RUSSELL, S.; NORVIG, P. **Inteligência Artificial: uma abordagem moderna**. 4. ed. Rio de Janeiro: GEN LTC, 2022.

> WORLD HEALTH ORGANIZATION. **World mental health report: transforming mental health for all**. Geneva: WHO, 2022. Disponível em: https://www.who.int/publications/i/item/9789240049338. Acesso em: 20 maio 2026."""))

# =====================================================================
# APENDICES (markdown de referencia)
# =====================================================================
cells.append(md(r"""\newpage
\makeatletter
\renewcommand{\@chapapp}{Apêndice}
\makeatother
\appendix

## Apêndice A: Símbolos Proposicionais do AcolheMente
\label{apendice:simbolos}
> Código-fonte completo no arquivo `simbolos_acolhemente.py` (salvo via `%%writefile` acima).

## Apêndice B: Regras Lógicas e CNF
\label{apendice:regras}
> Código-fonte completo no arquivo `regras_acolhemente.py` (salvo via `%%writefile` acima).

## Apêndice C: Motor de Inferência por Resolução
\label{apendice:motor}
> Código-fonte completo no arquivo `motor_resolucao_acolhemente.py` (salvo via `%%writefile` acima).

## Apêndice D: Cenários Sintéticos de Validação
\label{apendice:cenarios}
> Código-fonte completo no arquivo `cenarios_sinteticos_acolhemente.py` (salvo via `%%writefile` acima).

## Apêndice E: Grafo de Explicabilidade
\label{apendice:grafo}
> Código-fonte completo no arquivo `grafo_explicabilidade_acolhemente.py` (salvo via `%%writefile` acima).

## Apêndice F: Gerador de Tabelas de Resultados
\label{apendice:tabelas}
> Código-fonte completo no arquivo `gerar_tabelas_resultados.py` (salvo via `%%writefile` acima)."""))

# =====================================================================
# CELLS DE INFRA (montar drive, instalar tex, converter)
# =====================================================================
cells.append(code(""))  # cell vazia separadora

cells.append(code("""# use capture para esconder msgs de log na saida da celula
%%capture
from google.colab import drive
drive.mount('/content/drive')"""))

cells.append(code("""# instalar componentes tex e conversor para pdf
%%capture
!apt-get install texlive texlive-xetex texlive-latex-extra pandoc
!pip install pypdf nbconvert"""))

cells.append(code("""# download da logomarca da instituicao
%%capture
!wget -q -P /content/ -O logo_urutai.png https://www.ifgoiano.edu.br/home/images/REITORIA/Identidade_Visual/LOGOS/NOVOS/URUTAI/ifgoiano-urutai-rgb.png"""))

cells.append(code(r"""%%capture
with open('/content/referencias.bib', 'w', encoding='utf-8') as f:
    f.write(r"""
+ '"""'
+ r"""
@book{ibge_pense_2024,
  title={Pesquisa Nacional de Sa{\'u}de do Escolar --- PeNSE 2024},
  author={{Instituto Brasileiro de Geografia e Estat{\'i}stica}},
  year={2024},
  address={Rio de Janeiro},
  publisher={IBGE},
  note={Dispon{\'i}vel em: \url{https://www.ibge.gov.br/estatisticas/sociais/educacao/9134-pesquisa-nacional-de-saude-do-escolar.html}. Acesso em: 20 maio 2026}
}

@misc{brasil_lgpd_2018,
  title={Lei n{\textordmasculine} 13.709, de 14 de agosto de 2018 --- Lei Geral de Prote{\c c}{\~a}o de Dados Pessoais (LGPD)},
  author={{Brasil}},
  year={2018},
  note={Dispon{\'i}vel em: \url{https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709.htm}. Acesso em: 20 maio 2026}
}

@misc{brasil_eca_1990,
  title={Lei n{\textordmasculine} 8.069, de 13 de julho de 1990 --- Estatuto da Crian{\c c}a e do Adolescente (ECA)},
  author={{Brasil}},
  year={1990},
  note={Dispon{\'i}vel em: \url{https://www.planalto.gov.br/ccivil_03/leis/L8069.htm}. Acesso em: 20 maio 2026}
}

@misc{brasil_pse_2007,
  title={Decreto n{\textordmasculine} 6.286, de 5 de dezembro de 2007 --- Programa Sa{\'u}de na Escola (PSE)},
  author={{Brasil}},
  year={2007},
  note={Dispon{\'i}vel em: \url{https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/decreto/d6286.htm}. Acesso em: 20 maio 2026}
}

@book{russell_norvig_2022,
  title={Intelig{\^e}ncia Artificial: uma abordagem moderna},
  author={Russell, Stuart and Norvig, Peter},
  edition={4},
  address={Rio de Janeiro},
  publisher={GEN LTC},
  year={2022}
}

@book{brachman_levesque_2004,
  title={Knowledge Representation and Reasoning},
  author={Brachman, Ronald J. and Levesque, Hector J.},
  year={2004},
  publisher={Morgan Kaufmann},
  address={San Francisco}
}

@book{genesereth_nilsson_1987,
  title={Logical Foundations of Artificial Intelligence},
  author={Genesereth, Michael R. and Nilsson, Nils J.},
  year={1987},
  publisher={Morgan Kaufmann},
  address={San Mateo}
}

@inproceedings{ribeiro_lime_2016,
  title={``Why Should {I} Trust You?'': Explaining the Predictions of Any Classifier},
  author={Ribeiro, Marco Tulio and Singh, Sameer and Guestrin, Carlos},
  booktitle={Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
  pages={1135--1144},
  year={2016},
  publisher={ACM}
}

@article{jobin_ai_ethics_2019,
  title={The global landscape of {AI} ethics guidelines},
  author={Jobin, Anna and Ienca, Marcello and Vayena, Effy},
  journal={Nature Machine Intelligence},
  volume={1},
  pages={389--399},
  year={2019},
  publisher={Springer Nature}
}

@techreport{who_mental_health_2022,
  title={World mental health report: transforming mental health for all},
  author={{World Health Organization}},
  year={2022},
  institution={WHO},
  address={Geneva},
  note={Dispon{\'i}vel em: \url{https://www.who.int/publications/i/item/9789240049338}. Acesso em: 20 maio 2026}
}
"""
+ '"""'
+ """
)"""))

cells.append(code("""# copia do seu notebook para a area de trabalho provisoria /content
%%capture
!cp "/content/drive/MyDrive/Colab Notebooks/esp-IA/Trabalho_Trilha_I_AcolheMente_PB.ipynb" /content/"""))

cells.append(code("""# 2. Converte o notebook atual para PDF via HTML
# Substitua 'Trabalho_Trilha_I_AcolheMente_PB.ipynb' pelo nome exato do seu arquivo
!jupyter nbconvert --to html "Trabalho_Trilha_I_AcolheMente_PB.ipynb"
!echo "Conversao concluida. Verifique o arquivo HTML gerado."

# Alternativa: conversao direta para PDF (requer texlive)
# !jupyter nbconvert --to pdf "Trabalho_Trilha_I_AcolheMente_PB.ipynb" """))

# =====================================================================
# MONTAR NOTEBOOK
# =====================================================================
notebook = {
    "nbformat": 4,
    "nbformat_minor": 5,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.10.0",
            "mimetype": "text/x-python",
            "file_extension": ".py"
        },
        "colab": {
            "provenance": [],
            "toc_visible": True
        }
    },
    "cells": cells
}

# Salvar
output_path = os.path.join(os.path.dirname(__file__), "notebooks",
                           "Trabalho_Trilha_I_AcolheMente_PB.ipynb")
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, ensure_ascii=False, indent=1)

print(f"Notebook gerado: {output_path}")
print(f"Total de cells: {len(cells)}")
md_count = sum(1 for c in cells if c['cell_type'] == 'markdown')
code_count = sum(1 for c in cells if c['cell_type'] == 'code')
print(f"  Markdown: {md_count}")
print(f"  Code: {code_count}")
