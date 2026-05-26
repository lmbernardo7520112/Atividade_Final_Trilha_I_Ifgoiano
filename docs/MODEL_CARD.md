# MODEL_CARD.md — AcolheMente Escolar PB

## Informações do Modelo

| Campo | Valor |
|-------|-------|
| **Nome** | AcolheMente Escolar PB |
| **Tipo** | Sistema Baseado em Conhecimento (SBC) |
| **Técnica** | Lógica Proposicional + Inferência por Resolução (CNF) |
| **Domínio** | Saúde mental escolar — Paraíba, Brasil |
| **Saída** | Acolhimento humano prioritário (binário: sim/não) |
| **Versão** | v0.3.0 (7 variáveis, 6 regras) |

## Variáveis de Entrada

### 5 Nucleares
- **E** — Sofrimento emocional recorrente (PeNSE: B12004, B12005, B12007)
- **B** — Baixo apoio socioafetivo percebido (PeNSE: B12003, B07004)
- **V** — Indicador crítico de desvalor da vida (PeNSE: B12008)
- **S** — Sinal autorreferido de autoagressão (PeNSE: B12009)

### 2 Contextuais
- **C** — Contexto comportamental agravante (PeNSE: B03010C, B03006B)
- **I** — Insuficiência institucional de resposta (PeNSE: E01P60, E01P117)

### Variável de Saída
- **A** — Acolhimento humano prioritário (única conclusão operacional)

## Base de Conhecimento (6 regras)

| Regra | Lógica | CNF |
|-------|--------|-----|
| R1 | S → A | ¬S ∨ A |
| R2 | V ∧ E → A | ¬V ∨ ¬E ∨ A |
| R3 | E ∧ B → A | ¬E ∨ ¬B ∨ A |
| R4 | V ∧ B → A | ¬V ∨ ¬B ∨ A |
| R5 | E ∧ B ∧ C → A | ¬E ∨ ¬B ∨ ¬C ∨ A |
| R6 | V ∧ I → A | ¬V ∨ ¬I ∨ A |

## Limitações

1. **Não é diagnóstico:** O sistema não gera diagnóstico clínico de nenhuma condição.
2. **Não é predição:** O sistema não prediz comportamento futuro.
3. **Não usa ML/DL:** Não há modelo treinado; as regras são explícitas e determinísticas.
4. **Não classifica indivíduos:** O sistema opera sobre cenários, não sobre alunos reais.
5. **Não substitui profissional:** Toda saída requer revisão humana obrigatória.
6. **C e I não inferem A isoladamente:** São variáveis de modulação contextual.
7. **Dataset externo não infere sobre Brasil:** Apenas benchmark metodológico.

## Considerações Éticas

- Nenhum dado identificável é processado (LGPD compliance)
- Nenhuma classificação de menor (ECA compliance)
- Human-in-the-Loop obrigatório em toda decisão
- Sem ranking de estudantes
- Sem linguagem diagnóstica em nenhum artefato
- Grafo de explicabilidade audita toda decisão

## Uso Pretendido

Ferramenta de suporte à decisão para equipes pedagógicas, psicólogos escolares e
coordenadores do PSE, auxiliando na priorização de acolhimento em saúde mental escolar.

## Uso NÃO Pretendido

- Diagnóstico clínico automatizado
- Substituição de consulta com profissional de saúde
- Vigilância ou monitoramento discente
- Ranking ou classificação de alunos
- Inferência epidemiológica a partir de dados externos
