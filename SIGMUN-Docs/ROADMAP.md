
# Roadmap de Implementação do SIGMUN

**Projeto:** SIGMUN - Sistema Integrado de Gestão Municipal

**Município:** Prefeitura Municipal de Camacan - Bahia

**Domínio:** Governança

**Versão:** 1.3

**Status:** Vigente

**Última atualização:** 2026-09-01

**Responsável:** Equipe SIGMUN

---

## 1. Situação de Partida

O SIGMUN possui a documentação corporativa, o modelo de negócio, o framework de requisitos e o domínio-piloto de Compras redigidos.

A implementação técnica ainda está no estágio de fundação: o backend possui scaffolding para módulos, a API possui endpoints técnicos, existem estruturas iniciais de infraestrutura e CI/CD, mas ainda não há implementação completa de módulos de negócio em produção.

O roadmap prioriza uma entrega vertical do `DOM-COMPRAS-001` para validar arquitetura, dados, segurança, APIs, testes e operação antes da expansão para os demais domínios.

O Mapa Consolidado de Domínios possui atualmente **33 domínios**, incluindo o `DOM-DIA — Gestão de Diárias`.

---

## 1.1 Classificação de Maturidade

| Categoria | Definição | Estado atual |
|---|---|---|
| Documentação | Artefatos que especificam, modelam ou governam o produto. | Documentação corporativa, arquitetural e de domínios em evolução contínua. |
| Scaffolding | Estruturas iniciais que preparam o desenvolvimento ou a operação. | Estruturas iniciais de aplicação, infraestrutura, API, banco e CI/CD. |
| Implementação real | Funcionalidade executável com regra de negócio, persistência, segurança, testes e evidência de operação. | DOM-COMPRAS-001 implementado e em operação controlada; DOM-CUM-001, DOM-IDN-001, DOM-DAD-001 e DOM-MET-001 implementados com repositórios SQLAlchemy, APIs REST e migrações. |

Documentação concluída não equivale a implementação real.

Scaffolding concluído indica preparação técnica, não capacidade operacional disponível.

Um domínio somente será considerado implementado quando cumprir os critérios técnicos, funcionais, de segurança, qualidade, auditoria, homologação e operação definidos neste roadmap e em sua documentação específica.

---

# 2. Princípios de Execução

A implementação do SIGMUN seguirá os seguintes princípios:

1. Validar a fundação antes de expandir domínios.
2. Implementar por fatias verticais, do dado à API e ao teste.
3. Manter rastreabilidade entre requisito, caso de uso, código e teste.
4. Tratar identidade, autorização, auditoria e LGPD como capacidades estruturais.
5. Automatizar qualidade, migrações, documentação e implantação desde o primeiro domínio.
6. Promover um domínio somente quando seus critérios de saída forem comprovados.
7. Evitar dependências diretas entre bancos de dados de domínios.
8. Utilizar APIs, eventos e contratos de integração para comunicação entre domínios.
9. Priorizar reutilização de capacidades corporativas.
10. Manter observabilidade desde as primeiras implementações.
11. Tratar dados corporativos como ativos compartilhados e governados.
12. Registrar alterações relevantes de arquitetura por meio de ADR.
13. Manter documentação e implementação sincronizadas.
14. Evoluir incrementalmente, evitando desenvolvimento isolado de grandes módulos.
15. Preservar a separação de responsabilidades entre domínios.

---

# 3. Ondas de Implementação

A implementação do SIGMUN será organizada em ondas.

As ondas representam uma estratégia arquitetural e de dependências. Isso não significa que todos os domínios de uma mesma onda serão obrigatoriamente implementados de forma simultânea.

---

## 3.1 Onda 0 - Fundação Técnica

**Status:** 🟡 Em andamento

**Objetivo:** tornar o framework executável, seguro, observável e repetível.

| Entrega | Situação |
|---|---|
| Estrutura FastAPI e Clean Architecture/DDD | 🟡 Scaffolding criado; implementação real em evolução |
| Configuração e gestão de ambientes | 🟡 Inicial |
| PostgreSQL | 🟢 Migrações `20260820_01` a `20260901_01` aplicadas (schemas `core`, `compras`, `idn`, `dad` e `met`) |
| SQLAlchemy | 🟢 Repositórios SQLAlchemy dos 6 agregados do DOM-COMPRAS-001 implementados e validados contra PostgreSQL (40 testes de integração; routers persistem via `infrastructure/database/models.py`) |
| Alembic | 🟢 Estrutura configurada; migration aplicada |
| Migrações | 🟢 Migrações `20260820_01` a `20260901_01` criadas e aplicadas (`core`, `compras`, `idn`, `dad`, `met`; tabelas, constraints, triggers e índices) |
| CI/CD | 🟡 Pipeline executando lint, migrações (`alembic upgrade head`) e suíte completa contra PostgreSQL em service container |
| Docker | 🟡 Scaffolding criado |
| Kubernetes | 🟡 Scaffolding/documentação |
| Terraform | 🟡 Scaffolding/documentação |
| Logging estruturado | ⚪ Pendente |
| Observabilidade | ⚪ Pendente |
| Identidade e autorização | 🟢 DOM-IDN-001 implementado: autenticação, autorização, usuários, roles, permissões, sessões e auditoria |
| Auditoria técnica | ⚪ Pendente |
| Testes automatizados | 🟡 Estrutura inicial |
| Quality gates | 🟡 Estrutura inicial |
| Gestão de configurações e segredos | ⚪ Pendente |

