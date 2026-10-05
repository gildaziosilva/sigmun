# 011 – Critérios de Aceitação – Contabilidade Pública

#### Critérios de Aceitação – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-011

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

Este artefato especifica os critérios de aceitação das histórias de usuário do
domínio de Contabilidade Pública, no formato *Dado / Quando / Então*, ensuring a
verificação objetiva de cada comportamento declarado.

---

# 2. Convenções

* Identificador `CA-CON-<história><sequencial>`.
* Cenário **Dado**: estado inicial conhecido. **Quando**: ação. **Então**: resultado
  esperado, incluindo o código de erro quando aplicável.
* Cenários marcados como *não implementado* correspondem a requisitos planejados.

---

# 3. Critérios de Aceitação

## CA-CON-001 — Emissão de empenho (HU-CON-001)

| ID | Dado | Quando | Então |
| --- | --- | --- | --- |
| CA-CON-001.1 | Dotação com saldo suficiente | Emeter empenho com valor válido | Empenho criado em estado EMITIDO e dotação debitada |
| CA-CON-001.2 | Número já usado no exercício | Tentar emitir | Retorna erro de regra; nenhum empenho criado |
| CA-CON-001.3 | Número não informado | Tentar emitir | Retorna erro de regra |
| CA-CON-001.4 | Valor zero ou negativo | Tentar emitir | Retorna erro de regra |
| CA-CON-001.5 | Dotação sem saldo | Tentar emitir | Retorna erro do DOM-ORC; dotação inalterada |
| CA-CON-001.6 | Dotação inexistente | Informar `dotacao_id` inválido | Retorna 404 |
| CA-CON-001.7 | Exercício válido | Informar exercício anterior a 2000 | Payload rejeitado com 422 |

---

## CA-CON-002 — Liquidação (HU-CON-002)

| ID | Dado | Quando | Então |
| --- | --- | --- | --- |
| CA-CON-002.1 | Empenho EMITIDO com saldo | Liquidar valor válido | Liquidação criada e empenho passa a LIQUIDADO |
| CA-CON-002.2 | Empenho com saldo parcial | Liquidar parte do valor | Saldo a liquidar é atualizado |
| CA-CON-002.3 | Valor acima do saldo a liquidar | Tentar liquidar | Retorna erro; valores não são alterados |
| CA-CON-002.4 | Valor zero ou negativo | Tentar liquidar | Retorna erro |
| CA-CON-002.5 | Empenho inexistente | Informar identificador inválido | Retorna erro de não encontrado |
| CA-CON-002.6 | Empenho em estado terminal | Tentar liquidar | Retorna erro de estado inválido |

---

## CA-CON-003 — Pagamento (HU-CON-003)

| ID | Dado | Quando | Então |
| --- | --- | --- | --- |
| CA-CON-003.1 | Liquidação CONFIRMADA | Pagar valor válido | Pagamento criado e efetivado |
| CA-CON-003.2 | Liquidação REGISTRADA | Tentar pagar | Retorna erro; nenhum pagamento criado |
| CA-CON-003.3 | Valor acima do saldo a pagar | Tentar pagar | Retorna erro |
| CA-CON-003.4 | Valor ou competência válido | Registrar pagamento | Número da ordem e conta bancária são gravados |
| CA-CON-003.5 | Empenho totalmente pago | Registrar último pagamento | Empenho passa a PAGO (estado terminal) |
| CA-CON-003.6 | Empenho já PAGO | Tentar cancelar | Retorna erro (RN-CON-004) |

---

## CA-CON-004 — Anulação e cancelamento (HU-CON-004)

| ID | Dado | Quando | Então |
| --- | --- | --- | --- |
| CA-CON-004.1 | Empenho com saldo a liquidar | Anular valor parcial | Valor anulado é acumulado |
| CA-CON-004.2 | Anulação integral | Anular todo o valor | Empenho passa a ANULADO e saldo retorna à dotação |
| CA-CON-004.3 | Valor acima do saldo a liquidar | Tentar anular | Retorna erro |
| CA-CON-004.4 | Empenho sem saldo a liquidar | Tentar anular | Retorna erro |
| CA-CON-004.5 | Empenho EMITIDO | Cancelar | Empenho passa a CANCELADO com motivo |
| CA-CON-004.6 | Empenho PAGO | Tentar cancelar | Retorna erro (RN-CON-004) |
| CA-CON-004.7 | Anulação sem valor líquido e sem liquidado | Concluir anulação | Estado terminal ANULADO |

---

