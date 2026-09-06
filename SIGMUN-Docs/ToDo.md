# ToDo — `DOM-GDO` — Gestão Documental

> **Domínio:** Gestão Documental (`DOM-GDO`)
> **Projeto:** SIGMUN — Sistema Integrado de Gestão Municipal (Camacan-BA)
> **Base:** Onda 2 — Domínios Mestres e Transversais (ROADMAP §5)
> **Ambiente:** `/home/gildazio/Projetos-Python/sigmun-v1/sigmun-v1`
> **Python venv:** `.venv/bin/python` (pytest 9.1.1 — validado)
> **Referência técnica:** módulo `sigmun_met` (DOM-MET, implementação mais recente)
> **Data:** 2026-09-01

---

## 5.2 Domínios

### Visão do domínio

Conforme o ROADMAP (§5.2) e o Mapa de Domínios, o **`DOM-GDO` — Gestão Documental** é responsável por:

- **documentos** (criação, armazenamento, recuperação, conteúdo binário);
- **classificação** (planos/códigos documentais, estrutura hierárquica);
- **versionamento** (controle de versões, integridade via hash SHA-256);
- **retenção** (prazos por tipo documental);
- **arquivamento** (fases do ciclo de vida: corrente → intermediário → permanente);
- **temporalidade** (tabela de temporalidade, destinação final: eliminação ou guarda permanente).

Relaciona-se com: Gestão de Processos, Protocolo, Segurança (`DOM-SEG`), Governança de Dados (`DOM-DAD`/`DOM-MET`), Cadastro (`DOM-CUM`) e Identidade (`DOM-IDN`).

### Escopo implementado alvo (referência DOM-MET)

| Capacidade | Alvo |
|---|---|
| Entidades de domínio | 5 (Documento, VersaoDocumento, ClassificacaoDocumental, TabelaTemporalidade, Arquivamento) |
| Repositórios SQLAlchemy | 5 |
| Tabelas (schema `gdo`) | 5 |
| Casos de uso | ~24 |
| Endpoints REST (`/api/v1/gdo`) | ~30 |
| Testes unitários | ≥ 36 (repositórios em memória) |

### Dependências

- **Pré-requisito documental:** artefatos `SIGMUN-Docs/DOM-GDO/001` a `026` estão todos como **"Em elaboração"** (esboços). O ROADMAP §10 condiciona a promoção do domínio à existência de todos eles. → tratados na **Fase 0**.
- **Pré-requisito técnico:** `DOM-IDN` (autenticação/autorização), `DOM-CUM` (unidades/pessoas), `DOM-MET` (taxonomias/metadados).
- **Infraestrutura:** PostgreSQL ativo (docker-compose) para migrações e testes de integração; filesystem/S3-compatível para conteúdo binário (abstração por interface).

---

## Fase 0 — Pré-requisitos documentais (artefatos do domínio)

O ROADMAP §10 exige, para promoção: mapa de atores, capacidades, processos, serviços, casos de uso, histórias de usuário, regras de negócio, requisitos (funcionais/não-funcionais), especificações, critérios de aceitação, matriz de rastreabilidade, modelo de dados, modelo de integração, arquitetura de serviços, modelo de segurança, modelo de auditoria, plano de testes, casos de teste, estrutura técnica, plano de implantação, plano de migração.

