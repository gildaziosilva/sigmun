# 010 – Especificações – Contabilidade Pública

#### Especificações – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-010

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

Este artefato especifica as especificações técnicas do domínio de Contabilidade
Pública, complementando os requisitos funcionais com o contrato de dados, as
validações, as regras de domínio e o comportamento esperado de cada operação.

---

# 2. Convenções

* Cada especificação declara o contrato de entrada, a validação, o comportamento e o
  contrato de saída.
* Validações de formato são implementadas nos schemas Pydantic; validações de regra são
  implementadas no domínio.
* A coluna **Situação** reflete a auditoria.

---

# 3. Especificação das Entidades

### 3.1 Empenho

| Campo | Domínio | Persistência | Observação |
| --- | --- | --- | --- |
| `id` | UUID | UUID | Gerado pelo domínio (`uuid4`) |
| `exercicio` | int | INTEGER | Obrigatório; validado ≥ 2000 na entrada |
| `numero` | string | TEXT | Obrigatório; único no exercício |
| `dotacao_id` | UUID | TEXT | Obrigatório; referência ao DOM-ORC |
| `reserva_id` | UUID | TEXT | Opcional; referência ao DOM-ORC |
| `favorecido_id` | UUID | **ausente** | **Lacuna A-01** |
| `favorecido_nome` | string | TEXT | Opcional |
| `tipo` | TipoEmpenho | TEXT | Padrão `ordinario` |
| `descricao` | string | TEXT | Opcional |
| `valor_empenhado` | decimal | FLOAT | Padrão 0 |
| `valor_anulado` | decimal | FLOAT | Padrão 0 |
| `valor_liquidado` | decimal | FLOAT | Padrão 0 |
| `valor_pago` | decimal | FLOAT | Padrão 0 |
| `status` | StatusEmpenho | TEXT | Padrão `emitido` |
| `data_emissao` | datetime | TIMESTAMPTZ | Padrão agora |
| `data_anulacao` | datetime | **ausente** | **Lacuna A-01** |
| `motivo_anulacao` | string | TEXT | Opcional |

**Propriedades derivadas:** `valor_liquido`, `saldo_a_liquidar`, `saldo_a_pagar`,
`is_terminal`, `is_active`.

### 3.2 Liquidacao

| Campo | Domínio | Persistência | Observação |
| --- | --- | --- | --- |
| `id` | UUID | UUID | Gerado pelo domínio |
| `empenho_id` | UUID | UUID | Obrigatório; FK com `ON DELETE RESTRICT` |
| `numero` | string | TEXT | Opcional |
| `valor` | decimal | FLOAT | Obrigatório |
| `documento_fiscal` | string | TEXT | Comprova a obrigação |
| `descricao` | string | **ausente** | **Lacuna A-01** |
| `status` | StatusLiquidacao | TEXT | Padrão `registrada` |
| `data_liquidacao` | datetime | **ausente** | **Lacuna A-01** |
| `data_cancelamento` | datetime | **ausente** | **Lacuna A-01** |
| `motivo_cancelamento` | string | TEXT | Opcional |

### 3.3 Pagamento

| Campo | Domínio | Persistência | Observação |
| --- | --- | --- | --- |
| `id` | UUID | UUID | Gerado pelo domínio |
| `liquidacao_id` | UUID | UUID | Obrigatório; FK com `RESTRICT` |
| `empenho_id` | UUID | UUID | Obrigatório; FK com `RESTRICT` |
| `numero_ob` | string | TEXT | Opcional |
| `valor` | decimal | FLOAT | Obrigatório |
| `conta_bancaria` | string | TEXT | Opcional |
| `descricao` | string | **ausente** | **Lacuna A-01** |
| `status` | StatusPagamento | TEXT | Padrão `programado` |
| `data_programacao` | datetime | **ausente** | **Lacuna A-01** |
| `data_efetivacao` | datetime | **ausente** | **Lacuna A-01** |
| `motivo_cancelamento` | string | TEXT | Opcional |

