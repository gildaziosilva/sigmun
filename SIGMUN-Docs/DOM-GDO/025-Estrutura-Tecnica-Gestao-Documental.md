# 025 – Estrutura Técnica – Gestão Documental

#### Estrutura Técnica – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-025

**Domínio:** Gestão Documental

**Versão:** 2.0

**Status:** Concluído

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

- `000-Dominio-Gestao-Documental.md`
- `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
- `000A-Padrao-Corporativo-De-Documentacao-do-SIGMUN.md`
- `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
- `013-Modelo-De-Dados-Gestao-Documental.md`
- `014-Modelo-De-Integracao-Gestao-Documental.md`
- `021-Checklist-De-Prontidao-De-Producao-Gestao-Documental.md`
- `018-Plano-De-Testes-Gestao-Documental.md`
- `020-Plano-De-Implantacao-Gestao-Documental.md`

---

# 1. Finalidade

O **Estrutura Técnica – Gestão Documental** descreve a arquitetura física detalhada do domínio `DOM-GDO`, incluindo infraestrutura, banco de dados, serviços, APIs, padrões de implementação e ambientes de execução.

---

# 2. Visão Geral da Arquitetura

```
┌─────────────────────────────────────────────────────────────────┐
│                    ENVIRONMENT DEPLOYMENT                       │
├─────────────────────────────────────────────────────────────────┤
│  Produção         │  Homologação          │  Desenvolvimento    │
│  docker-compose   │  docker-compose       │  docker-compose dev   │
│  + CI/CD GitHub   │  + scripts/           │  + makefile test      │
└─────────────────────────────────────────────────────────────────┘
```

---

# 3. Pilha Tecnológica

| Camada | Tecnologia | Versão | Observações |
|--------|------------|--------|-------------|
| **Linguagem** | Python | 3.11+ | Tipado estático com type-check |
| **Framework** | FastAPI | 0.104+ | API moderna, OpenAPI nativo |
| **ORM** | SQLAlchemy | 2.0+ | Mapeamento objeto-relacional |
| **Migrações** | Alembic | 1.12+ | Versionamento de schema |
| **Banco de Dados** | PostgreSQL | 15 | Docker volume `postgres_data` |
| **Containerização** | Docker + Docker Compose | 2.0+ | Três serviços: api, db, pgadmin |
| **Testes** | Pytest | 8.0+ | 93 testes de domínio + 520 total projeto |
| **Lint/Type** | Ruff / MyPy | 0 violações | Fase II validado |
| **Documentação** | OpenAPI 3.0 | Auto-generaté | `/openapi.json`, `/docs`, ReDoc |

---

# 4. Modelo Físico de Dados

## 4.1 Schema `gdo` — 11 Tabelas

| Tabela | Primary Key | Foreign Keys | Índices Notáveis |
|--------|-------------|--------------|------------------|
| `documentos` | `id` (UUID) | `tipo_id`, `classificacao_id`, `temporalidade_id` | `codigo` (unique), `status`, `tipo_id` |
| `tipos_documentais` | `id` | — | `codigo` (unique) |
| `classificacoes` | `id` | — | `codigo` (unique) |
| `temporalidades` | `id` | — | `codigo` (unique) |
| `versoes_documentos` | `id` (UUID) | `documento_id` | `documento_id`, `numero_versao` |
| `tramitacoes` | `id` (UUID) | `documento_id`, `usuario_id` | `documento_id`, `status`, `data_tramitacao` |
| `eventos_outbox` | `id` (UUID) | — | `status`, `created_at` |
| `assinaturas` | `id` (UUID) | `documento_id` | `documento_id`, `hash_assinatura` |
| `eventos_auditoria` | `id` (UUID) | — | `entidade`, `timestamp` |
| `parametros_sistema` | `chave` (PK) | — | — |
| `sessoes_usuarios` | `id` (UUID) | — | — |

## 4.2 Constraints e Regras de Integridade

- **Unicidade de código:** `documentos.codigo` — RN-GDO-001 (409)
- **Check de status:** `documentos.status` — valores: rascunho, ativo, enviado, arquivado, encerrado
- **Check de tipo/destinação:** validações de domínio (RN-GDO-002 a RN-GDO-028)
- **FKs com cascade/restrict:** definido por regra de negócio
- **Hash SHA-256:** `documentos.conteudo_ref` — integridade de conteúdo (RN-GDO-002)

---

# 5. API — Endpoints (20 endpoints em `/api/v1/gdo`)