## CA-CON-005 — Plano de contas (HU-CON-005)

| ID | Dado | Quando | Então |
| --- | --- | --- | --- |
| CA-CON-005.1 | Código inexistente | Criar conta | Conta criada com `aceita_lancamento` verdadeiro se analítica |
| CA-CON-005.2 | Código já existente | Criar conta | Retorna erro de duplicidade |
| CA-CON-005.3 | Código ou nome vazio | Criar conta | Retorna erro de obrigatoriedade |
| CA-CON-005.4 | Conta analítica | Lançar nela | Lançamento aceito |
| CA-CON-005.5 | Conta sintética | Lançar nela | Retorna erro (RN-CON-011) |
| CA-CON-005.6 | Conta desativada | Lançar nela | Retorna erro (RN-CON-012) |
| CA-CON-005.7 | Conta ativa | Desativar e reativar | Lançamento é recusado e depois aceito |

---

## CA-CON-006 — Lançamento contábil (HU-CON-006)

| ID | Dado | Quando | Então |
| --- | --- | --- | --- |
| CA-CON-006.1 | Duas partidas válidas e balanceadas | Lançar | Lançamento criado em LANCADO com totais |
| CA-CON-006.2 | Uma única partida | Tentar lançar | Retorna erro |
| CA-CON-006.3 | Débito ≠ crédito | Tentar lançar | Retorna `LancamentoDesequilibradoError` |
| CA-CON-006.4 | Conta inexistente | Lançar | Retorna erro |
| CA-CON-006.5 | Conta que não aceita lançamento | Lançar | Retorna erro |
| CA-CON-006.6 | Lançamento criado | Estornar | Estado passa a ESTORNADO |

---

## CA-CON-007 — Conciliação (HU-CON-007)

| ID | Dado | Quando | Então |
| --- | --- | --- | --- |
| CA-CON-007.1 | Saldos iguais | Conciliar | Conciliação marcada como CONCILIADA com diferença zero |
| CA-CON-007.2 | Saldos diferentes e justificativa | Conciliar | Conciliação marcada como DIVERGENTE com justificativa |
| CA-CON-007.3 | Saldos diferentes sem justificativa | Conciliar | Retorna erro |
| CA-CON-007.4 | Mês fora de 1 a 12 | Informar competência | Payload rejeitado com 422 |

---

## CA-CON-008 — Auditoria e consulta (HU-CON-008) — Não implementado

| ID | Dado | Quando | Então |
| --- | --- | --- | --- |
| CA-CON-008.1 | Execução registrada | Consultar por exercício | Retorna a execução filtrada |
| CA-CON-008.2 | Operação registrada | Auditar | Retorna autor, data e valores |
| CA-CON-008.3 | Registro íntegro | Estornar lançamento | Operação estornada mantém o lançamento original |

---

# 4. Critérios por História

| História | Critérios | Implementados | Cobertura |
| --- | --- | --- | --- |
| HU-CON-001 | 7 | 7 | 100 % |
| HU-CON-002 | 6 | 6 | 100 % |
| HU-CON-003 | 6 | 6 | 100 % |
| HU-CON-004 | 7 | 7 | 100 % |
| HU-CON-005 | 7 | 7 | 100 % |
| HU-CON-006 | 6 | 6 | 100 % |
| HU-CON-007 | 4 | 4 | 100 % |
| HU-CON-008 | 3 | 0 | 0 % |
| **Total** | **46** | **43** | **93 %** |

---

# 5. Critérios sem Teste Automatizado

| Critério | Cenário | Observação |
| --- | --- | --- |
| CA-CON-001.2 | Número duplicado no exercício | Sem teste; é também o cenário da corrida de unicidade |
| CA-CON-001.5 | Saldo insuficiente | Sem teste; depende do DOM-ORC |
| CA-CON-002.3 | Valor acima do saldo | Sem teste da exceção específica |
| CA-CON-003.2 | Liquidação não confirmada | Sem teste |
| CA-CON-003.5 | Empenho totalmente pago | Sem teste da transição para PAGO |
| CA-CON-004.5, CA-CON-004.6 | Cancelamento e recusa de cancelamento | Sem teste e sem serviço |
| CA-CON-005.5 | Conta sintética | Sem teste |
| CA-CON-006.4 | Conta inexistente | Sem teste |
| CA-CON-007.2, CA-CON-007.3 | Divergência justificada e não justificada | Sem teste da divergência |

Cobertura de critérios por teste automatizado: **6 de 46**. A meta da Onda 5 é elevar
esse número a 100 % dos critérios implementados.


