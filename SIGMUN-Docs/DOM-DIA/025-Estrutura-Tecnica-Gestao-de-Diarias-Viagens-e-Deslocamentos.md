# 025 – Estrutura-Tecnica – Gestão de Diárias, Viagens e Deslocamentos

#### Estrutura-Tecnica – Gestão de Diárias, Viagens e Deslocamentos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-DIA-025

**Domínio:** Gestão de Diárias, Viagens e Deslocamentos

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`
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

Este artefato detalha **a estrutura técnica** do domínio Gestão de Diárias, Viagens e Deslocamentos (`DOM-DIA`), com base na implementação material identificada em `src/modules/sigmun_dia` e no conteúdo de negócio declarado no gerador.

---

# 2. Módulo `sigmun_dia`

| Arquivo | Linhas |
| --- | --- |
| `src/modules/sigmun_dia/__init__.py` | 11 |
| `src/modules/sigmun_dia/application/__init__.py` | 1 |
| `src/modules/sigmun_dia/application/interfaces/__init__.py` | 101 |
| `src/modules/sigmun_dia/application/interfaces/repositories.py` | 137 |
| `src/modules/sigmun_dia/application/use_cases/__init__.py` | 778 |
| `src/modules/sigmun_dia/application/use_cases/aprovar_prestacao_use_case.py` | 79 |
| `src/modules/sigmun_dia/application/use_cases/criar_diaria_use_case.py` | 112 |
| `src/modules/sigmun_dia/application/use_cases/criar_prestacao_use_case.py` | 93 |
| `src/modules/sigmun_dia/application/use_cases/glosar_prestacao_use_case.py` | 97 |
| `src/modules/sigmun_dia/application/use_cases/restituir_prestacao_use_case.py` | 85 |
| `src/modules/sigmun_dia/domain/__init__.py` | 1 |
| `src/modules/sigmun_dia/domain/entities/__init__.py` | 459 |
| `src/modules/sigmun_dia/domain/events/__init__.py` | 1 |
| `src/modules/sigmun_dia/domain/exceptions.py` | 93 |
| `src/modules/sigmun_dia/domain/services/__init__.py` | 1 |
| `src/modules/sigmun_dia/domain/value_objects/__init__.py` | 1 |
| `src/modules/sigmun_dia/infrastructure/__init__.py` | 1 |
| `src/modules/sigmun_dia/infrastructure/database/__init__.py` | 1 |
| `src/modules/sigmun_dia/infrastructure/database/models.py` | 172 |
| `src/modules/sigmun_dia/infrastructure/database/seeds.py` | 71 |
| `src/modules/sigmun_dia/infrastructure/repositories/__init__.py` | 16 |
| `src/modules/sigmun_dia/infrastructure/repositories/sqlalchemy_diaria_repository.py` | 186 |
| `src/modules/sigmun_dia/infrastructure/repositories/sqlalchemy_prestacao_repository.py` | 116 |
| `src/modules/sigmun_dia/infrastructure/repositories/sqlalchemy_viagem_repository.py` | 118 |
| `src/modules/sigmun_dia/presentation/__init__.py` | 5 |
| `src/modules/sigmun_dia/presentation/api/__init__.py` | 616 |
| `src/modules/sigmun_dia/presentation/schemas/__init__.py` | 25 |
| `src/modules/sigmun_dia/presentation/schemas/dia_schemas.py` | 286 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 025-Gestao-de-Diarias-Viagens-e-Deslocamentos-Estrutura-Tecnica.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
