# 025 – Estrutura-Tecnica – Segurança da Informação

#### Estrutura-Tecnica – Segurança da Informação

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-SEG-025

**Domínio:** Segurança da Informação

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Seguranca-da-Informacao.md`
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

Este artefato detalha **a estrutura técnica** do domínio Segurança da Informação (`DOM-SEG`), com base na implementação material identificada em `src/modules/sigmun_seg` e no conteúdo de negócio declarado no gerador.

---

# 2. Módulo `sigmun_seg`

| Arquivo | Linhas |
| --- | --- |
| `src/modules/sigmun_seg/__init__.py` | 0 |
| `src/modules/sigmun_seg/application/__init__.py` | 0 |
| `src/modules/sigmun_seg/application/interfaces/__init__.py` | 177 |
| `src/modules/sigmun_seg/application/use_cases/__init__.py` | 1 |
| `src/modules/sigmun_seg/application/use_cases/chave_use_cases.py` | 154 |
| `src/modules/sigmun_seg/application/use_cases/controle_use_cases.py` | 178 |
| `src/modules/sigmun_seg/application/use_cases/credencial_use_cases.py` | 147 |
| `src/modules/sigmun_seg/application/use_cases/incidente_use_cases.py` | 166 |
| `src/modules/sigmun_seg/application/use_cases/politica_use_cases.py` | 144 |
| `src/modules/sigmun_seg/domain/__init__.py` | 0 |
| `src/modules/sigmun_seg/domain/entities/__init__.py` | 261 |
| `src/modules/sigmun_seg/domain/events/__init__.py` | 66 |
| `src/modules/sigmun_seg/domain/exceptions.py` | 75 |
| `src/modules/sigmun_seg/domain/services/__init__.py` | 52 |
| `src/modules/sigmun_seg/domain/value_objects/__init__.py` | 44 |
| `src/modules/sigmun_seg/infrastructure/__init__.py` | 0 |
| `src/modules/sigmun_seg/infrastructure/database/__init__.py` | 0 |
| `src/modules/sigmun_seg/infrastructure/database/models.py` | 204 |
| `src/modules/sigmun_seg/infrastructure/repositories/__init__.py` | 20 |
| `src/modules/sigmun_seg/infrastructure/repositories/sqlalchemy_chave_repository.py` | 135 |
| `src/modules/sigmun_seg/infrastructure/repositories/sqlalchemy_controle_repository.py` | 154 |
| `src/modules/sigmun_seg/infrastructure/repositories/sqlalchemy_credencial_repository.py` | 147 |
| `src/modules/sigmun_seg/infrastructure/repositories/sqlalchemy_incidente_repository.py` | 149 |
| `src/modules/sigmun_seg/infrastructure/repositories/sqlalchemy_politica_repository.py` | 138 |
| `src/modules/sigmun_seg/presentation/__init__.py` | 0 |
| `src/modules/sigmun_seg/presentation/api/__init__.py` | 766 |
| `src/modules/sigmun_seg/presentation/schemas/__init__.py` | 0 |
| `src/modules/sigmun_seg/presentation/schemas/chave_schemas.py` | 29 |
| `src/modules/sigmun_seg/presentation/schemas/controle_schemas.py` | 36 |
| `src/modules/sigmun_seg/presentation/schemas/credencial_schemas.py` | 27 |
| `src/modules/sigmun_seg/presentation/schemas/incidente_schemas.py` | 29 |
| `src/modules/sigmun_seg/presentation/schemas/politica_schemas.py` | 25 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 025-Seguranca-da-Informacao-Estrutura-Tecnica.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
