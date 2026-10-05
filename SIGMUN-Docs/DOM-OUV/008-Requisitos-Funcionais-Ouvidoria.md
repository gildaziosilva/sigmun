# 008 – Requisitos-Funcionais – Ouvidoria

#### Requisitos-Funcionais – Ouvidoria

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OUV-008

**Domínio:** Ouvidoria

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Ouvidoria.md`
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

Este artefato detalha **os requisitos funcionais** do domínio Ouvidoria (`DOM-OUV`), com base na implementação material identificada em `src/modules/sigmun_ouvidoria` e no conteúdo de negócio declarado no gerador.

---

# 2. Requisitos

| ID | Requisito | Prioridade | Recurso | Capacidade |
| --- | --- | --- | --- | --- |
| RF-OU-001 | GET /api/v1/ouv/denuncias | Média | v | CAP-OU-001 |
| RF-OU-002 | POST /api/v1/ouv/denuncias | Alta | v | CAP-OU-001 |
| RF-OU-003 | POST /api/v1/ouv/denuncias/{denuncia_id}/encaminhar | Alta | v | CAP-OU-001 |
| RF-OU-004 | GET /api/v1/ouv/estatisticas | Média | v | CAP-OU-001 |
| RF-OU-005 | GET /api/v1/ouv/manifestacoes | Média | v | CAP-OU-001 |
| RF-OU-006 | POST /api/v1/ouv/manifestacoes | Alta | v | CAP-OU-001 |
| RF-OU-007 | GET /api/v1/ouv/manifestacoes-vencendo | Média | v | CAP-OU-001 |
| RF-OU-008 | GET /api/v1/ouv/manifestacoes/{identificador} | Média | v | CAP-OU-001 |
| RF-OU-009 | POST /api/v1/ouv/manifestacoes/{manifestacao_id}/avaliar | Alta | v | CAP-OU-001 |
| RF-OU-010 | POST /api/v1/ouv/manifestacoes/{manifestacao_id}/prorrogar | Alta | v | CAP-OU-001 |
| RF-OU-011 | POST /api/v1/ouv/manifestacoes/{manifestacao_id}/responder | Alta | v | CAP-OU-001 |
| RF-OU-012 | POST /api/v1/ouv/manifestacoes/{manifestacao_id}/status | Alta | v | CAP-OU-001 |
| RF-OU-013 | GET /api/v1/ouv/pedidos-lai | Média | v | CAP-OU-001 |
| RF-OU-014 | POST /api/v1/ouv/pedidos-lai | Alta | v | CAP-OU-001 |
| RF-OU-015 | POST /api/v1/ouv/pedidos-lai/{pedido_id}/recurso | Alta | v | CAP-OU-001 |
| RF-OU-016 | POST /api/v1/ouv/pedidos-lai/{recurso_id}/decidir-recurso | Alta | v | CAP-OU-001 |

---

# 3. Cobertura

Operações publicadas: **16**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 008-Ouvidoria-Requisitos-Funcionais.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
