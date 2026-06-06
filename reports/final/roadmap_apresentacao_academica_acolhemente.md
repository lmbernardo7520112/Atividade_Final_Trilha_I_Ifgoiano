# Roadmap Conceitual para Apresentação Acadêmica — AcolheMente Escolar PB

> **Versão:** v3.3 | **Data:** 2026-06-06
> **Contexto:** Atividade Final da Trilha I — Pós-Graduação IF Goiano

---

## 1. Abertura da apresentação

**Objetivo:** situar o problema no mundo real antes de falar de tecnologia.

- Saúde mental adolescente no Brasil: dados da PeNSE 2019 indicam que 16,4% dos adolescentes já se sentiram pouco valorizados pela vida (B12008) e 10,9% declararam autoagressão (B12009).
- Na Paraíba, os indicadores são comparáveis ou superiores à média nacional.
- A escola pública é o primeiro e muitas vezes único ponto de contato institucional com o estudante em sofrimento.
- Gestores escolares não dispõem de fluxo formal, sistemático e governado para priorizar acolhimento em saúde mental.
- O trabalho propõe um motor de inferência lógico para apoio à gestão — não um sistema de diagnóstico.

**Frase-chave:** "A escola pode acolher melhor se souber priorizar com método, transparência e responsabilidade."

---

## 2. Justificativa do tema

- A PeNSE (Pesquisa Nacional de Saúde do Escolar, IBGE) é a fonte agregada que motiva a escolha das variáveis, mas **não alimenta o motor**.
- Os dados da PeNSE fundamentam o problema (TIER_A): sofrimento emocional recorrente, desvalor da vida, baixo apoio percebido e autoagressão são problemas documentados.
- A escola precisa de um fluxo de acolhimento que seja governado, explicável e proporcional ao risco — sem estigmatizar, sem diagnosticar, sem rankear estudantes.
- Dados reais de estudantes não entram no motor na versão acadêmica: o trabalho valida a lógica com cenários sintéticos determinísticos.

**Frase-chave:** "A PeNSE mostra que o problema é real; o motor mostra que a priorização pode ser responsável."

---

## 3. Arquitetura de dados e proveniência

### Três tiers de dados

| Tier | Fonte | Função | Entra no motor? |
|------|-------|--------|:---:|
| **TIER_A** | PeNSE/IBGE 2019/2024 | Motivação empírica, EDA, escolha de variáveis | ❌ |
| **TIER_B** | Cenários sintéticos (2^6 = 64) | Validação exaustiva da lógica | ✅ (teste) |
| **TIER_C** | Dataset externo (benchmark) | Exploração comparativa | ❌ |

### Princípios de governança

- Proibição de merge entre tiers.
- TIER_A nunca alimenta inferência individual.
- TIER_B é determinístico: verifica toda combinação possível de entradas.
- Pseudonimização (não anonimização) projetada para piloto futuro.
- Reidentificação restrita a equipe autorizada para viabilizar acolhimento real.

**Frase-chave:** "Três camadas de dados com papéis distintos: motivar, validar e explorar — nunca misturar."

---

## 4. Escolha da técnica de IA

- **Por que Sistema Baseado em Conhecimento (SBC)?** Porque o domínio exige explicabilidade total, auditabilidade e proporcionalidade. O conhecimento é codificado explicitamente em regras, não em pesos opacos.
- **Por que lógica proposicional?** Porque as variáveis são binárias (presente/ausente) e as combinações são finitas (2^6 = 64). Não há necessidade de lógica de primeira ordem ou fuzzy nesta etapa.
- **Por que inferência por resolução?** Porque é um método completo e correto para lógica proposicional (Russell & Norvig, 2022), permite prova formal e é determinístico.
- **Por que NÃO machine learning/deep learning?** Porque (a) não há dataset rotulado de acolhimento escolar; (b) modelos opacos são inadequados para decisões sobre menores; (c) o domínio é sensível e regulado (LGPD/ECA); (d) a transparência vale mais que a complexidade neste contexto.

**Frase-chave:** "Em domínio sensível, transparência vale mais que complexidade."

---

## 5. Representação do conhecimento

### 7 variáveis proposicionais

| Var | Tipo | Semântica | Fontes PeNSE |
|-----|------|-----------|-------------|
| E | Entrada nuclear | Sofrimento emocional recorrente | B12004, B12005, B12007 |
| B | Entrada nuclear | Baixo apoio socioafetivo percebido | B12003, B07004 |
| V | Entrada nuclear | Indicador de desvalor da vida | B12008 |
| S | Entrada nuclear crítica | Sinal de autoagressão | B12009 |
| C | Entrada contextual | Contexto comportamental agravante | B03010C, B03006B |
| I | Entrada contextual | Insuficiência institucional | E01P60, E01P117 |
| A | **Saída inferida** | Acolhimento prioritário | Motor |

