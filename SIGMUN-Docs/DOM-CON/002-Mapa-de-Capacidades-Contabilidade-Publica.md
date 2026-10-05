# 002 – Mapa de Capacidades – Contabilidade Pública

#### Mapa de Capacidades – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-002

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

Este artefato consolida as capacidades de negócio oferecidas pelo domínio de
Contabilidade Pública, relacionando cada capacidade aos processos que a executam,
às regras de negócio que a governam e aos atores que a exercem.

---

# 2. Princípios

* Uma capacidade descreve **o que** o domínio entrega, não **como** é implementado.
* Capacidades são independentes de tecnologia e de interface.
* Toda capacidade deve estar rastreada a processos, requisitos e regras.
* A coluna **Estado** indica se a capacidade está implementada no módulo
  `sigmun_con`, planejada, ou implementada porém **não exposta** na API.
* A marcação decorre da auditoria `AUDITORIA-DOM-CON-2026-09-30.md`: o módulo não
  registra seus routers em `src/main.py`, de modo que nenhuma capacidade é
  alcançável por consumidor externo.

---

# 3. Capacidades Identificadas

| Identificador | Capacidade | Descrição | Estado | Processos | Regras |
| --- | --- | --- | --- | --- | --- |
| CAP-CON-001 | Gestão do plano de contas (PCASP) | Manter o plano de contas do município segundo o PCASP, com hierarquia classe/grupo, natureza de saldo e controle de aceitabilidade de lançamento. | Implementada, não exposta | PRO-CON-001 | RN-CON-010, RN-CON-011, RN-CON-012 |
| CAP-CON-002 | Execução do empenho | Registrar o compromisso de despesa contra dotação autorizada, com numeração única por exercício e estorno, anulação e cancelamento controlados. | Implementada, não exposta | PRO-CON-002, PRO-CON-005, PRO-CON-006 | RN-CON-001, RN-CON-002, RN-CON-003, RN-CON-004 |
| CAP-CON-003 | Liquidação da despesa | Comprovar o direito adquirido sobre o empenho, com documento fiscal e controle de saldo a liquidar. | Implementada, não exposta | PRO-CON-003 | RN-CON-020, RN-CON-021, RN-CON-022 |
| CAP-CON-004 | Pagamento da despesa | Executar a ordem bancária sobre liquidação confirmada, com controle de saldo a pagar e registro da conta bancária. | Implementada, não exposta | PRO-CON-004 | RN-CON-030, RN-CON-031, RN-CON-032 |
| CAP-CON-005 | Registro de lançamentos contábeis | Registrar partidas dobradas por conta do plano, com balanço obrigatório e rastreabilidade da origem. | Implementada, não exposta | PRO-CON-007, PRO-CON-008 | RN-CON-040 |
| CAP-CON-006 | Conciliação bancária | Comparar o saldo contábil da conta com o extrato bancário na competência e justificar divergências. | Implementada, não exposta | PRO-CON-009 | RN-CON-050 |
| CAP-CON-007 | Consulta e transparência da execução | Disponibilizar a execução da despesa para controle interno, externalização e controle social. | Planejada | PRO-CON-010 | RN-CON-001 |
| CAP-CON-008 | Trilha de auditoria contábil | Preservar autoria, data e valor de cada operação com efeito contábil para fins de responsabilização. | Parcial | PRO-CON-011 | RN-CON-060 |

---

# 4. Detalhamento

## CAP-CON-001 — Gestão do plano de contas (PCASP)

**Descrição:** Manter o plano de contas do município segundo o PCASP, com hierarquia classe/grupo, natureza de saldo e controle de aceitabilidade de lançamento.

**Estado:** Implementada, não exposta

**Processos:** PRO-CON-001

**Regras aplicáveis:** RN-CON-010, RN-CON-011, RN-CON-012

**Atores:** AT-CON-003

**Entidades:** `ContaContabil`

---

## CAP-CON-002 — Execução do empenho

**Descrição:** Registrar o compromisso de despesa contra dotação autorizada, com numeração única por exercício e estorno, anulação e cancelamento controlados.

**Estado:** Implementada, não exposta

**Processos:** PRO-CON-002, PRO-CON-005, PRO-CON-006

**Regras aplicáveis:** RN-CON-001, RN-CON-002, RN-CON-003, RN-CON-004

**Atores:** AT-CON-001, AT-CON-002, AT-CON-008

**Entidades:** `Empenho`, `Liquidacao`, `Pagamento`

---

## CAP-CON-003 — Liquidação da despesa

**Descrição:** Comprovar o direito adquirido sobre o empenho, com documento fiscal e controle de saldo a liquidar.

**Estado:** Implementada, não exposta

**Processos:** PRO-CON-003

