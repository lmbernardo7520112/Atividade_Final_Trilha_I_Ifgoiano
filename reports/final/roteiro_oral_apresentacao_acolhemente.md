# Roteiro Oral de Apresentação — AcolheMente Escolar PB

> **Versão:** v3.3 | **Data:** 2026-06-06

---

# VERSÃO 1 — APRESENTAÇÃO CURTA (10–12 minutos)

## Bloco 1 — Abertura e problema (0:00–1:30)

**Objetivo:** capturar atenção com o problema real.

**Fala:**
> "Boa tarde. Meu trabalho é o AcolheMente Escolar PB, um motor de inferência lógico para apoio à gestão escolar na priorização responsável de acolhimento em saúde mental. O problema é simples e urgente: a PeNSE 2019 mostra que mais de 16% dos adolescentes brasileiros já se sentiram pouco valorizados pela vida e quase 11% declaram autoagressão. Na Paraíba, os números são semelhantes. A escola pública é muitas vezes o único ponto de contato institucional com esse estudante — mas os gestores não dispõem de um fluxo formal, transparente e governado para priorizar quem mais precisa de acolhimento."

**Evidência visual:** Slide/PDF com dados PeNSE; gráfico de `eda_plots.py`.

**Pergunta provável:** "Esses dados são da Paraíba especificamente?"
**Resposta:** "A PeNSE é nacional, com estratificação por UF. Os dados da PB fundamentam a motivação; o motor não classifica respondentes da PeNSE."

---

## Bloco 2 — Escolha metodológica (1:30–3:00)

**Objetivo:** justificar SBC e resolução, posicionar contra ML.

**Fala:**
> "Escolhi um Sistema Baseado em Conhecimento com lógica proposicional e inferência por resolução. Por quê? Primeiro, porque as variáveis são binárias — presente ou ausente. Segundo, porque o espaço de estados é finito: 2 elevado a 6 = 64 combinações. Terceiro — e mais importante — porque em domínio sensível envolvendo menores, transparência vale mais que complexidade. Cada decisão do motor pode ser rastreada até a regra e a variável que a originou. Machine learning exigiria dataset rotulado que não existe, produziria modelo opaco e seria inadequado neste contexto."

**Evidência visual:** Tabela de variáveis do PDF; `regras_acolhemente.py`.

**Pergunta provável:** "E se houvesse dados rotulados?"
**Resposta:** "Mesmo com dados, a LGPD e o ECA exigiriam explicabilidade para decisões envolvendo menores. ML poderia complementar, não substituir, a base simbólica."

---

## Bloco 3 — Variáveis e regras (3:00–5:00)

**Objetivo:** apresentar a representação do conhecimento.

**Fala:**
> "O motor usa 7 variáveis proposicionais: 4 entradas nucleares — sofrimento emocional, baixo apoio, desvalor da vida e autoagressão; 2 entradas contextuais — contexto comportamental agravante e insuficiência institucional; e 1 saída inferida — acolhimento prioritário. Por isso testamos 2 elevado a 6 = 64 combinações, não 128. A saída A é inferida, não entrada."

> "As 6 regras R1 a R6 codificam o conhecimento do domínio. R1: autoagressão sozinha já aciona acolhimento — é regra de urgência. R3: sofrimento emocional combinado com baixo apoio também aciona. Os guardrails: contexto social ou falha institucional isolados nunca acionam A. Isso evita estigmatização."

**Evidência visual:** Tabela de variáveis e tabela de regras no PDF.

**Pergunta provável:** "O que é R5?"
**Resposta:** "R5 adiciona contexto agravante a R3, mas é formalmente subsumida: sempre que R5 dispara, R3 já disparou. R5 é mantida por valor explicativo."

---

## Bloco 4 — Validação exaustiva (5:00–6:30)

**Objetivo:** demonstrar rigor formal.

**Fala:**
> "A validação não é amostral. Testamos todas as 64 combinações possíveis das 6 entradas. Para cada combinação, o motor é executado e comparado com um oráculo independente — uma função booleana separada que expressa a mesma lógica de forma diferente. Resultado: 64 testes, 64 acertos, zero falhas. O CSV com todas as 64 linhas está disponível como artefato do projeto."

**Evidência visual:** `validacao_exaustiva_64.csv`; gráfico de ativação de regras.

**Pergunta provável:** "Como garante que o oráculo está correto?"
**Resposta:** "O oráculo é a disjunção direta das condições das regras. É verificável por inspeção: `S or (V and E) or (E and B) or (V and B) or (V and I)`. R5 não aparece porque é subsumida por R3."

---

## Bloco 5 — Governança e LGPD (6:30–8:00)

**Objetivo:** demonstrar maturidade ética.

**Fala:**
> "O motor não faz diagnóstico. Não rankeia estudantes. Não toma decisão automatizada. Ele sinaliza prioridade para revisão humana — é human-in-the-loop. Na versão acadêmica, nenhum dado real de estudante é processado. Para piloto futuro, o desenho prevê pseudonimização com case_id, reidentificação restrita a equipe autorizada, e consentimento informado. A conformidade com LGPD, ECA e PSE é considerada desde o desenho da arquitetura."

**Evidência visual:** `fluxo_pseudonimizacao_acolhimento.png`; `grafo_governanca_acolhemente.png`.

---

