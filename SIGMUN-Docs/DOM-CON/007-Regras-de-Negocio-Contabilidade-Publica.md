# 007 – Regras de Negócio – Contabilidade Pública

#### Regras de Negócio – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-007

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

Este artefato consolida as regras de negócio do domínio de Contabilidade Pública,
declarando as invariantes que a implementação deve preservar.

As regras foram extraídas da implementação em
`src/modules/sigmun_con/domain/`, onde aparecem como docstrings e como estruturas de
dados (`TRANSICOES_EMPENHO`, `ESTADOS_TERMINAIS_EMPENHO`). A numeração é estável e
não é reutilizada.

---

# 2. Convenção de Identificação

As regras seguem o padrão `RN-CON-<grupo><sequencial>`, onde o grupo identifica a
entidade governada e o sequencial é estável no tempo.

| Grupo | Entidade governada |
| --- | --- |
| RN-CON-0**1**0 a RN-CON-0**1**9 | `Empenho` |
| RN-CON-0**2**0 a RN-CON-0**2**9 | `ContaContabil` (PCASP) |
| RN-CON-0**3**0 a RN-CON-0**3**9 | `Liquidacao` |
| RN-CON-0**4**0 a RN-CON-0**4**9 | `Pagamento` |
| RN-CON-0**5**0 a RN-CON-0**5**9 | `LancamentoContabil` |
| RN-CON-0**6**0 a RN-CON-0**6**9 | `ConciliacaoContabil` |
| RN-CON-0**7**0 a RN-CON-0**7**9 | Auditoria e transparência |

---

# 3. Classificação das Regras

| Tipo | Regras | Significado |
| --- | --- | --- |
| Máquina de estados | RN-CON-001, RN-CON-004, RN-CON-020, RN-CON-022, RN-CON-030, RN-CON-032 | Governa as transições permitidas entre situações. |
| Restrição | RN-CON-002, RN-CON-003, RN-CON-010, RN-CON-011, RN-CON-012, RN-CON-021, RN-CON-031 | Limita os valores aceitos pelo domínio. |
| Integridade | RN-CON-050, RN-CON-060 | Garante a reconciliação e a rastreabilidade. |

---

# 4. Regras do Empenho

## RN-CON-001 — Unicidade do Número do Empenho

**Tipo:** Máquina de estados · **Processo:** PRO-CON-002

**Descrição:** O número do empenho é único dentro do exercício; código e nome são
obrigatórios.

**Justificativa:** O número do empenho é a identificação legal da despesa e organiza a
execução por exercício. A duplicidade quebraria a ordenação e a prestacao de contas.

**Garantia técnica:** validação em `EmitirEmpenhoUseCase` por
`RepositorioEmpenho.get_by_numero_exercicio`.

**Lacuna:** a unicidade **não é garantida pelo banco** — não existe restrição
`UNIQUE (exercicio, numero)` em `con.empenhos`. A verificação em aplicação é
suscetível a condição de corrida (achado A-02).

---

## RN-CON-002 — Empenho Exige Saldo na Dotação

**Tipo:** Restrição · **Processo:** PRO-CON-002, PRO-CON-005

**Descrição:** O empenho exige saldo disponível na dotação; a anulação devolve o valor
à dotação de origem.

**Justificativa:** É o fundamento do princípio da universalidade: nenhum valor pode
ser comprometido acima da autorização orçamentária. A anulação restitui a
disponibilidade.

**Garantia técnica:** `Dotacao.empenhar_direto` no DOM-ORC (RN-ORC-032) e
`Dotacao.anular_empenho`.

**Observação:** a dependência funcional existe, mas **não há chave estrangeira** entre
`con.empenhos.dotacao_id` e `orc.dotacoes.id` (achado A-03).

---

## RN-CON-003 — Limite do Valor Liquidado

**Tipo:** Restrição · **Processo:** PRO-CON-002, PRO-CON-003

**Descrição:** O valor liquidado acumulado nunca excede o valor líquido do empenho.