**Critério de saída:**

A aplicação inicial deverá executar com:

- banco de dados versionado;
- configuração segura;
- migrações reproduzíveis;
- pipeline de qualidade;
- logs estruturados;
- testes automatizados;
- tratamento padronizado de erros;
- documentação técnica mínima;
- ambiente reproduzível.

---

# 4. Onda 1 - DOM-COMPRAS-001

**Domínio:** Gestão de Compras e Contratações

**Código:** `DOM-COMPRAS-001`

**Status:** 🟡 Em andamento (processos documentais, contratos, integração de formalização, auditoria, OpenAPI, autorização e validações de negócio implementados; persistência real via repositórios SQLAlchemy sobre PostgreSQL implementada e validada (40 testes de integração; 301 testes na suíte); homologação automatizada aprovada (47/47); checklist de prontidão executado (2026-08-29) com resultado NÃO PRONTO para produção e pendências P-001 a P-010 registradas; próxima etapa: implantação em ambiente controlado (item 19))

**Objetivo:** implementar a primeira capacidade operacional ponta a ponta do SIGMUN.

O `DOM-COMPRAS-001` será o domínio-piloto utilizado para validar o padrão de construção dos demais domínios.

## 4.1 Sequência recomendada

1. Consolidar modelo de domínio de Compras.
2. Consolidar modelo físico de Compras e entidades compartilhadas.
3. ✅ Criar migrações para `core` e `compras` (migrations `20260820_01` e `20260821_01` criadas e aplicadas).
4. ✅ Implementar fornecedores (entidade, casos de uso, repositório SQLAlchemy, APIs REST e testes).
5. ✅ Implementar itens e produtos/serviços (entidade ItemCompra sobre `compras.itens_compras`, casos de uso, repositório SQLAlchemy e APIs REST).
6. ✅ Implementar solicitações e processos de compras (entidade Compra com máquina de estados processual sobre `compras.compras`, casos de uso, repositório SQLAlchemy e APIs REST; Requisição/Demanda – ENT-COMPRAS-001 – aguarda evolução do modelo físico).
7. ✅ Implementar processos documentais (entidade ProcessoDocumental sobre `core.processos_documentais` com unicidade numero/ano, casos de uso, repositório SQLAlchemy e APIs REST).
8. ✅ Implementar contratos (entidade Contrato sobre `compras.contratos` com máquina de estados e unicidade numero, casos de uso, repositório SQLAlchemy e APIs REST).
9. ✅ Implementar integrações necessárias (Formalização da Contratação Compra → Contrato com `compra_id`, migração `20260821_01`).
10. ✅ Expor APIs REST com OpenAPI (metadados, tags e schema `/openapi.json`; Docs e ReDoc).
11. ✅ Aplicar autorização (módulo compartilhado `shared/security` com autenticação por `X-Usuario-Id`/`X-Usuario-Papel` e guardas 401/403; aplicado à Formalização da Contratação).
12. ✅ Implementar auditoria (trilha append-only em `auditoria.eventos` — migration `20260822_01` com imutabilidade por trigger; ServicoDeAuditoria; consulta restrita por perfil em `/api/v1/auditoria` com auditoria do próprio acesso; eventos nas operações de contratos).
13. ✅ Implementar validações de negócio (guardas de domínio nas entidades Compra, Contrato, Fornecedor, ItemCompra e ProcessoDocumental: campos obrigatórios, valor não negativo, quantidade positiva (RN-COMPRAS-011/012), vigência coerente (RN-COMPRAS-037/046), transições da máquina de estados processual (RN-COMPRAS-026/027), estados terminais de compra e contrato (RN-COMPRAS-026/106) e bloqueio de operações sobre registros excluídos (RN-COMPRAS-004); exceções de domínio centralizadas em `domain/exceptions.py` (ex.: `ContratoDuplicadoError` RN-COMPRAS-036, `FornecedorJaCadastradoError` RN-COMPRAS-031, `OperacaoNaoPermitidaError`) mapeadas para respostas HTTP 400/404/409; validação/normalização de identificação do fornecedor (RN-COMPRAS-030/031); trilha de auditoria valida categoria/resultado dos eventos).
14. ✅ Criar testes unitários (entidade e casos de uso de Contrato).
15. ✅ Criar testes de integração (API de Contratos).
16. ✅ Criar testes de contratos de API (endpoints de Contratos com repositório em memória).
17. ✅ Executar homologação (roteiro E2E automatizado `scripts/homologacao_compras.py`, executado em 2026-08-29 sobre a aplicação real — uvicorn + HTTP — com repositórios em memória: 47/47 verificações aprovadas cobrindo funcionalidades da API (health/docs/OpenAPI), cadastros de fornecedores (RN-COMPRAS-030/031), processos documentais (RN-COMPRAS-028/029), itens de compra (RN-COMPRAS-011/012), ciclo processual da compra (RN-COMPRAS-026/027), Formalização da Contratação (UC-COMPRAS-022, RN-COMPRAS-036/038), ciclo de vida do contrato (RN-COMPRAS-046/106), exclusão lógica (RN-COMPRAS-004), permissões (401/403), auditoria (017, seções 40/41/44) e integridade referencial; suíte de testes com 261 aprovados; restrição registrada: Docker/PostgreSQL estavam indisponíveis no momento da homologação — ambiente provido em 2026-08-29 (Docker + PostgreSQL 15 via `docker compose`, schemas `core`/`compras`/`auditoria` criados e migrations `20260820_01` a `20260823_01` aplicadas no head), reexecução E2E sobre PostgreSQL a cargo da implantação em ambiente controlado (item 19); log em `SIGMUN-Docs/DOM-COMPRAS-001/evidencias/`).
18. ✅ Executar checklist de prontidão (reexecutado em 2026-08-29 após resolução das pendências P-001 a P-010 — resultado: PRONTO COM RESSALVAS para ambiente controlado; 261/261 testes aprovados; sistema saudável (API/banco/OpenAPI); evidência em `evidencias/2026-08-29-reexecucao-checklist-prontidao.md`).
19. ✅ Implantar em ambiente controlado (executado em 2026-08-29 — script `scripts/deploy_controlled_env.py` criado e validado; migrações aplicadas; 261/261 testes; health check OK; evidência em `evidencias/20260829_191412-deploy-ambiente-controlado.md`).
20. ✅ Iniciar operação monitorada (executado em 2026-08-29 — script `scripts/operations_monitor.py` criado com monitoramento contínuo, dashboard operacional, gestão de incidentes, alertas via webhook/email e backup automatizado; dashboard validado com sistema saudável (100% uptime, 0 incidentes); evidência em `evidencias/20260829_191412-deploy-ambiente-controlado.md`).
21. ✅ Implementar repositórios SQLAlchemy persistentes (executado em 2026-08-30 — 6 repositórios: `SqlAlchemyFornecedorRepository`, `SqlAlchemyProcessoDocumentalRepository`, `SqlAlchemyItemCompraRepository`, `SqlAlchemyCompraRepository`, `SqlAlchemyContratoRepository` e `SqlAlchemyTrilhaAuditoriaRepository`, em `infrastructure/repositories/`, sobre os models ORM de `infrastructure/database/models.py`, com exclusão lógica `deleted_at` (RN-COMPRAS-004), paginação e filtros; todos os routers passaram a persistir via PostgreSQL; migração `20260831_01` corrige omissão da coluna `situacao` em `compras.contratos` (RN-COMPRAS-046/106) com `server_default='EM_ELABORACAO'` e constraint de domínio; suíte `tests/integration/test_sqlalchemy_repositories.py` com 40 testes de integração validados contra PostgreSQL (Docker, porta 5433); suíte completa: 301 testes aprovados).
22. ✅ Wiring de persistência por ambiente e CI com banco (executado em 2026-08-30 — pipeline de CI aplica `alembic upgrade head` antes do `pytest` com service container PostgreSQL 15 (paridade com `docker-compose`) e variáveis `DB_*` explícitas, executando também os 40 testes de integração SQLAlchemy; `pyproject.toml` com `pythonpath` explícito; `/health` reporta conectividade com o banco (`database: 'up'/'down'`, degradação graciosa — endpoint segue HTTP 200 com `status: healthy` mesmo sem banco) e o startup registra o status do banco, com `engine.dispose()` no shutdown; `alembic/env.py` autossuficiente (`Base` local, sem depender de engine duplicado) e `shared/config/database.py` marcado como deprecated, consolidando engine/sessão em `core/infrastructure/database/session.py`; Makefile com alvo `test-integration`; suíte completa: 301 testes aprovados).

