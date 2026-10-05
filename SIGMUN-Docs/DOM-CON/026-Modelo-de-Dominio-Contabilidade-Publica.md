# 026 – Modelo de Domínio – Contabilidade Pública

#### Modelo de Domínio – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-026

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

Este artefato descreve o modelo de domínio de Contabilidade Pública: as
entidades, seus invariantes, as relações entre elas, as máquinas de estado e as
fronteiras com outros domínios.

---

# 2. Conceitos

| Conceito | Definição |
| --- | --- |
| **Dotação** | Autorização orçamentária maximized, mantida pelo DOM-ORC |
| **Empenho** | Compromisso formal de despesa contra dotação |
| **Liquidação** | Reconhecimento do direito adquirido, com documento fiscal |
| **Pagamento** | Efetivação da saída de recursos |
| **PCASP** | Plano de Contas Aplicável ao Setor Público |
| **Partida dobrada** | Registro de débito e crédito em igual valor |
| **Conciliação** | Comparação entre saldo contábil e extrato bancário |
| **Competência** | Exercício e mês a que se refere o registro |

---

# 3. Agregados

| Agregado | Raiz | Entidades internas | Invariante central |
| --- | --- | --- | --- |
| Execução da despesa | `Empenho` | `Liquidacao`, `Pagamento` | `liquidado ≤ líquido` e `pago ≤ liquidado` |
| Contabilidade analítica | `LancamentoContabil` | `Partida` | `débito = crédito` |
| Plano de contas | `ContaContabil` | — | Código único; somente analítica ativa aceita lançamento |
| Conciliação | `ConciliacaoContabil` | — | Divergência exige justificativa |

O **Empenho** é o agregado raiz do ciclo da despesa: liquidações e pagamentos são
comprovantes vinculados ao mesmo saldo, e não possessam identidade contábil própria.

---

# 4. Entidades

## 4.1 Empenho

| Atributo | Tipo | Descrição |
| --- | --- | --- |
| `id` | UUID | Identificador |
| `exercicio` | int | Exercício fiscal |
| `numero` | string | Número do empenho, único no exercício |
| `dotacao_id` | UUID | Referência ao DOM-ORC |
| `reserva_id` | UUID | Referência à reserva (DOM-ORC) |
| `favorecido_id` | UUID | Referência ao favorecido (DOM-COM) |
| `favorecido_nome` | string | Nome do favorecido |
| `tipo` | TipoEmpenho | `ordinario`, `global`, `estimativo` |
| `descricao` | string | Objeto da despesa |
| `valor_empenhado` | decimal | Valor comprometido |
| `valor_anulado` | decimal | Valor anulado acumulado |
| `valor_liquidado` | decimal | Valor liquidado acumulado |
| `valor_pago` | decimal | Valor pago acumulado |
| `status` | StatusEmpenho | Estado |
| `data_emissao` | datetime | Emissão |
| `data_anulacao` | datetime | Anulação |
| `motivo_anulacao` | string | Motivo |

**Propriedades derivadas:** `valor_liquido` = empenhado − anulado;
`saldo_a_liquidar` = líquido − liquidado; `saldo_a_pagar` = liquidado − pago.

**Comportamento:** `liquidar`, `estornar_liquidacao`, `pagar`, `anular`, `cancelar`.

## 4.2 Liquidacao

Comprova o direito adquirido. Referencia `empenho_id`, guarda `valor`,
`documento_fiscal` e `numero`. Estados: `registrada`, `confirmada`, `cancelada`.

**Comportamento:** `confirmar`, `cancelar`.

## 4.3 Pagamento

Ordem bancária. Referencia `liquidacao_id` **e** `empenho_id`, guarda `numero_ob`,
`valor` e `conta_bancaria`. Estados: `programado`, `efetivado`, `cancelado`.

**Comportamento:** `efetivar`, `cancelar`.

A referência redundante a `empenho_id` é intencional: viabiliza o estorno e o relatório
de execução sem junção com a liquidação.

## 4.4 ContaContabil

Conta do PCASP. Atributos: `codigo` (único), `nome`, `classe`, `grupo`,
`natureza_saldo`, `tipo` (`analitica` ou `sintetica`), `aceita_lancamento`, `ativa`,
`conta_pai_id`.

**Comportamento:** `pode_receber_lancamento`, `desativar`, `reativar`.

## 4.5 LancamentoContabil