## Bloco 6 — Limitações e evolução (8:00–9:30)

**Objetivo:** demonstrar honestidade intelectual.

**Fala:**
> "Este trabalho não é sistema clínico. Não substitui psicólogos. Não usa dados de alunos reais na versão acadêmica. A PeNSE é base populacional — não captura especificidades locais. O motor pedagógico é didático; produção exigiria validação operacional. A evolução responsável passaria por piloto institucional governado, integração com PSE/UBS/CAPS, e auditoria humana periódica."

---

## Bloco 7 — Fechamento (9:30–10:30)

**Fala:**
> "A tese deste trabalho é que a técnica correta em contexto sensível não é necessariamente a mais complexa; é a mais explicável, governável, auditável e proporcional ao risco. O motor sinaliza; o profissional decide. Obrigado."

---

---

# VERSÃO 2 — APRESENTAÇÃO COMPLETA (20–25 minutos)

## Bloco 1 — Abertura e contextualização (0:00–3:00)

**Fala:** Expandir Bloco 1 da versão curta com:
- Dados específicos PeNSE PB vs Brasil
- Contexto do PSE (Programa Saúde na Escola)
- Papel da escola pública como primeiro contato
- Lacuna: ausência de ferramenta formal de priorização

**Evidência:** Gráficos EDA do PDF; `fluxo_proveniencia_dados.png`.

---

## Bloco 2 — Justificativa e fundamentação (3:00–6:00)

**Fala:** Expandir Bloco 2 com:
- Definição formal de SBC (Russell & Norvig, 2022)
- Comparação SBC vs ML vs DL para este contexto
- Explicar o que é CNF e resolução em linguagem acessível
- Mostrar a equivalência `p → q ≡ ¬p ∨ q`
- Explicar por que a resolução é completa e correta

**Evidência:** Tabela de regras CNF do PDF; `regras_acolhemente.py:18–24`.

---

## Bloco 3 — Variáveis e representação (6:00–9:00)

**Fala:** Expandir Bloco 3 com:
- Cada variável explicada com rastreabilidade à PeNSE
- Explicar a diferença entre nuclear e contextual
- Mostrar A como saída inferida (taxonomia 4-2-1)
- Demonstrar o cálculo: 2^6 = 64

**Evidência:** `simbolos_acolhemente.py`; `_build/tabela_variaveis.tex`.

---

## Bloco 4 — Regras R1–R6 detalhadas (9:00–12:00)

**Fala:** Cada regra individualmente:
- R1: urgência absoluta de S
- R2: combinação V+E
- R3: combinação E+B
- R4: combinação V+B
- R5: subsunção por R3, valor explicativo
- R6: V+I (desvalor + falha institucional)
- Guardrails: C isolado, I isolado, C+I sem nucleares → todos NÃO

**Evidência:** `regras_acolhemente.py`; cenários da tabela no PDF.

---

## Bloco 5 — Implementação e dois motores (12:00–14:00)

**Fala:**
- Mostrar `inferir_acolhimento()` — 10 linhas no motor pedagógico
- Explicar `_resolve()` e `inferir_por_resolucao()`
- Mostrar que o motor modular tem a mesma assinatura
- Explicar o teste de equivalência

**Evidência:** `motor_resolucao_acolhemente.py:49–59`; `src/acolhemente/motor.py:77–96`.

---

## Bloco 6 — Validação exaustiva detalhada (14:00–16:30)

**Fala:** Expandir com:
- Loop `itertools.product`
- Oráculo independente e por que R5 não aparece
- CSV: colunas, resultado, contagem de A=SIM (50) vs A=NÃO (14)
- Teste de R5 sem R3 = 0

**Evidência:** Notebook célula 14; `validacao_exaustiva_64.csv`.

---

## Bloco 7 — Explicabilidade e grafos (16:30–18:30)

**Fala:**
- Grafo de regras: variáveis → regras → A
- Grafo de governança: sinal → revisão → encaminhamento
- Fluxo de proveniência: TIER_A/B/C
- Fluxo de pseudonimização: case_id → motor → revisão → reidentificação restrita

**Evidência:** Todas as figuras em `figures/`.

---

## Bloco 8 — Governança LGPD/ECA/PSE (18:30–20:30)

**Fala:** Expandir com:
- Art. 20 LGPD: direito à explicação
- ECA Art. 17, 18, 100: dignidade, privacidade, interesse superior
- PSE: finalidade de saúde escolar
- Human-in-the-loop como requisito
- Pseudonimização vs anonimização
- Por que anonimizar impede acolher

---

## Bloco 9 — Resultados e baseline (20:30–22:00)

**Fala:**
- 50/64 acionam A; 14/64 não acionam
- Guardrails funcionam: C e I isolados → NÃO
- Baseline qualitativo: rubrica comparativa
- Não é experimento empírico

**Evidência:** `comparacao_baseline_motor.png`; `_build/tabela_cenarios.tex`.

---

## Bloco 10 — Limitações e evolução (22:00–24:00)

**Fala:** Expandir as 7 limitações e o roadmap de 5 fases.

---

## Bloco 11 — Fechamento (24:00–25:00)

**Fala:** Tese final + frase de encerramento.

---

*Roteiro preparado em 2026-06-06. Baseado na versão v3.3 do AcolheMente Escolar PB.*