- [x] **0.1** Revisar e consolidar o `000-Dominio-Gestao-Documental.md` (já ✅ no Plano de Trabalho). ✅ *Concluído — arquivo consolidado (v1.0, status Vigente).*
- [x] **0.2** Elaborar `001-Mapa-de-Atores-Gestao-Documental.md` — atores: Servidor/Gestor Documental, Autoridade Homologadora, Público (consulta), Administrador GDO. ✅ *Concluído em 2026-09-01 — 318 linhas, 15 seções (identificação, princípios, conceito, classificação, atores internos/externos/institucionais/controle/apoio, sistemas externos, ciclo de vida, segregação de funções, perfis DOM-IDN, identificador ACT-MAP-GDO-001).*
- [x] **0.3** Elaborar `002-Mapa-de-Capacidades-Gestao-Documental.md`. ✅ *Concluído em 2026-09-01 — 314 linhas, 13 seções (11 capacidades nível 1, 42 nível 2, relacionamentos com atores/domínios/ciclo de vida, indicadores, identificador ACT-CAP-GDO-001).*
- [x] **0.4** Elaborar `003-Mapa-de-Processos-Gestao-Documental.md` — fluxo captura → classificação → tramitação → arquivamento → destinação. ✅ *Concluído em 2026-09-01 — 647 linhas, 21 seções (11 processos, fluxos de trabalho, atividades, regras de negócio, indicadores, relacionamentos, identificador ACT-PRO-GDO-001).*
- [x] **0.5** Elaborar `004-Mapa-de-Servicos-Gestao-Documental.md` — serviços REST internos e expostos. ✅ *Concluído em 2026-09-01 — 392 linhas, 18 seções (9 routers, ~50 endpoints, schemas, relacionamentos, identificador ACT-SER-GDO-001).*
- [x] **0.6** Elaborar `005-Casos-de-Uso-Gestao-Documental.md` — ~24 casos de uso (ver Fase 3).
- [x] **0.7** Elaborar `006-Historias-de-Usuario-Gestao-Documental.md`. ✅ *Concluído — 44 histórias de usuário, 21 seções.*
- [x] **0.8** Elaborar `007-Regras-de-Negocio-Gestao-Documental.md` (RN-GDO-001..005). ✅ *Concluído — 28 regras, 21 seções.*
- [x] **0.9** Elaborar `008-Requisitos-Funcionais` e `009-Requisitos-Nao-Funcionais`. ✅ *Concluído — 48 RF + 33 RNF.*
- [x] **0.10** Elaborar `010-Especificacoes-Gestao-Documental.md` + `011-Criterios-de-Aceitacao-Gestao-Documental.md`. ✅ *Concluído — 11 especificações + 32 critérios.*
- [x] **0.11** Elaborar `012-Matriz-de-Rastreabilidade-Gestao-Documental.md`. ✅ *Concluído.*
- [x] **0.12** Elaborar `013-Modelo-de-Dados-Gestao-Documental.md`. ✅ *Concluído — 11 entidades.*
- [x] **0.13** Elaborar `014-Modelo-de-Integracao-Gestao-Documental.md`. ✅ *Concluído.*
- [x] **0.14** Elaborar `015-Arquitetura-de-Servicos` + `016-Modelo-de-Seguranca` + `017-Modelo-de-Auditoria`. ✅ *Concluído — 8 serviços, 5 perfis, 27 eventos.*
- [x] **0.15** Elaborar `018-Plano-de-Testes` + `019-Casos-de-Teste` + `025-Estrutura-Tecnica`. ✅ *Concluído.*
- [x] **0.16** Elaborar `020-Plano-de-Implantacao` + `022-Plano-de-Migracao-de-Dados` + `023-Plano-de-Treinamento` + `024-Plano-de-Suporte-e-Operacao`. ✅ *Concluído.*
- [x] **0.17** Atualizar status no Plano de Trabalho e ToDo:
  ```bash
  cd /home/gildazio/Projetos-Python/sigmun-v1/sigmun-v1
  .venv/bin/python scripts/atualizar_tabela_plano.py
  ```

> **Aceite Fase 0:** todos os artefatos `001`–`026` com `**Status:** Vigente` (não mais "Em elaboração").

---

## Ciclo 1 — Fundação Técnica (scaffolding do módulo)

Infraestrutura, configuração, padrões e componentes compartilhados. Replica a estrutura validada do `sigmun_met`.

- [ ] **1.1** Criar a árvore de diretórios do módulo `sigmun_gdo`:
  ```bash
  cd /home/gildazio/Projetos-Python/sigmun-v1/sigmun-v1/src/modules
  mkdir -p sigmun_gdo/{domain/{entities,value_objects,services,events},application/{interfaces,use_cases},infrastructure/{database,repositories},presentation/{api,schemas}}
  touch sigmun_gdo/__init__.py
  touch sigmun_gdo/domain/__init__.py sigmun_gdo/domain/entities/__init__.py
  touch sigmun_gdo/domain/value_objects/__init__.py sigmun_gdo/domain/services/__init__.py
  touch sigmun_gdo/domain/events/__init__.py sigmun_gdo/domain/exceptions.py
  touch sigmun_gdo/application/__init__.py sigmun_gdo/application/interfaces/__init__.py
  touch sigmun_gdo/application/use_cases/__init__.py
  touch sigmun_gdo/infrastructure/__init__.py sigmun_gdo/infrastructure/database/__init__.py
  touch sigmun_gdo/infrastructure/repositories/__init__.py
  touch sigmun_gdo/presentation/__init__.py sigmun_gdo/presentation/api/__init__.py
  touch sigmun_gdo/presentation/schemas/__init__.py
  ```
