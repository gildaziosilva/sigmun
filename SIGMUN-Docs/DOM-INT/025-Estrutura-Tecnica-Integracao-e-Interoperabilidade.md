# 025 – Estrutura-Tecnica – Integração e Interoperabilidade

#### Estrutura-Tecnica – Integração e Interoperabilidade

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-INT-025

**Domínio:** Integração e Interoperabilidade

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Integracao-e-Interoperabilidade.md`
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

Este artefato detalha **a estrutura técnica** do domínio Integração e Interoperabilidade (`DOM-INT`), com base na implementação material identificada em `src/modules/sigmun_int` e no conteúdo de negócio declarado no gerador.

---

# 2. Módulo `sigmun_int`

| Arquivo | Linhas |
| --- | --- |
| `src/modules/sigmun_int/__init__.py` | 1 |
| `src/modules/sigmun_int/application/__init__.py` | 1 |
| `src/modules/sigmun_int/application/interfaces/__init__.py` | 303 |
| `src/modules/sigmun_int/application/use_cases/__init__.py` | 70 |
| `src/modules/sigmun_int/application/use_cases/api_use_cases.py` | 169 |
| `src/modules/sigmun_int/application/use_cases/bus_use_cases.py` | 172 |
| `src/modules/sigmun_int/application/use_cases/conector_use_cases.py` | 229 |
| `src/modules/sigmun_int/application/use_cases/contrato_use_cases.py` | 181 |
| `src/modules/sigmun_int/application/use_cases/entrega_use_cases.py` | 97 |
| `src/modules/sigmun_int/application/use_cases/webhook_use_cases.py` | 165 |
| `src/modules/sigmun_int/domain/__init__.py` | 1 |
| `src/modules/sigmun_int/domain/entities/__init__.py` | 332 |
| `src/modules/sigmun_int/domain/events/__init__.py` | 74 |
| `src/modules/sigmun_int/domain/exceptions.py` | 84 |
| `src/modules/sigmun_int/domain/value_objects/__init__.py` | 75 |
| `src/modules/sigmun_int/infrastructure/__init__.py` | 1 |
| `src/modules/sigmun_int/infrastructure/database/__init__.py` | 1 |
| `src/modules/sigmun_int/infrastructure/database/models.py` | 213 |
| `src/modules/sigmun_int/infrastructure/database/seeds.py` | 57 |
| `src/modules/sigmun_int/infrastructure/messaging/__init__.py` | 6 |
| `src/modules/sigmun_int/infrastructure/messaging/despachador_webhooks.py` | 57 |
| `src/modules/sigmun_int/infrastructure/messaging/outbox_source.py` | 74 |
| `src/modules/sigmun_int/infrastructure/repositories/__init__.py` | 17 |
| `src/modules/sigmun_int/infrastructure/repositories/sqlalchemy_api_externa_repository.py` | 134 |
| `src/modules/sigmun_int/infrastructure/repositories/sqlalchemy_conector_repository.py` | 108 |
| `src/modules/sigmun_int/infrastructure/repositories/sqlalchemy_contrato_repository.py` | 119 |
| `src/modules/sigmun_int/infrastructure/repositories/sqlalchemy_entrega_repository.py` | 158 |
| `src/modules/sigmun_int/infrastructure/repositories/sqlalchemy_evento_processado_repository.py` | 100 |
| `src/modules/sigmun_int/infrastructure/repositories/sqlalchemy_webhook_repository.py` | 119 |
| `src/modules/sigmun_int/presentation/api/__init__.py` | 887 |
| `src/modules/sigmun_int/presentation/schemas/__init__.py` | 33 |
| `src/modules/sigmun_int/presentation/schemas/api_schemas.py` | 45 |
| `src/modules/sigmun_int/presentation/schemas/conector_schemas.py` | 44 |
| `src/modules/sigmun_int/presentation/schemas/contrato_schemas.py` | 33 |
| `src/modules/sigmun_int/presentation/schemas/entrega_schemas.py` | 70 |
| `src/modules/sigmun_int/presentation/schemas/webhook_schemas.py` | 42 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 025-Integracao-e-Interoperabilidade-Estrutura-Tecnica.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
