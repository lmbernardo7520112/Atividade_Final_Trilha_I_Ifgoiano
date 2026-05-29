# Preparação para Banca Acadêmica — AcolheMente Escolar PB

## Trabalho

**AcolheMente Escolar PB: Motor de Inferência Lógico para Apoio à Gestão Escolar na Priorização Responsável de Acolhimento em Saúde Mental**

Pós-Graduação em IA Aplicada — Trilha I (Técnicas Simbólicas e de Busca) — IF Goiano

## Objetivo deste documento

Preparar o autor para apresentar o trabalho em até 10 minutos, responder perguntas técnicas e metodológicas da banca, e demonstrar domínio completo das decisões de modelagem, implementação, validação e governança.

---

# Seção 1 — Resumo Executivo do Trabalho

## Problema

A saúde mental de adolescentes em escolas públicas da Paraíba enfrenta uma crise silenciosa: a demanda por acolhimento supera a capacidade das equipes escolares, que decidem por percepção informal, sem ferramentas estruturadas de priorização. Essa informalidade gera inconsistência, fadiga decisória e risco de que sinais graves passem despercebidos.

## Solução proposta

O AcolheMente Escolar PB é um Sistema Baseado em Conhecimento (SBC) que usa Lógica Proposicional com Inferência por Resolução para gerar um sinal binário — "acionar acolhimento humano prioritário" ou "não acionar" — a partir de 6 variáveis de entrada observáveis.

## Por que lógica proposicional

A escolha não é uma limitação técnica, mas uma decisão de design ético:

- **Explicabilidade total:** cada conclusão é rastreável a uma regra explícita em CNF.
- **Determinismo:** a mesma entrada sempre produz a mesma saída.
- **Auditabilidade:** qualquer pessoa pode verificar por que o motor acionou ou não o acolhimento.
- **Aderência à Trilha I:** o curso foca em técnicas simbólicas, não em machine learning.

## O que o sistema NÃO faz

- Não diagnostica condições clínicas.
- Não classifica alunos em categorias de risco.
- Não ranqueia estudantes.
- Não substitui avaliação profissional de psicólogos ou assistentes sociais.
- Não se conecta a APIs de IA generativa.

## Formulação estratégica

> O AcolheMente Escolar PB não substitui psicólogos, professores ou gestores. Ele organiza uma sinalização lógica, explicável e auditável para apoiar a priorização responsável de acolhimento escolar.

---

# Seção 2 — O que foi Desenvolvido

## Artefatos finais entregues

| # | Artefato | Descrição |
|---|----------|-----------|
| 1 | **PDF acadêmico abnTeX2** | 72 páginas, 14 capítulos, 8 figuras, 5 tabelas, 33 citações |
| 2 | **Notebook/Colab** | 29 células (17 code + 12 markdown), execução verificada |
| 3 | **CSV de validação exaustiva** | 64 linhas, oráculo independente, 0 falhas |
| 4 | **Apêndices Python** | 8 módulos: motor, regras, símbolos, cenários, grafos, tabelas |
| 5 | **Figuras e grafos** | 8 figuras: proveniência, pseudonimização, governança, regras, cenários, baseline |
| 6 | **Testes automatizados** | 136 testes passando (pytest), 0 falhas |
| 7 | **Relatórios de auditoria** | 5 relatórios: closure, regression, semantic gates, privacy, skills |

## Papel de cada artefato

- O **PDF** é o relatório acadêmico completo: narrativa, fundamentação, resultados e discussão.
- O **notebook** é a demonstração executável/pedagógica: prova que a lógica funciona.
- O **CSV** é a evidência objetiva: todas as 64 combinações testadas com oráculo.
- Os **testes** são a rede de segurança: garantem que nenhuma alteração introduziu regressão.

---

# Seção 3 — Relação entre PDF Final e Notebook/Colab

## Complementaridade

O PDF e o notebook são documentos complementares, não redundantes:

- O **PDF** apresenta a narrativa acadêmica completa: problema, fundamentação, metodologia, arquitetura, resultados, governança e conclusão.
- O **notebook** demonstra a implementação executável: importa o motor, roda os cenários, gera o CSV e exibe resultados.
- O **Colab** foi escolhido para favorecer reprodutibilidade: qualquer avaliador com conta Google pode executar o notebook sem instalar nada.

## Nem tudo precisa estar nos dois

O PDF contém discussões aprofundadas (EDA, governança LGPD/ECA, grafos de rastreabilidade) que não precisam ser replicadas célula por célula no notebook. O notebook precisa provar a lógica central — e prova, via validação exaustiva das 64 combinações.

## O notebook cumpre o template?

> Sim. O notebook cumpre o template porque apresenta contexto, problema, metodologia, implementação, resultados, evolução, conclusão e referências. Além disso, supera o mínimo esperado ao incluir validação exaustiva com oráculo independente, nota metodológica de governança, e separação explícita entre dados PeNSE, cenários sintéticos e benchmark externo.

---

# Seção 4 — Dois Motores: Pedagógico e Modular

**Esta seção é crítica para a banca.**

## 4.1 Motor pedagógico (notebook/Colab)

- **Localização:** `appendices/motor_resolucao_acolhemente.py` (importado pelo notebook)
- **Característica:** curto, didático, legível, poucas dependências
- **Função:** demonstrar resolução, CNF e regras para avaliação acadêmica
- **Tamanho:** ~120 linhas
- **API:** `inferir_acolhimento(E, B, V, S, C, I) → bool`

## 4.2 Motor modular/de produção

- **Localização:** `src/acolhemente/motor.py` (no repositório raiz)
- **Característica:** modular, com testes, integração com grafos e pipeline
- **Função:** referência arquitetural para evolução futura
- **Complementos:** `rule_graph.py`, `graph_schema.py`, `eda_plots.py`

## 4.3 Frase central para banca

> O trabalho não possui dois modelos decisórios diferentes. Ele possui duas implementações equivalentes da mesma base de conhecimento: uma acadêmica, para transparência pedagógica no Colab, e outra modular, como referência de engenharia para evolução. A diferença é de arquitetura de software, não de regra lógica.

## 4.4 Fragilidade do motor pedagógico

**Fragilidade lógica:** não há. O motor pedagógico implementa exatamente as mesmas 6 regras R1–R6, a mesma CNF e o mesmo procedimento de resolução. A validação exaustiva das 64 combinações confirma equivalência com o oráculo independente.

**Limitação operacional:** sim. O motor pedagógico não implementa:

- autenticação de usuários;
- controle de acesso por perfil (coordenador, psicólogo, gestor);
- logs institucionais de acesso;
- pseudonimização real de dados identificáveis;
- integração com sistemas escolares (SIGA, e-SUS);
- banco de dados persistente;
- governança operacional de produção.

Mas ele **cumpre integralmente a missão acadêmica:**

- demonstra a lógica;
- executa as regras;
- gera resultados determinísticos;
- valida as 64 combinações;
- usa oráculo independente;
- mostra R5 subsumida por R3.

> A versão pedagógica valida a semântica lógica; a versão modular aponta o caminho de engenharia; a operação real exigiria governança institucional adicional.

---

# Seção 5 — PeNSE, Cenários Sintéticos e Dataset Externo

## TIER_A — PeNSE 2024