**Justificativa:** Impede que se reconheça direito adquirido sobre objeto inexistente.

**Garantia técnica:** propriedade `saldo_a_liquidar` validada em `Empenho.liquidar`.

---

## RN-CON-004 — Estados Terminais do Empenho

**Tipo:** Máquina de estados · **Processo:** PRO-CON-005, PRO-CON-006

**Descrição:** Os estados PAGO, ANULADO e CANCELADO são terminais; empenho PAGO não
pode ser cancelado.

**Justificativa:** O encerramento do ciclo impede alteração posterior de registro já
efetivado no orçamento.

**Garantia técnica:** `ESTADOS_TERMINAIS_EMPENHO` e `TRANSICOES_EMPENHO`.

**Transições:**

| De | Para | Evento |
| --- | --- | --- |
| — | EMITIDO | emissão |
| EMITIDO | LIQUIDADO | primeira liquidação |
| EMITIDO | ANULADO | anulação integral |
| EMITIDO | CANCELADO | cancelamento |
| LIQUIDADO | PAGO | liquidação e pagamento totais |
| LIQUIDADO | EMITIDO | estorno zera o valor liquidado |
| LIQUIDADO | CANCELADO | cancelamento |
| PAGO | — | terminal |
| ANULADO | — | terminal |
| CANCELADO | — | terminal |

---

# 5. Regras do Plano de Contas

## RN-CON-010 — Unicidade do Código da Conta

**Tipo:** Restrição · **Processo:** PRO-CON-001

**Descrição:** O código da conta é único no plano vigente; código e nome são
obrigatórios.

**Garantia técnica:** `UNIQUE` em `con.contas_contabeis.codigo` e validação em
`CriarContaUseCase`.

---

## RN-CON-011 — Conta Sintética Não Recebe Lançamento

**Tipo:** Restrição · **Processo:** PRO-CON-001, PRO-CON-007

**Descrição:** Somente contas analíticas recebem lançamento; contas sintéticas apenas
consolidam o saldo das filhas.

**Justificativa:** Duplicar o valor em conta sintética e em suas filhas distorceria o
saldo contábil.

**Garantia técnica:** `ContaContabil.pode_receber_lancamento()` valida `tipo ==
"analitica"`; `CriarContaUseCase` define `aceita_lancamento` a partir do tipo.

---

## RN-CON-012 — Conta Inativa Não Recebe Lançamento

**Tipo:** Restrição · **Processo:** PRO-CON-001, PRO-CON-007

**Descrição:** Conta desativada não aceita lançamento.

**Justificativa:** Permite encerrar o uso de uma conta sem apagar o histórico.

**Garantia técnica:** `ContaContabil.is_active` considera `ativa` e `is_deleted`.

---

# 6. Regras da Liquidação

## RN-CON-020 — Vinculação da Liquidação ao Empenho

**Tipo:** Máquina de estados · **Processo:** PRO-CON-003

**Descrição:** A liquidação referencia empenho em EMITIDO ou LIQUIDADO, com saldo
disponível.

**Garantia técnica:** validação em `Empenho.liquidar`.

---

## RN-CON-021 — Limite do Valor da Liquidação

**Tipo:** Restrição · **Processo:** PRO-CON-003

**Descrição:** O valor da liquidação nunca excede o saldo a liquidar e deve ser maior
que zero.

**Garantia técnica:** `Empenho.liquidar` compara com `saldo_a_liquidar`.

---

## RN-CON-022 — Estados Terminais da Liquidação

**Tipo:** Máquina de estados · **Processo:** PRO-CON-003

**Descrição:** CONFIRMADA e CANCELADA são terminais; a confirmação exige o documento
fiscal que comprova a obrigação.

**Garantia técnica:** `TRANSICOES_LIQUIDACAO` e `Liquidacao.confirmar`.

---

# 7. Regras do Pagamento

## RN-CON-030 — Pagamento Exige Liquidação Confirmada

**Tipo:** Máquina de estados · **Processo:** PRO-CON-004

**Descrição:** Somente liquidação confirmada origina pagamento.

