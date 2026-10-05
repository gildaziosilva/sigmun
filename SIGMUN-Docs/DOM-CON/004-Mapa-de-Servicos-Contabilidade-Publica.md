# 004 – Mapa de Serviços – Contabilidade Pública

#### Mapa de Serviços – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-004

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

Este artefato consolida os serviços expostos pelo domínio de Contabilidade Pública,
relacionando cada serviço ao processo que executa, ao caso de uso correspondente, ao
endpoint que o disponibiliza e às regras aplicadas.

A implementação atual define sete serviços, todos sob o prefixo `/api/v1/con` e todos
com a tag `Contabilidade Pública`. **Nenhum deles está registrado na aplicação** — ver
achado C-01 da auditoria.

---

# 2. Princípios

* Um serviço é a unidade publicamente addressável do domínio.
* Cada serviço corresponde a um caso de uso da camada de aplicação.
* Serviços são síncronos; integrações com outros domínios ocorrem dentro do caso de uso.
* O serviço não decide regra de negócio: ele delega ao caso de uso.

---

# 3. Serviços Identificados

| Identificador | Serviço | Método e caminho | Caso de uso | Estado HTTP |
| --- | --- | --- | --- | --- |
| SVC-CON-001 | Emissão de empenho | `POST /api/v1/con/empenhos` | `EmitirEmpenhoUseCase` | 201 |
| SVC-CON-002 | Liquidação de empenho | `POST /api/v1/con/empenhos/{empenho_id}/liquidar` | `LiquidarEmpenhoUseCase` | 200 |
| SVC-CON-003 | Anulação de empenho | `POST /api/v1/con/empenhos/{empenho_id}/anular` | `AnularEmpenhoUseCase` | 200 |
| SVC-CON-004 | Pagamento de liquidação | `POST /api/v1/con/pagamentos` | `PagarLiquidacaoUseCase` | 201 |
| SVC-CON-005 | Criação de conta contábil | `POST /api/v1/con/contas` | `CriarContaUseCase` | 201 |
| SVC-CON-006 | Lançamento contábil | `POST /api/v1/con/lancamentos` | `LancarContabilUseCase` | 201 |
| SVC-CON-007 | Conciliação de conta | `POST /api/v1/con/conciliacoes` | `ConciliarContaUseCase` | 201 |

---

# 4. Detalhamento

## SVC-CON-001 — Emissão de empenho

**Processo:** PRO-CON-002

**Payload:** `exercicio` (≥ 2000), `numero`, `dotacao_id`, `valor` (> 0), `favorecido_nome`, `descricao`, `tipo`, `created_by`.

**Comportamento:** busca a dotação no repositório do DOM-ORC; se não existir, responde 404. Executa `EmitirEmpenhoUseCase`, que valida número único no exercício e saldo, debita a dotação e persiste o empenho. Persiste a dotação alterada.

**Resposta:** identificador, exercício, número, valores de empenhado, liquidado e pago, status e data de criação.

**Regras:** RN-CON-001, RN-CON-002

**Erros:** 404 dotação inexistente; 409 número duplicado ou saldo insuficiente.

---

## SVC-CON-002 — Liquidação de empenho

**Processo:** PRO-CON-003

**Payload:** `valor` (> 0), `documento`.

**Comportamento:** carrega o empenho, aplica `liquidar` (que valida saldo a liquidar e transiciona o estado), persiste o empenho, cria a liquidação já confirmada e a persiste.

**Regras:** RN-CON-020, RN-CON-021, RN-CON-022

**Erros:** 404 empenho inexistente; 409 saldo insuficiente ou estado inválido.

---

## SVC-CON-003 — Anulação de empenho

**Processo:** PRO-CON-005

**Payload:** `valor` (> 0), `documento` (usado como motivo).

**Comportamento:** carrega o empenho e a dotação; aplica `anular`; devolve o valor à dotação e persiste ambos.

**Regras:** RN-CON-002, RN-CON-004

**Erros:** 404 empenho ou dotação inexistente; 409 valor acima do saldo a liquidar.

---

## SVC-CON-004 — Pagamento de liquidação

**Processo:** PRO-CON-004

**Payload:** `liquidacao_id`, `valor` (> 0), `conta_bancaria`, `created_by`.

**Comportamento:** carrega a liquidação e exige estado CONFIRMADA; carrega o empenho; aplica `pagar`; cria o pagamento já efetivado.

**Regras:** RN-CON-030, RN-CON-031, RN-CON-032

**Erros:** 404 liquidação ou empenho inexistente; 409 liquidação não confirmada ou saldo insuficiente.

---

## SVC-CON-005 — Criação de conta contábil

**Processo:** PRO-CON-001

**Payload:** `codigo`, `nome`, `classe`, `tipo`, `natureza`, `created_by`.

**Comportamento:** valida preenchimento de código e nome; verifica unicidade do código; cria a conta com `aceita_lancamento` derivado do tipo.

**Regras:** RN-CON-010

**Erros:** 409 código duplicado ou campos obrigatórios ausentes.

