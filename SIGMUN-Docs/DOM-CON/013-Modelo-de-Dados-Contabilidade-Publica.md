# 013 – Modelo de Dados – Contabilidade Pública

#### Modelo de Dados – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-013

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

Este artefato descreve o modelo de dados do domínio de Contabilidade Pública,
com base no schema `con` do PostgreSQL e nos modelos ORM definidos em
`src/modules/sigmun_con/infrastructure/database/`.

As tabelas foram criadas pelas migrations `20260919_05_dom_con_models` e
`20260919_06_dom_con_contabil`.

---

# 2. Convenções

* Todas as tabelas residem no schema `con`, exclusivo do domínio.
* A chave primária é `id` do tipo UUID.
* Campos de auditoria: `created_at`, `updated_at`, `created_by`, `updated_by`,
  `is_deleted` (exclusão lógica).
* Valores monetários usam `FLOAT` — ver ressalva de precisão na seção 7.

---

# 3. Entidades

| Entidade | Tabela | Chave natural | Cardinalidade |
| --- | --- | --- | --- |
| `Empenho` | `con.empenhos` | `numero` + `exercicio` | 1 — N `Liquidacao`, N `Pagamento` |
| `Liquidacao` | `con.liquidacoes` | `numero` | N — 1 `Empenho` |
| `Pagamento` | `con.pagamentos` | `numero_ob` | N — 1 `Liquidacao`, N — 1 `Empenho` |
| `ContaContabil` | `con.contas_contabeis` | `codigo` | 1 — N `Partida`, N `Conciliacao` |
| `LancamentoContabil` | `con.lancamentos` | `numero` + `exercicio` | 1 — N `Partida` (JSON) |
| `ConciliacaoContabil` | `con.conciliacoes` | `conta_id` + competência | N — 1 `ContaContabil` |

---

# 4. Tabela `con.empenhos`

| Coluna | Tipo | Nulo | Padrão | Descrição |
| --- | --- | --- | --- | --- |
| `id` | UUID | não | — | Chave primária |
| `exercicio` | INTEGER | não | — | Exercício fiscal |
| `numero` | TEXT | não | — | Número do empenho |
| `dotacao_id` | TEXT | não | — | Referência à dotação (DOM-ORC) |
| `reserva_id` | TEXT | sim | — | Referência à reserva (DOM-ORC) |
| `favorecido_nome` | TEXT | sim | — | Nome do favorecido |
| `tipo` | TEXT | não | `ordinario` | `ordinario`, `global`, `estimativo` |
| `descricao` | TEXT | sim | — | Descrição do objeto da despesa |
| `valor_empenhado` | FLOAT | não | `0` | Valor comprometido |
| `valor_anulado` | FLOAT | não | `0` | Valor anulado acumulado |
| `valor_liquidado` | FLOAT | não | `0` | Valor liquidado acumulado |
| `valor_pago` | FLOAT | não | `0` | Valor pago acumulado |
| `status` | TEXT | não | `emitido` | Estado do empenho |
| `data_emissao` | TIMESTAMPTZ | sim | `now()` | Data de emissão |
| `motivo_anulacao` | TEXT | sim | — | Motivo da anulação ou cancelamento |
| `created_at` | TIMESTAMPTZ | não | `now()` | Criação |
| `updated_at` | TIMESTAMPTZ | sim | — | Atualização |
| `created_by` | TEXT | sim | — | Autor |
| `updated_by` | TEXT | sim | — | Autor da última alteração |
| `is_deleted` | BOOLEAN | não | `false` | Exclusão lógica |

**Derivados (não persistidos):** `valor_liquido` = `valor_empenhado` − `valor_anulado`;
`saldo_a_liquidar` = `valor_liquido` − `valor_liquidado`; `saldo_a_pagar` =
`valor_liquidado` − `valor_pago`.

**Chaves estrangeiras:** nenhuma para `orc.dotacoes` nem `orc.reservas` (achado A-03).

---

# 5. Tabela `con.liquidacoes`

