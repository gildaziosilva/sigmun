# 003 – Mapa de Processos – Contabilidade Pública

#### Mapa de Processos – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-003

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

Este artefato consolida os processos de negócio executados pelo domínio de
Contabilidade Pública, relacionando cada processo às suas atividades, às entradas e
saídas, aos atores responsáveis e às regras que o governam.

O ciclo da despesa segue as fases previstas na Lei 4.320/64: **empenho** (compromisso),
**liquidação** (direito adquirido) e **pagamento** (efetivação), às quais se somam os
processos de contabilidade analítica — plano de contas, lançamentos e conciliação —
e os processos de controle.

---

# 2. Princípios

* Um processo descreve uma sequência de atividades que produz um resultado de negócio.
* Processos do domínio não correspondem a endpoints: um processo pode ser disparado
  por um ou mais serviços.
* Processos nunca alteram dados de outro domínio diretamente; solicitam por integração.
* Atividades que exigem autorização são marcadas como *decisão*.

---

# 3. Processos Identificados

| Identificador | Processo | Ator principal | Entradas | Saídas | Estado |
| --- | --- | --- | --- | --- | --- |
| PRO-CON-001 | Manutenção do plano de contas | AT-CON-003 | Estrutura de contas do PCASP | Conta cadastrada, desativada ou reativada | Implementado, não exposto |
| PRO-CON-002 | Emissão de empenho | AT-CON-001 | Dotação autorizada, número, valor, favorecido | Empenho emitido e saldo da dotação debitado | Implementado, não exposto |
| PRO-CON-003 | Liquidação da despesa | AT-CON-001 | Empenho, valor, documento fiscal | Liquidação confirmada | Implementado, não exposto |
| PRO-CON-004 | Pagamento da despesa | AT-CON-005 | Liquidação confirmada, conta bancária | Pagamento efetivado | Implementado, não exposto |
| PRO-CON-005 | Anulação de empenho | AT-CON-001 | Empenho, valor, motivo | Saldo devolvido à dotação | Implementado, não exposto |
| PRO-CON-006 | Cancelamento de empenho | AT-CON-001 | Empenho, motivo | Empenho cancelado | Implementado, não exposto |
| PRO-CON-007 | Lançamento contábil | AT-CON-001 | Partidas dobradas por conta | Lançamento lançado | Implementado, não exposto |
| PRO-CON-008 | Estorno de lançamento | AT-CON-001 | Lançamento lançado | Lançamento estornado | Planejado |
| PRO-CON-009 | Conciliação bancária | AT-CON-004 | Saldo contábil e extrato da competência | Conciliação registrada ou divergência justificada | Implementado, não exposto |
| PRO-CON-010 | Consulta da execução | AT-CON-006, AT-CON-007 | Filtros de exercício, dotação, período | Execução consolidada da despesa | Planejado |
| PRO-CON-011 | Auditoria de operações | AT-CON-006 | Trilha de auditoria | Evidência de autoria e data | Planejado |

---

# 4. Detalhamento

## PRO-CON-002 — Emissão de empenho

**Fluxo principal:**

1. Identificar a dotação autorizada no DOM-ORC.
2. Verificar se o número já foi emitido no exercício (RN-CON-001).
3. Verificar saldo disponível na dotação (RN-CON-002).
4. Registrar o empenho com valor, tipo e favorecido.
5. Debitar o valor na dotação (DOM-ORC).
6. Persistir o empenho em estado EMITIDO.

**Decisão:** a emissão exige saldo na dotação; sem saldo, o processo é recusado.

**Regras:** RN-CON-001, RN-CON-002, RN-CON-004

**Serviços:** SVC-CON-001

**Estado:** Implementado, não exposto.

---

## PRO-CON-003 — Liquidação da despesa

**Fluxo principal:**

1. Localizar o empenho e validar seu estado.
2. Verificar se o valor não excede o saldo a liquidar (RN-CON-021).
3. Registrar a liquidação com documento fiscal.
4. Confirmar a liquidação e transicionar o empenho para LIQUIDADO (RN-CON-020, RN-CON-022).

**Decisão:** o valor deve ser positivo e não pode ultrapassar o saldo a liquidar.

**Regras:** RN-CON-020, RN-CON-021, RN-CON-022

**Serviços:** SVC-CON-002

---

## PRO-CON-004 — Pagamento da despesa

**Fluxo principal:**

1. Localizar a liquidação e exigir estado CONFIRMADA (RN-CON-030).
2. Verificar se o valor não excede o saldo a pagar (RN-CON-031).
3. Registrar o pagamento com conta bancária e número da ordem.
4. Efetivar o pagamento e transicionar o empenho para PAGO quando totalmente pago (RN-CON-032).

