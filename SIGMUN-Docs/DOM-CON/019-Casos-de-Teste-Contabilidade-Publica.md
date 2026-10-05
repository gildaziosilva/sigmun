# 019 – Casos de Teste – Contabilidade Pública

#### Casos de Teste – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-019

**Domínio:** Contabilidade Pública

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Contabilidade-Publica.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000C-HIERARQUIA-DOCUMENTAL-v1.0.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `AUDITORIA-DOM-CON-2026-09-30.md`

---

# 1. Finalidade

Este artefato especifica os casos de teste do domínio de Contabilidade Pública,
organizados por suíte e rastreados aos critérios de aceitação, requisitos e regras que
verificam.

---

# 2. Convenções

* Identificador `CT-CON-<grupo><sequencial>`.
* Cada caso declara Given/When/Then e o artefato rastreado.
* A coluna **Estado** indica se o caso está implementado na suíte atual.

---

# 3. Suíte CT-01 — Máquina de Estados do Empenho

| ID | Cenário | Rastreia | Estado |
| --- | --- | --- | --- |
| CT-CON-001 | Empenho inicia em EMITIDO ao ser criado | RN-CON-004 | Não implementado |
| CT-CON-002 | Liquidar valor move EMITIDO para LIQUIDADO | RN-CON-003, CA-CON-002.1 | Parcial |
| CT-CON-003 | Liquidar mantém EMITIDO se já liquidado parcialmente | RN-CON-003 | Não implementado |
| CT-CON-004 | Liquidar acima do saldo a liquidar é recusado | RN-CON-021, CA-CON-002.3 | Parcial |
| CT-CON-005 | Liquidar valor não positivo é recusado | RN-CON-021 | Não implementado |
| CT-CON-006 | Estorno zera liquidado e retorna a EMITIDO | RN-CON-004 | Não implementado |
| CT-CON-007 | Estorno que comprometeria valor pago é recusado | RN-CON-004 | Não implementado |
| CT-CON-008 | Pagamento total move LIQUIDADO para PAGO | RN-CON-031, CA-CON-003.5 | Não implementado |
| CT-CON-009 | Pagamento acima do saldo a pagar é recusado | RN-CON-031 | Não implementado |
| CT-CON-010 | Anulação integral move para ANULADO | RN-CON-002, CA-CON-004.2 | Não implementado |
| CT-CON-011 | Anulação parcial mantém estado | RN-CON-002 | Não implementado |
| CT-CON-012 | Empenho PAGO não pode ser cancelado | RN-CON-004, CA-CON-004.6 | Não implementado |

---

# 4. Suíte CT-02 — Invariantes de Saldo

| ID | Cenário | Rastreia | Estado |
| --- | --- | --- | --- |
| CT-CON-013 | `valor_liquido` = empenhado − anulado | RN-CON-003 | Não implementado |
| CT-CON-014 | `saldo_a_liquidar` = líquido − liquidado | RN-CON-003 | Parcial |
| CT-CON-015 | `saldo_a_pagar` = liquidado − pago | RN-CON-031 | Não implementado |
| CT-CON-016 | Liquidações parciais não excedem o saldo | RN-CON-021 | Não implementado |
| CT-CON-017 | Pagamentos parciais não excedem o saldo | RN-CON-031 | Não implementado |
| CT-CON-018 | Anulação não excede o saldo a liquidar | RN-CON-002 | Não implementado |
| CT-CON-019 | Diferença de arredondamento inferior a 0,005 é aceita | RN-CON-050 | Não implementado |
| CT-CON-020 | Diferença de arredondamento igual ou superior é recusada | RN-CON-050 | Não implementado |
| CT-CON-021 | Saldos com três casas decimais são tratados corretamente | RN-CON-050 | Não implementado |
| CT-CON-022 | Sequência de anulação e liquidação mantém coerência | RN-CON-002, RN-CON-003 | Não implementado |

---

# 5. Suíte CT-03 — Integração com DOM-ORC

| ID | Cenário | Rastreia | Estado |
| --- | --- | --- | --- |
| CT-CON-023 | Empenho debita a dotação pelo valor exato | RN-CON-002, CA-CON-001.1 | Não implementado |
| CT-CON-024 | Empenho sem saldo é recusado | RN-CON-002, CA-CON-001.5 | Não implementado |
| CT-CON-025 | Anulação devolve o valor à dotação | RN-CON-002, CA-CON-004.2 | Não implementado |
| CT-CON-026 | Número duplicado no exercício é recusado | RN-CON-001, CA-CON-001.2 | Não implementado |
| CT-CON-027 | Falha na gravação do empenho reverte o débito | RNF-CON-005 | Não implementado |
| CT-CON-028 | Duas emissões simultâneas não criam duplicidade | A-02 | Não implementado |

