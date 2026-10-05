# 013 – Modelo-de-Dados – Integração e Interoperabilidade

#### Modelo-de-Dados – Integração e Interoperabilidade

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-INT-013

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

Este artefato detalha **o modelo de dados** do domínio Integração e Interoperabilidade (`DOM-INT`), com base na implementação material identificada em `src/modules/sigmun_int` e no conteúdo de negócio declarado no gerador.

---

# 2. Tabelas no schema `int`

### apis_externas (`ApiExternaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<UQ, NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| provedor : TEXT | opcional |
| url_base : TEXT | opcional |
| tipo : TEXT <<NN>> | NOT NULL |
| autenticacao : TEXT <<NN>> | NOT NULL |
| estado : TEXT <<NN>> | NOT NULL |
| versao : TEXT <<NN>> | NOT NULL |
| limite_por_minuto : INTEGER <<NN>> | NOT NULL |
| timeout_seg : INTEGER <<NN>> | NOT NULL |
| criado_em : DATETIME <<NN>> | NOT NULL |
| atualizado_em : DATETIME <<NN>> | NOT NULL |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### conectores (`ConectorModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<UQ, NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| provedor : TEXT | opcional |
| url_base : TEXT | opcional |
| autenticacao_tipo : TEXT <<NN>> | NOT NULL |
| estado : TEXT <<NN>> | NOT NULL |
| config : JSON <<NN>> | NOT NULL |
| criado_em : DATETIME <<NN>> | NOT NULL |
| atualizado_em : DATETIME <<NN>> | NOT NULL |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### contratos_integracao (`ContratoIntegracaoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<UQ, NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| versao_formato : TEXT <<NN>> | NOT NULL |
| esquema_ref : TEXT | opcional |
| api_externa_id : UUID | opcional |
| estado : TEXT <<NN>> | NOT NULL |
| criado_em : DATETIME <<NN>> | NOT NULL |
| atualizado_em : DATETIME <<NN>> | NOT NULL |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### entregas_webhook (`EntregaWebhookModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| webhook_id : UUID <<NN>> | NOT NULL |
| url_destino : TEXT <<NN>> | NOT NULL |
| cabecalhos : JSON <<NN>> | NOT NULL |
| topico : TEXT <<NN>> | NOT NULL |
| evento_nome : TEXT <<NN>> | NOT NULL |
| agregado_tipo : TEXT <<NN>> | NOT NULL |
| agregado_id : TEXT <<NN>> | NOT NULL |
| payload : JSON <<NN>> | NOT NULL |
| estado : TEXT <<NN>> | NOT NULL |
| tentativas : INTEGER <<NN>> | NOT NULL |
| max_tentativas : INTEGER <<NN>> | NOT NULL |
| backoff_base_seg : INTEGER <<NN>> | NOT NULL |
| ultimo_http_status : INTEGER | opcional |
| ultimo_erro : TEXT | opcional |
| proximo_retry : DATETIME | opcional |
| criado_em : DATETIME <<NN>> | NOT NULL |
| entregue_em : DATETIME | opcional |
| atualizado_em : DATETIME <<NN>> | NOT NULL |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### eventos_processados (`EventoProcessadoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| fonte : TEXT <<NN>> | NOT NULL |
| evento_outbox_id : TEXT <<NN>> | NOT NULL |
| topico : TEXT <<NN>> | NOT NULL |
| evento_nome : TEXT <<NN>> | NOT NULL |
| agregado_tipo : TEXT <<NN>> | NOT NULL |
| agregado_id : TEXT <<NN>> | NOT NULL |
| payload : JSON <<NN>> | NOT NULL |
| recebido_em : DATETIME <<NN>> | NOT NULL |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### webhooks (`WebhookModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| nome : TEXT <<UQ, NN>> | NOT NULL |
| url_destino : TEXT <<NN>> | NOT NULL |
| segredo_ref : TEXT | opcional |
| topicos : JSON <<NN>> | NOT NULL |
| cabecalhos : JSON <<NN>> | NOT NULL |
| estado : TEXT <<NN>> | NOT NULL |
| max_tentativas : INTEGER <<NN>> | NOT NULL |
| backoff_base_seg : INTEGER <<NN>> | NOT NULL |
| criado_em : DATETIME <<NN>> | NOT NULL |
| atualizado_em : DATETIME <<NN>> | NOT NULL |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 013-Integracao-e-Interoperabilidade-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