### 3.4 ContaContabil

| Campo | Domínio | Persistência | Observação |
| --- | --- | --- | --- |
| `id` | UUID | UUID | Gerado pelo domínio |
| `codigo` | string | TEXT | Obrigatório; **UNIQUE** |
| `nome` | string | TEXT | Obrigatório |
| `classe` | string | TEXT | Classe do PCASP |
| `grupo` | string | **ausente** | **Lacuna A-01** |
| `natureza_saldo` | string | TEXT | Padrão `devedora` |
| `tipo` | string | TEXT | Padrão `analitica` |
| `aceita_lancamento` | boolean | BOOLEAN | Derivado do tipo na criação |
| `ativa` | boolean | BOOLEAN | Padrão verdadeiro |
| `conta_pai_id` | UUID | TEXT | Auto-referência sem FK |

### 3.5 LancamentoContabil

| Campo | Domínio | Persistência | Observação |
| --- | --- | --- | --- |
| `id` | UUID | UUID | Gerado pelo domínio |
| `exercicio` | int | INTEGER | Obrigatório; validado ≥ 2000 |
| `numero` | string | TEXT | Opcional |
| `data_lancamento` | datetime | **ausente** | **Lacuna A-01 — viola o MCASP** |
| `historico` | string | TEXT | Opcional |
| `origem` | string | TEXT | Entidade de origem |
| `origem_id` | UUID | TEXT | Identificador da origem |
| `partidas` | list de Partida | TEXT (JSON) | Sem integridade referencial |
| `total_debito` | decimal | FLOAT | Somatório dos débitos |
| `total_credito` | decimal | FLOAT | Somatório dos créditos |
| `status` | StatusLancamento | TEXT | Padrão `rascunho` |

### 3.6 ConciliacaoContabil

| Campo | Domínio | Persistência | Observação |
| --- | --- | --- | --- |
| `id` | UUID | UUID | Gerado pelo domínio |
| `conta_id` | UUID | TEXT | Obrigatório; sem FK |
| `codigo_conta` | string | TEXT | Redundante para consulta |
| `competencia_ano` | int | INTEGER | Obrigatório; validado ≥ 2000 |
| `competencia_mes` | int | INTEGER | Obrigatório; validado 1–12 |
| `saldo_contabil` | decimal | FLOAT | Saldo contábil |
| `saldo_extrato` | decimal | FLOAT | Saldo do extrato |
| `diferenca` | decimal | FLOAT | Diferença apurada |
| `status` | StatusConciliacao | TEXT | Padrão `aberta` |
| `justificativa` | string | TEXT | Obrigatória se divergente |

---

# 4. Especificação das Validações

## 4.1 Validações de Formato (Pydantic)

| Campo | Regra | Erro |
| --- | --- | --- |
| `exercicio` | ≥ 2000 | 422 |
| `mes` | entre 1 e 12 | 422 |
| `valor` | > 0 | 422 |
| `numero` | obrigatório, comprimento ≥ 1 | 422 |
| `codigo_conta` | obrigatório | 422 |
| `partidas` | no mínimo 2 itens | 422 |
| `tipo` da partida | `debito` ou `credito` | 422 |

## 4.2 Validações de Regra (Domínio)

| Regra | Mensagem gerada |
| --- | --- |
| RN-CON-001 | "Empenho já existe" |
| RN-CON-003 | "Excede saldo a liquidar" |
| RN-CON-004 | "Transição inválida: estado_a → estado_b" |
| RN-CON-021 | "Excede saldo a liquidar" |
| RN-CON-030 | "Pagamento exige liquidação confirmada" |
| RN-CON-031 | "Pagamento excede saldo a pagar" |
| RN-CON-040 | "Débito diferente de crédito" |
| RN-CON-050 | "Há divergência; use divergente" |

---

# 5. Especificação das Operações