**Justificativa:** Só o direito adquirido limitado e documentado pode virar saída de
recursos.

**Garantia técnica:** `PagarLiquidacaoUseCase` verifica `StatusLiquidacao.CONFIRMADA`.

---

## RN-CON-031 — Limite do Valor Pago

**Tipo:** Restrição · **Processo:** PRO-CON-004

**Descrição:** O valor pago nunca excede o saldo a pagar da liquidação e deve ser maior
que zero.

**Garantia técnica:** `Empenho.pagar` compara com `saldo_a_pagar`.

---

## RN-CON-032 — Estados Terminais do Pagamento

**Tipo:** Máquina de estados · **Processo:** PRO-CON-004

**Descrição:** EFETIVADO e CANCELADO são terminais.

**Garantia técnica:** `Pagamento.efetivar` e `Pagamento.cancelar` validam estado
PROGRAMADO.

---

# 8. Regras do Lançamento Contábil

## RN-CON-050 — Partidas Dobradas Balanceadas

**Tipo:** Restrição · **Processo:** PRO-CON-007, PRO-CON-008

**Descrição:** O lançamento exige ao menos duas partidas e o total de débito deve igualar
o total de crédito, com diferença inferior a 0,005.

**Justificativa:** O método das partidas dobradas é a base da contabilidade pública; um
lançamento desequilibrado falseia o saldo de todas as contas.

**Garantia técnica:** `LancamentoContabil.balanceado` e `lancar()`, que lança
`LancamentoDesequilibradoError`.

**Lacuna:** as partidas são gravadas como **JSON em coluna TEXT**, sem tabela filha e
sem integridade referencial com as contas. O balanço é validado apenas na aplicação
(achado M-02).

---

## RN-CON-051 — Aceitabilidade da Conta no Lançamento

**Tipo:** Restrição · **Processo:** PRO-CON-007

**Descrição:** Toda partida referencia conta existente, analítica, ativa e com
`aceita_lancamento` verdadeiro.

**Garantia técnica:** `LancarContabilUseCase` valida `pode_receber_lancamento()` para
cada partida.

---

## RN-CON-052 — Origem do Lançamento

**Tipo:** Restrição · **Processo:** PRO-CON-007

**Descrição:** O lançamento registra `origem` e `origem_id`, permitindo rastrear a
operação orçamentária que o originou.

**Justificativa:** Sem a origem, não é possível ligar o reflexo contábil ao fato
orçamentário.

**Lacuna:** nenhum caso de uso do ciclo do empenho gera lançamento automaticamente —
o campo existe mas permanece vazio na prática (achado M-03).

---

# 9. Regras da Conciliação

## RN-CON-060 — Conciliação por Competência

**Tipo:** Integridade · **Processo:** PRO-CON-009

**Descrição:** A conciliação compara o saldo contábil com o extrato na competência
(ano e mês); diferença zero resulta em CONCILIADA.

**Garantia técnica:** `ConciliacaoContabil.conciliar` calcula a diferença com
arredondamento para duas casas.

---

## RN-CON-061 — Justificativa da Divergência

**Tipo:** Integridade · **Processo:** PRO-CON-009

**Descrição:** Havendo diferença, a conciliação é marcada como DIVERGENTE e exige
justificativa.

**Justificativa:** A divergência sem justificativa impede o fechamento da conciliação e
esconde irregularidade.

**Garantia técnica:** `marcar_divergente(justificativa)`; `ConciliarContaUseCase` exige
justificativa quando a conciliação falha.

**Lacuna:** o mês de competência não possui restrição `CHECK` no banco (achado M-04).

---

# 10. Regras de Auditoria

## RN-CON-070 — Autoria e Data da Operação

**Tipo:** Integridade · **Processo:** PRO-CON-011

**Descrição:** Toda operação com efeito contábil registra autor e data.

**Lacuna:** os campos `created_by` existem em todas as entidades, mas **não são
preenchidos** por nenhum caminho de escrita dos repositórios; `lancamentos` e
`conciliacoes` não possuem `updated_at` nem `updated_by` (achado M-04).

