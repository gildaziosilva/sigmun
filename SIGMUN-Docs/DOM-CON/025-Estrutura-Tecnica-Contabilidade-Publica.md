# 025 – Estrutura Técnica – Contabilidade Pública

#### Estrutura Técnica – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-025

**Domínio:** Contabilidade Pública

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Contabilidade-Publica.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000C-HIERARQUIA-DOCUMENTAL-v1.0.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `AUDITORIA-DOM-CON-2026-09-30.md`

---

# 1. Finalidade

Este artefato descreve a estrutura técnica do módulo `sigmun_con`, descrevendo a
organização de pacotes, as tecnologias utilizadas, os pontos de entrada e as dependências.

---

# 2. Localização

```text
src/modules/sigmun_con/
```

**Schema de persistência:** `con` (PostgreSQL)
**Prefixo da API:** `/api/v1/con`
**Tag da API:** `Contabilidade Pública`

---

# 3. Árvore de Módulos

```text
sigmun_con/
├── application/
│   ├── interfaces.py               Ports (Protocol) de repositório
│   ├── use_cases_execucao.py       Empenho, liquidação, anulação, pagamento
│   └── use_cases_contabil.py       Contas, lançamentos, conciliação
├── domain/
│   ├── entities/
│   │   ├── empenho.py              Empenho, StatusEmpenho, TipoEmpenho
│   │   ├── liquidacao.py           Liquidacao, StatusLiquidacao
│   │   ├── pagamento.py            Pagamento, StatusPagamento
│   │   ├── conta.py                ContaContabil (PCASP)
│   │   └── lancamento.py           LancamentoContabil, Partida,
│   │                               ConciliacaoContabil, Status e Tipos
│   └── exceptions.py               13 exceções de negócio
├── infrastructure/
│   ├── database/
│   │   ├── models.py               Empenho, Liquidacao, Pagamento
│   │   └── models_contabil.py      Conta, Lancamento, Conciliacao
│   └── repositories/
│       ├── sqlalchemy_empenho_repository.py
│       ├── sqlalchemy_liq_pag_repository.py
│       ├── sqlalchemy_conta_repository.py
│       └── sqlalchemy_lanc_conc_repository.py
└── presentation/
    ├── api/
    │   ├── base.py                 Factories de repositório
    │   ├── execucao_endpoints.py   Router de execução
    │   └── contabil_endpoints.py   Router contábil
    └── schemas/
        └── con_schemas.py          16 schemas Pydantic
```

**Total:** 21 arquivos Python.

---

# 4. Camadas Ausentes

Comparado aos demais 30 módulos do sistema, `sigmun_con` não possui:

| Pacote ausente | Consequência | Achado |
| --- | --- | --- |
| `domain/events/` | Sem eventos de domínio; integração assíncrona inviável | M-01 |
| `domain/value_objects/` | Sem `Exercicio`, `ValorMonetario`, `Competencia` | M-01 |
| `domain/services/` | Regras complexas permanecem nos casos de uso | M-01 |

Apenas `sigmun_orc` apresenta a mesma lacuna.

---

# 5. Tecnologias

| Camada | Tecnologia | Versão |
| --- | --- | --- |
| Linguagem | Python | 3.10 |
| Framework web | FastAPI | — |
| Validação de entrada | Pydantic | 2.x |
| ORM | SQLAlchemy | 2.x |
| Banco de dados | PostgreSQL | — |
| Migrations | Alembic | — |
| Testes | pytest | 9.x |
| Qualidade estática | ruff, mypy | — |
| Documentação de domínio | PlantUML | 2.x |

---

# 6. Pontos de Entrada

## 6.1 API

| Router | Prefixo | Operações |
| --- | --- | --- |
| `execucao_endpoints.py` | `/api/v1/con` | POST `/empenhos`, `/empenhos/{id}/liquidar`, `/empenhos/{id}/anular`, `/pagamentos` |
| `contabil_endpoints.py` | `/api/v1/con` | POST `/contas`, `/lancamentos`, `/conciliacoes` |

## 6.2 Registro na Aplicação

**Estado:** os routers **não são importados nem registrados** em `src/main.py`
(achado C-01). A correção é:

```python
from src.modules.sigmun_con.presentation.api import (
    routers as con_routers,
)
# ...
for _con_router in con_routers:
    app.include_router(_con_router)
```

## 6.3 Factories de Repositório

`presentation/api/base.py` expõe funções de dependência do FastAPI:

