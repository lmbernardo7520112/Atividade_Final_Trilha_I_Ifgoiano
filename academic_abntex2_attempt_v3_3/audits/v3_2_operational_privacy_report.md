# Relat\u00f3rio de Privacidade Operacional v3.2

> **Vers\u00e3o:** academic_abntex2_attempt_v3_2
> **Data:** 2026-05-27
> **Base:** academic_abntex2_attempt_v3_1

## 1. Confirma\u00e7\u00e3o de Origem

- v3_2 criada a partir de `cp -a academic_abntex2_attempt_v3_1 academic_abntex2_attempt_v3_2`
- Hash v3_1 .tex: `61a9b0875af24d8affdd0b0e45986c6d`
- v3_1 **inalterada** ap\u00f3s edi\u00e7\u00f5es da v3_2: **confirmado**
- Nada fora de `academic_abntex2_attempt_v3_2/` foi alterado

## 2. Resumo da Nova Discuss\u00e3o

A v3.2 adiciona discuss\u00e3o conceitual, \u00e9tica e arquitetural sobre:

- **Anonimiza\u00e7\u00e3o irrevers\u00edvel:** adequada para relat\u00f3rios, pain\u00e9is agregados e pesquisa, mas incomp\u00e1tivel com acolhimento individual real (n\u00e3o \u00e9 poss\u00edvel saber quem acolher)
- **Pseudonimiza\u00e7\u00e3o:** motor recebe `case_id` + vari\u00e1veis booleanas m\u00ednimas; n\u00e3o conhece nome, matr\u00edcula, CPF, telefone
- **Reidentifica\u00e7\u00e3o restrita:** chave segregada, sob cust\u00f3dia da equipe m\u00ednima autorizada, com registro audit\u00e1vel
- **Perfis de acesso:** 5 perfis (Professor, Coordena\u00e7\u00e3o, Dire\u00e7\u00e3o, PSE/UBS/CAPS, Painel anal\u00edtico) com permiss\u00f5es expl\u00edcitas
- **DPIA/RIPD:** mencionado como requisito para piloto operacional
- **Pol\u00edtica de reten\u00e7\u00e3o e descarte:** referenciada
- **Logs de acesso:** obrigat\u00f3rios e audit\u00e1veis

## 3. Localiza\u00e7\u00e3o Exata dos Par\u00e1grafos Adicionados

| Local | Conte\u00fado | Linhas aprox. |
|-------|----------|---------------|
| Cap. 5 (ap\u00f3s Tabela de tiers) | `\subsection*{Anonimiza\u00e7\u00e3o, pseudonimiza\u00e7\u00e3o e reidentifica\u00e7\u00e3o restrita}` + 7 par\u00e1grafos + tabela de perfis + figura de fluxo | ~60 linhas |
| Cap. 13 (Discuss\u00e3o Cr\u00edtica) | 3 par\u00e1grafos sobre tens\u00e3o privacidade/a\u00e7\u00e3o | ~12 linhas |
| Cap. 14 (Perspectiva) | 2 par\u00e1grafos sobre DPIA/RIPD, protocolo, treinamento, logs | ~10 linhas |
| Cap. 15 (Conclus\u00e3o) | 1 par\u00e1grafo sobre pseudonimiza\u00e7\u00e3o em piloto operacional | ~4 linhas |
| Ap\u00eandice I | Novo ap\u00eandice: Fluxo Operacional Pseudonimizado | ~3 linhas |

## 4. Figura Criada

- **Arquivo:** `figures/fluxo_pseudonimizacao_acolhimento.png` (183 KB)
- **Script:** `appendices/grafo_pseudonimizacao_acolhimento.py`
- **Conte\u00fado:** 8 n\u00f3s de fluxo + 4 n\u00f3s de proibi\u00e7\u00e3o (motor n\u00e3o v\u00ea nome, painel n\u00e3o mostra ranking, professores n\u00e3o acessam chave, GitHub n\u00e3o recebe dados reais)

## 5. Tabela de Perfis de Acesso

- **Label:** `tab:perfis_acesso`
- **5 perfis:** Professor, Coordena\u00e7\u00e3o/orienta\u00e7\u00e3o, Dire\u00e7\u00e3o/equipe designada, PSE/UBS/CAPS, Painel anal\u00edtico
- **Colunas:** Perfil, Pode visualizar, N\u00e3o pode visualizar, Finalidade
- **Referenciada no texto:** sim (Tabela~\\ref{tab:perfis_acesso})

## 6. Testes Adicionados

| Arquivo | Checks | Resultado |
|---------|--------|-----------|
| `test_operational_privacy_contract.py` | 25 checks | \u2705 25/25 passed |
| `test_attempt_pdf_quality.py` (v3.2 additions) | 10 checks | \u2705 10/10 passed |

## 7. Resultado do pytest

```
125 passed, 1 skipped, 0 failed
```

| Suite | Resultado |
|-------|-----------|
| `test_academic_flow_contract.py` | \u2705 21/21 passed |
| `test_attempt_academic_structure.py` | \u2705 18/18 passed |
| `test_attempt_abntex2_contract.py` | \u2705 9/9 passed |
| `test_attempt_pdf_quality.py` | \u2705 29/29 passed |
| `test_data_usage_explanation_contract.py` | \u2705 20/20 passed |
| `test_motor_equivalence_contract.py` | \u2705 1 passed, 1 skipped |
| `test_operational_privacy_contract.py` | \u2705 25/25 passed |
| **Total** | **125 passed, 1 skipped, 0 failed** |

## 8. Status do PDF

| M\u00e9trica | Valor |
|---------|-------|
| P\u00e1ginas | 71 |
| Tamanho | 1.6 MB |
| Erros fatais | 0 |
| Figuras | 7 (+1 nova) |
| Tabelas | 5 (+1 nova) |
| `\section{}` no corpo | 0 |
| `\subsection*{}` no corpo | 1 (n\u00e3o numerada) |
| Ap\u00eandices | 9 (+1 novo) |
| Glifos corrompidos | 0 |
| Bordas em links | Nenhuma |

## 9. Caminho do PDF Final

`academic_abntex2_attempt_v3_2/outputs/main_acolhemente_abntex2.pdf`

## 10. Decis\u00e3o

> **\u2705 APROVADO.** A v3.2 fecha a lacuna conceitual sobre anonimiza\u00e7\u00e3o vs. pseudonimiza\u00e7\u00e3o, adicionando discuss\u00e3o acad\u00eamica fluida sobre como o AcolheMente funcionaria em piloto real sem expor estudantes. O motor permanece intacto. O sum\u00e1rio continua limpo. Todos os 125 testes passam.
