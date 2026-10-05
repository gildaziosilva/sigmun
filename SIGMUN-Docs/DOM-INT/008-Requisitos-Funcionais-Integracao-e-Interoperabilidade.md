# 008 – Requisitos-Funcionais – Integração e Interoperabilidade

#### Requisitos-Funcionais – Integração e Interoperabilidade

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-INT-008

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

Este artefato detalha **os requisitos funcionais** do domínio Integração e Interoperabilidade (`DOM-INT`), com base na implementação material identificada em `src/modules/sigmun_int` e no conteúdo de negócio declarado no gerador.

---

# 2. Requisitos

| ID | Requisito | Prioridade | Recurso | Capacidade |
| --- | --- | --- | --- | --- |
| RF-INT-001 | GET /api/v1/int/apis | Média | apis | CAP-INT-001 |
| RF-INT-002 | POST /api/v1/int/apis | Alta | apis | CAP-INT-001 |
| RF-INT-003 | DELETE /api/v1/int/apis/{api_id} | Alta | apis | CAP-INT-001 |
| RF-INT-004 | GET /api/v1/int/apis/{api_id} | Média | apis | CAP-INT-001 |
| RF-INT-005 | PATCH /api/v1/int/apis/{api_id} | Média | apis | CAP-INT-001 |
| RF-INT-006 | POST /api/v1/int/apis/{api_id}/estado | Alta | apis | CAP-INT-001 |
| RF-INT-007 | POST /api/v1/int/barras/eventos/consumir | Alta | barras | CAP-INT-001 |
| RF-INT-008 | POST /api/v1/int/barras/webhooks/despachar | Alta | barras | CAP-INT-001 |
| RF-INT-009 | GET /api/v1/int/conectores | Média | conectores | CAP-INT-001 |
| RF-INT-010 | POST /api/v1/int/conectores | Alta | conectores | CAP-INT-001 |
| RF-INT-011 | DELETE /api/v1/int/conectores/{conector_id} | Alta | conectores | CAP-INT-001 |
| RF-INT-012 | GET /api/v1/int/conectores/{conector_id} | Média | conectores | CAP-INT-001 |
| RF-INT-013 | PATCH /api/v1/int/conectores/{conector_id} | Média | conectores | CAP-INT-001 |
| RF-INT-014 | POST /api/v1/int/conectores/{conector_id}/estado | Alta | conectores | CAP-INT-001 |
| RF-INT-015 | GET /api/v1/int/contratos | Média | contratos | CAP-INT-001 |
| RF-INT-016 | POST /api/v1/int/contratos | Alta | contratos | CAP-INT-001 |
| RF-INT-017 | DELETE /api/v1/int/contratos/{contrato_id} | Alta | contratos | CAP-INT-001 |
| RF-INT-018 | GET /api/v1/int/contratos/{contrato_id} | Média | contratos | CAP-INT-001 |
| RF-INT-019 | PATCH /api/v1/int/contratos/{contrato_id} | Média | contratos | CAP-INT-001 |
| RF-INT-020 | POST /api/v1/int/contratos/{contrato_id}/aprovar | Alta | contratos | CAP-INT-001 |
| RF-INT-021 | POST /api/v1/int/contratos/{contrato_id}/retirar | Alta | contratos | CAP-INT-001 |
| RF-INT-022 | GET /api/v1/int/entregas | Média | entregas | CAP-INT-001 |
| RF-INT-023 | GET /api/v1/int/entregas/{entrega_id} | Média | entregas | CAP-INT-001 |
| RF-INT-024 | POST /api/v1/int/entregas/{entrega_id}/reenfileirar | Alta | entregas | CAP-INT-001 |
| RF-INT-025 | GET /api/v1/int/webhooks | Média | webhooks | CAP-INT-001 |
| RF-INT-026 | POST /api/v1/int/webhooks | Alta | webhooks | CAP-INT-001 |
| RF-INT-027 | DELETE /api/v1/int/webhooks/{webhook_id} | Alta | webhooks | CAP-INT-001 |
| RF-INT-028 | GET /api/v1/int/webhooks/{webhook_id} | Média | webhooks | CAP-INT-001 |
| RF-INT-029 | PATCH /api/v1/int/webhooks/{webhook_id} | Média | webhooks | CAP-INT-001 |
| RF-INT-030 | GET /api/v1/int/webhooks/{webhook_id}/entregas | Média | webhooks | CAP-INT-001 |
| RF-INT-031 | POST /api/v1/int/webhooks/{webhook_id}/estado | Alta | webhooks | CAP-INT-001 |

---

# 3. Cobertura

Operações publicadas: **31**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 008-Integracao-e-Interoperabilidade-Requisitos-Funcionais.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
