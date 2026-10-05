# 006 – Histórias de Usuário – Contabilidade Pública

#### Histórias de Usuário – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-006

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

Este artefato especifica as histórias de usuário do domínio de Contabilidade
Pública, cada uma vinculada a uma capacidade, aos casos de uso que a implementam e
aos requisitos funcionais que a materializam.

As histórias seguem o formato *Como / quero / para que*, com critérios de aceitação
resumidos. Os critérios completos estão no artefato `011-Criterios-de-Aceitacao`.

---

# 2. Convenções

* Cada história é atomicamente verificável e tem valor de negócio para o município.
* A prioridade usa MoSCoW: **Must** (obrigatório), **Should**, **Could**, **Won't**.
* A estimativa é em pontos de história.

---

# 3. Histórias Identificadas

| Identificador | História | Ator | Capacidade | Prioridade | Pontos |
| --- | --- | --- | --- | --- | --- |
| HU-CON-001 | Emitir empenho sobre dotação autorizada | Contador | CAP-CON-002 | Must | 5 |
| HU-CON-002 | Liquidar despesa comprovar o direito adquirido | Contador | CAP-CON-003 | Must | 5 |
| HU-CON-003 | Pagar liquidação confirmada | Tesoureiro | CAP-CON-004 | Must | 5 |
| HU-CON-004 | Anular e cancelar empenho | Contador / Ordenador | CAP-CON-002 | Must | 3 |
| HU-CON-005 | Manter o plano de contas | Gestor do PCASP | CAP-CON-001 | Must | 3 |
| HU-CON-006 | Lançar partidas dobradas | Contador | CAP-CON-005 | Must | 5 |
| HU-CON-007 | Conciliar conta bancária | Contador da conciliação | CAP-CON-006 | Should | 5 |
| HU-CON-008 | Auditar a execução da despesa | Controle interno | CAP-CON-007, CAP-CON-008 | Should | 8 |

---

# 4. Detalhamento

## HU-CON-001 — Emitir empenho sobre dotação autorizada

**Como** contador responsável pela execução orçamentária,
**quero** emitir empenho sobre dotação autorizada,
**para que** o compromisso de despesa fique registrado e o saldo da dotação seja
debitado.

**Capacidade:** CAP-CON-002 · **Processos:** PRO-CON-002 · **Casos de uso:** CU-CON-001

**Critérios de aceitação resumidos:**

* O número do empenho deve ser único dentro do exercício.
* O valor deve ser maior que zero.
* A dotação deve existir e ter saldo disponível.
* Após a emissão, o empenho fica em estado EMITIDO.
* O saldo da dotação é debitado pelo valor do empenho.

**Requisitos:** RF-CON-001 a RF-CON-005

**Regras:** RN-CON-001, RN-CON-002

---

## HU-CON-002 — Liquidar despesa

**Como** contador responsável pela execução orçamentária,
**quero** registrar a liquidação com o documento fiscal,
**para que** o direito adquirido sobre o empenho fique comprovado.

**Capacidade:** CAP-CON-003 · **Processo:** PRO-CON-003 · **Caso de uso:** CU-CON-002

**Critérios de aceitação resumidos:**

* O valor da liquidação não pode exceder o saldo a liquidar.
* O valor deve ser maior que zero.
* A liquidação exige documento fiscal.
* Após a confirmação, o empenho passa a LIQUIDADO.

**Requisitos:** RF-CON-006 a RF-CON-009

**Regras:** RN-CON-020, RN-CON-021, RN-CON-022

---

## HU-CON-003 — Pagar liquidação

**Como** tesoureiro,
**quero** registrar o pagamento de uma liquidação confirmada,
**para que** a saída de recursos seja registrada e a despesa seja efetivada.

**Capacidade:** CAP-CON-004 · **Processo:** PRO-CON-004 · **Caso de uso:** CU-CON-003

**Critérios de aceitação resumidos:**

* Somente liquidação confirmada pode ser paga.
* O valor não pode exceder o saldo a pagar.
* O pagamento registra conta bancária.
* Quando o empenho é totalmente pago, passa a PAGO.

**Requisitos:** RF-CON-010 a RF-CON-013