## 5.1 SVC-CON-001 — Emissão de empenho

**Entrada:** `exercicio`, `numero`, `dotacao_id`, `valor`, `favorecido_nome`,
`descricao`, `tipo`, `created_by`

**Pré-condições:** dotação existe e possui saldo; número não usado no exercício.

**Comportamento:**

1. Validar presença do número e valor positivo.
2. Verificar unicidade por exercício.
3. Debitar o valor na dotação (DOM-ORC).
4. Criar o empenho com tipo e favorecido.
5. Persistir o empenho e a dotação.

**Saída:** `id`, `exercicio`, `numero`, `valor_empenhado`, `valor_liquidado`,
`valor_pago`, `status`, `created_at`.

**Erros:** 404 dotação inexistente; 409 número duplicado ou saldo insuficiente;
422 payload inválido.

## 5.2 SVC-CON-002 — Liquidação

**Entrada:** `valor`, `documento`

**Comportamento:** carregar o empenho; aplicar `liquidar`; persistir; criar a
liquidação; confirmar; persistir.

**Saída:** `id`, `empenho_id`, `valor`, `status`, `created_at`.

**Erros:** 404 empenho inexistente; 409 saldo insuficiente ou estado inválido.

## 5.3 SVC-CON-003 — Anulação

**Entrada:** `valor`, `documento` (usado como motivo)

**Comportamento:** carregar empenho e dotação; aplicar `anular`; devolver saldo;
persistir ambos.

**Saída:** representação do empenho atualizado.

**Erros:** 404 empenho ou dotação inexistente; 409 valor acima do saldo.

## 5.4 SVC-CON-004 — Pagamento

**Entrada:** `liquidacao_id`, `valor`, `conta_bancaria`, `created_by`

**Comportamento:** carregar a liquidação; exigir CONFIRMADA; carregar o empenho;
aplicar `pagar`; criar o pagamento; efetivar; persistir.

**Saída:** `id`, `liquidacao_id`, `empenho_id`, `valor`, `status`, `created_at`.

**Erros:** 404 liquidação ou empenho inexistente; 409 não confirmada ou saldo
insuficiente.

## 5.5 SVC-CON-005 — Criação de conta

**Entrada:** `codigo`, `nome`, `classe`, `tipo`, `natureza`, `created_by`

**Comportamento:** validar obrigatoriedade; verificar unicidade do código; criar a
conta com `aceita_lancamento` conforme o tipo.

**Saída:** `id`, `codigo`, `nome`, `tipo`, `created_at`.

**Erros:** 409 código duplicado ou campo obrigatório ausente.

## 5.6 SVC-CON-006 — Lançamento contábil

**Entrada:** `exercicio`, `historico`, `partidas`, `origem`, `origem_id`, `created_by`

**Comportamento:** exigir no mínimo duas partidas; validar cada conta; montar as
partidas; aplicar `lancar`; persistir.

**Saída:** `id`, `exercicio`, `historico`, `total_debito`, `total_credito`, `status`.

**Erros:** 409 conta inválida, conta que não aceita lançamento ou lançamento
desequilibrado.

## 5.7 SVC-CON-007 — Conciliação

**Entrada:** `conta_id`, `codigo_conta`, `ano`, `mes`, `saldo_contabil`,
`saldo_extrato`, `justificativa`, `created_by`

**Comportamento:** criar a conciliação; tentar conciliar; havendo divergência e
justificativa, marcar como divergente.

**Saída:** `id`, `conta_id`, `competencia_ano`, `competencia_mes`, `saldo_contabil`,
`saldo_extrato`, `diferenca`, `status`.

**Erros:** 409 divergência sem justificativa.

---

# 6. Regras de Estado Especificadas

