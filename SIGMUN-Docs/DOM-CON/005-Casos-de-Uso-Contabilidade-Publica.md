# 005 – Casos de Uso – Contabilidade Pública

#### Casos de Uso – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-005

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

Este artefato especifica os casos de uso do domínio de Contabilidade Pública,
relacionando cada cenário à sua implementação na camada de casos de uso
(`src/modules/sigmun_con/application/`).

Cada caso de uso corresponde a uma classe concreta e a um serviço publicado. Cenários
de leitura direta ao repositório são identificados como tales, pois não exigem lógica
de negócio própria.

---

# 2. Convenções

* Casos de uso descrevem **cenários de negócio**; a implementação é referenciada
  pelo nome da classe correspondente.
* Regras aplicadas usam o padrão `RN-CON-<grupo><sequencial>`.
* A coluna **Estado** reflete a auditoria: implementados, mas **não expostos na API**.

---

# 3. Casos de Uso

## CU-CON-001 — Emitir empenho

**Ator:** AT-CON-001
**Capacidade:** CAP-CON-002
**Processo:** PRO-CON-002
**Implementador:** `EmitirEmpenhoUseCase`
**Serviço:** SVC-CON-001

**Pré-condições:** O servidor está autenticado e autorizado; existe dotação autorizada
com saldo disponível no DOM-ORC.

**Fluxo principal:**

1. Validar que o número do empenho foi informado (RN-CON-001).
2. Validar que o valor é maior que zero.
3. Verificar que não existe empenho com o mesmo número no exercício (RN-CON-001).
4. Debitar o valor na dotação recebida (RN-CON-002).
5. Criar a entidade `Empenho` com tipo, descrição e favorecido.
6. Persistir o empenho e devolver a entidade.

**Pós-condições:** empenho persistido em estado EMITIDO; saldo da dotação debitado.

**Fluxos alternativos e exceções:**

| Condição | Resultado |
| --- | --- |
| Número não informado | `RegraNegocioError` |
| Valor ≤ 0 | `RegraNegocioError` |
| Número já usado no exercício | `RegraNegocioError` |
| Dotação sem saldo | `DomOrcDomainError` (RN-ORC-032) |

**Regras aplicadas:** RN-CON-001, RN-CON-002

---

## CU-CON-002 — Liquidar empenho

**Ator:** AT-CON-001
**Capacidade:** CAP-CON-003
**Processo:** PRO-CON-003
**Implementador:** `LiquidarEmpenhoUseCase`
**Serviço:** SVC-CON-002

**Pré-condições:** O empenho existe e está em estado EMITIDO ou LIQUIDADO.

**Fluxo principal:**

1. Carregar o empenho pelo identificador.
2. Aplicar `Empenho.liquidar(valor)`, que valida valor positivo e saldo a liquidar (RN-CON-021).
3. Persistir o empenho com o valor liquidado acumulado.
4. Criar a `Liquidacao` vinculada ao empenho, com documento fiscal.
5. Confirmar a liquidação (RN-CON-020, RN-CON-022).
6. Persistir a liquidação.

**Pós-condições:** empenho em LIQUIDADO; liquidação em CONFIRMADA.

**Exceções:** empenho inexistente (`EmpenhoNaoEncontradoError`); valor acima do saldo
a liquidar; tentativa de liquidar empenho terminal.

**Regras aplicadas:** RN-CON-020, RN-CON-021, RN-CON-022

---

## CU-CON-003 — Pagar liquidação

**Ator:** AT-CON-005
**Capacidade:** CAP-CON-004
**Processo:** PRO-CON-004
**Implementador:** `PagarLiquidacaoUseCase`
**Serviço:** SVC-CON-004

**Pré-condições:** A liquidação existe e está CONFIRMADA (RN-CON-030); há saldo a pagar.

**Fluxo principal:**

