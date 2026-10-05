# 017 – Modelo de Auditoria – Contabilidade Pública

#### Modelo de Auditoria – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-017

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

Este artefato especifica o modelo de auditoria do domínio de Contabilidade Pública,
definindo o que deve ser registrado, como a trilha de auditoria deve ser estruturada e
quais os requisitos de responsabilização aplicáveis.

---

# 2. Finalidade da Auditoria Contábil

A auditoria contábil responde a três perguntas:

1. **Quem** realizou a operação?
2. **Quando** foi realizada?
3. **Em que termos** — valor antes e depois, estado e evidência?

Sem essas três respostas, o registro contábil não é auditável e a execução da despesa
não pode ser prestada ao órgão de controle.

---

# 3. Escopo Auditado

| Operação | Entidade | Evidência esperada | Estado |
| --- | --- | --- | --- |
| Emissão de empenho | `Empenho` | Autor, data, dotação, valor, tipo | Parcial |
| Liquidação | `Liquidacao` | Autor, data, valor, documento fiscal | Parcial |
| Pagamento | `Pagamento` | Autor, data, valor, conta, número da OB | Parcial |
| Anulação | `Empenho` | Autor, data, valor, motivo | **Ausente** |
| Cancelamento | `Empenho` | Autor, data, motivo | **Ausente** |
| Criação de conta | `ContaContabil` | Autor, data, código | Parcial |
| Lançamento contábil | `LancamentoContabil` | Autor, data, partidas, totais | **Ausente** |
| Estorno de lançamento | `LancamentoContabil` | Autor, data, justificativa | **Não implementada** |
| Conciliação | `ConciliacaoContabil` | Autor, data, saldos, divergência | **Ausente** |

---

# 4. Campos de Auditoria por Entidade

| Entidade | `created_at` | `created_by` | `updated_at` | `updated_by` |
| --- | --- | --- | --- | --- |
| `Empenho` | Sim | Sim | Sim | Sim |
| `Liquidacao` | Sim | Sim | Sim | Sim |
| `Pagamento` | Sim | Sim | Sim | Sim |
| `ContaContabil` | Sim | Sim | Sim | **Não** |
| `LancamentoContabil` | Sim | Sim | **Não** | **Não** |
| `ConciliacaoContabil` | Sim | Sim | **Não** | **Não** |

**Lacuna estrutural:** mesmo onde os campos existem, **`created_by` nunca é
preenchido** por nenhum caminho de escrita dos repositórios. A auditoria identifica
zero registros com autoria preenchida (achado M-04).

---

# 5. Eventos de Domínio Necessários

A auditoria de alto nível exige eventos, que hoje **não existem** (achado M-01):

| Evento | Disparado por | Dados mínimos |
| --- | --- | --- |
| `EmpenhoEmitido` | `EmitirEmpenhoUseCase` | empenho_id, dotacao_id, valor, autor |
| `EmpenhoLiquidado` | `LiquidarEmpenhoUseCase` | empenho_id, liquidacao_id, valor, autor |
| `EmpenhoPago` | `PagarLiquidacaoUseCase` | empenho_id, pagamento_id, valor, conta, autor |
| `EmpenhoAnulado` | `AnularEmpenhoUseCase` | empenho_id, valor, motivo, autor |
| `EmpenhoCancelado` | `Empenho.cancelar` | empenho_id, motivo, autor |
| `LancamentoRegistrado` | `LancarContabilUseCase` | lancamento_id, total_debito, total_credito, origem, autor |
| `LancamentoEstornado` | — | lancamento_id, justificativa, autor |
| `ConciliacaoDivergente` | `ConciliarContaUseCase` | conciliacao_id, conta, competencia, diferenca, justificativa |

---

# 6. Trilha de Auditoria

## 6.1 Estrutura Mínima