**Taxonomia:** 4 entradas nucleares + 2 entradas contextuais + 1 saída inferida = 7 variáveis, 6 de entrada.

**Por que 2^6 = 64 (e não 2^7 = 128)?** Porque A é saída, não entrada. O espaço de teste é formado pelas combinações das 6 variáveis de entrada.

---

## 6. Base de regras R1–R6

| Regra | Forma implicativa | Intenção |
|-------|-------------------|----------|
| R1 | S → A | Autoagressão sempre aciona acolhimento (regra de urgência) |
| R2 | V ∧ E → A | Desvalor + sofrimento = combinação crítica |
| R3 | E ∧ B → A | Sofrimento + isolamento socioafetivo |
| R4 | V ∧ B → A | Desvalor + isolamento |
| R5 | E ∧ B ∧ C → A | Sofrimento + isolamento + contexto agravante |
| R6 | V ∧ I → A | Desvalor + falha institucional |

### Design decisions

- **C e I nunca inferem A isoladamente.** Contexto social negativo ou falha institucional não devem estigmatizar sem evidência nuclear.
- **S isolado aciona alerta (R1).** Autoagressão é sinal de urgência independente de outras variáveis.
- **R5 é subsumida por R3.** Sempre que E, B e C são verdadeiros, R3 (E ∧ B) já dispara. R5 é mantida por valor explicativo — indica que o contexto agravante agrava uma situação já prioritária.
- **A não é diagnóstico.** É sinalização para revisão humana.

---

## 7. Forma Normal Conjuntiva (CNF) e inferência por resolução

### CNF em linguagem simples

Cada regra `p → q` é convertida em `¬p ∨ q` (equivalência lógica fundamental). Exemplo:
- R1: `S → A` vira `¬S ∨ A`
- R3: `E ∧ B → A` vira `¬E ∨ ¬B ∨ A`

### Prova por resolução

1. Adiciona-se `¬A` (negação da conclusão) ao conjunto de cláusulas.
2. Aplica-se resolução iterativamente (cancelamento de literais complementares).
3. Se a cláusula vazia é derivada → A é consequência lógica (motor infere acolhimento).
4. Se nenhuma nova cláusula pode ser derivada → A não é inferido.

**Por que é auditável:** cada passo da prova é rastreável; não há "caixa preta".

---

## 8. Implementação computacional

### Motor pedagógico (apêndices)

- `appendices/motor_resolucao_acolhemente.py` — 102 linhas, funções `inferir_acolhimento()`, `explicar_decisao()`, `_resolve()`
- Didático, curto, rastreável — ideal para apresentação em banca.
- Importado e executado pelo notebook Colab.

### Motor modular (produção)

- `src/acolhemente/motor.py` — 147 linhas, mesma assinatura `inferir_acolhimento()`.
- Complementos: `rule_graph.py`, `graph_schema.py`, `eda_plots.py`.
- Diferença: arquitetura (modular, testável industrialmente), não lógica.

### Teste de equivalência

- `tests/test_motor_equivalence_contract.py` — verifica que ambos produzem resultados idênticos para todas as combinações.

**Frase-chave:** "Duas implementações, mesma semântica. A didática é para a banca; a modular é para engenharia."

---

## 9. Cenários sintéticos e validação

### 64 combinações exaustivas

- `itertools.product([0, 1], repeat=6)` — gera todo o espaço de estados.
- Oráculo independente: `oraculo_acolhimento(E, B, V, S, C, I)` — função booleana separada do motor.
- CSV resultante: `validacao_exaustiva_64.csv` — 64 linhas, 64 ok=True, 0 falhas.

### Cenários didáticos destacados

| Cenário | E B V S C I | A | Regras | Lição |
|---------|:-----------:|:-:|--------|-------|
| Nulo | 0 0 0 0 0 0 | NÃO | — | Sem entradas nucleares → sem acolhimento |
| S isolado | 0 0 0 1 0 0 | SIM | R1 | Urgência absoluta |
| C isolado | 0 0 0 0 1 0 | NÃO | — | Contexto não estigmatiza |
| I isolado | 0 0 0 0 0 1 | NÃO | — | Falha institucional não condena |
| C+I | 0 0 0 0 1 1 | NÃO | — | Guardrail duplo |
| V+E | 1 0 1 0 0 0 | SIM | R2 | Combinação nuclear crítica |
| E+B | 1 1 0 0 0 0 | SIM | R3 | Sofrimento + isolamento |
| E+B+C | 1 1 0 0 1 0 | SIM | R3, R5 | R5 co-aciona mas R3 já cobria |
| Todas | 1 1 1 1 1 1 | SIM | R1–R6 | Todas as regras acionadas |