**Decisão:** somente liquidação confirmada origina pagamento.

**Regras:** RN-CON-030, RN-CON-031, RN-CON-032

**Serviços:** SVC-CON-003

---

## PRO-CON-005 — Anulação de empenho

**Fluxo principal:**

1. Localizar o empenho e validar seu estado (EMITIDO ou LIQUIDADO).
2. Verificar se o valor não excede o saldo a liquidar.
3. Somar o valor à parcela anulada.
4. Transicionar para ANULADO quando não houver valor líquido nem liquidado.
5. Devolver o valor à dotação no DOM-ORC.

**Decisão:** a anulação exige motivo e devolve saldo à dotação.

**Regras:** RN-CON-002, RN-CON-004

**Serviços:** SVC-CON-004

---

## PRO-CON-006 — Cancelamento de empenho

**Fluxo principal:**

1. Localizar o empenho.
2. Recusar se o estado for PAGO (RN-CON-004).
3. Transicionar para CANCELADO e registrar o motivo.

**Decisão:** o cancelamento encerra o empenho sem alteração de valores.

**Regras:** RN-CON-004

**Serviços:** — (não há endpoint dedicado; operação disponível no domínio)

---

## PRO-CON-007 — Lançamento contábil

**Fluxo principal:**

1. Receber ao menos duas partidas (RN-CON-040).
2. Validar cada conta: deve existir, ser analítica, estar ativa e aceitar lançamento (RN-CON-011, RN-CON-012).
3. Somar débito e crédito e exigir igualdade (RN-CON-040).
4. Persistir o lançamento com origem e totais.

**Decisão:** lançamento desequilibrado ou em conta inválida é recusado.

**Regras:** RN-CON-010, RN-CON-011, RN-CON-012, RN-CON-040

**Serviços:** SVC-CON-005

---

## PRO-CON-009 — Conciliação bancária

**Fluxo principal:**

1. Informar conta, competência e os dois saldos.
2. Calcular a diferença entre saldo contábil e saldo do extrato.
3. Se a diferença for zero, marcar como CONCILIADA.
4. Se houver diferença, exigir justificativa e marcar como DIVERGENTE (RN-CON-050).

**Regras:** RN-CON-050

**Serviços:** SVC-CON-006

---

# 5. Ciclo da Despesa

```text
PRO-CON-002                PRO-CON-003              PRO-CON-004
  Empenho        ──────►    Liquidação     ──────►   Pagamento
  (EMITIDO)                  (CONFIRMADA)            (EFETIVADO)
     │                            │                       │
     │                            ▼                       ▼
     │                       PRO-CON-007              PRO-CON-007
     │                       Lançamento              Lançamento
     │                            │                       │
     ▼                            └───────┬───────────────┘
PRO-CON-005 / 006                          ▼
  Anulação / Cancelamento            PRO-CON-009
                                           │
                                           ▼
                                    Conciliação
```

Cada etapa da despesa deve produzir o correspondente lançamento contábil
(etapa 3.4 do plano de trabalho: a geração automática ainda não existe).

---

# 6. Processos × Regras

| Regra | Processos que a aplicam |
| --- | --- |
| RN-CON-001 | PRO-CON-002, PRO-CON-010 |
| RN-CON-002 | PRO-CON-002, PRO-CON-005 |
| RN-CON-003 | PRO-CON-002, PRO-CON-003 |
| RN-CON-004 | PRO-CON-005, PRO-CON-006 |
| RN-CON-010 | PRO-CON-001 |
| RN-CON-011 | PRO-CON-001, PRO-CON-007 |
| RN-CON-012 | PRO-CON-001, PRO-CON-007 |
| RN-CON-020 | PRO-CON-003 |
| RN-CON-021 | PRO-CON-003 |
| RN-CON-022 | PRO-CON-003 |
| RN-CON-030 | PRO-CON-004 |
| RN-CON-031 | PRO-CON-004 |
| RN-CON-032 | PRO-CON-004 |
| RN-CON-040 | PRO-CON-007, PRO-CON-008 |
| RN-CON-050 | PRO-CON-009 |

---

# 7. Lacunas Identificadas

| Lacuna | Processos afetados | Achado |
| --- | --- | --- |
| Processos implementados não expostos na API | PRO-CON-001 a PRO-CON-007, PRO-CON-009 | C-01 |
| Estorno de lançamento sem serviço | PRO-CON-008 | M-03 |
| Consulta da execução inexistente | PRO-CON-010 | B-05 |
| Sem eventos de domínio | todos | M-01 |