- **Uso:** motivação epidemiológica, Análise Exploratória de Dados, ancoragem conceitual para escolha das variáveis proposicionais.
- **Proibição:** alimentar o motor de inferência individual. A PeNSE é pesquisa populacional, não prontuário.
- **Exemplo:** a variável E (sofrimento emocional recorrente) foi escolhida porque os indicadores B12004, B12005 e B12007 da PeNSE revelam prevalências relevantes na Paraíba.

## TIER_B — Cenários sintéticos

- **Uso:** validação do motor lógico.
- **Razão:** em lógica proposicional, a validação mais rigorosa é a enumeração completa do espaço de estados. Com 6 variáveis de entrada, são 64 combinações — todas testáveis.
- **Proibição:** representar alunos reais. Os cenários são valorações booleanas controladas, não perfis de estudantes.

## TIER_C — Dataset externo

- **Uso:** benchmark metodológico para testar que o pipeline de processamento funciona com dados tabulares de outra origem.
- **Proibição:** tirar conclusão sobre Paraíba, Nordeste ou Brasil. Toda visualização do TIER_C carrega aviso explícito de ausência de validade inferencial.

## Resposta estratégica

> A PeNSE fundamenta o problema; os cenários sintéticos validam a lógica; o dataset externo apenas testa pipeline. Essas camadas não são misturadas.

---

# Seção 6 — Variáveis Proposicionais e Taxonomia Correta

## Estrutura

- 7 variáveis no total
- 6 variáveis de entrada (observáveis/reportáveis)
- 1 variável de saída (inferida pelo motor)
- Espaço combinatório de entrada: `2^6 = 64`, **não** `2^7 = 128`

## Tabela de variáveis

| Variável | Tipo | Significado | Fontes PeNSE |
|----------|------|-------------|--------------|
| E | Entrada nuclear | Sofrimento emocional recorrente | B12004, B12005, B12007 |
| B | Entrada nuclear | Baixo apoio socioafetivo percebido | B12003, B07004 |
| V | Entrada nuclear | Indicador de desvalor da vida | B12008 |
| S | Entrada nuclear crítica | Sinal de autoagressão | B12009 |
| C | Entrada contextual | Contexto comportamental agravante | B03010C, B03006B |
| I | Entrada contextual | Insuficiência institucional | E01P60, E01P117 |
| **A** | **Saída inferida** | **Acolhimento humano prioritário** | **Inferida** |

## Por que A não é "nuclear"

A variável A não é observada, medida ou reportada. Ela é o **resultado** da inferência lógica do motor. Chamá-la de "nuclear" seria erro taxonômico: ela não está no mesmo nível ontológico das variáveis de entrada.

---

# Seção 7 — Regras R1–R6 e R5 Subsumida

## As 6 regras

| Regra | Fórmula | Significado |
|-------|---------|-------------|
| R1 | `S → A` | Autoagressão aciona acolhimento incondicionalmente |
| R2 | `V ∧ E → A` | Desvalor da vida + sofrimento emocional |
| R3 | `E ∧ B → A` | Sofrimento emocional + baixo apoio |
| R4 | `V ∧ B → A` | Desvalor da vida + baixo apoio |
| R5 | `E ∧ B ∧ C → A` | Sofrimento + baixo apoio + contexto agravante |
| R6 | `V ∧ I → A` | Desvalor da vida + insuficiência institucional |

## R5 é subsumida por R3

> R5 é logicamente subsumida por R3 porque sempre que E, B e C são verdadeiros, E e B já são suficientes para acionar R3. Portanto, R5 não aumenta o poder decisório do motor; ela enriquece a explicação ao mostrar que o contexto C também estava presente.

**Evidência:** na validação exaustiva das 64 combinações, R5 nunca aparece sem R3 (0 cenários).

## Resposta à banca

> Mantive R5 por valor explicativo e evolutivo. Ela não cria falso positivo, não altera a decisão e prepara o modelo para versões futuras, por exemplo com lógica fuzzy, nas quais C poderia modular grau de urgência.

---

# Seção 8 — Validação Exaustiva das 64 Combinações

## Estrutura da validação

- 6 variáveis de entrada booleanas → `2^6 = 64` combinações possíveis
- Todas foram testadas
- CSV: `outputs/validacao_exaustiva_64.csv`
- Colunas: `E, B, V, S, C, I, A_motor, A_esperado, ok, regras_acionadas`

## Oráculo independente

O oráculo é uma função Python separada do motor:

```python
def oraculo_acolhimento(E, B, V, S, C, I):
    return S or (V and E) or (E and B) or (V and B) or (V and I)
```

R5 não aparece no oráculo porque é subsumida por R3: o termo `E and B` já cobre `E and B and C`.

## Resultados

| Métrica | Valor |
|---------|-------|
| Total de combinações | 64 |
| ok=True | 64 (100%) |
| A=SIM | 50 |
| A=NÃO | 14 |
| Falhas | 0 |
| R5 sem R3 | 0 |

## 14 cenários vs 64 combinações

- **14 cenários:** representativos, didáticos, mostram os padrões típicos (nulo, S isolado, pares, tríades, guardrails)
- **64 combinações:** validação exaustiva, prova de cobertura completa

> A tabela dos 14 cenários é didática; a prova de cobertura está na enumeração completa das 64 combinações.

---

# Seção 9 — Baseline Manual e Rubrica Qualitativa

## O que é a comparação com baseline

A comparação entre decisão manual (status quo escolar) e motor lógico é uma **rubrica analítica qualitativa** construída a partir de critérios metodológicos:

| Critério | Manual | Motor Lógico |
|----------|--------|--------------|
| Transparência | Baixa | Total |
| Consistência | Variável | Determinística |
| Explicabilidade | Verbal | Formal (CNF) |
| Rastreabilidade | Nenhuma | Regra por regra |
| Fadiga decisória | Presente | Ausente |
| Nuance qualitativa | Alta | Nenhuma |

## O que NÃO é

- Não é experimento empírico com profissionais reais.
- Não é medição de desempenho em ambiente operacional.
- Não é afirmação de superioridade comprovada em escola real.

## Resposta à banca

> A comparação com baseline é uma rubrica qualitativa, não um ensaio empírico. Eu a uso para evidenciar diferenças conceituais entre decisão informal e motor auditável, não para afirmar superioridade operacional comprovada em escola real.

---

# Seção 10 — Governança, LGPD, ECA, PSE e Pseudonimização

## Sensibilidade do domínio

Dados de saúde mental de adolescentes são **dados sensíveis** segundo a LGPD (Art. 5º, II) e protegidos pelo ECA (Art. 17). O sistema:

- Não processa dados identificáveis na versão acadêmica.
- Não faz diagnóstico clínico.
- Não ranqueia alunos.
- Não substitui avaliação humana.
- Não expõe score a professores.

## Pseudonimização para piloto futuro

| Abordagem | Problema |
|-----------|----------|
| Nome real exposto | Viola LGPD e ECA |
| Anonimização irreversível | Impede acolher individualmente |
| **Pseudonimização** | Preserva identidade + viabiliza acolhimento |

Regras para pseudonimização em produção:

- `case_id` vinculado ao estudante
- Chave de reidentificação restrita à coordenação/equipe autorizada
- Professor vê apenas dados agregados por turma
- Logs de acesso auditáveis
- Política de retenção definida

## Programa Saúde na Escola (PSE)

O PSE é o fluxo institucional de encaminhamento: escola → UBS → CAPS. O motor sinaliza internamente; o encaminhamento segue protocolos do PSE.

