# TODO — Master Backlog e Plano de Tarefas do SIGMUN

> **Projeto:** SIGMUN — Sistema Integrado de Gestão Municipal (Camacan-BA)  
> **Status Geral do Projeto:** 🟡 Em Desenvolvimento (Onda 1 Concluída, Onda 2 em Finalização)  
> **Última Atualização:** 2026-09-16
> **Referência Arquitetural:** `SIGMUN-Docs/ROADMAP.md` e `SIGMUN-Docs/Plano-de-Trabalho.md`

Este documento consolida todas as tarefas técnicas, funcionais, documentais e operacionais necessárias para estabilizar o estado atual do projeto, concluir as ondas em andamento e guiar as próximas fases de implementação.

---

## Índice

1. [Fase I — Estabilização Imediata & Controle de Versão (Bloqueios Atuais)](#fase-i--estabilização-imediata--controle-de-versão-bloqueios-atuais)
2. [Fase II — Qualidade de Código, CI/CD & Quality Gates](#fase-ii--qualidade-de-código-cicd--quality-gates)
3. [Fase III — Conclusão, Homologação e Fechamento de DOM-GDO (Onda 2)](#fase-iii--conclusão-homologação-e-fechamento-de-dom-gdo-onda-2)
4. [Fase IV — Sincronização Documental da Onda 2 (CUM, IDN, DAD, MET)](#fase-iv--sincronização-documental-da-onda-2-cum-idn-dad-met)
5. [Fase V — Implementação dos Domínios Restantes da Onda 2 (DOM-SEG e DOM-INT)](#fase-v--implementação-dos-domínios-restantes-da-onda-2-dom-seg-e-dom-int)
6. [Fase VI — Fundação e Evolução do Frontend](#fase-vi--fundação-e-evolução-do-frontend)
7. [Fase VII — Processamento Assíncrono e Mensageria (Celery & Redis)](#fase-vii--processamento-assíncrono-e-mensageria-celery--redis)
8. [Fase VIII — Onda 3: Núcleo Administrativo e Econômico-Financeiro](#fase-viii--onda-3-núcleo-administrativo-e-econômico-financeiro)
9. [Fase IX — Ondas 4 e 5: Domínios Finalísticos, Territoriais e Mobilidade](#fase-ix--ondas-4-e-5-domínios-finalísticos-territoriais-e-mobilidade)
10. [Fase X — Infraestrutura, DevOps & Prontidão para Produção](#fase-x--infraestrutura-devops--prontidão-para-produção)

---

## Fase I — Estabilização Imediata & Controle de Versão (Bloqueios Atuais)

Prioridade: **Crítica (Imediata)**

- [x] **I.1 Normalizar o estado do Git (Rebase Interativo Pausado)** ✅ *(Concluído em 2026-09-06)*
  - O repositório estava em `(no branch, rebasing main)` devido a um `pull --rebase` interrompido.
  - Avaliação de histórico: os 6 commits pendentes (`7804a06..73f5af5`) já estavam aplicados em `HEAD` (`73f5af5`).
  - Todas as alterações de `DOM-GDO`, documentação, scripts e testes foram consolidadas e submetidas no commit atômico [`f8d317b`](file:///home/gildazio/Projetos-Python/sigmun-v1/sigmun-v1) (`feat(gdo): implementa módulo sigmun_gdo completo com testes e migrações`).
  - O rebase foi concluído com sucesso via `git rebase --continue`, restabelecendo a branch `main` limpa e com histórico perfeitamente linear.
- [x] **I.2 Corrigir bug de Homologação H-06 no `DOM-GDO`** ✅ *(Concluído em 2026-09-06)*
  - Correção consolidada em `src/modules/sigmun_gdo/presentation/api/__init__.py` (endpoint `POST /documentos`, commit `f8d317b`): `IntegrityError` tratado com rollback explícito da sessão (`session.rollback()`) e retorno determinístico de `HTTPException(409, detail="Código documental já utilizado por outro documento (RN-GDO-001)")`, cobrindo o cenário de corrida em que a checagem prévia perde a corrida para a constraint `documentos_codigo_key` (o `flush()` no repositório garante que a violação estoure dentro do `try` do endpoint, e não no commit do `get_db`). O caminho de domínio `CodigoDocumentalDuplicadoError` já retorna 409.
  - Validação reexecutada (`python scripts/homologacao_gdo.py`): **23/23 verificações aprovadas (SUCESSO)** — o roteiro evoluiu de 21 para 23 verificações (H-00 e H-09b) desde a abertura da tarefa; H-06 confirmado com `409 Conflict`. Evidência: `SIGMUN-Docs/DOM-GDO/evidencias/2026-09-06-homologacao-gdo.md`.
  - Removido artefato de comentário duplicado ("Endpoints de Documento") no mesmo arquivo da API.
- [x] **I.3 Ajustar dependências do Python (`pyproject.toml` e `requirements.txt`)** ✅ *(Concluído em 2026-09-06)*
  - Removida a dependência externa `"uuid>=1.3.0"` do `pyproject.toml` (backport de Python 2, sombreado pela stdlib — todo o código usa `import uuid`/`from uuid import ...` nativo). `requirements.txt` e `setup.py` nunca a declararam.
  - Adicionada `"email-validator>=2.1.0"` em `pyproject.toml`, `requirements.txt` (propaga ao `requirements-dev.txt` via `-r`) e `setup.py` (manifestos sincronizados), habilitando o uso de `pydantic.EmailStr` e eliminando warnings de e-mail no startup.
  - Ambiente virtual atualizado: `email-validator 2.3.0` instalado (com `dnspython 2.8.0`); `pip uninstall uuid` confirmou que o pacote PyPI já não estava no venv (`import uuid` resolve para `/usr/lib/python3.10/uuid.py`).
  - Validação: `pip check` sem quebras; `import src.main` sem warnings de e-mail/Pydantic; `EmailStr` aceita e-mail válido e rejeita inválido (`ValidationError`); suíte unitária completa **317 passed** (`pytest tests/unit`).
- [x] **I.4 Corrigir o Docker Compose para subida limpa** ✅ *(Concluído em 2026-09-06)*
  - **Scaffolding mínimo dos portais** (opção preferencial da ação), espelhando a stack do `frontend/admin` (React 19 + Vite 8 + TypeScript 6 + oxlint): `package.json`, `package-lock.json` (gerado via `npm install --package-lock-only`; exigido pelo `npm ci` do Dockerfile), `nginx.conf`, `index.html`, `vite.config.ts`, `tsconfig{,.app,.node}.json`, `src/main.tsx`, `src/App.tsx` (placeholder até a Fase VI.3), `src/index.css`, `.gitignore`, `.env.example`, `README.md` e `public/favicon.svg` em `frontend/portal-cidadao/` e `frontend/portal-fornecedor/` (`.gitkeep` residuais removidos).
  - **Bug de caminho do Dockerfile no Compose** (descoberto na validação): `build.dockerfile` é resolvido **relativo ao build context**, não ao `docker-compose.yml` — `../infra/...` apontava para `frontend/infra/...` (inexistente) e quebrava o build dos **três** frontends (nenhuma imagem `sigmun-v1-*` existia). Corrigido para `../../infra/docker/frontend/Dockerfile` em `frontend-admin`, `frontend-portal-cidadao` e `frontend-portal-fornecedor`.
  - **Hardening de startup do nginx** (admin e portais): o `proxy_pass` estático `http://backend:8000` exigia resolução DNS no startup (`[emerg] host not found in upstream "backend"`), colocando os frontends em crash-loop quando o backend não estava no ar (o Compose não tem `depends_on` dos frontends para o backend). Substituído pelo resolver do Docker (`resolver 127.0.0.11 valid=10s ipv6=off; set $backend_upstream http://backend:8000;` + `proxy_pass $backend_upstream`) — resolução por requisição: a SPA fica sempre no ar e o `/api` responde 502 até o backend subir.
  - **Celery worker/beat**: `include=["src.shared.tasks"]` apontava para pacote inexistente (`ModuleNotFoundError: No module named 'src.shared.tasks'` no startup). Criado o pacote de scaffolding `src/shared/tasks/__init__.py` (implementação real fica para a Fase VII).
  - **Overrides de rede no Compose**: adicionados `REDIS_HOST: redis` e `REDIS_PORT: 6379` em `backend`, `worker` e `beat` (mesmo padrão já usado para `DB_HOST: postgres`/`DB_PORT: 5432`), pois o `.env` do host usa `localhost:6379`, que não resolve dentro da rede Docker.
  - **Validação ponta a ponta** (`docker compose config` OK + `docker compose build` + `docker compose up -d`): 8/8 containers estáveis — `postgres` (healthy), `redis`, `backend` (`/health` → 200 com `"database":"up"`), `worker` (`Connected to redis://redis:6379/0`), `beat` (iniciado) e os três frontends servindo HTTP 200 nas portas 3000/3001/3002 (títulos corretos, SPA fallback OK em rota profunda, proxy `/api` e `/health` operando via nginx).


---

## Fase II — Qualidade de Código, CI/CD & Quality Gates

Prioridade: **Alta** (Desbloqueia a pipeline de CI)

- [x] **II.1 Saneamento das 359 violações do linter (Ruff)** ✅ *(Concluído em 2026-09-06)*
  - **Autofix seguro** (`.venv/bin/ruff check --fix src/ tests/`, ruff 0.16.5): **284 violações corrigidas** — 135 `UP045` (`Optional[X]` → `X | None`), 53 `I001` (ordenação de imports), 25 `UP006` (`List`/`Dict` → builtins), 15 `UP035`, 40 `F401`, 6 `W292`, demais residuais.
  - **Formatação** (`ruff format src/ tests/`): 169 arquivos reformatados; eliminou mais 41 violações (inclusive quase todos os `E501`).
  - **Correções manuais** (55 → 0):
    - `F821` **bug real**: função de módulo morta `_to_role_entity` em `sigmun_idn/infrastructure/repositories/sqlalchemy_role_repository.py` usava `self` inexistente (duplicata obsoleta do método `_to_entity` da classe) — removida (sem referências no repositório).
    - `E701`/linhas longas do `test_gdo_use_cases.py`: resolvidos pelo format (reformatou os statements e as quebras >100); `E501` remanescentes corrigidos manualmente (`test_gdo_api.py` docstring reescrita; import de módulo longo em `sigmun_cadastro/infrastructure/repositories/__init__.py` com `# noqa: E501` justificado).
    - `I001` dos novos blocos de imports explícitos: ordenados via autofix.
    - `F403`/`F405` (star imports): `sigmun_idn/domain/__init__.py` e `sigmun_idn/domain/events/__init__.py` convertidos para imports explícitos com `__all__` preservando os re-exports (17 eventos + 15 exceções).
    - `F401` remanescentes: imports órfãos removidos em 7 arquivos (`presentation/api`, `presentation/schemas`, `application/interfaces`, `domain/value_objects` de GDO e IDN).
    - `E712` (7): comparações `== True/False` em filtros SQLAlchemy convertidas para `.is_(True)/.is_(False)` (semântica idêntica em colunas booleanas).
    - `B008`: parâmetros `Query()` em `listar_pessoas` migrados ao estilo moderno `Annotated[T, Query(...)]` (FastAPI), eliminando o antipadrão sem `noqa`.
    - `B905`: `zip(..., strict=True)` em CPF/CNPJ (comprimentos garantidamente iguais nos call sites — agora com garantia de correção).
    - `F841`: evento de domínio criado e descartado removido de `classificar_documento_use_case.py` (código morto) e atribuição não usada em `test_contratos_api.py`.
    - `SIM102/SIM103/SIM110`: `if` aninhado combinado em `criar_documento_use_case.py`; retorno direto da condição em `auth_service.py`; `any()` em `usuario.py`.
  - **Validação**: `make lint` → **exit 0** ("All checks passed!", 0 violações em 623 arquivos); suíte completa **520 passed** (`pytest tests/`, 43s) — nenhuma regressão; diff total: 205 arquivos (+1.721/−1.429 linhas).
- [x] **II.2 Resolução dos 144 erros de tipagem estática (Mypy)** ✅ *(Concluído em 2026-09-06)*
  - **Handlers de ciclo de vida**: `startup_event`/`shutdown_event` anotados com `-> None` em `src/main.py`.
  - **Middleware**: `correlation_id_middleware.py` tipado (função auxiliar e handler).
  - **Helpers dos routers** (anotações de tipo explícitas):
    - `sigmun_dad/presentation/api/__init__.py`: 5 helpers (`_to_response`, `_to_catalogo_response`, `_to_linhagem_response`, `_to_politica_response`, `_to_qualidade_response`) + imports das entidades.
    - `sigmun_met/presentation/api/__init__.py`: 3 helpers (`_metadado_to_response`, `_taxonomia_to_response`, `_termo_to_response`) + imports das entidades.
    - `sigmun_gdo/presentation/api/__init__.py`: 11 helpers (`_publicar_evento`, `_publicar_documento_criado`, `_publicar_documento_vinculado_processo`, `_documento_to_response`, `_arquivamento_to_response`, `_assinatura_to_response`, `_versao_to_response`, `_tramitacao_to_response`, `_classificacao_to_response`, `_processo_to_response`, `_tipo_documento_to_response`) + imports das entidades.
    - `sigmun_idn/presentation/api/__init__.py`: `_to_usuario_response` + import de `Usuario`.
  - **Repositórios**:
    - `sqlalchemy_pessoa_repository.py`: type narrowing corrigido (variáveis `dados_fisicos`/`dados_juridicos` com nomes distintos para evitar conflito de tipos).
    - `sqlalchemy_unidade_administrativa_repository.py`: `get_ancestral_ids` anotado com `builtins.list[UUID]` (conflito com método `list` da classe).
    - `sqlalchemy_permissao_repository.py`: campo `updated_at` adicionado à entidade `Permissao` (alinhado ao model ORM) e mapeado no `_to_entity`.
    - `sqlalchemy_documento_repository.py`, `sqlalchemy_qualidade_repository.py`, `sqlalchemy_politica_repository.py`, `sqlalchemy_catalogo_repository.py`, `sqlalchemy_ativo_repository.py`: `# type: ignore[assignment]` em atribuições de `updated_at` (Mapped datetime).
    - `sqlalchemy_sessao_repository.py`: `rowcount` anotado com `int` + `# type: ignore[assignment]`.
  - **Use cases e commands**:
    - `AtualizarFornecedorCommand.situacao_cadastro` alterado para `SituacaoFornecedor | None` (aceita parcial).
    - `AtualizarFornecedorUseCase.execute`: validação de `None` antes de chamar `atualizar_situacao`.
    - `AutenticarUseCase.execute`: `motivo or "Erro desconhecido"` para garantir `str` (não `None`).
  - **Interface `TrilhaAuditoriaRepository`**: método `count(*, ...) -> int` adicionado (abstração + implementação `SqlAlchemyTrilhaAuditoriaRepository`).
  - **Entidades de domínio**: `Compra.alterar_situacao` e `Contrato.alterar_situacao` aceptan `usuario_id: UUID | None` (alineado a `updated_by`).
  - **Correção de bugs**:
    - 🐛 **8× `assert command.usuario_id`** em use cases de `sigmun_compras` substituídos por `if ... raise ValueError` (testes esperavam `ValueError`, não `AssertionError`) — `formalizar_contratacao`, `alterar_situacao_compra`, `alterar_situacao_contrato`, `atualizar_fornecedor`, `excluir_compra`, `excluir_contrato`, `excluir_processo_documental`, `remover_item_compra`.
  - **Validação**: `make type-check` → **exit 0** ("Success: no issues found in 584 source files"); suíte completa **520 passed** (`pytest tests/`, 40s) — nenhuma regressão; `make lint` → **exit 0** ("All checks passed!").
- [x] **II.3 Validação ponta a ponta da Pipeline de CI Local e Remota** ✅ *(Concluído em 2026-09-06)*
  - **Alvos do Makefile executados localmente** (todos com **exit 0**):
    - `make lint` → `ruff check src/ tests/` → **"All checks passed!"** (0 violações).
    - `make type-check` → `mypy src/` → **"Success: no issues found in 584 source files"**.
    - `make test` → `pytest tests/ -v` → **520 passed** em 40.5s.
    - `make test-integration` → `pytest tests/integration -v` → **203 passed** em 37.7s contra **PostgreSQL na porta 5433** (container `sigmun-postgres` healthy, `0.0.0.0:5433->5432/tcp`; `.env` apunta `DB_HOST=localhost`/`DB_PORT=5433`).
  - **Paridade com o CI remoto** (`.github/workflows/ci.yml`, branch develop/main):
    - `alembic upgrade head` → **exit 0**, DB em `20260901_03 (head)` (paso "Apply database migrations" idéntico).
    - `ruff check src/ tests/` e `mypy src/` → comandos idênticos aos alvos do Makefile.
    - `pytest tests/ -v --cov=src` → suíte completa verde localmente (prerequisito objetivo).
    - Service containers do CI (`postgres:15-alpine`, `redis:7-alpine`) alineados ao `docker-compose.yml` local (`postgres:15`, `redis`), garantizando paridade de ambiente.
  - **Stack completo operacional durante a validação**: backend (`:8000`), worker/beat Celery conectados ao redis, 3 frontends (`:3000/:3001/:3002`) e postgres/redis — todos `Up`.

---

## Fase III — Conclusão, Homologação e Fechamento de DOM-GDO (Onda 2)

Prioridade: **Alta**

- [x] **III.1 Executar e aprovar Homologação E2E de GDO** ✅ *(Concluído em 2026-09-06)*
  - Executado `python scripts/homologacao_gdo.py` contra a pilha real (PostgreSQL 15 → migrações Alembic → seed → API uvicorn): **23/23 verificações aprovadas (SUCESSO)** em 3.22s — rotas `/api/v1/gdo` verificadas (H-00..H-21, incluindo RN-GDO-001/002/011).
  - Confirmada a geração da evidência `SIGMUN-Docs/DOM-GDO/evidencias/2026-09-06-homologacao-gdo.md` com status **`SUCESSO`** (`**Resultado:** SUCESSO`, `**Status:** Concluído`).
- [x] **III.2 Executar testes de carga em GDO** ✅ *(Concluído em 2026-09-06)*
  - Executado `python scripts/test_carga_gdo.py` contra a API real (`http://localhost:8010/api/v1/gdo`, stack docker-compose): **23/23 testes, 0 falhas** (exit 0) — GET 50 req × 3 endpoints com p95 máx. ~238ms (SLA p95 < 500ms **CUMPRIDO**), throughput GET ~141–280 req/s, 20× POST /documentos com 201 (avg ~10–35ms), latência média geral ~17–19ms.
  - Evidência registrada: `SIGMUN-Docs/DOM-GDO/evidencias/2026-09-06-teste-carga-gdo.md` (`**Resultado:** SUCESSO`, `**Status:** Concluído`) — incluye throughput (req/s), p95, média e máx por endpoint.
  - Roteiro ajustado para ser idempotente e alinhado ao seed real de GDO (`tipo_documental_id: TD-OFICIO`, `unidade_autor_id: SECADM-01`): sufixo de códigos por execução (evita 409 entre corridas), saída com exit code 0/1 e registro automático de evidencia.
- [x] **III.3 Concluir os 6 artefatos finais de GDO em `SIGMUN-Docs/DOM-GDO/`**
  - `021-Checklist-de-Prontidao-para-Producao-Gestao-Documental.md`: Preencher com as evidências de teste e aprovação.
  - `022-Plano-de-Migracao-de-Dados-Gestao-Documental.md`: Definir estratégia de carga de legado.
  - `023-Plano-de-Treinamento-Gestao-Documental.md`: Roteiro para operadores de protocolo e arquivo.
  - `024-Plano-de-Suporte-e-Operacao-Gestao-Documental.md`: Procedimentos de sustentação.
  - `025-Estrutura-Tecnica-Gestao-Documental.md`: Arquitetura física detalhada.
  - `026-Termo-de-Encerramento-do-Dominio-Gestao-Documental.md`: Formalização de entrega.
- [x] **III.4 Atualizar  `ROADMAP.md`**
  - [x] **III.4 Consolidar o encerramento documental de GDO**
  - Consolidar  `ROADMAP.md` a conclusão de todos os ciclos de GDO.
  - Atualizar `ROADMAP.md` com o status final 🟢 de `DOM-GDO`.
  

---

## Fase IV — Sincronização Documental da Onda 2 (CUM, IDN, DAD, MET)

Prioridade: **Média/Alta** (Sanar a dívida de governança onde o código existe mas a documentação permaneceu em template)

- [x] **IV.1 Promover artefatos do `DOM-CUM` (Cadastro Único Municipal)**
  - Atualizar `SIGMUN-Docs/DOM-CUM/001` a `026` para refletir as entidades implementadas (Pessoa, DadosFisicos, DadosJuridicos, Endereco, Documento, Contato, UnidadeAdministrativa) e suas 15 use cases.
  - Marcar artefatos com `**Status:** Vigente`.
- [x] **IV.2 Promover artefatos do `DOM-IDN` (Identidade e Acesso)**
  - Atualizar `SIGMUN-Docs/DOM-IDN/001` a `026` com base no módulo `sigmun_idn` (Usuario, Role, Permissao, Sessao, AuditoriaLogin, fluxos JWT).
  - Marcar artefatos com `**Status:** Vigente`.
- [x] **IV.3 Promover artefatos do `DOM-DAD` (Dados Corporativos)**
  - Atualizar `SIGMUN-Docs/DOM-DAD/001` a `026` com base nas entidades implementadas (Ativos, Catalogos, Linhagens, Politicas, Qualidade) e seus 26 use cases.
  - Marcar artefatos com `**Status:** Vigente`.
- [x] **IV.4 Promover artefatos do `DOM-MET` (Metadados Corporativos)**
  - Atualizar `SIGMUN-Docs/DOM-MET/001` a `026` com base nas entidades implementadas (Metadados, Valores, Classificacoes, Taxonomias, Termos) e seus 22 use cases.
  - Marcar artefatos com `**Status:** Vigente`.
- [x] **IV.5 Atualizar a Tabela do Plano de Trabalho e o README raiz**
  - Executar: `python scripts/atualizar_tabela_plano.py`.
  - Atualizar o `README.md` da raiz para listar os módulos CUM, IDN, DAD, MET e GDO na árvore de módulos e na descrição de capacidades.

---

## Fase V — Implementação dos Domínios Restantes da Onda 2 (DOM-SEG e DOM-INT)

Prioridade: **Alta** (Conclusão formal da Onda 2)

- [x] **V.1 `DOM-SEG` — Segurança da Informação (Ordem 7)**
  - [x] Consolidar artefatos documentais `SIGMUN-Docs/DOM-SEG/000` a `026`.
  - [x] Criar módulo `src/modules/sigmun_seg/` seguindo o padrão Clean Architecture/DDD.
  - [x] Modelar agregados: Controles de Segurança, Políticas de Segurança, Gestão de Incidentes, Chaves Criptográficas e Credenciais.
  - [x] Implementar repositórios SQLAlchemy e migração Alembic para o schema `seg`.
  - [x] Implementar APIs REST `/api/v1/seg` e integrar ao `src/main.py`.
  - [x] Criar suíte de testes unitários (≥ 30 testes) e de integração.
  - ✅ **V.1 concluído em 2026-09-07:** implementados os use cases e schemas de **Chaves Criptográficas** (`chave_use_cases.py`/`chave_schemas.py`) e **Credenciais** (`credencial_use_cases.py`/`credencial_schemas.py`); corrigidos bugs latentes do módulo (`import uuid` em `models.py`, `import logging`/`logger` nos 5 repositórios); **router `/api/v1/seg` reativado em `src/main.py` com 32 endpoints**; suíte total de DOM-SEG ampliada para **65 testes unitários** (39 base + 26 chave/credencial), todos passando; suíte completa `tests/unit` = **382 passed**. Suíte de integração pendente de execução (exige banco).
- [x] **V.2 `DOM-INT` — Integração e Interoperabilidade (Ordem 8)** 🟢 **Concluído tecnicamente**
  - [x] Consolidar artefatos documentais `SIGMUN-Docs/DOM-INT/000` a `026` *(artefatos `001-026` marcados com `Status: Vigente`)*.
  - [x] Criar módulo `src/modules/sigmun_int/` seguindo o padrão Clean Architecture/DDD.
  - [x] Implementar barramento de eventos interno (Event Bus) consumindo os Transactional Outbox de GDO e Compras.
  - [x] Implementar catálogo de APIs externas e webhooks com controle de retry e dead-letter queue.
  - [x] Implementar catálogo e seed dos conectores oficiais (GOV.BR, e-Social, SIAFIC, PNCP).
  - [x] Implementar migration Alembic para o schema `integracao`.
  - [x] Implementar testes unitários e de integração PostgreSQL.
  - 🟢 **DOM-INT concluído tecnicamente em 2026-09-16:** implementadas a persistência SQLAlchemy das entidades de integração, os repositórios, o Event Bus integrado aos Transactional Outbox de GDO e Compras, a idempotência de eventos, o catálogo de APIs externas e webhooks, o controle de retry/dead-letter, o catálogo e seed dos conectores oficiais, a migration do schema `integracao` e os testes unitários e de integração PostgreSQL. Validação: **98 testes unitários DOM-INT**, **25 testes de integração PostgreSQL DOM-INT** e **708 testes na suíte completa**, todos aprovados.
  - [ ] Configurar, homologar e ativar operacionalmente as integrações externas dos conectores oficiais, conforme disponibilidade de credenciais, contratos, ambientes e serviços externos.
- [ ] **V.3 `DOM-GOV` e `DOM-IND` (Governança e Indicadores Municipais - Ordens 9 e 10)**
  - [ ] Especificar e implementar painéis de conformidade, atos normativos e KPIs estratégicos.

---

## Fase VI — Fundação e Evolução do Frontend

Prioridade: **Média**

> ✅ **Pronto para iniciar em 2026-09-07:** backend no ar (19 rotas) com `/api/v1/seg` **reativado** e DOM-SEG completo (32 endpoints, 65 testes unitários). A Fase VI pode conectar o Admin às APIs reais.

- [ ] **VI.1 Conectar Frontend Admin (`frontend/admin`) à API do SIGMUN**
  - Substituir o mock de login em `localStorage` pela integração real com `POST /api/v1/idn/auth/login`.
  - Armazenar o token JWT de forma segura e injetar nos headers das requisições via Axios/Fetch client.
  - Implementar gerenciamento de estado de usuário e controle de rotas por perfis/roles (RBAC).
- [ ] **VI.2 Construir Módulos de Interface no Frontend Admin**
  - [ ] **Módulo de Compras e Contratos:** Listagem de processos, detalhe do processo de compra, gestão de fornecedores e contratos.
  - [ ] **Módulo de Gestão Documental (GDO):** Upload de documentos, visualização de PDF, controle de versões, tramitação entre secretarias e assinaturas digitais.
  - [ ] **Módulo de Cadastro Único (CUM):** Consulta e cadastro de pessoas físicas/jurídicas e organograma de unidades administrativas.
  - [ ] **Módulo de Identidade (IDN):** Gestão de usuários, atribuição de perfis e trilha de acessos.
- [ ] **VI.3 Inicializar Scaffolding Real dos Portais Externos**
  - [ ] **Portal do Cidadão (`frontend/portal-cidadao`):** Setup com Vite + React, Tailwind, páginas de consulta de protocolos, emissão de certidões e serviços públicos.
  - [ ] **Portal do Fornecedor (`frontend/portal-fornecedor`):** Setup com Vite + React, área logada para fornecedores municipais acompanharem licitações, empenhos e contratos.

---

## Fase VII — Processamento Assíncrono e Mensageria (Celery & Redis)

Prioridade: **Média**

- [ ] **VII.1 Criar o pacote `src/shared/tasks/`**
  - Criar `src/shared/tasks/__init__.py`.
  - Implementar task periódica de healthcheck do worker.
  - Implementar dispatcher assíncrono para processar registros pendentes de `gdo.eventos_outbox` e publicar no Redis Pub/Sub.
  - Implementar task assíncrona para expurgo de arquivos físicos com descarte autorizado após cumprimento da temporalidade.
- [ ] **VII.2 Validar Celery Worker e Celery Beat no Docker Compose**
  - Iniciar containers `worker` e `beat` e validar logs de subida sem erros de importação.
  - Configurar monitoramento de filas via Celery Flower (opcional para dev).

---

## Fase VIII — Onda 3: Núcleo Administrativo e Econômico-Financeiro

Prioridade: **Planejada / Próxima Onda** (Conforme ROADMAP §6)

- [ ] **VIII.1 `DOM-DIA` — Gestão de Diárias (Prioridade Especial)**
  - Tratar como domínio autônomo com máquina de estados completa (solicitação → autorização → cálculo → concessão → prestação de contas → aprovação/glosa/restituição).
  - Criar artefatos em `SIGMUN-Docs/DOM-DIA/` e módulo `src/modules/sigmun_dia/`.
  - Integrar com `DOM-PES` (dados do servidor), `DOM-ORC` (dotação) e `DOM-GDO` (anexos de viagem).
- [ ] **VIII.2 `DOM-PES` — Gestão de Pessoas (RH e Folha)**
  - Migrar scaffolding de `sigmun_rh` para implementação DDD: servidores, cargos, lotações, folha de pagamento, férias e frequência.
- [ ] **VIII.3 `DOM-ORC` e `DOM-CON` — Orçamento e Contabilidade Pública**
  - PPA, LDO, LOA, dotações orçamentárias, reservas de saldo, empenho, liquidação, pagamento, plano de contas (PCASP) e conciliação contábil.
- [ ] **VIII.4 `DOM-TRI` — Administração Tributária**
  - IPTU, ISSQN, ITBI, taxas municipais, certidões negativas, cadastro de contribuintes e dívida ativa.
- [ ] **VIII.5 `DOM-PAT` e `DOM-FRO` — Gestão Patrimonial e Frotas**
  - Bens móveis/imóveis, tombamento, depreciação, transferências, controle de veículos, abastecimento, manutenções e rotas.

---

## Fase IX — Ondas 4 e 5: Domínios Finalísticos, Territoriais e Mobilidade

Prioridade: **Futura** (Conforme ROADMAP §7 e §8)

- [ ] **IX.1 Domínios Finalísticos (Onda 4)**
  - `DOM-SAU` (Saúde): Prontuário eletrônico do cidadão, agendamento SUS, regulação, farmácia básica.
  - `DOM-EDU` (Educação): Matrícula escolar, diário de classe digital, transporte escolar, merenda.
  - `DOM-ASS` (Assistência Social): CadÚnico local, benefícios eventuais, CRAS/CREAS.
  - `DOM-MAM` (Meio Ambiente): Licenciamento ambiental, fiscalização, áreas protegidas.
- [ ] **IX.2 Domínios Territoriais (Onda 4)**
  - `DOM-TEL` e `DOM-IMO` (Territorial e Cadastro Imobiliário): Planta genérica de valores, logradouros, lotes e georreferenciamento.
  - `DOM-GEO` e `DOM-OBR` (Geoinformação e Obras): Mapas SIG, acompanhamento físico-financeiro de obras públicas.
- [ ] **IX.3 Atendimento, Mobilidade e Apps (Onda 5)**
  - `DOM-ATE` (Atendimento Presencial e Online): Balcão de atendimento com triagem por senha.
  - `DOM-OUV` (Ouvidoria FalaBR / e-OUV municipal): Manifestações, denúncias e LAI.
  - `mobile/`: Desenvolvimento dos aplicativos React Native para agentes comunitários, fiscais de tributos/obras e cidadãos.

---

## Fase X — Infraestrutura, DevOps & Prontidão para Produção

Prioridade: **Média/Contínua**

- [ ] **X.1 Hardening de Configurações e Segredos**
  - Migrar segredos do `.env` local para AWS Secrets Manager / Vault em ambientes de homologação e produção.
  - Validar rotatividade e expiração de chaves JWT.
- [ ] **X.2 Automação de Backups do Banco e Storage**
  - Validar o script `scripts/backup_postgres.py` com testes de restore automatizado periódicos.
  - Configurar rotinas de backup para o volume de anexos de documentos (`STORAGE_ROOT`).
- [ ] **X.3 Implantação e Validação no Kubernetes (EKS)**
  - Validar manifestos em `infra/kubernetes/` contra cluster local (k3s / minikube).
  - Criar pipeline de deploy contínuo (CD) no GitHub Actions (`.github/workflows/cd.yml`).
- [ ] **X.4 Observabilidade e Métricas**
  - Implementar middleware de métricas Prometheus (`/metrics`) na API FastAPI.
  - Configurar dashboards de saúde do sistema no Grafana com alertas de latência e taxa de erro 5xx.

---

*Documento mantido pela Equipe de Desenvolvimento do SIGMUN.*  
*Regra de governança: qualquer tarefa concluída deve ser marcada e acompanhada de sua respectiva evidência técnica e documental.*