---

# 11. Matriz de Rastreabilidade das Regras

| Regra | Entidade | Onde é implementada | Teste |
| --- | --- | --- | --- |
| RN-CON-001 | `Empenho` | `EmitirEmpenhoUseCase` | parcial |
| RN-CON-002 | `Empenho` | `Dotacao.empenhar_direto` | parcial |
| RN-CON-003 | `Empenho` | `Empenho.saldo_a_liquidar` | — |
| RN-CON-004 | `Empenho` | `TRANSICOES_EMPENHO` | — |
| RN-CON-010 | `ContaContabil` | `UNIQUE` + `CriarContaUseCase` | parcial |
| RN-CON-011 | `ContaContabil` | `pode_receber_lancamento()` | parcial |
| RN-CON-012 | `ContaContabil` | `is_active` | — |
| RN-CON-020 | `Liquidacao` | `Empenho.liquidar` | — |
| RN-CON-021 | `Liquidacao` | `Empenho.liquidar` | parcial |
| RN-CON-022 | `Liquidacao` | `TRANSICOES_LIQUIDACAO` | — |
| RN-CON-030 | `Pagamento` | `PagarLiquidacaoUseCase` | — |
| RN-CON-031 | `Pagamento` | `Empenho.pagar` | — |
| RN-CON-032 | `Pagamento` | `StatusPagamento` | — |
| RN-CON-050 | `LancamentoContabil` | `balanceado` / `lancar()` | parcial |
| RN-CON-051 | `LancamentoContabil` | `LancarContabilUseCase` | parcial |
| RN-CON-052 | `LancamentoContabil` | campos `origem` / `origem_id` | — |
| RN-CON-060 | `ConciliacaoContabil` | `conciliar()` | parcial |
| RN-CON-061 | `ConciliacaoContabil` | `marcar_divergente()` | — |
| RN-CON-070 | todas | — (não implementada) | — |

Apenas 8 das 19 regras possuem algum teste. A cobertura de regras é uma das prioridades
da Onda 5 do plano de trabalho.


---

Este artefato consolida as regras de negócio do domínio de Contabilidade Pública,
declarando as invariantes que a implementação deve preservar.

As regras foram extraídas da implementação em
`src/modules/sigmun_con/domain/`, onde aparecem como docstrings e como estruturas de
dados (`TRANSICOES_EMPENHO`, `ESTADOS_TERMINAIS_EMPENHO`). A numeração é estável e
não é reutilizada.

---

# 2. Convenção de Identificação

As regras seguem o padrão `RN-CON-<grupo><sequencial>`, onde o grupo identifica a
entidade governada e o sequencial é estável no tempo.

| Grupo | Entidade governada |
| --- | --- |
| RN-CON-0**1**0 a RN-CON-0**1**9 | `Empenho` |
| RN-CON-0**2**0 a RN-CON-0**2**9 | `ContaContabil` (PCASP) |
| RN-CON-0**3**0 a RN-CON-0**3**9 | `Liquidacao` |
| RN-CON-0**4**0 a RN-CON-0**4**9 | `Pagamento` |
| RN-CON-0**5**0 a RN-CON-0**5**9 | `LancamentoContabil` |
| RN-CON-0**6**0 a RN-CON-0**6**9 | `ConciliacaoContabil` |
| RN-CON-0**7**0 a RN-CON-0**7**9 | Auditoria e transparência |

---

# 3. Classificação das Regras

| Tipo | Regras | Significado |
| --- | --- | --- |
| Máquina de estados | RN-CON-001, RN-CON-004, RN-CON-020, RN-CON-022, RN-CON-030, RN-CON-032 | Governa as transições permitidas entre situações. |
| Restrição | RN-CON-002, RN-CON-003, RN-CON-010, RN-CON-011, RN-CON-012, RN-CON-021, RN-CON-031 | Limita os valores aceitos pelo domínio. |
| Integridade | RN-CON-050, RN-CON-060 | Garante a reconciliação e a rastreabilidade. |