| Função | Repositório |
| --- | --- |
| `get_empenho_repo` | `SQLAlchemyEmpenhoRepository` |
| `get_liquidacao_repo` | `SQLAlchemyLiquidacaoRepository` |
| `get_pagamento_repo` | `SQLAlchemyPagamentoRepository` |
| `get_conta_repo` | `SQLAlchemyContaRepository` |
| `get_lancamento_repo` | `SQLAlchemyLancamentoRepository` |
| `get_conciliacao_repo` | `SQLAlchemyConciliacaoRepository` |
| `get_dotacao_repo_con` | `SQLAlchemyDotacaoRepository` (DOM-ORC) |

A dependência `get_dotacao_repo_con` é a **única ponte entre DOM-CON e DOM-ORC**.

---

# 7. Persistência

| Item | Detalhe |
| --- | --- |
| Migrations | `20260919_05_dom_con_models`, `20260919_06_dom_con_contabil` |
| Tabelas | 6 no schema `con` |
| Chaves estrangeiras | 3 internas com `ON DELETE RESTRICT` |
| Unicidade | `UNIQUE` apenas em `contas_contabeis.codigo` |
| Índices | **Nenhum** |

**Observação estrutural:** `database/models.py` e `database/models_contabil.py`
declaram **bases ORM distintas** — `declarative_base()` próprio e um
`declarative_base()` separado em `models_contabil.py`. Isso divide o metadado em dois
blocos e impede introspecção conjunta (contribui para os 131 erros de tipagem).

---

# 8. Dependências

## 8.1 Internas

| Depende de | Uso |
| --- | --- |
| `src.core.infrastructure.database.session` | Sessão do banco (`get_db`) |

## 8.2 Externas — Domínios

| Domínio | Dependência |
| --- | --- |
| `sigmun_orc` | `RepositorioDotacao`, `DomOrcDomainError` |
| `src.modules.sigmun_con.presentation.schemas` | Schemas próprios |

## 8.3 Não utilizadas

Os módulos `sigmun_contabilidade` e `sigmun_controladoria` **não são importados** por
`DOM-CON`. Ambos são esqueletos vazios, com a mesma estrutura de pastas do SIGMUN
implementado, mas sem qualquer classe Python.

**Consequência:** existe uma colisão de fronteira não resolvida entre `sigmun_con`,
`sigmun_contabilidade` e `sigmun_controladoria`, e `sigmun_con` não consta do catálogo
`05-Modulos/index.md` (achado C-04).

---

# 9. Schemas Pydantic

| Schema | Tipo | Uso |
| --- | --- | --- |
| `EmpenhoCreateRequest` | Entrada | Emissão de empenho |
| `EmpenhoValorRequest` | Entrada | Liquidação e anulação |
| `EmpenhoResponse` | Saída | Empenho |
| `LiquidacaoResponse` | Saída | Liquidação |
| `PagamentoCreateRequest` | Entrada | Pagamento |
| `PagamentoResponse` | Saída | Pagamento |
| `ContaCreateRequest` | Entrada | Criação de conta |
| `ContaResponse` | Saída | Conta |
| `PartidaRequest` | Aninhado | Partida dobrada |
| `LancamentoCreateRequest` | Entrada | Lançamento |
| `LancamentoResponse` | Saída | Lançamento |
| `ConciliacaoCreateRequest` | Entrada | Conciliação |
| `ConciliacaoResponse` | Saída | Conciliação |

**Validações declaradas:** `exercicio` ≥ 2000, `valor` > 0, `mes` entre 1 e 12,
`tipo` de partida limitado a `debito` ou `credito`, `partidas` com no mínimo 2 itens.

---

# 10. Exceções

| Exceção | Usos | Observação |
| --- | --- | --- |
| `DomConDomainError` | 9 | Base de todas |
| `RegraNegocioError` | 46 | Regra genérica |
| `EmpenhoNaoEncontradoError` | 6 | Em uso |
| `EmpenhoJaExistenteError` | 0 | **Órfã** |
| `EmpenhoEmEstadoInvalidoError` | 0 | **Órfã** |
| `LiquidacaoNaoEncontradaError` | 2 | Em uso |
| `PagamentoNaoEncontradoError` | 0 | **Órfã** |
| `ContaContabilNaoEncontradaError` | 0 | **Órfã** |
| `ContaContabilJaExistenteError` | 0 | **Órfã** |
| `LancamentoNaoEncontradoError` | 0 | **Órfã** |
| `LancamentoDesequilibradoError` | 2 | Em uso |
| `ConciliacaoNaoEncontradaError` | 0 | **Órfã** |
| `TransicaoInvalidaError` | 0 | **Órfã** |