| Entidade | Estado inicial | Transições permitidas | Terminais |
| --- | --- | --- | --- |
| `Empenho` | EMITIDO | EMITIDO → LIQUIDADO, ANULADO, CANCELADO; LIQUIDADO → PAGO, EMITIDO, CANCELADO | PAGO, ANULADO, CANCELADO |
| `Liquidacao` | REGISTRADA | REGISTRADA → CONFIRMADA, CANCELADA | CONFIRMADA, CANCELADA |
| `Pagamento` | PROGRAMADO | PROGRAMADO → EFETIVADO, CANCELADO | EFETIVADO, CANCELADO |
| `LancamentoContabil` | RASCUNHO | RASCUNHO → LANCADO; LANCADO → ESTORNADO | ESTORNADO |
| `ConciliacaoContabil` | ABERTA | ABERTA → CONCILIADA, DIVERGENTE; DIVERGENTE → CONCILIADA | CONCILIADA |

---

# 7. Especificação da Precisão Monetária

| Aspecto | Especificação atual | Recomendação |
| --- | --- | --- |
| Tipo de coluna | `FLOAT` (dupla precisão) | `NUMERIC(15,2)` |
| Tolerância de balanço | 0,005 | Manter |
| Arredondamento da diferença | Duas casas | Manter |
| Validação de valor positivo | `> 0` | Manter |

O uso de ponto flutuante em valor monetário pode gerar diferença de arredondamento. A
tolerância de 0,005 mitiga o efeito no balanço, mas a migração para `NUMERIC` é
recomendada para sistemas contábeis e requer avaliação separada.

---

# 8. Especificação dos Códigos de Erro

| Situação | Código atual | Código correto | Ação |
| --- | --- | --- | --- |
| Recurso inexistente | 409 | **404** | Mapear exceções `*NaoEncontradaError` |
| Regra violada | 409 | 409 | Adequado |
| Duplicidade | 409 | 409 | Adequado |
| Saldo insuficiente | 409 | **422** | Mapear por tipo de regra |
| Payload inválido | 422 | 422 | Adequado |
| Transição inválida | 409 | 409 | Adequado |

O mapeamento por tipo requer a adoção das **oito exceções órfãs** declaradas em
`exceptions.py` (achado A-06).

---

# 9. Especificação da Integração com DOM-ORC

| Ponto de integração | Contrato | Garantia atual |
| --- | --- | --- |
| Busca de dotação | Retorna a dotação pelo identificador | Não há FK; dotação órfã é aceita |
| Débito na emissão | `empenhar_direto(valor)` | Validação em `Dotacao` |
| Devolução na anulação | `anular_empenho(valor)` | Validação em `Dotacao` |
| Atomicidade | Débito e gravação do empenho juntos | **Não garantida** |

**Requisito de atomicidade:** a emissão deve ocorrer em transação única que abranca o
DOM-ORC e o DOM-CON. Sem isso, uma falha após o débito deixa a dotação comprometida sem
registro contábil (achado RNF-CON-005).

---

# 10. Especificação da Trilha de Auditoria

| Campo | Especificação | Estado |
| --- | --- | --- |
| `created_at` | Data e hora da criação | Implementado |
| `created_by` | Identificador do usuário autenticado | **Não preenchido** |
| `updated_at` | Data e hora da última alteração | Parcial |
| `updated_by` | Autor da última alteração | Parcial |
| Evento de domínio | Publicação no barramento | **Inexistente** |
| Valores antes e depois | Registro da mutação | **Inexistente** |

---

# 11. Situações Conhecidas

| Situação | Descrição | Achado |
| --- | --- | --- |
| Sem transação entre domínios | Empenho e dotação em unidades transacionais distintas | RNF-CON-005 |
| Campos perdidos | Dez campos do domínio não são persistidos | A-01 |
| Sem índices | Nenhum índice no schema `con` | A-04 |
| Erro indiferenciado | Toda falha responde 409 | A-06 |
| Sem idempotência | Reenvio pode duplicar operação | A-02 |
| Sem eventos | Nenhuma integração assíncrona | M-01 |
| Lançamento manual | Reflexo contábil depende de intervenção humana | M-03 |