Lançamento por partidas dobradas. Atributos: `exercicio`, `numero`, `data_lancamento`,
`historico`, `origem`, `origem_id`, `status`.

**Propriedades derivadas:** `total_debito`, `total_credito`, `balanceado`.

**Comportamento:** `lancar`, `estornar`.

## 4.6 Partida

Objeto de valor da partida dobrada: `conta_id`, `codigo_conta`, `tipo` (débito ou
crédito), `valor`, `historico`. **Não possui identidade nem ciclo de vida próprio** —
existe apenas dentro de um lançamento.

## 4.7 ConciliacaoContabil

Atributos: `conta_id`, `codigo_conta`, `competencia_ano`, `competencia_mes`,
`saldo_contabil`, `saldo_extrato`, `diferenca`, `status`, `justificativa`,
`data_conciliacao`.

**Comportamento:** `conciliar`, `marcar_divergente`.

---

# 5. Relações

```text
            ┌─────────────────┐
            │     Empenho     │  (raiz de agregado)
            └────────┬────────┘
                     │ 1
        ┌────────────┼────────────┐
        │ N          │ N          │ N
┌───────▼──────┐ ┌───▼─────────┐  │
│  Liquidacao  │ │  Pagamento  │  │
└───────┬──────┘ └─────┬───────┘  │
        │ 1            │ 1         │
        └──────┬───────┘           │
               │ N                 │
               │                   │
┌──────────────▼──────┐   ┌────────▼─────────┐
│     Pagamento       │   │  Dotação (ORC)   │
└─────────────────────┘   └──────────────────┘

┌─────────────────────┐        ┌──────────────────┐
│ LancamentoContabil  │ 1    *  │  ContaContabil   │
│  (raiz de agregado) ├───────►│   (PCASP)        │
└──────────┬──────────┘        └────────┬─────────┘
           │ 1                          │ 1
           │ *                          │ N
┌──────────▼──────────┐        ┌────────▼─────────┐
│      Partida        │        │ ConciliacaoContab│
│  (objeto de valor)  │        └──────────────────┘
└─────────────────────┘
```

---

# 6. Máquinas de Estado

## 6.1 Empenho

```text
[*] ──► EMITIDO ──liquidação──► LIQUIDADO ──pgto total──► PAGO
            │                       │                       │
       anulação                  estorno zera            (terminal)
            │                       │
            ▼                       ▼
        ANULADO ◄──────────────── EMITIDO
        (terminal)                   │
            │                    cancelamento
            │                       ▼
            │                   CANCELADO
            │                    (terminal)
            └── anulação integral ──┘
```

| De | Para | Condição |
| --- | --- | --- |
| — | EMITIDO | Emissão |
| EMITIDO | LIQUIDADO | Primeira liquidação |
| EMITIDO | ANULADO | Anulação integral |
| EMITIDO | CANCELADO | Cancelamento |
| LIQUIDADO | PAGO | Liquidação e pagamento totais |
| LIQUIDADO | EMITIDO | Estorno zera o valor liquidado |
| LIQUIDADO | CANCELADO | Cancelamento |

**Terminais:** PAGO, ANULADO, CANCELADO.

## 6.2 Liquidação

```text
[*] ──► REGISTRADA ──confirmar──► CONFIRMADA (terminal)
            │
        cancelar
            ▼
      CANCELADA (terminal)
```

## 6.3 Pagamento

```text
[*] ──► PROGRAMADO ──efetivar──► EFETIVADO (terminal)
            │
        cancelar
            ▼
      CANCELADO (terminal)
```

## 6.4 Lançamento Contábil

```text
[*] ──► RASCUNHO ──lançar (balanceado)──► LANCADO ──estornar──► ESTORNADO
                                                                        (terminal)
```

## 6.5 Conciliação

```text
[*] ──► ABERTA ──diferença zero──► CONCILIADA
            │
        diferença ≠ zero
            ▼
      DIVERGENTE ──ajuste──► CONCILIADA
```

---

# 7. Invariantes

