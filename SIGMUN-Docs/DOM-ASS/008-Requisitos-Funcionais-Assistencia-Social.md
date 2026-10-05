# 008 – Requisitos-Funcionais – Assistência Social

#### Requisitos-Funcionais – Assistência Social

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ASS-008

**Domínio:** Assistência Social

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Assistencia-Social.md`
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

Este artefato detalha **os requisitos funcionais** do domínio Assistência Social (`DOM-ASS`), com base na implementação material identificada em `src/modules/sigmun_assistencia_social` e no conteúdo de negócio declarado no gerador.

---

# 2. Requisitos

| ID | Requisito | Prioridade | Recurso | Capacidade |
| --- | --- | --- | --- | --- |
| RF-ASS-001 | GET /api/v1/ass/atendimentos | Média | atendimentos | CAP-ASS-001 |
| RF-ASS-002 | POST /api/v1/ass/atendimentos | Alta | atendimentos | CAP-ASS-001 |
| RF-ASS-003 | GET /api/v1/ass/atendimentos/{atendimento_id} | Média | atendimentos | CAP-ASS-001 |
| RF-ASS-004 | GET /api/v1/ass/beneficios | Média | beneficios | CAP-ASS-001 |
| RF-ASS-005 | POST /api/v1/ass/beneficios | Alta | beneficios | CAP-ASS-001 |
| RF-ASS-006 | GET /api/v1/ass/beneficios/{beneficio_id} | Média | beneficios | CAP-ASS-001 |
| RF-ASS-007 | POST /api/v1/ass/beneficios/{beneficio_id}/aprovar | Alta | beneficios | CAP-ASS-001 |
| RF-ASS-008 | POST /api/v1/ass/beneficios/{beneficio_id}/cancelar | Alta | beneficios | CAP-ASS-001 |
| RF-ASS-009 | POST /api/v1/ass/beneficios/{beneficio_id}/entregar | Alta | beneficios | CAP-ASS-001 |
| RF-ASS-010 | POST /api/v1/ass/beneficios/{beneficio_id}/negar | Alta | beneficios | CAP-ASS-001 |
| RF-ASS-011 | GET /api/v1/ass/familias | Média | familias | CAP-ASS-001 |
| RF-ASS-012 | POST /api/v1/ass/familias | Alta | familias | CAP-ASS-001 |
| RF-ASS-013 | GET /api/v1/ass/familias/nis/{nis} | Média | familias | CAP-ASS-001 |
| RF-ASS-014 | DELETE /api/v1/ass/familias/{familia_id} | Alta | familias | CAP-ASS-001 |
| RF-ASS-015 | GET /api/v1/ass/familias/{familia_id} | Média | familias | CAP-ASS-001 |
| RF-ASS-016 | PATCH /api/v1/ass/familias/{familia_id} | Média | familias | CAP-ASS-001 |
| RF-ASS-017 | GET /api/v1/ass/familias/{familia_id}/beneficios | Média | familias | CAP-ASS-001 |
| RF-ASS-018 | GET /api/v1/ass/familias/{familia_id}/pessoas | Média | familias | CAP-ASS-001 |
| RF-ASS-019 | GET /api/v1/ass/pessoas | Média | pessoas | CAP-ASS-001 |
| RF-ASS-020 | POST /api/v1/ass/pessoas | Alta | pessoas | CAP-ASS-001 |
| RF-ASS-021 | GET /api/v1/ass/pessoas/cpf/{cpf} | Média | pessoas | CAP-ASS-001 |
| RF-ASS-022 | DELETE /api/v1/ass/pessoas/{pessoa_id} | Alta | pessoas | CAP-ASS-001 |
| RF-ASS-023 | GET /api/v1/ass/pessoas/{pessoa_id} | Média | pessoas | CAP-ASS-001 |
| RF-ASS-024 | PATCH /api/v1/ass/pessoas/{pessoa_id} | Média | pessoas | CAP-ASS-001 |
| RF-ASS-025 | GET /api/v1/ass/pessoas/{pessoa_id}/atendimentos | Média | pessoas | CAP-ASS-001 |
| RF-ASS-026 | GET /api/v1/ass/unidades | Média | unidades | CAP-ASS-001 |
| RF-ASS-027 | POST /api/v1/ass/unidades | Alta | unidades | CAP-ASS-001 |
| RF-ASS-028 | DELETE /api/v1/ass/unidades/{unidade_id} | Alta | unidades | CAP-ASS-001 |
| RF-ASS-029 | GET /api/v1/ass/unidades/{unidade_id} | Média | unidades | CAP-ASS-001 |
| RF-ASS-030 | PATCH /api/v1/ass/unidades/{unidade_id} | Média | unidades | CAP-ASS-001 |
| RF-ASS-031 | GET /api/v1/ass/unidades/{unidade_id}/atendimentos | Média | unidades | CAP-ASS-001 |

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

**Documento:** 008-Assistencia-Social-Requisitos-Funcionais.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