---

Este artefato consolida os processos de negócio executados pelo domínio de
Contabilidade Pública, relacionando cada processo às suas atividades, às entradas e
saídas, aos atores responsáveis e às regras que o governam.

O ciclo da despesa segue as fases previstas na Lei 4.320/64: **empenho** (compromisso),
**liquidação** (direito adquirido) e **pagamento** (efetivação), às quais se somam os
processos de contabilidade analítica — plano de contas, lançamentos e conciliação —
e os processos de controle.

---

# 2. Princípios

* Um processo descreve uma sequência de atividades que produz um resultado de negócio.
* Processos do domínio não correspondem a endpoints: um processo pode ser disparado
  por um ou mais serviços.
* Processos nunca alteram dados de outro domínio diretamente; solicitam por integração.
* Atividades que exigem autorização são marcadas como *decisão*.

---

# 3. Processos Identificados

| Identificador | Processo | Ator principal | Entradas | Saídas | Estado |
| --- | --- | --- | --- | --- | --- |
| PRO-CON-001 | Manutenção do plano de contas | AT-CON-003 | Estrutura de contas do PCASP | Conta cadastrada, desativada ou reativada | Implementado, não exposto |
| PRO-CON-002 | Emissão de empenho | AT-CON-001 | Dotação autorizada, número, valor, favorecido | Empenho emitido e saldo da dotação debitado | Implementado, não exposto |
| PRO-CON-003 | Liquidação da despesa | AT-CON-001 | Empenho, valor, documento fiscal | Liquidação confirmada | Implementado, não exposto |
| PRO-CON-004 | Pagamento da despesa | AT-CON-005 | Liquidação confirmada, conta bancária | Pagamento efetivado | Implementado, não exposto |
| PRO-CON-005 | Anulação de empenho | AT-CON-001 | Empenho, valor, motivo | Saldo devolvido à dotação | Implementado, não exposto |
| PRO-CON-006 | Cancelamento de empenho | AT-CON-001 | Empenho, motivo | Empenho cancelado | Implementado, não exposto |
| PRO-CON-007 | Lançamento contábil | AT-CON-001 | Partidas dobradas por conta | Lançamento lançado | Implementado, não exposto |
| PRO-CON-008 | Estorno de lançamento | AT-CON-001 | Lançamento lançado | Lançamento estornado | Planejado |
| PRO-CON-009 | Conciliação bancária | AT-CON-004 | Saldo contábil e extrato da competência | Conciliação registrada ou divergência justificada | Implementado, não exposto |
| PRO-CON-010 | Consulta da execução | AT-CON-006, AT-CON-007 | Filtros de exercício, dotação, período | Execução consolidada da despesa | Planejado |
| PRO-CON-011 | Auditoria de operações | AT-CON-006 | Trilha de auditoria | Evidência de autoria e data | Planejado |

---

# 4. Detalhamento

## PRO-CON-002 — Emissão de empenho

**Fluxo principal:**

1. Identificar a dotação autorizada no DOM-ORC.
2. Verificar se o número já foi emitido no exercício (RN-CON-001).
3. Verificar saldo disponível na dotação (RN-CON-002).
4. Registrar o empenho com valor, tipo e favorecido.
5. Debitar o valor na dotação (DOM-ORC).
6. Persistir o empenho em estado EMITIDO.

**Decisão:** a emissão exige saldo na dotação; sem saldo, o processo é recusado.

**Regras:** RN-CON-001, RN-CON-002, RN-CON-004

**Serviços:** SVC-CON-001

**Estado:** Implementado, não exposto.

---

## PRO-CON-003 — Liquidação da despesa

**Fluxo principal:**

1. Localizar o empenho e validar seu estado.
2. Verificar se o valor não excede o saldo a liquidar (RN-CON-021).
3. Registrar a liquidação com documento fiscal.
4. Confirmar a liquidação e transicionar o empenho para LIQUIDADO (RN-CON-020, RN-CON-022).

**Decisão:** o valor deve ser positivo e não pode ultrapassar o saldo a liquidar.

**Regras:** RN-CON-020, RN-CON-021, RN-CON-022

**Serviços:** SVC-CON-002

---

## PRO-CON-004 — Pagamento da despesa

**Fluxo principal:**

1. Localizar a liquidação e exigir estado CONFIRMADA (RN-CON-030).
2. Verificar se o valor não excede o saldo a pagar (RN-CON-031).
3. Registrar o pagamento com conta bancária e número da ordem.
4. Efetivar o pagamento e transicionar o empenho para PAGO quando totalmente pago (RN-CON-032).