---

Este artefato especifica os critérios de aceitação das histórias de usuário do
domínio de Contabilidade Pública, no formato *Dado / Quando / Então*, ensuring a
verificação objetiva de cada comportamento declarado.

---

# 2. Convenções

* Identificador `CA-CON-<história><sequencial>`.
* Cenário **Dado**: estado inicial conhecido. **Quando**: ação. **Então**: resultado
  esperado, incluindo o código de erro quando aplicável.
* Cenários marcados como *não implementado* correspondem a requisitos planejados.

---

# 3. Critérios de Aceitação

## CA-CON-001 — Emissão de empenho (HU-CON-001)

| ID | Dado | Quando | Então |
| --- | --- | --- | --- |
| CA-CON-001.1 | Dotação com saldo suficiente | Emeter empenho com valor válido | Empenho criado em estado EMITIDO e dotação debitada |
| CA-CON-001.2 | Número já usado no exercício | Tentar emitir | Retorna erro de regra; nenhum empenho criado |
| CA-CON-001.3 | Número não informado | Tentar emitir | Retorna erro de regra |
| CA-CON-001.4 | Valor zero ou negativo | Tentar emitir | Retorna erro de regra |
| CA-CON-001.5 | Dotação sem saldo | Tentar emitir | Retorna erro do DOM-ORC; dotação inalterada |
| CA-CON-001.6 | Dotação inexistente | Informar `dotacao_id` inválido | Retorna 404 |
| CA-CON-001.7 | Exercício válido | Informar exercício anterior a 2000 | Payload rejeitado com 422 |

---

## CA-CON-002 — Liquidação (HU-CON-002)

| ID | Dado | Quando | Então |
| --- | --- | --- | --- |
| CA-CON-002.1 | Empenho EMITIDO com saldo | Liquidar valor válido | Liquidação criada e empenho passa a LIQUIDADO |
| CA-CON-002.2 | Empenho com saldo parcial | Liquidar parte do valor | Saldo a liquidar é atualizado |
| CA-CON-002.3 | Valor acima do saldo a liquidar | Tentar liquidar | Retorna erro; valores não são alterados |
| CA-CON-002.4 | Valor zero ou negativo | Tentar liquidar | Retorna erro |
| CA-CON-002.5 | Empenho inexistente | Informar identificador inválido | Retorna erro de não encontrado |
| CA-CON-002.6 | Empenho em estado terminal | Tentar liquidar | Retorna erro de estado inválido |

---

## CA-CON-003 — Pagamento (HU-CON-003)

| ID | Dado | Quando | Então |
| --- | --- | --- | --- |
| CA-CON-003.1 | Liquidação CONFIRMADA | Pagar valor válido | Pagamento criado e efetivado |
| CA-CON-003.2 | Liquidação REGISTRADA | Tentar pagar | Retorna erro; nenhum pagamento criado |
| CA-CON-003.3 | Valor acima do saldo a pagar | Tentar pagar | Retorna erro |
| CA-CON-003.4 | Valor ou competência válido | Registrar pagamento | Número da ordem e conta bancária são gravados |
| CA-CON-003.5 | Empenho totalmente pago | Registrar último pagamento | Empenho passa a PAGO (estado terminal) |
| CA-CON-003.6 | Empenho já PAGO | Tentar cancelar | Retorna erro (RN-CON-004) |

---

## CA-CON-004 — Anulação e cancelamento (HU-CON-004)

| ID | Dado | Quando | Então |
| --- | --- | --- | --- |
| CA-CON-004.1 | Empenho com saldo a liquidar | Anular valor parcial | Valor anulado é acumulado |
| CA-CON-004.2 | Anulação integral | Anular todo o valor | Empenho passa a ANULADO e saldo retorna à dotação |
| CA-CON-004.3 | Valor acima do saldo a liquidar | Tentar anular | Retorna erro |
| CA-CON-004.4 | Empenho sem saldo a liquidar | Tentar anular | Retorna erro |
| CA-CON-004.5 | Empenho EMITIDO | Cancelar | Empenho passa a CANCELADO com motivo |
| CA-CON-004.6 | Empenho PAGO | Tentar cancelar | Retorna erro (RN-CON-004) |
| CA-CON-004.7 | Anulação sem valor líquido e sem liquidado | Concluir anulação | Estado terminal ANULADO |

---

## CA-CON-005 — Plano de contas (HU-CON-005)