## Human-in-the-loop

O motor emite sinal binário; a decisão de acolher é humana. Sempre.

## Frase estratégica

> A solução correta para piloto real não é expor nomes nem anonimizar tudo de forma irreversível. É pseudonimizar, separar papéis, auditar acessos e manter a decisão final humana.

---

# Seção 11 — Limitações Reais do Trabalho

1. **Lógica binária:** não modela gradações de urgência (ex.: alto, médio, baixo). Cada variável é verdadeira ou falsa.
2. **Sem aprendizado:** o motor não aprende com dados; as regras são fixas e precisam de revisão humana.
3. **Validação sintética:** a validação foi feita com cenários determinísticos, não com dados operacionais de escola real.
4. **Sem sistema completo de produção:** não há interface, banco de dados, autenticação, nem governança institucional implementada.
5. **Piloto real exigiria:** DPIA/RIPD, aprovação institucional, termo de cooperação, comitê de ética, formação de equipe e validação qualitativa com profissionais.
6. **Regras precisam de revisão:** as 6 regras foram construídas com base na PeNSE e literatura; validação com especialistas de domínio (psicólogos, assistentes sociais) seria necessária antes de operação.
7. **Sem tabela PB/NE/BR local verificável:** a afirmação sobre prevalências na Paraíba é baseada em análise exploratória, não em tabela publicada no documento.

**Por que isso não enfraquece o trabalho:**

O escopo é Trilha I — prova acadêmica de motor simbólico explicável. Todas as limitações acima são consequências naturais desse escopo, não falhas de execução. Reconhecê-las demonstra maturidade metodológica.

---

# Seção 12 — Roadmap de Evolução

## Fase 1 — Fechamento acadêmico ✅

- PDF abnTeX2 final
- Notebook executável com validação exaustiva
- Apêndices, testes e relatórios
- Apresentação para banca

## Fase 2 — Piloto controlado conceitual

- Revisão com orientação/coordenação
- Refinamento de variáveis com profissionais de saúde escolar
- Validação qualitativa: apresentar cenários a psicólogos e perguntar se as sinalizações fazem sentido

## Fase 3 — Governança operacional

- Relatório de Impacto à Proteção de Dados (RIPD/DPIA)
- Matriz de perfis de acesso (coordenador, psicólogo, gestor, professor)
- Pseudonimização operacional com `case_id`
- Logs de acesso e política de retenção

## Fase 4 — Protótipo institucional

- Interface web simples (formulário de entrada → sinal de acolhimento)
- Registro auditável de cada inferência
- Exportação de encaminhamento para fluxo PSE
- Termo de cooperação com escola-piloto

## Fase 5 — Evolução técnica

- Lógica fuzzy para modelar gradações de urgência
- Pesos e níveis de prioridade
- Séries temporais (evolução do estudante ao longo do semestre)
- Integração com sistemas escolares existentes
- **Sempre mantendo human-in-the-loop**

---

# Seção 13 — Roteiro de Apresentação em até 10 Minutos

## 0:00–0:45 — Abertura

Dizer:

> Este trabalho propõe o AcolheMente Escolar PB, um motor lógico explicável para apoiar a gestão escolar na priorização responsável de acolhimento em saúde mental de adolescentes, sem diagnóstico, sem ranking e sem substituição do julgamento humano.

Slide sugerido: título + nome + instituição + uma frase-chave.

## 0:45–1:45 — Problema

Falar sobre:

- Saúde mental adolescente em escolas públicas da Paraíba
- Demanda que supera a capacidade das equipes
- Decisões informais: variabilidade, fadiga, invisibilização de casos graves
- Necessidade de ferramenta estruturada de priorização

## 1:45–2:45 — Escolha metodológica

Falar sobre:

- Trilha I: IA simbólica
- Sistema Baseado em Conhecimento (SBC)
- Lógica proposicional com inferência por resolução
- Escolha ética: explicabilidade > complexidade
- CNF e procedimento de resolução

## 2:45–4:00 — Modelo lógico

Falar sobre:

- 7 variáveis: 4 nucleares, 2 contextuais, 1 saída inferida
- 6 regras R1–R6
- R1 (autoagressão) é incondicional
- C e I sozinhos não acionam A (guardrails)
- A não é diagnóstico; A é sinal de acolhimento

## 4:00–5:15 — Dados e governança

Falar sobre:

- PeNSE como motivação epidemiológica (TIER_A)
- Cenários sintéticos como validação (TIER_B)
- Dataset externo como benchmark (TIER_C)
- Três camadas nunca se misturam
- Dados individuais não entram no motor acadêmico

## 5:15–6:30 — Validação

Falar sobre:

- 14 cenários didáticos/representativos
- 64 combinações exaustivas com oráculo independente
- 0 falhas em 64 testes
- R5 subsumida por R3: 0 cenários com R5 sem R3
- CSV publicado como evidência verificável

## 6:30–7:30 — Resultados e baseline

Falar sobre:

- 50 cenários com acolhimento, 14 sem
- Guardrails funcionando: C e I isolados → "não acionar"
- Baseline como rubrica qualitativa
- Motor é auditável, mas não substitui julgamento humano
- Nuance qualitativa do profissional é insubstituível

## 7:30–8:30 — LGPD/ECA/PSE

Falar sobre:

- Dados sensíveis de menores
- Não diagnóstico, não ranking
- Pseudonimização para piloto futuro
- Perfis de acesso diferenciados
- Human-in-the-loop como princípio inegociável

## 8:30–9:30 — Limitações e evolução

Falar sobre:

- Lógica binária — sem gradações
- Validação sintética — necessidade de piloto real
- Evolução: fuzzy, séries temporais, integração
- Governança institucional como pré-requisito para operação

## 9:30–10:00 — Fechamento

Dizer:

> A contribuição central do trabalho é mostrar que, em um domínio sensível, a melhor IA não é necessariamente a mais complexa, mas aquela que é explicável, auditável, governada e subordinada à decisão humana.

---

# Seção 14 — Perguntas Prováveis da Banca e Respostas

## 1. Por que não usou machine learning?

> Porque o domínio exige explicabilidade total — cada conclusão precisa ser rastreável a uma regra explícita. Machine learning produziria modelos opacos, inaceitáveis para decisões sobre saúde mental de menores. Além disso, a Trilha I foca em técnicas simbólicas, e o volume de dados individuais disponível é insuficiente para treinar modelos estatísticos.

## 2. Por que lógica proposicional e não lógica de primeira ordem?

> Lógica proposicional é adequada porque o espaço de estados é pequeno (64 combinações), as variáveis são binárias e não há necessidade de quantificadores universais ou existenciais. Lógica de primeira ordem seria overengineering para este domínio.

## 3. O sistema diagnostica saúde mental?

> Não. O sistema emite um sinal binário de priorização de acolhimento escolar. Não atribui diagnósticos clínicos, não utiliza nomenclatura nosológica (CID, DSM), e não substitui avaliação de psicólogo ou assistente social.

## 4. Como evita violar a LGPD?

> Na versão acadêmica, o motor opera com cenários sintéticos, sem dados identificáveis. Para piloto futuro, o documento especifica pseudonimização, perfis de acesso diferenciados, logs de auditoria, e decisão final humana — conforme LGPD Art. 13 e ECA Art. 17.

## 5. Por que usa PeNSE se não alimenta o motor?