---

Este artefato especifica as especificações técnicas do domínio de Contabilidade
Pública, complementando os requisitos funcionais com o contrato de dados, as
validações, as regras de domínio e o comportamento esperado de cada operação.

---

# 2. Convenções

* Cada especificação declara o contrato de entrada, a validação, o comportamento e o
  contrato de saída.
* Validações de formato são implementadas nos schemas Pydantic; validações de regra são
  implementadas no domínio.
* A coluna **Situação** reflete a auditoria.

---

# 3. Especificação das Entidades

### 3.1 Empenho

| Campo | Domínio | Persistência | Observação |
| --- | --- | --- | --- |
| `id` | UUID | UUID | Gerado pelo domínio (`uuid4`) |
| `exercicio` | int | INTEGER | Obrigatório; validado ≥ 2000 na entrada |
| `numero` | string | TEXT | Obrigatório; único no exercício |
| `dotacao_id` | UUID | TEXT | Obrigatório; referência ao DOM-ORC |
| `reserva_id` | UUID | TEXT | Opcional; referência ao DOM-ORC |
| `favorecido_id` | UUID | **ausente** | **Lacuna A-01** |
| `favorecido_nome` | string | TEXT | Opcional |
| `tipo` | TipoEmpenho | TEXT | Padrão `ordinario` |
| `descricao` | string | TEXT | Opcional |
| `valor_empenhado` | decimal | FLOAT | Padrão 0 |
| `valor_anulado` | decimal | FLOAT | Padrão 0 |
| `valor_liquidado` | decimal | FLOAT | Padrão 0 |
| `valor_pago` | decimal | FLOAT | Padrão 0 |
| `status` | StatusEmpenho | TEXT | Padrão `emitido` |
| `data_emissao` | datetime | TIMESTAMPTZ | Padrão agora |
| `data_anulacao` | datetime | **ausente** | **Lacuna A-01** |
| `motivo_anulacao` | string | TEXT | Opcional |

**Propriedades derivadas:** `valor_liquido`, `saldo_a_liquidar`, `saldo_a_pagar`,
`is_terminal`, `is_active`.

### 3.2 Liquidacao

| Campo | Domínio | Persistência | Observação |
| --- | --- | --- | --- |
| `id` | UUID | UUID | Gerado pelo domínio |
| `empenho_id` | UUID | UUID | Obrigatório; FK com `ON DELETE RESTRICT` |
| `numero` | string | TEXT | Opcional |
| `valor` | decimal | FLOAT | Obrigatório |
| `documento_fiscal` | string | TEXT | Comprova a obrigação |
| `descricao` | string | **ausente** | **Lacuna A-01** |
| `status` | StatusLiquidacao | TEXT | Padrão `registrada` |
| `data_liquidacao` | datetime | **ausente** | **Lacuna A-01** |
| `data_cancelamento` | datetime | **ausente** | **Lacuna A-01** |
| `motivo_cancelamento` | string | TEXT | Opcional |

### 3.3 Pagamento

| Campo | Domínio | Persistência | Observação |
| --- | --- | --- | --- |
| `id` | UUID | UUID | Gerado pelo domínio |
| `liquidacao_id` | UUID | UUID | Obrigatório; FK com `RESTRICT` |
| `empenho_id` | UUID | UUID | Obrigatório; FK com `RESTRICT` |
| `numero_ob` | string | TEXT | Opcional |
| `valor` | decimal | FLOAT | Obrigatório |
| `conta_bancaria` | string | TEXT | Opcional |
| `descricao` | string | **ausente** | **Lacuna A-01** |
| `status` | StatusPagamento | TEXT | Padrão `programado` |
| `data_programacao` | datetime | **ausente** | **Lacuna A-01** |
| `data_efetivacao` | datetime | **ausente** | **Lacuna A-01** |
| `motivo_cancelamento` | string | TEXT | Opcional |