---

# 6. Suíte CT-04 — Regras do PCASP

| ID | Cenário | Rastreia | Estado |
| --- | --- | --- | --- |
| CT-CON-029 | Criar conta com código único | RN-CON-010, CA-CON-005.1 | Implementado |
| CT-CON-030 | Criar conta com código duplicado é recusado | RN-CON-010, CA-CON-005.2 | Parcial |
| CT-CON-031 | Criar conta sem código ou nome é recusado | RN-CON-010, CA-CON-005.3 | Parcial |
| CT-CON-032 | Lançamento em conta sintética é recusado | RN-CON-011, CA-CON-005.5 | Não implementado |
| CT-CON-033 | Lançamento em conta inativa é recusado | RN-CON-012, CA-CON-005.6 | Não implementado |
| CT-CON-034 | Lançamento em conta analítica ativa é aceito | RN-CON-011 | Parcial |
| CT-CON-035 | Desativar conta impede novo lançamento | RN-CON-012 | Não implementado |
| CT-CON-036 | Reativar conta restabelece o lançamento | RN-CON-012 | Não implementado |

---

# 7. Suíte CT-05 — Partidas Dobradas

| ID | Cenário | Rastreia | Estado |
| --- | --- | --- | --- |
| CT-CON-037 | Lançamento com duas partidas balanceadas é lançado | RN-CON-050, CA-CON-006.1 | Implementado |
| CT-CON-038 | Lançamento desequilibrado é recusado | RN-CON-050, CA-CON-006.3 | Implementado |
| CT-CON-039 | Lançamento com uma única partida é recusado | RN-CON-050, CA-CON-006.2 | Parcial |
| CT-CON-040 | Conta inexistente na partida é recusada | RN-CON-051, CA-CON-006.4 | Não implementado |
| CT-CON-041 | Conta que não aceita lançamento é recusada | RN-CON-051, CA-CON-006.5 | Parcial |
| CT-CON-042 | Estorno de lançamento lançado é permitido | RF-CON-031 | Não implementado |

---

# 8. Suíte CT-06 — Conciliação

| ID | Cenário | Rastreia | Estado |
| --- | --- | --- | --- |
| CT-CON-043 | Saldos iguais geram conciliação concluída | RN-CON-060, CA-CON-007.1 | Implementado |
| CT-CON-044 | Saldos diferentes com justificativa geram divergência | RN-CON-061, CA-CON-007.2 | Não implementado |
| CT-CON-045 | Saldos diferentes sem justificativa são recusados | RN-CON-061, CA-CON-007.3 | Não implementado |
| CT-CON-046 | Diferença é arredondada a duas casas | RN-CON-060 | Não implementado |
| CT-CON-047 | Mês fora do intervalo é rejeitado | RNF-018 | Parcial |

---

# 9. Suíte CT-07 — Persistência

| ID | Cenário | Rastreia | Estado |
| --- | --- | --- | --- |
| CT-CON-048 | Empenho sobrevive ao round-trip com todos os campos | A-01 | Não implementado |
| CT-CON-049 | Liquidação sobrevive ao round-trip com data de liquidação | A-01 | Não implementado |
| CT-CON-050 | Pagamento sobrevive ao round-trip com data de efetivação | A-01 | Não implementado |
| CT-CON-051 | Lançamento sobrevive ao round-trip com data de competência | A-01 | Não implementado |
| CT-CON-052 | Conta sobrevive ao round-trip com grupo do PCASP | A-01 | Não implementado |
| CT-CON-053 | Registro excluído logicamente não é recuperado | — | Não implementado |

---

# 10. Suíte CT-08 — API

