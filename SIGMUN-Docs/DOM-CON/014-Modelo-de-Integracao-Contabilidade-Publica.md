# 014 – Modelo de Integração – Contabilidade Pública

#### Modelo de Integração – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-014

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

Este artefato descreve o modelo de integração do domínio de Contabilidade Pública,
identificando os domínios com os quais há relação de dados, os serviços consumidos ou
publicados e as fronteiras de responsabilidade.

---

# 2. Princípios

* Cada domínio é dono dos seus dados; DOM-CON referencia identificadores sem duplicar
  cadastros.
* Integrações são síncronas quando a resposta é necessária à transação; assíncronas
  quando há apenas notificação.
* Falha em integração não pode deixar o domínio em estado inconsistente.
* A fronteira entre DOM-ORC e DOM-CON é a mais sensível do domínio: ela altera saldo
  orçamentário real.

---

# 3. Integrações Identificadas

| Identificador | Domínio | Direção | Tipo | Dados | Criticidade |
| --- | --- | --- | --- | --- | --- |
| INT-CON-001 | DOM-ORC — Orçamento Público | DOM-ORC → DOM-CON | Síncrona | Dotação, saldo disponível | **Crítica** |
| INT-CON-002 | DOM-GDO — Gestão Documental | DOM-CON → DOM-GDO | Síncrona | Documento fiscal, comprovante | Alta |
| INT-CON-003 | DOM-IDN — Identidade e Acesso | DOM-IDN → DOM-CON | Síncrona | Autenticação e autorização | Alta |
| INT-CON-004 | Auditoria | DOM-CON → Auditoria | Assíncrona | Eventos de operação contábil | Alta |
| INT-CON-005 | Notificações | DOM-CON → Notificações | Assíncrona | Avisos de pendência | Média |
| INT-CON-006 | DOM-COM — Compras e Contratações | DOM-COM → DOM-CON | Consulta | Obrigação contratada | Média |
| INT-CON-007 | DOM-FRO — Gestão de Frota | DOM-FRO → DOM-CON | Consulta | Conta bancária de crédito | Média |
| INT-CON-008 | DOM-TRI — Administração Tributária | DOM-TRI → DOM-CON | Consulta | Créditos tributários | Baixa |
| INT-CON-009 | Portal da Transparência | DOM-CON → Portal | Assíncrona | Execução da despesa | Média |

---

# 4. Detalhamento

## INT-CON-001 — DOM-ORC (Orçamento Público)

**Direção:** DOM-ORC fornece dados; DOM-CON consome e devolve o efeito no saldo.

**Operações utilizadas:**

| Operação | Momento | Efeito |
| --- | --- | --- |
| Buscar dotação por identificador | Antes de emitir | Valida existência |
| `empenhar_direto(valor)` | Na emissão | Debita o saldo da dotação |
| `anular_empenho(valor)` | Na anulação | Devolve saldo à dotação |

**Contrato:** DOM-CON **não duplica** o cadastro orçamentário; referencia `dotacao_id`
e `reserva_id`.

**Estado atual — problema crítico:** os routers de DOM-ORC **também não estão
registrados** na aplicação. Não existe dotação alcançável, portanto a integração é
inexistente na prática (achado C-02).

**Risco:** a alteração do saldo orçamentário e a gravação do empenho **não compartilham
a mesma unidade transacional**. Uma falha após o débito deixa a dotação comprometida
sem contrapartida contábil.

**Dependência de dados:** `con.empenhos.dotacao_id` referencia `orc.dotacoes.id`
**sem chave estrangeira** (achado A-03).

---

## INT-CON-002 — DOM-GDO (Gestão Documental)

**Direção:** DOM-CON referencia documentos mantidos no DOM-GDO.

**Uso:** documento fiscal que comprova a liquidação; comprovante de pagamento.

**Contrato:** DOM-CON guarda apenas a **referência** e, no caso do documento fiscal,
o identificador do documento — não o arquivo.

**Estado atual:** a integração **não está implementada**. O campo `documento_fiscal`
recebe texto livre, sem validação de existência no DOM-GDO.

---

## INT-CON-003 — DOM-IDN (Identidade e Acesso)

**Direção:** DOM-IDN autentica e autoriza.

**Uso:** garantir que apenas servidores autorizados realizem operações contábeis com
efeito financeiro.

