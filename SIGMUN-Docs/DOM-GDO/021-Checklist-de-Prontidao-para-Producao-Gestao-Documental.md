# 021 – Checklist de Prontidão para Produção – Gestão Documental

#### Checklist de Prontidão para Produção – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-021

**Domínio:** Gestão Documental

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

- `000-Dominio-Gestao-Documental.md`
- `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
- `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
- `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
- `018-Plano-de-Testes-Gestao-Documental.md`
- `019-Casos-de-Teste-Gestao-Documental.md`
- `020-Plano-de-Implantacao-Gestao-Documental.md`
- `022-Plano-de-Migracao-de-Dados-Gestao-Documental.md`
- `025-Estrutura-Tecnica-Gestao-Documental.md`
- `026-Termo-de-Encerramento-do-Dominio-Gestao-Documental.md`
- Evidências: `2026-09-06-homologacao-gdo.md` e `2026-09-06-teste-carga-gdo.md`

---

# 1. Finalidade

O **Checklist de Prontidão para Produção – Gestão Documental** verifica, de forma estruturada, se o domínio `DOM-GDO` está técnica, funcional, operacional e institucionalmente preparado para entrar em produção.

Este documento constitui um **gate de produção**. A entrada em produção somente deverá ocorrer quando os critérios críticos de prontidão estiverem atendidos e formalmente validados com evidência.

---

# 2. Objetivos

São objetivos deste checklist:

1. Verificar a conclusão da implementação (módulo `sigmun_gdo`);
2. Verificar a conclusão dos testes automatizados;
3. Validar as regras de negócio RN-GDO-001 a RN-GDO-028;
4. Validar segurança e auditoria;
5. Validar o modelo de dados e as migrações Alembic;
6. Validar integrações (Transactional Outbox);
7. Validar infraestrutura;
8. Validar backup e recuperação;
9. Validar usuários e permissões;
10. Validar documentação técnica e funcional;
11. Validar treinamento;
12. Validar suporte e operação;
13. Validar monitoramento;
14. Registrar pendências;
15. Apoiar a decisão de entrada em produção.

---

# 3. Regra de Decisão

A decisão de produção considera quatro estados principais:

```text
PRONTO
NÃO PRONTO
PRONTO COM RESSALVAS
BLOQUEADO
```

**3.1 PRONTO** — todos os critérios críticos foram atendidos.

**3.2 NÃO PRONTO** — existem pendências que impedem a entrada em produção.

**3.3 PRONTO COM RESSALVAS** — existem pendências não críticas formalmente aceitas.

**3.4 BLOQUEADO** — existe risco crítico que impede a implantação.

---

# 4. Legenda do Checklist

| Símbolo | Significado      |
| ------- | ---------------- |
| [ ]     | Não verificado   |
| [x]     | Aprovado         |
| [!]     | Pendência        |
| [B]     | Bloqueio         |
| [N/A]   | Não aplicável    |

---

# 5. Governança da Prontidão

| Item                     | Status | Evidência                                                             | Responsável       |
| ------------------------ | ------ | --------------------------------------------------------------------- | ----------------- |
| Escopo aprovado          | [x]    | Fatia completa do DOM-GDO (ROADMAP §5.2): 20 endpoints, 11 tabelas    | Equipe SIGMUN     |
| Versão definida          | [x]    | 0.1.0 (`pyproject.toml`, `src/main.py`)                              | Equipe SIGMUN     |
| Responsáveis definidos   | [x]    | Equipe SIGMUN (artefatos 000-026)                                     | Equipe SIGMUN     |
| Janela de implantação    | [!]    | Pendente de aprovação institucional (pré-requisito seção 27)          | Prefeitura/Equipe |
| Aprovação registrada     | [!]    | Aprovação formal pendente (gate seção 28)                            | Equipe SIGMUN     |
| Plano de comunicação     | [!]    | Pendência institucional (seção 26)                                    | Equipe SIGMUN     |

---

# 6. Documentação

## 6.1 Documentação Arquitetural

- [x] Domínio documentado. (`000-Dominio-Gestao-Documental.md`)
- [x] Mapa de atores atualizado. (`001`)
- [x] Mapa de capacidades atualizado. (`002`)
- [x] Mapa de processos atualizado. (`003`)
- [x] Mapa de serviços atualizado. (`004`)
- [x] Casos de uso documentados. (`005`)
- [x] Histórias de usuário documentadas. (`006`)
- [x] Regras de negócio documentadas. (`007` — 28 RNs)
- [x] Requisitos funcionais documentados. (`008`)
- [x] Requisitos não funcionais documentados. (`009`)
- [x] Especificações documentadas. (`010`)
- [x] Critérios de aceitação documentados. (`011`)
- [x] Matriz de rastreabilidade documentada. (`012`)
- [x] Modelo de dados atualizado. (`013`)
- [x] Modelo de integrazação atualizado (014)
- [x] Arquitetura de serviços atualizada (015)
- [x] Modelo de segurança atualizado (016)
- [x] Modelo de auditoria atualizado (017)
- [x] Plano de testes atualizado (018)
- [x] Casos de teste documentados. (`019`)
- [x] Plano de implantação atualizado. (`020`)
- [x] Plano de migração de dados atualizado. (`022`)
- [x] Plano de treinamento atualizado. (`023`)
- [x] Plano de suporte e operação atualizado. (`024`)
- [x] Estrutura técnica atualizada. (`025`)
- [x] Termo de encerramento formalizado (026)

**Status da seção:** [x] (26 artefatos verificados)

---

# 7. Requisitos

- [x] Requisitos funcionais implementados (fluxo completo criar → versão → classificar → tramitar → assinar → arquivar → destinar)
- [x] Regras de negócio implementadas. (RN-GDO-001/002/011 homologadas; 28 RNs documentadas)
- [x] Critérios de aceitação atendidos. (homologação E2E 23/23 — evidência 2026-09-06)
- [x] RNFs de performance atendidos (teste de carga 23/23 SLA p95 < 500ms CUMPRIDO)
- [x] Requisitos críticos validados. (integridade SHA-256, unicidade de código, eliminação autorizada)
- [x] Exceções aprovadas (autenticação provisional por headers até DOM-IDN)

**Status da seção:** [x]

---

# 8. Rastreabilidade

- [x] Casos de uso possuem rastreabilidade. (`005`/`012`)
- [x] Histórias de usuário possuem rastreabilidade. (`006`/`012`)
- [x] Regras de negócio possuem rastreabilidade (007/012)
- [x] Requisitos possuem rastreabilidade (008/009/012)
- [x] Critérios de aceitação possuem rastreabilidade. (`011`/`012`)
- [x] Casos de teste possuem rastreabilidade. (`018`/`019`; IDs H-xx da homologação)
- [x] Evidências de teste vinculadas. (`SIGMUN-Docs/DOM-GDO/evidencias/`)
- [x] Matriz de rastreabilidade atualizada (012-Matriz-de-Rastreabilidade)
- [x] Mapa mestre atualizado (00-Governanca/000H-MAPA-MESTRE)

**Status da seção:** [x]
---

# 9. Implementação

- [x] Código-fonte disponível (`src/modules/sigmun_gdo` — Clean Architecture/DDD)
- [x] Código versionado (git; commit `f8d317b` em `main`)
- [x] Branch de produção definida (`main` — gatilho de CI/CD)
- [x] Versão de release definida (0.1.0)
- [x] Dependências identificadas (`requirements.txt` / `requirements-dev.txt` / `pyproject.toml`)
- [x] Dependências atualizadas (revisão validada no CI — Fase II)
- [x] Código revisado (lint e type-check 0 violações — Fase II)
- [x] Débitos técnicos críticos tratados (exceções de domínio centralizadas)
- [x] Configurações externas identificadas (`.env`; docker-compose com overrides)
- [x] Segredos não armazenados no código
- [x] Variáveis de ambiente configuradas (`src/shared/config`)
- [x] Scripts de implantação disponíveis (Makefile + docker-compose)
- [x] Scripts de rollback disponíveis (`alembic downgrade`; procedimento no 020)

**Status da seção:** [x]

---

# 10. Banco de Dados

- [x] Modelo físico validado (schema `gdo` com 11 tabelas)
- [x] Migrações versionadas (`20260901_02` e `20260901_03` Alembic)
- [x] Scripts de criação disponíveis (alembic + `infra/docker/database/init.sql`)
- [x] Scripts de atualização disponíveis (`alembic upgrade head` — Makefile migrate)
- [x] Índices revisados (`documentos.codigo`, `versoes_documentos.documento_id`, `eventos_outbox.status`)
- [x] Constraints revisadas (unicidade de código, checks de status/tipo/destinação, FKs)
- [x] Integridade referencial validada (documento inexistente 404 — H-20; hash inválido 400 — H-07)
- [x] Regras de unicidade validadas (RN-GDO-001 código duplicado 409 — H-06)
- [x] Dados iniciais preparados (seed idempotente: 12 tipos documentais, 9 classificações, 4 temporalidades)
- [x] Migração definitiva validada (reaplicável via `alembic upgrade head`)

**Status da seção:** [x]
---

# 11. Qualidade dos Dados

- [x] Dados obrigatórios disponíveis (seed validado no PostgreSQL)
- [x] Dados duplicados tratados (RN-GDO-001 unicidade de código — 409)
- [x] Dados inconsistentes tratados (validações de domínio e transições de estado)
- [x] Dados inválidos identificados (validação de entrada — 422/400/404/409)
- [x] Relacionamentos validados (integridade referencial homologada)
- [x] Identificadores preservados (UUIDs; códigos documentais únicos)
- [N/A] Origem dos dados identificada (sem carga de legado nesta fase — ver 022)
- [x] Migração de teste executada (migrações aplicadas em PostgreSQL na homologação)
- [x] Migração definitiva validada (E2E sobre PostgreSQL — ambiente disponível)

**Status da seção:** [x]

---

# 12. APIs

- [x] APIs implementadas (20 endpoints OpenAPI em `/api/v1/gdo`)
- [x] Endpoints documentados (OpenAPI em `/openapi.json`; docs `/docs` e ReDoc)
- [x] Autenticação validada (401 sem `X-Usuario-Id`/`X-Usuario-Papel` — provisório até DOM-IDN)
- [x] Autorização validada (403 — H-18 eliminação sem homologadora)
- [x] Validação de entrada implementada (Pydantic; 422 — H-08)
- [x] Tratamento de erros validado (400/404/409 com exceções de domínio centralizadas)
- [x] Unicidade validada (RN-GDO-001 — 409 H-06)
- [x] Paginação validada (`page`/`page_size` — H-21)
- [x] Versionamento definido (`/api/v1`)
- [x] Logs implementados (logging padrão nos routers; `logging_config` corporativo)
- [x] APIs críticas testadas (93 testes + homologação 23/23)

**Status da seção:** [x]

---

# 13. Serviços

- [x] Serviços de aplicação implementados (12 use cases em `application/use_cases`)
- [x] Contratos de serviço definidos (OpenAPI + schemas Pydantic request/response)
- [x] Dependências identificadas (injeção via `Depends`; repositórios em memória e SQLAlchemy)
- [x] Tratamento de exceções validado (`domain/exceptions.py` para 400/404/409)
- [x] Mensageria implementada (Transactional Outbox em `gdo.eventos_outbox`)
- [x] Tópicos de integração definidos (`TópicosGDO`)
- [x] Eventos publicados na mesma transação (integridade da outbox)
- [x] 9 repositórios SQLAlchemy com paginação e soft-delete

**Status da seção:** [x]
---

# 14. Integrações

- [x] Sistemas identificados (DOM-IDN identidade; DOM-CUM unidades; barramento de eventos — modelo 014)
- [x] Integração com storage de arquivos (conteúdo referenciado via `conteudo_ref` + hash SHA-256)
- [x] Outbox publicado (eventos disponíveis para consumidores — DOM-INT Fase V)
- [x] Responsável definido (Equipe SIGMUN)
- [N/A] Integrações externas (consumidores dependem de DOM-INT/DOM-IDN — Fases posteriores)

**Status da seção:** [x]

---

# 15. Segurança

- [x] Autenticação implementada (provisória por headers `X-Usuario-Id`/`X-Usuario-Papel` até DOM-IDN)
- [x] Autorização implementada (guardas 401/403 validadas na homologação H-18)
- [x] Perfis definidos (operador, gestor documental, autoridade homologadora, administrador — modelo 016)
- [!] Permissões revisadas (perfis provisórios; revisão formal com DOM-IDN)
- [!] Princípio do menor privilégio aplicado (refinar com identidade corporativa)
- [!] Segregação de funções validada (papéis exercitados na homologação; segregação formal pendente)
- [x] Credenciais protegidas (`.env` externo ao código)
- [x] Segredos não versionados (compose apenas com credenciais locais)
- [x] Integridade de conteúdo (hash SHA-256 — RN-GDO-002)
- [x] Sigilo documental (`is_sigiloso` no modelo de dados)
- [!] Comunicação protegida (TLS/HTTPS não configurado no ambiente atual — P-GDO-007)
- [x] Auditoria de segurança ativa (trilha de auditoria core)
- [!] Vulnerabilidades críticas tratadas (pentest pendente — P-GDO-007)

**Status da seção:** [!] (autenticação provisória e TLS pendentes antes de produção)

---

# 16. Auditoria

- [x] Auditoria implementada (trilha core + eventos de domínio)
- [x] Operações críticas auditadas (criação, versão, tramitação, assinatura, arquivamento, destinação)
- [x] Usuário registrado
- [x] Data/hora registrada
- [x] Operação registrada
- [x] Entidade registrada
- [x] Identificador registrado
- [x] Resultado registrado
- [x] Correlation ID registrado quando aplicável
- [x] Registros protegidos contra alteração indevida (outbox append-only)
- [x] Consulta de auditoria validada (acesso restrito)

**Status da seção:** [x] (homologação automatizada 23/23 — `scripts/homologacao_gdo.py`)

---

# 17. Logs

- [x] Logs de aplicação disponíveis (logging padrão nos routers; uvicorn)
- [x] Logs de erro disponíveis (exceções registradas; logs em `logs/`)
- [x] Logs de segurança disponíveis (trilha de auditoria)
- [N/A] Logs de integração externa (sem integrações externas nesta fase)
- [x] Correlation ID implementado quando aplicável (middleware corporativo)
- [!] Política de retenção definida (pendente — P-GDO-002)
- [x] Dados sensíveis não registrados indevidamente (logs com IDs e operações)
- [!] Logs consultáveis pela equipe autorizada (agregação centralizada pendente — P-GDO-002)

**Status da seção:** [!]

---

# 18. Testes

- [x] Testes unitários implementados (42 em `tests/unit/test_gdo_use_cases.py`)
- [x] Testes de integração implementados (51 — API, eventos/outbox e seeds)
- [x] Total da suíte do domínio: 93 testes
- [x] Suite completa do projeto: 520 passed (Fase II)
- [x] Lint e type-check: 0 violações (Fase II)
- [x] Critérios de aceitação homologados (E2E 23/23 — seção 19)
- [x] Performance validada (teste de carga 23/23 — seção 20)
- [x] Evidências registradas em `SIGMUN-Docs/DOM-GDO/evidencias/`

**Status da seção:** [x]
---

# 19. Homologação E2E

- [x] Roteiro executado (`python scripts/homologacao_gdo.py`)
- [x] Resultado: 23/23 verificações aprovadas (SUCESSO) em 3.22s
- [x] Pilha real validada (PostgreSQL 15 → Alembic → seed → API uvicorn)
- [x] H-00 migrações no head | H-01 health | H-02 OpenAPI (17 rotas na homologação)
- [x] H-03/H-04 seed de tipos e classificações
- [x] H-05/H-06/H-07/H-08 criação, RN-GDO-001 (409), RN-GDO-002 (400), payload 422
- [x] H-09/H-09b/H-10 versionamento (v1 e v2, histórico)
- [x] H-11/H-12 tramitação | H-13 temporalidade | H-14 assinatura
- [x] H-15/H-16/H-17/H-18/H-19 arquivamento, guarda permanente, estado final, RN-GDO-011 (403/200)
- [x] H-20/H-21 404 e listagem
- [x] Evidência: `SIGMUN-Docs/DOM-GDO/evidencias/2026-09-06-homologacao-gdo.md`

**Status da seção:** [x]

---

# 20. Teste de Carga (RNFs de Performance)

- [x] Roteiro executado (`python scripts/test_carga_gdo.py`)
- [x] Resultado: 23/23 testes, 0 falhas (exit 0)
- [x] GET `/tipos-documentais`: 50/50, avg 67.2ms, p95 237.4ms, 141 req/s
- [x] GET `/classificacoes`: 50/50, avg 41.9ms, p95 80.8ms, 218 req/s
- [x] GET `/temporalidades/TEMP-001`: 50/50, avg 33.8ms, p95 70.5ms, 280 req/s
- [x] POST `/documentos`: 20× 201, avg 10–35ms
- [x] SLA GET p95 < 500ms: CUMPRIDO
- [x] Latência média geral: ~17–19ms; duração total ~1.6s
- [x] Evidência: `SIGMUN-Docs/DOM-GDO/evidencias/2026-09-06-teste-carga-gdo.md`

**Status da seção:** [x]

---

# 21. Backup e Recuperação

- [x] Volume de dados persistente (`postgres_data` no docker-compose)
- [x] Script de backup disponível (`scripts/backup_postgres.py`)
- [x] Procedimento documentado (artefato 024, seção Backup)
- [!] Rotina de backup automática (cron/agendamento pendente — P-GDO-004)
- [!] Restauração testada (pendente — P-GDO-004)

**Status da seção:** [!]

---

# 22. Monitoramento

- [x] Health check implementado (`GET /health`)
- [x] Logs operacionais disponíveis (`logs/`)
- [x] Monitoramento via docker-compose (restart, healthcheck do postgres)
- [!] Métricas Prometheus/Grafana (pendente — Fase X.4)
- [!] Alertas de latência/erro 5xx (pendente — Fase X.4)
- [x] Monitoramento operacional manual durante a homologação (100% dos endpoints ok)

**Status da seção:** [!]
---

# 23. Suporte

- [x] Plano de suporte e operação elaborado (artefato 024)
- [x] Procedimentos de sustentação documentados (024)
- [x] Canais de suporte definidos (024)
- [x] Equipe de suporte capacitada (023/024)
- [!] SLA de atendimento formalizado (pendência institucional)

**Status da seção:** [!]

---

# 24. Treinamento

- [x] Plano de treinamento elaborado (artefato 023)
- [x] Perfis mapeados (operador de protocolo, arquivista, gestor, autoridade homologadora, admin)
- [x] Material de apoio definido (023)
- [!] Treinamento executado com os usuários finais (pendente institucional)
- [x] Roteiro prático documentado (023)

**Status da seção:** [!]

---

# 25. Documentação Operacional

- [x] Manuais operacionais referenciados (024)
- [x] Procedimentos de contingência documentados (024)
- [x] Documentação de migração disponível (022)
- [x] Termo de encerramento formalizado (026)

**Status da seção:** [x]

---

# 26. Plano de Comunicação

- [!] Comunicação da implantação aos órgãos (pendente institucional)
- [!] Calendário de treinamento divulgado (pendente)
- [x] Material de divulgação preparado (referências nos artefatos 023/024)

**Status da seção:** [!]

---

# 27. Pendências Registradas

| ID        | Descrição                                                | Impacto     | Responsável       |
| --------- | -------------------------------------------------------- | ----------- | ----------------- |
| P-GDO-002 | Política de retenção de logs / agregação centralizada    | Baixo       | Equipe SIGMUN     |
| P-GDO-004 | Rotina de backup e teste de restauração                  | Médio       | Equipe SIGMUN     |
| P-GDO-007 | TLS/HTTPS e pentest                                      | Alto (prod) | Equipe SIGMUN     |
| P-GDO-009 | Treinamento formal com usuários finais                   | Médio       | Prefeitura/Equipe |
| P-GDO-010 | Aprovação institucional do go-live                       | Alto        | Prefeitura        |

**Status da seção:** [!] (nenhuma pendência bloqueia homologação; P-GDO-007 e P-GDO-010 condicionam produção)

---

# 28. Decisão de Go-Live

Após análise do presente checklist:

- [ ] AUTORIZADA A ENTRADA EM PRODUÇÃO
- [ ] AUTORIZADA COM RESSALVAS
- [x] NÃO AUTORIZADA (pendências institucionais e de segurança non críticas)
- [ ] BLOQUEADA

**Justificativa:** O domínio DOM-GDO está implementado, homologado (23/23 E2E) e com performance validada (23/23 carga). As pendências restantes são de natureza institucional (aprovação go-live) e de infraestrutura (TLS/HTTPS, política de retenção), a concluir em fase operacional posterior. Homologação e teste de carga concluídos com sucesso. Recomenda-se prosseguir com implantação controlada (artefato 020).

---

# 29. Controle de Versões

| Versão | Data       | Descrição                                                                        |
| ------ | ---------- | -------------------------------------------------------------------------------- |
| 1.0    | 2026-08-20 | Criação do esboço inicial padronizado do artefato                                |
| 2.0    | 2026-09-06 | Preenchimento completo com evidências de homologação (23/23) e teste de carga (23/23) e formalização do gate de produção |

---

**Documento:** 021-Checklist-de-Prontidao-para-Producao-Gestao-Documental.md

**Última atualização:** 2026-09-06

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
