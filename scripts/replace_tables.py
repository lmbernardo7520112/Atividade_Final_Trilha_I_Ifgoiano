"""
Remove markdown tables from notebook and replace with
list-based representations that compile cleanly in LaTeX.
"""
import nbformat
import re

NB_PATH = "notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb"

with open(NB_PATH, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

for cell in nb.cells:
    if cell.cell_type != 'markdown':
        continue

    # Check if cell contains a markdown table
    if '| ---' not in cell.source and '|:---' not in cell.source:
        continue

    # Replace variable tables (Section 5.2)
    if '| **E** |' in cell.source and 'B12004' in cell.source:
        cell.source = cell.source.split('## 5.2')[0] + """## 5.2 Variáveis Nucleares (5)

- **E** — Sofrimento emocional recorrente (choro, isolamento agudo). Fontes PeNSE: B12004, B12005, B12007.
- **B** — Baixo apoio familiar/social percebido. Fontes PeNSE: B12003, B07004.
- **V** — Indicador crítico de desvalor/desesperança em relação à vida. Fonte PeNSE: B12008.
- **S** — Sinal autorreferido de autoagressão. Fonte PeNSE: B12009.
- **A** — Acolhimento humano prioritário (**saída do motor**). Derivada por inferência.

## 5.3 Variáveis Contextuais de Modulação (2)

- **C** — Contexto comportamental agravante (mudança brusca de comportamento). Fontes PeNSE: B03010C, B03006B.
- **I** — Insuficiência institucional de resposta. Fontes PeNSE: E01P60, E01P117.

As variáveis contextuais **nunca** inferem **A** isoladamente. **C** só participa de regras em conjunção com **E** e **B** (R5); **I** só participa em conjunção com **V** (R6). Essa restrição é um *guardrail* lógico: impede que fatores contextuais, por si sós, gerem falsos positivos de priorização.

## 5.4 Nota sobre Não Diagnóstico

O sistema **NÃO diagnostica** condições clínicas. As variáveis representam indicadores comportamentais observáveis e auto-reportados, não categorias nosológicas. A variável **A** sinaliza necessidade de acolhimento pedagógico/psicossocial — uma ação escolar, não uma intervenção clínica. Essa distinção é fundamental e perpassa todo o *design* do motor."""

    # Replace CNF table (Section 7.2)
    if '| **R1** |' in cell.source and 'CNF' in cell.source:
        cell.source = re.sub(
            r'\| Regra \|.*?(?=\n## 7\.3|\Z)',
            """As regras convertidas para CNF são:

- **R1:** $S \\\\rightarrow A$ → CNF: $\\\\neg S \\\\lor A$
- **R2:** $V \\\\land E \\\\rightarrow A$ → CNF: $\\\\neg V \\\\lor \\\\neg E \\\\lor A$
- **R3:** $E \\\\land B \\\\rightarrow A$ → CNF: $\\\\neg E \\\\lor \\\\neg B \\\\lor A$
- **R4:** $V \\\\land B \\\\rightarrow A$ → CNF: $\\\\neg V \\\\lor \\\\neg B \\\\lor A$
- **R5:** $E \\\\land B \\\\land C \\\\rightarrow A$ → CNF: $\\\\neg E \\\\lor \\\\neg B \\\\lor \\\\neg C \\\\lor A$
- **R6:** $V \\\\land I \\\\rightarrow A$ → CNF: $\\\\neg V \\\\lor \\\\neg I \\\\lor A$

""",
            cell.source,
            flags=re.DOTALL
        )

with open(NB_PATH, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print("Tables replaced with list format")