1. Carregar a liquidação e exigir estado CONFIRMADA.
2. Carregar o empenho vinculado.
3. Aplicar `Empenho.pagar(valor)`, validando saldo a pagar (RN-CON-031).
4. Persistir o empenho com o valor pago acumulado.
5. Criar o `Pagamento` com conta bancária.
6. Efetivar o pagamento (RN-CON-032).
7. Persistir o pagamento.

**Pós-condições:** pagamento em EFETIVADO; empenho em PAGO se totalmente quitado.

**Exceções:** liquidação não confirmada; liquidação ou empenho inexistente; valor
acima do saldo a pagar.

**Regras aplicadas:** RN-CON-030, RN-CON-031, RN-CON-032

---

## CU-CON-004 — Anular empenho

**Ator:** AT-CON-001
**Capacidade:** CAP-CON-002
**Processo:** PRO-CON-005
**Implementador:** `AnularEmpenhoUseCase`
**Serviço:** SVC-CON-003

**Pré-condições:** O empenho existe e está em EMITIDO ou LIQUIDADO.

**Fluxo principal:**

1. Carregar o empenho.
2. Aplicar `Empenho.anular(valor, motivo)`, validando saldo a liquidar.
3. Devolver o valor à dotação pelo DOM-ORC.
4. Persistir empenho e dotação.

**Pós-condições:** valor anulado acumulado; empenho em ANULADO quando não restar
valor líquido nem liquidado.

**Regras aplicadas:** RN-CON-002, RN-CON-004

---

## CU-CON-005 — Cancelar empenho

**Ator:** AT-CON-002
**Capacidade:** CAP-CON-002
**Processo:** PRO-CON-006
**Implementador:** — (método de domínio `Empenho.cancelar`)

**Pré-condições:** O empenho existe e não está em PAGO (RN-CON-004).

**Fluxo principal:**

1. Carregar o empenho.
2. Recusar se o estado for PAGO.
3. Validar a transição para CANCELADO.
4. Registrar o motivo do cancelamento.

**Regras aplicadas:** RN-CON-004

**Observação:** não há serviço publicado para esta operação (lacuna B-05).

---

## CU-CON-006 — Criar conta contábil

**Ator:** AT-CON-003
**Capacidade:** CAP-CON-001
**Processo:** PRO-CON-001
**Implementador:** `CriarContaUseCase`
**Serviço:** SVC-CON-005

**Pré-condições:** Código e nome informados.

**Fluxo principal:**

1. Validar preenchimento de código e nome (RN-CON-010).
2. Verificar que o código não existe no plano.
3. Criar a conta com `aceita_lancamento` igual a `true` apenas para conta analítica.

**Regras aplicadas:** RN-CON-010, RN-CON-011

---

## CU-CON-007 — Lançar partidas dobradas

**Ator:** AT-CON-001
**Capacidade:** CAP-CON-005
**Processo:** PRO-CON-007
**Implementador:** `LancarContabilUseCase`
**Serviço:** SVC-CON-006

**Pré-condições:** Existem ao menos duas partidas; cada conta existe e aceita lançamento.

**Fluxo principal:**

1. Exigir ao menos duas partidas.
2. Para cada partida, carregar a conta e validar `pode_receber_lancamento()` (RN-CON-011, RN-CON-012).
3. Montar as `Partida` com tipo débito ou crédito.
4. Criar o `LancamentoContabil` com origem e totais.
5. Aplicar `lancar()`, que exige débito igual a crédito (RN-CON-040).
6. Persistir.

**Exceções:** menos de duas partidas; conta inexistente; conta que não aceita
lançamento; lançamento desequilibrado (`LancamentoDesequilibradoError`).

**Regras aplicadas:** RN-CON-011, RN-CON-012, RN-CON-040

---

## CU-CON-008 — Conciliar conta bancária

**Ator:** AT-CON-004
**Capacidade:** CAP-CON-006
**Processo:** PRO-CON-009
**Implementador:** `ConciliarContaUseCase`
**Serviço:** SVC-CON-007

**Pré-condições:** Conta e competência informadas.

**Fluxo principal:**