**Estado atual:** o middleware existe na aplicação, mas **não há evidência de aplicação
de permissão por operação contábil** — os endpoints do domínio não verificam perfil
(achado RNF-CON-007).

**Requisito de segregação:** o perfil do contador que emite não deve permitir
cancelar empenho nem efetuar o pagamento correspondente sem o ordenador
correspondente.

---

## INT-CON-004 — Auditoria

**Direção:** DOM-CON publica eventos de operação contábil.

**Estado atual:** **não implementada**. Não existem eventos de domínio no módulo; os
campos `created_by` existem mas não são preenchidos (achado M-04).

**Eventos necessários:** `EmpenhoEmitido`, `EmpenhoLiquidado`, `EmpenhoPago`,
`EmpenhoAnulado`, `EmpenhoCancelado`, `LancamentoRegistrado`, `LancamentoEstornado`,
`ConciliacaoDivergente`.

---

## INT-CON-005 — Notificações

**Direção:** DOM-CON notifica.

**Uso:** avisar sobre saldo insuficiente, divergência de conciliação, empenho com
prazo em risco.

**Estado atual:** planejada.

---

## INT-CON-009 — Portal da Transparência

**Direção:** DOM-CON publica dados de execução.

**Uso:** atender ao princípio da transparência da despesa pública, permitindo ao
cidadão consultar a execução.

**Estado atual:** **não implementada**. Não existe endpoint de leitura no módulo
(achado B-05, RF-CON-028).

---

# 5. Mapa de Dependências

```text
                DOM-ORC (dotação, saldo)
                       │
            authorize  │  debita/devolve saldo
                       ▼
     ┌─────────────────────────────┐
     │          DOM-CON            │
     │  empenho → liquidação → pagamento
     │  contas → lançamentos → conciliação
     └─────────────────────────────┘
          │        │        │        │
          ▼        ▼        ▼        ▼
      DOM-GDO  DOM-IDN  Auditoria  Transparência
     (documentos) (acesso) (eventos)  (execução)
```

---

# 6. Matriz de Integração

| Domínio | Compartilha dados | Consome serviço | Publica evento | Estado |
| --- | --- | --- | --- | --- |
| DOM-ORC | Identificadores de dotação e reserva | Consulta e manipulação de saldo | Não | Código existe, não exposto |
| DOM-GDO | Identificador de documento | Armazenamento | Não | Planejado |
| DOM-IDN | — | Autenticação e autorização | Não | Parcial |
| Auditoria | — | — | Sim | Planejado |
| Notificações | — | — | Aviso | Planejado |
| DOM-COM | Identificador do favorecido | Consulta de obrigação | Não | Planejado |
| DOM-FRO | Identificador da conta bancária | Consulta de conta | Não | Texto livre |
| DOM-TRI | Identificador do contribuinte | Consulta de crédito | Não | Planejado |
| Transparência | — | — | Execução | Planejado |

---

# 7. Riscos de Integração

| Risco | Integração | Probabilidade | Impacto | Mitigação |
| --- | --- | --- | --- | --- |
| Débito orçamentário sem contrapartida contábil | INT-CON-001 | Média | **Alto** | Teste de falha transacional (Onda 3, tarefa 3.3) |
| Empenho órfão por dotação inexistente | INT-CON-001 | Média | Alto | Chave estrangeira (Onda 1, tarefa 1.5) |
| Documento fiscal inexistente | INT-CON-002 | Alta | Médio | Validar referência no DOM-GDO |
| Operação sem autorização por perfil | INT-CON-003 | Média | **Alto** | Implementar segregação de funções |
| Operação sem rastro de auditoria | INT-CON-004 | **Certa** | **Alto** | Onda 4, tarefa 4.5 |
| Perda de linha do tempo do ciclo | INT-CON-001/002 | **Certa** | Alto | Migration das 10 colunas (Onda 1) |

---

# 8. Lacunas Identificadas

| Lacuna | Integrações afetadas | Achado |
| --- | --- | --- |
| DOM-ORC não exposto | INT-CON-001 | C-02 |
| Sem chave estrangeira para a dotação | INT-CON-001 | A-03 |
| Transação não atômica entre domínios | INT-CON-001 | RNF-CON-005 |
| DOM-GDO não integrado | INT-CON-002 | — |
| Sem eventos de domínio | INT-CON-004, INT-CON-005 | M-01 |
| Autorização por perfil não aplicada | INT-CON-003 | RNF-CON-008 |
| Transparência não publicada | INT-CON-009 | B-05 |


