# 025 – Estrutura-Tecnica – Administração Tributária

#### Estrutura-Tecnica – Administração Tributária

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TRI-025

**Domínio:** Administração Tributária

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Administracao-Tributaria.md`
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

Este artefato detalha **a estrutura técnica** do domínio Administração Tributária (`DOM-TRI`), com base na implementação material identificada em `src/modules/sigmun_tributos` e no conteúdo de negócio declarado no gerador.

---

# 2. Módulo `sigmun_tributos`

| Arquivo | Linhas |
| --- | --- |
| `src/modules/sigmun_tributos/__init__.py` | 1 |
| `src/modules/sigmun_tributos/application/commands/__init__.py` | 1 |
| `src/modules/sigmun_tributos/application/interfaces.py` | 114 |
| `src/modules/sigmun_tributos/application/queries/__init__.py` | 1 |
| `src/modules/sigmun_tributos/application/use_cases.py` | 360 |
| `src/modules/sigmun_tributos/domain/entities/__init__.py` | 1 |
| `src/modules/sigmun_tributos/domain/entities/certidao.py` | 73 |
| `src/modules/sigmun_tributos/domain/entities/contribuinte.py` | 96 |
| `src/modules/sigmun_tributos/domain/entities/divida_ativa.py` | 89 |
| `src/modules/sigmun_tributos/domain/entities/imovel.py` | 70 |
| `src/modules/sigmun_tributos/domain/entities/lancamento.py` | 126 |
| `src/modules/sigmun_tributos/domain/events/__init__.py` | 1 |
| `src/modules/sigmun_tributos/domain/exceptions.py` | 78 |
| `src/modules/sigmun_tributos/domain/services/__init__.py` | 1 |
| `src/modules/sigmun_tributos/domain/value_objects/__init__.py` | 1 |
| `src/modules/sigmun_tributos/infrastructure/database/__init__.py` | 1 |
| `src/modules/sigmun_tributos/infrastructure/database/models.py` | 136 |
| `src/modules/sigmun_tributos/infrastructure/integrations/__init__.py` | 1 |
| `src/modules/sigmun_tributos/infrastructure/repositories/__init__.py` | 1 |
| `src/modules/sigmun_tributos/infrastructure/repositories/sqlalchemy_certidao_repository.py` | 89 |
| `src/modules/sigmun_tributos/infrastructure/repositories/sqlalchemy_contribuinte_repository.py` | 107 |
| `src/modules/sigmun_tributos/infrastructure/repositories/sqlalchemy_divida_ativa_repository.py` | 100 |
| `src/modules/sigmun_tributos/infrastructure/repositories/sqlalchemy_imovel_repository.py` | 117 |
| `src/modules/sigmun_tributos/infrastructure/repositories/sqlalchemy_lancamento_repository.py` | 146 |
| `src/modules/sigmun_tributos/presentation/api/__init__.py` | 17 |
| `src/modules/sigmun_tributos/presentation/api/contribuintes_imoveis_endpoints.py` | 167 |
| `src/modules/sigmun_tributos/presentation/api/divida_certidao_endpoints.py` | 176 |
| `src/modules/sigmun_tributos/presentation/api/lancamentos_endpoints.py` | 145 |
| `src/modules/sigmun_tributos/presentation/schemas/__init__.py` | 1 |
| `src/modules/sigmun_tributos/presentation/schemas/tri_schemas.py` | 163 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 025-Administracao-Tributaria-Estrutura-Tecnica.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