```json
{
  "evento_id": "uuid",
  "timestamp": "2026-09-30T14:32:11Z",
  "autor_id": "uuid",
  "autor_nome": "string",
  "papel": "contador",
  "operacao": "empenho.emitir",
  "entidade": "empenho",
  "entidade_id": "uuid",
  "valores_antes": { "status": "—", "valor_liquidado": 0 },
  "valores_depois": { "status": "emitido", "valor_liquidado": 0 },
  "referencias": { "dotacao_id": "uuid" },
  "correlacao_id": "uuid"
}
```

**Justificativa do `valores_antes` e `valores_depois`:** a responsabilização exige saber
o que mudou. O repositório atual atualiza campos **sem registrar o valor anterior**.

## 6.2 Imutabilidade

O registro de auditoria, uma vez gravado, **não pode ser alterado nem removido**.
Recomenda-se armazenamento em tabela somente-insert, com restrição que impeça
`UPDATE` e `DELETE`.

---

# 7. Requisitos de Rastreabilidade

| Requisito | Origem | Situação |
| --- | --- | --- |
| Registrar autor em toda operação | RN-CON-070 | **Não implementada** |
| Registrar data em toda operação | RN-CON-070 | Parcial |
| Preservar histórico de alterações | RN-CON-070 | Parcial — `updated_at` não é preenchido |
| Registrar motivo de anulação e cancelamento | RN-CON-002 | Parcial |
| Registrar justificativa de divergência | RN-CON-061 | Implementada |
| Impedir alteração de lançamento lançado | RNF-CON-009 | Planejado |
| Correlacionar operações entre domínios | RNF-CON-018 | Planejado |

---

# 8. Rastreabilidade do Empenho

Para permitir auditoria completa, o ciclo do empenho deve ser reconstituível:

| Etapa | Data | Valor acumulado | Estado | Autor |
| --- | --- | --- | --- | --- |
| Emissão | `data_emissao` | `valor_empenhado` | EMITIDO | A preencher |
| Liquidação | `data_liquidacao` | `valor_liquidado` | LIQUIDADO | A preencher |
| Pagamento | `data_efetivacao` | `valor_pago` | PAGO | A preencher |
| Anulação | `data_anulacao` | `valor_anulado` | ANULADO | A preencher |

**Estado atual:** apenas `data_emissao` é persistida. **Quatro das cinco datas do
ciclo são perdidas** — o que impede reconstituir a linha do tempo da despesa
(achado A-01).

---

# 9. Auditoria Externa

Para atendimento ao Tribunal de Contas, o domínio deve permitir:

| Necessidade | Atende hoje |
| --- | --- |
| Extrato da execução por exercício e dotação | Não (RF-CON-028 inexistente) |
| Relação de empenhos, liquidações e pagamentos | Não |
| Extrato de lançamentos por conta e competência | Não |
| Registro de conciliações e divergências justificadas | Parcial — dados existem, consulta não |
| Identificação do responsável por cada operação | Não |
| Documento comprobatório da despesa | Não — DOM-GDO não integrado |

**Conclusão:** o domínio **não está em condições de prestar contas ao Tribunal de
Contas**. Não por ausência de dados — que em boa parte existem — mas por ausência
dos meios de consulta e de atribuição de autoria.

---

# 10. Plano de Adequação

| Prioridade | Ação | Onda |
| --- | --- | --- |
| 1 | Preencher `created_by` a partir do usuário autenticado | Onda 4, tarefa 4.4 |
| 2 | Criar as 10 colunas ausentes, incluindo as datas do ciclo | Onda 1, tarefa 1.1 |
| 3 | Implementar `updated_at` e `updated_by` em lançamentos e conciliações | Onda 4, tarefa 4.4 |
| 4 | Emitir eventos de domínio | Onda 4, tarefa 4.5 |
| 5 | Registrar valores antes e depois | Onda 4, tarefa 4.5 |
| 6 | Tornar a tabela de auditoria somente-insert | Onda 4 |
| 7 | Implementar consulta de execução para controle externo | Onda 3, Onda 7 |