| Coluna | Tipo | Nulo | Descrição |
| --- | --- | --- | --- |
| `id` | UUID | não | Chave primária |
| `empenho_id` | UUID | não | FK `→ con.empenhos.id`, `ON DELETE RESTRICT` |
| `numero` | TEXT | sim | Número da liquidação |
| `valor` | FLOAT | não | Valor liquidado |
| `documento_fiscal` | TEXT | sim | Documento que comprova a obrigação |
| `status` | TEXT | não | `registrada`, `confirmada`, `cancelada` |
| `motivo_cancelamento` | TEXT | sim | Motivo do cancelamento |
| *auditoria* | — | — | `created_at`, `updated_at`, `created_by`, `updated_by`, `is_deleted` |

---

# 6. Tabela `con.pagamentos`

| Coluna | Tipo | Nulo | Descrição |
| --- | --- | --- | --- |
| `id` | UUID | não | Chave primária |
| `liquidacao_id` | UUID | não | FK `→ con.liquidacoes.id`, `ON DELETE RESTRICT` |
| `empenho_id` | UUID | não | FK `→ con.empenhos.id`, `ON DELETE RESTRICT` |
| `numero_ob` | TEXT | sim | Número da ordem bancária |
| `valor` | FLOAT | não | Valor pago |
| `conta_bancaria` | TEXT | sim | Conta de crédito |
| `status` | TEXT | não | `programado`, `efetivado`, `cancelado` |
| `motivo_cancelamento` | TEXT | sim | Motivo do cancelamento |
| *auditoria* | — | — | `created_at`, `updated_at`, `created_by`, `updated_by`, `is_deleted` |

A referência a `empenho_id` é **redundante** em relação a `liquidacao_id`, mas
intencional: viabiliza o relatório de execução e o estorno sem juntar a liquidação.

---

# 7. Tabela `con.contas_contabeis`

| Coluna | Tipo | Nulo | Descrição |
| --- | --- | --- | --- |
| `id` | UUID | não | Chave primária |
| `codigo` | TEXT | não | Código da conta — **UNIQUE** |
| `nome` | TEXT | não | Denominação |
| `classe` | TEXT | sim | Classe do PCASP (1 a 8) |
| `natureza_saldo` | TEXT | não | `devedora` ou `credora` |
| `tipo` | TEXT | não | `analitica` ou `sintetica` |
| `aceita_lancamento` | BOOLEAN | não | Permissão explícita de lançamento |
| `ativa` | BOOLEAN | não | Situação da conta |
| `conta_pai_id` | TEXT | sim | Auto-referência para a hierarquia |
| *auditoria* | — | — | `created_at`, `updated_at`, `created_by`, `is_deleted` |

---

# 8. Tabela `con.lancamentos`

| Coluna | Tipo | Nulo | Descrição |
| --- | --- | --- | --- |
| `id` | UUID | não | Chave primária |
| `exercicio` | INTEGER | não | Exercício de competência |
| `numero` | TEXT | sim | Número do lançamento |
| `historico` | TEXT | sim | Descrição do fato contábil |
| `origem` | TEXT | sim | Entidade que originou o lançamento |
| `origem_id` | TEXT | sim | Identificador da origem |
| `partidas` | TEXT | não | **JSON** com as partidas dobradas |
| `total_debito` | FLOAT | não | Somatório dos débitos |
| `total_credito` | FLOAT | não | Somatório dos créditos |
| `status` | TEXT | não | `rascunho`, `lancado`, `estornado` |
| *auditoria* | — | — | `created_at`, `created_by`, `is_deleted` |

**Ressalva:** as partidas são serializadas em JSON dentro de uma coluna TEXT. Não há
tabela filha, não há chave estrangeira para `contas_contabeis` e não há índice. A
integridade do balanço é validada apenas na camada de aplicação (achado M-02).

---

# 9. Tabela `con.conciliacoes`

| Coluna | Tipo | Nulo | Descrição |
| --- | --- | --- | --- |
| `id` | UUID | não | Chave primária |
| `conta_id` | TEXT | não | Referência à conta (sem FK) |
| `codigo_conta` | TEXT | sim | Código redundante para consulta |
| `competencia_ano` | INTEGER | não | Ano da competência |
| `competencia_mes` | INTEGER | não | Mês da competência (1 a 12) |
| `saldo_contabil` | FLOAT | não | Saldo segundo a contabilidade |
| `saldo_extrato` | FLOAT | não | Saldo segundo o extrato bancário |
| `diferenca` | FLOAT | não | Diferença apurada |
| `status` | TEXT | não | `aberta`, `conciliada`, `divergente` |
| `justificativa` | TEXT | sim | Justificativa da divergência |
| `data_conciliacao` | TIMESTAMPTZ | sim | Data da conciliação |
| *auditoria* | — | — | `created_at`, `created_by`, `is_deleted` |

