# -*- coding: utf-8 -*-
# =====================================================================
# APENDICE A: Simbolos Proposicionais do AcolheMente Escolar PB
# =====================================================================
# 7 variaveis proposicionais:
#   - 4 entradas nucleares
#   - 2 entradas contextuais
#   - 1 saida inferida
#
# Entradas do motor: E, B, V, S, C, I
# Saida inferida: A
#
# Fontes conceituais: PeNSE 2024 (IBGE) - Tema 12 (Saude Mental)
# ADR-008/009: sem linguagem diagnostica, sem dados identificaveis
# =====================================================================


# ---------------------------------------------------------------------
# 1. Entradas nucleares
# ---------------------------------------------------------------------
# Variaveis diretamente relacionadas a sinais de sofrimento subjetivo,
# apoio socioafetivo, desvalor da vida ou autoagressao.
#
# Importante:
# Estas variaveis NAO representam diagnostico clinico. Elas funcionam
# apenas como indicadores logicos para apoio a priorizacao de acolhimento
# humano.
# ---------------------------------------------------------------------

E = "Sofrimento emocional recorrente"        # PeNSE: B12004, B12005, B12007
B = "Baixo apoio socioafetivo percebido"     # PeNSE: B12003, B07004
V = "Indicador critico de desvalor da vida"  # PeNSE: B12008
S = "Sinal autorreferido de autoagressao"    # PeNSE: B12009


# ---------------------------------------------------------------------
# 2. Entradas contextuais de modulacao
# ---------------------------------------------------------------------
# Variaveis de contexto. Elas NAO devem acionar acolhimento prioritario
# isoladamente. Sua funcao e modular ou qualificar cenarios nos quais
# tambem existam sinais nucleares.
# ---------------------------------------------------------------------

C = "Contexto comportamental agravante"          # PeNSE: B03010C, B03006B
I = "Insuficiencia institucional de resposta"    # PeNSE: E01P60, E01P117


# ---------------------------------------------------------------------
# 3. Saida inferida pelo motor
# ---------------------------------------------------------------------
# A nao e entrada observada. A e a conclusao logica inferida a partir
# das seis entradas E, B, V, S, C, I e das regras R1-R6.
#
# Por isso, a validacao exaustiva cobre 2^6 = 64 cenarios, e nao 2^7.
# ---------------------------------------------------------------------

A = "Acolhimento humano prioritario"  # Saida inferida pelo motor


# ---------------------------------------------------------------------
# 4. Catalogo semantico das variaveis
# ---------------------------------------------------------------------
# Cada simbolo proposicional possui:
#   - semantica: significado no dominio escolar;
#   - tipo: papel da variavel na arquitetura logica;
#   - fontes: variaveis/fonte PeNSE ou indicacao de inferencia.
# ---------------------------------------------------------------------

VARIAVEIS = {
    "E": {
        "semantica": E,
        "tipo": "nuclear",
        "papel": "entrada",
        "fontes": ["B12004", "B12005", "B12007"],
    },
    "B": {
        "semantica": B,
        "tipo": "nuclear",
        "papel": "entrada",
        "fontes": ["B12003", "B07004"],
    },
    "V": {
        "semantica": V,
        "tipo": "nuclear",
        "papel": "entrada",
        "fontes": ["B12008"],
    },
    "S": {
        "semantica": S,
        "tipo": "nuclear",
        "papel": "entrada",
        "fontes": ["B12009"],
    },
    "C": {
        "semantica": C,
        "tipo": "contextual",
        "papel": "entrada",
        "fontes": ["B03010C", "B03006B"],
    },
    "I": {
        "semantica": I,
        "tipo": "contextual",
        "papel": "entrada",
        "fontes": ["E01P60", "E01P117"],
    },
    "A": {
        "semantica": A,
        "tipo": "saida",
        "papel": "inferida",
        "fontes": ["inferida"],
    },
}