---

## SVC-CON-006 — Lançamento contábil

**Processo:** PRO-CON-007

**Payload:** `exercicio` (≥ 2000), `historico`, `partidas` (≥ 2), `origem`, `origem_id`, `created_by`.

**Comportamento:** para cada partida, carrega a conta e verifica se pode receber lançamento; monta o lançamento e aplica `lancar`, que exige balanço.

**Regras:** RN-CON-011, RN-CON-012, RN-CON-040

**Erros:** 409 conta inexistente, conta que não aceita lançamento ou lançamento desequilibrado.

---

## SVC-CON-007 — Conciliação de conta

**Processo:** PRO-CON-009

**Payload:** `conta_id`, `codigo_conta`, `ano` (≥ 2000), `mes` (1–12), `saldo_contabil`, `saldo_extrato`, `justificativa`, `created_by`.

**Comportamento:** cria a conciliação e tenta marcar como conciliada; havendo divergência e justificativa informada, marca como divergente; sem justificativa, propaga o erro.

**Regras:** RN-CON-050

**Erros:** 409 divergência sem justificativa.

---

# 5. Serviços Planejados

| Identificador | Serviço | Finalidade | Origem do compromisso |
| --- | --- | --- | --- |
| SVC-CON-008 | Consulta de empenhos | Listar e filtrar a execução da despesa | CAP-CON-007 |
| SVC-CON-009 | Consulta de saldos por conta | Posicionar saldo contábil por conta | CAP-CON-007 |
| SVC-CON-010 | Estorno de lançamento | Estornar lançamento lançado | M-03 |

---

# 6. Lacunas Identificadas

| Lacuna | Serviços afetados | Achado |
| --- | --- | --- |
| Nenhum serviço registrado na aplicação | SVC-CON-001 a SVC-CON-007 | C-01 |
| Codificação de erro indiferenciada (tudo 409) | todos | A-06 |
| Sem paginação nem filtro | SVC-CON-001 a SVC-CON-007 | B-05 |
| Serviços de consulta inexistentes | SVC-CON-008, SVC-CON-009 | B-05 |
| Tag `Contabilidade Pública` ausente do OpenAPI | todos | C-01 |

---

# 7. Observação sobre a Contrato de Erro

Os sete endpoints capturam `DomConDomainError` e respondem **409** em qualquer falha
de regra. O contrato correto distingue:

| Situação | Código atual | Código correto |
| --- | --- | --- |
| Recurso inexistente | 409 | 404 |
| Regra violada / duplicidade | 409 | 409 |
| Saldo insuficiente | 409 | 422 |
| Payload inválido | 422 | 422 |


---

Este artefato consolida os serviços expostos pelo domínio de Contabilidade Pública,
relacionando cada serviço ao processo que executa, ao caso de uso correspondente, ao
endpoint que o disponibiliza e às regras aplicadas.

A implementação atual define sete serviços, todos sob o prefixo `/api/v1/con` e todos
com a tag `Contabilidade Pública`. **Nenhum deles está registrado na aplicação** — ver
achado C-01 da auditoria.

---

# 2. Princípios

* Um serviço é a unidade publicamente addressável do domínio.
* Cada serviço corresponde a um caso de uso da camada de aplicação.
* Serviços são síncronos; integrações com outros domínios ocorrem dentro do caso de uso.
* O serviço não decide regra de negócio: ele delega ao caso de uso.

---

# 3. Serviços Identificados

| Identificador | Serviço | Método e caminho | Caso de uso | Estado HTTP |
| --- | --- | --- | --- | --- |
| SVC-CON-001 | Emissão de empenho | `POST /api/v1/con/empenhos` | `EmitirEmpenhoUseCase` | 201 |
| SVC-CON-002 | Liquidação de empenho | `POST /api/v1/con/empenhos/{empenho_id}/liquidar` | `LiquidarEmpenhoUseCase` | 200 |
| SVC-CON-003 | Anulação de empenho | `POST /api/v1/con/empenhos/{empenho_id}/anular` | `AnularEmpenhoUseCase` | 200 |
| SVC-CON-004 | Pagamento de liquidação | `POST /api/v1/con/pagamentos` | `PagarLiquidacaoUseCase` | 201 |
| SVC-CON-005 | Criação de conta contábil | `POST /api/v1/con/contas` | `CriarContaUseCase` | 201 |
| SVC-CON-006 | Lançamento contábil | `POST /api/v1/con/lancamentos` | `LancarContabilUseCase` | 201 |
| SVC-CON-007 | Conciliação de conta | `POST /api/v1/con/conciliacoes` | `ConciliarContaUseCase` | 201 |

---

# 4. Detalhamento

## SVC-CON-001 — Emissão de empenho

**Processo:** PRO-CON-002

**Payload:** `exercicio` (≥ 2000), `numero`, `dotacao_id`, `valor` (> 0), `favorecido_nome`, `descricao`, `tipo`, `created_by`.