### 3.4 ContaContabil

| Campo | Domínio | Persistência | Observação |
| --- | --- | --- | --- |
| `id` | UUID | UUID | Gerado pelo domínio |
| `codigo` | string | TEXT | Obrigatório; **UNIQUE** |
| `nome` | string | TEXT | Obrigatório |
| `classe` | string | TEXT | Classe do PCASP |
| `grupo` | string | **ausente** | **Lacuna A-01** |
| `natureza_saldo` | string | TEXT | Padrão `devedora` |
| `tipo` | string | TEXT | Padrão `analitica` |
| `aceita_lancamento` | boolean | BOOLEAN | Derivado do tipo na criação |
| `ativa` | boolean | BOOLEAN | Padrão verdadeiro |
| `conta_pai_id` | UUID | TEXT | Auto-referência sem FK |

### 3.5 LancamentoContabil

| Campo | Domínio | Persistência | Observação |
| --- | --- | --- | --- |
| `id` | UUID | UUID | Gerado pelo domínio |
| `exercicio` | int | INTEGER | Obrigatório; validado ≥ 2000 |
| `numero` | string | TEXT | Opcional |
| `data_lancamento` | datetime | **ausente** | **Lacuna A-01 — viola o MCASP** |
| `historico` | string | TEXT | Opcional |
| `origem` | string | TEXT | Entidade de origem |
| `origem_id` | UUID | TEXT | Identificador da origem |
| `partidas` | list de Partida | TEXT (JSON) | Sem integridade referencial |
| `total_debito` | decimal | FLOAT | Somatório dos débitos |
| `total_credito` | decimal | FLOAT | Somatório dos créditos |
| `status` | StatusLancamento | TEXT | Padrão `rascunho` |

### 3.6 ConciliacaoContabil

| Campo | Domínio | Persistência | Observação |
| --- | --- | --- | --- |
| `id` | UUID | UUID | Gerado pelo domínio |
| `conta_id` | UUID | TEXT | Obrigatório; sem FK |
| `codigo_conta` | string | TEXT | Redundante para consulta |
| `competencia_ano` | int | INTEGER | Obrigatório; validado ≥ 2000 |
| `competencia_mes` | int | INTEGER | Obrigatório; validado 1–12 |
| `saldo_contabil` | decimal | FLOAT | Saldo contábil |
| `saldo_extrato` | decimal | FLOAT | Saldo do extrato |
| `diferenca` | decimal | FLOAT | Diferença apurada |
| `status` | StatusConciliacao | TEXT | Padrão `aberta` |
| `justificativa` | string | TEXT | Obrigatória se divergente |

---

# 4. Especificação das Validações

## 4.1 Validações de Formato (Pydantic)

| Campo | Regra | Erro |
| --- | --- | --- |
| `exercicio` | ≥ 2000 | 422 |
| `mes` | entre 1 e 12 | 422 |
| `valor` | > 0 | 422 |
| `numero` | obrigatório, comprimento ≥ 1 | 422 |
| `codigo_conta` | obrigatório | 422 |
| `partidas` | no mínimo 2 itens | 422 |
| `tipo` da partida | `debito` ou `credito` | 422 |

## 4.2 Validações de Regra (Domínio)

| Regra | Mensagem gerada |
| --- | --- |
| RN-CON-001 | "Empenho já existe" |
| RN-CON-003 | "Excede saldo a liquidar" |
| RN-CON-004 | "Transição inválida: estado_a → estado_b" |
| RN-CON-021 | "Excede saldo a liquidar" |
| RN-CON-030 | "Pagamento exige liquidação confirmada" |
| RN-CON-031 | "Pagamento excede saldo a pagar" |
| RN-CON-040 | "Débito diferente de crédito" |
| RN-CON-050 | "Há divergência; use divergente" |

---

# 5. Especificação das Operações

## 5.1 SVC-CON-001 — Emissão de empenho

