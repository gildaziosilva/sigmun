# 001 – Mapa de Atores – Contabilidade Pública

#### Mapa de Atores – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-001

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

Este artefato identifica as pessoas, unidades organizacionais, papéis, agentes de
integração e entidades externas que interagem com o domínio de Contabilidade Pública,
estabelecendo quem participa, com que responsabilidade e em qual capacidade.

---

# 2. Princípios

* Atores representam papéis, e não pessoas específicas.
* A mesma pessoa pode exercer mais de um papel.
* Responsabilidade de negócio não se confunde com permissão de sistema.
* Atores externos são identificados quando influenciam os processos.
* A segregação de funções exige que emissão, liquidação e pagamento possam ser
  exercidos por papéis distintos.

---

# 3. Atores Identificados

| Identificador | Ator | Tipo | Papel no domínio | Capacidades |
| --- | --- | --- | --- | --- |
| AT-CON-001 | Contador da execução orçamentária | Servidor municipal | Emite, liquida e anula empenhos; responde pela execução da despesa. | CAP-CON-002, CAP-CON-003, CAP-CON-005 |
| AT-CON-002 | Ordenador de despesa | Servidor municipal | Autoriza a edição, o estorno e o cancelamento de empenhos. | CAP-CON-002, CAP-CON-004 |
| AT-CON-003 | Gestor do plano de contas | Servidor municipal | Mantém o PCASP e responde pela estrutura de contas do plano municipal. | CAP-CON-001 |
| AT-CON-004 | Contador da conciliação | Servidor municipal | Concilia saldos contábeis com extratos bancários e justifica divergências. | CAP-CON-006 |
| AT-CON-005 | Tesoureiro | Servidor municipal | Executa a ordem bancária do pagamento e confirma a saída de recursos. | CAP-CON-004 |
| AT-CON-006 | Controle interno e externalização | Servidor / órgão de controle | Fiscaliza a execução da despesa e consulta os registros contábeis. | CAP-CON-007, CAP-CON-008 |
| AT-CON-007 | Cidadão e Controle Social | Público externo | Consulta a execução orçamentária publicada para transparência. | CAP-CON-007 |
| AT-CON-008 | DOM-ORC — Orçamento Público | Sistema | Fornece a dotação autorizada e o saldo disponível que governa o empenho. | CAP-CON-002 |
| AT-CON-009 | DOM-GDO — Gestão Documental | Sistema | Armazena documentos fiscais e comprovantes de pagamento. | CAP-CON-003, CAP-CON-004 |
| AT-CON-010 | DOM-IDN — Identidade e Acesso | Sistema | Autentica e autoriza o servidor responsável pela operação contábil. | CAP-CON-008 |

---

# 4. Detalhamento

## AT-CON-001 — Contador da execução orçamentária

**Tipo:** Servidor municipal

**Papel:** Emite, liquida e anula empenhos; responde pela execução da despesa.

**Decisões que pode tomar:** Emitir empenho sobre dotação com saldo; registrar liquidação com documento fiscal; anular empenho; registrar pagamento; lançar partidas dobradas.

**Sistemas utilizados:** SIGMUN — Contabilidade Pública; DOM-ORC; DOM-GDO

**Capacidades exercidas:** CAP-CON-002, CAP-CON-003, CAP-CON-005

---

## AT-CON-002 — Ordenador de despesa

**Tipo:** Servidor municipal

**Papel:** Autoriza a edição, o estorno e o cancelamento de empenhos.

**Decisões que pode tomar:** Autorizar cancelamento de empenho; estornar liquidação; decidir sobre retenção de saldo.

**Sistemas utilizados:** SIGMUN — Contabilidade Pública

**Capacidades exercidas:** CAP-CON-002, CAP-CON-004

---

## AT-CON-003 — Gestor do plano de contas

**Tipo:** Servidor municipal

**Papel:** Mantém o PCASP e responde pela estrutura de contas do plano municipal.

**Decisões que pode tomar:** Criar e desdobrar contas; desativar contas que não devem receber lançamento; criar vínculos de conta pai.

**Sistemas utilizados:** SIGMUN — Contabilidade Pública

**Capacidades exercidas:** CAP-CON-001

---

## AT-CON-004 — Contador da conciliação

**Tipo:** Servidor municipal

**Papel:** Concilia saldos contábeis com extratos bancários e justifica divergências.

**Decisões que pode tomar:** Registrar conciliação conciliada; marcar divergência com justificativa.