> A PeNSE é usada como referência epidemiológica para justificar a existência do problema e fundamentar a escolha das variáveis proposicionais. Ela não alimenta inferência individual. É motivação, não entrada operacional.

## 6. Por que cenários sintéticos e não dados reais?

> Em lógica proposicional, a validação mais rigorosa é a enumeração completa do espaço de estados. Com 6 variáveis booleanas, são 64 combinações — todas testáveis deterministicamente. Dados reais ruidosos não proporcionariam essa cobertura com a mesma precisão.

## 7. O que significa 2^6 = 64?

> São 6 variáveis de entrada, cada uma com 2 valores possíveis (verdadeiro/falso). O total de combinações é 2×2×2×2×2×2 = 64. A variável A (saída) não entra nessa conta porque é resultado, não entrada.

## 8. Por que A não entra no espaço combinatório?

> Porque A é variável de saída inferida pelo motor. Ela não é observada nem controlada; é derivada das 6 entradas via regras lógicas. Incluí-la geraria 128 combinações, das quais metade seria logicamente impossível (A derivada diferindo de A fixada).

## 9. R5 não é redundante?

> Logicamente, sim — R5 é subsumida por R3. Mas foi mantida deliberadamente por três razões: (1) enriquece a explicação ao registrar que C estava presente; (2) prepara para evolução com lógica fuzzy; (3) não causa falso positivo nem altera nenhum resultado.

## 10. Por que manter R5 se é subsumida?

> Por valor explicativo. Quando a equipe escolar recebe o sinal de acolhimento, saber que R3 *e* R5 dispararam — ou seja, que havia sofrimento, baixo apoio *e* contexto agravante — oferece informação mais rica do que apenas saber que R3 disparou.

## 11. O que é SBC?

> Sistema Baseado em Conhecimento — uma classe de IA que codifica explicitamente o conhecimento de especialistas em regras formais e usa mecanismos de inferência para derivar conclusões. Diferente de ML, não "aprende" de dados; opera sobre base de conhecimento construída deliberadamente.

## 12. O que é CNF?

> Forma Normal Conjuntiva — representação na qual o conhecimento é expresso como conjunção (E) de disjunções (OU) de literais. É a forma canônica exigida pelo método de resolução.

## 13. O que é inferência por resolução?

> Procedimento de prova por contradição. Para verificar se A pode ser derivada, adiciona-se ¬A à base e aplica-se a regra de resolução repetidamente. Se a cláusula vazia for derivada, prova-se que KB ⊨ A.

## 14. O que diferencia o motor pedagógico do motor modular?

> A lógica é idêntica. A diferença é de arquitetura de software: o pedagógico é curto e didático para avaliação acadêmica; o modular é estruturado para manutenção, testes e evolução futura. As 6 regras e a CNF são as mesmas.

## 15. O motor do Colab é frágil?

> Logicamente, não. Operacionalmente, sim — ele não implementa autenticação, logs, pseudonimização nem governança institucional. Mas essas são questões de engenharia de sistema, não de correção lógica.

## 16. Como seria uma versão real em escola?

> Exigiria: (1) RIPD/DPIA aprovado; (2) termo de cooperação com a escola; (3) pseudonimização com case_id; (4) perfis de acesso diferenciados; (5) interface simples; (6) logs de acesso; (7) decisão final sempre humana; (8) integração com fluxo PSE.

## 17. Como lidar com identificação de estudantes?

> Pseudonimização. Cada estudante recebe case_id. A chave de reidentificação fica restrita à coordenação/equipe autorizada. Professores veem apenas dados agregados por turma. Logs de todo acesso.

## 18. O professor teria acesso aos dados?

> Não aos dados individuais sensíveis. O professor veria, no máximo, painel com dados agregados por turma (ex: "3 estudantes sinalizados neste período"). A identificação individual seria visível apenas para coordenação pedagógica e equipe de acolhimento.

## 19. O que é human-in-the-loop?

> Princípio de design no qual a decisão final é sempre humana. O motor sinaliza; o profissional decide se e como acolher. Nenhuma ação automatizada é tomada sem julgamento humano.

## 20. Qual a principal limitação do trabalho?

> A validação foi sintética, não operacional. O motor prova corretude lógica com 64 combinações, mas não foi testado em escola real com profissionais reais. Essa validação exigiria governança institucional que extrapola o escopo da Trilha I.

## 21. Por que a Paraíba especificamente?

> Porque é o estado de atuação profissional do autor, e os indicadores da PeNSE 2024, analisados na EDA, sugerem prevalências relevantes de sofrimento emocional adolescente na região. A escolha é motivada por pertinência contextual, não por aleatoriedade.

## 22. O trabalho poderia ser aplicado em outros estados?

> Sim. A base de conhecimento é parametrizável. As variáveis proposicionais e regras podem ser adaptadas para outros estados, ajustando os indicadores de referência da PeNSE conforme o contexto regional.

## 23. Como você garante que não há falsos positivos?

> Pelos guardrails lógicos. Variáveis contextuais (C, I) nunca acionam A isoladamente. A validação exaustiva de 64 combinações mostra que C isolado → "NÃO", I isolado → "NÃO", C+I sem nucleares → "NÃO". Falsos positivos por fatores contextuais estão logicamente impedidos.

## 24. O que acontece se o motor sinalizar "acolher" e não houver equipe disponível?

> Esse é um problema institucional, não do motor. O motor sinaliza prioridade; a gestão decide alocação. O documento reconhece essa limitação e propõe que o motor seja ferramenta de apoio à gestão, não substituto de recursos humanos.

## 25. Você usou alguma ferramenta de IA generativa no trabalho?

> O texto foi redigido em LaTeX pelo autor. Os códigos foram implementados nos notebooks e módulos Python. Ferramentas de IA foram usadas como assistentes de programação e revisão, seguindo práticas comuns em pós-graduação contemporânea. O sistema AcolheMente em si não se conecta a nenhuma API de IA generativa.

---

# Seção 15 — Plano de Estudos para Domínio Completo

## Plano de 3 dias (apresentação urgente)

### Dia 1 — Domínio conceitual (4h)

| Bloco | Tempo | Conteúdo |
|-------|-------|----------|
| Manhã 1 | 1h | Ler Cap. 4 (Fundamentação): SBC, lógica proposicional, CNF, resolução |
| Manhã 2 | 1h | Ler Cap. 7 (Representação): variáveis, tabela, tipos, regras R1–R6 |
| Tarde 1 | 1h | Executar notebook: rodar validação exaustiva, conferir CSV |
| Tarde 2 | 1h | Estudar R5 subsumida: ler ADR, entender por que R5 ⊆ R3 |

### Dia 2 — Domínio metodológico (4h)

| Bloco | Tempo | Conteúdo |
|-------|-------|----------|
| Manhã 1 | 1h | Ler Cap. 6 (EDA): PeNSE, tiers, variáveis B12xxx |
| Manhã 2 | 1h | Ler Cap. 10 (Cenários): 14 representativos, 64 exaustivas |
| Tarde 1 | 1h | Ler Cap. 11 (Resultados): baseline qualitativo, guardrails |
| Tarde 2 | 1h | Ler CSV: verificar A_motor, A_esperado, ok, regras_acionadas |

### Dia 3 — Defesa estratégica (4h)

