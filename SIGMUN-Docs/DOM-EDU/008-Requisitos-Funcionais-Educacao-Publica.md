# 008 – Requisitos-Funcionais – Educação Pública

#### Requisitos-Funcionais – Educação Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-EDU-008

**Domínio:** Educação Pública

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Educacao-Publica.md`
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

Este artefato detalha **os requisitos funcionais** do domínio Educação Pública (`DOM-EDU`), com base na implementação material identificada em `src/modules/sigmun_educacao` e no conteúdo de negócio declarado no gerador.

---

# 2. Requisitos

| ID | Requisito | Prioridade | Recurso | Capacidade |
| --- | --- | --- | --- | --- |
| RF-EDU-001 | GET /api/v1/edu/alunos | Média | alunos | CAP-EDU-001 |
| RF-EDU-002 | POST /api/v1/edu/alunos | Alta | alunos | CAP-EDU-001 |
| RF-EDU-003 | GET /api/v1/edu/alunos/{aluno_id} | Média | alunos | CAP-EDU-001 |
| RF-EDU-004 | PATCH /api/v1/edu/alunos/{aluno_id} | Média | alunos | CAP-EDU-001 |
| RF-EDU-005 | GET /api/v1/edu/diario | Média | diario | CAP-EDU-001 |
| RF-EDU-006 | POST /api/v1/edu/diario | Alta | diario | CAP-EDU-001 |
| RF-EDU-007 | GET /api/v1/edu/matriculas | Média | matriculas | CAP-EDU-001 |
| RF-EDU-008 | POST /api/v1/edu/matriculas | Alta | matriculas | CAP-EDU-001 |
| RF-EDU-009 | GET /api/v1/edu/matriculas/{matricula_id} | Média | matriculas | CAP-EDU-001 |
| RF-EDU-010 | POST /api/v1/edu/matriculas/{matricula_id}/cancelar | Alta | matriculas | CAP-EDU-001 |
| RF-EDU-011 | POST /api/v1/edu/matriculas/{matricula_id}/concluir | Alta | matriculas | CAP-EDU-001 |
| RF-EDU-012 | POST /api/v1/edu/matriculas/{matricula_id}/transferir | Alta | matriculas | CAP-EDU-001 |
| RF-EDU-013 | GET /api/v1/edu/merenda/distribuicoes | Média | merenda | CAP-EDU-001 |
| RF-EDU-014 | POST /api/v1/edu/merenda/distribuicoes | Alta | merenda | CAP-EDU-001 |
| RF-EDU-015 | GET /api/v1/edu/merenda/itens | Média | merenda | CAP-EDU-001 |
| RF-EDU-016 | POST /api/v1/edu/merenda/itens | Alta | merenda | CAP-EDU-001 |
| RF-EDU-017 | GET /api/v1/edu/merenda/itens/{item_id} | Média | merenda | CAP-EDU-001 |
| RF-EDU-018 | POST /api/v1/edu/merenda/itens/{item_id}/repor | Alta | merenda | CAP-EDU-001 |
| RF-EDU-019 | GET /api/v1/edu/transporte/passagens | Média | transporte | CAP-EDU-001 |
| RF-EDU-020 | POST /api/v1/edu/transporte/passagens | Alta | transporte | CAP-EDU-001 |
| RF-EDU-021 | GET /api/v1/edu/transporte/rotas | Média | transporte | CAP-EDU-001 |
| RF-EDU-022 | POST /api/v1/edu/transporte/rotas | Alta | transporte | CAP-EDU-001 |
| RF-EDU-023 | GET /api/v1/edu/transporte/rotas/{rota_id} | Média | transporte | CAP-EDU-001 |
| RF-EDU-024 | POST /api/v1/edu/transporte/rotas/{rota_id}/ativar | Alta | transporte | CAP-EDU-001 |
| RF-EDU-025 | POST /api/v1/edu/transporte/rotas/{rota_id}/inativar | Alta | transporte | CAP-EDU-001 |

---

# 3. Cobertura

Operações publicadas: **25**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 008-Educacao-Publica-Requisitos-Funcionais.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