---

# 4. Regras do Empenho

## RN-CON-001 — Unicidade do Número do Empenho

**Tipo:** Máquina de estados · **Processo:** PRO-CON-002

**Descrição:** O número do empenho é único dentro do exercício; código e nome são
obrigatórios.

**Justificativa:** O número do empenho é a identificação legal da despesa e organiza a
execução por exercício. A duplicidade quebraria a ordenação e a prestacao de contas.

**Garantia técnica:** validação em `EmitirEmpenhoUseCase` por
`RepositorioEmpenho.get_by_numero_exercicio`.

**Lacuna:** a unicidade **não é garantida pelo banco** — não existe restrição
`UNIQUE (exercicio, numero)` em `con.empenhos`. A verificação em aplicação é
suscetível a condição de corrida (achado A-02).

---

## RN-CON-002 — Empenho Exige Saldo na Dotação

**Tipo:** Restrição · **Processo:** PRO-CON-002, PRO-CON-005

**Descrição:** O empenho exige saldo disponível na dotação; a anulação devolve o valor
à dotação de origem.

**Justificativa:** É o fundamento do princípio da universalidade: nenhum valor pode
ser comprometido acima da autorização orçamentária. A anulação restitui a
disponibilidade.

**Garantia técnica:** `Dotacao.empenhar_direto` no DOM-ORC (RN-ORC-032) e
`Dotacao.anular_empenho`.

**Observação:** a dependência funcional existe, mas **não há chave estrangeira** entre
`con.empenhos.dotacao_id` e `orc.dotacoes.id` (achado A-03).

---

## RN-CON-003 — Limite do Valor Liquidado

**Tipo:** Restrição · **Processo:** PRO-CON-002, PRO-CON-003

**Descrição:** O valor liquidado acumulado nunca excede o valor líquido do empenho.

**Justificativa:** Impede que se reconheça direito adquirido sobre objeto inexistente.

**Garantia técnica:** propriedade `saldo_a_liquidar` validada em `Empenho.liquidar`.

---

## RN-CON-004 — Estados Terminais do Empenho

**Tipo:** Máquina de estados · **Processo:** PRO-CON-005, PRO-CON-006

**Descrição:** Os estados PAGO, ANULADO e CANCELADO são terminais; empenho PAGO não
pode ser cancelado.

**Justificativa:** O encerramento do ciclo impede alteração posterior de registro já
efetivado no orçamento.

**Garantia técnica:** `ESTADOS_TERMINAIS_EMPENHO` e `TRANSICOES_EMPENHO`.

**Transições:**

| De | Para | Evento |
| --- | --- | --- |
| — | EMITIDO | emissão |
| EMITIDO | LIQUIDADO | primeira liquidação |
| EMITIDO | ANULADO | anulação integral |
| EMITIDO | CANCELADO | cancelamento |
| LIQUIDADO | PAGO | liquidação e pagamento totais |
| LIQUIDADO | EMITIDO | estorno zera o valor liquidado |
| LIQUIDADO | CANCELADO | cancelamento |
| PAGO | — | terminal |
| ANULADO | — | terminal |
| CANCELADO | — | terminal |

---

# 5. Regras do Plano de Contas

## RN-CON-010 — Unicidade do Código da Conta

**Tipo:** Restrição · **Processo:** PRO-CON-001

**Descrição:** O código da conta é único no plano vigente; código e nome são
obrigatórios.

**Garantia técnica:** `UNIQUE` em `con.contas_contabeis.codigo` e validação em
`CriarContaUseCase`.

---

## RN-CON-011 — Conta Sintética Não Recebe Lançamento

**Tipo:** Restrição · **Processo:** PRO-CON-001, PRO-CON-007

**Descrição:** Somente contas analíticas recebem lançamento; contas sintéticas apenas
consolidam o saldo das filhas.

**Justificativa:** Duplicar o valor em conta sintética e em suas filhas distorceria o
saldo contábil.

