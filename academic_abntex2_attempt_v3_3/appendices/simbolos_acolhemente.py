# =====================================================================
# APENDICE A: Simbolos Proposicionais do AcolheMente Escolar PB
# =====================================================================
# 7 variaveis: 4 entradas nucleares, 2 entradas contextuais, 1 saida inferida
# Fontes: PeNSE 2024 (IBGE) - Tema 12 (Saude Mental)
# ADR-008/009: Sem linguagem diagnostica, sem dados identificaveis
# =====================================================================

# --- 4 Variaveis Nucleares de Entrada ---
E = "Sofrimento emocional recorrente"       # PeNSE: B12004, B12005, B12007
B = "Baixo apoio socioafetivo percebido"    # PeNSE: B12003, B07004
V = "Indicador critico de desvalor da vida" # PeNSE: B12008
S = "Sinal autorreferido de autoagressao"   # PeNSE: B12009
A = "Acolhimento humano prioritario"        # Saida do motor (inferida)

# --- 2 Variaveis Contextuais de Modulacao ---
C = "Contexto comportamental agravante"     # PeNSE: B03010C, B03006B
I = "Insuficiencia institucional de resposta"  # PeNSE: E01P60, E01P117

# --- Mapeamento completo ---
VARIAVEIS = {
    "E": {"semantica": E, "tipo": "nuclear",    "fontes": ["B12004","B12005","B12007"]},
    "B": {"semantica": B, "tipo": "nuclear",    "fontes": ["B12003","B07004"]},
    "V": {"semantica": V, "tipo": "nuclear",    "fontes": ["B12008"]},
    "S": {"semantica": S, "tipo": "nuclear",    "fontes": ["B12009"]},
    "A": {"semantica": A, "tipo": "saida_inferida", "fontes": ["inferida"]},
    "C": {"semantica": C, "tipo": "contextual", "fontes": ["B03010C","B03006B"]},
    "I": {"semantica": I, "tipo": "contextual", "fontes": ["E01P60","E01P117"]},
}

assert len(VARIAVEIS) == 7, "Budget: exatamente 7 variaveis"
assert sum(1 for v in VARIAVEIS.values() if v["tipo"]=="nuclear") == 4
assert sum(1 for v in VARIAVEIS.values() if v["tipo"]=="saida_inferida") == 1
assert sum(1 for v in VARIAVEIS.values() if v["tipo"]=="contextual") == 2

if __name__ == "__main__":
    print("=== Variaveis Proposicionais do AcolheMente ===")
    for nome, info in VARIAVEIS.items():
        print(f"  {nome} ({info['tipo']}): {info['semantica']}")
        print(f"       Fontes PeNSE: {', '.join(info['fontes'])}")