1. Criar a conciliação com os dois saldos.
2. Tentar `conciliar()`: calcula a diferença e exige que seja zero.
3. Havendo diferença e justificativa, marcar como DIVERGENTE (RN-CON-050).
4. Persistir a conciliação.

**Exceções:** divergência sem justificativa.

**Regras aplicadas:** RN-CON-050

---

# 4. Rastreabilidade dos Casos de Uso

| Caso de uso | Serviço | Regras | Teste unitário existente |
| --- | --- | --- | --- |
| CU-CON-001 Emitir empenho | SVC-CON-001 | RN-CON-001, RN-CON-002 | `test_con_use_cases.py` |
| CU-CON-002 Liquidar | SVC-CON-002 | RN-CON-020 a RN-CON-022 | `test_con_use_cases.py` |
| CU-CON-003 Pagar | SVC-CON-004 | RN-CON-030 a RN-CON-032 | `test_con_use_cases.py` |
| CU-CON-004 Anular | SVC-CON-003 | RN-CON-002, RN-CON-004 | — |
| CU-CON-005 Cancelar | — | RN-CON-004 | — |
| CU-CON-006 Criar conta | SVC-CON-005 | RN-CON-010 | `test_con_contabil.py` |
| CU-CON-007 Lançar | SVC-CON-006 | RN-CON-011, RN-CON-012, RN-CON-040 | `test_con_contabil.py` |
| CU-CON-008 Conciliar | SVC-CON-007 | RN-CON-050 | `test_con_contabil.py` |

Os casos CU-CON-004 e CU-CON-005 **não possuem teste automatizado**, o que é crítico
porque concentram as operações que alteram o saldo da dotação oramentária.

---

# 5. Lacunas Identificadas

| Lacuna | Casos afetados | Achado |
| --- | --- | --- |
| Casos implementados não expostos | todos | C-01 |
| Cancelamento sem serviço | CU-CON-005 | B-05 |
| Sem teste para anulação e cancelamento | CU-CON-004, CU-CON-005 | A-07 |
| Sem idempotência na reemissão | CU-CON-001 a CU-CON-003 | A-02 |


---

Este artefato especifica os casos de uso do domínio de Contabilidade Pública,
relacionando cada cenário à sua implementação na camada de casos de uso
(`src/modules/sigmun_con/application/`).

Cada caso de uso corresponde a uma classe concreta e a um serviço publicado. Cenários
de leitura direta ao repositório são identificados como tales, pois não exigem lógica
de negócio própria.

---

# 2. Convenções

* Casos de uso descrevem **cenários de negócio**; a implementação é referenciada
  pelo nome da classe correspondente.
* Regras aplicadas usam o padrão `RN-CON-<grupo><sequencial>`.
* A coluna **Estado** reflete a auditoria: implementados, mas **não expostos na API**.

---

# 3. Casos de Uso

## CU-CON-001 — Emitir empenho

**Ator:** AT-CON-001
**Capacidade:** CAP-CON-002
**Processo:** PRO-CON-002
**Implementador:** `EmitirEmpenhoUseCase`
**Serviço:** SVC-CON-001

**Pré-condições:** O servidor está autenticado e autorizado; existe dotação autorizada
com saldo disponível no DOM-ORC.

**Fluxo principal:**

1. Validar que o número do empenho foi informado (RN-CON-001).
2. Validar que o valor é maior que zero.
3. Verificar que não existe empenho com o mesmo número no exercício (RN-CON-001).
4. Debitar o valor na dotação recebida (RN-CON-002).
5. Criar a entidade `Empenho` com tipo, descrição e favorecido.
6. Persistir o empenho e devolver a entidade.

**Pós-condições:** empenho persistido em estado EMITIDO; saldo da dotação debitado.

**Fluxos alternativos e exceções:**

| Condição | Resultado |
| --- | --- |
| Número não informado | `RegraNegocioError` |
| Valor ≤ 0 | `RegraNegocioError` |
| Número já usado no exercício | `RegraNegocioError` |
| Dotação sem saldo | `DomOrcDomainError` (RN-ORC-032) |