**Garantia técnica:** `ContaContabil.pode_receber_lancamento()` valida `tipo ==
"analitica"`; `CriarContaUseCase` define `aceita_lancamento` a partir do tipo.

---

## RN-CON-012 — Conta Inativa Não Recebe Lançamento

**Tipo:** Restrição · **Processo:** PRO-CON-001, PRO-CON-007

**Descrição:** Conta desativada não aceita lançamento.

**Justificativa:** Permite encerrar o uso de uma conta sem apagar o histórico.

**Garantia técnica:** `ContaContabil.is_active` considera `ativa` e `is_deleted`.

---

# 6. Regras da Liquidação

## RN-CON-020 — Vinculação da Liquidação ao Empenho

**Tipo:** Máquina de estados · **Processo:** PRO-CON-003

**Descrição:** A liquidação referencia empenho em EMITIDO ou LIQUIDADO, com saldo
disponível.

**Garantia técnica:** validação em `Empenho.liquidar`.

---

## RN-CON-021 — Limite do Valor da Liquidação

**Tipo:** Restrição · **Processo:** PRO-CON-003

**Descrição:** O valor da liquidação nunca excede o saldo a liquidar e deve ser maior
que zero.

**Garantia técnica:** `Empenho.liquidar` compara com `saldo_a_liquidar`.

---

## RN-CON-022 — Estados Terminais da Liquidação

**Tipo:** Máquina de estados · **Processo:** PRO-CON-003

**Descrição:** CONFIRMADA e CANCELADA são terminais; a confirmação exige o documento
fiscal que comprova a obrigação.

**Garantia técnica:** `TRANSICOES_LIQUIDACAO` e `Liquidacao.confirmar`.

---

# 7. Regras do Pagamento

## RN-CON-030 — Pagamento Exige Liquidação Confirmada

**Tipo:** Máquina de estados · **Processo:** PRO-CON-004

**Descrição:** Somente liquidação confirmada origina pagamento.

**Justificativa:** Só o direito adquirido limitado e documentado pode virar saída de
recursos.

**Garantia técnica:** `PagarLiquidacaoUseCase` verifica `StatusLiquidacao.CONFIRMADA`.

---

## RN-CON-031 — Limite do Valor Pago

**Tipo:** Restrição · **Processo:** PRO-CON-004

**Descrição:** O valor pago nunca excede o saldo a pagar da liquidação e deve ser maior
que zero.

**Garantia técnica:** `Empenho.pagar` compara com `saldo_a_pagar`.

---

## RN-CON-032 — Estados Terminais do Pagamento

**Tipo:** Máquina de estados · **Processo:** PRO-CON-004

**Descrição:** EFETIVADO e CANCELADO são terminais.

**Garantia técnica:** `Pagamento.efetivar` e `Pagamento.cancelar` validam estado
PROGRAMADO.

---

# 8. Regras do Lançamento Contábil

## RN-CON-050 — Partidas Dobradas Balanceadas

**Tipo:** Restrição · **Processo:** PRO-CON-007, PRO-CON-008

**Descrição:** O lançamento exige ao menos duas partidas e o total de débito deve igualar
o total de crédito, com diferença inferior a 0,005.

**Justificativa:** O método das partidas dobradas é a base da contabilidade pública; um
lançamento desequilibrado falseia o saldo de todas as contas.

**Garantia técnica:** `LancamentoContabil.balanceado` e `lancar()`, que lança
`LancamentoDesequilibradoError`.

**Lacuna:** as partidas são gravadas como **JSON em coluna TEXT**, sem tabela filha e
sem integridade referencial com as contas. O balanço é validado apenas na aplicação
(achado M-02).

---

## RN-CON-051 — Aceitabilidade da Conta no Lançamento

**Tipo:** Restrição · **Processo:** PRO-CON-007

**Descrição:** Toda partida referencia conta existente, analítica, ativa e com
`aceita_lancamento` verdadeiro.

**Garantia técnica:** `LancarContabilUseCase` valida `pode_receber_lancamento()` para
cada partida.

---

## RN-CON-052 — Origem do Lançamento