---

Este artefato especifica o modelo de auditoria do domínio de Contabilidade Pública,
definindo o que deve ser registrado, como a trilha de auditoria deve ser estruturada e
quais os requisitos de responsabilização aplicáveis.

---

# 2. Finalidade da Auditoria Contábil

A auditoria contábil responde a três perguntas:

1. **Quem** realizou a operação?
2. **Quando** foi realizada?
3. **Em que termos** — valor antes e depois, estado e evidência?

Sem essas três respostas, o registro contábil não é auditável e a execução da despesa
não pode ser prestada ao órgão de controle.

---

# 3. Escopo Auditado

| Operação | Entidade | Evidência esperada | Estado |
| --- | --- | --- | --- |
| Emissão de empenho | `Empenho` | Autor, data, dotação, valor, tipo | Parcial |
| Liquidação | `Liquidacao` | Autor, data, valor, documento fiscal | Parcial |
| Pagamento | `Pagamento` | Autor, data, valor, conta, número da OB | Parcial |
| Anulação | `Empenho` | Autor, data, valor, motivo | **Ausente** |
| Cancelamento | `Empenho` | Autor, data, motivo | **Ausente** |
| Criação de conta | `ContaContabil` | Autor, data, código | Parcial |
| Lançamento contábil | `LancamentoContabil` | Autor, data, partidas, totais | **Ausente** |
| Estorno de lançamento | `LancamentoContabil` | Autor, data, justificativa | **Não implementada** |
| Conciliação | `ConciliacaoContabil` | Autor, data, saldos, divergência | **Ausente** |

---

# 4. Campos de Auditoria por Entidade

| Entidade | `created_at` | `created_by` | `updated_at` | `updated_by` |
| --- | --- | --- | --- | --- |
| `Empenho` | Sim | Sim | Sim | Sim |
| `Liquidacao` | Sim | Sim | Sim | Sim |
| `Pagamento` | Sim | Sim | Sim | Sim |
| `ContaContabil` | Sim | Sim | Sim | **Não** |
| `LancamentoContabil` | Sim | Sim | **Não** | **Não** |
| `ConciliacaoContabil` | Sim | Sim | **Não** | **Não** |

**Lacuna estrutural:** mesmo onde os campos existem, **`created_by` nunca é
preenchido** por nenhum caminho de escrita dos repositórios. A auditoria identifica
zero registros com autoria preenchida (achado M-04).

---

# 5. Eventos de Domínio Necessários

A auditoria de alto nível exige eventos, que hoje **não existem** (achado M-01):

| Evento | Disparado por | Dados mínimos |
| --- | --- | --- |
| `EmpenhoEmitido` | `EmitirEmpenhoUseCase` | empenho_id, dotacao_id, valor, autor |
| `EmpenhoLiquidado` | `LiquidarEmpenhoUseCase` | empenho_id, liquidacao_id, valor, autor |
| `EmpenhoPago` | `PagarLiquidacaoUseCase` | empenho_id, pagamento_id, valor, conta, autor |
| `EmpenhoAnulado` | `AnularEmpenhoUseCase` | empenho_id, valor, motivo, autor |
| `EmpenhoCancelado` | `Empenho.cancelar` | empenho_id, motivo, autor |
| `LancamentoRegistrado` | `LancarContabilUseCase` | lancamento_id, total_debito, total_credito, origem, autor |
| `LancamentoEstornado` | — | lancamento_id, justificativa, autor |
| `ConciliacaoDivergente` | `ConciliarContaUseCase` | conciliacao_id, conta, competencia, diferenca, justificativa |

---

# 6. Trilha de Auditoria

## 6.1 Estrutura Mínima

