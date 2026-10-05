# 025 – Estrutura-Tecnica – Educação Pública

#### Estrutura-Tecnica – Educação Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-EDU-025

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

Este artefato detalha **a estrutura técnica** do domínio Educação Pública (`DOM-EDU`), com base na implementação material identificada em `src/modules/sigmun_educacao` e no conteúdo de negócio declarado no gerador.

---

# 2. Módulo `sigmun_educacao`

| Arquivo | Linhas |
| --- | --- |
| `src/modules/sigmun_educacao/__init__.py` | 1 |
| `src/modules/sigmun_educacao/application/interfaces.py` | 152 |
| `src/modules/sigmun_educacao/application/use_cases.py` | 469 |
| `src/modules/sigmun_educacao/domain/entities/__init__.py` | 21 |
| `src/modules/sigmun_educacao/domain/entities/aluno.py` | 82 |
| `src/modules/sigmun_educacao/domain/entities/diario.py` | 41 |
| `src/modules/sigmun_educacao/domain/entities/matricula.py` | 100 |
| `src/modules/sigmun_educacao/domain/entities/merenda.py` | 93 |
| `src/modules/sigmun_educacao/domain/entities/transporte.py` | 95 |
| `src/modules/sigmun_educacao/domain/events/__init__.py` | 1 |
| `src/modules/sigmun_educacao/domain/exceptions.py` | 92 |
| `src/modules/sigmun_educacao/domain/services/__init__.py` | 1 |
| `src/modules/sigmun_educacao/domain/value_objects/__init__.py` | 1 |
| `src/modules/sigmun_educacao/infrastructure/database/__init__.py` | 1 |
| `src/modules/sigmun_educacao/infrastructure/database/models.py` | 147 |
| `src/modules/sigmun_educacao/infrastructure/integrations/__init__.py` | 1 |
| `src/modules/sigmun_educacao/infrastructure/repositories/__init__.py` | 1 |
| `src/modules/sigmun_educacao/infrastructure/repositories/sqlalchemy_aluno_repository.py` | 60 |
| `src/modules/sigmun_educacao/infrastructure/repositories/sqlalchemy_edu_repository.py` | 141 |
| `src/modules/sigmun_educacao/presentation/api/__init__.py` | 4 |
| `src/modules/sigmun_educacao/presentation/api/endpoints.py` | 278 |
| `src/modules/sigmun_educacao/presentation/schemas/__init__.py` | 1 |
| `src/modules/sigmun_educacao/presentation/schemas/edu_schemas.py` | 94 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 025-Educacao-Publica-Estrutura-Tecnica.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