| # | Invariante | Regra |
| --- | --- | --- |
| 1 | O valor liquidado nunca excede o valor líquido | RN-CON-003 |
| 2 | O valor pago nunca excede o valor liquidado | RN-CON-031 |
| 3 | O saldo devolve à dotação acompanha o valor anulado | RN-CON-002 |
| 4 | O total de débito iguala o total de crédito | RN-CON-050 |
| 5 | Somente conta analítica e ativa recebe lançamento | RN-CON-011, RN-CON-012 |
| 6 | O número do empenho é único no exercício | RN-CON-001 |
| 7 | Somente liquidação confirmada origina pagamento | RN-CON-030 |
| 8 | Estados terminais não sofrem transição | RN-CON-004, 022, 032 |
| 9 | Divergência de conciliação exige justificativa | RN-CON-061 |
| 10 | O código da conta é único no plano | RN-CON-010 |

---

# 8. Fronteiras

| Fronteira | Responsabilidade |
| --- | --- |
| DOM-CON → DOM-ORC | O saldo da dotação é mantido pelo DOM-ORC |
| DOM-ORC → DOM-CON | Fornece a dotação e o saldo disponível |
| DOM-CON → DOM-GDO | Mantém o documento fiscal e o comprovante |
| DOM-COM → DOM-CON | Fornece a identificação do favorecido |
| DOM-CON → Identidade | Autentica e autoriza a operação |

**Regras de fronteira:**

* DOM-CON **não duplica** cadastros: referencia identificadores de dotação, reserva,
  favorecido e documento.
* DOM-CON **não altera** saldo orçamentário diretamente: solicita a operação ao
  DOM-ORC.
* DOM-CON **não gerencia** documentos: apenas os referencia.

---

# 9. Elementos Externos

| Elemento | Domínio | Relação |
| --- | --- | --- |
| Dotação | DOM-ORC | Autoriza o empenho e detém o saldo |
| Reserva | DOM-ORC | Recurso reservado da dotação |
| Favornecido | DOM-COM | Recebe o pagamento |
| Conta bancária | DOM-FRO | Credita o pagamento |
| Documento fiscal | DOM-GDO | Comprova a liquidação |
| Usuário | DOM-IDN | Autoriza a operação |

---

# 10. Diagrama do Ciclo da Despesa

```text
   Necessidade              Autorização           Compromisso
   da despesa      ──────►  Ordotária  ──────►     Empenho
                                                    │
                       ┌────────────────────────────┘
                       ▼
                   Direito
                   adquirido        ◄── Documento fiscal
                       │                  (DOM-GDO)
                       ▼
                   Saída de
                   recursos          ◄── Ordem bancária
                       │                  (DOM-FRO)
                       ▼
                   Reciprocidade        ──► Contabilidade
                                          analítica (PCASP)
                                              │
                                              ▼
                                          Conciliação
                                          bancária
```

---

# 11. Decisões de Modelagem

| Decisão | Justificativa |
| --- | --- |
| Empenho como agregado raiz | Saldos acumulados em um único registro evitam consulta agregada |
| Saldos desnormalizados | Leitura direta do posicionamento da execução |
| Partida como objeto de valor | Não possui identidade; existe apenas dentro do lançamento |
| Partidas em JSON | Simplicidade de implementação; **em contrapartida, sem integridade referencial** |
| Referência redundante ao empenho no pagamento | Viabiliza estorno e relatório sem junção |
| Datas ausentes na persistência | **Lacuna** — impede reconstituir a linha do tempo |
| Sem chave estrangeira para o DOM-ORC | Fronteira entre domínios sem acoplamento físico; **com risco de órfãos** |

---

# 12. Relação com os Diagramas PlantUML

| Diagrama | Conteúdo |
| --- | --- |
| `000-Visao-Arquitetural.puml` | Componentes e infraestrutura |
| `001-Modelo-de-Dominio.puml` | Entidades, relações e cardinalidades |
| `002-Processos.puml` | Ciclo da execução da despesa |
| `003-Maquina-de-Estados.puml` | Estados de empenho, liquidação, pagamento, lançamento e conciliação |
| `004-Integracoes.puml` | Relações com os demais domínios |
| `005-Persistencia.puml` | Tabelas, colunas e restrições |

---

# 13. Lacunas do Modelo

| Lacuna | Consequência | Achado |
| --- | --- | --- |
| Dez campos sem persistência | Perda de datas e do vínculo com o favorecido | A-01 |
| Partidas em JSON | Sem integridade referencial com as contas | M-02 |
| Sem eventos de domínio | Sem integração assíncrona nem auditoria por evento | M-01 |
| Sem valor monetário próprio | Arredondamento em ponto flutuante | RNF-CON-017 |
| Lançamento não automático | Reflexo contábil depende de intervenção manual | M-03 |
| Sem unicidade no banco | Condição de corrida na numeração | A-02 |


