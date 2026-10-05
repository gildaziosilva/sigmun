# 025 – Estrutura-Tecnica – Gestão Patrimonial

#### Estrutura-Tecnica – Gestão Patrimonial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-PAT-025

**Domínio:** Gestão Patrimonial

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-Patrimonial.md`
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

Este artefato detalha **a estrutura técnica** do domínio Gestão Patrimonial (`DOM-PAT`), com base na implementação material identificada em `src/modules/sigmun_patrimonio` e no conteúdo de negócio declarado no gerador.

---

# 2. Módulo `sigmun_patrimonio`

| Arquivo | Linhas |
| --- | --- |
| `src/modules/sigmun_patrimonio/__init__.py` | 1 |
| `src/modules/sigmun_patrimonio/application/commands/__init__.py` | 1 |
| `src/modules/sigmun_patrimonio/application/interfaces.py` | 56 |
| `src/modules/sigmun_patrimonio/application/queries/__init__.py` | 1 |
| `src/modules/sigmun_patrimonio/application/use_cases.py` | 213 |
| `src/modules/sigmun_patrimonio/domain/entities/__init__.py` | 1 |
| `src/modules/sigmun_patrimonio/domain/entities/bem.py` | 119 |
| `src/modules/sigmun_patrimonio/domain/entities/depreciacao.py` | 33 |
| `src/modules/sigmun_patrimonio/domain/entities/transferencia.py` | 65 |
| `src/modules/sigmun_patrimonio/domain/events/__init__.py` | 1 |
| `src/modules/sigmun_patrimonio/domain/exceptions.py` | 50 |
| `src/modules/sigmun_patrimonio/domain/services/__init__.py` | 1 |
| `src/modules/sigmun_patrimonio/domain/value_objects/__init__.py` | 1 |
| `src/modules/sigmun_patrimonio/infrastructure/database/__init__.py` | 1 |
| `src/modules/sigmun_patrimonio/infrastructure/database/models.py` | 75 |
| `src/modules/sigmun_patrimonio/infrastructure/integrations/__init__.py` | 1 |
| `src/modules/sigmun_patrimonio/infrastructure/repositories/__init__.py` | 1 |
| `src/modules/sigmun_patrimonio/infrastructure/repositories/sqlalchemy_bem_repository.py` | 115 |
| `src/modules/sigmun_patrimonio/infrastructure/repositories/sqlalchemy_depreciacao_transferencia_repository.py` | 129 |
| `src/modules/sigmun_patrimonio/presentation/api/__init__.py` | 6 |
| `src/modules/sigmun_patrimonio/presentation/api/endpoints.py` | 229 |
| `src/modules/sigmun_patrimonio/presentation/schemas/__init__.py` | 1 |
| `src/modules/sigmun_patrimonio/presentation/schemas/pat_schemas.py` | 100 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 025-Gestao-Patrimonial-Estrutura-Tecnica.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
