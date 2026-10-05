# 015 – Arquitetura de Serviços – Contabilidade Pública

#### Arquitetura de Serviços – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-015

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

Este artefato descreve a arquitetura de serviços do domínio de Contabilidade Pública,
organizando o módulo `sigmun_con` segundo a arquitetura hexagonal adotada no SIGMUN.

---

# 2. Camadas

| Camada | Responsabilidade | Pacote |
| --- | --- | --- |
| Domínio | Entidades, invariantes, máquina de estados e exceções | `domain/` |
| Aplicação | Casos de uso e ports de repositório | `application/` |
| Infraestrutura | Modelos ORM, repositórios e factories | `infrastructure/` |
| Apresentação | Endpoints HTTP e schemas de entrada e saída | `presentation/` |

A regra de dependência é unidirecional: a apresentação depende da aplicação, que
depende do domínio. **O domínio não conhece camadas externas.**

---

# 3. Componentes

## 3.1 Domínio (`domain/`)

| Componente | Arquivo | Responsabilidade |
| --- | --- | --- |
| `Empenho` | `entities/empenho.py` | Raiz do agregado da despesa; máquina de estados e invariantes de saldo |
| `Liquidacao` | `entities/liquidacao.py` | Comprovante do direito adquirido |
| `Pagamento` | `entities/pagamento.py` | Ordem bancária e efetivação |
| `ContaContabil` | `entities/conta.py` | Plano de contas do PCASP |
| `LancamentoContabil` | `entities/lancamento.py` | Lançamento por partidas dobradas |
| `Partida` | `entities/lancamento.py` | Objeto de valor da partida dobrada |
| `ConciliacaoContabil` | `entities/lancamento.py` | Comparação entre contábil e extrato |
| Exceções | `exceptions.py` | 13 exceções de negócio |

**Enumerações:** `StatusEmpenho`, `TipoEmpenho`, `StatusLiquidacao`,
`StatusPagamento`, `StatusLancamento`, `StatusConciliacao`, `TipoPartida`.

**Estruturas de máquina de estados:** `TRANSICOES_EMPENHO`,
`ESTADOS_TERMINAIS_EMPENHO`, `TRANSICOES_LIQUIDACAO`,
`ESTADOS_TERMINAIS_LIQUIDACAO`.

**Propriedades derivadas:** `valor_liquido`, `saldo_a_liquidar`, `saldo_a_pagar`,
`balanceado`, `pode_receber_lancamento`, `is_active`, `is_terminal`.

**Camadas ausentes:** `domain/events`, `domain/value_objects` e `domain/services` —
o módulo é um dos dois do sistema sem essas pastas (achado M-01).

## 3.2 Aplicação (`application/`)

| Componente | Responsabilidade |
| --- | --- |
| `use_cases_execucao.py` | `EmitirEmpenhoUseCase`, `AnularEmpenhoUseCase`, `LiquidarEmpenhoUseCase`, `PagarLiquidacaoUseCase` |
| `use_cases_contabil.py` | `CriarContaUseCase`, `LancarContabilUseCase`, `ConciliarContaUseCase` |
| `interfaces.py` | Ports `RepositorioEmpenho`, `RepositorioLiquidacao`, `RepositorioPagamento`, `RepositorioContaContabil`, `RepositorioLancamento`, `RepositorioConciliacao` |

Os ports são `Protocol`, o que permite inversão de dependência sem acoplamento a
framework.

## 3.3 Infraestrutura (`infrastructure/`)

| Componente | Responsabilidade |
| --- | --- |
| `database/models.py` | `EmpenhoModel`, `LiquidacaoModel`, `PagamentoModel` |
| `database/models_contabil.py` | `ContaContabilModel`, `LancamentoModel`, `ConciliacaoModel` |
| `repositories/sqlalchemy_empenho_repository.py` | `SQLAlchemyEmpenhoRepository` |
| `repositories/sqlalchemy_liq_pag_repository.py` | `SQLAlchemyLiquidacaoRepository`, `SQLAlchemyPagamentoRepository` |
| `repositories/sqlalchemy_conta_repository.py` | `SQLAlchemyContaRepository` |
| `repositories/sqlalchemy_lanc_conc_repository.py` | `SQLAlchemyLancamentoRepository`, `SQLAlchemyConciliacaoRepository` |