## 4.2 Critério de saída

O domínio será considerado implementado somente quando possuir:

- código executável;
- banco de dados;
- migrações;
- APIs;
- regras de negócio;
- segurança;
- autorização;
- auditoria;
- testes;
- observabilidade;
- documentação;
- implantação automatizada;
- homologação;
- operação controlada.

---

# 5. Onda 2 - Domínios Mestres e Transversais

**Status:** 🟡 Em andamento (slices 1 a 3 entregues: DOM-CUM, DOM-IDN, DOM-DAD e DOM-MET)

**Objetivo:** implementar os domínios que fornecem dados, identidade, serviços e capacidades corporativas reutilizáveis.

## 5.1 Entregas

### `DOM-CUM-001` — Cadastro Único Municipal (Pessoas e Unidades) 🟢

**Entrega:** módulo `sigmun_cadastro` com domínio, aplicação e infraestrutura completos.

**Escopo implementado:**
- **Agregado Pessoa** com extensão 1:1 (pessoa física/jurídica), endereços (histórico de vigência), documentos e contatos
- **Unidade Administrativa** hierárquica com validação de ciclos (RN-CUM-008)
- **Value Objects** CPF/CNPJ com validação de dígitos verificadores (RN-CUM-002/003)
- **15 use cases**: registro, consulta, listagem, atualização e exclusão de pessoas/unidades; adição de endereços/documentos/contatos
- **Repositórios SQLAlchemy** com sync de agregados, soft-delete em cascata e validação de unicidade
- **APIs REST** (`/api/v1/pessoas`, `/api/v1/unidades`) com paginação e filtros
- **Migração** `20260831_02`: tabelas `core.enderecos`, `core.documentos`, `core.contatos` + coluna `nome` em `pessoas_fisicas`

