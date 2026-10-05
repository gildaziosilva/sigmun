# 025 – Estrutura-Tecnica – Gestão de Frota

#### Estrutura-Tecnica – Gestão de Frota

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-FRO-025

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

Este artefato detalha **a estrutura técnica** do domínio Gestão de Frota (`DOM-FRO`), com base na implementação material identificada em `src/modules/sigmun_frotas` e no conteúdo de negócio declarado no gerador.

---

# 2. Módulo `sigmun_frotas`

| Arquivo | Linhas |
| --- | --- |
| `src/modules/sigmun_frotas/__init__.py` | 1 |
| `src/modules/sigmun_frotas/application/commands/__init__.py` | 1 |
| `src/modules/sigmun_frotas/application/interfaces.py` | 85 |
| `src/modules/sigmun_frotas/application/queries/__init__.py` | 1 |
| `src/modules/sigmun_frotas/application/use_cases.py` | 312 |
| `src/modules/sigmun_frotas/domain/entities/__init__.py` | 1 |
| `src/modules/sigmun_frotas/domain/entities/operacional.py` | 151 |
| `src/modules/sigmun_frotas/domain/entities/veiculo.py` | 124 |
| `src/modules/sigmun_frotas/domain/events/__init__.py` | 1 |
| `src/modules/sigmun_frotas/domain/exceptions.py` | 57 |
| `src/modules/sigmun_frotas/domain/services/__init__.py` | 1 |
| `src/modules/sigmun_frotas/domain/value_objects/__init__.py` | 1 |
| `src/modules/sigmun_frotas/infrastructure/database/__init__.py` | 1 |
| `src/modules/sigmun_frotas/infrastructure/database/models.py` | 105 |
| `src/modules/sigmun_frotas/infrastructure/integrations/__init__.py` | 1 |
| `src/modules/sigmun_frotas/infrastructure/repositories/__init__.py` | 1 |
| `src/modules/sigmun_frotas/infrastructure/repositories/sqlalchemy_operacional_repository.py` | 153 |
| `src/modules/sigmun_frotas/infrastructure/repositories/sqlalchemy_rota_repository.py` | 78 |
| `src/modules/sigmun_frotas/infrastructure/repositories/sqlalchemy_veiculo_repository.py` | 123 |
| `src/modules/sigmun_frotas/presentation/api/__init__.py` | 6 |
| `src/modules/sigmun_frotas/presentation/api/endpoints.py` | 329 |
| `src/modules/sigmun_frotas/presentation/schemas/__init__.py` | 1 |
| `src/modules/sigmun_frotas/presentation/schemas/fro_schemas.py` | 149 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 025-Gestao-de-Frota-Estrutura-Tecnica.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