---

Este artefato descreve o modelo de domínio de Contabilidade Pública: as
entidades, seus invariantes, as relações entre elas, as máquinas de estado e as
fronteiras com outros domínios.

---

# 2. Conceitos

| Conceito | Definição |
| --- | --- |
| **Dotação** | Autorização orçamentária maximized, mantida pelo DOM-ORC |
| **Empenho** | Compromisso formal de despesa contra dotação |
| **Liquidação** | Reconhecimento do direito adquirido, com documento fiscal |
| **Pagamento** | Efetivação da saída de recursos |
| **PCASP** | Plano de Contas Aplicável ao Setor Público |
| **Partida dobrada** | Registro de débito e crédito em igual valor |
| **Conciliação** | Comparação entre saldo contábil e extrato bancário |
| **Competência** | Exercício e mês a que se refere o registro |

---

# 3. Agregados

| Agregado | Raiz | Entidades internas | Invariante central |
| --- | --- | --- | --- |
| Execução da despesa | `Empenho` | `Liquidacao`, `Pagamento` | `liquidado ≤ líquido` e `pago ≤ liquidado` |
| Contabilidade analítica | `LancamentoContabil` | `Partida` | `débito = crédito` |
| Plano de contas | `ContaContabil` | — | Código único; somente analítica ativa aceita lançamento |
| Conciliação | `ConciliacaoContabil` | — | Divergência exige justificativa |

O **Empenho** é o agregado raiz do ciclo da despesa: liquidações e pagamentos são
comprovantes vinculados ao mesmo saldo, e não possessam identidade contábil própria.

---

# 4. Entidades

## 4.1 Empenho

| Atributo | Tipo | Descrição |
| --- | --- | --- |
| `id` | UUID | Identificador |
| `exercicio` | int | Exercício fiscal |
| `numero` | string | Número do empenho, único no exercício |
| `dotacao_id` | UUID | Referência ao DOM-ORC |
| `reserva_id` | UUID | Referência à reserva (DOM-ORC) |
| `favorecido_id` | UUID | Referência ao favorecido (DOM-COM) |
| `favorecido_nome` | string | Nome do favorecido |
| `tipo` | TipoEmpenho | `ordinario`, `global`, `estimativo` |
| `descricao` | string | Objeto da despesa |
| `valor_empenhado` | decimal | Valor comprometido |
| `valor_anulado` | decimal | Valor anulado acumulado |
| `valor_liquidado` | decimal | Valor liquidado acumulado |
| `valor_pago` | decimal | Valor pago acumulado |
| `status` | StatusEmpenho | Estado |
| `data_emissao` | datetime | Emissão |
| `data_anulacao` | datetime | Anulação |
| `motivo_anulacao` | string | Motivo |

**Propriedades derivadas:** `valor_liquido` = empenhado − anulado;
`saldo_a_liquidar` = líquido − liquidado; `saldo_a_pagar` = liquidado − pago.

**Comportamento:** `liquidar`, `estornar_liquidacao`, `pagar`, `anular`, `cancelar`.

## 4.2 Liquidacao

Comprova o direito adquirido. Referencia `empenho_id`, guarda `valor`,
`documento_fiscal` e `numero`. Estados: `registrada`, `confirmada`, `cancelada`.

**Comportamento:** `confirmar`, `cancelar`.

## 4.3 Pagamento

Ordem bancária. Referencia `liquidacao_id` **e** `empenho_id`, guarda `numero_ob`,
`valor` e `conta_bancaria`. Estados: `programado`, `efetivado`, `cancelado`.

**Comportamento:** `efetivar`, `cancelar`.

A referência redundante a `empenho_id` é intencional: viabiliza o estorno e o relatório
de execução sem junção com a liquidação.

## 4.4 ContaContabil

Conta do PCASP. Atributos: `codigo` (único), `nome`, `classe`, `grupo`,
`natureza_saldo`, `tipo` (`analitica` ou `sintetica`), `aceita_lancamento`, `ativa`,
`conta_pai_id`.

**Comportamento:** `pode_receber_lancamento`, `desativar`, `reativar`.

## 4.5 LancamentoContabil

Lançamento por partidas dobradas. Atributos: `exercicio`, `numero`, `data_lancamento`,
`historico`, `origem`, `origem_id`, `status`.