**Regras:** RN-CON-030, RN-CON-031, RN-CON-032

---

## HU-CON-004 — Anular e cancelar empenho

**Como** contador ou ordenador da despesa,
**quero** anular ou cancelar um empenho,
**para que** o orçamento refita a realidae da obrigação e, no cancelamento, devolve
sua decisão administrativa.

**Capacidade:** CAP-CON-002 · **Processos:** PRO-CON-005, PRO-CON-006
**Casos de uso:** CU-CON-004, CU-CON-005

**Critérios de aceitação resumidos:**

* A anulação devolve saldo à dotação e exige motivo.
* A anulação não pode ocorrer quando não há saldo a liquidar.
* Empenho pago não pode ser cancelado.
* Estados terminais são PAGO, ANULADO e CANCELADO.

**Requisitos:** RF-CON-014 a RF-CON-016

**Regras:** RN-CON-002, RN-CON-004

---

## HU-CON-005 — Manter o plano de contas

**Como** gestor do plano de contas,
**quero** cadastrar e desativar contas do PCASP,
**para que** os lançamentos contábeis usem uma estrutura padronizada.

**Capacidade:** CAP-CON-001 · **Processo:** PRO-CON-001 · **Caso de uso:** CU-CON-006

**Critérios de aceitação resumidos:**

* O código da conta é único no plano.
* Conta sintética não recebe lançamento.
* Conta inativa não recebe lançamento.
* Somente conta analítica aceita lançamento.

**Requisitos:** RF-CON-017 a RF-CON-020

**Regras:** RN-CON-010, RN-CON-011, RN-CON-012

---

## HU-CON-006 — Lançar partidas dobradas

**Como** contador,
**quero** registrar um lançamento por partidas dobradas,
**para que** o fato contábil seja refletido com o total de débito igual ao de crédito.

**Capacidade:** CAP-CON-005 · **Processo:** PRO-CON-007 · **Caso de uso:** CU-CON-007

**Critérios de aceitação resumidos:**

* O lançamento exige ao menos duas partidas.
* Cada conta deve existir, ser analítica e estar ativa.
* O total de débito deve igualar o total de crédito.
* O lançamento registra origem e identificador de origem.

**Requisitos:** RF-CON-021 a RF-CON-024

**Regras:** RN-CON-011, RN-CON-012, RN-CON-040

---

## HU-CON-007 — Conciliar conta bancária

**Como** contador responsável pela conciliação,
**quero** comparar o saldo contábil com o extrato bancário,
**para que** divergências sejam identificadas e justificadas.

**Capacidade:** CAP-CON-006 · **Processo:** PRO-CON-009 · **Caso de uso:** CU-CON-008

**Critérios de aceitação resumidos:**

* A conciliação é registrada por conta e competência (ano e mês).
* Diferença zero resulta em conciliação concluída.
* Diferença diferente de zero exige justificativa e gera divergência.

**Requisitos:** RF-CON-025 a RF-CON-027

**Regras:** RN-CON-050

---

## HU-CON-008 — Auditar a execução da despesa

**Como** responsável pelo controle interno,
**quero** consultar a execução e a trilha de auditoria,
**para que** possa fiscalizar a legalidade dos registros.

**Capacidade:** CAP-CON-007, CAP-CON-008 · **Processo:** PRO-CON-010, PRO-CON-011

**Critérios de aceitação resumidos:**

* Deve ser possível filtrar a execução por exercício, dotação e período.
* Cada operação deve registrar autor, data e valores antes e depois.
* O acesso de consulta não pode permitir alteração.

**Requisitos:** RF-CON-028 a RF-CON-031

**Regras:** RN-CON-060

**Estado:** **Planejada** — não existem endpoints de leitura nem trilha de auditoria
completa no módulo (achados B-05 e M-04).

---

# 5. Backlog de Implementação

| História | Estado | Bloqueio |
| --- | --- | --- |
| HU-CON-001 a HU-CON-007 | Implementada, não exposta | C-01 |
| HU-CON-008 | Planejada | B-05, M-04 |

**Observação:** as sete histórias implementadas permanecem inacessíveis até que os
routers do domínio sejam registrados na aplicação. Nenhuma história pode ser declarada
concluída antes disso.