Não há restrição `CHECK` para `competencia_mes` entre 1 e 12 (achado M-04).

---

# 10. Divergências entre Domínio e Persistência

A comparação campo a campo entre as entidades e os modelos identificou **10 campos
declarados no domínio sem coluna correspondente**, todos perdidos silenciosamente:

| Entidade | Campo perdido | Consequência |
| --- | --- | --- |
| `Empenho` | `favorecido_id` | Perda do vínculo com o fornecedor; resta apenas o nome livre |
| `Empenho` | `data_anulacao` | Impossibilidade de datar a anulação |
| `Liquidacao` | `descricao` | Perda de informação descritiva |
| `Liquidacao` | `data_liquidacao` | Impossibilidade de datar o direito adquirido |
| `Liquidacao` | `data_cancelamento` | Impossibilidade de datar o cancelamento |
| `Pagamento` | `descricao` | Perda de informação descritiva |
| `Pagamento` | `data_programacao` | Impossibilidade de datar a ordem bancária |
| `Pagamento` | `data_efetivacao` | Impossibilidade de datar a saída de recursos |
| `ContaContabil` | `grupo` | Perda da hierarquia oficial do PCASP |
| `LancamentoContabil` | `data_lancamento` | **Lançamento contábil sem data de competência — viola o MCASP** |

A correção está planejada na Onda 1 do plano de trabalho (tarefa 1.1).

---

# 11. Índices

**O schema `con` não possui nenhum índice.** As migrations não criam índices, o que
força varredura sequencial nos caminhos de consulta mais frequentes.

| Índice recomendado | Tabela | Consultas atendidas |
| --- | --- | --- |
| `ix_con_empenhos_dotacao_id` | `con.empenhos` | Empenhos por dotação |
| `ix_con_empenhos_status` | `con.empenhos` | Empenhos por estado |
| `ix_con_empenhos_exercicio` | `con.empenhos` | Empenhos por exercício |
| `ix_con_liquidacoes_empenho_id` | `con.liquidacoes` | Liquidações de um empenho |
| `ix_con_pagamentos_liquidacao_id` | `con.pagamentos` | Pagamentos de uma liquidação |
| `ix_con_conciliacoes_conta_competencia` | `con.conciliacoes` | Conciliação por conta e competência |
| `ix_con_lancamentos_origem` | `con.lancamentos` | Lançamentos por origem |

---

# 12. Precisão Monetária

Os valores monetários são armazenados como `FLOAT` (ponto flutuante de dupla
precisão). Na aritmética contábil isso pode gerar diferença de arredondamento,
embora o domínio_compare a diferença com tolerância de 0,005.

**Recomendação:** migrar para `NUMERIC(15,2)`, padrão adotado por sistemas contábeis
para valores em reais. Esta alteração está fora do escopo atual e requer avaliação
separada.

---

# 13. Referências Externas

| Coluna | Destino | Tipo de vínculo | Situação |
| --- | --- | --- | --- |
| `con.empenhos.dotacao_id` | `orc.dotacoes.id` | Identificador, sem FK | Pendente (A-03) |
| `con.empenhos.reserva_id` | `orc.reservas.id` | Identificador, sem FK | Pendente (A-03) |
| `con.conciliacoes.conta_id` | `con.contas_contabeis.id` | Identificador, sem FK | Pendente (A-03) |
| `con.contas_contabeis.conta_pai_id` | `con.contas_contabeis.id` | Identificador, sem FK | Pendente (A-03) |
| `con.lancamentos.partidas` | `con.contas_contabeis.id` | JSON sem FK | Pendente (M-02) |
| `con.pagamentos.conta_bancaria` | `fro.contas_bancarias` | Texto livre | Planejado |

---

# 14. Regras de Exclusão

Nenhuma tabela permite exclusão física quando há dependência:

* `liquidacoes.empenho_id` com `ON DELETE RESTRICT` impede apagar empenho com
  liquidação.
* `pagamentos.liquidacao_id` e `pagamentos.empenho_id` com `ON DELETE RESTRICT`
  impedem apagar registros que sustentam pagamento.
* Todas as tabelas possuem `is_deleted` para exclusão lógica.

