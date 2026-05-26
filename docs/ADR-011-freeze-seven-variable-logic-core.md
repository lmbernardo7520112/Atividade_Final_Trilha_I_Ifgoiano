# ADR-011: Congelamento do Motor Lógico de 7 Variáveis para Entrega da Trilha I

## Status
**APROVADO** — 2026-05-26

## Contexto
O motor lógico AcolheMente Escolar PB evoluiu de 5 para 7 variáveis proposicionais
na versão v0.3.0, adicionando as variáveis contextuais C (Contexto comportamental
agravante) e I (Insuficiência institucional de resposta), bem como as regras R5
(E ∧ B ∧ C → A) e R6 (V ∧ I → A).

O Council deliberou que esta configuração atinge o ponto ótimo entre:
- **Expressividade escolar:** as 7 variáveis capturam fatores emocionais, sociais,
  comportamentais e institucionais relevantes para acolhimento.
- **Simplicidade acadêmica:** o motor permanece compreensível para avaliador da
  Trilha I, com regras explícitas em CNF e inferência por resolução.
- **Governança ética:** todas as proibições (diagnóstico, ranking, dados identificáveis,
  merge indevido, API externa) estão implementadas e testadas.

## Decisão

### Congelamento declarado:
1. **O motor possui exatamente 7 variáveis proposicionais**, organizadas em:
   - 5 variáveis nucleares: E, B, V, S, A
   - 2 variáveis contextuais de modulação: C, I
2. **O motor possui exatamente 6 regras lógicas** (R1–R6), todas em CNF.
3. **A é a única conclusão operacional** — nenhuma outra variável é saída do motor.
4. **C e I não inferem A isoladamente** — C requer E∧B (R5); I requer V (R6).
5. **Nenhuma nova variável ou regra será adicionada** na entrega da Trilha I.
6. Expansões futuras (≥ v0.4.0) poderão ser propostas em ADR separado, fora do escopo
   da entrega acadêmica.

### Justificativa:
- A parcimônia de 7 variáveis e 6 regras é suficiente para demonstrar a técnica
  de Lógica Proposicional com Inferência por Resolução.
- Expansões adicionais arriscariam ultrapassar o escopo esperado para a Trilha I.
- As variáveis contextuais C e I já representam a contribuição diferencial do projeto
  em relação ao notebook-base (`Resposta_Trabalho_Trilha_I.ipynb`).

## Consequências

### Positivas
- Escopo acadêmico estabilizado para entrega.
- CI gates (62+ testes) validam o congelamento.
- Documentação (README, SDD, MODEL_CARD, CHANGELOG) reflete o estado final.

### Negativas
- Variáveis potencialmente relevantes (ex: bullying, uso de substâncias) ficam
  fora do escopo v0.3.x.
- Regras mais granulares (ex: E ∧ V ∧ I → A) não serão exploradas nesta versão.

## Referências
- ADR-009: Deterministic Knowledge Graph for Explainability
- implementation_plan_revisado_1.md (v3)
- relatorio_7vars.md
