# 025 – Estrutura-Tecnica – Assistência Social

#### Estrutura-Tecnica – Assistência Social

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ASS-025

**Domínio:** Assistência Social

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Assistencia-Social.md`
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

Este artefato detalha **a estrutura técnica** do domínio Assistência Social (`DOM-ASS`), com base na implementação material identificada em `src/modules/sigmun_assistencia_social` e no conteúdo de negócio declarado no gerador.

---

# 2. Módulo `sigmun_assistencia_social`

| Arquivo | Linhas |
| --- | --- |
| `src/modules/sigmun_assistencia_social/__init__.py` | 1 |
| `src/modules/sigmun_assistencia_social/application/commands/__init__.py` | 1 |
| `src/modules/sigmun_assistencia_social/application/interfaces.py` | 130 |
| `src/modules/sigmun_assistencia_social/application/queries/__init__.py` | 1 |
| `src/modules/sigmun_assistencia_social/application/use_cases.py` | 620 |
| `src/modules/sigmun_assistencia_social/domain/entities/__init__.py` | 344 |
| `src/modules/sigmun_assistencia_social/domain/events/__init__.py` | 1 |
| `src/modules/sigmun_assistencia_social/domain/exceptions.py` | 85 |
| `src/modules/sigmun_assistencia_social/domain/services/__init__.py` | 1 |
| `src/modules/sigmun_assistencia_social/domain/value_objects/__init__.py` | 1 |
| `src/modules/sigmun_assistencia_social/infrastructure/database/__init__.py` | 1 |
| `src/modules/sigmun_assistencia_social/infrastructure/database/models.py` | 144 |
| `src/modules/sigmun_assistencia_social/infrastructure/database/seeds.py` | 933 |
| `src/modules/sigmun_assistencia_social/infrastructure/integrations/__init__.py` | 1 |
| `src/modules/sigmun_assistencia_social/infrastructure/repositories/__init__.py` | 491 |
| `src/modules/sigmun_assistencia_social/presentation/api/__init__.py` | 6 |
| `src/modules/sigmun_assistencia_social/presentation/api/endpoints.py` | 677 |
| `src/modules/sigmun_assistencia_social/presentation/schemas/__init__.py` | 193 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 025-Assistencia-Social-Estrutura-Tecnica.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