**Tipo:** Restrição · **Processo:** PRO-CON-007

**Descrição:** O lançamento registra `origem` e `origem_id`, permitindo rastrear a
operação orçamentária que o originou.

**Justificativa:** Sem a origem, não é possível ligar o reflexo contábil ao fato
orçamentário.

**Lacuna:** nenhum caso de uso do ciclo do empenho gera lançamento automaticamente —
o campo existe mas permanece vazio na prática (achado M-03).

---

# 9. Regras da Conciliação

## RN-CON-060 — Conciliação por Competência

**Tipo:** Integridade · **Processo:** PRO-CON-009

**Descrição:** A conciliação compara o saldo contábil com o extrato na competência
(ano e mês); diferença zero resulta em CONCILIADA.

**Garantia técnica:** `ConciliacaoContabil.conciliar` calcula a diferença com
arredondamento para duas casas.

---

## RN-CON-061 — Justificativa da Divergência

**Tipo:** Integridade · **Processo:** PRO-CON-009

**Descrição:** Havendo diferença, a conciliação é marcada como DIVERGENTE e exige
justificativa.

**Justificativa:** A divergência sem justificativa impede o fechamento da conciliação e
esconde irregularidade.

**Garantia técnica:** `marcar_divergente(justificativa)`; `ConciliarContaUseCase` exige
justificativa quando a conciliação falha.

**Lacuna:** o mês de competência não possui restrição `CHECK` no banco (achado M-04).

---

# 10. Regras de Auditoria

## RN-CON-070 — Autoria e Data da Operação

**Tipo:** Integridade · **Processo:** PRO-CON-011

**Descrição:** Toda operação com efeito contábil registra autor e data.

**Lacuna:** os campos `created_by` existem em todas as entidades, mas **não são
preenchidos** por nenhum caminho de escrita dos repositórios; `lancamentos` e
`conciliacoes` não possuem `updated_at` nem `updated_by` (achado M-04).

---

# 11. Matriz de Rastreabilidade das Regras

| Regra | Entidade | Onde é implementada | Teste |
| --- | --- | --- | --- |
| RN-CON-001 | `Empenho` | `EmitirEmpenhoUseCase` | parcial |
| RN-CON-002 | `Empenho` | `Dotacao.empenhar_direto` | parcial |
| RN-CON-003 | `Empenho` | `Empenho.saldo_a_liquidar` | — |
| RN-CON-004 | `Empenho` | `TRANSICOES_EMPENHO` | — |
| RN-CON-010 | `ContaContabil` | `UNIQUE` + `CriarContaUseCase` | parcial |
| RN-CON-011 | `ContaContabil` | `pode_receber_lancamento()` | parcial |
| RN-CON-012 | `ContaContabil` | `is_active` | — |
| RN-CON-020 | `Liquidacao` | `Empenho.liquidar` | — |
| RN-CON-021 | `Liquidacao` | `Empenho.liquidar` | parcial |
| RN-CON-022 | `Liquidacao` | `TRANSICOES_LIQUIDACAO` | — |
| RN-CON-030 | `Pagamento` | `PagarLiquidacaoUseCase` | — |
| RN-CON-031 | `Pagamento` | `Empenho.pagar` | — |
| RN-CON-032 | `Pagamento` | `StatusPagamento` | — |
| RN-CON-050 | `LancamentoContabil` | `balanceado` / `lancar()` | parcial |
| RN-CON-051 | `LancamentoContabil` | `LancarContabilUseCase` | parcial |
| RN-CON-052 | `LancamentoContabil` | campos `origem` / `origem_id` | — |
| RN-CON-060 | `ConciliacaoContabil` | `conciliar()` | parcial |
| RN-CON-061 | `ConciliacaoContabil` | `marcar_divergente()` | — |
| RN-CON-070 | todas | — (não implementada) | — |

Apenas 8 das 19 regras possuem algum teste. A cobertura de regras é uma das prioridades
da Onda 5 do plano de trabalho.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 007-Regras-de-Negocio-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