| ID | Dado | Quando | Então |
| --- | --- | --- | --- |
| CA-CON-005.1 | Código inexistente | Criar conta | Conta criada com `aceita_lancamento` verdadeiro se analítica |
| CA-CON-005.2 | Código já existente | Criar conta | Retorna erro de duplicidade |
| CA-CON-005.3 | Código ou nome vazio | Criar conta | Retorna erro de obrigatoriedade |
| CA-CON-005.4 | Conta analítica | Lançar nela | Lançamento aceito |
| CA-CON-005.5 | Conta sintética | Lançar nela | Retorna erro (RN-CON-011) |
| CA-CON-005.6 | Conta desativada | Lançar nela | Retorna erro (RN-CON-012) |
| CA-CON-005.7 | Conta ativa | Desativar e reativar | Lançamento é recusado e depois aceito |

---

## CA-CON-006 — Lançamento contábil (HU-CON-006)

| ID | Dado | Quando | Então |
| --- | --- | --- | --- |
| CA-CON-006.1 | Duas partidas válidas e balanceadas | Lançar | Lançamento criado em LANCADO com totais |
| CA-CON-006.2 | Uma única partida | Tentar lançar | Retorna erro |
| CA-CON-006.3 | Débito ≠ crédito | Tentar lançar | Retorna `LancamentoDesequilibradoError` |
| CA-CON-006.4 | Conta inexistente | Lançar | Retorna erro |
| CA-CON-006.5 | Conta que não aceita lançamento | Lançar | Retorna erro |
| CA-CON-006.6 | Lançamento criado | Estornar | Estado passa a ESTORNADO |

---

## CA-CON-007 — Conciliação (HU-CON-007)

| ID | Dado | Quando | Então |
| --- | --- | --- | --- |
| CA-CON-007.1 | Saldos iguais | Conciliar | Conciliação marcada como CONCILIADA com diferença zero |
| CA-CON-007.2 | Saldos diferentes e justificativa | Conciliar | Conciliação marcada como DIVERGENTE com justificativa |
| CA-CON-007.3 | Saldos diferentes sem justificativa | Conciliar | Retorna erro |
| CA-CON-007.4 | Mês fora de 1 a 12 | Informar competência | Payload rejeitado com 422 |

---

## CA-CON-008 — Auditoria e consulta (HU-CON-008) — Não implementado

| ID | Dado | Quando | Então |
| --- | --- | --- | --- |
| CA-CON-008.1 | Execução registrada | Consultar por exercício | Retorna a execução filtrada |
| CA-CON-008.2 | Operação registrada | Auditar | Retorna autor, data e valores |
| CA-CON-008.3 | Registro íntegro | Estornar lançamento | Operação estornada mantém o lançamento original |

---

# 4. Critérios por História

| História | Critérios | Implementados | Cobertura |
| --- | --- | --- | --- |
| HU-CON-001 | 7 | 7 | 100 % |
| HU-CON-002 | 6 | 6 | 100 % |
| HU-CON-003 | 6 | 6 | 100 % |
| HU-CON-004 | 7 | 7 | 100 % |
| HU-CON-005 | 7 | 7 | 100 % |
| HU-CON-006 | 6 | 6 | 100 % |
| HU-CON-007 | 4 | 4 | 100 % |
| HU-CON-008 | 3 | 0 | 0 % |
| **Total** | **46** | **43** | **93 %** |

---

# 5. Critérios sem Teste Automatizado

| Critério | Cenário | Observação |
| --- | --- | --- |
| CA-CON-001.2 | Número duplicado no exercício | Sem teste; é também o cenário da corrida de unicidade |
| CA-CON-001.5 | Saldo insuficiente | Sem teste; depende do DOM-ORC |
| CA-CON-002.3 | Valor acima do saldo | Sem teste da exceção específica |
| CA-CON-003.2 | Liquidação não confirmada | Sem teste |
| CA-CON-003.5 | Empenho totalmente pago | Sem teste da transição para PAGO |
| CA-CON-004.5, CA-CON-004.6 | Cancelamento e recusa de cancelamento | Sem teste e sem serviço |
| CA-CON-005.5 | Conta sintética | Sem teste |
| CA-CON-006.4 | Conta inexistente | Sem teste |
| CA-CON-007.2, CA-CON-007.3 | Divergência justificada e não justificada | Sem teste da divergência |

Cobertura de critérios por teste automatizado: **6 de 46**. A meta da Onda 5 é elevar
esse número a 100 % dos critérios implementados.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 011-Criterios-de-Aceitacao-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