Preservar a trilha contábil é requisito legal; a restrição é intencional.


---

Este artefato descreve o modelo de dados do domínio de Contabilidade Pública,
com base no schema `con` do PostgreSQL e nos modelos ORM definidos em
`src/modules/sigmun_con/infrastructure/database/`.

As tabelas foram criadas pelas migrations `20260919_05_dom_con_models` e
`20260919_06_dom_con_contabil`.

---

# 2. Convenções

* Todas as tabelas residem no schema `con`, exclusivo do domínio.
* A chave primária é `id` do tipo UUID.
* Campos de auditoria: `created_at`, `updated_at`, `created_by`, `updated_by`,
  `is_deleted` (exclusão lógica).
* Valores monetários usam `FLOAT` — ver ressalva de precisão na seção 7.

---

# 3. Entidades

| Entidade | Tabela | Chave natural | Cardinalidade |
| --- | --- | --- | --- |
| `Empenho` | `con.empenhos` | `numero` + `exercicio` | 1 — N `Liquidacao`, N `Pagamento` |
| `Liquidacao` | `con.liquidacoes` | `numero` | N — 1 `Empenho` |
| `Pagamento` | `con.pagamentos` | `numero_ob` | N — 1 `Liquidacao`, N — 1 `Empenho` |
| `ContaContabil` | `con.contas_contabeis` | `codigo` | 1 — N `Partida`, N `Conciliacao` |
| `LancamentoContabil` | `con.lancamentos` | `numero` + `exercicio` | 1 — N `Partida` (JSON) |
| `ConciliacaoContabil` | `con.conciliacoes` | `conta_id` + competência | N — 1 `ContaContabil` |

---

# 4. Tabela `con.empenhos`

| Coluna | Tipo | Nulo | Padrão | Descrição |
| --- | --- | --- | --- | --- |
| `id` | UUID | não | — | Chave primária |
| `exercicio` | INTEGER | não | — | Exercício fiscal |
| `numero` | TEXT | não | — | Número do empenho |
| `dotacao_id` | TEXT | não | — | Referência à dotação (DOM-ORC) |
| `reserva_id` | TEXT | sim | — | Referência à reserva (DOM-ORC) |
| `favorecido_nome` | TEXT | sim | — | Nome do favorecido |
| `tipo` | TEXT | não | `ordinario` | `ordinario`, `global`, `estimativo` |
| `descricao` | TEXT | sim | — | Descrição do objeto da despesa |
| `valor_empenhado` | FLOAT | não | `0` | Valor comprometido |
| `valor_anulado` | FLOAT | não | `0` | Valor anulado acumulado |
| `valor_liquidado` | FLOAT | não | `0` | Valor liquidado acumulado |
| `valor_pago` | FLOAT | não | `0` | Valor pago acumulado |
| `status` | TEXT | não | `emitido` | Estado do empenho |
| `data_emissao` | TIMESTAMPTZ | sim | `now()` | Data de emissão |
| `motivo_anulacao` | TEXT | sim | — | Motivo da anulação ou cancelamento |
| `created_at` | TIMESTAMPTZ | não | `now()` | Criação |
| `updated_at` | TIMESTAMPTZ | sim | — | Atualização |
| `created_by` | TEXT | sim | — | Autor |
| `updated_by` | TEXT | sim | — | Autor da última alteração |
| `is_deleted` | BOOLEAN | não | `false` | Exclusão lógica |

**Derivados (não persistidos):** `valor_liquido` = `valor_empenhado` − `valor_anulado`;
`saldo_a_liquidar` = `valor_liquido` − `valor_liquidado`; `saldo_a_pagar` =
`valor_liquidado` − `valor_pago`.

**Chaves estrangeiras:** nenhuma para `orc.dotacoes` nem `orc.reservas` (achado A-03).

---

# 5. Tabela `con.liquidacoes`

| Coluna | Tipo | Nulo | Descrição |
| --- | --- | --- | --- |
| `id` | UUID | não | Chave primária |
| `empenho_id` | UUID | não | FK `→ con.empenhos.id`, `ON DELETE RESTRICT` |
| `numero` | TEXT | sim | Número da liquidação |
| `valor` | FLOAT | não | Valor liquidado |
| `documento_fiscal` | TEXT | sim | Documento que comprova a obrigação |
| `status` | TEXT | não | `registrada`, `confirmada`, `cancelada` |
| `motivo_cancelamento` | TEXT | sim | Motivo do cancelamento |
| *auditoria* | — | — | `created_at`, `updated_at`, `created_by`, `updated_by`, `is_deleted` |

