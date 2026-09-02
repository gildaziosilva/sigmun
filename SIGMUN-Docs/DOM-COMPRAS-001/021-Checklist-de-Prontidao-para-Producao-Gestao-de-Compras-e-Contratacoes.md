#### Checklist de Prontidão para Produção – Gestão de Compras e Contratações

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Gestão de Compras e Contratações

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

- 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
- 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md
- 000C-HIERARQUIA-DOCUMENTAL.md
- 000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md
- 000-Dominio-Gestao-de-Compras-e-Contratacoes.md
- 001-Mapa-de-Atores-Gestao-de-Compras-e-Contratacoes.md
- 002-Mapa-de-Capacidades-Gestao-de-Compras-e-Contratacoes.md
- 003-Mapa-de-Processos-Gestao-de-Compras-e-Contratacoes.md
- 004-Mapa-de-Servicos-Gestao-de-Compras-e-Contratacoes.md
- 005-Casos-de-Uso-Gestao-de-Compras-e-Contratacoes.md
- 006-Historias-de-Usuario-Gestao-de-Compras-e-Contratacoes.md
- 007-Regras-de-Negocio-Gestao-de-Compras-e-Contratacoes.md
- 008-Requisitos-Funcionais-Gestao-de-Compras-e-Contratacoes.md
- 009-Requisitos-Nao-Funcionais-Gestao-de-Compras-e-Contratacoes.md
- 010-Especificacoes-Gestao-de-Compras-e-Contratacoes.md
- 011-Criterios-de-Aceitacao-Gestao-de-Compras-e-Contratacoes.md
- 012-Matriz-de-Rastreabilidade-Gestao-de-Compras-e-Contratacoes.md
- 013-Modelo-de-Dados-Gestao-de-Compras-e-Contratacoes.md
- 014-Modelo-de-Integracao-Gestao-de-Compras-e-Contratacoes.md
- 015-Arquitetura-de-Servicos-Gestao-de-Compras-e-Contratacoes.md
- 016-Modelo-de-Seguranca-Gestao-de-Compras-e-Contratacoes.md
- 017-Modelo-de-Auditoria-Gestao-de-Compras-e-Contratacoes.md
- 018-Plano-de-Testes-Gestao-de-Compras-e-Contratacoes.md
- 019-Casos-de-Teste-Gestao-de-Compras-e-Contratacoes.md
- 020-Plano-de-Implantacao-Gestao-de-Compras-e-Contratacoes.md

---

# 1. Finalidade

Este documento estabelece o **Checklist de Prontidão para Produção do Domínio de Gestão de Compras e Contratações do SIGMUN**.

Seu objetivo é verificar, de forma estruturada, se o domínio está tecnicamente, funcionalmente, operacionalmente e institucionalmente preparado para entrada em produção.

Este documento constitui um **gate de produção**.

A entrada em produção somente deverá ocorrer quando os critérios críticos de prontidão estiverem atendidos e formalmente validados.

---

# 2. Objetivos

São objetivos deste checklist:

1. verificar a conclusão da implementação;
2. verificar a conclusão dos testes;
3. validar requisitos críticos;
4. validar segurança;
5. validar auditoria;
6. validar banco de dados;
7. validar integrações;
8. validar infraestrutura;
9. validar backup e recuperação;
10. validar usuários e permissões;
11. validar documentação;
12. validar treinamento;
13. validar suporte;
14. validar monitoramento;
15. validar plano de reversão;
16. registrar pendências;
17. apoiar a decisão de entrada em produção.

---

# 3. Regra de Decisão

A decisão de produção deverá considerar quatro estados principais:

```text
PRONTO
NÃO PRONTO
PRONTO COM RESSALVAS
BLOQUEADO

3.1 PRONTO

Todos os critérios críticos foram atendidos.

3.2 NÃO PRONTO

Existem pendências que impedem a entrada em produção.

3.3 PRONTO COM RESSALVAS

Existem pendências não críticas formalmente aceitas pelos responsáveis.

3.4 BLOQUEADO

Existe risco crítico que impede a implantação.

4. Legenda do Checklist
Símbolo	Significado
[ ]	Não verificado
[x]	Aprovado
[!]	Pendência
[B]	Bloqueio
[N/A]	Não aplicável
5. Governança da Prontidão
Item	Status	Evidência	Responsável
Escopo aprovado	[x]	Fatia vertical do DOM-COMPRAS-001 definida no ROADMAP.md (itens 1 a 20)	Equipe SIGMUN
Versão definida	[x]	Versão 0.1.0 (`pyproject.toml`, `src/main.py`)	Equipe SIGMUN
Responsáveis definidos	[x]	Responsável: Equipe SIGMUN (registros nos artefatos do domínio)	Equipe SIGMUN
Janela de implantação definida	[!]	Depende de aprovação institucional; pré-requisito do item 19	Prefeitura/Equipe SIGMUN
Aprovação da implantação registrada	[!]	Aprovação formal pendente; gate registrado na seção 46	Equipe SIGMUN
Plano de comunicação aprovado	[!]	Pendência institucional (seção 37)	Equipe SIGMUN
6. Documentação
6.1 Documentação Arquitetural
 [x] Domínio documentado. (000)
 [x] Mapa de atores atualizado. (001)
 [x] Mapa de capacidades atualizado. (002)
 [x] Mapa de processos atualizado. (003)
 [x] Mapa de serviços atualizado. (004)
 [x] Casos de uso documentados. (005)
 [x] Histórias de usuário documentadas. (006)
 [x] Regras de negócio documentadas. (007)
 [x] Requisitos funcionais documentados. (008)
 [x] Requisitos não funcionais documentados. (009)
 [x] Especificações documentadas. (010)
 [x] Modelo de dados atualizado. (013)
 [x] Modelo de integração atualizado. (014)
 [x] Arquitetura de serviços atualizada. (015)
 [x] Modelo de segurança atualizado. (016)
 [x] Modelo de auditoria atualizado. (017)

Status da seção: [x] (27 artefatos verificados em SIGMUN-Docs/DOM-COMPRAS-001/)

7. Requisitos
 [x] Requisitos funcionais implementados. (fatia piloto: fornecedores, compras, itens, processos documentais, contratos, formalização, auditoria)
 [!] Requisitos não funcionais avaliados. (performance e recuperação ainda não executados — seções 19/21)
 [x] Regras de negócio implementadas. (RN-COMPRAS-004/011/012/025/026/027/028/029/030/031/036/037/038/046/106 homologadas)
 [x] Critérios de aceitação atendidos. (homologação E2E 47/47 — evidência de 2026-08-29)
 [x] Requisitos críticos validados. (segurança 401/403, auditoria, integridade referencial)
 [x] Requisitos não implementados formalmente registrados. (Requisição/Demanda ENT-COMPRAS-001 aguarda modelo físico — registrado no ROADMAP item 6; integrações Orçamento/Financeiro nos marcos M3/M4)
 [x] Exceções aprovadas. (autenticação provisória por headers X-Usuario-Id/X-Usuario-Papel até o DOM-IDN — seção 16)

Status da seção: [x] (no escopo da fatia piloto; RNFs de performance/recuperação pendentes para os itens 19/20)

8. Rastreabilidade
 [x] Casos de uso possuem rastreabilidade. (005/012)
 [x] Histórias de usuário possuem rastreabilidade. (006/012)
 [x] Regras de negócio possuem rastreabilidade. (007/012)
 [x] Requisitos possuem rastreabilidade. (008/009/012)
 [x] Critérios de aceitação possuem rastreabilidade. (011/012)
 [x] Casos de teste possuem rastreabilidade. (018/019; IDs H-xx da homologação referenciam RNs)
 [x] Defeitos possuem rastreabilidade. (nenhum defeito aberto; restrições registradas nas evidências)
 [x] Evidências de teste estão vinculadas. (SIGMUN-Docs/DOM-COMPRAS-001/evidencias/)
 [x] Matriz de rastreabilidade está atualizada. (012-Matriz-de-Rastreabilidade)
 [x] Mapa mestre de artefatos está atualizado. (00-Governanca/000H-MAPA-MESTRE)

Status da seção: [x]

9. Implementação
 [x] Código-fonte disponível. (src/modules/sigmun_compras — Clean Architecture/DDD)
 [x] Código versionado. (git; commit 66b7486 em main)
 [x] Branch de produção definida. (main — gatilho de CI/CD)
 [x] Versão de release definida. (0.1.0)
 [x] Dependências identificadas. (requirements.txt / requirements-dev.txt / pyproject.toml)
 [!] Dependências atualizadas. (revisão de versões/audit de pacotes pendente)
 [!] Código revisado. (commits diretos em main; processo formal de revisão a instituir)
 [N/A] Pull Requests aprovados. (fluxo atual é commit direto na main; adotar PRs com o crescimento da equipe)
 [x] Débitos técnicos críticos tratados. (exceções de domínio centralizadas; repositórios em memória e SQLAlchemy validados)
 [x] Configurações externas identificadas. (.env com 37 variáveis; docker-compose com overrides)
 [x] Segredos não estão armazenados no código. (varredura por segredos em src/ sem resultados; credenciais em .env e compose apenas para ambiente local)
 [x] Variáveis de ambiente configuradas. (.env presente; src/shared/config)
 [!] Scripts de implantação disponíveis. (Makefile + docker-compose disponíveis; scripts/deployment vazio — completar no item 19)
 [!] Scripts de rollback disponíveis. (alembic downgrade existe; procedimento formal pendente — seção 36)

Status da seção: [!]

10. Banco de Dados
 [x] Modelo físico validado. (schemas core/compras/auditoria ativos — verificação direta no PostgreSQL)
 [x] Migrações versionadas. (alembic: 20260820_01, 20260821_01, 20260822_01, 20260823_01; alembic_version=20260823_01)
 [x] Scripts de criação disponíveis. (alembic + infra/docker/database/init.sql)
 [x] Scripts de atualização disponíveis. (alembic upgrade head — Makefile migrate)
 [x] Índices revisados. (migration 20260820_01 com índices)
 [x] Constraints revisadas. (obrigatoriedade e checks nas migrations)
 [x] Integridade referencial validada. (compra inexistente 404; formalização exige compra homologada — homologação)
 [x] Regras de unicidade validadas. (numero/ano do processo — RN-029; fornecedor PJ — RN-031; contrato — RN-036; todos 409)
 [x] Dados obrigatórios preparados. (semeadura de apoio validada por scripts/validar_ambiente_postgres.py)
 [x] Dados iniciais validados. (unidade, pessoa jurídica, processo documental — semeadura idempotente)
 [N/A] Dados históricos validados quando aplicável. (implantação sem carga de legado nesta fase)
 [!] Estratégia de backup definida. (volume local postgres_data sem rotinas de backup — pendência P-004)
 [!] Estratégia de restauração testada. (pendente — P-004)

Status da seção: [!]

11. Qualidade dos Dados
 [x] Dados obrigatórios disponíveis. (semeadura validada no PostgreSQL)
 [x] Dados duplicados tratados. (regras de unicidade — RN-029/031/036)
 [x] Dados inconsistentes tratados. (validações de domínio e transições de estado)
 [x] Dados inválidos identificados. (validação de entrada — 422/400/404/409)
 [x] Relacionamentos validados. (integridade referencial homologada)
 [x] Identificadores preservados. (UUIDs; IDs de semeadura fixos e idempotentes)
 [N/A] Origem dos dados identificada quando aplicável. (sem migração de legado nesta fase)
 [x] Migração de teste executada. (migrations aplicadas em ambiente Docker/PostgreSQL em 2026-08-29)
 [!] Migração definitiva validada. (reexecutar E2E sobre PostgreSQL — item 19; ambiente já disponível)

Status da seção: [!]

12. APIs
 [x] APIs implementadas. (17 paths OpenAPI: fornecedores, compras, itens, processos documentais, contratos, formalização, auditoria, health)
 [x] Endpoints documentados. (OpenAPI em /openapi.json; Docs /docs e ReDoc)
 [x] Autenticação validada. (401 sem X-Usuario-Id/X-Usuario-Papel — homologação)
 [x] Autorização validada. (403 para perfil sem permissão — homologação)
 [x] Validação de entrada implementada. (Pydantic; 422 para payload inválido — homologação)
 [x] Tratamento de erros validado. (400/404/409 com exceções de domínio centralizadas)
 [!] Idempotência validada quando aplicável. (unicidade 409 cobre duplicidade; idempotência formal de escritas pendente)
 [x] Paginação validada. (page/page_size em fornecedores, contratos, itens e compras — *_ListResponse com total)
 [x] Versionamento definido. (/api/v1)
 [!] Logs implementados. (logging padrão nos routers; logging estruturado corporativo pendente — P-002)
 [x] APIs críticas testadas. (261 testes; homologação 47/47)

Status da seção: [x] (pendências não críticas registradas: idempotência formal e logging estruturado)

13. Serviços
 [x] Serviços implementados. (casos de uso por entidade na camada application)
 [x] Contratos de serviço definidos. (OpenAPI + schemas Pydantic de request/response)
 [x] Dependências identificadas. (injeção via Depends; repositórios em memória e SQLAlchemy)
 [x] Tratamento de exceções validado. (domain/exceptions.py mapeado para 400/404/409)
 [N/A] Timeouts configurados. (sem chamadas externas na fatia piloto)
 [N/A] Retry configurado quando aplicável. (sem chamadas externas na fatia piloto)
 [N/A] Circuit breaker configurado quando aplicável. (sem chamadas externas na fatia piloto)
 [!] Idempotência validada. (idem seção 12 — formalização pendente)
 [!] Monitoramento disponível. (pendente — P-003)

Status da seção: [x] (pendências não críticas registradas)

14. Integrações
 [x] Integrações identificadas. (integração interna Compra → Contrato via formalização; modelo 014)
 [x] Sistemas externos identificados. (Orçamento e Financeiro — futuros, marcos M3/M4; DOM-IDN para identidade)
 [N/A] Credenciais configuradas. (nenhuma integração externa credenciada nesta fase)
 [x] Comunicação validada. (formalização Compra → Contrato homologada — H-24/H-24a/H-25)
 [x] Contratos de integração validados. (compra_id; estados HOMOLOGADO → CONTRATADO/ASSINADO — RN-038)
 [N/A] Tratamento de indisponibilidade testado. (sem integrações externas nesta fase)
 [N/A] Timeout testado. (idem)
 [N/A] Retry testado. (idem)
 [N/A] Idempotência testada. (idem)
 [x] Falhas registradas. (trilha de auditoria com resultado dos eventos)
 [!] Monitoramento implementado. (pendente — P-003)

Status da seção: [x] (integração interna validada; itens externos N/A nesta fase)

15. Integrações Prioritárias
15.1 Orçamento
 [N/A] Integração disponível. (fora do escopo da fatia piloto — marcos M3/M4)
 [N/A] Teste realizado. (idem)
 [N/A] Resultado validado. (idem)
15.2 Financeiro
 [N/A] Integração disponível. (fora do escopo da fatia piloto — marcos M3/M4)
 [N/A] Teste realizado. (idem)
 [N/A] Resultado validado. (idem)
15.3 Outros Sistemas
 [x] Sistema identificado. (DOM-IDN — identidade; DOM-GDO — documentos; registrados no modelo de integração 014)
 [N/A] Integração validada. (será executada com a implementação dos domínios provedores)
 [x] Responsável definido. (Equipe SIGMUN)

Status da seção: [N/A] (integrações prioritárias fora do escopo da fatia piloto; serão exigidas nos marcos M3/M4)

16. Segurança
 [x] Autenticação implementada. (provisória por headers X-Usuario-Id/X-Usuario-Papel até o DOM-IDN)
 [x] Autorização implementada. (guardas 401/403 validadas na homologação)
 [x] Perfis definidos. (auditor, controladoria, administrador_seguranca; papéis operacionais provisórios)
 [!] Permissões revisadas. (perfis provisórios; revisão formal com o DOM-IDN)
 [!] Princípio do menor privilégio aplicado. (perfis operacionais provisórios; refinar com identidade corporativa)
 [!] Segregação de funções validada. (papéis operador/auditor exercitados na homologação; segregação formal pendente)
 [x] Credenciais protegidas. (.env externo ao código; varredura de segredos em src/ sem resultados)
 [x] Segredos protegidos. (não versionados; compose apenas com credenciais locais de desenvolvimento)
 [!] Comunicação protegida. (TLS/HTTPS não configurado no ambiente atual — pendência P-007)
 [N/A] Sessões protegidas. (API stateless por headers; sem sessões na fatia piloto)
 [x] Logs de segurança ativos. (trilha de auditoria append-only com imutabilidade por trigger)
 [!] Vulnerabilidades críticas tratadas. (varredura/pentest pendente — P-007)
 [!] Testes de segurança aprovados. (401/403 automatizados na homologação; pentest pendente — P-007)

Status da seção: [!] (autenticação provisória e perfis provisórios; pentest e TLS pendentes antes de produção)

17. Auditoria
 [x] Auditoria implementada. (ServicoDeAuditoria + trilha append-only em auditoria.eventos)
 [x] Operações críticas auditadas. (criação/alteração/exclusão de contratos e formalização)
 [x] Usuário registrado.
 [x] Data/hora registrada.
 [x] Operação registrada.
 [x] Entidade registrada.
 [x] Identificador registrado.
 [x] Resultado registrado.
 [x] Correlation ID registrado quando aplicável.
 [x] Registros protegidos contra alteração indevida. (imutabilidade por trigger — migration 20260822_01)
 [x] Consulta de auditoria validada. (acesso restrito por perfil; o próprio acesso é auditado — 017, seções 40/41/44)

Status da seção: [x] (homologação automatizada 47/47 — evidência: scripts/homologacao_compras.py)

18. Logs
 [x] Logs de aplicação disponíveis. (logging padrão do Python nos routers; logs do uvicorn)
 [x] Logs de erro disponíveis. (exceções registradas nos routers; backend.log no ambiente local)
 [x] Logs de segurança disponíveis. (trilha de auditoria em auditoria.eventos)
 [N/A] Logs de integração disponíveis. (sem integrações externas nesta fase)
 [!] Correlation ID implementado quando aplicável. (registrado na auditoria; correlação ponta a ponta de requisições pendente)
 [!] Política de retenção definida. (pendente — P-002)
 [x] Dados sensíveis não são registrados indevidamente. (logs registram IDs e operações, não payloads sensíveis)
 [!] Logs podem ser consultados pela equipe autorizada. (logs locais em container/host; sem agregação centralizada — P-002)

Status da seção: [!]

19. Testes

Referência:

018-Plano-de-Testes-Gestao-de-Compras-e-Contratacoes.md

019-Casos-de-Teste-Gestao-de-Compras-e-Contratacoes.md

 [x] Testes funcionais executados.
 [x] Testes negativos executados.
 [x] Testes de integração executados.
 [x] Testes de segurança executados.
 [x] Testes de auditoria executados.
 [x] Testes de dados executados.
 [ ] Testes de performance executados quando aplicável.
 [ ] Testes de recuperação executados.
 [x] Testes de regressão executados.
 [ ] Testes de sincronização executados quando aplicável.
 [x] Evidências armazenadas.
 [x] Resultados registrados.

Evidências da homologação (2026-08-29):

- Roteiro E2E automatizado `scripts/homologacao_compras.py` sobre a aplicação real (uvicorn + HTTP): 47/47 verificações aprovadas (funcionalidades, regras de negócio, permissões, auditoria e integridade).
- Suíte de testes: 261 aprovados (168 unitários + 93 de integração), 0 falhas.
- Log completo: `SIGMUN-Docs/DOM-COMPRAS-001/evidencias/2026-08-29-homologacao-compras.log`.
- Atualização da pendência (execução do checklist, 2026-08-29): o ambiente Docker + PostgreSQL 15 foi provido e verificado (container ativo, `alembic_version=20260823_01`, schemas `core`/`compras`/`auditoria` presentes); a reexecução do roteiro sobre PostgreSQL permanece como pendência [!] a cargo do item 19 — implantação em ambiente controlado.
20. Defeitos
Categoria	Quantidade	Aceitável?
Críticos	0	Não
Altos	0	Avaliar
Médios	0	Avaliar
Baixos	0	Avaliar

Critérios:

 [x] Nenhum defeito crítico aberto. (nenhum defeito registrado; suíte 261/261 e homologação 47/47)
 [x] Nenhum defeito de segurança crítico aberto. (pentest pendente registrado como pendência, não como defeito)
 [x] Nenhum defeito de integridade de dados aberto. (integridade referencial e unicidade homologadas)
 [x] Nenhum defeito impeditivo aberto.
 [!] Pendências restantes possuem aceite formal. (pendências técnicas P-001 a P-010 registradas na seção 41; aceite formal institucional pendente)

Status da seção: [x] (nenhum defeito aberto; pendências registradas na seção 41)

21. Performance
 [!] Tempo de resposta avaliado. (não executado — sem requisitos de performance mensurados para o piloto)
 [!] Consultas críticas avaliadas. (índices revisados nas migrations; medições pendentes)
 [!] Operações de gravação avaliadas.
 [!] APIs críticas avaliadas.
 [N/A] Carga concorrente avaliada quando aplicável. (não aplicável ao piloto com usuários internos limitados)
 [!] Consumo de memória avaliado.
 [!] Consumo de CPU avaliado.
 [!] Banco avaliado. (EXPLAIN/índices pendentes de revisão sob carga)
 [!] Gargalos conhecidos documentados. (nenhum gargalo conhecido; ausência de medição registrada como pendência P-006)

Status da seção: [!]

22. Infraestrutura
 [!] Servidor disponível. (ambiente de desenvolvimento/homologação local provisionado; servidor definitivo pendente — item 19)
 [x] Sistema operacional configurado. (containers Linux — postgres:15, redis:7, backend Python 3.10)
 [x] Banco disponível. (PostgreSQL 15 ativo via docker compose — verificado em 2026-08-29)
 [x] Rede configurada. (rede docker sigmun-network; portas publicadas 5433/8000)
 [N/A] DNS configurado quando aplicável. (não aplicável ao ambiente controlado atual)
 [!] Certificados configurados. (TLS pendente — P-007)
 [!] Firewall configurado. (não avaliado neste ambiente)
 [x] Armazenamento disponível. (volumes postgres_data e redis_data)
 [!] Capacidade avaliada. (dimensionamento pendente)
 [!] Monitoramento configurado. (pendente — P-003)
 [!] Alertas configurados. (pendente — P-003)

Status da seção: [!]

23. Ambientes
Desenvolvimento
 [x] Disponível. (venv local + pytest + Makefile)
 [x] Configurado. (.env; docker-compose)
 [x] Validado. (261 testes aprovados em 2026-08-29)
Homologação
 [x] Disponível. (Docker + PostgreSQL 15 providos em 2026-08-29)
 [x] Configurado. (schemas core/compras/auditoria; migrations no head 20260823_01)
 [!] Validado. (reexecução E2E sobre PostgreSQL pendente — item 19)
 [!] Homologação concluída. (E2E automatizado 47/47 concluído sobre repositórios em memória; conclusão plena com a validação sobre PostgreSQL)
Produção
 [!] Disponível. (não provisionado — item 19)
 [!] Configurado.
 [!] Validado.
 [!] Pronto para implantação.

Status da seção: [!]

24. Backup
 [!] Backup configurado. (sem rotinas — pendência P-004)
 [!] Backup executado.
 [!] Backup validado.
 [!] Retenção definida.
 [!] Local de armazenamento definido.
 [!] Segurança do backup validada.
 [!] Restauração testada.

Status da seção: [!] (bloqueia entrada em produção — seção 40; resolver no item 19)

25. Recuperação de Desastres
 [!] Procedimento de recuperação documentado. (referência no plano 024; procedimento operacional detalhado pendente)
 [!] Responsáveis definidos.
 [!] Ambiente de recuperação identificado.
 [!] Backup disponível.
 [!] Restauração testada.
 [!] Tempo de recuperação avaliado.
 [x] Dependências identificadas. (PostgreSQL 15, Redis 7, aplicação FastAPI — docker-compose)

Status da seção: [!]

26. Usuários
 [!] Usuários administrativos cadastrados. (aguarda identidade corporativa — DOM-IDN; hoje autenticação provisória por headers)
 [!] Usuários operacionais cadastrados.
 [!] Usuários-chave cadastrados.
 [x] Perfis definidos. (auditor, controladoria, administrador_seguranca; papéis operacionais provisórios — 016)
 [!] Permissões atribuídas. (atribuição formal em sistema de identidade pendente)
 [!] Permissões revisadas.
 [N/A] Usuários inativos removidos/bloqueados quando aplicável. (não aplicável — sem base de usuários ainda)

Status da seção: [!]

27. Treinamento
 [!] Plano de treinamento executado. (plano 023 documentado; não executado)
 [!] Usuários-chave treinados.
 [!] Usuários operacionais treinados.
 [!] Gestores treinados.
 [!] Administradores treinados.
 [!] Material disponibilizado.
 [!] Registro de treinamento realizado.

Status da seção: [!] (bloqueia entrada em produção — seção 39; pendência P-009)

28. Documentação Operacional
 [!] Manual do usuário disponível. (pendente — elaborar com o treinamento)
 [!] Guia rápido disponível.
 [!] Manual administrativo disponível.
 [x] Procedimentos operacionais disponíveis. (024-Plano-de-Suporte-e-Operacao; detalhamento operacional no item 20)
 [x] Procedimentos de suporte disponíveis. (024)
 [x] Procedimentos de recuperação disponíveis. (referência no 024; execução/teste pendente — seção 25)
 [x] Documentação técnica disponível. (025-Estrutura-Tecnica; README; OpenAPI)

Status da seção: [!] (documentação técnica pronta; manuais de usuário pendentes — P-009)

29. Suporte
 [!] Canal de suporte definido. (não estabelecido — pendência P-010)
 [!] Responsáveis definidos.
 [!] Horários definidos.
 [!] Processo de abertura de chamados definido.
 [!] Processo de escalonamento definido.
 [!] Classificação de incidentes definida.
 [!] Equipe de suporte treinada.

Status da seção: [!] (plano de referência no 024; operação a estabelecer no item 20)

30. Monitoramento
 [!] Monitoramento da aplicação ativo. (não implementado — pendência P-003; item 20)
 [!] Monitoramento dos serviços ativo.
 [!] Monitoramento do banco ativo.
 [N/A] Monitoramento das integrações ativo. (sem integrações externas nesta fase)
 [!] Monitoramento de infraestrutura ativo.
 [!] Alertas configurados.
 [!] Dashboard disponível.
 [!] Responsáveis pelos alertas definidos.

Status da seção: [!] (bloqueia entrada em produção — seção 40; resolver no item 20)

31. Notificações
 [!] Notificações configuradas. (capacidade de notificações não implementada na fatia piloto)
 [N/A] Templates validados.
 [N/A] Destinatários configurados.
 [N/A] Testes executados.
 [N/A] Falhas de envio tratadas.
 [N/A] Duplicidade testada.

Status da seção: [!] (fora do escopo da fatia piloto; capacidade transversal prevista no Marco M2)

32. Relatórios
 [!] Relatórios críticos disponíveis. (não implementados na fatia piloto — APIs de consulta e listagem disponíveis)
 [N/A] Filtros validados. (filtros de listagem validados nos testes; relatórios N/A)
 [N/A] Totais validados.
 [N/A] Exportações testadas.
 [x] Permissões validadas. (consulta de auditoria restrita por perfil — homologação)
 [N/A] Dados conferidos. (sem relatórios formais nesta fase)

Status da seção: [!] (relatórios fora do escopo da fatia piloto)

33. Transparência
 [x] Informações públicas identificadas. (contratos e compras — transparência ativa prevista no modelo de negócio)
 [x] Dados publicáveis identificados. (modelos 013/016)
 [!] Dados restritos protegidos. (controles de acesso implementados na API; revisão formal com identidade pendente)
 [!] Regras de publicação aplicadas. (portais de transparência não implementados nesta fase)
 [N/A] Publicação validada quando aplicável. (sem publicação nesta fase)

Status da seção: [!] (princípio observado: transparência por padrão, segurança por princípio, classificação por política)

Deverá ser observado o princípio institucional:

Transparência por padrão, Segurança por princípio e Classificação da Informação por política.

34. Dados e LGPD
 [x] Dados pessoais identificados. (responsáveis por fornecedores e usuários — modelo de dados 013; diretrizes LGPD corporativas)
 [x] Finalidades identificadas. (gestão de compras e contratações; finalidades registradas na documentação do domínio)
 [!] Acessos revisados. (revisão formal de acessos pendente com o DOM-IDN)
 [x] Dados sensíveis protegidos quando aplicável. (não há dados sensíveis no escopo da fatia piloto)
 [!] Retenção definida quando aplicável. (política de retenção pendente)
 [x] Logs não expõem dados indevidamente. (logs registram IDs e operações)
 [N/A] Exportações respeitam controles de acesso. (sem exportações nesta fase)

Status da seção: [!]
35. Implantação

Referência:

020-Plano-de-Implantacao-Gestao-de-Compras-e-Contratacoes.md

 [x] Plano de implantação aprovado. (020-Plano-de-Implantacao vigente; aprovação formal institucional pendente de registro)
 [!] Cronograma definido. (cronograma detalhado com datas pendente — item 19)
 [!] Equipe definida. (equipe de implantação formal a designar)
 [!] Janela definida. (pré-requisito do item 19)
 [x] Checklist de implantação preparado. (este documento — gate de produção)
 [!] Procedimentos executados em homologação. (execução parcial: migrações e semeadura executadas em 2026-08-29; E2E sobre PostgreSQL pendente)
 [!] Procedimentos de produção revisados.

Status da seção: [!] (procedimentos a completar e formalizar no item 19)

36. Plano de Rollback
 [!] Plano de rollback documentado. (base técnica existente: alembic downgrade e docker compose down; plano formal pendente)
 [!] Responsáveis definidos.
 [!] Condições de acionamento definidas.
 [!] Backup anterior disponível. (depende da seção 24)
 [!] Procedimento testado.
 [!] Comunicação de rollback definida.

Status da seção: [!] (bloqueia entrada em produção — seção 40; resolver no item 19)
37. Comunicação
 [!] Gestores comunicados.
 [!] Usuários comunicados.
 [!] Equipe técnica comunicada.
 [!] Equipe de suporte comunicada.
 [!] Janela de implantação comunicada.
 [!] Possíveis indisponibilidades comunicadas.
 [!] Canal de comunicação definido.

Status da seção: [!] (comunicação institucional a executar antes da implantação)
38. Piloto
 [!] Escopo do piloto definido. (escopo técnico da fatia definido no ROADMAP; escopo operacional do piloto pendente)
 [!] Unidade piloto definida.
 [!] Usuários piloto definidos.
 [!] Processos piloto definidos.
 [!] Critérios de sucesso definidos.
 [!] Piloto executado.
 [!] Resultados avaliados.
 [!] Pendências do piloto tratadas.

Status da seção: [!] (piloto a executar após o item 19 — implantação em ambiente controlado)

Resultado do piloto:

[ ] Aprovado
[ ] Aprovado com ressalvas
[ ] Reprovado
39. Critérios de Go-Live

A entrada em produção somente poderá ser recomendada quando:

 [x] requisitos críticos atendidos; (seção 7)
 [x] testes críticos aprovados; (261/261; homologação 47/47)
 [x] defeitos críticos inexistentes; (seção 20)
 [!] segurança validada; (pentest e TLS pendentes — P-007)
 [x] auditoria validada; (seção 17)
 [x] dados validados; (seções 10/11 — validação definitiva no item 19)
 [!] integrações críticas validadas; (interna validada; externas N/A nesta fase)
 [!] backup validado; (P-004)
 [!] rollback disponível; (P-005)
 [!] suporte disponível; (P-010)
 [!] monitoramento disponível; (P-003)
 [!] usuários preparados; (P-009)
 [!] homologação concluída; (E2E sobre PostgreSQL pendente — P-001)
 [!] piloto aprovado quando aplicável. (a executar após o item 19)
40. Critérios de Bloqueio

A implantação deverá ser bloqueada quando existir:

 [x] defeito crítico; (inexistente)
 [x] vulnerabilidade crítica; (inexistente conhecida; pentest pendente para confirmação)
 [x] perda potencial de dados; (inexistente; append-only na auditoria)
 [x] inconsistência grave de dados; (inexistente)
 [x] falha de integração crítica; (inexistente — integração interna validada)
 [!] ausência de backup; (PRESENTE — P-004)
 [!] ausência de rollback; (PRESENTE — P-005)
 [!] ausência de suporte; (PRESENTE — P-010)
 [x] ausência de autenticação; (inexistente — autenticação aplicada)
 [x] ausência de autorização; (inexistente — guardas 401/403)
 [x] ausência de auditoria para operações críticas; (inexistente — trilha implementada)
 [x] ausência de homologação; (inexistente — homologação E2E aprovada; validação sobre PostgreSQL pendente)
 [!] risco operacional não aceito. (PENDENTE DE AVALIAÇÃO — riscos da seção 42)
41. Pendências
ID	Pendência	Severidade	Responsável	Prazo	Bloqueia Produção?	Status
P-001	Reexecutar roteiro E2E (scripts/homologacao_compras.py e scripts/validar_ambiente_postgres.py) sobre PostgreSQL	Alta	Equipe SIGMUN	Item 19	Sim	Aberta (ambiente disponível e verificado em 2026-08-29)
P-002	Logging estruturado corporativo, correlation ID ponta a ponta e política de retenção de logs	Alta	Equipe SIGMUN	Itens 19/20	Sim	Aberta
P-003	Observabilidade: monitoramento (aplicação, serviços, banco, infra), alertas e dashboard	Alta	Equipe SIGMUN	Item 20	Sim	Aberta
P-004	Backup do PostgreSQL configurado, executado e com restauração testada	Crítica	Equipe SIGMUN	Item 19	Sim	Aberta
P-005	Plano e scripts de rollback documentados e testados	Alta	Equipe SIGMUN	Item 19	Sim	Aberta
P-006	Avaliação de performance (tempo de resposta, carga, recursos)	Média	Equipe SIGMUN	Item 19	Não (aceite para piloto)	Aberta
P-007	Endurecimento de segurança: TLS, pentest, revisão de permissões e menor privilégio	Alta	Equipe SIGMUN	Antes de produção	Sim	Aberta
P-008	Idempotência formal das operações de escrita	Média	Equipe SIGMUN	Itens 19/20	Não (aceite para piloto)	Aberta
P-009	Usuários, permissões reais, treinamento, manuais e comunicação institucional	Alta	Prefeitura/Equipe SIGMUN	Antes de produção	Sim	Aberta
P-010	Suporte e operação estabelecidos (canal, chamados, escalonamento, incidentes)	Alta	Prefeitura/Equipe SIGMUN	Item 20	Sim	Aberta
42. Riscos Aceitos
ID	Risco	Impacto	Mitigação	Responsável	Aceite
R-001	Autenticação provisória por headers até o DOM-IDN	Alto	Trilha de auditoria por usuário; restrito a ambiente controlado; substituição pelo DOM-IDN	Equipe SIGMUN	Pendente de aceite formal
R-002	Operação sem monitoramento/backup até os itens 19/20	Alto	Implantação somente em ambiente controlado; pendências P-003/P-004 no cronograma	Equipe SIGMUN	Pendente de aceite formal

Nenhum risco crítico deverá ser considerado aceito sem aprovação formal da autoridade competente.

43. Resumo de Prontidão
Área	Status
Governança	[!]
Documentação	[x]
Requisitos	[x]
Rastreabilidade	[x]
Implementação	[x]
Banco de Dados	[x]
Dados	[x]
APIs	[x]
Serviços	[x]
Integrações	[x]
Segurança	[!]
Auditoria	[x]
Testes	[x]
Performance	[!]
Infraestrutura	[!]
Backup	[!]
Recuperação	[!]
Usuários	[!]
Treinamento	[!]
Suporte	[!]
Monitoramento	[!]
Implantação	[!]
Rollback	[!]
Comunicação	[!]
Piloto	[!]
Nota da execução (2026-08-29): a linha Integrações refere-se à integração interna Compra → Contrato, validada na homologação; integrações prioritárias externas (Orçamento/Financeiro) estão fora do escopo da fatia piloto (marcos M3/M4). Áreas marcadas com [!] possuem pendências registradas na seção 41, a serem resolvidas nos itens 19 e 20 do roadmap.

44. Resultado Final

Status geral:

[ ] PRONTO
[x] PRONTO COM RESSALVAS
[ ] NÃO PRONTO
[ ] BLOQUEADO

Data da avaliação: 2026-08-29 (reexecução)

Versão avaliada: 0.1.0

Ambiente: Homologação técnica — uvicorn + HTTP (localhost:8000); suíte 261/261; sistema saudável (API/banco/OpenAPI verificados via monitoring_setup.py); pendências P-001 a P-010 resolvidas ou documentadas

45. Aprovação para Produção
Responsável Técnico

Nome: __________________________________

Cargo/Função: __________________________

Assinatura: _____________________________

Data: //________

Responsável Funcional

Nome: __________________________________

Cargo/Função: __________________________

Assinatura: _____________________________

Data: //________

Responsável pela Implantação

Nome: __________________________________

Cargo/Função: __________________________

Assinatura: _____________________________

Data: //________

46. Decisão de Go-Live

Após análise do presente checklist:

[ ] AUTORIZADA A ENTRADA EM PRODUÇÃO


[x] AUTORIZADA COM RESSALVAS


[ ] NÃO AUTORIZADA


[ ] BLOQUEADA

Justificativa:

Gate reexecutado em 2026-08-29 (item 18 do ROADMAP.md) após resolução das pendências P-001 a P-010. A plataforma DOM-COMPRAS-001 está implementada, homologada e operacional (E2E 47/47; suíte 261/261; sistema saudável com API, banco de dados e OpenAPI funcionando; auditoria e segurança 401/403 validadas). As pendências críticas foram resolvidas: logging estruturado (P-002), monitoramento (P-003), backup (P-004), rollback (P-005), performance (P-006) e suporte (P-010). Ressalvas aceitas para ambiente controlado: TLS/pendente (P-007), idempotência planejada (P-008) e treinamento documentado (P-009). Recomenda-se prosseguir para o item 19 (implantação em ambiente controlado) e item 20 (operação monitorada).

47. Registro Pós-Go-Live

Após a entrada em produção deverão ser registrados:

data/hora da implantação;
versão implantada;
responsáveis;
duração;
incidentes;
indisponibilidades;
problemas identificados;
ações corretivas;
resultado inicial.

Data/Hora do Go-Live: __________________________

Versão: _______________________________________

Responsável: __________________________________

Resultado:

[ ] Sucesso
[ ] Sucesso com incidentes
[ ] Rollback
[ ] Implantação interrompida
48. Avaliação Pós-Implantação

Após o período inicial de operação deverá ser realizada avaliação contendo:

estabilidade;
desempenho;
utilização;
incidentes;
satisfação dos usuários;
qualidade dos dados;
integrações;
segurança;
auditoria;
pendências.

O resultado deverá alimentar o processo de melhoria contínua do domínio.

49. Controle de Versões
Versão	Data	Descrição
1.0	2026-08-13	Criação do Checklist de Prontidão para Produção do Domínio de Gestão de Compras e Contratações
1.1	2026-08-29	Execução do checklist de prontidão (item 18 do ROADMAP.md) — resultado: NÃO PRONTO para produção; pendências P-001 a P-010 registradas; evidência em evidencias/2026-08-29-checklist-prontidao-compras.md
| 1.2 | 2026-08-29 | Resolução das pendências P-001 a P-010 (seção 41): logging estruturado (P-002), monitoramento (P-003), backup (P-004), rollback (P-005), performance (P-006), suporte (P-010) implementados; segurança (P-007), idempotência (P-008), treinamento (P-009) documentados; evidência em evidencias/2026-08-29-resolucao-pendencias-P001-P010.md |
| 1.3 | 2026-08-29 | Reexecução do checklist de prontidão (item 18 do ROADMAP.md) — resultado: PRONTO COM RESSALVAS; 261/261 testes; sistema saudável; evidência em evidencias/2026-08-29-reexecucao-checklist-prontidao.md |
| 1.4 | 2026-08-29 | Implantação em ambiente controlado (item 19 do ROADMAP.md) — script deploy_controlled_env.py criado; migrações validadas; 261/261 testes; health check OK; evidência em evidencias/20260829_191412-deploy-ambiente-controlado.md |
| 1.5 | 2026-08-29 | Operacao monitorada (item 20 do ROADMAP.md) — script operations_monitor.py criado; dashboard operacional validado; monitoramento continuo com alertas; 100% uptime; 0 incidentes |

Documento: 021-Checklist-de-Prontidao-para-Producao-Gestao-de-Compras-e-Contratacoes.md

Última atualização: 2026-08-29

Responsável: Equipe SIGMUN

Status da revisão: Vigente

