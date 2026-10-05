# 008 – Requisitos-Funcionais – Cadastro Único Municipal

#### Requisitos-Funcionais – Cadastro Único Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CUM-008

**Domínio:** Cadastro Único Municipal

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Cadastro-Unico-Municipal.md`
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

Este artefato detalha **os requisitos funcionais** do domínio Cadastro Único Municipal (`DOM-CUM`), com base na implementação material identificada em `src/modules/sigmun_cadastro` e no conteúdo de negócio declarado no gerador.

---

# 2. Requisitos

| ID | Requisito | Prioridade | Recurso | Capacidade |
| --- | --- | --- | --- | --- |
| RF-CUM-001 | GET /api/v1/cadastro/pessoas | Média | pessoas | CAP-CUM-001 |
| RF-CUM-002 | POST /api/v1/cadastro/pessoas | Alta | pessoas | CAP-CUM-001 |
| RF-CUM-003 | DELETE /api/v1/cadastro/pessoas/{pessoa_id} | Alta | pessoas | CAP-CUM-001 |
| RF-CUM-004 | GET /api/v1/cadastro/pessoas/{pessoa_id} | Média | pessoas | CAP-CUM-001 |
| RF-CUM-005 | PATCH /api/v1/cadastro/pessoas/{pessoa_id}/categoria | Média | pessoas | CAP-CUM-001 |
| RF-CUM-006 | POST /api/v1/cadastro/pessoas/{pessoa_id}/contatos | Alta | pessoas | CAP-CUM-001 |
| RF-CUM-007 | PATCH /api/v1/cadastro/pessoas/{pessoa_id}/dados-fisicos | Média | pessoas | CAP-CUM-001 |
| RF-CUM-008 | PATCH /api/v1/cadastro/pessoas/{pessoa_id}/dados-juridicos | Média | pessoas | CAP-CUM-001 |
| RF-CUM-009 | POST /api/v1/cadastro/pessoas/{pessoa_id}/documentos | Alta | pessoas | CAP-CUM-001 |
| RF-CUM-010 | POST /api/v1/cadastro/pessoas/{pessoa_id}/enderecos | Alta | pessoas | CAP-CUM-001 |
| RF-CUM-011 | GET /api/v1/cadastro/unidades-administrativas | Média | unidades-administrativas | CAP-CUM-001 |
| RF-CUM-012 | POST /api/v1/cadastro/unidades-administrativas | Alta | unidades-administrativas | CAP-CUM-001 |

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

**Documento:** 008-Cadastro-Unico-Municipal-Requisitos-Funcionais.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