**Observação estrutural:** `models.py` e `models_contabil.py` **definem bases
declarativas distintas** (`Base` próprio e `declarative_base()` separado). Isso divide
o metadado ORM em dois blocos e dificulta a introspecção conjunta (achado A-05).

## 3.4 Apresentação (`presentation/`)

| Componente | Responsabilidade |
| --- | --- |
| `api/execucao_endpoints.py` | Router de execução: empenho, liquidação, anulação, pagamento |
| `api/contabil_endpoints.py` | Router contábil: contas, lançamentos, conciliações |
| `api/base.py` | Factories de repositório via dependência FastAPI |
| `schemas/con_schemas.py` | 16 schemas Pydantic |

**Prefixo:** `/api/v1/con` · **Tag:** `Contabilidade Pública`

---

# 4. Fluxo de uma Requisição

```text
Cliente HTTP
    │
    ▼
Middleware (correlação, autenticação)
    │
    ▼
Endpoint (presentation/api)
    │  valida schema Pydantic
    │  injeta repositórios via Depends
    ▼
Caso de uso (application)
    │  executa regra de negócio
    │  manipula a entidade de domínio
    ▼
Entidade (domain)
    │  valida invariantes
    │  aplica transição de estado
    ▼
Port (application/interfaces)
    │
    ▼
Repositório (infrastructure)
    │
    ▼
PostgreSQL — schema con
```

O caso de uso devolve a entidade de domínio; a camada de apresentação a converte em
schema de resposta.

---

# 5. Catálogo de Serviços

| Serviço | Caso de uso | Repositórios necessários |
| --- | --- | --- |
| SVC-CON-001 Emissão | `EmitirEmpenhoUseCase` | Empenho, Dotação (DOM-ORC) |
| SVC-CON-002 Liquidação | `LiquidarEmpenhoUseCase` | Empenho, Liquidação |
| SVC-CON-003 Anulação | `AnularEmpenhoUseCase` | Empenho, Dotação (DOM-ORC) |
| SVC-CON-004 Pagamento | `PagarLiquidacaoUseCase` | Empenho, Liquidação, Pagamento |
| SVC-CON-005 Criar conta | `CriarContaUseCase` | Conta |
| SVC-CON-006 Lançar | `LancarContabilUseCase` | Lançamento, Conta |
| SVC-CON-007 Conciliar | `ConciliarContaUseCase` | Conciliação |

---

# 6. Pontos de Extensão

| Ponto | Implementação atual | Ponto de extensão previsto |
| --- | --- | --- |
| Persistência | SQLAlchemy + PostgreSQL | Outro repositório via port `Protocol` |
| Autenticação | DOM-IDN (não aplicado ao domínio) | Middleware de autorização por operação |
| Documentos | Texto livre | Cliente do DOM-GDO |
| Notificações | Inexistente | Barramento de eventos |
| Relatórios | Inexistente | Serviço de consulta da execução |

A definição dos ports como `Protocol` permite substituir a persistência sem alterar o
domínio nem a aplicação.

---

# 7. Estado da Arquitetura

| Aspecto | Situação |
| --- | --- |
| Arquitetura hexagonal | Estruturalmente correta |
| Inversão de dependência | Ports como `Protocol` |
| Regra de dependência | Respeitada |
| Testabilidade do domínio | Boa — sem dependência externa |
| Exposição HTTP | **Inexistente** (C-01) |
| Eventos de domínio | **Inexistentes** (M-01) |
| Objetos de valor | **Inexistentes** (M-01) |
| Tipagem | 131 erros (A-05) |
| Metadado ORM unificado | **Não** — duas bases declarativas |