**Validação:** migração `20260831_03` criada; 8 tabelas no schema `idn` (usuarios, roles, permissoes, usuario_roles, role_permissoes, sessoes, auditoria_logins) com constraints, foreign keys e triggers.

### `DOM-IDN-001` — Identidade e Acesso 🟢

**Entrega:** módulo `sigmun_idn` com domínio, aplicação e infraestrutura completos.

**Escopo implementado:**
- **Entidades de domínio:** Usuario, Role, Permissao, Sessao, AuditoriaLogin
- **Value Objects:** Email, Senha, Login com validação
- **Serviços de domínio:** AutenticacaoService, AutorizacaoService, AuditoriaService
- **8 use cases:** CriarUsuario, AtivarUsuario, DesativarUsuario, BloquearUsuario, BuscarUsuario, AutenticarUsuario, Logout
- **5 repositórios SQLAlchemy:** Usuario, Role, Permissao, Sessao, AuditoriaLogin
- **APIs REST** (`/api/v1/idn`) com 8 endpoints
- **Migração** `20260831_03`: 7 tabelas no schema `idn` com relacionamentos N:N, triggers e indexes

### `DOM-DAD-001` — Dados Corporativos 🟢

**Entrega:** módulo `sigmun_dad` com domínio, aplicação e infraestrutura completos.

**Escopo implementado:**
- **Ativos de Dados** com ciclo de vida (ativo/inativo/arquivado) e ativação/desativação/arquivamento
- **Catálogos** com vinculação e remoção de ativos de dados
- **Linhagem de Dados** (relacionamentos origem → destino entre ativos)
- **Políticas de Governança** com regras associadas
- **Qualidade de Dados** com avaliação por dimensões e score
- **26 use cases** (criação, atualização, busca, listagem, exclusão e operações de composição)
- **5 repositórios SQLAlchemy** com soft-delete, filtros e paginação
- **APIs REST** (`/api/v1/dad`) com 29 endpoints
- **Migração** `20260831_04`: 5 tabelas no schema `dad` (ativos_dados, catalogos, linhagens, politicas, qualidade_dados) com constraints e triggers
- **37 testes unitários** com repositórios em memória; validação ponta a ponta contra PostgreSQL

### `DOM-MET-001` — Metadados Corporativos 🟢

**Entrega:** módulo `sigmun_met` com domínio, aplicação e infraestrutura completos.

**Escopo implementado:**
- **Metadados** com tipos de dado (texto, número, data, booleano, lista, JSON), obrigatoriedade, multi-valor e aplicabilidade por tipo de entidade, com ativação/desativação
- **Valores de Metadado** atribuídos a entidades (upsert por metadado+entidade) com validação por tipo de dado
- **Classificações** (confidencialidade, assunto, retenção, origem) com níveis
- **Taxonomias** hierárquicas com **Termos** (pai/filho), sinônimos, ordem e validação de ciclos
- **Value Objects** com validação de códigos, nomes, valores e entidades alvo
- **22 use cases**, incluindo atribuição/validação de valores e navegação hierárquica de termos
- **5 repositórios SQLAlchemy** com soft-delete, filtros e paginação
- **APIs REST** (`/api/v1/met`) com 30 endpoints (inclui `/taxonomias/{id}/termos` e `/termos/{id}/filhos`)
- **Migração** `20260901_01`: 5 tabelas no schema `met` (metadados, valores_metadados, classificacoes, taxonomias, termos_taxonomias) com constraints e triggers
- **36 testes unitários** com repositórios em memória; rotas validadas na aplicação