---

# 6. Tabela `con.pagamentos`

| Coluna | Tipo | Nulo | Descrição |
| --- | --- | --- | --- |
| `id` | UUID | não | Chave primária |
| `liquidacao_id` | UUID | não | FK `→ con.liquidacoes.id`, `ON DELETE RESTRICT` |
| `empenho_id` | UUID | não | FK `→ con.empenhos.id`, `ON DELETE RESTRICT` |
| `numero_ob` | TEXT | sim | Número da ordem bancária |
| `valor` | FLOAT | não | Valor pago |
| `conta_bancaria` | TEXT | sim | Conta de crédito |
| `status` | TEXT | não | `programado`, `efetivado`, `cancelado` |
| `motivo_cancelamento` | TEXT | sim | Motivo do cancelamento |
| *auditoria* | — | — | `created_at`, `updated_at`, `created_by`, `updated_by`, `is_deleted` |

A referência a `empenho_id` é **redundante** em relação a `liquidacao_id`, mas
intencional: viabiliza o relatório de execução e o estorno sem juntar a liquidação.

---

# 7. Tabela `con.contas_contabeis`

| Coluna | Tipo | Nulo | Descrição |
| --- | --- | --- | --- |
| `id` | UUID | não | Chave primária |
| `codigo` | TEXT | não | Código da conta — **UNIQUE** |
| `nome` | TEXT | não | Denominação |
| `classe` | TEXT | sim | Classe do PCASP (1 a 8) |
| `natureza_saldo` | TEXT | não | `devedora` ou `credora` |
| `tipo` | TEXT | não | `analitica` ou `sintetica` |
| `aceita_lancamento` | BOOLEAN | não | Permissão explícita de lançamento |
| `ativa` | BOOLEAN | não | Situação da conta |
| `conta_pai_id` | TEXT | sim | Auto-referência para a hierarquia |
| *auditoria* | — | — | `created_at`, `updated_at`, `created_by`, `is_deleted` |

---

# 8. Tabela `con.lancamentos`

| Coluna | Tipo | Nulo | Descrição |
| --- | --- | --- | --- |
| `id` | UUID | não | Chave primária |
| `exercicio` | INTEGER | não | Exercício de competência |
| `numero` | TEXT | sim | Número do lançamento |
| `historico` | TEXT | sim | Descrição do fato contábil |
| `origem` | TEXT | sim | Entidade que originou o lançamento |
| `origem_id` | TEXT | sim | Identificador da origem |
| `partidas` | TEXT | não | **JSON** com as partidas dobradas |
| `total_debito` | FLOAT | não | Somatório dos débitos |
| `total_credito` | FLOAT | não | Somatório dos créditos |
| `status` | TEXT | não | `rascunho`, `lancado`, `estornado` |
| *auditoria* | — | — | `created_at`, `created_by`, `is_deleted` |

**Ressalva:** as partidas são serializadas em JSON dentro de uma coluna TEXT. Não há
tabela filha, não há chave estrangeira para `contas_contabeis` e não há índice. A
integridade do balanço é validada apenas na camada de aplicação (achado M-02).

---

# 9. Tabela `con.conciliacoes`

| Coluna | Tipo | Nulo | Descrição |
| --- | --- | --- | --- |
| `id` | UUID | não | Chave primária |
| `conta_id` | TEXT | não | Referência à conta (sem FK) |
| `codigo_conta` | TEXT | sim | Código redundante para consulta |
| `competencia_ano` | INTEGER | não | Ano da competência |
| `competencia_mes` | INTEGER | não | Mês da competência (1 a 12) |
| `saldo_contabil` | FLOAT | não | Saldo segundo a contabilidade |
| `saldo_extrato` | FLOAT | não | Saldo segundo o extrato bancário |
| `diferenca` | FLOAT | não | Diferença apurada |
| `status` | TEXT | não | `aberta`, `conciliada`, `divergente` |
| `justificativa` | TEXT | sim | Justificativa da divergência |
| `data_conciliacao` | TIMESTAMPTZ | sim | Data da conciliação |
| *auditoria* | — | — | `created_at`, `created_by`, `is_deleted` |