- [ ] **1.2** Criar arquivos de teste:
  ```bash
  cd /home/gildazio/Projetos-Python/sigmun-v1/sigmun-v1/tests
  touch tests/unit/test_gdo_documento_use_cases.py
  touch tests/unit/test_gdo_versao_use_cases.py
  touch tests/unit/test_gdo_classificacao_use_cases.py
  touch tests/unit/test_gdo_temporalidade_use_cases.py
  touch tests/unit/test_gdo_arquivamento_use_cases.py
  touch tests/integration/test_gdo_api.py
  ```
- [ ] **1.3** Garantir dependências (já em `requirements.txt`): `fastapi`, `sqlalchemy>=2.0`, `alembic`, `psycopg2-binary`, `pydantic>=2`, `python-multipart` (upload).
- [ ] **1.4** Confirmar Docker/Postgres disponível:
  ```bash
  cd /home/gildazio/Projetos-Python/sigmun-v1/sigmun-v1
  make docker-up
  ```

> **Aceite Ciclo 1:** estrutura de módulo criada, venv com dependências, Postgres no ar.


---

## Ciclo 2 — Núcleo do Domínio (entidades, agregados, estados, regras essenciais)

- [ ] **2.1** `domain/value_objects/__init__.py` — Value Objects e Enumerações:
  - `TipoDocumental` (Enum): `DESPACHO`, `PARECER`, `MEMORANDO`, `OFICIO`, `ATA`, `CONTRATO`, `PORTARIA`, `RESOLUCAO`, `PROCESSO_ADMINISTRATIVO`, `OUTRO`.
  - `StatusDocumento` (Enum): `RASCUNHO`, `ATIVO`, `ARQUIVADO_CORRENTE`, `ARQUIVADO_INTERMEDIARIO`, `GUARDA_PERMANENTE`, `ELIMINACAO_AUTORIZADA`, `ELIMINADO`.
  - `FaseCicloVida` (Enum): `CORRENTE`, `INTERMEDIARIA`, `PERMANENTE`.
  - `DestinacaoFinal` (Enum): `ELIMINACAO`, `GUARDA_PERMANENTE`.
  - `CodigoDocumental` (Value Object) — valida formato `AAA-NNNN/AAAA`.
  - `HashIntegridade` (Value Object) — calcula/valida SHA-256 do conteúdo.
- [ ] **2.2** `domain/entities/__init__.py` — Entidades e agregados:
  - **`Documento`** (agregado raiz): `id`, `codigo` (único), `titulo`, `tipo_documental`, `classificacao_id`, `conteudo_ref` (path/URI no storage), `hash_integridade`, `versao_atual` (int), `status`, `unidade_autor_id` (FK DOM-CUM), `autor_id` (FK DOM-IDN), `processo_ref` (opcional), `created_at`, `updated_at`, `is_deleted`; métodos `arquivar()`, `eliminar_autorizar()`, `guardar_permanente()`, `restaurar()`.
  - **`VersaoDocumento`**: `id`, `documento_id` (FK), `numero_versao`, `conteudo_ref`, `hash_integridade`, `autor_id`, `motivo_alteracao`, `created_at`; regra: versão é **imutável** após criação.
  - **`ClassificacaoDocumental`** (hierárquica, como taxonomia MET): `id`, `codigo` (único), `nome`, `descricao`, `pai_id` (auto-ref), `nivel`, `created_at`; método de validação anti-ciclo.
  - **`TabelaTemporalidade`**: `id`, `classificacao_id` (FK), `fase_corrente_dias`, `fase_intermediaria_dias`, `destinacao_final` (Enum), `fundamentacao_legal`, `created_at`.
  - **`Arquivamento`**: `id`, `documento_id` (FK), `unidade_origem_id` (FK CUM), `unidade_destino_id` (FK CUM), `data_envio`, `data_recebimento`, `status` (ENVIADO/RECEBIDO/EM_TRAMITE), `observacao`, `created_at`.
