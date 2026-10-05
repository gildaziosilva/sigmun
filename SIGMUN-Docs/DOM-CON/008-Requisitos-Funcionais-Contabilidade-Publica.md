# 008 – Requisitos Funcionais – Contabilidade Pública

#### Requisitos Funcionais – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-008

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

Este artefato especifica os requisitos funcionais do domínio de Contabilidade
Pública, cada um vinculado a uma capacidade, a uma regra de negócio e a um caso de uso
que o materializa.

---

# 2. Convenções

* Identificador `RF-CON-<grupo><sequencial>`, alinhado aos grupos de regra.
* Requisito descreve **o que o sistema deve fazer**, de forma verificável.
* A coluna **Estado** reflete a auditoria: implementados, mas não expostos na API.

---

# 3. Requisitos Identificados

| Identificador | Requisito | Capacidade | Regras | Caso de uso | Estado |
| --- | --- | --- | --- | --- | --- |
| RF-CON-001 | O sistema deve emitir empenho sobre dotação autorizada | CAP-CON-002 | RN-CON-001, RN-CON-002 | CU-CON-001 | Implementado, não exposto |
| RF-CON-002 | O sistema deve garantir unicidade do número no exercício | CAP-CON-002 | RN-CON-001 | CU-CON-001 | Parcial |
| RF-CON-003 | O sistema deve recusar empenho sem saldo na dotação | CAP-CON-002 | RN-CON-002 | CU-CON-001 | Implementado, não exposto |
| RF-CON-004 | O sistema deve debitar o valor na dotação ao emitir | CAP-CON-002 | RN-CON-002 | CU-CON-001 | Implementado, não exposto |
| RF-CON-005 | O sistema deve devolver saldo à dotação ao anular | CAP-CON-002 | RN-CON-002 | CU-CON-004 | Implementado, não exposto |
| RF-CON-006 | O sistema deve registrar liquidação com documento fiscal | CAP-CON-003 | RN-CON-020 | CU-CON-002 | Implementado, não exposto |
| RF-CON-007 | O sistema deve validar o saldo a liquidar | CAP-CON-003 | RN-CON-021 | CU-CON-002 | Implementado, não exposto |
| RF-CON-008 | O sistema deve confirmar a liquidação | CAP-CON-003 | RN-CON-022 | CU-CON-002 | Implementado, não exposto |
| RF-CON-009 | O sistema deve permitir cancelar a liquidação registrada | CAP-CON-003 | RN-CON-022 | — | Implementado no domínio |
| RF-CON-010 | O sistema deve exigir liquidação confirmada para pagamento | CAP-CON-004 | RN-CON-030 | CU-CON-003 | Implementado, não exposto |
| RF-CON-011 | O sistema deve validar o saldo a pagar | CAP-CON-004 | RN-CON-031 | CU-CON-003 | Implementado, não exposto |
| RF-CON-012 | O sistema deve registrar conta bancária e número da ordem | CAP-CON-004 | RN-CON-032 | CU-CON-003 | Implementado, não exposto |
| RF-CON-013 | O sistema deve efetivar o pagamento programado | CAP-CON-004 | RN-CON-032 | CU-CON-003 | Implementado, não exposto |
| RF-CON-014 | O sistema deve anular empenho parcial ou total | CAP-CON-002 | RN-CON-002 | CU-CON-004 | Implementado, não exposto |
| RF-CON-015 | O sistema deve exigir motivo na anulação | CAP-CON-002 | RN-CON-002 | CU-CON-004 | Parcial |
| RF-CON-016 | O sistema deve cancelar empenho não pago | CAP-CON-002 | RN-CON-004 | CU-CON-005 | Implementado no domínio |
| RF-CON-017 | O sistema deve criar conta do plano de contas | CAP-CON-001 | RN-CON-010 | CU-CON-006 | Implementado, não exposto |
| RF-CON-018 | O sistema deve garantir unicidade do código da conta | CAP-CON-001 | RN-CON-010 | CU-CON-006 | Implementado, não exposto |
| RF-CON-019 | O sistema deve permitir desativar e reativar conta | CAP-CON-001 | RN-CON-012 | — | Implementado no domínio |
| RF-CON-020 | O sistema deve recusar lançamento em conta não analítica ou inativa | CAP-CON-005 | RN-CON-011, RN-CON-012 | CU-CON-007 | Implementado, não exposto |
| RF-CON-021 | O sistema deve registrar partidas dobradas | CAP-CON-005 | RN-CON-050 | CU-CON-007 | Implementado, não exposto |
| RF-CON-022 | O sistema deve exigir pelo menos duas partidas | CAP-CON-005 | RN-CON-050 | CU-CON-007 | Implementado, não exposto |
| RF-CON-023 | O sistema deve recusar lançamento desequilibrado | CAP-CON-005 | RN-CON-050 | CU-CON-007 | Implementado, não exposto |
| RF-CON-024 | O sistema deve registrar a origem do lançamento | CAP-CON-005 | RN-CON-052 | CU-CON-007 | Parcial |
| RF-CON-025 | O sistema deve registrar conciliação por competência | CAP-CON-006 | RN-CON-060 | CU-CON-008 | Implementado, não exposto |
| RF-CON-026 | O sistema deve calcular a diferença entre os saldos | CAP-CON-006 | RN-CON-060 | CU-CON-008 | Implementado, não exposto |
| RF-CON-027 | O sistema deve exigir justificativa em divergência | CAP-CON-006 | RN-CON-061 | CU-CON-008 | Implementado, não exposto |
| RF-CON-028 | O sistema deve permitir consultar a execução da despesa | CAP-CON-007 | RN-CON-070 | — | Planejado |
| RF-CON-029 | O sistema deve permitir filtrar por exercício e dotação | CAP-CON-007 | RN-CON-070 | — | Planejado |
| RF-CON-030 | O sistema deve registrar autoria e data de cada operação | CAP-CON-008 | RN-CON-070 | — | Parcial |
| RF-CON-031 | O sistema deve permitir estornar lançamento lançado | CAP-CON-005 | RN-CON-052 | — | Planejado |

