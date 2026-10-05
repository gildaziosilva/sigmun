# 025 – Estrutura-Tecnica – Saúde Pública

#### Estrutura-Tecnica – Saúde Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-SAU-025

**Domínio:** Saúde Pública

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Saude-Publica.md`
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

Este artefato detalha **a estrutura técnica** do domínio Saúde Pública (`DOM-SAU`), com base na implementação material identificada em `src/modules/sigmun_saude` e no conteúdo de negócio declarado no gerador.

---

# 2. Módulo `sigmun_saude`

| Arquivo | Linhas |
| --- | --- |
| `src/modules/sigmun_saude/__init__.py` | 1 |
| `src/modules/sigmun_saude/application/interfaces.py` | 115 |
| `src/modules/sigmun_saude/application/use_cases.py` | 357 |
| `src/modules/sigmun_saude/domain/entities/__init__.py` | 26 |
| `src/modules/sigmun_saude/domain/entities/atendimento.py` | 152 |
| `src/modules/sigmun_saude/domain/entities/farmacia_regulacao.py` | 177 |
| `src/modules/sigmun_saude/domain/entities/paciente.py` | 90 |
| `src/modules/sigmun_saude/domain/events/__init__.py` | 1 |
| `src/modules/sigmun_saude/domain/exceptions.py` | 85 |
| `src/modules/sigmun_saude/domain/services/__init__.py` | 1 |
| `src/modules/sigmun_saude/domain/value_objects/__init__.py` | 1 |
| `src/modules/sigmun_saude/infrastructure/database/__init__.py` | 1 |
| `src/modules/sigmun_saude/infrastructure/database/models.py` | 128 |
| `src/modules/sigmun_saude/infrastructure/integrations/__init__.py` | 1 |
| `src/modules/sigmun_saude/infrastructure/repositories/__init__.py` | 1 |
| `src/modules/sigmun_saude/infrastructure/repositories/sqlalchemy_atendimento_repository.py` | 103 |
| `src/modules/sigmun_saude/infrastructure/repositories/sqlalchemy_paciente_repository.py` | 62 |
| `src/modules/sigmun_saude/presentation/api/__init__.py` | 4 |
| `src/modules/sigmun_saude/presentation/api/endpoints.py` | 188 |
| `src/modules/sigmun_saude/presentation/schemas/__init__.py` | 1 |
| `src/modules/sigmun_saude/presentation/schemas/sau_schemas.py` | 72 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 025-Saude-Publica-Estrutura-Tecnica.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