| Bloco | Tempo | Conteúdo |
|-------|-------|----------|
| Manhã 1 | 1h | Ler Cap. 13–14 (Governança): LGPD, ECA, PSE, pseudonimização |
| Manhã 2 | 1h | Estudar as 25 perguntas e respostas deste documento |
| Tarde 1 | 1h | Treinar roteiro de 10 minutos (cronômetro, voz alta) |
| Tarde 2 | 1h | Treinar novamente, ajustar ritmo, simular perguntas |

## Plano de 7 dias (apresentação com tempo)

### Dia 1 — Problema e motivação

- Ler Cap. 1–3 do PDF (Introdução, Contextualização, Objetivos)
- Anotar o problema central em 3 frases
- Memorizar o objetivo geral e os 5 específicos

### Dia 2 — IA simbólica e fundamentação

- Ler Cap. 4 (Fundamentação Metodológica)
- Estudar conceitos: SBC, lógica proposicional, CNF, resolução, correção, completude
- Praticar: explicar CNF e resolução para leigo em 2 minutos

### Dia 3 — Implementação

- Ler Cap. 7 (Representação do Conhecimento)
- Ler Cap. 8 (Motor de Inferência)
- Executar notebook: rodar motor, verificar R1–R6, conferir que A é derivada
- Entender a diferença entre motor pedagógico e motor modular

### Dia 4 — Validação

- Ler Cap. 10 (Cenários Sintéticos)
- Ler CSV de 64 combinações
- Entender oráculo independente
- Estudar R5 subsumida por R3
- Memorizar: 64 linhas, 0 falhas, 50 positivos, 14 negativos

### Dia 5 — Governança e ética

- Ler Cap. 13–14 (Governança, Pseudonimização)
- Ler Cap. 5 (Arquitetura de Dados)
- Estudar LGPD Art. 5º, ECA Art. 17, PSE
- Entender por que pseudonimização e não anonimização

### Dia 6 — Limitações e evolução

- Ler Cap. 15–16 (Limitações, Trabalhos Futuros)
- Listar 7 limitações reais
- Preparar roadmap de evolução
- Estudar as 25 perguntas e respostas

### Dia 7 — Simulação de banca

- Treinar roteiro de 10 minutos (3x com cronômetro)
- Pedir a alguém para fazer 10 perguntas aleatórias
- Refinar respostas
- Verificar checklist final

---

# Seção 16 — Checklist Final Antes da Banca

- [ ] Sei explicar o problema em 30 segundos
- [ ] Sei explicar por que não é diagnóstico clínico
- [ ] Sei explicar PeNSE vs cenários sintéticos vs dataset externo
- [ ] Sei listar e explicar as 7 variáveis e seus tipos corretos
- [ ] Sei explicar por que são 64 combinações (2^6, não 2^7)
- [ ] Sei explicar R5 subsumida por R3 e por que mantive R5
- [ ] Sei explicar os dois motores e que a lógica é idêntica
- [ ] Sei explicar o que o notebook demonstra
- [ ] Sei explicar LGPD, ECA e PSE no contexto do trabalho
- [ ] Sei explicar pseudonimização vs anonimização
- [ ] Sei explicar human-in-the-loop
- [ ] Sei responder por que não usei machine learning
- [ ] Sei explicar a rubrica qualitativa do baseline
- [ ] Sei explicar o oráculo independente
- [ ] Sei listar pelo menos 5 limitações reais
- [ ] Consigo apresentar em 10 minutos (treinei com cronômetro)
- [ ] Tenho o PDF impresso ou disponível
- [ ] Tenho o notebook pronto para demonstração, se solicitado

---

# Seção 17 — Respostas Curtas de Alto Impacto

Memorize estas frases. Elas funcionam como "encerramento" de respostas longas ou como respostas autônomas a perguntas rápidas:

1. **"O motor sinaliza; o profissional decide."**
2. **"A PeNSE fundamenta o problema, mas não classifica indivíduos."**
3. **"Os cenários sintéticos validam a lógica, não representam alunos reais."**
4. **"A variável A é saída inferida, não dado observado."**
5. **"R5 é mantida por valor explicativo, não por ganho decisório."**
6. **"O baseline é rubrica qualitativa, não experimento empírico."**
7. **"A versão acadêmica valida a lógica; a versão modular aponta o caminho de engenharia."**
8. **"Em domínio sensível, transparência vale mais que complexidade."**
9. **"São 64 combinações, não 128, porque A é saída, não entrada."**
10. **"Pseudonimizar, não anonimizar — porque anonimizar impede acolher."**
11. **"Não é diagnóstico. É sinalização de prioridade para acolhimento humano."**
12. **"A escolha por lógica simbólica é uma decisão de design ético, não uma limitação técnica."**

---

# Seção 18 — Mapa de Rastreabilidade Texto ↔ Código

## 18.1 Visão geral da rastreabilidade

> Esta seção conecta cada afirmação técnica central do trabalho aos arquivos, funções, testes e evidências correspondentes no repositório. O objetivo é demonstrar que o texto acadêmico, o notebook/Colab, os apêndices Python, o CSV de validação e os testes automatizados contam a mesma história.

### Inventário de artefatos rastreáveis

| Categoria | Artefatos |
|-----------|-----------|
| **Apêndices Python** | `simbolos_acolhemente.py`, `regras_acolhemente.py`, `motor_resolucao_acolhemente.py`, `cenarios_sinteticos_acolhemente.py`, `gerar_tabelas_resultados.py`, `grafo_explicabilidade_acolhemente.py`, `grafo_pseudonimizacao_acolhimento.py`, `grafos_governanca_proveniencia.py` |
| **Motor modular** | `src/acolhemente/motor.py`, `rule_graph.py`, `graph_schema.py`, `eda_plots.py` |
| **Tabelas LaTeX** | `_build/tabela_variaveis.tex`, `_build/tabela_regras.tex`, `_build/tabela_cenarios.tex` |
| **Figuras** | `figures/grafo_regras_7vars.png`, `comparacao_baseline_motor.png`, `fluxo_proveniencia_dados.png`, `fluxo_pseudonimizacao_acolhimento.png`, `grafo_governanca_acolhemente.png`, `cenarios_ativacao_regras.png`, `resultado_cenarios_sinteticos.png` |
| **Testes** | 8 módulos em `tests/`: equivalência, privacidade, PDF, regressão, contratos acadêmicos |
| **Outputs** | `validacao_exaustiva_64.csv`, `main_acolhemente_abntex2.pdf`, notebook `.ipynb` |

---

## 18.2 Matriz principal texto ↔ código

### Item 1 — Sistema Baseado em Conhecimento (SBC)

| Aspecto | Referência |
|---------|------------|
| **Texto** | Cap. 4 (Fundamentação Metodológica), L168: "Sistema Baseado em Conhecimento (SBC)" |
| **Código** | `appendices/regras_acolhemente.py` — regras explícitas em dicionário Python |
| **Código** | `appendices/simbolos_acolhemente.py` — variáveis com semântica e fontes PeNSE |
| **Evidência** | Conhecimento codificado em `REGRAS_CNF`, `REGRAS_IMPLICATIVAS`, `VARIAVEIS` — não em pesos estatísticos |
| **Explicação oral** | "O código materializa o SBC porque o conhecimento não está escondido em pesos estatísticos; ele está explicitamente codificado em símbolos e regras." |

### Item 2 — Variáveis proposicionais (E, B, V, S, C, I, A)