Não há restrição `CHECK` para `competencia_mes` entre 1 e 12 (achado M-04).

---

# 10. Divergências entre Domínio e Persistência

A comparação campo a campo entre as entidades e os modelos identificou **10 campos
declarados no domínio sem coluna correspondente**, todos perdidos silenciosamente:

| Entidade | Campo perdido | Consequência |
| --- | --- | --- |
| `Empenho` | `favorecido_id` | Perda do vínculo com o fornecedor; resta apenas o nome livre |
| `Empenho` | `data_anulacao` | Impossibilidade de datar a anulação |
| `Liquidacao` | `descricao` | Perda de informação descritiva |
| `Liquidacao` | `data_liquidacao` | Impossibilidade de datar o direito adquirido |
| `Liquidacao` | `data_cancelamento` | Impossibilidade de datar o cancelamento |
| `Pagamento` | `descricao` | Perda de informação descritiva |
| `Pagamento` | `data_programacao` | Impossibilidade de datar a ordem bancária |
| `Pagamento` | `data_efetivacao` | Impossibilidade de datar a saída de recursos |
| `ContaContabil` | `grupo` | Perda da hierarquia oficial do PCASP |
| `LancamentoContabil` | `data_lancamento` | **Lançamento contábil sem data de competência — viola o MCASP** |

A correção está planejada na Onda 1 do plano de trabalho (tarefa 1.1).

---

# 11. Índices

**O schema `con` não possui nenhum índice.** As migrations não criam índices, o que
força varredura sequencial nos caminhos de consulta mais frequentes.

| Índice recomendado | Tabela | Consultas atendidas |
| --- | --- | --- |
| `ix_con_empenhos_dotacao_id` | `con.empenhos` | Empenhos por dotação |
| `ix_con_empenhos_status` | `con.empenhos` | Empenhos por estado |
| `ix_con_empenhos_exercicio` | `con.empenhos` | Empenhos por exercício |
| `ix_con_liquidacoes_empenho_id` | `con.liquidacoes` | Liquidações de um empenho |
| `ix_con_pagamentos_liquidacao_id` | `con.pagamentos` | Pagamentos de uma liquidação |
| `ix_con_conciliacoes_conta_competencia` | `con.conciliacoes` | Conciliação por conta e competência |
| `ix_con_lancamentos_origem` | `con.lancamentos` | Lançamentos por origem |

---

# 12. Precisão Monetária

Os valores monetários são armazenados como `FLOAT` (ponto flutuante de dupla
precisão). Na aritmética contábil isso pode gerar diferença de arredondamento,
embora o domínio_compare a diferença com tolerância de 0,005.

**Recomendação:** migrar para `NUMERIC(15,2)`, padrão adotado por sistemas contábeis
para valores em reais. Esta alteração está fora do escopo atual e requer avaliação
separada.

---

# 13. Referências Externas

| Coluna | Destino | Tipo de vínculo | Situação |
| --- | --- | --- | --- |
| `con.empenhos.dotacao_id` | `orc.dotacoes.id` | Identificador, sem FK | Pendente (A-03) |
| `con.empenhos.reserva_id` | `orc.reservas.id` | Identificador, sem FK | Pendente (A-03) |
| `con.conciliacoes.conta_id` | `con.contas_contabeis.id` | Identificador, sem FK | Pendente (A-03) |
| `con.contas_contabeis.conta_pai_id` | `con.contas_contabeis.id` | Identificador, sem FK | Pendente (A-03) |
| `con.lancamentos.partidas` | `con.contas_contabeis.id` | JSON sem FK | Pendente (M-02) |
| `con.pagamentos.conta_bancaria` | `fro.contas_bancarias` | Texto livre | Planejado |

---

# 14. Regras de Exclusão

Nenhuma tabela permite exclusão física quando há dependência:

* `liquidacoes.empenho_id` com `ON DELETE RESTRICT` impede apagar empenho com
  liquidação.
* `pagamentos.liquidacao_id` e `pagamentos.empenho_id` com `ON DELETE RESTRICT`
  impedem apagar registros que sustentam pagamento.
* Todas as tabelas possuem `is_deleted` para exclusão lógica.

Preservar a trilha contábil é requisito legal; a restrição é intencional.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 013-Modelo-de-Dados-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