---

Este artefato descreve o modelo de integração do domínio de Contabilidade Pública,
identificando os domínios com os quais há relação de dados, os serviços consumidos ou
publicados e as fronteiras de responsabilidade.

---

# 2. Princípios

* Cada domínio é dono dos seus dados; DOM-CON referencia identificadores sem duplicar
  cadastros.
* Integrações são síncronas quando a resposta é necessária à transação; assíncronas
  quando há apenas notificação.
* Falha em integração não pode deixar o domínio em estado inconsistente.
* A fronteira entre DOM-ORC e DOM-CON é a mais sensível do domínio: ela altera saldo
  orçamentário real.

---

# 3. Integrações Identificadas

| Identificador | Domínio | Direção | Tipo | Dados | Criticidade |
| --- | --- | --- | --- | --- | --- |
| INT-CON-001 | DOM-ORC — Orçamento Público | DOM-ORC → DOM-CON | Síncrona | Dotação, saldo disponível | **Crítica** |
| INT-CON-002 | DOM-GDO — Gestão Documental | DOM-CON → DOM-GDO | Síncrona | Documento fiscal, comprovante | Alta |
| INT-CON-003 | DOM-IDN — Identidade e Acesso | DOM-IDN → DOM-CON | Síncrona | Autenticação e autorização | Alta |
| INT-CON-004 | Auditoria | DOM-CON → Auditoria | Assíncrona | Eventos de operação contábil | Alta |
| INT-CON-005 | Notificações | DOM-CON → Notificações | Assíncrona | Avisos de pendência | Média |
| INT-CON-006 | DOM-COM — Compras e Contratações | DOM-COM → DOM-CON | Consulta | Obrigação contratada | Média |
| INT-CON-007 | DOM-FRO — Gestão de Frota | DOM-FRO → DOM-CON | Consulta | Conta bancária de crédito | Média |
| INT-CON-008 | DOM-TRI — Administração Tributária | DOM-TRI → DOM-CON | Consulta | Créditos tributários | Baixa |
| INT-CON-009 | Portal da Transparência | DOM-CON → Portal | Assíncrona | Execução da despesa | Média |

---

# 4. Detalhamento

## INT-CON-001 — DOM-ORC (Orçamento Público)

**Direção:** DOM-ORC fornece dados; DOM-CON consome e devolve o efeito no saldo.

**Operações utilizadas:**

| Operação | Momento | Efeito |
| --- | --- | --- |
| Buscar dotação por identificador | Antes de emitir | Valida existência |
| `empenhar_direto(valor)` | Na emissão | Debita o saldo da dotação |
| `anular_empenho(valor)` | Na anulação | Devolve saldo à dotação |

**Contrato:** DOM-CON **não duplica** o cadastro orçamentário; referencia `dotacao_id`
e `reserva_id`.

**Estado atual — problema crítico:** os routers de DOM-ORC **também não estão
registrados** na aplicação. Não existe dotação alcançável, portanto a integração é
inexistente na prática (achado C-02).

**Risco:** a alteração do saldo orçamentário e a gravação do empenho **não compartilham
a mesma unidade transacional**. Uma falha após o débito deixa a dotação comprometida
sem contrapartida contábil.

**Dependência de dados:** `con.empenhos.dotacao_id` referencia `orc.dotacoes.id`
**sem chave estrangeira** (achado A-03).

---

## INT-CON-002 — DOM-GDO (Gestão Documental)

**Direção:** DOM-CON referencia documentos mantidos no DOM-GDO.

**Uso:** documento fiscal que comprova a liquidação; comprovante de pagamento.

**Contrato:** DOM-CON guarda apenas a **referência** e, no caso do documento fiscal,
o identificador do documento — não o arquivo.

**Estado atual:** a integração **não está implementada**. O campo `documento_fiscal`
recebe texto livre, sem validação de existência no DOM-GDO.

---

## INT-CON-003 — DOM-IDN (Identidade e Acesso)

**Direção:** DOM-IDN autentica e autoriza.

**Uso:** garantir que apenas servidores autorizados realizem operações contábeis com
efeito financeiro.

**Estado atual:** o middleware existe na aplicação, mas **não há evidência de aplicação
de permissão por operação contábil** — os endpoints do domínio não verificam perfil
(achado RNF-CON-007).