## 5.2 Domínios

### `DOM-CUM` — Cadastro Único Municipal 🟢

Responsável pelos cadastros corporativos compartilhados.

### `DOM-IDN` — Identidade e Acesso 🟢

Responsável por:

- identidade;
- autenticação;
- autorização;
- perfis;
- papéis;
- permissões;
- acesso institucional.

**Implementação:** módulo `sigmun_idn` completo com domínio, aplicação, infraestrutura e apresentação.

### `DOM-DAD` — Dados Corporativos 🟢

Responsável por:

- governança de dados;
- qualidade;
- catálogo;
- linhagem;
- políticas;
- compartilhamento;
- gestão dos ativos de dados.

**Implementação:** módulo `sigmun_dad` completo com domínio, aplicação, infraestrutura e apresentação (26 use cases, 5 repositórios SQLAlchemy e 29 endpoints em `/api/v1/dad`).

### `DOM-MET` — Metadados Corporativos 🟢

Responsável por:

- metadados;
- classificações;
- taxonomias;
- referências semânticas;
- padrões corporativos.

**Implementação:** módulo `sigmun_met` completo com domínio, aplicação, infraestrutura e apresentação (22 use cases, 5 repositórios SQLAlchemy e 30 endpoints em `/api/v1/met`).

### `DOM-GDO` — Gestão Documental

Responsável por:

- documentos;
- classificação;
- versionamento;
- retenção;
- arquivamento;
- temporalidade.

### `DOM-SEG` — Segurança da Informação

Responsável por:

- controles de segurança;
- políticas;
- proteção;
- incidentes;
- monitoramento;
- segurança corporativa.

### `DOM-INT` — Integração e Interoperabilidade

Responsável por:

- APIs;
- eventos;
- mensageria;
- integrações externas;
- interoperabilidade;
- contratos de integração.

### `DOM-GOV` — Governança Municipal

Responsável por:

- governança;
- políticas;
- decisões;
- conformidade;
- gestão institucional.

### `DOM-IND` — Indicadores e Desempenho

Responsável por:

- indicadores;
- métricas;
- painéis;
- acompanhamento de desempenho.

### Dependência

A implementação da Onda 2 deverá utilizar os padrões validados pelo `DOM-COMPRAS-001`.

---

# 6. Onda 3 - Núcleo Administrativo e Econômico-Financeiro

**Status:** ⚪ Planejada

**Objetivo:** implementar os principais processos administrativos e econômico-financeiros do município.

## 6.1 Domínios

- `DOM-PES` — Gestão de Pessoas
- `DOM-DIA` — Gestão de Diárias
- `DOM-ORC` — Orçamento Público
- `DOM-CON` — Contabilidade Pública
- `DOM-TRI` — Administração Tributária
- `DOM-PAT` — Gestão Patrimonial
- `DOM-FRO` — Gestão de Frota
- `DOM-PLA` — Planejamento Governamental
- `DOM-CPT` — Gestão de Competências

## 6.2 DOM-DIA — Gestão de Diárias

O `DOM-DIA` será tratado como **domínio próprio**, e não como simples funcionalidade de Gestão de Pessoas ou Contabilidade.

Seu objetivo será administrar o ciclo de vida das diárias, viagens e deslocamentos oficiais.

### Principais capacidades

- solicitação de diária;
- solicitação de viagem;
- justificativa;
- autorização;
- cálculo;
- concessão;
- definição de período;
- definição de destino;
- controle de deslocamento;
- antecipação;
- alteração;
- cancelamento;
- integração orçamentária;
- integração contábil;
- pagamento;
- prestação de contas;
- análise;
- aprovação;
- restituição;
- glosa;
- documentos;
- auditoria;
- transparência;
- indicadores.

### Integrações principais

O `DOM-DIA` deverá utilizar serviços e dados de outros domínios sem assumir suas responsabilidades internas.

| Domínio | Relação |
|---|---|
| `DOM-PES` | Dados do servidor/agente público |
| `DOM-ORC` | Controle e disponibilidade orçamentária |
| `DOM-CON` | Registros e integrações contábeis |
| `DOM-GDO` | Documentos e gestão documental |
| `DOM-IDN` | Identidade, autenticação e autorização |
| `DOM-DAD` | Dados corporativos |
| `DOM-INT` | Integrações |
| `DOM-IND` | Indicadores e desempenho |

### Dependência

A Onda 3 dependerá da consolidação das capacidades transversais necessárias, principalmente:

- Cadastro Único Municipal;
- Identidade e Acesso;
- Dados Corporativos;
- Gestão Documental;
- Segurança;
- Integração.

A ordem interna dos domínios poderá ser ajustada por ADR conforme dependências técnicas e de negócio.