**Oito exceções órfãs** impedem o contrato correto de erro: como os casos de uso
lançam `RegraNegocioError`, os endpoints respondem 409 para qualquer falha, inclusive
recurso inexistente, que deveria responder 404 (achado A-06).

---

# 11. Artefatos de Documentação

| Artefato | Caminho |
| --- | --- |
| Domínio | `SIGMUN-Docs/DOM-CON/` |
| Diagramas PlantUML | `SIGMUN-Docs/DOM-CON/puml/` |
| Auditoria | `SIGMUN-Docs/00-Governanca/AUDITORIA-DOM-CON-2026-09-30.md` |
| Plano de trabalho | `SIGMUN-Docs/00-Governanca/PLANO-DE-TRABALHO-DOM-CON-2026-09-30.md` |

---

# 12. Qualidade Estática

| Ferramenta | Resultado |
| --- | --- |
| `ruff check src/modules/sigmun_con/` | Sem erros |
| `mypy src/modules/sigmun_con/` | **131 erros em 12 arquivos** |

Distribuição dos erros de tipagem:

| Arquivo | Erros |
| --- | --- |
| `sqlalchemy_lanc_conc_repository.py` | 30 |
| `sqlalchemy_liq_pag_repository.py` | 22 |
| `sqlalchemy_empenho_repository.py` | 19 |
| `sqlalchemy_conta_repository.py` | 12 |
| `database/models.py` | 9 |
| Endpoints e casos de uso | 20 |
| Entidades | 2 |

---

# 13. Configuração

| Variável | Finalidade |
| --- | --- |
| `APP_ENV` | Modo da aplicação |
| `DATABASE_URL` | Conexão com o PostgreSQL |
| `ALLOWED_HOSTS` | Origens autorizadas no CORS |

O módulo não introduz variáveis próprias.

---

# 14. Resumo

| Aspecto | Estado |
| --- | --- |
| Organização de pastas | Conforme o padrão, sem as três camadas de domínio |
| Ports e inversão de dependência | Correta |
| Persistência | Implementada com perdas de campo e sem índices |
| API | Implementada, **não registrada** |
| Integração com DOM-ORC | Implementada, sem FK e sem atomicidade |
| Testes | 6 casos unitários, nenhum de integração |
| Qualidade estática | Lint limpo, 131 erros de tipagem |
| Colisão de módulo | Não resolvida |


---

Este artefato descreve a estrutura técnica do módulo `sigmun_con`, descrevendo a
organização de pacotes, as tecnologias utilizadas, os pontos de entrada e as dependências.

---

# 2. Localização

```text
src/modules/sigmun_con/
```

**Schema de persistência:** `con` (PostgreSQL)
**Prefixo da API:** `/api/v1/con`
**Tag da API:** `Contabilidade Pública`

---

# 3. Árvore de Módulos

```text
sigmun_con/
├── application/
│   ├── interfaces.py               Ports (Protocol) de repositório
│   ├── use_cases_execucao.py       Empenho, liquidação, anulação, pagamento
│   └── use_cases_contabil.py       Contas, lançamentos, conciliação
├── domain/
│   ├── entities/
│   │   ├── empenho.py              Empenho, StatusEmpenho, TipoEmpenho
│   │   ├── liquidacao.py           Liquidacao, StatusLiquidacao
│   │   ├── pagamento.py            Pagamento, StatusPagamento
│   │   ├── conta.py                ContaContabil (PCASP)
│   │   └── lancamento.py           LancamentoContabil, Partida,
│   │                               ConciliacaoContabil, Status e Tipos
│   └── exceptions.py               13 exceções de negócio
├── infrastructure/
│   ├── database/
│   │   ├── models.py               Empenho, Liquidacao, Pagamento
│   │   └── models_contabil.py      Conta, Lancamento, Conciliacao
│   └── repositories/
│       ├── sqlalchemy_empenho_repository.py
│       ├── sqlalchemy_liq_pag_repository.py
│       ├── sqlalchemy_conta_repository.py
│       └── sqlalchemy_lanc_conc_repository.py
└── presentation/
    ├── api/
    │   ├── base.py                 Factories de repositório
    │   ├── execucao_endpoints.py   Router de execução
    │   └── contabil_endpoints.py   Router contábil
    └── schemas/
        └── con_schemas.py          16 schemas Pydantic
```

**Total:** 21 arquivos Python.

---

