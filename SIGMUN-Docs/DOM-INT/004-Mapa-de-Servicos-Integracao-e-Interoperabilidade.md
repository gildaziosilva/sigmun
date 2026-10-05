# 004 – Mapa-de-Servicos – Integração e Interoperabilidade

#### Mapa-de-Servicos – Integração e Interoperabilidade

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-INT-004

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

Este artefato detalha **o mapa de serviços** do domínio Integração e Interoperabilidade (`DOM-INT`), com base na implementação material identificada em `src/modules/sigmun_int` e no conteúdo de negócio declarado no gerador.

---

# 2. Operações publicadas em `/api/v1/int`

| Método | Caminho | Recurso | Resumo |
| --- | --- | --- | --- |
| GET | `/api/v1/int/apis` | apis | Lista APIs externas do catálogo |
| POST | `/api/v1/int/apis` | apis | Registra uma API externa no catálogo |
| DELETE | `/api/v1/int/apis/{api_id}` | apis | Exclui (exclusão lógica) uma API externa |
| GET | `/api/v1/int/apis/{api_id}` | apis | Busca uma API externa por ID |
| PATCH | `/api/v1/int/apis/{api_id}` | apis | Atualiza uma API externa |
| POST | `/api/v1/int/apis/{api_id}/estado` | apis | Muda o estado de uma API |
| POST | `/api/v1/int/barras/eventos/consumir` | barras | Consome eventos pendentes do outbox de um domínio produtor |
| POST | `/api/v1/int/barras/webhooks/despachar` | barras | Despacha entregas pendentes para webhooks com retry e backoff |
| GET | `/api/v1/int/conectores` | conectores | Lista conectores oficiais |
| POST | `/api/v1/int/conectores` | conectores | Registra um conector oficial |
| DELETE | `/api/v1/int/conectores/{conector_id}` | conectores | Exclui (exclusão lógica) um conector |
| GET | `/api/v1/int/conectores/{conector_id}` | conectores | Busca um conector por ID |
| PATCH | `/api/v1/int/conectores/{conector_id}` | conectores | Atualiza um conector |
| POST | `/api/v1/int/conectores/{conector_id}/estado` | conectores | Muda o estado de um conector (RN-INT-004) |
| GET | `/api/v1/int/contratos` | contratos | Lista contratos de integração |
| POST | `/api/v1/int/contratos` | contratos | Crea um contrato de integração |
| DELETE | `/api/v1/int/contratos/{contrato_id}` | contratos | Exclui (exclusão lógica) um contrato |
| GET | `/api/v1/int/contratos/{contrato_id}` | contratos | Busca um contrato por ID |
| PATCH | `/api/v1/int/contratos/{contrato_id}` | contratos | Atualiza um contrato de integração |
| POST | `/api/v1/int/contratos/{contrato_id}/aprovar` | contratos | Aprova um contrato (rascunho -> vigente) |
| POST | `/api/v1/int/contratos/{contrato_id}/retirar` | contratos | Retira um contrato (vigente -> retirado) |
| GET | `/api/v1/int/entregas` | entregas | Lista entregas de mensagens |
| GET | `/api/v1/int/entregas/{entrega_id}` | entregas | Busca uma entrega por ID |
| POST | `/api/v1/int/entregas/{entrega_id}/reenfileirar` | entregas | Reenfileira uma entrega da fila de mensagens mortas |
| GET | `/api/v1/int/webhooks` | webhooks | Lista webhooks |
| POST | `/api/v1/int/webhooks` | webhooks | Registra um webhook inscrito no barramento |
| DELETE | `/api/v1/int/webhooks/{webhook_id}` | webhooks | Exclui (exclusão lógica) um webhook |
| GET | `/api/v1/int/webhooks/{webhook_id}` | webhooks | Busca um webhook por ID |
| PATCH | `/api/v1/int/webhooks/{webhook_id}` | webhooks | Atualiza um webhook |
| GET | `/api/v1/int/webhooks/{webhook_id}/entregas` | webhooks | Lista entregas de um webhook |
| POST | `/api/v1/int/webhooks/{webhook_id}/estado` | webhooks | Ativa ou desativa um webhook |

---

# 3. Recursos publicados

| Recurso | Operações |
| --- | --- |
| apis | 6 |
| barras | 2 |
| conectores | 6 |
| contratos | 7 |
| entregas | 3 |
| webhooks | 7 |

---

# 4. Lacunas a validar

* Definir a política de reprocessamento e o limite de tentativas por entrega.
* Definir a janela de retenção das entregas recebidas.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 004-Integracao-e-Interoperabilidade-Mapa-de-Servicos.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