---

Este artefato descreve a arquitetura de serviços do domínio de Contabilidade Pública,
organizando o módulo `sigmun_con` segundo a arquitetura hexagonal adotada no SIGMUN.

---

# 2. Camadas

| Camada | Responsabilidade | Pacote |
| --- | --- | --- |
| Domínio | Entidades, invariantes, máquina de estados e exceções | `domain/` |
| Aplicação | Casos de uso e ports de repositório | `application/` |
| Infraestrutura | Modelos ORM, repositórios e factories | `infrastructure/` |
| Apresentação | Endpoints HTTP e schemas de entrada e saída | `presentation/` |

A regra de dependência é unidirecional: a apresentação depende da aplicação, que
depende do domínio. **O domínio não conhece camadas externas.**

---

# 3. Componentes

## 3.1 Domínio (`domain/`)

| Componente | Arquivo | Responsabilidade |
| --- | --- | --- |
| `Empenho` | `entities/empenho.py` | Raiz do agregado da despesa; máquina de estados e invariantes de saldo |
| `Liquidacao` | `entities/liquidacao.py` | Comprovante do direito adquirido |
| `Pagamento` | `entities/pagamento.py` | Ordem bancária e efetivação |
| `ContaContabil` | `entities/conta.py` | Plano de contas do PCASP |
| `LancamentoContabil` | `entities/lancamento.py` | Lançamento por partidas dobradas |
| `Partida` | `entities/lancamento.py` | Objeto de valor da partida dobrada |
| `ConciliacaoContabil` | `entities/lancamento.py` | Comparação entre contábil e extrato |
| Exceções | `exceptions.py` | 13 exceções de negócio |

**Enumerações:** `StatusEmpenho`, `TipoEmpenho`, `StatusLiquidacao`,
`StatusPagamento`, `StatusLancamento`, `StatusConciliacao`, `TipoPartida`.

**Estruturas de máquina de estados:** `TRANSICOES_EMPENHO`,
`ESTADOS_TERMINAIS_EMPENHO`, `TRANSICOES_LIQUIDACAO`,
`ESTADOS_TERMINAIS_LIQUIDACAO`.

**Propriedades derivadas:** `valor_liquido`, `saldo_a_liquidar`, `saldo_a_pagar`,
`balanceado`, `pode_receber_lancamento`, `is_active`, `is_terminal`.

**Camadas ausentes:** `domain/events`, `domain/value_objects` e `domain/services` —
o módulo é um dos dois do sistema sem essas pastas (achado M-01).

## 3.2 Aplicação (`application/`)

| Componente | Responsabilidade |
| --- | --- |
| `use_cases_execucao.py` | `EmitirEmpenhoUseCase`, `AnularEmpenhoUseCase`, `LiquidarEmpenhoUseCase`, `PagarLiquidacaoUseCase` |
| `use_cases_contabil.py` | `CriarContaUseCase`, `LancarContabilUseCase`, `ConciliarContaUseCase` |
| `interfaces.py` | Ports `RepositorioEmpenho`, `RepositorioLiquidacao`, `RepositorioPagamento`, `RepositorioContaContabil`, `RepositorioLancamento`, `RepositorioConciliacao` |

Os ports são `Protocol`, o que permite inversão de dependência sem acoplamento a
framework.

## 3.3 Infraestrutura (`infrastructure/`)

| Componente | Responsabilidade |
| --- | --- |
| `database/models.py` | `EmpenhoModel`, `LiquidacaoModel`, `PagamentoModel` |
| `database/models_contabil.py` | `ContaContabilModel`, `LancamentoModel`, `ConciliacaoModel` |
| `repositories/sqlalchemy_empenho_repository.py` | `SQLAlchemyEmpenhoRepository` |
| `repositories/sqlalchemy_liq_pag_repository.py` | `SQLAlchemyLiquidacaoRepository`, `SQLAlchemyPagamentoRepository` |
| `repositories/sqlalchemy_conta_repository.py` | `SQLAlchemyContaRepository` |
| `repositories/sqlalchemy_lanc_conc_repository.py` | `SQLAlchemyLancamentoRepository`, `SQLAlchemyConciliacaoRepository` |