**Regras aplicadas:** RN-CON-001, RN-CON-002

---

## CU-CON-002 — Liquidar empenho

**Ator:** AT-CON-001
**Capacidade:** CAP-CON-003
**Processo:** PRO-CON-003
**Implementador:** `LiquidarEmpenhoUseCase`
**Serviço:** SVC-CON-002

**Pré-condições:** O empenho existe e está em estado EMITIDO ou LIQUIDADO.

**Fluxo principal:**

1. Carregar o empenho pelo identificador.
2. Aplicar `Empenho.liquidar(valor)`, que valida valor positivo e saldo a liquidar (RN-CON-021).
3. Persistir o empenho com o valor liquidado acumulado.
4. Criar a `Liquidacao` vinculada ao empenho, com documento fiscal.
5. Confirmar a liquidação (RN-CON-020, RN-CON-022).
6. Persistir a liquidação.

**Pós-condições:** empenho em LIQUIDADO; liquidação em CONFIRMADA.

**Exceções:** empenho inexistente (`EmpenhoNaoEncontradoError`); valor acima do saldo
a liquidar; tentativa de liquidar empenho terminal.

**Regras aplicadas:** RN-CON-020, RN-CON-021, RN-CON-022

---

## CU-CON-003 — Pagar liquidação

**Ator:** AT-CON-005
**Capacidade:** CAP-CON-004
**Processo:** PRO-CON-004
**Implementador:** `PagarLiquidacaoUseCase`
**Serviço:** SVC-CON-004

**Pré-condições:** A liquidação existe e está CONFIRMADA (RN-CON-030); há saldo a pagar.

**Fluxo principal:**

1. Carregar a liquidação e exigir estado CONFIRMADA.
2. Carregar o empenho vinculado.
3. Aplicar `Empenho.pagar(valor)`, validando saldo a pagar (RN-CON-031).
4. Persistir o empenho com o valor pago acumulado.
5. Criar o `Pagamento` com conta bancária.
6. Efetivar o pagamento (RN-CON-032).
7. Persistir o pagamento.

**Pós-condições:** pagamento em EFETIVADO; empenho em PAGO se totalmente quitado.

**Exceções:** liquidação não confirmada; liquidação ou empenho inexistente; valor
acima do saldo a pagar.

**Regras aplicadas:** RN-CON-030, RN-CON-031, RN-CON-032

---

## CU-CON-004 — Anular empenho

**Ator:** AT-CON-001
**Capacidade:** CAP-CON-002
**Processo:** PRO-CON-005
**Implementador:** `AnularEmpenhoUseCase`
**Serviço:** SVC-CON-003

**Pré-condições:** O empenho existe e está em EMITIDO ou LIQUIDADO.

**Fluxo principal:**

1. Carregar o empenho.
2. Aplicar `Empenho.anular(valor, motivo)`, validando saldo a liquidar.
3. Devolver o valor à dotação pelo DOM-ORC.
4. Persistir empenho e dotação.

**Pós-condições:** valor anulado acumulado; empenho em ANULADO quando não restar
valor líquido nem liquidado.

**Regras aplicadas:** RN-CON-002, RN-CON-004

---

## CU-CON-005 — Cancelar empenho

**Ator:** AT-CON-002
**Capacidade:** CAP-CON-002
**Processo:** PRO-CON-006
**Implementador:** — (método de domínio `Empenho.cancelar`)

**Pré-condições:** O empenho existe e não está em PAGO (RN-CON-004).

**Fluxo principal:**

1. Carregar o empenho.
2. Recusar se o estado for PAGO.
3. Validar a transição para CANCELADO.
4. Registrar o motivo do cancelamento.

**Regras aplicadas:** RN-CON-004

**Observação:** não há serviço publicado para esta operação (lacuna B-05).

---

## CU-CON-006 — Criar conta contábil