| Grupo | Endpoint | Método | Descrição |
|-------|----------|--------|-----------|
| Tipos | `/tipos-documentais` | GET | Listar tipos documentais |
| Classificações | `/classificacoes` | GET | Listar classificações |
| Temporalidades | `/temporalidades/{id}` | GET | Consultar temporalidade |
| Documentos | `/documentos` | POST | Criar documento |
| Documentos | `/documentos/{id}` | GET | Consultar documento |
| Documentos | `/documentos/{id}/versoes` | POST | Criar versão |
| Documentos | `/documentos/{id}/versoes` | GET | Listar versões |
| Documentos | `/documentos/{id}/tramitar` | POST | Tramitar documento |
| Documentos | `/documentos/{id}/tramitacoes` | GET | Listar tramitações |
| Documentos | `/documentos/{id}/assinar` | POST | Assinar documento |
| Documentos | `/documentos/{id}/arquivar` | POST | Archivar documento |
| Documentos | `/documentos/{id}/destinar` | POST | Destinar documento |
| Documentos | `/documentos/{id}/eliminar` | DELETE | Eliminar (com homologação) |
| Health | `/health` | GET | Health check |
| OpenAPI | `/openapi.json` | GET | Especificação da API |
| Documentação | `/docs` | GET | Swagger UI |
| ReDoc | `/redoc` | GET | ReDoc docs |

---

# 6. Arquitetura de Serviços

- **12 use cases** em `application/use_cases`
- **9 repositórios SQLAlchemy** com paginação e soft-delete
- **Transactional Outbox** pattern em `gdo.eventos_outbox`
- **Injeção de dependência** via `Depends` (FastAPI)
- **Exceções de domínio** centralizadas em `domain/exceptions.py` (400, 404, 409)
- **Modelos Pydantic** para request/response schemas
- **Autenticação provisória** por headers `X-Usuario-Id`/`X-Usuario-Papel` até DOM-IDN
- **Autorização** por guards 401/403 validados na homologação H-18

---

# 7. Segurança da Infraestrutura

- **Segredos externos:** `.env` não versionado, compose com credenciais locais
- **Variáveis de ambiente:** `src/shared/config` — carregamento dinâmico
- **Integridade de conteúdo:** hash SHA-256 por RN-GDO-002
- **Sigilo documental:** atributo `is_sigiloso` no modelo de dados
- **Auditoria ativa:** trilha core + eventos de domínio na tabela `eventos_auditoria`
- **TLS/HTTPS:** pendente de configuração (P-GDO-007)

---

# 8. Ambientes

| Ambiente | Composição | Observações |
|----------|------------|-------------|
| **Desenvolvimento** | `docker-compose up --build` | Hot-reload, logs em console |
| **Homologação** | `docker-compose -f docker-compose.yml -f docker-compose.homol.yml up` | 23/23 E2E tests passed |
| **Produção** | `docker-compose -f docker-compose.yml -f docker-compose.prod.yml up` | TLS pendente, health checks ativos |

---

# 9. Deploy e Operação

## 9.1 Scripts Disponíveis (Makefile)

| Comando | Descrição |
|---------|-----------|
| `make up` | Iniciar todos os serviços (dev) |
| `make down` | Parar todos os serviços |
| `make migrate` | `alembic upgrade head` — aplicar migrações |
| `make rollback` | `alembic downgrade -1` — desfazer última migração |
| `make test` | `pytest` — executar suíte de testes |
| `make lint` | `ruff check` — linting |
| `make type-check` | `mypy` — type checking |

## 9.2 Rollback Procedure

1. `make rollback` — `alembic downgrade -1`
2. Verificar integridade dos dados
3. Se crítico: restaurar backup `scripts/backup_postgres.py`
4. Notificar Suporte Nível 3

---

# 10. Versionamento de Release

| Versão | Data | Commit | Observações |
|--------|------|--------|-------------|
| 0.1.0 | 2026-08-20 | `initial` | Esboço do domínio |
| 0.2.0 | 2026-08-25 | `feat: seed data` | 12 tipos, 9 classif, 4 temp |
| 1.0.0 | 2026-09-01 | `feat: api v1` | 20 endpoints implementados |
| 2.0.0 | 2026-09-06 | `feat: homologation complete` | 23/23 E2E, load test 23/23 |

---

# 11. Dependências Externas

- `.env` — credenciais de banco, chaves de configuração
- `docker-compose.yml` — orquestração de serviços
- `alembic.ini` — configuração de migrações
- `scripts/` — backup, homologação, teste de carga

---

# 12. Rastreabilidade Técnica

| Artefato | Referência | Status |
|----------|------------|--------|
| Modelo de dados | `013-Modelo-De-Dados` | Atualizado (11 tabelas) |
| Modelo de integração | `014-Modelo-De-Integracao` | Atualizado (Outbox pattern) |
| Matriz de rastreabilidade | `012-Matriz-De-Rastreabilidade` | Atualizada |
| Casos de teste | `019-Casos-De-Teste` | 93 testes implementados |
| Plano de testes | `018-Plano-De-Testes` | Concluído |

---

**Documento:** 025-Estrutura-Tecnica-Gestao-Documental.md

**Última atualização:** 2026-09-06

**Responsável:** Equipe SIGMUN

**Status da revisão:** Concluído