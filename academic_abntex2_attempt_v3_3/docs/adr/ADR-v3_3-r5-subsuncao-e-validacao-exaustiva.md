# ADR-v3.3: R5 — Subsunção e Validação Exaustiva

> **Status:** Aceito
> **Data:** 2026-05-28
> **Contexto:** Versão v3.3 (excellence closure)

## 1. Contexto

A regra R5 do AcolheMente é definida como:

```
R5: E ∧ B ∧ C → A
```

Ou seja, sofrimento emocional + baixo apoio socioafetivo + contexto comportamental
agravante implica acolhimento prioritário.

A regra R3 é:

```
R3: E ∧ B → A
```

Observa-se que **R3 subsume R5**: sempre que R5 é verdadeira (E=1, B=1, C=1),
R3 também é verdadeira (pois E=1 e B=1 já bastam). Portanto, R5 nunca é a
*única* regra que aciona A — R3 sempre a acompanha.

## 2. Decisão

**R5 é mantida** na base de conhecimento, apesar da subsunção, pelos seguintes
motivos:

1. **Explicabilidade enriquecida:** Quando R5 dispara junto com R3, a explicação
   ao profissional humano inclui o fator contextual C, oferecendo informação
   adicional sobre o contexto comportamental agravante. Remover R5 perderia
   essa informação na saída explicativa.

2. **Preparação para evolução:** Em versões futuras com lógica fuzzy ou graus de
   urgência, R5 poderia contribuir para um *score* de prioridade mais alto que
   R3 sozinha, justificando sua presença na base.

3. **Registro de intenção:** R5 documenta a intenção explícita de que o contexto
   comportamental agravante é relevante para a priorização, mesmo que
   logicamente redundante na versão booleana.

4. **Sem efeito colateral:** A presença de R5 não introduz falsos positivos nem
   altera o resultado de nenhum dos 64 cenários. A subsunção é inofensiva.

## 3. Validação

A validação exaustiva de todas as $2^6 = 64$ combinações confirma:

- Cenários onde R5 dispara: R3 **sempre** dispara simultaneamente.
- Nenhum cenário existe onde R5 é a *única* regra acionada.
- O resultado de A (sim/não) é idêntico com e sem R5.
- A diferença é apenas na lista de regras reportadas na explicação.

O CSV `outputs/validacao_exaustiva_64.csv` registra todas as 64 combinações com
colunas `E,B,V,S,C,I,A,regras_acionadas`.

## 4. Consequências

- R5 permanece na base de conhecimento.
- A subsunção é documentada no PDF (Capítulo 10 e Capítulo 13).
- A validação exaustiva é registrada em CSV e no notebook.
- Nenhuma alteração nas regras R1-R6, CNF ou motor.
