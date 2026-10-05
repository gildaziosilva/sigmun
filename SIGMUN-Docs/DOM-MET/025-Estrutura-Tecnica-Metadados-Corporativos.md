# 025 – Estrutura-Tecnica – Metadados Corporativos

#### Estrutura-Tecnica – Metadados Corporativos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-MET-025

**Domínio:** Metadados Corporativos

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Metadados-Corporativos.md`
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

Este artefato detalha **a estrutura técnica** do domínio Metadados Corporativos (`DOM-MET`), com base na implementação material identificada em `src/modules/sigmun_met` e no conteúdo de negócio declarado no gerador.

---

# 2. Módulo `sigmun_met`

| Arquivo | Linhas |
| --- | --- |
| `src/modules/sigmun_met/__init__.py` | 3 |
| `src/modules/sigmun_met/application/__init__.py` | 1 |
| `src/modules/sigmun_met/application/interfaces/__init__.py` | 185 |
| `src/modules/sigmun_met/application/use_cases/__init__.py` | 112 |
| `src/modules/sigmun_met/application/use_cases/classificacao_use_cases.py` | 164 |
| `src/modules/sigmun_met/application/use_cases/metadado_use_cases.py` | 231 |
| `src/modules/sigmun_met/application/use_cases/taxonomia_use_cases.py` | 138 |
| `src/modules/sigmun_met/application/use_cases/termo_use_cases.py` | 173 |
| `src/modules/sigmun_met/application/use_cases/valor_metadado_use_cases.py` | 160 |
| `src/modules/sigmun_met/domain/__init__.py` | 114 |
| `src/modules/sigmun_met/domain/entities/__init__.py` | 266 |
| `src/modules/sigmun_met/domain/events/__init__.py` | 104 |
| `src/modules/sigmun_met/domain/exceptions.py` | 112 |
| `src/modules/sigmun_met/domain/services/__init__.py` | 190 |
| `src/modules/sigmun_met/domain/value_objects/__init__.py` | 109 |
| `src/modules/sigmun_met/infrastructure/__init__.py` | 1 |
| `src/modules/sigmun_met/infrastructure/database/__init__.py` | 17 |
| `src/modules/sigmun_met/infrastructure/database/models.py` | 180 |
| `src/modules/sigmun_met/infrastructure/repositories/__init__.py` | 15 |
| `src/modules/sigmun_met/infrastructure/repositories/sqlalchemy_classificacao_repository.py` | 118 |
| `src/modules/sigmun_met/infrastructure/repositories/sqlalchemy_metadado_repository.py` | 142 |
| `src/modules/sigmun_met/infrastructure/repositories/sqlalchemy_taxonomia_repository.py` | 113 |
| `src/modules/sigmun_met/infrastructure/repositories/sqlalchemy_termo_repository.py` | 126 |
| `src/modules/sigmun_met/infrastructure/repositories/sqlalchemy_valor_metadado_repository.py` | 115 |
| `src/modules/sigmun_met/presentation/__init__.py` | 1 |
| `src/modules/sigmun_met/presentation/api/__init__.py` | 841 |
| `src/modules/sigmun_met/presentation/schemas/__init__.py` | 266 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 025-Metadados-Corporativos-Estrutura-Tecnica.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