---

Este artefato especifica as histórias de usuário do domínio de Contabilidade
Pública, cada uma vinculada a uma capacidade, aos casos de uso que a implementam e
aos requisitos funcionais que a materializam.

As histórias seguem o formato *Como / quero / para que*, com critérios de aceitação
resumidos. Os critérios completos estão no artefato `011-Criterios-de-Aceitacao`.

---

# 2. Convenções

* Cada história é atomicamente verificável e tem valor de negócio para o município.
* A prioridade usa MoSCoW: **Must** (obrigatório), **Should**, **Could**, **Won't**.
* A estimativa é em pontos de história.

---

# 3. Histórias Identificadas

| Identificador | História | Ator | Capacidade | Prioridade | Pontos |
| --- | --- | --- | --- | --- | --- |
| HU-CON-001 | Emitir empenho sobre dotação autorizada | Contador | CAP-CON-002 | Must | 5 |
| HU-CON-002 | Liquidar despesa comprovar o direito adquirido | Contador | CAP-CON-003 | Must | 5 |
| HU-CON-003 | Pagar liquidação confirmada | Tesoureiro | CAP-CON-004 | Must | 5 |
| HU-CON-004 | Anular e cancelar empenho | Contador / Ordenador | CAP-CON-002 | Must | 3 |
| HU-CON-005 | Manter o plano de contas | Gestor do PCASP | CAP-CON-001 | Must | 3 |
| HU-CON-006 | Lançar partidas dobradas | Contador | CAP-CON-005 | Must | 5 |
| HU-CON-007 | Conciliar conta bancária | Contador da conciliação | CAP-CON-006 | Should | 5 |
| HU-CON-008 | Auditar a execução da despesa | Controle interno | CAP-CON-007, CAP-CON-008 | Should | 8 |

---

# 4. Detalhamento

## HU-CON-001 — Emitir empenho sobre dotação autorizada

**Como** contador responsável pela execução orçamentária,
**quero** emitir empenho sobre dotação autorizada,
**para que** o compromisso de despesa fique registrado e o saldo da dotação seja
debitado.

**Capacidade:** CAP-CON-002 · **Processos:** PRO-CON-002 · **Casos de uso:** CU-CON-001

**Critérios de aceitação resumidos:**

* O número do empenho deve ser único dentro do exercício.
* O valor deve ser maior que zero.
* A dotação deve existir e ter saldo disponível.
* Após a emissão, o empenho fica em estado EMITIDO.
* O saldo da dotação é debitado pelo valor do empenho.

**Requisitos:** RF-CON-001 a RF-CON-005

**Regras:** RN-CON-001, RN-CON-002

---

## HU-CON-002 — Liquidar despesa

**Como** contador responsável pela execução orçamentária,
**quero** registrar a liquidação com o documento fiscal,
**para que** o direito adquirido sobre o empenho fique comprovado.

**Capacidade:** CAP-CON-003 · **Processo:** PRO-CON-003 · **Caso de uso:** CU-CON-002

**Critérios de aceitação resumidos:**

* O valor da liquidação não pode exceder o saldo a liquidar.
* O valor deve ser maior que zero.
* A liquidação exige documento fiscal.
* Após a confirmação, o empenho passa a LIQUIDADO.

**Requisitos:** RF-CON-006 a RF-CON-009

**Regras:** RN-CON-020, RN-CON-021, RN-CON-022

---

## HU-CON-003 — Pagar liquidação

**Como** tesoureiro,
**quero** registrar o pagamento de uma liquidação confirmada,
**para que** a saída de recursos seja registrada e a despesa seja efetivada.

**Capacidade:** CAP-CON-004 · **Processo:** PRO-CON-004 · **Caso de uso:** CU-CON-003

**Critérios de aceitação resumidos:**

* Somente liquidação confirmada pode ser paga.
* O valor não pode exceder o saldo a pagar.
* O pagamento registra conta bancária.
* Quando o empenho é totalmente pago, passa a PAGO.

**Requisitos:** RF-CON-010 a RF-CON-013

**Regras:** RN-CON-030, RN-CON-031, RN-CON-032

---