| ID | Cenário | Rastreia | Estado |
| --- | --- | --- | --- |
| CT-CON-054 | Emissão de empenho responde 201 | RF-CON-001 | Não implementado |
| CT-CON-055 | Dotação inexistente responde 404 | A-06 | Não implementado |
| CT-CON-056 | Número duplicado responde 409 | A-06 | Não implementado |
| CT-CON-057 | Saldo insuficiente responde 422 | A-06 | Não implementado |
| CT-CON-058 | Liquidação responde 200 | RF-CON-006 | Não implementado |
| CT-CON-059 | Anulação responde 200 | RF-CON-014 | Não implementado |
| CT-CON-060 | Pagamento responde 201 | RF-CON-010 | Não implementado |
| CT-CON-061 | Criação de conta responde 201 | RF-CON-017 | Não implementado |
| CT-CON-062 | Lançamento responde 201 | RF-CON-021 | Não implementado |
| CT-CON-063 | Conciliação responde 201 | RF-CON-025 | Não implementado |
| CT-CON-064 | Sete rotas constam no OpenAPI | C-01 | Não implementado |
| CT-CON-065 | Tag do domínio consta no OpenAPI | C-01 | Não implementado |
| CT-CON-066 | Payload inválido responde 422 | RNF-018 | Não implementado |
| CT-CON-067 | Acesso sem autorização é recusado | RNF-CON-007 | Não implementado |

---

# 11. Resumo de Cobertura

| Suíte | Casos | Implementados | Parciais | Cobertura |
| --- | --- | --- | --- | --- |
| CT-01 Estados | 12 | 0 | 2 | 17 % |
| CT-02 Invariantes | 10 | 0 | 1 | 10 % |
| CT-03 DOM-ORC | 6 | 0 | 0 | 0 % |
| CT-04 PCASP | 8 | 1 | 2 | 25 % |
| CT-05 Partidas | 6 | 2 | 2 | 50 % |
| CT-06 Conciliação | 5 | 1 | 1 | 40 % |
| CT-07 Persistência | 6 | 0 | 0 | 0 % |
| CT-08 API | 14 | 0 | 0 | 0 % |
| **Total** | **67** | **4** | **8** | **12 %** |

---

# 12. Prioridade de Implementação

| Prioridade | Casos | Justificativa |
| --- | --- | --- |
| 1 | CT-01 e CT-02 (22 casos) | Invariantes financeiras e transições de estado |
| 2 | CT-03 (6 casos) | Integridade com o orçamento |
| 3 | CT-08 (14 casos) | Só é possível após a exposição da API |
| 4 | CT-04 e CT-05 (14 casos) | Correção contábil |
| 5 | CT-07 (6 casos) | Só após a Onda 1 do plano |
| 6 | CT-06 (5 casos) | Conciliação |


---

Este artefato especifica os casos de teste do domínio de Contabilidade Pública,
organizados por suíte e rastreados aos critérios de aceitação, requisitos e regras que
verificam.

---

# 2. Convenções

* Identificador `CT-CON-<grupo><sequencial>`.
* Cada caso declara Given/When/Then e o artefato rastreado.
* A coluna **Estado** indica se o caso está implementado na suíte atual.

---

# 3. Suíte CT-01 — Máquina de Estados do Empenho

| ID | Cenário | Rastreia | Estado |
| --- | --- | --- | --- |
| CT-CON-001 | Empenho inicia em EMITIDO ao ser criado | RN-CON-004 | Não implementado |
| CT-CON-002 | Liquidar valor move EMITIDO para LIQUIDADO | RN-CON-003, CA-CON-002.1 | Parcial |
| CT-CON-003 | Liquidar mantém EMITIDO se já liquidado parcialmente | RN-CON-003 | Não implementado |
| CT-CON-004 | Liquidar acima do saldo a liquidar é recusado | RN-CON-021, CA-CON-002.3 | Parcial |
| CT-CON-005 | Liquidar valor não positivo é recusado | RN-CON-021 | Não implementado |
| CT-CON-006 | Estorno zera liquidado e retorna a EMITIDO | RN-CON-004 | Não implementado |
| CT-CON-007 | Estorno que comprometeria valor pago é recusado | RN-CON-004 | Não implementado |
| CT-CON-008 | Pagamento total move LIQUIDADO para PAGO | RN-CON-031, CA-CON-003.5 | Não implementado |
| CT-CON-009 | Pagamento acima do saldo a pagar é recusado | RN-CON-031 | Não implementado |
| CT-CON-010 | Anulação integral move para ANULADO | RN-CON-002, CA-CON-004.2 | Não implementado |
| CT-CON-011 | Anulação parcial mantém estado | RN-CON-002 | Não implementado |
| CT-CON-012 | Empenho PAGO não pode ser cancelado | RN-CON-004, CA-CON-004.6 | Não implementado |