- [ ] **2.3** `domain/services/__init__.py` — Serviços de domínio:
  - `TemporalidadeService.calcular_fase(documento, tabela) → FaseCicloVida` — decide a fase com base nas datas de referência e prazos.
  - `TemporalidadeService.prever_destinacao(tabela, fase_atual) → DestinacaoFinal`.
  - `VersionamentoService.nova_versao(documento, conteudo_bytes, autor_id, motivo) → VersaoDocumento` — gera hash SHA-256, incrementa `versao_atual`.
- [ ] **2.4** `domain/events/__init__.py` — Eventos de domínio: `DocumentoCriado`, `VersaoCriada`, `DocumentoClassificado`, `DocumentoArquivado`, `DocumentoEmTramite`, `EliminacaoAutorizada`, `DocumentoGuardadoPermanente`.
- [ ] **2.5** `domain/exceptions.py` — Exceções: `DocumentoJaExisteError`, `DocumentoNaoEncontradoError`, `CodigoDocumentalInvalidoError`, `IntegridadeVioladaError`, `VersaoImutavelError`, `ClassificacaoNaoEncontradaError`, `ClassificacaoJaExisteError`, `HierarquiaCiclicaError`, `TemporalidadeNaoDefinidaError`, `OperacaoNaoPermitidaError`, `ArquivamentoNaoEncontradoError`, `DocumentoNaoArquivavelError`.

> **Aceite Ciclo 2:** núcleo compila sem erros de import; enums, entidades, VOs, serviços, eventos e exceções implementados.


---

## Ciclo 3 — Aplicação (casos de uso e serviços de aplicação)

Interfaces (portas) e ~24 use cases distribuídos por agregado.

- [ ] **3.1** `application/interfaces/__init__.py` — Protocolos de repositório (5): `DocumentoRepositoryInterface`, `VersaoDocumentoRepositoryInterface`, `ClassificacaoRepositoryInterface`, `TemporalidadeRepositoryInterface`, `ArquivamentoRepositoryInterface` (cada um com `get_by_id`, `save`, `delete`, `list_all`, e métodos específicos como `get_by_codigo`, `list_by_status`, `list_by_documento`).
- [ ] **3.2** `application/use_cases/__init__.py` — re-exports de todos os use cases.
- [ ] **3.3** `application/use_cases/documento_use_cases.py`:
  - `CriarDocumentoUseCase`, `BuscarDocumentoUseCase`, `AtualizarDocumentoUseCase`, `DeletarDocumentoUseCase` (soft-delete), `ListarDocumentosUseCase` (filtros: status, tipo, classificação, paginação), `RestaurarDocumentoUseCase`, `ArquivarDocumentoUseCase`, `AutorizarEliminacaoUseCase`, `GuardarPermanenteUseCase`.
- [ ] **3.4** `application/use_cases/versao_documento_use_cases.py`:
  - `CriarVersaoDocumentoUseCase` (upload de conteúdo → hash), `ListarVersoesUseCase`, `BuscarVersaoUseCase`, `RestaurarVersaoUseCase`, `VerificarIntegridadeUseCase`.
- [ ] **3.5** `application/use_cases/classificacao_use_cases.py`:
  - `CriarClassificacaoUseCase`, `BuscarClassificacaoUseCase`, `AtualizarClassificacaoUseCase`, `DeletarClassificacaoUseCase`, `ListarClassificacoesUseCase`, `ListarFilhosUseCase`.
- [ ] **3.6** `application/use_cases/temporalidade_use_cases.py`:
  - `CriarTemporalidadeUseCase`, `BuscarTemporalidadeUseCase`, `AtualizarTemporalidadeUseCase`, `DeletarTemporalidadeUseCase`, `ListarTemporalidadesUseCase`, `AvaliarFaseDocumentoUseCase`, `AplicarTemporalidadeUseCase`.
- [ ] **3.7** `application/use_cases/arquivamento_use_cases.py`:
  - `RegistrarArquivamentoUseCase` (envio), `ReceberArquivamentoUseCase`, `ListarArquivamentosUseCase`, `BuscarArquivamentoUseCase`, `TransferirDocumentoUseCase`.
- [ ] **3.8** `application/interfaces/storage.py` (opcional, Fase 5) — abstração `ContentStorageInterface` (put/get/delete) para o conteúdo binário; implementação local em Fase 5.

> **Aceite Ciclo 3:** todos os use cases importáveis; lógica de aplicação testável via repositórios em memória.


---

