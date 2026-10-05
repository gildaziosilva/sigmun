# 005 – Casos-de-Uso – Integração e Interoperabilidade

#### Casos-de-Uso – Integração e Interoperabilidade

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-INT-005

**Domínio:** Integração e Interoperabilidade

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Integracao-e-Interoperabilidade.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `030-Roadmap-de-Implementacao-dos-Dominios.md`
* `Mapa-de-Dominios.md`

---


# 1. Finalidade

Este artefato detalha **os casos de uso** do domínio Integração e Interoperabilidade (`DOM-INT`), com base na implementação material identificada em `src/modules/sigmun_int` e no conteúdo de negócio declarado no gerador.

---

# 2. Casos de uso implementados

| Identificador | Caso de uso | Classe | Resumo |
| --- | --- | --- | --- |
| CU-INT-001 | CriarApiExterna | `CriarApiExternaUseCase` | Registra uma nova API externa no catálogo. |
| CU-INT-002 | BuscarApiExterna | `BuscarApiExternaUseCase` | Consulta do catálogo de APIs externas. |
| CU-INT-003 | AtualizarApiExterna | `AtualizarApiExternaUseCase` | Atualiza os dados de uma API externa (atualização parcial). |
| CU-INT-004 | MudarEstadoApi | `MudarEstadoApiUseCase` | Transiciona uma API entre os estados do ciclo de vida. |
| CU-INT-005 | DeletarApiExterna | `DeletarApiExternaUseCase` | Exclui (exclusão lógica) uma API externa do catálogo. |
| CU-INT-006 | CriarContratoIntegracao | `CriarContratoIntegracaoUseCase` | Cria um contrato de integração para uma API do catálogo. |
| CU-INT-007 | BuscarContratoIntegracao | `BuscarContratoIntegracaoUseCase` | Consulta de contratos de integração. |
| CU-INT-008 | AtualizarContratoIntegracao | `AtualizarContratoIntegracaoUseCase` | Atualiza os dados de um contrato de integração. |
| CU-INT-009 | AprovarContratoIntegracao | `AprovarContratoIntegracaoUseCase` | Aprova um contrato (rascunho -> vigente). |
| CU-INT-010 | RetirarContratoIntegracao | `RetirarContratoIntegracaoUseCase` | Retira um contrato (vigente -> retirado). |
| CU-INT-011 | DeletarContratoIntegracao | `DeletarContratoIntegracaoUseCase` | Exclui (exclusão lógica) um contrato de integração. |
| CU-INT-012 | CriarConector | `CriarConectorUseCase` | Registra um conector oficial de interoperabilidade. |
| CU-INT-013 | BuscarConector | `BuscarConectorUseCase` | Consulta de conectores oficiais. |
| CU-INT-014 | AtualizarConector | `AtualizarConectorUseCase` | Atualiza a configuração de um conector (merge do dict config). |
| CU-INT-015 | MudarEstadoConector | `MudarEstadoConectorUseCase` | Transiciona o estado de configuração do conector. |
| CU-INT-016 | DeletarConector | `DeletarConectorUseCase` | Exclui (exclusão lógica) um conector. |
| CU-INT-017 | RegistrarWebhook | `RegistrarWebhookUseCase` | Registra um webhook inscrito para receber eventos do barramento. |
| CU-INT-018 | BuscarWebhook | `BuscarWebhookUseCase` | Consulta de webhooks. |
| CU-INT-019 | AtualizarWebhook | `AtualizarWebhookUseCase` | Atualiza os dados de um webhook (atualizacao parcial). |
| CU-INT-020 | MudarEstadoWebhook | `MudarEstadoWebhookUseCase` | Ativa ou desativa a recepcao de eventos de um webhook. |
| CU-INT-021 | DeletarWebhook | `DeletarWebhookUseCase` | Exclui (exclusao logica) um webhook. |
| CU-INT-022 | BuscarEntregaWebhook | `BuscarEntregaWebhookUseCase` | Consulta de entregas de mensagens. |
| CU-INT-023 | RetryEntregaWebhook | `RetryEntregaWebhookUseCase` | Reenfileira uma entrega falhada ou na fila de mensagens mortas. |
| CU-INT-024 | CancelarEntregaWebhook | `CancelarEntregaWebhookUseCase` | Cancela uma entrega pendente (não será reentregue). |
| CU-INT-025 | ConsumirOutbox | `ConsumirOutboxUseCase` | Consome eventos pendentes do outbox de um domínio produtor. |
| CU-INT-026 | DespacharWebhooks | `DespacharWebhooksUseCase` | Entrega as mensagens pendentes aos webhooks inscritos. |

---

# 3. Cobertura

Casos de uso no código: **26**. Operações publicadas: **31**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 005-Integracao-e-Interoperabilidade-Casos-de-Uso.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