---

# 4. Requisitos por Capacidade

| Capacidade | Requisitos |
| --- | --- |
| CAP-CON-001 | RF-CON-017 a RF-CON-019 |
| CAP-CON-002 | RF-CON-001 a RF-CON-005, RF-CON-014 a RF-CON-016 |
| CAP-CON-003 | RF-CON-006 a RF-CON-009 |
| CAP-CON-004 | RF-CON-010 a RF-CON-013 |
| CAP-CON-005 | RF-CON-020 a RF-CON-024, RF-CON-031 |
| CAP-CON-006 | RF-CON-025 a RF-CON-027 |
| CAP-CON-007 | RF-CON-028, RF-CON-029 |
| CAP-CON-008 | RF-CON-030 |

---

# 5. Requisitos por Estado

| Estado | Quantidade | Requisitos |
| --- | --- | --- |
| Implementado, não exposto | 18 | RF-CON-001, 003 a 008, 010 a 014, 016 a 018, 020 a 023, 025 a 027 |
| Implementado no domínio, sem serviço | 3 | RF-CON-009, RF-CON-015, RF-CON-019 |
| Parcial | 4 | RF-CON-002, RF-CON-015, RF-CON-024, RF-CON-030 |
| Planejado | 4 | RF-CON-028, RF-CON-029, RF-CON-031 |

**Nenhum requisito pode ser declarado concluído enquanto C-01 não for resolvido**,
pois a totalidade dos requisitos implementados está inacessível ao consumidor.

---

# 6. Requisitos × Regras

| Regra | Requisitos que a exigem |
| --- | --- |
| RN-CON-001 | RF-CON-001, RF-CON-002 |
| RN-CON-002 | RF-CON-001, RF-CON-003, RF-CON-004, RF-CON-005, RF-CON-014 |
| RN-CON-004 | RF-CON-016 |
| RN-CON-010 | RF-CON-017, RF-CON-018 |
| RN-CON-011 | RF-CON-020 |
| RN-CON-012 | RF-CON-019, RF-CON-020 |
| RN-CON-020 | RF-CON-006 |
| RN-CON-021 | RF-CON-007 |
| RN-CON-022 | RF-CON-008, RF-CON-009 |
| RN-CON-030 | RF-CON-010 |
| RN-CON-031 | RF-CON-011 |
| RN-CON-032 | RF-CON-012, RF-CON-013 |
| RN-CON-050 | RF-CON-021, RF-CON-022, RF-CON-023 |
| RN-CON-052 | RF-CON-024, RF-CON-031 |
| RN-CON-060 | RF-CON-025, RF-CON-026 |
| RN-CON-061 | RF-CON-027 |
| RN-CON-070 | RF-CON-028, RF-CON-029, RF-CON-030 |


