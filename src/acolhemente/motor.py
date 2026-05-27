"""
Motor de Inferência por Resolução — AcolheMente Escolar PB.

Técnica: Lógica Proposicional com Inferência por Resolução.
Variáveis: E, B, V, S, C, I (entrada), A (saída).
Regras: R1–R6 em Forma Normal Conjuntiva (CNF).

Este módulo NÃO deve ser alterado sem revisão do ADR-011.
"""

# ── Base de Conhecimento em CNF ──────────────────────────────────────
# Cada cláusula é representada como frozenset de literais.
# Literais positivos: "X"; negativos: "~X".

REGRAS_CNF = {
    "R1": frozenset({"~S", "A"}),           # S → A
    "R2": frozenset({"~V", "~E", "A"}),     # V ∧ E → A
    "R3": frozenset({"~E", "~B", "A"}),     # E ∧ B → A
    "R4": frozenset({"~V", "~B", "A"}),     # V ∧ B → A
    "R5": frozenset({"~E", "~B", "~C", "A"}),  # E ∧ B ∧ C → A
    "R6": frozenset({"~V", "~I", "A"}),     # V ∧ I → A
}

# Mapeamento legível das regras
REGRAS_NATURAIS = {
    "R1": "S → A",
    "R2": "V ∧ E → A",
    "R3": "E ∧ B → A",
    "R4": "V ∧ B → A",
    "R5": "E ∧ B ∧ C → A",
    "R6": "V ∧ I → A",
}

VARIAVEIS = ["E", "B", "V", "S", "C", "I"]


def _resolve(c1, c2):
    """Aplica regra de resolução entre duas cláusulas."""
    for lit in c1:
        complement = lit[1:] if lit.startswith("~") else f"~{lit}"
        if complement in c2:
            resolvente = (c1 | c2) - {lit, complement}
            return resolvente
    return None


def inferir_por_resolucao(clausulas, conclusao="A"):
    """
    Inferência por resolução: verifica se `conclusao` pode ser
    derivada da base de conhecimento (conjunto de cláusulas).

    Retorna True se KB |= conclusao.
    """
    # Adiciona negação da conclusão
    negacao = frozenset({f"~{conclusao}"})
    todas = set(clausulas) | {negacao}

    novas = set()
    while True:
        pares = [
            (ci, cj)
            for ci in todas
            for cj in todas
            if ci != cj
        ]
        for ci, cj in pares:
            resolvente = _resolve(ci, cj)
            if resolvente is not None:
                if len(resolvente) == 0:
                    return True  # cláusula vazia → prova
                novas.add(frozenset(resolvente))
        if novas.issubset(todas):
            return False  # sem novas cláusulas → falha
        todas |= novas


def inferir_acolhimento(
    E=False, B=False, V=False, S=False, C=False, I=False
):
    """
    Verifica se A (acolhimento priorizado) deve ser inferido
    dado o estado das variáveis de entrada.

    Retorna True/False.
    """
    # Gera cláusulas unitárias para fatos verdadeiros
    fatos = []
    mapa = {"E": E, "B": B, "V": V, "S": S, "C": C, "I": I}
    for var, val in mapa.items():
        if val:
            fatos.append(frozenset({var}))
        else:
            fatos.append(frozenset({f"~{var}"}))

    clausulas = list(REGRAS_CNF.values()) + fatos
    return inferir_por_resolucao(clausulas, "A")


def explicar_decisao(
    E=False, B=False, V=False, S=False, C=False, I=False
):
    """
    Explica quais regras são acionadas pelo estado dado.

    Retorna dict com:
      - resultado: bool
      - regras_acionadas: list[str]
      - explicacao: str
    """
    mapa = {"E": E, "B": B, "V": V, "S": S, "C": C, "I": I}
    resultado = inferir_acolhimento(**mapa)

    # Identifica regras acionadas por verificação direta
    acionadas = []
    antecedentes = {
        "R1": {"S": True},
        "R2": {"V": True, "E": True},
        "R3": {"E": True, "B": True},
        "R4": {"V": True, "B": True},
        "R5": {"E": True, "B": True, "C": True},
        "R6": {"V": True, "I": True},
    }

    for regra, requisitos in antecedentes.items():
        if all(mapa.get(v) == val for v, val in requisitos.items()):
            acionadas.append(regra)

    if acionadas:
        regras_str = ", ".join(
            f"{r} ({REGRAS_NATURAIS[r]})" for r in acionadas
        )
        explicacao = (
            f"Acolhimento PRIORIZADO. "
            f"Regras acionadas: {regras_str}."
        )
    else:
        explicacao = (
            "Acolhimento NÃO priorizado. "
            "Nenhuma regra acionada."
        )

    return {
        "resultado": resultado,
        "regras_acionadas": acionadas,
        "explicacao": explicacao,
    }