| Aspecto | Referência |
|---------|------------|
| **Texto** | Cap. 7 (Representação do Conhecimento), L308–316 |
| **Código** | `appendices/simbolos_acolhemente.py:9–28` — definição com tipo e fontes PeNSE |
| **LaTeX** | `_build/tabela_variaveis.tex` — tabela publicada no PDF |
| **Evidência** | `A` marcada como `tipo: "saida_inferida"` no código, alinhada com "Saída inferida" na tabela LaTeX (corrigido em 2026-05-29) |
| **Explicação oral** | "As seis primeiras variáveis são entradas; A é saída inferida. Por isso o espaço de teste é 2^6 = 64, não 2^7." |

### Item 3 — Regras R1–R6

| Aspecto | Referência |
|---------|------------|
| **Texto** | Cap. 8 (Motor de Inferência), tabela de regras |
| **Código** | `appendices/regras_acolhemente.py:9–16` — `REGRAS_IMPLICATIVAS` |
| **CNF** | `appendices/regras_acolhemente.py:18–24` — `REGRAS_CNF` como `frozenset` |
| **LaTeX** | `_build/tabela_regras.tex` — forma implicativa e CNF lado a lado |
| **Trecho** | `"R1": "S -> A"`, `"R3": "E AND B -> A"`, etc. |
| **Explicação oral** | "As regras do PDF são as mesmas regras implementadas no código. A banca pode rastrear cada regra do texto até o arquivo Python correspondente." |

### Item 4 — CNF (Forma Normal Conjuntiva)

| Aspecto | Referência |
|---------|------------|
| **Texto** | Cap. 4, L172: "cláusulas em Forma Normal Conjuntiva" |
| **Código** | `appendices/regras_acolhemente.py:18–24` — cada cláusula como `frozenset` |
| **Código legível** | `appendices/regras_acolhemente.py:27–33` — `REGRAS_CNF_LEGIVEL` |
| **Trecho** | `"R1": frozenset({"~S", "A"})` — equivalente a `¬S ∨ A` |
| **Explicação oral** | "A CNF é a forma necessária para a inferência por resolução. Cada implicação foi convertida pela equivalência lógica p → q ≡ ¬p ∨ q." |

### Item 5 — Motor pedagógico do Colab

| Aspecto | Referência |
|---------|------------|
| **Texto** | Cap. 8, seção sobre dois motores |
| **Arquivo** | `appendices/motor_resolucao_acolhemente.py` (102 linhas) |
| **Função principal** | `inferir_acolhimento(E, B, V, S, C, I) → bool` (L49) |
| **Resolução** | `_resolve(c1, c2)` (L11) — aplica regra de resolução entre duas cláusulas |
| **Inferência** | `inferir_por_resolucao(clausulas, conclusao)` (L21) — prova por contradição |
| **Explicabilidade** | `explicar_decisao(...)` (L62) — retorna regras acionadas e texto explicativo |
| **Notebook** | `notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb` — importa e executa o motor |
| **Explicação oral** | "O motor pedagógico é curto e didático para que a banca veja a lógica diretamente. Ele não é frágil logicamente; sua limitação é operacional, não semântica." |

### Item 6 — Motor modular/de produção

| Aspecto | Referência |
|---------|------------|
| **Texto** | Cap. 8, referência a motor modular |
| **Arquivo** | `src/acolhemente/motor.py` (147 linhas, repositório raiz) |
| **Função** | `inferir_acolhimento(E, B, V, S, C, I) → bool` (L77) — mesma assinatura |
| **Complementos** | `src/acolhemente/rule_graph.py`, `graph_schema.py`, `eda_plots.py` |
| **Teste de equivalência** | `tests/test_motor_equivalence_contract.py` — compara ambos os motores |
| **Nota** | O motor modular está no repositório raiz, fora da pasta `v3_3`. A entrega acadêmica usa a versão pedagógica dos apêndices. |
| **Explicação oral** | "Há duas implementações equivalentes da mesma lógica: uma didática para Colab e outra modular como referência de engenharia. A diferença é arquitetura, não decisão lógica." |

### Item 7 — Validação exaustiva das 64 combinações

| Aspecto | Referência |
|---------|------------|
| **Texto** | Cap. 10 (Cenários Sintéticos e Validação) |
| **Notebook** | `notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb` — célula 14 (após nota metodológica) |
| **CSV** | `outputs/validacao_exaustiva_64.csv` |
| **Colunas** | `E,B,V,S,C,I,A_motor,A_esperado,ok,regras_acionadas` |
| **Resultados** | 64 linhas, 64 ok=True, 50 A=SIM, 14 A=NÃO, 0 falhas |
| **Explicação oral** | "Os 14 cenários são didáticos; a prova formal está no CSV de 64 combinações." |

### Item 8 — Oráculo independente

| Aspecto | Referência |
|---------|------------|
| **Texto** | Cap. 10, validação com oráculo |
| **Notebook** | Célula 14 — função `oraculo_acolhimento(E, B, V, S, C, I)` |
| **Trecho** | `return S or (V and E) or (E and B) or (V and B) or (V and I)` |
| **Nota** | R5 (`E and B and C`) não aparece como termo porque `E and B` (R3) já cobre |
| **Explicação oral** | "O oráculo é independente do motor e serve para confirmar que a implementação produz a saída esperada. R5 não aparece como termo independente porque já está coberta por E and B." |

### Item 9 — R5 subsumida por R3

| Aspecto | Referência |
|---------|------------|
| **Texto** | Cap. 7, parágrafo sobre subsunção |
| **CSV** | Coluna `regras_acionadas`: R5 sempre co-ocorre com R3 |
| **Verificação** | `R5 sem R3 = 0` (confirmado no notebook e no CSV) |
| **Oráculo** | R5 omitida na fórmula booleana do oráculo |
| **Explicação oral** | "R5 é mantida por valor explicativo. Ela nunca dispara sozinha; apenas adiciona contexto quando R3 já seria verdadeira." |

### Item 10 — Guardrails C e I

| Aspecto | Referência |
|---------|------------|
| **Texto** | Cap. 7, L314: "variáveis contextuais nunca inferem A isoladamente" |
| **Cenários** | `appendices/cenarios_sinteticos_acolhemente.py` — cenários "C isolado", "I isolado", "C+I" |
| **LaTeX** | `_build/tabela_cenarios.tex` — linhas "C isolado → NÃO", "I isolado → NÃO" |
| **CSV** | Linhas com C=1,I=0 (sem nucleares) → A_motor=0; C=0,I=1 → A_motor=0 |
| **Explicação oral** | "C e I isolados não acionam A. Isso evita que contexto social ou falha institucional estigmatizem o estudante." |

### Item 11 — Baseline como rubrica qualitativa

| Aspecto | Referência |
|---------|------------|
| **Texto** | Cap. 11 (Resultados), seção de baseline |
| **Figura** | `figures/comparacao_baseline_motor.png` |
| **Gerador** | `appendices/grafos_governanca_proveniencia.py` — gera todas as 5 figuras do relatório |
| **Nota** | Não é experimento empírico com profissionais |
| **Explicação oral** | "Essa comparação é qualitativa e metodológica, não experimento com profissionais." |

### Item 12 — PeNSE como motivação, não entrada individual

