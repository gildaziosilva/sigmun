# 008 – Requisitos-Funcionais – Gestão de Frota

#### Requisitos-Funcionais – Gestão de Frota

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-FRO-008

**Domínio:** Gestão de Frota

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-de-Frota.md`
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

Este artefato detalha **os requisitos funcionais** do domínio Gestão de Frota (`DOM-FRO`), com base na implementação material identificada em `src/modules/sigmun_frotas` e no conteúdo de negócio declarado no gerador.

---

# 2. Requisitos

| ID | Requisito | Prioridade | Recurso | Capacidade |
| --- | --- | --- | --- | --- |
| RF-FRO-001 | GET /api/v1/fro/abastecimentos | Média | abastecimentos | CAP-FRO-001 |
| RF-FRO-002 | GET /api/v1/fro/manutencoes | Média | manutencoes | CAP-FRO-001 |
| RF-FRO-003 | POST /api/v1/fro/manutencoes/{manutencao_id}/concluir | Alta | manutencoes | CAP-FRO-001 |
| RF-FRO-004 | GET /api/v1/fro/rotas | Média | rotas | CAP-FRO-001 |
| RF-FRO-005 | POST /api/v1/fro/rotas/{rota_id}/concluir | Alta | rotas | CAP-FRO-001 |
| RF-FRO-006 | GET /api/v1/fro/veiculos | Média | veiculos | CAP-FRO-001 |
| RF-FRO-007 | POST /api/v1/fro/veiculos | Alta | veiculos | CAP-FRO-001 |
| RF-FRO-008 | GET /api/v1/fro/veiculos/{veiculo_id} | Média | veiculos | CAP-FRO-001 |
| RF-FRO-009 | GET /api/v1/fro/veiculos/{veiculo_id}/abastecimentos | Média | veiculos | CAP-FRO-001 |
| RF-FRO-010 | POST /api/v1/fro/veiculos/{veiculo_id}/abastecimentos | Alta | veiculos | CAP-FRO-001 |
| RF-FRO-011 | POST /api/v1/fro/veiculos/{veiculo_id}/baixar | Alta | veiculos | CAP-FRO-001 |
| RF-FRO-012 | POST /api/v1/fro/veiculos/{veiculo_id}/manutencoes | Alta | veiculos | CAP-FRO-001 |
| RF-FRO-013 | POST /api/v1/fro/veiculos/{veiculo_id}/rotas | Alta | veiculos | CAP-FRO-001 |

---

# 3. Cobertura

Operações publicadas: **13**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 008-Gestao-de-Frota-Requisitos-Funcionais.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