**Propriedades derivadas:** `total_debito`, `total_credito`, `balanceado`.

**Comportamento:** `lancar`, `estornar`.

## 4.6 Partida

Objeto de valor da partida dobrada: `conta_id`, `codigo_conta`, `tipo` (débito ou
crédito), `valor`, `historico`. **Não possui identidade nem ciclo de vida próprio** —
existe apenas dentro de um lançamento.

## 4.7 ConciliacaoContabil

Atributos: `conta_id`, `codigo_conta`, `competencia_ano`, `competencia_mes`,
`saldo_contabil`, `saldo_extrato`, `diferenca`, `status`, `justificativa`,
`data_conciliacao`.

**Comportamento:** `conciliar`, `marcar_divergente`.

---

# 5. Relações

```text
            ┌─────────────────┐
            │     Empenho     │  (raiz de agregado)
            └────────┬────────┘
                     │ 1
        ┌────────────┼────────────┐
        │ N          │ N          │ N
┌───────▼──────┐ ┌───▼─────────┐  │
│  Liquidacao  │ │  Pagamento  │  │
└───────┬──────┘ └─────┬───────┘  │
        │ 1            │ 1         │
        └──────┬───────┘           │
               │ N                 │
               │                   │
┌──────────────▼──────┐   ┌────────▼─────────┐
│     Pagamento       │   │  Dotação (ORC)   │
└─────────────────────┘   └──────────────────┘

┌─────────────────────┐        ┌──────────────────┐
│ LancamentoContabil  │ 1    *  │  ContaContabil   │
│  (raiz de agregado) ├───────►│   (PCASP)        │
└──────────┬──────────┘        └────────┬─────────┘
           │ 1                          │ 1
           │ *                          │ N
┌──────────▼──────────┐        ┌────────▼─────────┐
│      Partida        │        │ ConciliacaoContab│
│  (objeto de valor)  │        └──────────────────┘
└─────────────────────┘
```

---

# 6. Máquinas de Estado

## 6.1 Empenho

```text
[*] ──► EMITIDO ──liquidação──► LIQUIDADO ──pgto total──► PAGO
            │                       │                       │
       anulação                  estorno zera            (terminal)
            │                       │
            ▼                       ▼
        ANULADO ◄──────────────── EMITIDO
        (terminal)                   │
            │                    cancelamento
            │                       ▼
            │                   CANCELADO
            │                    (terminal)
            └── anulação integral ──┘
```

| De | Para | Condição |
| --- | --- | --- |
| — | EMITIDO | Emissão |
| EMITIDO | LIQUIDADO | Primeira liquidação |
| EMITIDO | ANULADO | Anulação integral |
| EMITIDO | CANCELADO | Cancelamento |
| LIQUIDADO | PAGO | Liquidação e pagamento totais |
| LIQUIDADO | EMITIDO | Estorno zera o valor liquidado |
| LIQUIDADO | CANCELADO | Cancelamento |

**Terminais:** PAGO, ANULADO, CANCELADO.

## 6.2 Liquidação

```text
[*] ──► REGISTRADA ──confirmar──► CONFIRMADA (terminal)
            │
        cancelar
            ▼
      CANCELADA (terminal)
```

## 6.3 Pagamento

```text
[*] ──► PROGRAMADO ──efetivar──► EFETIVADO (terminal)
            │
        cancelar
            ▼
      CANCELADO (terminal)
```

## 6.4 Lançamento Contábil

```text
[*] ──► RASCUNHO ──lançar (balanceado)──► LANCADO ──estornar──► ESTORNADO
                                                                        (terminal)
```

## 6.5 Conciliação

```text
[*] ──► ABERTA ──diferença zero──► CONCILIADA
            │
        diferença ≠ zero
            ▼
      DIVERGENTE ──ajuste──► CONCILIADA
```

---

# 7. Invariantes

| # | Invariante | Regra |
| --- | --- | --- |
| 1 | O valor liquidado nunca excede o valor líquido | RN-CON-003 |
| 2 | O valor pago nunca excede o valor liquidado | RN-CON-031 |
| 3 | O saldo devolve à dotação acompanha o valor anulado | RN-CON-002 |
| 4 | O total de débito iguala o total de crédito | RN-CON-050 |
| 5 | Somente conta analítica e ativa recebe lançamento | RN-CON-011, RN-CON-012 |
| 6 | O número do empenho é único no exercício | RN-CON-001 |
| 7 | Somente liquidação confirmada origina pagamento | RN-CON-030 |
| 8 | Estados terminais não sofrem transição | RN-CON-004, 022, 032 |
| 9 | Divergência de conciliação exige justificativa | RN-CON-061 |
| 10 | O código da conta é único no plano | RN-CON-010 |