**Entrada:** `exercicio`, `numero`, `dotacao_id`, `valor`, `favorecido_nome`,
`descricao`, `tipo`, `created_by`

**Pré-condições:** dotação existe e possui saldo; número não usado no exercício.

**Comportamento:**

1. Validar presença do número e valor positivo.
2. Verificar unicidade por exercício.
3. Debitar o valor na dotação (DOM-ORC).
4. Criar o empenho com tipo e favorecido.
5. Persistir o empenho e a dotação.

**Saída:** `id`, `exercicio`, `numero`, `valor_empenhado`, `valor_liquidado`,
`valor_pago`, `status`, `created_at`.

**Erros:** 404 dotação inexistente; 409 número duplicado ou saldo insuficiente;
422 payload inválido.

## 5.2 SVC-CON-002 — Liquidação

**Entrada:** `valor`, `documento`

**Comportamento:** carregar o empenho; aplicar `liquidar`; persistir; criar a
liquidação; confirmar; persistir.

**Saída:** `id`, `empenho_id`, `valor`, `status`, `created_at`.

**Erros:** 404 empenho inexistente; 409 saldo insuficiente ou estado inválido.

## 5.3 SVC-CON-003 — Anulação

**Entrada:** `valor`, `documento` (usado como motivo)

**Comportamento:** carregar empenho e dotação; aplicar `anular`; devolver saldo;
persistir ambos.

**Saída:** representação do empenho atualizado.

**Erros:** 404 empenho ou dotação inexistente; 409 valor acima do saldo.

## 5.4 SVC-CON-004 — Pagamento

**Entrada:** `liquidacao_id`, `valor`, `conta_bancaria`, `created_by`

**Comportamento:** carregar a liquidação; exigir CONFIRMADA; carregar o empenho;
aplicar `pagar`; criar o pagamento; efetivar; persistir.

**Saída:** `id`, `liquidacao_id`, `empenho_id`, `valor`, `status`, `created_at`.

**Erros:** 404 liquidação ou empenho inexistente; 409 não confirmada ou saldo
insuficiente.

## 5.5 SVC-CON-005 — Criação de conta

**Entrada:** `codigo`, `nome`, `classe`, `tipo`, `natureza`, `created_by`

**Comportamento:** validar obrigatoriedade; verificar unicidade do código; criar a
conta com `aceita_lancamento` conforme o tipo.

**Saída:** `id`, `codigo`, `nome`, `tipo`, `created_at`.

**Erros:** 409 código duplicado ou campo obrigatório ausente.

## 5.6 SVC-CON-006 — Lançamento contábil

**Entrada:** `exercicio`, `historico`, `partidas`, `origem`, `origem_id`, `created_by`

**Comportamento:** exigir no mínimo duas partidas; validar cada conta; montar as
partidas; aplicar `lancar`; persistir.

**Saída:** `id`, `exercicio`, `historico`, `total_debito`, `total_credito`, `status`.

**Erros:** 409 conta inválida, conta que não aceita lançamento ou lançamento
desequilibrado.

## 5.7 SVC-CON-007 — Conciliação

**Entrada:** `conta_id`, `codigo_conta`, `ano`, `mes`, `saldo_contabil`,
`saldo_extrato`, `justificativa`, `created_by`

**Comportamento:** criar a conciliação; tentar conciliar; havendo divergência e
justificativa, marcar como divergente.

**Saída:** `id`, `conta_id`, `competencia_ano`, `competencia_mes`, `saldo_contabil`,
`saldo_extrato`, `diferenca`, `status`.

**Erros:** 409 divergência sem justificativa.

---

# 6. Regras de Estado Especificadas