---

# 7. Onda 4 - Domínios Finalísticos e Territoriais

**Status:** ⚪ Planejada

**Objetivo:** implementar os processos diretamente relacionados à prestação de serviços públicos e à gestão territorial.

## 7.1 Domínios

### Finalísticos

- `DOM-SAU` — Saúde Pública
- `DOM-EDU` — Educação Pública
- `DOM-ASS` — Assistência Social
- `DOM-MAM` — Meio Ambiente
- `DOM-DEC` — Desenvolvimento Econômico

### Territoriais

- `DOM-TEL` — Gestão Territorial
- `DOM-IMO` — Cadastro Imobiliário
- `DOM-GEO` — Geoinformação Municipal
- `DOM-OBR` — Obras e Infraestrutura

A implantação deverá considerar:

- criticidade;
- impacto social;
- dependências;
- maturidade;
- disponibilidade de dados;
- capacidade institucional;
- capacidade técnica;
- prioridade estratégica municipal.

---

# 8. Onda 5 - Atendimento, Mobilidade, Inteligência e Infraestrutura

**Status:** ⚪ Planejada

**Objetivo:** consolidar a interação do SIGMUN com cidadãos, servidores, gestores, dispositivos móveis, serviços externos e capacidades avançadas de inteligência.

## 8.1 Domínios

- `DOM-CUM` — Cadastro Único Municipal, quando houver capacidades de atendimento relacionadas
- `DOM-ATE` — Atendimento ao Cidadão
- `DOM-OUV` — Ouvidoria
- `DOM-MOB` — Mobilidade e Serviços de Campo
- `DOM-ANA` — Analytics e Inteligência
- `DOM-INF` — Infraestrutura Tecnológica

**Observação:** o `DOM-CUM` possui sua implementação estrutural na Onda 2. Sua reutilização pelas capacidades de atendimento ocorrerá progressivamente nas ondas posteriores.

---

# 9. Ordem Estratégica dos Domínios

A ordem de referência será:

| Ordem | Código | Domínio | Prioridade |
|---:|---|---|---|
| 0 | — | Fundação Técnica | Crítica |
| 1 | `DOM-COM` | Compras e Contratações | Crítica |
| 2 | `DOM-CUM` | Cadastro Único Municipal | Crítica |
| 3 | `DOM-IDN` | Identidade e Acesso | Crítica |
| 4 | `DOM-DAD` | Dados Corporativos | Crítica |
| 5 | `DOM-MET` | Metadados Corporativos | Alta |
| 6 | `DOM-GDO` | Gestão Documental | Alta |
| 7 | `DOM-SEG` | Segurança da Informação | Alta |
| 8 | `DOM-INT` | Integração e Interoperabilidade | Alta |
| 9 | `DOM-GOV` | Governança Municipal | Alta |
| 10 | `DOM-IND` | Indicadores e Desempenho | Alta |
| 11 | `DOM-PES` | Gestão de Pessoas | Alta |
| 12 | `DOM-DIA` | Gestão de Diárias | Alta |
| 13 | `DOM-ORC` | Orçamento Público | Alta |
| 14 | `DOM-CON` | Contabilidade Pública | Alta |
| 15 | `DOM-TRI` | Administração Tributária | Alta |
| 16 | `DOM-PAT` | Gestão Patrimonial | Alta |
| 17 | `DOM-FRO` | Gestão de Frota | Média/Alta |
| 18 | `DOM-PLA` | Planejamento Governamental | Média/Alta |
| 19 | `DOM-CPT` | Gestão de Competências | Média/Alta |
| 20 | `DOM-TEL` | Gestão Territorial | Média/Alta |
| 21 | `DOM-IMO` | Cadastro Imobiliário | Média/Alta |
| 22 | `DOM-GEO` | Geoinformação Municipal | Média/Alta |
| 23 | `DOM-OBR` | Obras e Infraestrutura | Média/Alta |
| 24 | `DOM-SAU` | Saúde Pública | Alta |
| 25 | `DOM-EDU` | Educação Pública | Alta |
| 26 | `DOM-ASS` | Assistência Social | Alta |
| 27 | `DOM-MAM` | Meio Ambiente | Média |
| 28 | `DOM-DEC` | Desenvolvimento Econômico | Média |
| 29 | `DOM-ATE` | Atendimento ao Cidadão | Alta |
| 30 | `DOM-OUV` | Ouvidoria | Alta |
| 31 | `DOM-ANA` | Analytics e Inteligência | Alta |
| 32 | `DOM-MOB` | Mobilidade e Serviços de Campo | Média/Alta |
| 33 | `DOM-INF` | Infraestrutura Tecnológica | Alta |

A ordem acima representa uma **linha de base arquitetural**.

A sequência de execução poderá ser alterada mediante ADR, desde que sejam registrados:

- motivo da alteração;
- dependências;
- impacto;
- riscos;
- benefícios;
- consequências arquiteturais;
- impacto no roadmap.

---

# 10. Critérios de Promoção de um Domínio

Um domínio somente poderá avançar para implementação quando possuir:

- mapa de atores;
- mapa de capacidades;
- mapa de processos;
- mapa de serviços;
- casos de uso;
- histórias de usuário;
- regras de negócio;
- requisitos funcionais;
- requisitos não funcionais;
- especificações;
- critérios de aceitação;
- matriz de rastreabilidade;
- modelo de domínio;
- modelo de dados;
- modelo de integração;
- arquitetura de serviços;
- modelo de segurança;
- modelo de auditoria;
- plano de testes;
- casos de teste;
- estrutura técnica;
- plano de implantação;
- plano de migração, quando aplicável;
- plano de treinamento;
- plano de suporte e operação.

---

# 11. Estratégia de Implementação Incremental

Cada domínio será desenvolvido em ciclos.

### Ciclo 1 — Fundação

Infraestrutura, configuração, padrões e componentes compartilhados.

### Ciclo 2 — Núcleo do Domínio

Entidades, agregados, estados e regras essenciais.

### Ciclo 3 — Aplicação

Casos de uso e serviços de aplicação.

### Ciclo 4 — Interface

APIs e interfaces de usuário.

### Ciclo 5 — Integrações

Comunicação com outros domínios e sistemas externos.

### Ciclo 6 — Segurança e Auditoria

Controles, autorização, logs e rastreabilidade.

### Ciclo 7 — Testes

Testes unitários, integração, contratos, aceitação e segurança.

### Ciclo 8 — Homologação

Validação com usuários e responsáveis pelo negócio.

### Ciclo 9 — Implantação

Publicação controlada.

### Ciclo 10 — Operação

Monitoramento, suporte, indicadores e evolução.

---

# 12. Estratégia de Dependências

Nenhum domínio deverá assumir diretamente estruturas internas de outro domínio.

A comunicação deverá ocorrer por meio de:

- APIs;
- serviços;
- eventos;
- contratos de integração;
- modelos compartilhados formalmente definidos;
- mecanismos de interoperabilidade.

Deve ser evitado:

- acesso direto ao banco de outro domínio;
- duplicação de cadastros mestres;
- regras de negócio copiadas;
- dependências ocultas;
- integrações não documentadas;
- compartilhamento não governado de tabelas.

Cada domínio deverá ser responsável pelo seu próprio modelo interno.

---

# 13. Primeiro Marco Técnico — M1

## M1 — Primeiro Domínio Executável do SIGMUN

**Domínio:** `DOM-COMPRAS-001`

O primeiro marco deverá resultar em um domínio operacional composto por:

```text
DOM-COMPRAS-001
       │
       ├── Backend
       ├── Banco de Dados
       ├── Migrações
       ├── API
       ├── Segurança
       ├── Auditoria
       ├── Testes
       ├── Documentação
       ├── Observabilidade
       └── Implantação

14. Marco M2 — Framework Corporativo Reutilizável

Após a implementação inicial do DOM-COMPRAS-001, os componentes reutilizáveis deverão ser consolidados como capacidades corporativas.

Exemplos:

autenticação;
autorização;
usuários;
organizações;
auditoria;
documentos;
notificações;
eventos;
configuração;
logs;
observabilidade;
tratamento de erros;
paginação;
filtros;
versionamento;
APIs;
mecanismos de integração.

O objetivo é reduzir o custo e o tempo de implementação dos domínios seguintes.

15. Marco M3 — Expansão dos Domínios Mestres

Após a validação do padrão técnico, serão progressivamente implementados:

DOM-CUM;
DOM-IDN;
DOM-DAD;
DOM-MET;
DOM-GDO;
DOM-SEG;
DOM-INT;
DOM-GOV;
DOM-IND.

Esses domínios deverão disponibilizar capacidades corporativas reutilizáveis pelos demais domínios.

16. Marco M4 — Núcleo Administrativo Integrado

Após a consolidação das capacidades transversais, o SIGMUN avançará para o núcleo administrativo e econômico-financeiro.

Entre os primeiros domínios desse núcleo estarão:

DOM-PES;
DOM-DIA;
DOM-ORC;
DOM-CON;
DOM-TRI;
DOM-PAT;
DOM-FRO;
DOM-PLA;
DOM-CPT.

O DOM-DIA deverá demonstrar integração efetiva entre gestão de pessoas, orçamento, contabilidade, documentos, identidade e auditoria.

17. Marco M5 — Integração Corporativa

O SIGMUN deverá evoluir de:

domínios isolados

para:

ecossistema integrado de domínios

com:

APIs;
eventos;
serviços compartilhados;
dados mestres;
governança;
observabilidade;
segurança;
auditoria;
interoperabilidade.
18. Marco M6 — Plataforma Municipal Integrada

O estado-alvo do SIGMUN será:

                         SIGMUN
                           │
             ┌─────────────┼─────────────┐
             │             │             │
          Negócio         Dados       Serviços
             │             │             │
             └─────────────┼─────────────┘
                           │
                      Integrações
                           │
             ┌─────────────┼─────────────┐
             │             │             │
          Governo       Cidadão       Sistemas

O SIGMUN deverá operar como uma plataforma integrada de gestão municipal, e não como um conjunto de aplicações independentes.

19. Próximos Marcos
Marco	Critério de conclusão	Status
Consolidação arquitetural	Revisão geral, glossário, diagramas e referências concluídos	🟡
Modelo físico corporativo	DDL revisado e decisões de ordem, índices, auditoria e LGPD registradas	🟡
Primeira migração	alembic upgrade head executa em ambiente limpo	🟡
Fundação executável	API, banco, testes, quality gates e observabilidade básicos	⚪
Primeira fatia de Compras	Fornecedor, compra e item disponíveis por API e testes	⚪
Homologação do piloto	Critérios de aceitação e checklist de prontidão aprovados	⚪
Framework reutilizável	Capacidades transversais extraídas e documentadas	⚪
Expansão transversal	CUM 🟢, IDN 🟢, DAD, MET, GDO, SEG, INT, GOV e IND priorizados	🟡
Primeira implementação de Diárias	DOM-DIA implementado e integrado aos domínios necessários	⚪
20. Critérios de Priorização

Cada nova entrega será priorizada pela combinação de:

dependência corporativa;
valor operacional;
risco;
disponibilidade de requisitos;
capacidade de reutilização;
impacto institucional;
impacto social;
maturidade dos dados;
capacidade técnica;
capacidade operacional;
exigências legais;
urgência administrativa.

Nenhum domínio será considerado implementado apenas por possuir documentação ou scaffolding.

21. Indicadores de Execução

Serão acompanhados, entre outros:

Indicador	Objetivo
Domínios implementados	Medir evolução real
Domínios em desenvolvimento	Medir execução
Domínios planejados	Medir backlog
Cobertura de requisitos	Medir completude
Cobertura de rastreabilidade	Medir governança
Cobertura de testes	Medir qualidade
Percentual de reutilização	Medir maturidade arquitetural
APIs de negócio implementadas	Medir capacidade operacional
Migrações executadas	Medir evolução do banco
Incidentes por domínio	Medir estabilidade
Disponibilidade	Medir operação
Tempo médio de entrega	Medir eficiência
Débito técnico	Medir sustentabilidade
Integrações ativas	Medir interoperabilidade
22. Governança do Roadmap

Alterações significativas na ordem de implementação deverão ser registradas como decisão arquitetural.

Deverão ser considerados:

impacto;
dependências;
riscos;
custo;
capacidade institucional;
maturidade;
urgência;
legislação;
disponibilidade de dados;
impacto social;
estratégia municipal;
capacidade técnica.

O roadmap é um instrumento vivo de governança e poderá evoluir conforme a implementação do SIGMUN produzir evidências reais.

23. Rastreabilidade

Este documento deverá manter rastreabilidade com:

SIGMUN-Docs/02-Modelo-de-Negocio/Mapa-de-Dominios.md;
SIGMUN-Docs/00-Governanca/000H-MAPA-MESTRE-DE-ARTIFATOS-E-RASTREABILIDADE.md;
SIGMUN-Docs/Plano-de-Trabalho.md;
SIGMUN-Docs/ROADMAP.md;
SIGMUN-Docs/DECISOES-ARQUITETURAIS.md;
ADRs;
documentação específica de cada domínio;
arquitetura corporativa;
requisitos;
modelos de dados;
arquitetura de serviços;
planos de implantação.
24. Diretriz Final

O roadmap deverá ser tratado como instrumento vivo de governança arquitetural.

A implementação do SIGMUN não será conduzida pela quantidade de telas produzidas, mas pela capacidade de construir progressivamente:

domínios coesos;
serviços reutilizáveis;
dados governados;
processos integrados;
segurança estruturada;
auditoria;
observabilidade;
rastreabilidade;
qualidade;
arquitetura sustentável.

O DOM-COMPRAS-001 será o primeiro domínio executável e servirá como referência arquitetural para os demais domínios.

O DOM-DIA — Gestão de Diárias será tratado como domínio próprio e deverá ser implementado como parte do núcleo administrativo e econômico-financeiro, mantendo integração controlada com Gestão de Pessoas, Orçamento, Contabilidade, Gestão Documental, Identidade, Dados e Integrações.

O objetivo final é transformar progressivamente a documentação arquitetural do SIGMUN em uma plataforma municipal integrada, executável, governada, segura, interoperável e sustentável.       