**Comportamento:** busca a dotação no repositório do DOM-ORC; se não existir, responde 404. Executa `EmitirEmpenhoUseCase`, que valida número único no exercício e saldo, debita a dotação e persiste o empenho. Persiste a dotação alterada.

**Resposta:** identificador, exercício, número, valores de empenhado, liquidado e pago, status e data de criação.

**Regras:** RN-CON-001, RN-CON-002

**Erros:** 404 dotação inexistente; 409 número duplicado ou saldo insuficiente.

---

## SVC-CON-002 — Liquidação de empenho

**Processo:** PRO-CON-003

**Payload:** `valor` (> 0), `documento`.

**Comportamento:** carrega o empenho, aplica `liquidar` (que valida saldo a liquidar e transiciona o estado), persiste o empenho, cria a liquidação já confirmada e a persiste.

**Regras:** RN-CON-020, RN-CON-021, RN-CON-022

**Erros:** 404 empenho inexistente; 409 saldo insuficiente ou estado inválido.

---

## SVC-CON-003 — Anulação de empenho

**Processo:** PRO-CON-005

**Payload:** `valor` (> 0), `documento` (usado como motivo).

**Comportamento:** carrega o empenho e a dotação; aplica `anular`; devolve o valor à dotação e persiste ambos.

**Regras:** RN-CON-002, RN-CON-004

**Erros:** 404 empenho ou dotação inexistente; 409 valor acima do saldo a liquidar.

---

## SVC-CON-004 — Pagamento de liquidação

**Processo:** PRO-CON-004

**Payload:** `liquidacao_id`, `valor` (> 0), `conta_bancaria`, `created_by`.

**Comportamento:** carrega a liquidação e exige estado CONFIRMADA; carrega o empenho; aplica `pagar`; cria o pagamento já efetivado.

**Regras:** RN-CON-030, RN-CON-031, RN-CON-032

**Erros:** 404 liquidação ou empenho inexistente; 409 liquidação não confirmada ou saldo insuficiente.

---

## SVC-CON-005 — Criação de conta contábil

**Processo:** PRO-CON-001

**Payload:** `codigo`, `nome`, `classe`, `tipo`, `natureza`, `created_by`.

**Comportamento:** valida preenchimento de código e nome; verifica unicidade do código; cria a conta com `aceita_lancamento` derivado do tipo.

**Regras:** RN-CON-010

**Erros:** 409 código duplicado ou campos obrigatórios ausentes.

---

## SVC-CON-006 — Lançamento contábil

**Processo:** PRO-CON-007

**Payload:** `exercicio` (≥ 2000), `historico`, `partidas` (≥ 2), `origem`, `origem_id`, `created_by`.

**Comportamento:** para cada partida, carrega a conta e verifica se pode receber lançamento; monta o lançamento e aplica `lancar`, que exige balanço.

**Regras:** RN-CON-011, RN-CON-012, RN-CON-040

**Erros:** 409 conta inexistente, conta que não aceita lançamento ou lançamento desequilibrado.

---

## SVC-CON-007 — Conciliação de conta

**Processo:** PRO-CON-009

**Payload:** `conta_id`, `codigo_conta`, `ano` (≥ 2000), `mes` (1–12), `saldo_contabil`, `saldo_extrato`, `justificativa`, `created_by`.

**Comportamento:** cria a conciliação e tenta marcar como conciliada; havendo divergência e justificativa informada, marca como divergente; sem justificativa, propaga o erro.

**Regras:** RN-CON-050

**Erros:** 409 divergência sem justificativa.

---

# 5. Serviços Planejados

| Identificador | Serviço | Finalidade | Origem do compromisso |
| --- | --- | --- | --- |
| SVC-CON-008 | Consulta de empenhos | Listar e filtrar a execução da despesa | CAP-CON-007 |
| SVC-CON-009 | Consulta de saldos por conta | Posicionar saldo contábil por conta | CAP-CON-007 |
| SVC-CON-010 | Estorno de lançamento | Estornar lançamento lançado | M-03 |

---

# 6. Lacunas Identificadas

| Lacuna | Serviços afetados | Achado |
| --- | --- | --- |
| Nenhum serviço registrado na aplicação | SVC-CON-001 a SVC-CON-007 | C-01 |
| Codificação de erro indiferenciada (tudo 409) | todos | A-06 |
| Sem paginação nem filtro | SVC-CON-001 a SVC-CON-007 | B-05 |
| Serviços de consulta inexistentes | SVC-CON-008, SVC-CON-009 | B-05 |
| Tag `Contabilidade Pública` ausente do OpenAPI | todos | C-01 |

---

# 7. Observação sobre a Contrato de Erro

Os sete endpoints capturam `DomConDomainError` e respondem **409** em qualquer falha
de regra. O contrato correto distingue:

| Situação | Código atual | Código correto |
| --- | --- | --- |
| Recurso inexistente | 409 | 404 |
| Regra violada / duplicidade | 409 | 409 |
| Saldo insuficiente | 409 | 422 |
| Payload inválido | 422 | 422 |

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 004-Mapa-de-Servicos-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
