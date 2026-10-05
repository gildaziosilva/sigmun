# 008 – Requisitos-Funcionais – Dados Corporativos

#### Requisitos-Funcionais – Dados Corporativos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-DAD-008

**Domínio:** Dados Corporativos

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Dados-Corporativos.md`
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

Este artefato detalha **os requisitos funcionais** do domínio Dados Corporativos (`DOM-DAD`), com base na implementação material identificada em `src/modules/sigmun_dad` e no conteúdo de negócio declarado no gerador.

---

# 2. Requisitos

| ID | Requisito | Prioridade | Recurso | Capacidade |
| --- | --- | --- | --- | --- |
| RF-DAD-001 | GET /api/v1/dad/ativos | Média | ativos | CAP-DAD-001 |
| RF-DAD-002 | POST /api/v1/dad/ativos | Alta | ativos | CAP-DAD-001 |
| RF-DAD-003 | GET /api/v1/dad/ativos/{ativo_id} | Média | ativos | CAP-DAD-001 |
| RF-DAD-004 | POST /api/v1/dad/ativos/{ativo_id}/arquivar | Alta | ativos | CAP-DAD-001 |
| RF-DAD-005 | POST /api/v1/dad/ativos/{ativo_id}/ativar | Alta | ativos | CAP-DAD-001 |
| RF-DAD-006 | POST /api/v1/dad/ativos/{ativo_id}/desativar | Alta | ativos | CAP-DAD-001 |
| RF-DAD-007 | GET /api/v1/dad/catalogos | Média | catalogos | CAP-DAD-001 |
| RF-DAD-008 | POST /api/v1/dad/catalogos | Alta | catalogos | CAP-DAD-001 |
| RF-DAD-009 | DELETE /api/v1/dad/catalogos/{catalogo_id} | Alta | catalogos | CAP-DAD-001 |
| RF-DAD-010 | GET /api/v1/dad/catalogos/{catalogo_id} | Média | catalogos | CAP-DAD-001 |
| RF-DAD-011 | PATCH /api/v1/dad/catalogos/{catalogo_id} | Média | catalogos | CAP-DAD-001 |
| RF-DAD-012 | DELETE /api/v1/dad/catalogos/{catalogo_id}/ativos/{ativo_id} | Alta | catalogos | CAP-DAD-001 |
| RF-DAD-013 | POST /api/v1/dad/catalogos/{catalogo_id}/ativos/{ativo_id} | Alta | catalogos | CAP-DAD-001 |
| RF-DAD-014 | GET /api/v1/dad/linhagens | Média | linhagens | CAP-DAD-001 |
| RF-DAD-015 | POST /api/v1/dad/linhagens | Alta | linhagens | CAP-DAD-001 |
| RF-DAD-016 | DELETE /api/v1/dad/linhagens/{linhagem_id} | Alta | linhagens | CAP-DAD-001 |
| RF-DAD-017 | GET /api/v1/dad/linhagens/{linhagem_id} | Média | linhagens | CAP-DAD-001 |
| RF-DAD-018 | PATCH /api/v1/dad/linhagens/{linhagem_id} | Média | linhagens | CAP-DAD-001 |
| RF-DAD-019 | GET /api/v1/dad/politicas | Média | politicas | CAP-DAD-001 |
| RF-DAD-020 | POST /api/v1/dad/politicas | Alta | politicas | CAP-DAD-001 |
| RF-DAD-021 | DELETE /api/v1/dad/politicas/{politica_id} | Alta | politicas | CAP-DAD-001 |
| RF-DAD-022 | GET /api/v1/dad/politicas/{politica_id} | Média | politicas | CAP-DAD-001 |
| RF-DAD-023 | PATCH /api/v1/dad/politicas/{politica_id} | Média | politicas | CAP-DAD-001 |
| RF-DAD-024 | POST /api/v1/dad/politicas/{politica_id}/regras | Alta | politicas | CAP-DAD-001 |
| RF-DAD-025 | GET /api/v1/dad/qualidade | Média | qualidade | CAP-DAD-001 |
| RF-DAD-026 | POST /api/v1/dad/qualidade | Alta | qualidade | CAP-DAD-001 |
| RF-DAD-027 | DELETE /api/v1/dad/qualidade/{qualidade_id} | Alta | qualidade | CAP-DAD-001 |
| RF-DAD-028 | GET /api/v1/dad/qualidade/{qualidade_id} | Média | qualidade | CAP-DAD-001 |
| RF-DAD-029 | PATCH /api/v1/dad/qualidade/{qualidade_id} | Média | qualidade | CAP-DAD-001 |

---

# 3. Cobertura

Operações publicadas: **29**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 008-Dados-Corporativos-Requisitos-Funcionais.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