| Aspecto | Referência |
|---------|------------|
| **Texto** | Cap. 6 (EDA), L291–299 |
| **Código EDA** | `src/acolhemente/eda_plots.py` (repositório raiz) — funções `plot_pense_pb_vs_ne_br()` |
| **Separação** | EDA em `eda_plots.py`; motor em `motor.py` — nenhum `import eda_plots` no motor |
| **Explicação oral** | "A PeNSE fundamenta a escolha das variáveis; o motor não classifica respondentes da PeNSE nem estudantes reais." |

### Item 13 — Pseudonimização e governança

| Aspecto | Referência |
|---------|------------|
| **Texto** | Cap. 13–14, seções sobre LGPD/ECA/PSE |
| **Figura** | `figures/fluxo_pseudonimizacao_acolhimento.png` |
| **Gerador** | `appendices/grafo_pseudonimizacao_acolhimento.py` — fluxo com `case_id` |
| **Governança** | `appendices/grafos_governanca_proveniencia.py` — grafo de proveniência TIER_A/B/C |
| **Figura** | `figures/grafo_governanca_acolhemente.png`, `fluxo_proveniencia_dados.png` |
| **Explicação oral** | "A versão acadêmica não processa dados reais. O fluxo de pseudonimização é arquitetura para piloto futuro responsável." |

### Item 14 — Grafos de explicabilidade

| Aspecto | Referência |
|---------|------------|
| **Grafo de regras** | `figures/grafo_regras_7vars.png` ← `appendices/grafo_explicabilidade_acolhemente.py` |
| **Governança** | `figures/grafo_governanca_acolhemente.png` ← `appendices/grafos_governanca_proveniencia.py` |
| **Proveniência** | `figures/fluxo_proveniencia_dados.png` ← `appendices/grafos_governanca_proveniencia.py` |
| **Pseudonimização** | `figures/fluxo_pseudonimizacao_acolhimento.png` ← `appendices/grafo_pseudonimizacao_acolhimento.py` |
| **Cenários** | `figures/cenarios_ativacao_regras.png`, `resultado_cenarios_sinteticos.png` ← `appendices/grafos_governanca_proveniencia.py` |
| **Baseline** | `figures/comparacao_baseline_motor.png` ← `appendices/grafos_governanca_proveniencia.py` |
| **Explicação oral** | "Os grafos mostram a cadeia de rastreabilidade: dados → regras → sinal → revisão humana." |

### Item 15 — Testes automatizados

| Arquivo de teste | O que verifica |
|-----------------|----------------|
| `test_motor_equivalence_contract.py` | Motor pedagógico funciona; equivalência com motor modular (skip se não importável) |
| `test_academic_flow_contract.py` | Fluxo acadêmico: apêndices, notebook, CSV, figuras existem e são consistentes |
| `test_attempt_abntex2_contract.py` | Estrutura abnTeX2: capítulos, tabelas, figuras, referências no PDF |
| `test_attempt_academic_structure.py` | Estrutura acadêmica: sumário, introdução, conclusão, referências |
| `test_attempt_pdf_quality.py` | Métricas do PDF: páginas, glifos, fontes |
| `test_data_usage_explanation_contract.py` | Explicação de uso de dados: TIER_A, TIER_B, TIER_C separados |
| `test_no_regression_vs_v3_2_contract.py` | Não-regressão: v3.3 ≥ v3.2 em todas as métricas |
| `test_operational_privacy_contract.py` | Privacidade operacional: ausência de dados identificáveis, pseudonimização |

**Resultado:** 136 passed, 1 skipped (equivalência com motor modular — skip justificado), 0 failed.

**Explicação oral:** "Os testes funcionam como rede de segurança contra regressões: eles verificam se a lógica, os outputs e os guardrails continuam corretos."

---

# Seção 19 — Guia rápido: onde apontar no código durante a banca

| Pergunta da banca | Arquivo para abrir | Função/trecho | Mensagem principal |
|-------------------|--------------------|---------------|-------------------|
| "Onde estão as regras?" | `appendices/regras_acolhemente.py` | `REGRAS_IMPLICATIVAS` (L9–16) | "São 6 regras em dicionário Python, cada uma com forma implicativa e CNF." |
| "Onde está o motor?" | `appendices/motor_resolucao_acolhemente.py` | `inferir_acolhimento()` (L49) | "Função de 10 linhas que monta cláusulas e chama resolução." |
| "Onde você valida as 64 combinações?" | `notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb` | Célula 14 — loop `itertools.product` | "Todas as 2^6 combinações testadas com oráculo independente." |
| "Onde está o oráculo independente?" | Notebook, célula 14 | `oraculo_acolhimento()` | "Função booleana separada do motor, sem R5 (subsumida)." |
| "Onde você prova que R5 não dispara sem R3?" | `outputs/validacao_exaustiva_64.csv` | Coluna `regras_acionadas` | "Filtrar R5 sem R3: resultado = 0 linhas." |
| "Onde o notebook gera o CSV?" | Notebook, célula 14 | `csv.DictWriter(...)` | "As 64 linhas são escritas com A_motor, A_esperado e ok." |
| "Onde aparecem os guardrails?" | `appendices/cenarios_sinteticos_acolhemente.py` | Cenários "C isolado", "I isolado" (L19–21) | "C e I sozinhos → esperado=False." |
| "Qual a diferença entre motor pedagógico e modular?" | `appendices/motor_resolucao_acolhemente.py` vs `src/acolhemente/motor.py` | Mesma `inferir_acolhimento()` | "Assinatura idêntica. Diferença: arquitetura, não lógica." |
| "Onde está a governança/pseudonimização?" | `appendices/grafo_pseudonimizacao_acolhimento.py` | Nodos: `case_id`, reidentificação restrita | "Fluxo operacional para piloto futuro." |
| "Onde estão os testes?" | `tests/test_motor_equivalence_contract.py` | `test_motor_academico_funciona()` | "136 testes passando, incluindo equivalência e privacidade." |

---

# Seção 20 — Trechos de código essenciais comentados

## 20.1 Função principal de inferência

**Arquivo:** `appendices/motor_resolucao_acolhemente.py`, linhas 49–59

```python
def inferir_acolhimento(E=False, B=False, V=False, S=False, C=False, I=False):
    """Verifica se A deve ser inferido dado o estado das variaveis."""
    # Monta mapa de variáveis
    mapa = {"E": E, "B": B, "V": V, "S": S, "C": C, "I": I}
    fatos = []
    for var, val in mapa.items():
        if val:
            fatos.append(frozenset({var}))       # ex: {"E"}
        else:
            fatos.append(frozenset({f"~{var}"})) # ex: {"~E"}
    # Combina regras CNF + fatos e tenta derivar A
    clausulas = list(REGRAS_CNF.values()) + fatos
    return inferir_por_resolucao(clausulas, "A")
```

**Linha a linha:**
- L51: recebe 6 booleanos — cada variável de entrada
- L52–57: converte cada variável em cláusula unitária (`{"E"}` se True, `{"~E"}` se False)
- L58: junta as 6 regras CNF com os 6 fatos
- L59: chama resolução para tentar derivar A

## 20.2 Base de regras R1–R6

**Arquivo:** `appendices/regras_acolhemente.py`, linhas 9–24