**Observação estrutural:** `models.py` e `models_contabil.py` **definem bases
declarativas distintas** (`Base` próprio e `declarative_base()` separado). Isso divide
o metadado ORM em dois blocos e dificulta a introspecção conjunta (achado A-05).

## 3.4 Apresentação (`presentation/`)

| Componente | Responsabilidade |
| --- | --- |
| `api/execucao_endpoints.py` | Router de execução: empenho, liquidação, anulação, pagamento |
| `api/contabil_endpoints.py` | Router contábil: contas, lançamentos, conciliações |
| `api/base.py` | Factories de repositório via dependência FastAPI |
| `schemas/con_schemas.py` | 16 schemas Pydantic |

**Prefixo:** `/api/v1/con` · **Tag:** `Contabilidade Pública`

---

# 4. Fluxo de uma Requisição

```text
Cliente HTTP
    │
    ▼
Middleware (correlação, autenticação)
    │
    ▼
Endpoint (presentation/api)
    │  valida schema Pydantic
    │  injeta repositórios via Depends
    ▼
Caso de uso (application)
    │  executa regra de negócio
    │  manipula a entidade de domínio
    ▼
Entidade (domain)
    │  valida invariantes
    │  aplica transição de estado
    ▼
Port (application/interfaces)
    │
    ▼
Repositório (infrastructure)
    │
    ▼
PostgreSQL — schema con
```

O caso de uso devolve a entidade de domínio; a camada de apresentação a converte em
schema de resposta.

---

# 5. Catálogo de Serviços

| Serviço | Caso de uso | Repositórios necessários |
| --- | --- | --- |
| SVC-CON-001 Emissão | `EmitirEmpenhoUseCase` | Empenho, Dotação (DOM-ORC) |
| SVC-CON-002 Liquidação | `LiquidarEmpenhoUseCase` | Empenho, Liquidação |
| SVC-CON-003 Anulação | `AnularEmpenhoUseCase` | Empenho, Dotação (DOM-ORC) |
| SVC-CON-004 Pagamento | `PagarLiquidacaoUseCase` | Empenho, Liquidação, Pagamento |
| SVC-CON-005 Criar conta | `CriarContaUseCase` | Conta |
| SVC-CON-006 Lançar | `LancarContabilUseCase` | Lançamento, Conta |
| SVC-CON-007 Conciliar | `ConciliarContaUseCase` | Conciliação |

---

# 6. Pontos de Extensão

| Ponto | Implementação atual | Ponto de extensão previsto |
| --- | --- | --- |
| Persistência | SQLAlchemy + PostgreSQL | Outro repositório via port `Protocol` |
| Autenticação | DOM-IDN (não aplicado ao domínio) | Middleware de autorização por operação |
| Documentos | Texto livre | Cliente do DOM-GDO |
| Notificações | Inexistente | Barramento de eventos |
| Relatórios | Inexistente | Serviço de consulta da execução |

A definição dos ports como `Protocol` permite substituir a persistência sem alterar o
domínio nem a aplicação.

---

# 7. Estado da Arquitetura

| Aspecto | Situação |
| --- | --- |
| Arquitetura hexagonal | Estruturalmente correta |
| Inversão de dependência | Ports como `Protocol` |
| Regra de dependência | Respeitada |
| Testabilidade do domínio | Boa — sem dependência externa |
| Exposição HTTP | **Inexistente** (C-01) |
| Eventos de domínio | **Inexistentes** (M-01) |
| Objetos de valor | **Inexistentes** (M-01) |
| Tipagem | 131 erros (A-05) |
| Metadado ORM unificado | **Não** — duas bases declarativas |

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 015-Arquitetura-de-Servicos-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
