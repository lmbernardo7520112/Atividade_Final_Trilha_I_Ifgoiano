# =====================================================================
# APENDICE D: Cenarios Sinteticos de Validacao
# =====================================================================
# Validacao exaustiva do motor com cenarios representativos.
# TIER_B: dados sinteticos, sem dados reais de alunos.
# =====================================================================

from motor_resolucao_acolhemente import inferir_acolhimento, explicar_decisao

CENARIOS = [
    {"nome": "Cenario Nulo",            "E":False,"B":False,"V":False,"S":False,"C":False,"I":False, "esperado": False},
    {"nome": "S isolado (R1)",          "E":False,"B":False,"V":False,"S":True, "C":False,"I":False, "esperado": True},
    {"nome": "V+E (R2)",                "E":True, "B":False,"V":True, "S":False,"C":False,"I":False, "esperado": True},
    {"nome": "E+B (R3)",                "E":True, "B":True, "V":False,"S":False,"C":False,"I":False, "esperado": True},
    {"nome": "V+B (R4)",                "E":False,"B":True, "V":True, "S":False,"C":False,"I":False, "esperado": True},
    {"nome": "E+B+C (R5)",             "E":True, "B":True, "V":False,"S":False,"C":True, "I":False, "esperado": True},
    {"nome": "V+I (R6)",                "E":False,"B":False,"V":True, "S":False,"C":False,"I":True,  "esperado": True},
    {"nome": "C isolado (guardrail)",   "E":False,"B":False,"V":False,"S":False,"C":True, "I":False, "esperado": False},
    {"nome": "I isolado (guardrail)",   "E":False,"B":False,"V":False,"S":False,"C":False,"I":True,  "esperado": False},
    {"nome": "C+I (guardrail duplo)",   "E":False,"B":False,"V":False,"S":False,"C":True, "I":True,  "esperado": False},
    {"nome": "Todas verdadeiras",       "E":True, "B":True, "V":True, "S":True, "C":True, "I":True,  "esperado": True},
    {"nome": "E isolado",               "E":True, "B":False,"V":False,"S":False,"C":False,"I":False, "esperado": False},
    {"nome": "B isolado",               "E":False,"B":True, "V":False,"S":False,"C":False,"I":False, "esperado": False},
    {"nome": "V isolado",               "E":False,"B":False,"V":True, "S":False,"C":False,"I":False, "esperado": False},
]


def executar_validacao():
    """Executa todos os cenarios e retorna resultados."""
    resultados = []
    for c in CENARIOS:
        nome = c["nome"]
        esperado = c["esperado"]
        params = {k: c[k] for k in ["E","B","V","S","C","I"]}
        r = explicar_decisao(**params)
        obtido = r["resultado"]
        ok = obtido == esperado
        resultados.append({
            "nome": nome,
            "esperado": esperado,
            "obtido": obtido,
            "ok": ok,
            "regras": r["regras_acionadas"],
        })
    return resultados


if __name__ == "__main__":
    print("=== Validacao de Cenarios Sinteticos ===\n")
    print(f"{'Cenario':<30s} {'Esperado':>8s} {'Obtido':>8s} {'Status':>8s} {'Regras'}")
    print("-" * 80)
    resultados = executar_validacao()
    falhas = 0
    for r in resultados:
        e = "SIM" if r["esperado"] else "NAO"
        o = "SIM" if r["obtido"] else "NAO"
        s = "  OK" if r["ok"] else "FALHA"
        regras = ", ".join(r["regras"]) if r["regras"] else "--"
        print(f"  {r['nome']:<28s} {e:>8s} {o:>8s} {s:>8s}   {regras}")
        if not r["ok"]:
            falhas += 1
    print(f"\n{'='*80}")
    print(f"Total: {len(resultados)} cenarios, {falhas} falhas")
    if falhas == 0:
        print("RESULTADO: TODOS OS CENARIOS PASSARAM")
    else:
        print(f"RESULTADO: {falhas} CENARIO(S) FALHARAM")
