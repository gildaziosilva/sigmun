# 025 – Estrutura-Tecnica – Gestão de Pessoas

#### Estrutura-Tecnica – Gestão de Pessoas

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-PES-025

**Domínio:** Gestão de Pessoas

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-de-Pessoas.md`
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

Este artefato detalha **a estrutura técnica** do domínio Gestão de Pessoas (`DOM-PES`), com base na implementação material identificada em `src/modules/sigmun_rh` e no conteúdo de negócio declarado no gerador.

---

# 2. Módulo `sigmun_rh`

| Arquivo | Linhas |
| --- | --- |
| `src/modules/sigmun_rh/__init__.py` | 1 |
| `src/modules/sigmun_rh/application/commands/__init__.py` | 1 |
| `src/modules/sigmun_rh/application/interfaces.py` | 136 |
| `src/modules/sigmun_rh/application/queries/__init__.py` | 1 |
| `src/modules/sigmun_rh/application/use_cases/__init__.py` | 1 |
| `src/modules/sigmun_rh/application/use_cases_cargos_servidores.py` | 182 |
| `src/modules/sigmun_rh/application/use_cases_ferias.py` | 115 |
| `src/modules/sigmun_rh/application/use_cases_folha.py` | 155 |
| `src/modules/sigmun_rh/application/use_cases_frequencia.py` | 89 |
| `src/modules/sigmun_rh/application/use_cases_lotacao.py` | 97 |
| `src/modules/sigmun_rh/domain/entities/__init__.py` | 8 |
| `src/modules/sigmun_rh/domain/entities/cargo.py` | 52 |
| `src/modules/sigmun_rh/domain/entities/ferias.py` | 112 |
| `src/modules/sigmun_rh/domain/entities/folha.py` | 144 |
| `src/modules/sigmun_rh/domain/entities/frequencia.py` | 76 |
| `src/modules/sigmun_rh/domain/entities/lotacao.py` | 61 |
| `src/modules/sigmun_rh/domain/entities/servidor.py` | 132 |
| `src/modules/sigmun_rh/domain/events/__init__.py` | 1 |
| `src/modules/sigmun_rh/domain/exceptions.py` | 121 |
| `src/modules/sigmun_rh/domain/services/__init__.py` | 1 |
| `src/modules/sigmun_rh/domain/value_objects/__init__.py` | 1 |
| `src/modules/sigmun_rh/infrastructure/database/__init__.py` | 1 |
| `src/modules/sigmun_rh/infrastructure/database/models.py` | 77 |
| `src/modules/sigmun_rh/infrastructure/database/models_folha.py` | 84 |
| `src/modules/sigmun_rh/infrastructure/integrations/__init__.py` | 1 |
| `src/modules/sigmun_rh/infrastructure/repositories/__init__.py` | 1 |
| `src/modules/sigmun_rh/infrastructure/repositories/sqlalchemy_cargo_repository.py` | 88 |
| `src/modules/sigmun_rh/infrastructure/repositories/sqlalchemy_ferias_repository.py` | 84 |
| `src/modules/sigmun_rh/infrastructure/repositories/sqlalchemy_folha_repository.py` | 102 |
| `src/modules/sigmun_rh/infrastructure/repositories/sqlalchemy_frequencia_repository.py` | 94 |
| `src/modules/sigmun_rh/infrastructure/repositories/sqlalchemy_lotacao_repository.py` | 90 |
| `src/modules/sigmun_rh/infrastructure/repositories/sqlalchemy_servidor_repository.py` | 116 |
| `src/modules/sigmun_rh/presentation/api/__init__.py` | 23 |
| `src/modules/sigmun_rh/presentation/api/cargos.py` | 39 |
| `src/modules/sigmun_rh/presentation/api/cargos_endpoints.py` | 42 |
| `src/modules/sigmun_rh/presentation/api/ferias_freq_endpoints.py` | 168 |
| `src/modules/sigmun_rh/presentation/api/folha_endpoints.py` | 131 |
| `src/modules/sigmun_rh/presentation/api/lotacoes.py` | 53 |
| `src/modules/sigmun_rh/presentation/api/lotacoes_endpoints.py` | 72 |
| `src/modules/sigmun_rh/presentation/api/operacional.py` | 60 |
| `src/modules/sigmun_rh/presentation/api/servidores.py` | 57 |
| `src/modules/sigmun_rh/presentation/api/servidores_endpoints.py` | 93 |
| `src/modules/sigmun_rh/presentation/schemas/__init__.py` | 1 |
| `src/modules/sigmun_rh/presentation/schemas/pes_operacionais_schemas.py` | 131 |
| `src/modules/sigmun_rh/presentation/schemas/pes_schemas.py` | 78 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 025-Gestao-de-Pessoas-Estrutura-Tecnica.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