**Regras aplicáveis:** RN-CON-020, RN-CON-021, RN-CON-022

**Atores:** AT-CON-001, AT-CON-009

**Entidades:** `Liquidacao`

---

## CAP-CON-004 — Pagamento da despesa

**Descrição:** Executar a ordem bancária sobre liquidação confirmada, com controle de saldo a pagar e registro da conta bancária.

**Estado:** Implementada, não exposta

**Processos:** PRO-CON-004

**Regras aplicáveis:** RN-CON-030, RN-CON-031, RN-CON-032

**Atores:** AT-CON-005, AT-CON-009

**Entidades:** `Pagamento`

---

## CAP-CON-005 — Registro de lançamentos contábeis

**Descrição:** Registrar partidas dobradas por conta do plano, com balanço obrigatório e rastreabilidade da origem.

**Estado:** Implementada, não exposta

**Processos:** PRO-CON-007, PRO-CON-008

**Regras aplicáveis:** RN-CON-040

**Atores:** AT-CON-001

**Entidades:** `LancamentoContabil`, `Partida`

---

## CAP-CON-006 — Conciliação bancária

**Descrição:** Comparar o saldo contábil da conta com o extrato bancário na competência e justificar divergências.

**Estado:** Implementada, não exposta

**Processos:** PRO-CON-009

**Regras aplicáveis:** RN-CON-050

**Atores:** AT-CON-004

**Entidades:** `ConciliacaoContabil`

---

## CAP-CON-007 — Consulta e transparência da execução

**Descrição:** Disponibilizar a execução da despesa para controle interno, externalização e controle social.

**Estado:** Planejada — não existe endpoint de leitura no módulo `sigmun_con`.

**Processos:** PRO-CON-010

**Regras aplicáveis:** RN-CON-001

**Atores:** AT-CON-006, AT-CON-007

**Entidades:** `Empenho`, `Liquidacao`, `Pagamento`

---

## CAP-CON-008 — Trilha de auditoria contábil

**Descrição:** Preservar autoria, data e valor de cada operação com efeito contábil para fins de responsabilização.

**Estado:** Parcial — os campos `created_by` existem, mas não são preenchidos; `lancamentos` e `conciliacoes` não possuem `updated_at` nem `updated_by`; não há evento de domínio.

**Processos:** PRO-CON-011

**Regras aplicáveis:** RN-CON-060

**Atores:** AT-CON-006, AT-CON-010

**Entidades:** todas

---

# 5. Agrupamento por Natureza

| Natureza | Capacidades |
| --- | --- |
| Execução orçamentária | CAP-CON-002, CAP-CON-003, CAP-CON-004 |
| Contabilidade analítica | CAP-CON-001, CAP-CON-005 |
| Controle | CAP-CON-006, CAP-CON-007, CAP-CON-008 |

A separação entre execução orçamentária e contabilidade analítica é a fronteira
tradicional do orçamento público: a primeira responde pela **execução da despesa**
(dotação, empenho, liquidação, pagamento) e a segunda pelo **registro contábil**
(partidas dobradas, saldo por conta, conciliação).

---

# 6. Dependências entre Capacidades

```text
CAP-CON-008 (auditoria)
    ▲
    │ exige
CAP-CON-007 (consulta) ◄── CAP-CON-006 (conciliação)
    ▲
    │ alimenta
CAP-CON-005 (lançamentos)
    ▲
    │ requer plano de contas
CAP-CON-001 (PCASP)

CAP-CON-002 (empenho) ──► CAP-CON-003 (liquidação) ──► CAP-CON-004 (pagamento)
        │
        │ consome saldo
        ▼
   DOM-ORC (dotação autorizada)
```

* CAP-CON-001 é pré-requisito de CAP-CON-005: não há lançamento sem conta válida.
* CAP-CON-002 é pré-requisito de CAP-CON-003, que é pré-requisito de CAP-CON-004.
* CAP-CON-008 permeia todas as demais, pois toda operação com efeito contábil
  deve ser rastreável.
* CAP-CON-002 depende de dados externos: sem dotação autorizada no DOM-ORC não há
  empenho.

---

# 7. Lacunas Identificadas

| Lacuna | Capacidade afetada | Achado da auditoria |
| --- | --- | --- |
| Nenhuma capacidade exposta na API | Todas as implementadas | C-01 |
| DOM-ORC igualmente inacessível | CAP-CON-002 | C-02 |
| Consulta e relatórios inexistentes | CAP-CON-007 | B-05 |
| Trilha de auditoria incompleta | CAP-CON-008 | M-04 |
| Lançamento contábil não automático | CAP-CON-005 | M-03 |

---

# 8. Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteúdo inicial derivado da auditoria do módulo `sigmun_con` e do PCASP |

---

**Documento:** 002-Mapa-de-Capacidades-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente