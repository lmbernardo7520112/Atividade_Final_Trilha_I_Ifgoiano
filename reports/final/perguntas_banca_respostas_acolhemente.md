# Perguntas da Banca e Respostas — AcolheMente Escolar PB

> **Versão:** v3.3 | **Data:** 2026-06-06

---

## 1. Por que não usar dados reais no motor?

> Na versão acadêmica, o objetivo é validar a lógica, não classificar estudantes reais. Dados reais exigiriam comitê de ética, consentimento informado (menores = representantes legais), e protocolo de pseudonimização operacional. O motor é validado com cenários sintéticos determinísticos — todas as 64 combinações são testadas.

## 2. Como acolher um aluno se tudo está anonimizado?

> Não está anonimizado — está pseudonimizado. Pseudonimização mantém a possibilidade de reidentificação por equipe autorizada, permitindo que o acolhimento aconteça. Anonimização irreversível impediria localizar o estudante. O fluxo prevê case_id substituindo a identidade durante o processamento, com reidentificação restrita à equipe pedagógica/psicológica designada.

## 3. O sistema faz diagnóstico?

> Não. O motor faz sinalização de prioridade para acolhimento humano. Ele identifica quais combinações de indicadores justificam atenção prioritária. O diagnóstico, se necessário, é feito por profissional de saúde mental após encaminhamento. O motor sinaliza; o profissional decide.

## 4. Por que lógica proposicional?

> Porque as variáveis são binárias (presente/ausente), o espaço de estados é finito (2^6 = 64), e o domínio exige explicabilidade total. Lógica proposicional permite prova formal, auditabilidade e rastreabilidade de cada decisão. Não há necessidade de representação mais expressiva nesta etapa.

## 5. Por que não deep learning?

> Porque (a) não existe dataset rotulado de acolhimento escolar; (b) modelos de deep learning são opacos ("caixa preta"); (c) o domínio envolve menores, regulado por LGPD e ECA, que exigem explicabilidade; (d) 64 combinações possíveis não justificam a complexidade de um modelo estatístico.

## 6. O que são as 7 variáveis?

> E = sofrimento emocional recorrente; B = baixo apoio socioafetivo percebido; V = indicador de desvalor da vida; S = sinal de autoagressão; C = contexto comportamental agravante; I = insuficiência institucional de resposta; A = acolhimento prioritário (saída inferida). E, B, V e S são nucleares; C e I são contextuais; A é a saída do motor.

## 7. Por que são 6 entradas e 1 saída?

> A variável A é inferida pelo motor — não é dado observado. Por isso o espaço de teste é 2^6 = 64, não 2^7 = 128. A saída é determinada pela combinação das 6 entradas segundo as regras R1–R6.

## 8. O que significa 2^6 = 64?

> Com 6 variáveis binárias, existem 2^6 = 64 combinações possíveis de entradas. Cada combinação é um cenário. A validação exaustiva testa todas as 64, comparando o motor com um oráculo independente. Zero falhas.

## 9. O que impede falso positivo por contexto escolar negativo?

> Os guardrails. C (contexto comportamental agravante) e I (insuficiência institucional) nunca acionam A isoladamente. Mesmo C+I combinados, sem nenhuma variável nuclear verdadeira, resultam em A=NÃO. Isso evita que contexto social negativo estigmatize um estudante sem evidência de sofrimento ou risco.

## 10. O que acontece se C e I forem verdadeiros, mas E/B/V/S forem falsos?

> A = NÃO. Nenhum acolhimento é sinalizado. As variáveis contextuais só modulam a inferência quando acompanhadas de variáveis nucleares. Isso é verificado no CSV: a combinação (0,0,0,0,1,1) resulta em A_motor=0.

## 11. Quem decide após A ser inferido?

> O profissional humano. O motor apenas sinaliza prioridade. A decisão de acolher, encaminhar ou investigar cabe à equipe pedagógica/psicológica da escola, conforme protocolos do PSE. Human-in-the-loop é obrigatório.

## 12. Como a LGPD foi considerada?

> Princípios aplicados: finalidade (exclusivamente acolhimento); adequação (variáveis mínimas necessárias); necessidade (6 variáveis binárias); transparência (motor explicável); não-discriminação (guardrails contra estigmatização); segurança (pseudonimização projetada). Art. 20: direito à explicação de decisão automatizada.

## 13. Como o ECA foi considerado?

