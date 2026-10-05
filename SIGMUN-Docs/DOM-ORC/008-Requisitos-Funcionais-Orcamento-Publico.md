# 008 – Requisitos-Funcionais – Orçamento Público

#### Requisitos-Funcionais – Orçamento Público

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ORC-008

**Domínio:** Orçamento Público

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Orcamento-Publico.md`
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

Este artefato detalha **os requisitos funcionais** do domínio Orçamento Público (`DOM-ORC`), com base na implementação material identificada em `src/modules/sigmun_orc` e no conteúdo de negócio declarado no gerador.

---

# 2. Requisitos

| ID | Requisito | Prioridade | Recurso | Capacidade |
| --- | --- | --- | --- | --- |
| RF-ORC-001 | POST /api/v1/orc/dotacoes | Alta | dotacoes | CAP-ORC-001 |
| RF-ORC-002 | POST /api/v1/orc/dotacoes/{dotacao_id}/anular | Alta | dotacoes | CAP-ORC-001 |
| RF-ORC-003 | GET /api/v1/orc/dotacoes/{dotacao_id}/saldo | Média | dotacoes | CAP-ORC-001 |
| RF-ORC-004 | POST /api/v1/orc/dotacoes/{dotacao_id}/suplementar | Alta | dotacoes | CAP-ORC-001 |
| RF-ORC-005 | POST /api/v1/orc/ldos | Alta | ldos | CAP-ORC-001 |
| RF-ORC-006 | POST /api/v1/orc/ldos/{ldo_id}/sancionar | Alta | ldos | CAP-ORC-001 |
| RF-ORC-007 | POST /api/v1/orc/loas | Alta | loas | CAP-ORC-001 |
| RF-ORC-008 | POST /api/v1/orc/loas/{loa_id}/publicar | Alta | loas | CAP-ORC-001 |
| RF-ORC-009 | POST /api/v1/orc/ppas | Alta | ppas | CAP-ORC-001 |
| RF-ORC-010 | POST /api/v1/orc/ppas/{ppa_id}/publicar | Alta | ppas | CAP-ORC-001 |
| RF-ORC-011 | POST /api/v1/orc/reservas | Alta | reservas | CAP-ORC-001 |
| RF-ORC-012 | POST /api/v1/orc/reservas/{reserva_id}/cancelar | Alta | reservas | CAP-ORC-001 |

---

# 3. Cobertura

Operações publicadas: **12**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 008-Orcamento-Publico-Requisitos-Funcionais.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