## Ciclo 4 — Interface (modelos ORM, migração, APIs e schemas)

Modelos ORM, migração Alembic, schemas Pydantic e endpoints REST (~30 endpoints em `/api/v1/gdo`).

- [ ] **4.1** `infrastructure/database/models.py` — Modelos SQLAlchemy (schema `gdo`) com base `GdoBase(DeclarativeBase)`:
  - `DocumentoModel` (`gdo.documentos`), `VersaoDocumentoModel` (`gdo.versoes_documento`), `ClassificacaoDocumentalModel` (`gdo.classificacoes_documentais`), `TemporalidadeModel` (`gdo.tabelas_temporalidade`), `ArquivamentoModel` (`gdo.arquivamentos`).
  - Todos com colunas de auditoria (`created_at/by`, `updated_at/by`, `deleted_at/by`) — padrão do `sigmun_met`.
- [ ] **4.2** Migração Alembic (próxima revisão após `20260901_01`):
  ```bash
  cd /home/gildazio/Projetos-Python/sigmun-v1/sigmun-v1
  .venv/bin/alembic revision -m "gdo documentos versoes classificacoes temporalidades arquivamentos"
  ```
  Gerar em `alembic/versions/20260901_02_gdo_*.py` com `revision = "20260901_02"`, `down_revision = "20260901_01"`, usando os helpers `uuid_column()` e `audit_columns()` (padrão da migração MET), `CREATE SCHEMA IF NOT EXISTS gdo`, `CheckConstraints` (status, tipo, destinacao), `ForeignKeys` e `indexes`. Testar:
  ```bash
  make migrate        # aplica
  make migrate-down   # rollback -1
  make migrate        # aplica novamente
  ```
- [ ] **4.3** `infrastructure/repositories/sqlalchemy_*.py` — 5 repositórios SQLAlchemy implementando as interfaces do Ciclo 3, com soft-delete, filtros e paginação.
- [ ] **4.4** `presentation/schemas/__init__.py` — Schemas Pydantic v2 (CreateRequest, UpdateRequest, Response, ListResponse) para cada agregado + `ErrorResponse`.
- [ ] **4.5** `presentation/api/__init__.py` — `APIRouter(prefix="/api/v1/gdo", tags=["gdo"])` com ~30 endpoints:
  - `POST /documentos`, `GET /documentos`, `GET /documentos/{id}`, `PATCH /documentos/{id}`, `DELETE /documentos/{id}`, `POST /documentos/{id}/arquivar`, `POST /documentos/{id}/autorizar-eliminacao`, `POST /documentos/{id}/guarda-permanente`.
  - `POST /documentos/{id}/versoes` (upload multipart), `GET /documentos/{id}/versoes`, `GET /versoes/{id}`, `POST /versoes/{id}/restaurar`, `POST /versoes/{id}/verificar-integridade`.
  - `POST /classificacoes`, `GET /classificacoes`, `GET /classificacoes/{id}`, `PATCH /classificacoes/{id}`, `DELETE /classificacoes/{id}`, `GET /classificacoes/{id}/filhos`.
  - `POST /temporalidades`, `GET /temporalidades`, `GET /temporalidades/{id}`, `PATCH /temporalidades/{id}`, `DELETE /temporalidades/{id}`, `POST /temporalidades/avaliar`.
  - `POST /arquivamentos`, `GET /arquivamentos`, `GET /arquivamentos/{id}`, `POST /arquivamentos/{id}/receber`, `POST /arquivamentos/transferir`.
  - Tratamento de exceções de domínio → HTTP (404/409/422) via `HTTPException`.
- [ ] **4.6** Registrar o router no `src/main.py` (junto aos demais):
  ```python
  from src.modules.sigmun_gdo.presentation.api import router as gdo_router
  ...
  app.include_router(gdo_router)
  ```
  Verificar:
  ```bash
  cd /home/gildazio/Projetos-Python/sigmun-v1/sigmun-v1
  make run-dev        # uvicorn com reload em :8000
  # conferir /docs (Swagger) → seção "gdo" listada
  ```

> **Aceite Ciclo 4:** migração aplicada; API documentada no Swagger com seção `gdo`; `GET /api/v1/gdo/documentos` responde 200.


---

## Ciclo 5 — Integrações (outros domínios e storage)