> Art. 17 (direito à dignidade), Art. 18 (proteção de integridade), Art. 100 (interesse superior da criança). O motor não expõe informações sensíveis, não rankeia, não diagnostica, e prevê human-in-the-loop para qualquer decisão sobre o menor.

## 14. Como o PSE entra na proposta?

> O Programa Saúde na Escola é o contexto institucional natural para o motor. O PSE prevê integração entre educação e saúde, com ações nas escolas. O motor apoiaria a gestão escolar na priorização de acolhimento, dentro do fluxo do PSE, com encaminhamento para UBS/CAPS quando necessário.

## 15. Qual é a diferença entre PeNSE e cenários sintéticos?

> A PeNSE é pesquisa populacional (TIER_A): fundamenta a escolha das variáveis, demonstra que o problema é real. Os cenários sintéticos (TIER_B) são combinações binárias determinísticas usadas para validar a lógica do motor. A PeNSE NÃO alimenta o motor; os cenários SIM (para teste).

## 16. Qual é o papel do dataset externo?

> TIER_C: benchmark exploratório para comparação de contexto. Não sustenta inferência regional, não entra no motor, não substitui a PeNSE. Serve para explorar se a abordagem tem viabilidade em outros contextos.

## 17. O motor acadêmico é igual ao motor de produção?

> Sim, logicamente. Ambos implementam a mesma `inferir_acolhimento()` com as mesmas regras R1–R6 em CNF. A diferença é arquitetura: o pedagógico (apêndices, 102 linhas) é didático; o modular (src/acolhemente, 147 linhas) é estruturado para engenharia. O teste de equivalência confirma resultados idênticos para todas as 64 combinações.

## 18. O que os grafos explicam?

> Os grafos visualizam a cadeia de rastreabilidade: (1) quais variáveis alimentam quais regras (grafo de regras); (2) como os dados fluem e se separam em tiers (proveniência); (3) o que acontece depois que A é inferido (governança pós-acolhimento); (4) como a pseudonimização protege o estudante durante o processamento.

## 19. Quais são as limitações do projeto?

> (1) Não é sistema clínico; (2) não faz diagnóstico; (3) não substitui profissionais; (4) não usa dados reais na versão acadêmica; (5) PeNSE é populacional, não local; (6) dataset externo não sustenta inferência regional; (7) motor pedagógico exigiria validação operacional para produção.

## 20. Como seria uma evolução futura responsável?

> Cinco fases: (1) piloto institucional governado com comitê de ética; (2) protocolos escolares integrados ao PSE; (3) integração PSE/UBS/CAPS; (4) avaliação de impacto (cobertura, tempo de resposta); (5) auditoria humana periódica. ML ou lógica fuzzy apenas como hipótese futura, sob governança.

## 21. Por que R5 é mantida se é subsumida?

> Por valor explicativo. R5 (E ∧ B ∧ C → A) indica que contexto agravante torna mais grave uma situação que já seria prioritária. R3 (E ∧ B → A) já cobre formalmente. Mas na explicação para o gestor, saber que C está presente tem valor informativo para o encaminhamento.

## 22. O que é CNF?

> Forma Normal Conjuntiva: cada regra é expressa como disjunção de literais. Obtida pela equivalência `p → q ≡ ¬p ∨ q`. Permite aplicar o método de resolução, que é completo e correto para lógica proposicional.

## 23. O baseline é experimento empírico?

> Não. É rubrica qualitativa comparativa — analisa metodologicamente o que um checklist manual faria versus o que o motor faz. Não envolve profissionais reais nem alunos. Serve para demonstrar consistência do motor, não para medir acurácia contra padrão-ouro.

## 24. Quantos testes automatizados existem?

> 8 módulos de teste com 136 asserções (pytest): equivalência dos motores, fluxo acadêmico, estrutura abnTeX2, qualidade do PDF, uso de dados, anti-regressão, privacidade operacional.

## 25. O que diferencia pseudonimização de anonimização?

> Anonimização é irreversível: impossibilita localizar o indivíduo. Pseudonimização substitui a identidade por um case_id, permitindo reidentificação restrita. Em acolhimento escolar, anonimizar impediria acolher — pseudonimizar protege durante o processamento e permite atuar quando necessário.

---

*Documento preparado em 2026-06-06. Baseado na versão v3.3 do AcolheMente Escolar PB.*
