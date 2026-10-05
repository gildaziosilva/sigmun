# 008 – Requisitos-Funcionais – Saúde Pública

#### Requisitos-Funcionais – Saúde Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-SAU-008

**Domínio:** Saúde Pública

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Saude-Publica.md`
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

Este artefato detalha **os requisitos funcionais** do domínio Saúde Pública (`DOM-SAU`), com base na implementação material identificada em `src/modules/sigmun_saude` e no conteúdo de negócio declarado no gerador.

---

# 2. Requisitos

| ID | Requisito | Prioridade | Recurso | Capacidade |
| --- | --- | --- | --- | --- |
| RF-SAU-001 | GET /api/v1/sau/agendamentos | Média | agendamentos | CAP-SAU-001 |
| RF-SAU-002 | POST /api/v1/sau/agendamentos | Alta | agendamentos | CAP-SAU-001 |
| RF-SAU-003 | POST /api/v1/sau/agendamentos/{agendamento_id}/cancelar | Alta | agendamentos | CAP-SAU-001 |
| RF-SAU-004 | POST /api/v1/sau/agendamentos/{agendamento_id}/confirmar | Alta | agendamentos | CAP-SAU-001 |
| RF-SAU-005 | POST /api/v1/sau/agendamentos/{agendamento_id}/realizar | Alta | agendamentos | CAP-SAU-001 |
| RF-SAU-006 | POST /api/v1/sau/atendimentos | Alta | atendimentos | CAP-SAU-001 |
| RF-SAU-007 | POST /api/v1/sau/dispensacoes | Alta | dispensacoes | CAP-SAU-001 |
| RF-SAU-008 | GET /api/v1/sau/medicamentos | Média | medicamentos | CAP-SAU-001 |
| RF-SAU-009 | POST /api/v1/sau/medicamentos | Alta | medicamentos | CAP-SAU-001 |
| RF-SAU-010 | POST /api/v1/sau/medicamentos/{medicamento_id}/repor | Alta | medicamentos | CAP-SAU-001 |
| RF-SAU-011 | GET /api/v1/sau/pacientes | Média | pacientes | CAP-SAU-001 |
| RF-SAU-012 | POST /api/v1/sau/pacientes | Alta | pacientes | CAP-SAU-001 |
| RF-SAU-013 | GET /api/v1/sau/pacientes/{paciente_id} | Média | pacientes | CAP-SAU-001 |
| RF-SAU-014 | GET /api/v1/sau/pacientes/{paciente_id}/prontuario | Média | pacientes | CAP-SAU-001 |
| RF-SAU-015 | GET /api/v1/sau/regulacoes | Média | regulacoes | CAP-SAU-001 |
| RF-SAU-016 | POST /api/v1/sau/regulacoes | Alta | regulacoes | CAP-SAU-001 |
| RF-SAU-017 | POST /api/v1/sau/regulacoes/{regulacao_id}/autorizar | Alta | regulacoes | CAP-SAU-001 |
| RF-SAU-018 | POST /api/v1/sau/regulacoes/{regulacao_id}/negar | Alta | regulacoes | CAP-SAU-001 |

---

# 3. Cobertura

Operações publicadas: **18**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 008-Saude-Publica-Requisitos-Funcionais.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
