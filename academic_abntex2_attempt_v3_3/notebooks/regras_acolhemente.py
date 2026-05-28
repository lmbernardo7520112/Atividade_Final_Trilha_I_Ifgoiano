# =====================================================================
# APENDICE B: Regras Logicas e Conversao para CNF
# =====================================================================
# 6 regras R1-R6 em forma implicativa e CNF
# A como unica conclusao operacional
# C e I nunca inferem A isoladamente (guardrail)
# =====================================================================

REGRAS_IMPLICATIVAS = {
    "R1": "S -> A",
    "R2": "V AND E -> A",
    "R3": "E AND B -> A",
    "R4": "V AND B -> A",
    "R5": "E AND B AND C -> A",
    "R6": "V AND I -> A",
}

REGRAS_CNF = {
    "R1": frozenset({"~S", "A"}),
    "R2": frozenset({"~V", "~E", "A"}),
    "R3": frozenset({"~E", "~B", "A"}),
    "R4": frozenset({"~V", "~B", "A"}),
    "R5": frozenset({"~E", "~B", "~C", "A"}),
    "R6": frozenset({"~V", "~I", "A"}),
}

REGRAS_CNF_LEGIVEL = {
    "R1": "~S OR A",
    "R2": "~V OR ~E OR A",
    "R3": "~E OR ~B OR A",
    "R4": "~V OR ~B OR A",
    "R5": "~E OR ~B OR ~C OR A",
    "R6": "~V OR ~I OR A",
}

# Antecedentes de cada regra (para verificacao direta)
ANTECEDENTES = {
    "R1": {"S": True},
    "R2": {"V": True, "E": True},
    "R3": {"E": True, "B": True},
    "R4": {"V": True, "B": True},
    "R5": {"E": True, "B": True, "C": True},
    "R6": {"V": True, "I": True},
}

assert len(REGRAS_CNF) == 6, "Budget: exatamente 6 regras"
assert all("A" in c for c in REGRAS_CNF.values()), "A deve ser consequente"

if __name__ == "__main__":
    print("=== Regras R1-R6 ===")
    for r in sorted(REGRAS_IMPLICATIVAS):
        print(f"  {r}: {REGRAS_IMPLICATIVAS[r]}")
        print(f"       CNF: {REGRAS_CNF_LEGIVEL[r]}")