# 025 – Estrutura-Tecnica – Dados Corporativos

#### Estrutura-Tecnica – Dados Corporativos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-DAD-025

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

Este artefato detalha **a estrutura técnica** do domínio Dados Corporativos (`DOM-DAD`), com base na implementação material identificada em `src/modules/sigmun_dad` e no conteúdo de negócio declarado no gerador.

---

# 2. Módulo `sigmun_dad`

| Arquivo | Linhas |
| --- | --- |
| `src/modules/sigmun_dad/application/interfaces/__init__.py` | 163 |
| `src/modules/sigmun_dad/application/use_cases/__init__.py` | 210 |
| `src/modules/sigmun_dad/application/use_cases/catalogo_use_cases.py` | 165 |
| `src/modules/sigmun_dad/application/use_cases/linhagem_use_cases.py` | 125 |
| `src/modules/sigmun_dad/application/use_cases/politica_use_cases.py` | 157 |
| `src/modules/sigmun_dad/application/use_cases/qualidade_use_cases.py` | 130 |
| `src/modules/sigmun_dad/domain/__init__.py` | 108 |
| `src/modules/sigmun_dad/domain/entities/__init__.py` | 289 |
| `src/modules/sigmun_dad/domain/events/__init__.py` | 109 |
| `src/modules/sigmun_dad/domain/exceptions.py` | 106 |
| `src/modules/sigmun_dad/domain/services/__init__.py` | 111 |
| `src/modules/sigmun_dad/domain/value_objects/__init__.py` | 76 |
| `src/modules/sigmun_dad/infrastructure/database/__init__.py` | 19 |
| `src/modules/sigmun_dad/infrastructure/database/models.py` | 188 |
| `src/modules/sigmun_dad/infrastructure/repositories/__init__.py` | 25 |
| `src/modules/sigmun_dad/infrastructure/repositories/sqlalchemy_ativo_repository.py` | 155 |
| `src/modules/sigmun_dad/infrastructure/repositories/sqlalchemy_catalogo_repository.py` | 115 |
| `src/modules/sigmun_dad/infrastructure/repositories/sqlalchemy_linhagem_repository.py` | 128 |
| `src/modules/sigmun_dad/infrastructure/repositories/sqlalchemy_politica_repository.py` | 123 |
| `src/modules/sigmun_dad/infrastructure/repositories/sqlalchemy_qualidade_repository.py` | 123 |
| `src/modules/sigmun_dad/presentation/api/__init__.py` | 806 |
| `src/modules/sigmun_dad/presentation/schemas/__init__.py` | 277 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 025-Dados-Corporativos-Estrutura-Tecnica.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