---

# 8. Fronteiras

| Fronteira | Responsabilidade |
| --- | --- |
| DOM-CON → DOM-ORC | O saldo da dotação é mantido pelo DOM-ORC |
| DOM-ORC → DOM-CON | Fornece a dotação e o saldo disponível |
| DOM-CON → DOM-GDO | Mantém o documento fiscal e o comprovante |
| DOM-COM → DOM-CON | Fornece a identificação do favorecido |
| DOM-CON → Identidade | Autentica e autoriza a operação |

**Regras de fronteira:**

* DOM-CON **não duplica** cadastros: referencia identificadores de dotação, reserva,
  favorecido e documento.
* DOM-CON **não altera** saldo orçamentário diretamente: solicita a operação ao
  DOM-ORC.
* DOM-CON **não gerencia** documentos: apenas os referencia.

---

# 9. Elementos Externos

| Elemento | Domínio | Relação |
| --- | --- | --- |
| Dotação | DOM-ORC | Autoriza o empenho e detém o saldo |
| Reserva | DOM-ORC | Recurso reservado da dotação |
| Favornecido | DOM-COM | Recebe o pagamento |
| Conta bancária | DOM-FRO | Credita o pagamento |
| Documento fiscal | DOM-GDO | Comprova a liquidação |
| Usuário | DOM-IDN | Autoriza a operação |

---

# 10. Diagrama do Ciclo da Despesa

```text
   Necessidade              Autorização           Compromisso
   da despesa      ──────►  Ordotária  ──────►     Empenho
                                                    │
                       ┌────────────────────────────┘
                       ▼
                   Direito
                   adquirido        ◄── Documento fiscal
                       │                  (DOM-GDO)
                       ▼
                   Saída de
                   recursos          ◄── Ordem bancária
                       │                  (DOM-FRO)
                       ▼
                   Reciprocidade        ──► Contabilidade
                                          analítica (PCASP)
                                              │
                                              ▼
                                          Conciliação
                                          bancária
```

---

# 11. Decisões de Modelagem

| Decisão | Justificativa |
| --- | --- |
| Empenho como agregado raiz | Saldos acumulados em um único registro evitam consulta agregada |
| Saldos desnormalizados | Leitura direta do posicionamento da execução |
| Partida como objeto de valor | Não possui identidade; existe apenas dentro do lançamento |
| Partidas em JSON | Simplicidade de implementação; **em contrapartida, sem integridade referencial** |
| Referência redundante ao empenho no pagamento | Viabiliza estorno e relatório sem junção |
| Datas ausentes na persistência | **Lacuna** — impede reconstituir a linha do tempo |
| Sem chave estrangeira para o DOM-ORC | Fronteira entre domínios sem acoplamento físico; **com risco de órfãos** |

---

# 12. Relação com os Diagramas PlantUML

| Diagrama | Conteúdo |
| --- | --- |
| `000-Visao-Arquitetural.puml` | Componentes e infraestrutura |
| `001-Modelo-de-Dominio.puml` | Entidades, relações e cardinalidades |
| `002-Processos.puml` | Ciclo da execução da despesa |
| `003-Maquina-de-Estados.puml` | Estados de empenho, liquidação, pagamento, lançamento e conciliação |
| `004-Integracoes.puml` | Relações com os demais domínios |
| `005-Persistencia.puml` | Tabelas, colunas e restrições |

---

# 13. Lacunas do Modelo

| Lacuna | Consequência | Achado |
| --- | --- | --- |
| Dez campos sem persistência | Perda de datas e do vínculo com o favorecido | A-01 |
| Partidas em JSON | Sem integridade referencial com as contas | M-02 |
| Sem eventos de domínio | Sem integração assíncrona nem auditoria por evento | M-01 |
| Sem valor monetário próprio | Arredondamento em ponto flutuante | RNF-CON-017 |
| Lançamento não automático | Reflexo contábil depende de intervenção manual | M-03 |
| Sem unicidade no banco | Condição de corrida na numeração | A-02 |

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 026-Modelo-de-Dominio-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
