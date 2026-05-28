# =====================================================================
# APENDICE C: Motor de Inferencia por Resolucao
# =====================================================================
# Implementacao do metodo de resolucao para logica proposicional.
# Correto e refutacionalmente completo (Russell; Norvig, 2022).
# =====================================================================

from regras_acolhemente import REGRAS_CNF, ANTECEDENTES, REGRAS_IMPLICATIVAS


def _resolve(c1, c2):
    """Aplica a regra de resolucao entre duas clausulas."""
    for lit in c1:
        complement = lit[1:] if lit.startswith("~") else f"~{lit}"
        if complement in c2:
            resolvente = (c1 | c2) - {lit, complement}
            return resolvente
    return None


def inferir_por_resolucao(clausulas, conclusao="A"):
    """
    Verifica se KB |= conclusao via metodo de resolucao.

    Procedimento:
      1. Adiciona ~conclusao ao conjunto de clausulas
      2. Aplica resolucao iterativamente
      3. Se clausula vazia derivada -> KB |= conclusao (True)
      4. Se nenhuma nova clausula -> KB |/= conclusao (False)
    """
    negacao = frozenset({f"~{conclusao}"})
    todas = set(clausulas) | {negacao}

    while True:
        novas = set()
        lista = list(todas)
        for i in range(len(lista)):
            for j in range(i + 1, len(lista)):
                resolvente = _resolve(lista[i], lista[j])
                if resolvente is not None:
                    if len(resolvente) == 0:
                        return True
                    novas.add(frozenset(resolvente))
        if novas.issubset(todas):
            return False
        todas |= novas


def inferir_acolhimento(E=False, B=False, V=False, S=False, C=False, I=False):
    """Verifica se A deve ser inferido dado o estado das variaveis."""
    mapa = {"E": E, "B": B, "V": V, "S": S, "C": C, "I": I}
    fatos = []
    for var, val in mapa.items():
        if val:
            fatos.append(frozenset({var}))
        else:
            fatos.append(frozenset({f"~{var}"}))
    clausulas = list(REGRAS_CNF.values()) + fatos
    return inferir_por_resolucao(clausulas, "A")


def explicar_decisao(E=False, B=False, V=False, S=False, C=False, I=False):
    """Retorna explicacao completa: resultado, regras acionadas, texto."""
    mapa = {"E": E, "B": B, "V": V, "S": S, "C": C, "I": I}
    resultado = inferir_acolhimento(**mapa)

    acionadas = []
    for regra, requisitos in ANTECEDENTES.items():
        if all(mapa.get(v) == val for v, val in requisitos.items()):
            acionadas.append(regra)

    if acionadas:
        regras_str = ", ".join(
            f"{r} ({REGRAS_IMPLICATIVAS[r]})" for r in acionadas
        )
        explicacao = f"Acolhimento PRIORIZADO. Regras: {regras_str}."
    else:
        explicacao = "Acolhimento NAO priorizado. Nenhuma regra acionada."

    return {
        "resultado": resultado,
        "regras_acionadas": acionadas,
        "explicacao": explicacao,
    }


if __name__ == "__main__":
    print("=== Motor de Resolucao - AcolheMente ===\n")
    testes = [
        ("Nulo", {}),
        ("S isolado (R1)", {"S": True}),
        ("V+E (R2)", {"V": True, "E": True}),
        ("E+B (R3)", {"E": True, "B": True}),
        ("C isolado (guardrail)", {"C": True}),
        ("I isolado (guardrail)", {"I": True}),
        ("Todas", {"E":True,"B":True,"V":True,"S":True,"C":True,"I":True}),
    ]
    for nome, params in testes:
        r = explicar_decisao(**params)
        status = "SIM" if r["resultado"] else "NAO"
        print(f"  {nome:30s} -> A={status}  {r['explicacao']}")