**Ator:** AT-CON-003
**Capacidade:** CAP-CON-001
**Processo:** PRO-CON-001
**Implementador:** `CriarContaUseCase`
**Serviço:** SVC-CON-005

**Pré-condições:** Código e nome informados.

**Fluxo principal:**

1. Validar preenchimento de código e nome (RN-CON-010).
2. Verificar que o código não existe no plano.
3. Criar a conta com `aceita_lancamento` igual a `true` apenas para conta analítica.

**Regras aplicadas:** RN-CON-010, RN-CON-011

---

## CU-CON-007 — Lançar partidas dobradas

**Ator:** AT-CON-001
**Capacidade:** CAP-CON-005
**Processo:** PRO-CON-007
**Implementador:** `LancarContabilUseCase`
**Serviço:** SVC-CON-006

**Pré-condições:** Existem ao menos duas partidas; cada conta existe e aceita lançamento.

**Fluxo principal:**

1. Exigir ao menos duas partidas.
2. Para cada partida, carregar a conta e validar `pode_receber_lancamento()` (RN-CON-011, RN-CON-012).
3. Montar as `Partida` com tipo débito ou crédito.
4. Criar o `LancamentoContabil` com origem e totais.
5. Aplicar `lancar()`, que exige débito igual a crédito (RN-CON-040).
6. Persistir.

**Exceções:** menos de duas partidas; conta inexistente; conta que não aceita
lançamento; lançamento desequilibrado (`LancamentoDesequilibradoError`).

**Regras aplicadas:** RN-CON-011, RN-CON-012, RN-CON-040

---

## CU-CON-008 — Conciliar conta bancária

**Ator:** AT-CON-004
**Capacidade:** CAP-CON-006
**Processo:** PRO-CON-009
**Implementador:** `ConciliarContaUseCase`
**Serviço:** SVC-CON-007

**Pré-condições:** Conta e competência informadas.

**Fluxo principal:**

1. Criar a conciliação com os dois saldos.
2. Tentar `conciliar()`: calcula a diferença e exige que seja zero.
3. Havendo diferença e justificativa, marcar como DIVERGENTE (RN-CON-050).
4. Persistir a conciliação.

**Exceções:** divergência sem justificativa.

**Regras aplicadas:** RN-CON-050

---

# 4. Rastreabilidade dos Casos de Uso

| Caso de uso | Serviço | Regras | Teste unitário existente |
| --- | --- | --- | --- |
| CU-CON-001 Emitir empenho | SVC-CON-001 | RN-CON-001, RN-CON-002 | `test_con_use_cases.py` |
| CU-CON-002 Liquidar | SVC-CON-002 | RN-CON-020 a RN-CON-022 | `test_con_use_cases.py` |
| CU-CON-003 Pagar | SVC-CON-004 | RN-CON-030 a RN-CON-032 | `test_con_use_cases.py` |
| CU-CON-004 Anular | SVC-CON-003 | RN-CON-002, RN-CON-004 | — |
| CU-CON-005 Cancelar | — | RN-CON-004 | — |
| CU-CON-006 Criar conta | SVC-CON-005 | RN-CON-010 | `test_con_contabil.py` |
| CU-CON-007 Lançar | SVC-CON-006 | RN-CON-011, RN-CON-012, RN-CON-040 | `test_con_contabil.py` |
| CU-CON-008 Conciliar | SVC-CON-007 | RN-CON-050 | `test_con_contabil.py` |

Os casos CU-CON-004 e CU-CON-005 **não possuem teste automatizado**, o que é crítico
porque concentram as operações que alteram o saldo da dotação oramentária.

---

# 5. Lacunas Identificadas

| Lacuna | Casos afetados | Achado |
| --- | --- | --- |
| Casos implementados não expostos | todos | C-01 |
| Cancelamento sem serviço | CU-CON-005 | B-05 |
| Sem teste para anulação e cancelamento | CU-CON-004, CU-CON-005 | A-07 |
| Sem idempotência na reemissão | CU-CON-001 a CU-CON-003 | A-02 |

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 005-Casos-de-Uso-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