---

Este artefato especifica os requisitos funcionais do domínio de Contabilidade
Pública, cada um vinculado a uma capacidade, a uma regra de negócio e a um caso de uso
que o materializa.

---

# 2. Convenções

* Identificador `RF-CON-<grupo><sequencial>`, alinhado aos grupos de regra.
* Requisito descreve **o que o sistema deve fazer**, de forma verificável.
* A coluna **Estado** reflete a auditoria: implementados, mas não expostos na API.

---

# 3. Requisitos Identificados

| Identificador | Requisito | Capacidade | Regras | Caso de uso | Estado |
| --- | --- | --- | --- | --- | --- |
| RF-CON-001 | O sistema deve emitir empenho sobre dotação autorizada | CAP-CON-002 | RN-CON-001, RN-CON-002 | CU-CON-001 | Implementado, não exposto |
| RF-CON-002 | O sistema deve garantir unicidade do número no exercício | CAP-CON-002 | RN-CON-001 | CU-CON-001 | Parcial |
| RF-CON-003 | O sistema deve recusar empenho sem saldo na dotação | CAP-CON-002 | RN-CON-002 | CU-CON-001 | Implementado, não exposto |
| RF-CON-004 | O sistema deve debitar o valor na dotação ao emitir | CAP-CON-002 | RN-CON-002 | CU-CON-001 | Implementado, não exposto |
| RF-CON-005 | O sistema deve devolver saldo à dotação ao anular | CAP-CON-002 | RN-CON-002 | CU-CON-004 | Implementado, não exposto |
| RF-CON-006 | O sistema deve registrar liquidação com documento fiscal | CAP-CON-003 | RN-CON-020 | CU-CON-002 | Implementado, não exposto |
| RF-CON-007 | O sistema deve validar o saldo a liquidar | CAP-CON-003 | RN-CON-021 | CU-CON-002 | Implementado, não exposto |
| RF-CON-008 | O sistema deve confirmar a liquidação | CAP-CON-003 | RN-CON-022 | CU-CON-002 | Implementado, não exposto |
| RF-CON-009 | O sistema deve permitir cancelar a liquidação registrada | CAP-CON-003 | RN-CON-022 | — | Implementado no domínio |
| RF-CON-010 | O sistema deve exigir liquidação confirmada para pagamento | CAP-CON-004 | RN-CON-030 | CU-CON-003 | Implementado, não exposto |
| RF-CON-011 | O sistema deve validar o saldo a pagar | CAP-CON-004 | RN-CON-031 | CU-CON-003 | Implementado, não exposto |
| RF-CON-012 | O sistema deve registrar conta bancária e número da ordem | CAP-CON-004 | RN-CON-032 | CU-CON-003 | Implementado, não exposto |
| RF-CON-013 | O sistema deve efetivar o pagamento programado | CAP-CON-004 | RN-CON-032 | CU-CON-003 | Implementado, não exposto |
| RF-CON-014 | O sistema deve anular empenho parcial ou total | CAP-CON-002 | RN-CON-002 | CU-CON-004 | Implementado, não exposto |
| RF-CON-015 | O sistema deve exigir motivo na anulação | CAP-CON-002 | RN-CON-002 | CU-CON-004 | Parcial |
| RF-CON-016 | O sistema deve cancelar empenho não pago | CAP-CON-002 | RN-CON-004 | CU-CON-005 | Implementado no domínio |
| RF-CON-017 | O sistema deve criar conta do plano de contas | CAP-CON-001 | RN-CON-010 | CU-CON-006 | Implementado, não exposto |
| RF-CON-018 | O sistema deve garantir unicidade do código da conta | CAP-CON-001 | RN-CON-010 | CU-CON-006 | Implementado, não exposto |
| RF-CON-019 | O sistema deve permitir desativar e reativar conta | CAP-CON-001 | RN-CON-012 | — | Implementado no domínio |
| RF-CON-020 | O sistema deve recusar lançamento em conta não analítica ou inativa | CAP-CON-005 | RN-CON-011, RN-CON-012 | CU-CON-007 | Implementado, não exposto |
| RF-CON-021 | O sistema deve registrar partidas dobradas | CAP-CON-005 | RN-CON-050 | CU-CON-007 | Implementado, não exposto |
| RF-CON-022 | O sistema deve exigir pelo menos duas partidas | CAP-CON-005 | RN-CON-050 | CU-CON-007 | Implementado, não exposto |
| RF-CON-023 | O sistema deve recusar lançamento desequilibrado | CAP-CON-005 | RN-CON-050 | CU-CON-007 | Implementado, não exposto |
| RF-CON-024 | O sistema deve registrar a origem do lançamento | CAP-CON-005 | RN-CON-052 | CU-CON-007 | Parcial |
| RF-CON-025 | O sistema deve registrar conciliação por competência | CAP-CON-006 | RN-CON-060 | CU-CON-008 | Implementado, não exposto |
| RF-CON-026 | O sistema deve calcular a diferença entre os saldos | CAP-CON-006 | RN-CON-060 | CU-CON-008 | Implementado, não exposto |
| RF-CON-027 | O sistema deve exigir justificativa em divergência | CAP-CON-006 | RN-CON-061 | CU-CON-008 | Implementado, não exposto |
| RF-CON-028 | O sistema deve permitir consultar a execução da despesa | CAP-CON-007 | RN-CON-070 | — | Planejado |
| RF-CON-029 | O sistema deve permitir filtrar por exercício e dotação | CAP-CON-007 | RN-CON-070 | — | Planejado |
| RF-CON-030 | O sistema deve registrar autoria e data de cada operação | CAP-CON-008 | RN-CON-070 | — | Parcial |
| RF-CON-031 | O sistema deve permitir estornar lançamento lançado | CAP-CON-005 | RN-CON-052 | — | Planejado |