# 4. Camadas Ausentes

Comparado aos demais 30 módulos do sistema, `sigmun_con` não possui:

| Pacote ausente | Consequência | Achado |
| --- | --- | --- |
| `domain/events/` | Sem eventos de domínio; integração assíncrona inviável | M-01 |
| `domain/value_objects/` | Sem `Exercicio`, `ValorMonetario`, `Competencia` | M-01 |
| `domain/services/` | Regras complexas permanecem nos casos de uso | M-01 |

Apenas `sigmun_orc` apresenta a mesma lacuna.

---

# 5. Tecnologias

| Camada | Tecnologia | Versão |
| --- | --- | --- |
| Linguagem | Python | 3.10 |
| Framework web | FastAPI | — |
| Validação de entrada | Pydantic | 2.x |
| ORM | SQLAlchemy | 2.x |
| Banco de dados | PostgreSQL | — |
| Migrations | Alembic | — |
| Testes | pytest | 9.x |
| Qualidade estática | ruff, mypy | — |
| Documentação de domínio | PlantUML | 2.x |

---

# 6. Pontos de Entrada

## 6.1 API

| Router | Prefixo | Operações |
| --- | --- | --- |
| `execucao_endpoints.py` | `/api/v1/con` | POST `/empenhos`, `/empenhos/{id}/liquidar`, `/empenhos/{id}/anular`, `/pagamentos` |
| `contabil_endpoints.py` | `/api/v1/con` | POST `/contas`, `/lancamentos`, `/conciliacoes` |

## 6.2 Registro na Aplicação

**Estado:** os routers **não são importados nem registrados** em `src/main.py`
(achado C-01). A correção é:

```python
from src.modules.sigmun_con.presentation.api import (
    routers as con_routers,
)
# ...
for _con_router in con_routers:
    app.include_router(_con_router)
```

## 6.3 Factories de Repositório

`presentation/api/base.py` expõe funções de dependência do FastAPI:

| Função | Repositório |
| --- | --- |
| `get_empenho_repo` | `SQLAlchemyEmpenhoRepository` |
| `get_liquidacao_repo` | `SQLAlchemyLiquidacaoRepository` |
| `get_pagamento_repo` | `SQLAlchemyPagamentoRepository` |
| `get_conta_repo` | `SQLAlchemyContaRepository` |
| `get_lancamento_repo` | `SQLAlchemyLancamentoRepository` |
| `get_conciliacao_repo` | `SQLAlchemyConciliacaoRepository` |
| `get_dotacao_repo_con` | `SQLAlchemyDotacaoRepository` (DOM-ORC) |

A dependência `get_dotacao_repo_con` é a **única ponte entre DOM-CON e DOM-ORC**.

---

# 7. Persistência

| Item | Detalhe |
| --- | --- |
| Migrations | `20260919_05_dom_con_models`, `20260919_06_dom_con_contabil` |
| Tabelas | 6 no schema `con` |
| Chaves estrangeiras | 3 internas com `ON DELETE RESTRICT` |
| Unicidade | `UNIQUE` apenas em `contas_contabeis.codigo` |
| Índices | **Nenhum** |

**Observação estrutural:** `database/models.py` e `database/models_contabil.py`
declaram **bases ORM distintas** — `declarative_base()` próprio e um
`declarative_base()` separado em `models_contabil.py`. Isso divide o metadado em dois
blocos e impede introspecção conjunta (contribui para os 131 erros de tipagem).

---

# 8. Dependências

## 8.1 Internas

| Depende de | Uso |
| --- | --- |
| `src.core.infrastructure.database.session` | Sessão do banco (`get_db`) |

## 8.2 Externas — Domínios

| Domínio | Dependência |
| --- | --- |
| `sigmun_orc` | `RepositorioDotacao`, `DomOrcDomainError` |
| `src.modules.sigmun_con.presentation.schemas` | Schemas próprios |

## 8.3 Não utilizadas

Os módulos `sigmun_contabilidade` e `sigmun_controladoria` **não são importados** por
`DOM-CON`. Ambos são esqueletos vazios, com a mesma estrutura de pastas do SIGMUN
implementado, mas sem qualquer classe Python.

**Consequência:** existe uma colisão de fronteira não resolvida entre `sigmun_con`,
`sigmun_contabilidade` e `sigmun_controladoria`, e `sigmun_con` não consta do catálogo
`05-Modulos/index.md` (achado C-04).

---

# 9. Schemas Pydantic