## HU-CON-004 — Anular e cancelar empenho

**Como** contador ou ordenador da despesa,
**quero** anular ou cancelar um empenho,
**para que** o orçamento refita a realidae da obrigação e, no cancelamento, devolve
sua decisão administrativa.

**Capacidade:** CAP-CON-002 · **Processos:** PRO-CON-005, PRO-CON-006
**Casos de uso:** CU-CON-004, CU-CON-005

**Critérios de aceitação resumidos:**

* A anulação devolve saldo à dotação e exige motivo.
* A anulação não pode ocorrer quando não há saldo a liquidar.
* Empenho pago não pode ser cancelado.
* Estados terminais são PAGO, ANULADO e CANCELADO.

**Requisitos:** RF-CON-014 a RF-CON-016

**Regras:** RN-CON-002, RN-CON-004

---

## HU-CON-005 — Manter o plano de contas

**Como** gestor do plano de contas,
**quero** cadastrar e desativar contas do PCASP,
**para que** os lançamentos contábeis usem uma estrutura padronizada.

**Capacidade:** CAP-CON-001 · **Processo:** PRO-CON-001 · **Caso de uso:** CU-CON-006

**Critérios de aceitação resumidos:**

* O código da conta é único no plano.
* Conta sintética não recebe lançamento.
* Conta inativa não recebe lançamento.
* Somente conta analítica aceita lançamento.

**Requisitos:** RF-CON-017 a RF-CON-020

**Regras:** RN-CON-010, RN-CON-011, RN-CON-012

---

## HU-CON-006 — Lançar partidas dobradas

**Como** contador,
**quero** registrar um lançamento por partidas dobradas,
**para que** o fato contábil seja refletido com o total de débito igual ao de crédito.

**Capacidade:** CAP-CON-005 · **Processo:** PRO-CON-007 · **Caso de uso:** CU-CON-007

**Critérios de aceitação resumidos:**

* O lançamento exige ao menos duas partidas.
* Cada conta deve existir, ser analítica e estar ativa.
* O total de débito deve igualar o total de crédito.
* O lançamento registra origem e identificador de origem.

**Requisitos:** RF-CON-021 a RF-CON-024

**Regras:** RN-CON-011, RN-CON-012, RN-CON-040

---

## HU-CON-007 — Conciliar conta bancária

**Como** contador responsável pela conciliação,
**quero** comparar o saldo contábil com o extrato bancário,
**para que** divergências sejam identificadas e justificadas.

**Capacidade:** CAP-CON-006 · **Processo:** PRO-CON-009 · **Caso de uso:** CU-CON-008

**Critérios de aceitação resumidos:**

* A conciliação é registrada por conta e competência (ano e mês).
* Diferença zero resulta em conciliação concluída.
* Diferença diferente de zero exige justificativa e gera divergência.

**Requisitos:** RF-CON-025 a RF-CON-027

**Regras:** RN-CON-050

---

## HU-CON-008 — Auditar a execução da despesa

**Como** responsável pelo controle interno,
**quero** consultar a execução e a trilha de auditoria,
**para que** possa fiscalizar a legalidade dos registros.

**Capacidade:** CAP-CON-007, CAP-CON-008 · **Processo:** PRO-CON-010, PRO-CON-011

**Critérios de aceitação resumidos:**

* Deve ser possível filtrar a execução por exercício, dotação e período.
* Cada operação deve registrar autor, data e valores antes e depois.
* O acesso de consulta não pode permitir alteração.

**Requisitos:** RF-CON-028 a RF-CON-031

**Regras:** RN-CON-060

**Estado:** **Planejada** — não existem endpoints de leitura nem trilha de auditoria
completa no módulo (achados B-05 e M-04).

---

# 5. Backlog de Implementação

| História | Estado | Bloqueio |
| --- | --- | --- |
| HU-CON-001 a HU-CON-007 | Implementada, não exposta | C-01 |
| HU-CON-008 | Planejada | B-05, M-04 |

**Observação:** as sete histórias implementadas permanecem inacessíveis até que os
routers do domínio sejam registrados na aplicação. Nenhuma história pode ser declarada
concluída antes disso.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 006-Historias-de-Usuario-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