# ---------------------------------------------------------------------
# 5. Conveniencias formais para o motor
# ---------------------------------------------------------------------

ENTRADAS_NUCLEARES = ["E", "B", "V", "S"]
ENTRADAS_CONTEXTUAIS = ["C", "I"]
ENTRADAS_MOTOR = ENTRADAS_NUCLEARES + ENTRADAS_CONTEXTUAIS
SAIDA_MOTOR = "A"


# ---------------------------------------------------------------------
# 6. Testes de contrato estrutural
# ---------------------------------------------------------------------
# Estes asserts protegem o "orcamento logico" do projeto.
# Se alguem alterar acidentalmente o numero ou o papel das variaveis,
# a execucao falha imediatamente.
# ---------------------------------------------------------------------

assert len(VARIAVEIS) == 7, "Budget: exatamente 7 variaveis proposicionais"

assert len(ENTRADAS_NUCLEARES) == 4, (
    "Devem existir exatamente 4 entradas nucleares: E, B, V, S"
)

assert len(ENTRADAS_CONTEXTUAIS) == 2, (
    "Devem existir exatamente 2 entradas contextuais: C, I"
)

assert len(ENTRADAS_MOTOR) == 6, (
    "O motor deve possuir exatamente 6 entradas: E, B, V, S, C, I"
)

assert SAIDA_MOTOR == "A", "A saida inferida deve ser A"

assert SAIDA_MOTOR not in ENTRADAS_MOTOR, (
    "A nao pode ser entrada do motor; A e saida inferida"
)

assert sum(1 for v in VARIAVEIS.values() if v["tipo"] == "nuclear") == 4, (
    "Devem existir exatamente 4 variaveis nucleares de entrada"
)

assert sum(1 for v in VARIAVEIS.values() if v["tipo"] == "contextual") == 2, (
    "Devem existir exatamente 2 variaveis contextuais de entrada"
)

assert sum(1 for v in VARIAVEIS.values() if v["tipo"] == "saida") == 1, (
    "Deve existir exatamente 1 variavel de saida inferida"
)

assert sum(1 for v in VARIAVEIS.values() if v["papel"] == "entrada") == 6, (
    "Devem existir exatamente 6 variaveis de entrada"
)

assert sum(1 for v in VARIAVEIS.values() if v["papel"] == "inferida") == 1, (
    "Deve existir exatamente 1 variavel inferida"
)


# ---------------------------------------------------------------------
# 7. Execucao didatica
# ---------------------------------------------------------------------
# Ao executar este arquivo diretamente, o avaliador visualiza o vocabulario
# formal do motor, seus papeis e suas fontes conceituais.
# ---------------------------------------------------------------------

if __name__ == "__main__":
    print("=== Variaveis Proposicionais do AcolheMente Escolar PB ===\n")

    print("Entradas nucleares:")
    for nome in ENTRADAS_NUCLEARES:
        info = VARIAVEIS[nome]
        print(f"  {nome}: {info['semantica']}")
        print(f"     Fontes PeNSE: {', '.join(info['fontes'])}")

    print("\nEntradas contextuais:")
    for nome in ENTRADAS_CONTEXTUAIS:
        info = VARIAVEIS[nome]
        print(f"  {nome}: {info['semantica']}")
        print(f"     Fontes PeNSE: {', '.join(info['fontes'])}")

    print("\nSaida inferida:")
    info = VARIAVEIS[SAIDA_MOTOR]
    print(f"  {SAIDA_MOTOR}: {info['semantica']}")
    print(f"     Fonte: {', '.join(info['fontes'])}")

    print("\nResumo estrutural:")
    print(f"  Total de variaveis proposicionais: {len(VARIAVEIS)}")
    print(f"  Entradas do motor: {len(ENTRADAS_MOTOR)} -> {', '.join(ENTRADAS_MOTOR)}")
    print(f"  Saida inferida: {SAIDA_MOTOR}")
    print("  Espaco de validacao: 2^6 = 64 cenarios")