```json
{
  "evento_id": "uuid",
  "timestamp": "2026-09-30T14:32:11Z",
  "autor_id": "uuid",
  "autor_nome": "string",
  "papel": "contador",
  "operacao": "empenho.emitir",
  "entidade": "empenho",
  "entidade_id": "uuid",
  "valores_antes": { "status": "—", "valor_liquidado": 0 },
  "valores_depois": { "status": "emitido", "valor_liquidado": 0 },
  "referencias": { "dotacao_id": "uuid" },
  "correlacao_id": "uuid"
}
```

**Justificativa do `valores_antes` e `valores_depois`:** a responsabilização exige saber
o que mudou. O repositório atual atualiza campos **sem registrar o valor anterior**.

## 6.2 Imutabilidade

O registro de auditoria, uma vez gravado, **não pode ser alterado nem removido**.
Recomenda-se armazenamento em tabela somente-insert, com restrição que impeça
`UPDATE` e `DELETE`.

---

# 7. Requisitos de Rastreabilidade

| Requisito | Origem | Situação |
| --- | --- | --- |
| Registrar autor em toda operação | RN-CON-070 | **Não implementada** |
| Registrar data em toda operação | RN-CON-070 | Parcial |
| Preservar histórico de alterações | RN-CON-070 | Parcial — `updated_at` não é preenchido |
| Registrar motivo de anulação e cancelamento | RN-CON-002 | Parcial |
| Registrar justificativa de divergência | RN-CON-061 | Implementada |
| Impedir alteração de lançamento lançado | RNF-CON-009 | Planejado |
| Correlacionar operações entre domínios | RNF-CON-018 | Planejado |

---

# 8. Rastreabilidade do Empenho

Para permitir auditoria completa, o ciclo do empenho deve ser reconstituível:

| Etapa | Data | Valor acumulado | Estado | Autor |
| --- | --- | --- | --- | --- |
| Emissão | `data_emissao` | `valor_empenhado` | EMITIDO | A preencher |
| Liquidação | `data_liquidacao` | `valor_liquidado` | LIQUIDADO | A preencher |
| Pagamento | `data_efetivacao` | `valor_pago` | PAGO | A preencher |
| Anulação | `data_anulacao` | `valor_anulado` | ANULADO | A preencher |

**Estado atual:** apenas `data_emissao` é persistida. **Quatro das cinco datas do
ciclo são perdidas** — o que impede reconstituir a linha do tempo da despesa
(achado A-01).

---

# 9. Auditoria Externa

Para atendimento ao Tribunal de Contas, o domínio deve permitir:

| Necessidade | Atende hoje |
| --- | --- |
| Extrato da execução por exercício e dotação | Não (RF-CON-028 inexistente) |
| Relação de empenhos, liquidações e pagamentos | Não |
| Extrato de lançamentos por conta e competência | Não |
| Registro de conciliações e divergências justificadas | Parcial — dados existem, consulta não |
| Identificação do responsável por cada operação | Não |
| Documento comprobatório da despesa | Não — DOM-GDO não integrado |

**Conclusão:** o domínio **não está em condições de prestar contas ao Tribunal de
Contas**. Não por ausência de dados — que em boa parte existem — mas por ausência
dos meios de consulta e de atribuição de autoria.

---

# 10. Plano de Adequação

| Prioridade | Ação | Onda |
| --- | --- | --- |
| 1 | Preencher `created_by` a partir do usuário autenticado | Onda 4, tarefa 4.4 |
| 2 | Criar as 10 colunas ausentes, incluindo as datas do ciclo | Onda 1, tarefa 1.1 |
| 3 | Implementar `updated_at` e `updated_by` em lançamentos e conciliações | Onda 4, tarefa 4.4 |
| 4 | Emitir eventos de domínio | Onda 4, tarefa 4.5 |
| 5 | Registrar valores antes e depois | Onda 4, tarefa 4.5 |
| 6 | Tornar a tabela de auditoria somente-insert | Onda 4 |
| 7 | Implementar consulta de execução para controle externo | Onda 3, Onda 7 |

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 017-Modelo-de-Auditoria-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