- [ ] **5.1** Integração **DOM-IDN**: dependência de autenticação nos endpoints (obter `current_user`); `autor_id`/`created_by` derivados do token.
- [ ] **5.2** Integração **DOM-CUM**: validar `unidade_autor_id` contra `core.unidades`; `unidade_origem_id/destino_id` contra cadastro.
- [ ] **5.3** Integração **DOM-MET**: vincular `classificacao_id` a termos de taxonomia (metadados semânticos), se aplicável.
- [ ] **5.4** Integração **DOM-COMPRAS**: expor endpoint `GET /api/v1/gdo/documentos?processo_tipo=compras&processo_id={id}` para o módulo de compras anexar documentos (consolida o `processo_documental` atualmente em `sigmun_compras`).
- [ ] **5.5** **Storage de conteúdo**: implementar `LocalContentStorage` (interface `ContentStorageInterface`) salvando bytes em `STORAGE_ROOT/{documento_id}/{versao}.bin` e registrando `conteudo_ref`; calcular `hash_integridade` SHA-256 no `CriarVersaoDocumentoUseCase`.
- [ ] **5.6** **API de upload/download**: `POST /documentos/{id}/versoes` (`multipart/form-data`, campo `arquivo`) e `GET /versoes/{id}/conteudo` (stream do binário).

> **Aceite Ciclo 5:** upload de documento gera versão com hash; download retorna o binário; cross-check com CUM/IDN funcional.

---

## Ciclo 6 — Segurança e Auditoria

- [ ] **6.1** Controle de acesso por operação: apenas `GESTOR_DOCUMENTAL` arquiva/elimina; `AUTORIDADE` autoriza eliminação/guarda permanente — usar roles/permissions do `DOM-IDN`.
- [ ] **6.2** Auditoria: registrar todas as mutações (criação, versão, arquivamento, transferência, eliminação) com `created_by`/`updated_by` e, quando aplicável, log em `gdo.auditoria_documental` ou uso do `core.trilha_auditoria` (migração `20260822_01`).
- [ ] **6.3** **LGPD / dados sensíveis**: marcação de documentos com `TabelaTemporalidade` de restrição; não expor conteúdo sem autorização.
- [ ] **6.4** **Imutabilidade de versão**: garantir que `VersaoDocumentoModel` não sofre `UPDATE` de conteúdo/hash após criação (regra de aplicação + assertiva de teste).

> **Aceite Ciclo 6:** permissões aplicadas; auditoria registrada; versão imutável garantida.


---

## Ciclo 7 — Testes (unitários, integração, contratos, aceitação)

- [ ] **7.1** **Testes unitários** (repositórios em memória, padrão `test_met_use_cases.py`): um arquivo por agregado em `tests/unit/test_gdo_*_use_cases.py`. Meta ≥ 36 testes. Cobrir: criação, validações de negócio (código duplicado, integridade, imutabilidade de versão, hierarquia anti-ciclo, temporalidade), estados de documento, arquivamento.
- [ ] **7.2** Testar:
  ```bash
  cd /home/gildazio/Projetos-Python/sigmun-v1/sigmun-v1
  .venv/bin/python -m pytest tests/unit/test_gdo_*.py -v
  make test                       # suíte completa
  ```
- [ ] **7.3** **Testes de integração** (`tests/integration/test_gdo_api.py`): endpoints contra PostgreSQL (via `get_db`), incluindo upload multipart e verificação de integridade end-to-end.
- [ ] **7.4** Testar:
  ```bash
  make docker-up                  # sobe Postgres
  make migrate
  .venv/bin/python -m pytest tests/integration/test_gdo_api.py -v
  ```
- [ ] **7.5** **Cobertura**:
  ```bash
  make test-cov
  # meta: cobertura do módulo sigmun_gdo ≥ 85%
  ```

> **Aceite Ciclo 7:** todos os testes verdes; cobertura ≥ 85% no módulo.

---

## Ciclo 8 — Homologação

- [ ] **8.1** Executar suite completa e qualidade:
  ```bash
  cd /home/gildazio/Projetos-Python/sigmun-v1/sigmun-v1
  make test
  make lint
  make type-check
  ```
- [ ] **8.2** Validação manual no Swagger (`/docs`): fluxo completo criar documento → upload versão → classificar → arquivar → consultar temporalidade → destinar.
- [ ] **8.3** Validação com responsáveis pelo negócio (regras RN-GDO-001..005, casos de uso do `005-Casos-de-Uso-Gestao-Documental`).
- [ ] **8.4** Atualizar `021-Checklist-de-Prontidao-para-Producao-Gestao-Documental.md` com evidências.