| Entidade | Estado inicial | Transições permitidas | Terminais |
| --- | --- | --- | --- |
| `Empenho` | EMITIDO | EMITIDO → LIQUIDADO, ANULADO, CANCELADO; LIQUIDADO → PAGO, EMITIDO, CANCELADO | PAGO, ANULADO, CANCELADO |
| `Liquidacao` | REGISTRADA | REGISTRADA → CONFIRMADA, CANCELADA | CONFIRMADA, CANCELADA |
| `Pagamento` | PROGRAMADO | PROGRAMADO → EFETIVADO, CANCELADO | EFETIVADO, CANCELADO |
| `LancamentoContabil` | RASCUNHO | RASCUNHO → LANCADO; LANCADO → ESTORNADO | ESTORNADO |
| `ConciliacaoContabil` | ABERTA | ABERTA → CONCILIADA, DIVERGENTE; DIVERGENTE → CONCILIADA | CONCILIADA |

---

# 7. Especificação da Precisão Monetária

| Aspecto | Especificação atual | Recomendação |
| --- | --- | --- |
| Tipo de coluna | `FLOAT` (dupla precisão) | `NUMERIC(15,2)` |
| Tolerância de balanço | 0,005 | Manter |
| Arredondamento da diferença | Duas casas | Manter |
| Validação de valor positivo | `> 0` | Manter |

O uso de ponto flutuante em valor monetário pode gerar diferença de arredondamento. A
tolerância de 0,005 mitiga o efeito no balanço, mas a migração para `NUMERIC` é
recomendada para sistemas contábeis e requer avaliação separada.

---

# 8. Especificação dos Códigos de Erro

| Situação | Código atual | Código correto | Ação |
| --- | --- | --- | --- |
| Recurso inexistente | 409 | **404** | Mapear exceções `*NaoEncontradaError` |
| Regra violada | 409 | 409 | Adequado |
| Duplicidade | 409 | 409 | Adequado |
| Saldo insuficiente | 409 | **422** | Mapear por tipo de regra |
| Payload inválido | 422 | 422 | Adequado |
| Transição inválida | 409 | 409 | Adequado |

O mapeamento por tipo requer a adoção das **oito exceções órfãs** declaradas em
`exceptions.py` (achado A-06).

---

# 9. Especificação da Integração com DOM-ORC

| Ponto de integração | Contrato | Garantia atual |
| --- | --- | --- |
| Busca de dotação | Retorna a dotação pelo identificador | Não há FK; dotação órfã é aceita |
| Débito na emissão | `empenhar_direto(valor)` | Validação em `Dotacao` |
| Devolução na anulação | `anular_empenho(valor)` | Validação em `Dotacao` |
| Atomicidade | Débito e gravação do empenho juntos | **Não garantida** |

**Requisito de atomicidade:** a emissão deve ocorrer em transação única que abranca o
DOM-ORC e o DOM-CON. Sem isso, uma falha após o débito deixa a dotação comprometida sem
registro contábil (achado RNF-CON-005).

---

# 10. Especificação da Trilha de Auditoria

| Campo | Especificação | Estado |
| --- | --- | --- |
| `created_at` | Data e hora da criação | Implementado |
| `created_by` | Identificador do usuário autenticado | **Não preenchido** |
| `updated_at` | Data e hora da última alteração | Parcial |
| `updated_by` | Autor da última alteração | Parcial |
| Evento de domínio | Publicação no barramento | **Inexistente** |
| Valores antes e depois | Registro da mutação | **Inexistente** |

---

# 11. Situações Conhecidas

| Situação | Descrição | Achado |
| --- | --- | --- |
| Sem transação entre domínios | Empenho e dotação em unidades transacionais distintas | RNF-CON-005 |
| Campos perdidos | Dez campos do domínio não são persistidos | A-01 |
| Sem índices | Nenhum índice no schema `con` | A-04 |
| Erro indiferenciado | Toda falha responde 409 | A-06 |
| Sem idempotência | Reenvio pode duplicar operação | A-02 |
| Sem eventos | Nenhuma integração assíncrona | M-01 |
| Lançamento manual | Reflexo contábil depende de intervenção humana | M-03 |

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 010-Especificacoes-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
