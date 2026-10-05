# 025 – Estrutura-Tecnica – Orçamento Público

#### Estrutura-Tecnica – Orçamento Público

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ORC-025

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

Este artefato detalha **a estrutura técnica** do domínio Orçamento Público (`DOM-ORC`), com base na implementação material identificada em `src/modules/sigmun_orc` e no conteúdo de negócio declarado no gerador.

---

# 2. Módulo `sigmun_orc`

| Arquivo | Linhas |
| --- | --- |
| `src/modules/sigmun_orc/application/interfaces.py` | 90 |
| `src/modules/sigmun_orc/application/use_cases_dotacao.py` | 154 |
| `src/modules/sigmun_orc/application/use_cases_planejamento.py` | 181 |
| `src/modules/sigmun_orc/domain/entities/__init__.py` | 40 |
| `src/modules/sigmun_orc/domain/entities/dotacao.py` | 178 |
| `src/modules/sigmun_orc/domain/entities/ldo.py` | 94 |
| `src/modules/sigmun_orc/domain/entities/loa.py` | 100 |
| `src/modules/sigmun_orc/domain/entities/ppa.py` | 101 |
| `src/modules/sigmun_orc/domain/entities/reserva.py` | 99 |
| `src/modules/sigmun_orc/domain/exceptions.py` | 102 |
| `src/modules/sigmun_orc/infrastructure/database/models.py` | 136 |
| `src/modules/sigmun_orc/infrastructure/repositories/sqlalchemy_dotacao_repository.py` | 79 |
| `src/modules/sigmun_orc/infrastructure/repositories/sqlalchemy_ldo_repository.py` | 70 |
| `src/modules/sigmun_orc/infrastructure/repositories/sqlalchemy_loa_repository.py` | 70 |
| `src/modules/sigmun_orc/infrastructure/repositories/sqlalchemy_ppa_repository.py` | 66 |
| `src/modules/sigmun_orc/infrastructure/repositories/sqlalchemy_reserva_repository.py` | 66 |
| `src/modules/sigmun_orc/presentation/api/__init__.py` | 7 |
| `src/modules/sigmun_orc/presentation/api/base.py` | 66 |
| `src/modules/sigmun_orc/presentation/api/dotacao_endpoints.py` | 126 |
| `src/modules/sigmun_orc/presentation/api/planejamento_endpoints.py` | 129 |
| `src/modules/sigmun_orc/presentation/schemas/orc_schemas.py` | 134 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 025-Orcamento-Publico-Estrutura-Tecnica.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