---

# 4. Suíte CT-02 — Invariantes de Saldo

| ID | Cenário | Rastreia | Estado |
| --- | --- | --- | --- |
| CT-CON-013 | `valor_liquido` = empenhado − anulado | RN-CON-003 | Não implementado |
| CT-CON-014 | `saldo_a_liquidar` = líquido − liquidado | RN-CON-003 | Parcial |
| CT-CON-015 | `saldo_a_pagar` = liquidado − pago | RN-CON-031 | Não implementado |
| CT-CON-016 | Liquidações parciais não excedem o saldo | RN-CON-021 | Não implementado |
| CT-CON-017 | Pagamentos parciais não excedem o saldo | RN-CON-031 | Não implementado |
| CT-CON-018 | Anulação não excede o saldo a liquidar | RN-CON-002 | Não implementado |
| CT-CON-019 | Diferença de arredondamento inferior a 0,005 é aceita | RN-CON-050 | Não implementado |
| CT-CON-020 | Diferença de arredondamento igual ou superior é recusada | RN-CON-050 | Não implementado |
| CT-CON-021 | Saldos com três casas decimais são tratados corretamente | RN-CON-050 | Não implementado |
| CT-CON-022 | Sequência de anulação e liquidação mantém coerência | RN-CON-002, RN-CON-003 | Não implementado |

---

# 5. Suíte CT-03 — Integração com DOM-ORC

| ID | Cenário | Rastreia | Estado |
| --- | --- | --- | --- |
| CT-CON-023 | Empenho debita a dotação pelo valor exato | RN-CON-002, CA-CON-001.1 | Não implementado |
| CT-CON-024 | Empenho sem saldo é recusado | RN-CON-002, CA-CON-001.5 | Não implementado |
| CT-CON-025 | Anulação devolve o valor à dotação | RN-CON-002, CA-CON-004.2 | Não implementado |
| CT-CON-026 | Número duplicado no exercício é recusado | RN-CON-001, CA-CON-001.2 | Não implementado |
| CT-CON-027 | Falha na gravação do empenho reverte o débito | RNF-CON-005 | Não implementado |
| CT-CON-028 | Duas emissões simultâneas não criam duplicidade | A-02 | Não implementado |

---

# 6. Suíte CT-04 — Regras do PCASP

| ID | Cenário | Rastreia | Estado |
| --- | --- | --- | --- |
| CT-CON-029 | Criar conta com código único | RN-CON-010, CA-CON-005.1 | Implementado |
| CT-CON-030 | Criar conta com código duplicado é recusado | RN-CON-010, CA-CON-005.2 | Parcial |
| CT-CON-031 | Criar conta sem código ou nome é recusado | RN-CON-010, CA-CON-005.3 | Parcial |
| CT-CON-032 | Lançamento em conta sintética é recusado | RN-CON-011, CA-CON-005.5 | Não implementado |
| CT-CON-033 | Lançamento em conta inativa é recusado | RN-CON-012, CA-CON-005.6 | Não implementado |
| CT-CON-034 | Lançamento em conta analítica ativa é aceito | RN-CON-011 | Parcial |
| CT-CON-035 | Desativar conta impede novo lançamento | RN-CON-012 | Não implementado |
| CT-CON-036 | Reativar conta restabelece o lançamento | RN-CON-012 | Não implementado |

---

# 7. Suíte CT-05 — Partidas Dobradas

| ID | Cenário | Rastreia | Estado |
| --- | --- | --- | --- |
| CT-CON-037 | Lançamento com duas partidas balanceadas é lançado | RN-CON-050, CA-CON-006.1 | Implementado |
| CT-CON-038 | Lançamento desequilibrado é recusado | RN-CON-050, CA-CON-006.3 | Implementado |
| CT-CON-039 | Lançamento com uma única partida é recusado | RN-CON-050, CA-CON-006.2 | Parcial |
| CT-CON-040 | Conta inexistente na partida é recusada | RN-CON-051, CA-CON-006.4 | Não implementado |
| CT-CON-041 | Conta que não aceita lançamento é recusada | RN-CON-051, CA-CON-006.5 | Parcial |
| CT-CON-042 | Estorno de lançamento lançado é permitido | RF-CON-031 | Não implementado |

---

# 8. Suíte CT-06 — Conciliação

