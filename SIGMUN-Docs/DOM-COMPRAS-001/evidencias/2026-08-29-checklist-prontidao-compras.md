# Evidência de Execução — Checklist de Prontidão (Item 18 do Roadmap)

**Domínio:** DOM-COMPRAS-001 — Gestão de Compras e Contratações

**Data da execução:** 2026-08-29

**Artefato avaliado:** `SIGMUN-Docs/DOM-COMPRAS-001/021-Checklist-de-Prontidao-para-Producao-Gestao-de-Compras-e-Contratacoes.md`

**Versão avaliada:** 0.1.0 (`pyproject.toml`, `src/main.py`)

**Ambiente:** Desenvolvimento/Homologação técnica — Docker Compose + PostgreSQL 15 (localhost:5433), schemas `core`/`compras`/`auditoria`

**Resultado:** **NÃO PRONTO para produção** — 10 pendências (P-001 a P-010) registradas; recomendação de avanço para o item 19 (implantação em ambiente controlado).

---

## 1. Verificações executadas (comandos e resultados)

| # | Verificação | Comando/Método | Resultado |
|---|---|---|---|
| 1 | Suíte de testes automatizados | `.venv/bin/python -m pytest tests/ -q` | **261 aprovados, 0 falhas** (2,69s) |
| 2 | Homologação E2E (item 17) | `scripts/homologacao_compras.py` — log de 2026-08-29 | **47/47 aprovadas** (`2026-08-29-homologacao-compras.log`) |
| 3 | Banco de dados ativo e migrado | Conexão psycopg2 localhost:5433 → `select version_num from alembic_version` | `20260823_01` (head) |
| 4 | Schemas do modelo físico | `information_schema.schemata` | `auditoria`, `compras`, `core` |
| 5 | Tabelas por schema | `information_schema.tables` | `auditoria(1)`, `compras(3)`, `core(6)` |
| 6 | Migrações versionadas | `alembic/versions/` | `20260820_01`, `20260821_01`, `20260822_01`, `20260823_01` |
| 7 | Segredos fora do código | Varredura regex por senhas/segredos literal em `src/**/*.py` | Nenhum resultado (segredos em `.env` externo) |
| 8 | Configuração externa | `.env` presente (37 linhas); `docker-compose.yml` com overrides de rede | OK |
| 9 | Paginação das APIs | Varredura `page`/`page_size` nos routers (fornecedores, contratos, itens, compras) | Implementada com `total` nos `*_ListResponse` |
| 10 | OpenAPI e saúde | `src/main.py`: `version="0.1.0"`, `/docs`, `/openapi.json`, `/health` | 17 paths publicados (homologação H-03) |
| 11 | CI/CD | `.github/workflows/ci.yml` (ruff, mypy, pytest+cov, build Docker) e `cd.yml` | CI funcional; CD com deploy ainda simulado (echo) |
| 12 | Auditoria | Trilha `auditoria.eventos` append-only (trigger); consulta restrita auditada | Homologada (H-34 a H-40) |
| 13 | Segurança de acesso | Guardas 401/403 por `X-Usuario-Id`/`X-Usuario-Papel` | Homologadas (H-24, H-31, H-34, H-35) |
| 14 | Logging estruturado | Varredura `import logging`/`getLogger` em `src/` | Apenas logging padrão nos routers — pendência (P-002) |
| 15 | Monitoramento/backup/rollback | Inspeção de `infra/`, `scripts/deployment/`, workflows | Ausentes — pendências (P-003/P-004/P-005) |
| 16 | Documentação do domínio | `SIGMUN-Docs/DOM-COMPRAS-001/` | 27 artefatos (000 a 026) presentes |

## 2. Síntese por área (seção 43 do checklist)

- **Aprovadas [x]:** Documentação, Requisitos, Rastreabilidade, Implementação, Banco de Dados, Dados, APIs, Serviços, Integrações (interna), Segurança (parcial), Auditoria, Testes.
- **Pendentes [!]:** Governança institucional, Segurança (endurecimento), Performance, Infraestrutura, Backup, Recuperação, Usuários, Treinamento, Suporte, Monitoramento, Implantação, Rollback, Comunicação, Piloto.
- **Não aplicáveis [N/A]:** Integrações prioritárias externas (marcos M3/M4), sessões (API stateless), dados históricos (sem legado).

## 3. Pendências registradas (seção 41 do checklist)

| ID | Pendência | Severidade | Bloqueia produção? | Prazo |
|---|---|---|---|---|
| P-001 | Reexecutar roteiro E2E sobre PostgreSQL | Alta | Sim | Item 19 |
| P-002 | Logging estruturado + correlation ID + retenção | Alta | Sim | Itens 19/20 |
| P-003 | Observabilidade (monitoramento, alertas, dashboard) | Alta | Sim | Item 20 |
| P-004 | Backup configurado, executado e restauração testada | Crítica | Sim | Item 19 |
| P-005 | Rollback documentado e testado | Alta | Sim | Item 19 |
| P-006 | Avaliação de performance | Média | Não (piloto) | Item 19 |
| P-007 | TLS, pentest, revisão de permissões | Alta | Sim | Antes de produção |
| P-008 | Idempotência formal de escritas | Média | Não (piloto) | Itens 19/20 |
| P-009 | Usuários, treinamento, manuais e comunicação | Alta | Sim | Antes de produção |
| P-010 | Suporte e operação estabelecidos | Alta | Sim | Item 20 |

## 4. Decisão do gate (seção 46 do checklist)

**NÃO AUTORIZADA a entrada em produção** nesta data. A plataforma funcional do domínio está implementada e homologada, porém os critérios de bloqueio da seção 40 do checklist (ausência de backup, rollback, suporte) impedem a produção. Encaminhamento: executar o item 19 (implantação em ambiente controlado — incluindo P-001) e o item 20 (operação monitorada — incluindo P-003/P-010) e reavaliar este gate.

## 5. Rastreabilidade

- ROADMAP.md, seção 4.1, item 18 (executado em 2026-08-29).
- 021-Checklist-de-Prontidao-para-Producao (versão 1.1 — execução registrada no Controle de Versões).
- Evidências anteriores: `2026-08-29-homologacao-compras.log` (item 17 — homologação 47/47).
