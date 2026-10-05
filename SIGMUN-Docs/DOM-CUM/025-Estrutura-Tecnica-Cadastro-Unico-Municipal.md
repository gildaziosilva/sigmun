# 025 – Estrutura-Tecnica – Cadastro Único Municipal

#### Estrutura-Tecnica – Cadastro Único Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CUM-025

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

Este artefato detalha **a estrutura técnica** do domínio Cadastro Único Municipal (`DOM-CUM`), com base na implementação material identificada em `src/modules/sigmun_cadastro` e no conteúdo de negócio declarado no gerador.

---

# 2. Módulo `sigmun_cadastro`

| Arquivo | Linhas |
| --- | --- |
| `src/modules/sigmun_cadastro/__init__.py` | 1 |
| `src/modules/sigmun_cadastro/application/__init__.py` | 1 |
| `src/modules/sigmun_cadastro/application/commands/__init__.py` | 31 |
| `src/modules/sigmun_cadastro/application/commands/pessoa_commands.py` | 177 |
| `src/modules/sigmun_cadastro/application/commands/unidade_commands.py` | 42 |
| `src/modules/sigmun_cadastro/application/queries/__init__.py` | 17 |
| `src/modules/sigmun_cadastro/application/queries/pessoa_queries.py` | 30 |
| `src/modules/sigmun_cadastro/application/queries/unidade_queries.py` | 26 |
| `src/modules/sigmun_cadastro/application/use_cases/__init__.py` | 49 |
| `src/modules/sigmun_cadastro/application/use_cases/adicionar_contato.py` | 40 |
| `src/modules/sigmun_cadastro/application/use_cases/adicionar_documento.py` | 68 |
| `src/modules/sigmun_cadastro/application/use_cases/adicionar_endereco.py` | 51 |
| `src/modules/sigmun_cadastro/application/use_cases/atualizar_pessoa.py` | 106 |
| `src/modules/sigmun_cadastro/application/use_cases/atualizar_unidade.py` | 97 |
| `src/modules/sigmun_cadastro/application/use_cases/consultar_pessoa.py` | 32 |
| `src/modules/sigmun_cadastro/application/use_cases/consultar_unidade.py` | 38 |
| `src/modules/sigmun_cadastro/application/use_cases/excluir_pessoa.py` | 49 |
| `src/modules/sigmun_cadastro/application/use_cases/excluir_unidade.py` | 67 |
| `src/modules/sigmun_cadastro/application/use_cases/listar_pessoas.py` | 34 |
| `src/modules/sigmun_cadastro/application/use_cases/listar_unidades.py` | 34 |
| `src/modules/sigmun_cadastro/application/use_cases/registrar_pessoa.py` | 109 |
| `src/modules/sigmun_cadastro/application/use_cases/registrar_unidade.py` | 79 |
| `src/modules/sigmun_cadastro/application/use_cases/revisar_cadastral.py` | 68 |
| `src/modules/sigmun_cadastro/domain/__init__.py` | 8 |
| `src/modules/sigmun_cadastro/domain/entities/__init__.py` | 32 |
| `src/modules/sigmun_cadastro/domain/entities/contato.py` | 70 |
| `src/modules/sigmun_cadastro/domain/entities/documento.py` | 89 |
| `src/modules/sigmun_cadastro/domain/entities/endereco.py` | 106 |
| `src/modules/sigmun_cadastro/domain/entities/pessoa.py` | 372 |
| `src/modules/sigmun_cadastro/domain/entities/unidade_administrativa.py` | 99 |
| `src/modules/sigmun_cadastro/domain/events/__init__.py` | 30 |
| `src/modules/sigmun_cadastro/domain/events/pessoa_events.py` | 104 |
| `src/modules/sigmun_cadastro/domain/events/unidade_events.py` | 47 |
| `src/modules/sigmun_cadastro/domain/exceptions.py` | 62 |
| `src/modules/sigmun_cadastro/domain/repositories/__init__.py` | 10 |
| `src/modules/sigmun_cadastro/domain/repositories/pessoa_repository.py` | 57 |
| `src/modules/sigmun_cadastro/domain/repositories/unidade_administrativa_repository.py` | 65 |
| `src/modules/sigmun_cadastro/domain/services/__init__.py` | 1 |
| `src/modules/sigmun_cadastro/domain/value_objects/__init__.py` | 6 |
| `src/modules/sigmun_cadastro/domain/value_objects/cnpj.py` | 61 |
| `src/modules/sigmun_cadastro/domain/value_objects/cpf.py` | 61 |
| `src/modules/sigmun_cadastro/infrastructure/__init__.py` | 1 |
| `src/modules/sigmun_cadastro/infrastructure/database/__init__.py` | 23 |
| `src/modules/sigmun_cadastro/infrastructure/database/models.py` | 179 |
| `src/modules/sigmun_cadastro/infrastructure/integrations/__init__.py` | 1 |
| `src/modules/sigmun_cadastro/infrastructure/repositories/__init__.py` | 13 |
| `src/modules/sigmun_cadastro/infrastructure/repositories/sqlalchemy_pessoa_repository.py` | 542 |
| `src/modules/sigmun_cadastro/infrastructure/repositories/sqlalchemy_unidade_administrativa_repository.py` | 228 |
| `src/modules/sigmun_cadastro/presentation/__init__.py` | 1 |
| `src/modules/sigmun_cadastro/presentation/api/__init__.py` | 1 |
| `src/modules/sigmun_cadastro/presentation/api/pessoas_router.py` | 482 |
| `src/modules/sigmun_cadastro/presentation/api/unidades_router.py` | 127 |
| `src/modules/sigmun_cadastro/presentation/schemas/__init__.py` | 51 |
| `src/modules/sigmun_cadastro/presentation/schemas/pessoa_schemas.py` | 263 |
| `src/modules/sigmun_cadastro/presentation/schemas/unidade_schemas.py` | 76 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 025-Cadastro-Unico-Municipal-Estrutura-Tecnica.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