---

# 4. Requisitos por Capacidade

| Capacidade | Requisitos |
| --- | --- |
| CAP-CON-001 | RF-CON-017 a RF-CON-019 |
| CAP-CON-002 | RF-CON-001 a RF-CON-005, RF-CON-014 a RF-CON-016 |
| CAP-CON-003 | RF-CON-006 a RF-CON-009 |
| CAP-CON-004 | RF-CON-010 a RF-CON-013 |
| CAP-CON-005 | RF-CON-020 a RF-CON-024, RF-CON-031 |
| CAP-CON-006 | RF-CON-025 a RF-CON-027 |
| CAP-CON-007 | RF-CON-028, RF-CON-029 |
| CAP-CON-008 | RF-CON-030 |

---

# 5. Requisitos por Estado

| Estado | Quantidade | Requisitos |
| --- | --- | --- |
| Implementado, não exposto | 18 | RF-CON-001, 003 a 008, 010 a 014, 016 a 018, 020 a 023, 025 a 027 |
| Implementado no domínio, sem serviço | 3 | RF-CON-009, RF-CON-015, RF-CON-019 |
| Parcial | 4 | RF-CON-002, RF-CON-015, RF-CON-024, RF-CON-030 |
| Planejado | 4 | RF-CON-028, RF-CON-029, RF-CON-031 |

**Nenhum requisito pode ser declarado concluído enquanto C-01 não for resolvido**,
pois a totalidade dos requisitos implementados está inacessível ao consumidor.

---

# 6. Requisitos × Regras

| Regra | Requisitos que a exigem |
| --- | --- |
| RN-CON-001 | RF-CON-001, RF-CON-002 |
| RN-CON-002 | RF-CON-001, RF-CON-003, RF-CON-004, RF-CON-005, RF-CON-014 |
| RN-CON-004 | RF-CON-016 |
| RN-CON-010 | RF-CON-017, RF-CON-018 |
| RN-CON-011 | RF-CON-020 |
| RN-CON-012 | RF-CON-019, RF-CON-020 |
| RN-CON-020 | RF-CON-006 |
| RN-CON-021 | RF-CON-007 |
| RN-CON-022 | RF-CON-008, RF-CON-009 |
| RN-CON-030 | RF-CON-010 |
| RN-CON-031 | RF-CON-011 |
| RN-CON-032 | RF-CON-012, RF-CON-013 |
| RN-CON-050 | RF-CON-021, RF-CON-022, RF-CON-023 |
| RN-CON-052 | RF-CON-024, RF-CON-031 |
| RN-CON-060 | RF-CON-025, RF-CON-026 |
| RN-CON-061 | RF-CON-027 |
| RN-CON-070 | RF-CON-028, RF-CON-029, RF-CON-030 |

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 008-Requisitos-Funcionais-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