---

## 10. Resultados

- **50 combinações** acionam A (acolhimento prioritário).
- **14 combinações** não acionam A.
- **0 falsos positivos** por variáveis contextuais isoladas (guardrail funciona).
- **R5 nunca dispara sem R3** — subsunção confirmada formalmente.
- Baseline qualitativo (rubrica comparativa, não experimento empírico) demonstra que o motor é mais consistente que avaliação manual hipotética.

---

## 11. Explicabilidade e grafos

| Grafo | Arquivo | O que mostra |
|-------|---------|-------------|
| Regras 7 variáveis | `grafo_regras_7vars.png` | Fluxo de variáveis para regras e destas para A |
| Governança | `grafo_governanca_acolhemente.png` | Cadeia pós-acolhimento: sinal → revisão → encaminhamento |
| Proveniência | `fluxo_proveniencia_dados.png` | TIER_A/B/C e seus papéis |
| Pseudonimização | `fluxo_pseudonimizacao_acolhimento.png` | Fluxo com case_id e reidentificação restrita |
| Ativação | `cenarios_ativacao_regras.png` | Quais regras acionam em cada cenário |
| Baseline | `comparacao_baseline_motor.png` | Rubrica qualitativa |

**Cadeia completa:** dados → regras → inferência → sinalização → revisão humana → acolhimento.

**Explicabilidade como requisito ético, não apenas técnico:** em domínio de menores, o sistema deve poder justificar cada decisão para cada estudante.

---

## 12. Governança LGPD/ECA/PSE

| Princípio | Aplicação |
|-----------|-----------|
| Não-diagnóstico | O motor sinaliza, não diagnostica |
| Não-ranking | Não ordena estudantes por gravidade |
| Não-decisão automatizada | Human-in-the-loop obrigatório (Art. 20 LGPD) |
| Proteção de menores | ECA Art. 17, 18, 100: dignidade, privacidade, interesse superior |
| Mínimo necessário | 6 variáveis binárias, sem dados sensíveis detalhados |
| Finalidade | Exclusivamente acolhimento escolar (PSE) |
| Pseudonimização | case_id substituindo identidade; reidentificação restrita |
| Consentimento informado | Previsto para piloto futuro |

---

## 13. PDF final e reprodutibilidade

- **PDF acadêmico final:** `academic_abntex2_attempt_v3_3/latex/main_acolhemente_abntex2.pdf` (72 pp, abnTeX2)
- **Gerado via:** pdflatex + bibtex sobre `main_acolhemente_abntex2.tex`
- **Notebook canônico:** `academic_abntex2_attempt_v3_3/notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb` (29 células, HASH-B)
- **Apêndices:** 8 scripts Python em `appendices/`
- **Figuras:** 8 PNGs em `figures/`
- **Tabelas:** 3 .tex em `_build/`
- **Testes:** 8 módulos em `tests/` (136 passed)
- **CSV:** `outputs/validacao_exaustiva_64.csv`

> **Nota:** O PDF em `reports/pdf/` (17 pp, nbconvert) é um artefato anterior, NÃO o PDF final da v3_3.

---

## 14. Limitações

1. Não é sistema clínico — não substitui avaliação psicológica profissional.
2. Não faz diagnóstico — apenas sinaliza prioridade para acolhimento.
3. Não substitui psicólogos, gestores ou rede de saúde.
4. Não usa dados de alunos reais na versão acadêmica.
5. PeNSE é pesquisa populacional — não captura especificidades locais.
6. Dataset externo (TIER_C) não sustenta inferência regional.
7. Motor pedagógico é didático — produção exigiria validação operacional adicional.

---

## 15. Perspectiva de evolução

1. **Piloto institucional governado:** parceria com secretaria de educação, comitê de ética.
2. **Protocolos escolares:** integração com BNCC socioafetivo e PSE.
3. **Integração PSE/UBS/CAPS:** fluxo de encaminhamento formal.
4. **Avaliação de impacto:** métricas de cobertura, tempo de resposta, satisfação.
5. **Auditoria humana:** revisão periódica das regras por profissionais de saúde mental.
6. **Lógica fuzzy ou ML:** apenas como hipótese futura, sob governança e com dados consentidos.

---

## 16. Fechamento

> "A técnica correta em contexto sensível não é necessariamente a mais complexa; é a mais explicável, governável, auditável e proporcional ao risco."

> "O motor sinaliza; o profissional decide."

---

*Roadmap preparado em 2026-06-06. Baseado na versão v3.3 do AcolheMente Escolar PB.*