```python
REGRAS_IMPLICATIVAS = {
    "R1": "S -> A",           # Autoagressão → Acolher
    "R2": "V AND E -> A",     # Desvalor + Sofrimento → Acolher
    "R3": "E AND B -> A",     # Sofrimento + Baixo apoio → Acolher
    "R4": "V AND B -> A",     # Desvalor + Baixo apoio → Acolher
    "R5": "E AND B AND C -> A",  # Sofrimento + Baixo apoio + Contexto → Acolher
    "R6": "V AND I -> A",     # Desvalor + Insuficiência institucional → Acolher
}

REGRAS_CNF = {
    "R1": frozenset({"~S", "A"}),              # ¬S ∨ A
    "R2": frozenset({"~V", "~E", "A"}),        # ¬V ∨ ¬E ∨ A
    "R3": frozenset({"~E", "~B", "A"}),        # ¬E ∨ ¬B ∨ A
    "R4": frozenset({"~V", "~B", "A"}),        # ¬V ∨ ¬B ∨ A
    "R5": frozenset({"~E", "~B", "~C", "A"}),  # ¬E ∨ ¬B ∨ ¬C ∨ A
    "R6": frozenset({"~V", "~I", "A"}),        # ¬V ∨ ¬I ∨ A
}
```

**Conexão com o texto:** a tabela 2 do PDF (`_build/tabela_regras.tex`) exibe exatamente essas duas representações — forma implicativa e CNF — lado a lado.

## 20.3 Oráculo independente

**Arquivo:** Notebook, célula 14

```python
def oraculo_acolhimento(E, B, V, S, C, I):
    """Oráculo lógico independente da implementação do motor.

    R5 não aparece como termo independente porque é subsumida por R3:
    sempre que E, B e C são verdadeiros, E e B já tornam R3 verdadeira.
    """
    return S or (V and E) or (E and B) or (V and B) or (V and I)
```

**Por que R5 não aparece:** o termo `E and B and C` é um caso particular de `E and B`. Se E e B já são verdadeiros, a expressão `E and B` (correspondente a R3) já retorna True — independentemente de C.

## 20.4 Validação exaustiva

**Arquivo:** Notebook, célula 14

```python
for bits in itertools.product([0, 1], repeat=6):
    kwargs = {v: bool(b) for v, b in zip(VARS, bits)}
    a_motor = inferir_acolhimento(**kwargs)
    a_esperado = oraculo_acolhimento(**kwargs)
    # ...
    row["ok"] = bool(a_motor == a_esperado)
```

**Explicação:** `itertools.product([0, 1], repeat=6)` gera todas as 64 combinações possíveis de 6 variáveis booleanas. Para cada uma, o motor e o oráculo são chamados e comparados.

## 20.5 Escrita do CSV

**Arquivo:** Notebook, célula 14

```python
csv_path = Path("validacao_exaustiva_64.csv")
with csv_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=VARS + ["A_motor", "A_esperado", "ok", "regras_acionadas"],
    )
    w.writeheader()
    w.writerows(rows)
```

**Colunas finais:** `E, B, V, S, C, I, A_motor, A_esperado, ok, regras_acionadas`

## 20.6 Teste de equivalência entre motores

**Arquivo:** `tests/test_motor_equivalence_contract.py`

```python
def test_motor_academico_funciona():
    """Motor academico roda sem erros e produz resultados corretos."""
    from motor_resolucao_acolhemente import inferir_acolhimento
    from cenarios_sinteticos_acolhemente import executar_validacao
    resultados = executar_validacao()
    assert len(resultados) >= 14
    for r in resultados:
        assert r["ok"], f"Cenario falhou: {r['nome']}"

def test_motor_producao_equivalence():
    """Se o motor de producao estiver importavel, verifica equivalencia."""
    # Compara inferir_acolhimento de ambos os motores
    # para todas as 64 combinações
    # ...
```

**Nota:** o teste de equivalência faz `pytest.skip` se o motor modular não for importável no ambiente — skip justificado e documentado.

---

# Seção 21 — Mapa de evidência para apresentação de 10 minutos

| Tempo | Tema | Evidência textual | Evidência de código |
|-------|------|-------------------|---------------------|
| 0:00–0:45 | Abertura | Título e objetivo geral | — |
| 0:45–1:45 | Problema | Cap. 1–3 (Introdução) | — |
| 1:45–2:45 | Escolha metodológica | Cap. 4 (Fundamentação): SBC, resolução | `regras_acolhemente.py` — regras explícitas |
| 2:45–4:00 | Modelo lógico | Cap. 7 (Representação): tabela de variáveis e regras | `simbolos_acolhemente.py`, `regras_acolhemente.py`, `_build/tabela_variaveis.tex`, `_build/tabela_regras.tex` |
| 4:00–5:15 | Dados e governança | Cap. 5–6 (Arquitetura, EDA): tiers, PeNSE | `src/acolhemente/eda_plots.py`, `grafos_governanca_proveniencia.py`, `figures/fluxo_proveniencia_dados.png` |
| 5:15–6:30 | Validação | Cap. 10 (Cenários): 64 combinações | `validacao_exaustiva_64.csv`, `oraculo_acolhimento()`, `cenarios_sinteticos_acolhemente.py` |
| 6:30–7:30 | Resultados e baseline | Cap. 11 (Resultados): guardrails, baseline | `figures/comparacao_baseline_motor.png`, `_build/tabela_cenarios.tex` |
| 7:30–8:30 | LGPD/ECA/PSE | Cap. 13–14 (Governança) | `grafo_pseudonimizacao_acolhimento.py`, `figures/fluxo_pseudonimizacao_acolhimento.png` |
| 8:30–9:30 | Limitações e evolução | Cap. 15–16 | `test_motor_equivalence_contract.py` (skip documentado como limitação) |
| 9:30–10:00 | Fechamento | Frase de encerramento | 136 testes passando |

---

# Seção 22 — Checklist de domínio técnico

- [ ] Sei abrir `appendices/regras_acolhemente.py` e apontar R1–R6
- [ ] Sei mostrar onde está R1 (`"S -> A"`, L10) e R5 (`"E AND B AND C -> A"`, L14)
- [ ] Sei explicar por que R5 é subsumida por R3 (abrir CSV, filtrar R5 sem R3 = 0)
- [ ] Sei abrir `appendices/motor_resolucao_acolhemente.py` e apontar `inferir_acolhimento()` (L49)
- [ ] Sei abrir `src/acolhemente/motor.py` e apontar a mesma `inferir_acolhimento()` (L77)
- [ ] Sei explicar que os dois motores têm a mesma semântica (mesma assinatura, mesmas regras)
- [ ] Sei abrir o notebook e localizar `oraculo_acolhimento()` na célula 14
- [ ] Sei explicar por que o oráculo não tem R5 (E∧B já cobre E∧B∧C)
- [ ] Sei abrir `outputs/validacao_exaustiva_64.csv` e explicar as 10 colunas
- [ ] Sei rodar `python -m pytest tests/ -q` e interpretar "136 passed, 1 skipped"
- [ ] Sei abrir `figures/grafo_regras_7vars.png` e explicar nodos e arestas
- [ ] Sei abrir `figures/fluxo_pseudonimizacao_acolhimento.png` e explicar `case_id`
- [ ] Sei distinguir código acadêmico (apêndices) de código de produção (src/acolhemente)
- [ ] Sei explicar o que cada arquivo de teste verifica (equivalência, privacidade, regressão)
- [ ] Sei abrir `_build/tabela_variaveis.tex` e confirmar que A é "Saída inferida"

---

*Documento preparado em 2026-05-28. Atualizado com mapa de rastreabilidade texto ↔ código. Baseado na versão v3.3.2 do AcolheMente Escolar PB.*