> **Aceite Ciclo 8:** checklist de prontidão aprovado pelo negócio.

---

## Ciclo 9 — Implantação (publicação controlada)

- [ ] **9.1** Build/verificação final:
  ```bash
  cd /home/gildazio/Projetos-Python/sigmun-v1/sigmun-v1
  make clean
  make install-dev
  make test
  make lint
  ```
- [ ] **9.2** Migração em ambiente de homologação/produção:
  ```bash
  make migrate
  ```
- [ ] **9.3** Publicação controlada (usar scripts auxiliares `scripts/deploy_controlled_env.py` / `scripts/homologacao_compras.py` como referência).
- [ ] **9.4** Smoke test pós-deploy:
  ```bash
  curl -s http://localhost:8000/health
  curl -s http://localhost:8000/api/v1/gdo/documentos
  ```

> **Aceite Ciclo 9:** domínio operacional em ambiente controlado.

---

## Ciclo 10 — Operação (monitoramento, suporte, indicadores)

- [ ] **10.1** Observabilidade: logs estruturados (já via `logging_config`), correlação (`CorrelationIDMiddleware`); registrar métricas de GDO (documentos criados/arquivados/eliminados).
- [ ] **10.2** Suporte: `024-Plano-de-Suporte-e-Operacao-Gestao-Documental.md` em execução.
- [ ] **10.3** Indicadores documentais (arquitetura doc §25): volumes por tipo, tempo médio em fase corrente, documentos próximos à destinação.
- [ ] **10.4** **Backups**: incluir `conteudo_ref` (storage) na política de backup (arquitetura doc §6).

> **Aceite Ciclo 10:** domínio estável em operação, com monitoramento e indicadores.

---

## Definition of Done (critérios de promoção — ROADMAP §10 e §5.2)

O `DOM-GDO` somente será considerado implementado quando cumprir **todos** os critérios abaixo:

- [ ] Todos os artefatos documentais (`001`–`026`) com `**Status:** Vigente`.
- [ ] Módulo `sigmun_gdo` completo: domínio, aplicação, infraestrutura e apresentação.
- [ ] 5 entidades de domínio, 5 repositórios SQLAlchemy, 5 tabelas (`schema gdo`).
- [ ] ~24 casos de uso implementados e testados.
- [ ] ~30 endpoints REST em `/api/v1/gdo` (Swagger documentado).
- [ ] Migração Alembic (`20260901_02`) aplicada e validada (up/down).
- [ ] ≥ 36 testes unitários (repositórios em memória) + testes de integração.
- [ ] Cobertura de testes do módulo ≥ 85%.
- [ ] Integrações com DOM-IDN, DOM-CUM, DOM-MET e DOM-COMPRAS funcionais.
- [ ] Segurança (roles/permissões) e auditoria ativas.
- [ ] Checklist de prontidão (`021`) aprovado.
- [ ] ROADMAP atualizado: entrada `DOM-GDO` em §5.2 com bloco "Implementação: módulo `sigmun_gdo` completo…" e status **🟢**.

---

## Rastreabilidade

| Fonte | Referência |
|---|---|
| ROADMAP | §5 Onda 2, §5.2 `DOM-GDO`, §9 (ordem 6, prioridade Alta), §10 (critérios de promoção), §11 (ciclos) |
| Arquitetura Corporativa | `030-Roadmap-de-Implementacao-dos-Dominios.md` (GDO), `012-Arquitetura-de-Gestao-Documental-e-Arquivistica.md` (28 seções) |
| Modelo de Negócio | `Mapa-de-Dominios.md` (Domínio 11 — Gestão Documental) |
| Plano de Trabalho | itens `000`–`026` DOM-GDO (`scripts/atualizar_tabela_plano.py`) |
| Padrão técnico | módulo `sigmun_met` (DOM-MET) — migração `20260901_01`, 36 testes, 30 endpoints |
| Decisões | `SIGMUN-Docs/DECISOES-ARQUITETURAIS.md` (registrar ADRs de GDO) |

---

**Responsável:** Equipe SIGMUN
**Próximo domínio após GDO:** `DOM-SEG` — Segurança da Informação (ordem 7, ROADMAP §9).