**Requisito de segregação:** o perfil do contador que emite não deve permitir
cancelar empenho nem efetuar o pagamento correspondente sem o ordenador
correspondente.

---

## INT-CON-004 — Auditoria

**Direção:** DOM-CON publica eventos de operação contábil.

**Estado atual:** **não implementada**. Não existem eventos de domínio no módulo; os
campos `created_by` existem mas não são preenchidos (achado M-04).

**Eventos necessários:** `EmpenhoEmitido`, `EmpenhoLiquidado`, `EmpenhoPago`,
`EmpenhoAnulado`, `EmpenhoCancelado`, `LancamentoRegistrado`, `LancamentoEstornado`,
`ConciliacaoDivergente`.

---

## INT-CON-005 — Notificações

**Direção:** DOM-CON notifica.

**Uso:** avisar sobre saldo insuficiente, divergência de conciliação, empenho com
prazo em risco.

**Estado atual:** planejada.

---

## INT-CON-009 — Portal da Transparência

**Direção:** DOM-CON publica dados de execução.

**Uso:** atender ao princípio da transparência da despesa pública, permitindo ao
cidadão consultar a execução.

**Estado atual:** **não implementada**. Não existe endpoint de leitura no módulo
(achado B-05, RF-CON-028).

---

# 5. Mapa de Dependências

```text
                DOM-ORC (dotação, saldo)
                       │
            authorize  │  debita/devolve saldo
                       ▼
     ┌─────────────────────────────┐
     │          DOM-CON            │
     │  empenho → liquidação → pagamento
     │  contas → lançamentos → conciliação
     └─────────────────────────────┘
          │        │        │        │
          ▼        ▼        ▼        ▼
      DOM-GDO  DOM-IDN  Auditoria  Transparência
     (documentos) (acesso) (eventos)  (execução)
```

---

# 6. Matriz de Integração

| Domínio | Compartilha dados | Consome serviço | Publica evento | Estado |
| --- | --- | --- | --- | --- |
| DOM-ORC | Identificadores de dotação e reserva | Consulta e manipulação de saldo | Não | Código existe, não exposto |
| DOM-GDO | Identificador de documento | Armazenamento | Não | Planejado |
| DOM-IDN | — | Autenticação e autorização | Não | Parcial |
| Auditoria | — | — | Sim | Planejado |
| Notificações | — | — | Aviso | Planejado |
| DOM-COM | Identificador do favorecido | Consulta de obrigação | Não | Planejado |
| DOM-FRO | Identificador da conta bancária | Consulta de conta | Não | Texto livre |
| DOM-TRI | Identificador do contribuinte | Consulta de crédito | Não | Planejado |
| Transparência | — | — | Execução | Planejado |

---

# 7. Riscos de Integração

| Risco | Integração | Probabilidade | Impacto | Mitigação |
| --- | --- | --- | --- | --- |
| Débito orçamentário sem contrapartida contábil | INT-CON-001 | Média | **Alto** | Teste de falha transacional (Onda 3, tarefa 3.3) |
| Empenho órfão por dotação inexistente | INT-CON-001 | Média | Alto | Chave estrangeira (Onda 1, tarefa 1.5) |
| Documento fiscal inexistente | INT-CON-002 | Alta | Médio | Validar referência no DOM-GDO |
| Operação sem autorização por perfil | INT-CON-003 | Média | **Alto** | Implementar segregação de funções |
| Operação sem rastro de auditoria | INT-CON-004 | **Certa** | **Alto** | Onda 4, tarefa 4.5 |
| Perda de linha do tempo do ciclo | INT-CON-001/002 | **Certa** | Alto | Migration das 10 colunas (Onda 1) |

---

# 8. Lacunas Identificadas

| Lacuna | Integrações afetadas | Achado |
| --- | --- | --- |
| DOM-ORC não exposto | INT-CON-001 | C-02 |
| Sem chave estrangeira para a dotação | INT-CON-001 | A-03 |
| Transação não atômica entre domínios | INT-CON-001 | RNF-CON-005 |
| DOM-GDO não integrado | INT-CON-002 | — |
| Sem eventos de domínio | INT-CON-004, INT-CON-005 | M-01 |
| Autorização por perfil não aplicada | INT-CON-003 | RNF-CON-008 |
| Transparência não publicada | INT-CON-009 | B-05 |

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 014-Modelo-de-Integracao-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
