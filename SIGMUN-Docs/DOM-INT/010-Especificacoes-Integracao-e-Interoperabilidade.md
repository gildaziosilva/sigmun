# 010 – Especificacoes – Integração e Interoperabilidade

#### Especificacoes – Integração e Interoperabilidade

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-INT-010

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

Este artefato detalha **as especificações** do domínio Integração e Interoperabilidade (`DOM-INT`), com base na implementação material identificada em `src/modules/sigmun_int` e no conteúdo de negócio declarado no gerador.

---

# 2. Contratos publicados

| Método | Caminho | Recurso | Corpo |
| --- | --- | --- | --- |
| GET | `/api/v1/int/apis` | apis | JSON (payload do domínio) |
| POST | `/api/v1/int/apis` | apis | JSON (payload do domínio) |
| DELETE | `/api/v1/int/apis/{api_id}` | apis | JSON (payload do domínio) |
| GET | `/api/v1/int/apis/{api_id}` | apis | JSON (payload do domínio) |
| PATCH | `/api/v1/int/apis/{api_id}` | apis | JSON (payload do domínio) |
| POST | `/api/v1/int/apis/{api_id}/estado` | apis | JSON (payload do domínio) |
| POST | `/api/v1/int/barras/eventos/consumir` | barras | JSON (payload do domínio) |
| POST | `/api/v1/int/barras/webhooks/despachar` | barras | JSON (payload do domínio) |
| GET | `/api/v1/int/conectores` | conectores | JSON (payload do domínio) |
| POST | `/api/v1/int/conectores` | conectores | JSON (payload do domínio) |
| DELETE | `/api/v1/int/conectores/{conector_id}` | conectores | JSON (payload do domínio) |
| GET | `/api/v1/int/conectores/{conector_id}` | conectores | JSON (payload do domínio) |
| PATCH | `/api/v1/int/conectores/{conector_id}` | conectores | JSON (payload do domínio) |
| POST | `/api/v1/int/conectores/{conector_id}/estado` | conectores | JSON (payload do domínio) |
| GET | `/api/v1/int/contratos` | contratos | JSON (payload do domínio) |
| POST | `/api/v1/int/contratos` | contratos | JSON (payload do domínio) |
| DELETE | `/api/v1/int/contratos/{contrato_id}` | contratos | JSON (payload do domínio) |
| GET | `/api/v1/int/contratos/{contrato_id}` | contratos | JSON (payload do domínio) |
| PATCH | `/api/v1/int/contratos/{contrato_id}` | contratos | JSON (payload do domínio) |
| POST | `/api/v1/int/contratos/{contrato_id}/aprovar` | contratos | JSON (payload do domínio) |
| POST | `/api/v1/int/contratos/{contrato_id}/retirar` | contratos | JSON (payload do domínio) |
| GET | `/api/v1/int/entregas` | entregas | JSON (payload do domínio) |
| GET | `/api/v1/int/entregas/{entrega_id}` | entregas | JSON (payload do domínio) |
| POST | `/api/v1/int/entregas/{entrega_id}/reenfileirar` | entregas | JSON (payload do domínio) |
| GET | `/api/v1/int/webhooks` | webhooks | JSON (payload do domínio) |
| POST | `/api/v1/int/webhooks` | webhooks | JSON (payload do domínio) |
| DELETE | `/api/v1/int/webhooks/{webhook_id}` | webhooks | JSON (payload do domínio) |
| GET | `/api/v1/int/webhooks/{webhook_id}` | webhooks | JSON (payload do domínio) |
| PATCH | `/api/v1/int/webhooks/{webhook_id}` | webhooks | JSON (payload do domínio) |
| GET | `/api/v1/int/webhooks/{webhook_id}/entregas` | webhooks | JSON (payload do domínio) |
| POST | `/api/v1/int/webhooks/{webhook_id}/estado` | webhooks | JSON (payload do domínio) |

---

# 3. Validações aplicadas

| Regra | Validação |
| --- | --- |
| RN-INT-001 | API externa só opera quando o contrato está publicado. |
| RN-INT-002 | o contrato deve referenciar uma API existente do catálogo |
| RN-INT-004 | para passar a `ativo` o conector deve ter configuração |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 010-Integracao-e-Interoperabilidade-Especificacoes.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