**Sistemas utilizados:** SIGMUN — Contabilidade Pública

**Capacidades exercidas:** CAP-CON-006

---

## AT-CON-005 — Tesoureiro

**Tipo:** Servidor municipal

**Papel:** Executa a ordem bancária do pagamento e confirma a saída de recursos.

**Decisões que pode tomar:** Programar pagamento; efetivar pagamento; cancelar pagamento programado.

**Sistemas utilizados:** SIGMUN — Contabilidade Pública; DOM-FRO (contas bancárias)

**Capacidades exercidas:** CAP-CON-004

---

## AT-CON-006 — Controle interno e externalização

**Tipo:** Servidor municipal / órgão de controle

**Papel:** Fiscaliza a execução da despesa e consulta os registros contábeis.

**Decisões que pode tomar:** Não altera registros; requisita correções; emite parecer.

**Sistemas utilizados:** SIGMUN — Contabilidade Pública

**Capacidades exercidas:** CAP-CON-007, CAP-CON-008

---

## AT-CON-007 — Cidadão e Controle Social

**Tipo:** Público externo

**Papel:** Consulta a execução orçamentária publicada para transparência.

**Decisões que pode tomar:** Não altera registros; consulta dados publicados.

**Sistemas utilizados:** Portal da transparência; SIGMUN — Contabilidade Pública

**Capacidades exercidas:** CAP-CON-007

---

## AT-CON-008 — DOM-ORC — Orçamento Público

**Tipo:** Sistema

**Papel:** Fornece a dotação autorizada e o saldo disponível que governa o empenho.

**Decisões que pode tomar:** Autoriza dotação; mantém saldo disponível e saldo empenhado.

**Sistemas utilizados:** SIGMUN — DOM-ORC

**Capacidades exercidas:** CAP-CON-002

---

## AT-CON-009 — DOM-GDO — Gestão Documental

**Tipo:** Sistema

**Papel:** Armazena documentos fiscais e comprovantes de pagamento.

**Decisões que pode tomar:** Não altera o registro contábil; mantém a evidência documental.

**Sistemas utilizados:** SIGMUN — DOM-GDO

**Capacidades exercidas:** CAP-CON-003, CAP-CON-004

---

## AT-CON-010 — DOM-IDN — Identidade e Acesso

**Tipo:** Sistema

**Papel:** Autentica e autoriza o servidor responsável pela operação contábil.

**Decisões que pode tomar:** Concede ou nega a permissão sobre o recurso.

**Sistemas utilizados:** SIGMUN — DOM-IDN

**Capacidades exercidas:** CAP-CON-008

---

# 5. Segregação de Funções

O domínio exige segregação entre os seguintes pares, conforme o princípio da
segregação de funções previsto na Lei 4.320/64:

| Processo | Quem executa | Quem autoriza |
| --- | --- | --- |
| PRO-CON-002 — Emissão de empenho | AT-CON-001 | AT-CON-002 |
| PRO-CON-004 — Pagamento | AT-CON-001 | AT-CON-005 |
| PRO-CON-006 — Cancelamento de empenho | AT-CON-001 | AT-CON-002 |

A separação existe porque o mesmo servidor que compromete o orçamento não pode
liberar o pagamento correspondente sem aprovação do ordenador.

---

# 6. Matriz Ator × Capacidade

| Ator | CAP-001 | CAP-002 | CAP-003 | CAP-004 | CAP-005 | CAP-006 | CAP-007 | CAP-008 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AT-CON-001 | — | ✔ | ✔ | — | ✔ | — | — | ✔ |
| AT-CON-002 | — | ✔ | — | ✔ | — | — | ✔ | ✔ |
| AT-CON-003 | ✔ | — | — | — | — | — | — | — |
| AT-CON-004 | — | — | — | — | — | ✔ | — | ✔ |
| AT-CON-005 | — | — | — | ✔ | — | — | — | ✔ |
| AT-CON-006 | — | — | — | — | — | — | ✔ | ✔ |
| AT-CON-007 | — | — | — | — | — | — | ✔ | — |
| AT-CON-008 | — | ✔ | — | — | — | — | — | — |
| AT-CON-009 | — | — | ✔ | ✔ | — | — | — | — |
| AT-CON-010 | — | — | — | — | — | — | — | ✔ |

---

# 7. Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteúdo inicial derivado da auditoria do módulo `sigmun_con` e do PCASP |

---

**Documento:** 001-Mapa-de-Atores-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