| Schema | Tipo | Uso |
| --- | --- | --- |
| `EmpenhoCreateRequest` | Entrada | Emissão de empenho |
| `EmpenhoValorRequest` | Entrada | Liquidação e anulação |
| `EmpenhoResponse` | Saída | Empenho |
| `LiquidacaoResponse` | Saída | Liquidação |
| `PagamentoCreateRequest` | Entrada | Pagamento |
| `PagamentoResponse` | Saída | Pagamento |
| `ContaCreateRequest` | Entrada | Criação de conta |
| `ContaResponse` | Saída | Conta |
| `PartidaRequest` | Aninhado | Partida dobrada |
| `LancamentoCreateRequest` | Entrada | Lançamento |
| `LancamentoResponse` | Saída | Lançamento |
| `ConciliacaoCreateRequest` | Entrada | Conciliação |
| `ConciliacaoResponse` | Saída | Conciliação |

**Validações declaradas:** `exercicio` ≥ 2000, `valor` > 0, `mes` entre 1 e 12,
`tipo` de partida limitado a `debito` ou `credito`, `partidas` com no mínimo 2 itens.

---

# 10. Exceções

| Exceção | Usos | Observação |
| --- | --- | --- |
| `DomConDomainError` | 9 | Base de todas |
| `RegraNegocioError` | 46 | Regra genérica |
| `EmpenhoNaoEncontradoError` | 6 | Em uso |
| `EmpenhoJaExistenteError` | 0 | **Órfã** |
| `EmpenhoEmEstadoInvalidoError` | 0 | **Órfã** |
| `LiquidacaoNaoEncontradaError` | 2 | Em uso |
| `PagamentoNaoEncontradoError` | 0 | **Órfã** |
| `ContaContabilNaoEncontradaError` | 0 | **Órfã** |
| `ContaContabilJaExistenteError` | 0 | **Órfã** |
| `LancamentoNaoEncontradoError` | 0 | **Órfã** |
| `LancamentoDesequilibradoError` | 2 | Em uso |
| `ConciliacaoNaoEncontradaError` | 0 | **Órfã** |
| `TransicaoInvalidaError` | 0 | **Órfã** |

**Oito exceções órfãs** impedem o contrato correto de erro: como os casos de uso
lançam `RegraNegocioError`, os endpoints respondem 409 para qualquer falha, inclusive
recurso inexistente, que deveria responder 404 (achado A-06).

---

# 11. Artefatos de Documentação

| Artefato | Caminho |
| --- | --- |
| Domínio | `SIGMUN-Docs/DOM-CON/` |
| Diagramas PlantUML | `SIGMUN-Docs/DOM-CON/puml/` |
| Auditoria | `SIGMUN-Docs/00-Governanca/AUDITORIA-DOM-CON-2026-09-30.md` |
| Plano de trabalho | `SIGMUN-Docs/00-Governanca/PLANO-DE-TRABALHO-DOM-CON-2026-09-30.md` |

---

# 12. Qualidade Estática

| Ferramenta | Resultado |
| --- | --- |
| `ruff check src/modules/sigmun_con/` | Sem erros |
| `mypy src/modules/sigmun_con/` | **131 erros em 12 arquivos** |

Distribuição dos erros de tipagem:

| Arquivo | Erros |
| --- | --- |
| `sqlalchemy_lanc_conc_repository.py` | 30 |
| `sqlalchemy_liq_pag_repository.py` | 22 |
| `sqlalchemy_empenho_repository.py` | 19 |
| `sqlalchemy_conta_repository.py` | 12 |
| `database/models.py` | 9 |
| Endpoints e casos de uso | 20 |
| Entidades | 2 |

---

# 13. Configuração

| Variável | Finalidade |
| --- | --- |
| `APP_ENV` | Modo da aplicação |
| `DATABASE_URL` | Conexão com o PostgreSQL |
| `ALLOWED_HOSTS` | Origens autorizadas no CORS |

O módulo não introduz variáveis próprias.

---

# 14. Resumo

| Aspecto | Estado |
| --- | --- |
| Organização de pastas | Conforme o padrão, sem as três camadas de domínio |
| Ports e inversão de dependência | Correta |
| Persistência | Implementada com perdas de campo e sem índices |
| API | Implementada, **não registrada** |
| Integração com DOM-ORC | Implementada, sem FK e sem atomicidade |
| Testes | 6 casos unitários, nenhum de integração |
| Qualidade estática | Lint limpo, 131 erros de tipagem |
| Colisão de módulo | Não resolvida |

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 025-Estrutura-Tecnica-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