**Decisão:** somente liquidação confirmada origina pagamento.

**Regras:** RN-CON-030, RN-CON-031, RN-CON-032

**Serviços:** SVC-CON-003

---

## PRO-CON-005 — Anulação de empenho

**Fluxo principal:**

1. Localizar o empenho e validar seu estado (EMITIDO ou LIQUIDADO).
2. Verificar se o valor não excede o saldo a liquidar.
3. Somar o valor à parcela anulada.
4. Transicionar para ANULADO quando não houver valor líquido nem liquidado.
5. Devolver o valor à dotação no DOM-ORC.

**Decisão:** a anulação exige motivo e devolve saldo à dotação.

**Regras:** RN-CON-002, RN-CON-004

**Serviços:** SVC-CON-004

---

## PRO-CON-006 — Cancelamento de empenho

**Fluxo principal:**

1. Localizar o empenho.
2. Recusar se o estado for PAGO (RN-CON-004).
3. Transicionar para CANCELADO e registrar o motivo.

**Decisão:** o cancelamento encerra o empenho sem alteração de valores.

**Regras:** RN-CON-004

**Serviços:** — (não há endpoint dedicado; operação disponível no domínio)

---

## PRO-CON-007 — Lançamento contábil

**Fluxo principal:**

1. Receber ao menos duas partidas (RN-CON-040).
2. Validar cada conta: deve existir, ser analítica, estar ativa e aceitar lançamento (RN-CON-011, RN-CON-012).
3. Somar débito e crédito e exigir igualdade (RN-CON-040).
4. Persistir o lançamento com origem e totais.

**Decisão:** lançamento desequilibrado ou em conta inválida é recusado.

**Regras:** RN-CON-010, RN-CON-011, RN-CON-012, RN-CON-040

**Serviços:** SVC-CON-005

---

## PRO-CON-009 — Conciliação bancária

**Fluxo principal:**

1. Informar conta, competência e os dois saldos.
2. Calcular a diferença entre saldo contábil e saldo do extrato.
3. Se a diferença for zero, marcar como CONCILIADA.
4. Se houver diferença, exigir justificativa e marcar como DIVERGENTE (RN-CON-050).

**Regras:** RN-CON-050

**Serviços:** SVC-CON-006

---

# 5. Ciclo da Despesa

```text
PRO-CON-002                PRO-CON-003              PRO-CON-004
  Empenho        ──────►    Liquidação     ──────►   Pagamento
  (EMITIDO)                  (CONFIRMADA)            (EFETIVADO)
     │                            │                       │
     │                            ▼                       ▼
     │                       PRO-CON-007              PRO-CON-007
     │                       Lançamento              Lançamento
     │                            │                       │
     ▼                            └───────┬───────────────┘
PRO-CON-005 / 006                          ▼
  Anulação / Cancelamento            PRO-CON-009
                                           │
                                           ▼
                                    Conciliação
```

Cada etapa da despesa deve produzir o correspondente lançamento contábil
(etapa 3.4 do plano de trabalho: a geração automática ainda não existe).

---

# 6. Processos × Regras

| Regra | Processos que a aplicam |
| --- | --- |
| RN-CON-001 | PRO-CON-002, PRO-CON-010 |
| RN-CON-002 | PRO-CON-002, PRO-CON-005 |
| RN-CON-003 | PRO-CON-002, PRO-CON-003 |
| RN-CON-004 | PRO-CON-005, PRO-CON-006 |
| RN-CON-010 | PRO-CON-001 |
| RN-CON-011 | PRO-CON-001, PRO-CON-007 |
| RN-CON-012 | PRO-CON-001, PRO-CON-007 |
| RN-CON-020 | PRO-CON-003 |
| RN-CON-021 | PRO-CON-003 |
| RN-CON-022 | PRO-CON-003 |
| RN-CON-030 | PRO-CON-004 |
| RN-CON-031 | PRO-CON-004 |
| RN-CON-032 | PRO-CON-004 |
| RN-CON-040 | PRO-CON-007, PRO-CON-008 |
| RN-CON-050 | PRO-CON-009 |

---

# 7. Lacunas Identificadas

| Lacuna | Processos afetados | Achado |
| --- | --- | --- |
| Processos implementados não expostos na API | PRO-CON-001 a PRO-CON-007, PRO-CON-009 | C-01 |
| Estorno de lançamento sem serviço | PRO-CON-008 | M-03 |
| Consulta da execução inexistente | PRO-CON-010 | B-05 |
| Sem eventos de domínio | todos | M-01 |

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 003-Mapa-de-Processos-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
