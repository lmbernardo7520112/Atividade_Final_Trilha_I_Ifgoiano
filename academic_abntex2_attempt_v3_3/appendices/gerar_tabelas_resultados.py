# =====================================================================
# APENDICE F: Gerador de Tabelas de Resultados
# =====================================================================
# Gera tabelas LaTeX a partir dos cenarios sinteticos.
# =====================================================================

def gerar_tabela_variaveis_latex():
    """Gera tabela LaTeX das 7 variaveis proposicionais."""
    return r"""
\begin{table}[H]
\centering
\caption{Variáveis proposicionais do AcolheMente Escolar PB.}
\label{tab:variaveis}
\begin{tabular}{clll}
\toprule
\textbf{Var} & \textbf{Tipo} & \textbf{Semântica Operacional} & \textbf{Fontes PeNSE} \\
\midrule
E & Nuclear    & Sofrimento emocional recorrente       & B12004, B12005, B12007 \\
B & Nuclear    & Baixo apoio socioafetivo percebido     & B12003, B07004 \\
V & Nuclear    & Indicador de desvalor da vida          & B12008 \\
S & Nuclear    & Sinal de autoagressão                  & B12009 \\
A & Saída inferida    & Acolhimento prioritário (saída)        & Inferida \\
C & Contextual & Contexto comportamental agravante      & B03010C, B03006B \\
I & Contextual & Insuficiência institucional             & E01P60, E01P117 \\
\bottomrule
\end{tabular}
\end{table}
"""


def gerar_tabela_regras_latex():
    """Gera tabela LaTeX das regras R1-R6."""
    return r"""
\begin{table}[H]
\centering
\caption{Regras lógicas R1--R6 e respectivas cláusulas CNF.}
\label{tab:regras}
\begin{tabular}{cll}
\toprule
\textbf{Regra} & \textbf{Forma Implicativa} & \textbf{CNF} \\
\midrule
R1 & $S \rightarrow A$              & $\neg S \lor A$ \\
R2 & $V \land E \rightarrow A$      & $\neg V \lor \neg E \lor A$ \\
R3 & $E \land B \rightarrow A$      & $\neg E \lor \neg B \lor A$ \\
R4 & $V \land B \rightarrow A$      & $\neg V \lor \neg B \lor A$ \\
R5 & $E \land B \land C \rightarrow A$ & $\neg E \lor \neg B \lor \neg C \lor A$ \\
R6 & $V \land I \rightarrow A$      & $\neg V \lor \neg I \lor A$ \\
\bottomrule
\end{tabular}
\end{table}
"""


def gerar_tabela_cenarios_latex():
    """Gera tabela LaTeX dos cenarios de validacao."""
    return r"""
\begin{table}[H]
\centering
\caption{Cenários sintéticos de validação do motor de inferência.}
\label{tab:cenarios}
\begin{tabular}{lcccccccl}
\toprule
\textbf{Cenário} & \textbf{E} & \textbf{B} & \textbf{V} & \textbf{S} & \textbf{C} & \textbf{I} & \textbf{A} & \textbf{Regra(s)} \\
\midrule
Nulo             & 0 & 0 & 0 & 0 & 0 & 0 & NÃO & --- \\
S isolado        & 0 & 0 & 0 & 1 & 0 & 0 & SIM  & R1 \\
V+E              & 1 & 0 & 1 & 0 & 0 & 0 & SIM  & R2 \\
E+B              & 1 & 1 & 0 & 0 & 0 & 0 & SIM  & R3 \\
V+B              & 0 & 1 & 1 & 0 & 0 & 0 & SIM  & R4 \\
E+B+C            & 1 & 1 & 0 & 0 & 1 & 0 & SIM  & R3, R5 \\
V+I              & 0 & 0 & 1 & 0 & 0 & 1 & SIM  & R6 \\
C isolado        & 0 & 0 & 0 & 0 & 1 & 0 & NÃO & --- \\
I isolado        & 0 & 0 & 0 & 0 & 0 & 1 & NÃO & --- \\
Todas            & 1 & 1 & 1 & 1 & 1 & 1 & SIM  & R1--R6 \\
\bottomrule
\end{tabular}
\end{table}
"""


if __name__ == "__main__":
    print(gerar_tabela_variaveis_latex())
    print(gerar_tabela_regras_latex())
    print(gerar_tabela_cenarios_latex())