| ID | Cenário | Rastreia | Estado |
| --- | --- | --- | --- |
| CT-CON-043 | Saldos iguais geram conciliação concluída | RN-CON-060, CA-CON-007.1 | Implementado |
| CT-CON-044 | Saldos diferentes com justificativa geram divergência | RN-CON-061, CA-CON-007.2 | Não implementado |
| CT-CON-045 | Saldos diferentes sem justificativa são recusados | RN-CON-061, CA-CON-007.3 | Não implementado |
| CT-CON-046 | Diferença é arredondada a duas casas | RN-CON-060 | Não implementado |
| CT-CON-047 | Mês fora do intervalo é rejeitado | RNF-018 | Parcial |

---

# 9. Suíte CT-07 — Persistência

| ID | Cenário | Rastreia | Estado |
| --- | --- | --- | --- |
| CT-CON-048 | Empenho sobrevive ao round-trip com todos os campos | A-01 | Não implementado |
| CT-CON-049 | Liquidação sobrevive ao round-trip com data de liquidação | A-01 | Não implementado |
| CT-CON-050 | Pagamento sobrevive ao round-trip com data de efetivação | A-01 | Não implementado |
| CT-CON-051 | Lançamento sobrevive ao round-trip com data de competência | A-01 | Não implementado |
| CT-CON-052 | Conta sobrevive ao round-trip com grupo do PCASP | A-01 | Não implementado |
| CT-CON-053 | Registro excluído logicamente não é recuperado | — | Não implementado |

---

# 10. Suíte CT-08 — API

| ID | Cenário | Rastreia | Estado |
| --- | --- | --- | --- |
| CT-CON-054 | Emissão de empenho responde 201 | RF-CON-001 | Não implementado |
| CT-CON-055 | Dotação inexistente responde 404 | A-06 | Não implementado |
| CT-CON-056 | Número duplicado responde 409 | A-06 | Não implementado |
| CT-CON-057 | Saldo insuficiente responde 422 | A-06 | Não implementado |
| CT-CON-058 | Liquidação responde 200 | RF-CON-006 | Não implementado |
| CT-CON-059 | Anulação responde 200 | RF-CON-014 | Não implementado |
| CT-CON-060 | Pagamento responde 201 | RF-CON-010 | Não implementado |
| CT-CON-061 | Criação de conta responde 201 | RF-CON-017 | Não implementado |
| CT-CON-062 | Lançamento responde 201 | RF-CON-021 | Não implementado |
| CT-CON-063 | Conciliação responde 201 | RF-CON-025 | Não implementado |
| CT-CON-064 | Sete rotas constam no OpenAPI | C-01 | Não implementado |
| CT-CON-065 | Tag do domínio consta no OpenAPI | C-01 | Não implementado |
| CT-CON-066 | Payload inválido responde 422 | RNF-018 | Não implementado |
| CT-CON-067 | Acesso sem autorização é recusado | RNF-CON-007 | Não implementado |

---

# 11. Resumo de Cobertura

| Suíte | Casos | Implementados | Parciais | Cobertura |
| --- | --- | --- | --- | --- |
| CT-01 Estados | 12 | 0 | 2 | 17 % |
| CT-02 Invariantes | 10 | 0 | 1 | 10 % |
| CT-03 DOM-ORC | 6 | 0 | 0 | 0 % |
| CT-04 PCASP | 8 | 1 | 2 | 25 % |
| CT-05 Partidas | 6 | 2 | 2 | 50 % |
| CT-06 Conciliação | 5 | 1 | 1 | 40 % |
| CT-07 Persistência | 6 | 0 | 0 | 0 % |
| CT-08 API | 14 | 0 | 0 | 0 % |
| **Total** | **67** | **4** | **8** | **12 %** |

---

# 12. Prioridade de Implementação

| Prioridade | Casos | Justificativa |
| --- | --- | --- |
| 1 | CT-01 e CT-02 (22 casos) | Invariantes financeiras e transições de estado |
| 2 | CT-03 (6 casos) | Integridade com o orçamento |
| 3 | CT-08 (14 casos) | Só é possível após a exposição da API |
| 4 | CT-04 e CT-05 (14 casos) | Correção contábil |
| 5 | CT-07 (6 casos) | Só após a Onda 1 do plano |
| 6 | CT-06 (5 casos) | Conciliação |

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 019-Casos-de-Teste-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
