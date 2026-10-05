# 008 – Requisitos-Funcionais – Metadados Corporativos

#### Requisitos-Funcionais – Metadados Corporativos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-MET-008

**Domínio:** Metadados Corporativos

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Metadados-Corporativos.md`
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

Este artefato detalha **os requisitos funcionais** do domínio Metadados Corporativos (`DOM-MET`), com base na implementação material identificada em `src/modules/sigmun_met` e no conteúdo de negócio declarado no gerador.

---

# 2. Requisitos

| ID | Requisito | Prioridade | Recurso | Capacidade |
| --- | --- | --- | --- | --- |
| RF-MET-001 | GET /api/v1/met/classificacoes | Média | classificacoes | CAP-MET-001 |
| RF-MET-002 | POST /api/v1/met/classificacoes | Alta | classificacoes | CAP-MET-001 |
| RF-MET-003 | DELETE /api/v1/met/classificacoes/{classificacao_id} | Alta | classificacoes | CAP-MET-001 |
| RF-MET-004 | GET /api/v1/met/classificacoes/{classificacao_id} | Média | classificacoes | CAP-MET-001 |
| RF-MET-005 | PUT /api/v1/met/classificacoes/{classificacao_id} | Média | classificacoes | CAP-MET-001 |
| RF-MET-006 | GET /api/v1/met/entidades/{entidade_tipo}/{entidade_id}/valores | Média | entidades | CAP-MET-001 |
| RF-MET-007 | GET /api/v1/met/metadados | Média | metadados | CAP-MET-001 |
| RF-MET-008 | POST /api/v1/met/metadados | Alta | metadados | CAP-MET-001 |
| RF-MET-009 | DELETE /api/v1/met/metadados/{metadado_id} | Alta | metadados | CAP-MET-001 |
| RF-MET-010 | GET /api/v1/met/metadados/{metadado_id} | Média | metadados | CAP-MET-001 |
| RF-MET-011 | PUT /api/v1/met/metadados/{metadado_id} | Média | metadados | CAP-MET-001 |
| RF-MET-012 | POST /api/v1/met/metadados/{metadado_id}/ativar | Alta | metadados | CAP-MET-001 |
| RF-MET-013 | POST /api/v1/met/metadados/{metadado_id}/desativar | Alta | metadados | CAP-MET-001 |
| RF-MET-014 | GET /api/v1/met/taxonomias | Média | taxonomias | CAP-MET-001 |
| RF-MET-015 | POST /api/v1/met/taxonomias | Alta | taxonomias | CAP-MET-001 |
| RF-MET-016 | DELETE /api/v1/met/taxonomias/{taxonomia_id} | Alta | taxonomias | CAP-MET-001 |
| RF-MET-017 | GET /api/v1/met/taxonomias/{taxonomia_id} | Média | taxonomias | CAP-MET-001 |
| RF-MET-018 | PUT /api/v1/met/taxonomias/{taxonomia_id} | Média | taxonomias | CAP-MET-001 |
| RF-MET-019 | GET /api/v1/met/taxonomias/{taxonomia_id}/termos | Média | taxonomias | CAP-MET-001 |
| RF-MET-020 | GET /api/v1/met/termos | Média | termos | CAP-MET-001 |
| RF-MET-021 | POST /api/v1/met/termos | Alta | termos | CAP-MET-001 |
| RF-MET-022 | DELETE /api/v1/met/termos/{termo_id} | Alta | termos | CAP-MET-001 |
| RF-MET-023 | GET /api/v1/met/termos/{termo_id} | Média | termos | CAP-MET-001 |
| RF-MET-024 | PUT /api/v1/met/termos/{termo_id} | Média | termos | CAP-MET-001 |
| RF-MET-025 | GET /api/v1/met/termos/{termo_id}/filhos | Média | termos | CAP-MET-001 |
| RF-MET-026 | GET /api/v1/met/valores | Média | valores | CAP-MET-001 |
| RF-MET-027 | POST /api/v1/met/valores | Alta | valores | CAP-MET-001 |
| RF-MET-028 | DELETE /api/v1/met/valores/{valor_id} | Alta | valores | CAP-MET-001 |
| RF-MET-029 | GET /api/v1/met/valores/{valor_id} | Média | valores | CAP-MET-001 |
| RF-MET-030 | PUT /api/v1/met/valores/{valor_id} | Média | valores | CAP-MET-001 |

---

# 3. Cobertura

Operações publicadas: **30**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 008-Metadados-Corporativos-Requisitos-Funcionais.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
