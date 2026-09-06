# TODO — Master Backlog e Plano de Tarefas do SIGMUN

> **Projeto:** SIGMUN — Sistema Integrado de Gestão Municipal (Camacan-BA)  
> **Status Geral do Projeto:** 🟡 Em Desenvolvimento (Onda 1 Concluída, Onda 2 em Finalização)  
> **Última Atualização:** 2026-09-06  
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
- [ ] **I.2 Corrigir bug de Homologação H-06 no `DOM-GDO`**
  - Local: `src/modules/sigmun_gdo/presentation/api/__init__.py` no endpoint `POST /documentos`.
  - Problema: Código duplicado gera `500 Internal Server Error` em vez de `409 Conflict` sob certas condições de sessão do SQLAlchemy.
  - Ação: Tratar `IntegrityError` com rollback explícito da sessão (`session.rollback()`) e retorno consistente de `HTTPException(409, detail="Código documental já utilizado...")`.
  - Validação: Reexecutar `python scripts/homologacao_gdo.py` e garantir 21/21 verificações aprovadas (`SUCESSO`).
- [ ] **I.3 Ajustar dependências do Python (`pyproject.toml` e `requirements.txt`)**
  - Remover a dependência externa `"uuid>=1.3.0"` (módulo nativo da biblioteca padrão do Python).
  - Adicionar `"email-validator>=2.1.0"` para evitar warnings do Pydantic no startup e validar campos de e-mail.
  - Atualizar ambiente virtual: `pip install email-validator && pip uninstall -y uuid`.
- [ ] **I.4 Corrigir o Docker Compose para subida limpa**
  - Problema: Os serviços `frontend-portal-cidadao` e `frontend-portal-fornecedor` quebram o build do Compose por não possuírem `package.json` nem `nginx.conf`.
  - Ação: Criar arquivos mínimos de scaffolding nos dois portais ou comentar temporariamente os dois targets no `docker-compose.yml` até o início do seu ciclo de desenvolvimento.

---

## Fase II — Qualidade de Código, CI/CD & Quality Gates

Prioridade: **Alta** (Desbloqueia a pipeline de CI)

- [ ] **II.1 Saneamento das 359 violações do linter (Ruff)**
  - Executar autofix: `.venv/bin/ruff check --fix src/ tests/`.
  - Executar formatação: `.venv/bin/ruff format src/ tests/`.
  - Corrigir manualmente violações restantes:
    - Quebras de linha longas (>100 caracteres) em `tests/unit/test_gdo_use_cases.py`.
    - Múltiplos statements em uma linha (dois pontos) em testes de exceção com `pytest.raises`.
    - Organização e ordenação de imports com `I001`.
  - Validar: `make lint` saindo com código 0.
- [ ] **II.2 Resolução dos 144 erros de tipagem estática (Mypy)**
  - Adicionar anotações de retorno nos handlers de ciclo de vida (`startup_event -> None`, `shutdown_event -> None` em `src/main.py`).
  - Adicionar anotações em funções auxiliares e middlewares (`src/shared/middleware/correlation_id_middleware.py`).
  - Tipar explicitamente as injeções de dependência (`Depends`) e schemas de retorno nos routers de apresentação:
    - `sigmun_dad/presentation/api/__init__.py`
    - `sigmun_met/presentation/api/__init__.py`
    - `sigmun_gdo/presentation/api/__init__.py`
    - `sigmun_idn/presentation/api/__init__.py`
    - `sigmun_cadastro/infrastructure/repositories/`
  - Validar: `make type-check` saindo com código 0.
- [ ] **II.3 Validação ponta a ponta da Pipeline de CI Local e Remota**
  - Executar localmente todos os alvos do Makefile: `make lint`, `make type-check`, `make test`.
  - Garantir que a suíte de testes de integração (`make test-integration`) execute com sucesso com o PostgreSQL na porta 5433.

---

## Fase III — Conclusão, Homologação e Fechamento de DOM-GDO (Onda 2)

Prioridade: **Alta**

- [ ] **III.1 Executar e aprovar Homologação E2E de GDO**
  - Executar `python scripts/homologacao_gdo.py`.
  - Confirmar geração da evidência `SIGMUN-Docs/DOM-GDO/evidencias/YYYY-MM-DD-homologacao-gdo.md` com status `SUCESSO`.
- [ ] **III.2 Executar testes de carga em GDO**
  - Executar `python scripts/test_carga_gdo.py` e registrar evidências de throughput e tempo de resposta.
- [ ] **III.3 Concluir os 6 artefatos finais de GDO em `SIGMUN-Docs/DOM-GDO/`**
  - `021-Checklist-de-Prontidao-para-Producao-Gestao-Documental.md`: Preencher com as evidências de teste e aprovação.
  - `022-Plano-de-Migracao-de-Dados-Gestao-Documental.md`: Definir estratégia de carga de legado.
  - `023-Plano-de-Treinamento-Gestao-Documental.md`: Roteiro para operadores de protocolo e arquivo.
  - `024-Plano-de-Suporte-e-Operacao-Gestao-Documental.md`: Procedimentos de sustentação.
  - `025-Estrutura-Tecnica-Gestao-Documental.md`: Arquitetura física detalhada.
  - `026-Termo-de-Encerramento-do-Dominio-Gestao-Documental.md`: Formalização de entrega.
- [ ] **III.4 Atualizar `SIGMUN-Docs/ToDo.md` e `ROADMAP.md`**
  - Marcar todos os ciclos de GDO como concluídos em `SIGMUN-Docs/ToDo.md`.
  - Atualizar `ROADMAP.md` com o status final 🟢 de `DOM-GDO`.

---

## Fase IV — Sincronização Documental da Onda 2 (CUM, IDN, DAD, MET)

Prioridade: **Média/Alta** (Sanar a dívida de governança onde o código existe mas a documentação permaneceu em template)

- [ ] **IV.1 Promover artefatos do `DOM-CUM` (Cadastro Único Municipal)**
  - Atualizar `SIGMUN-Docs/DOM-CUM/001` a `026` para refletir as entidades implementadas (Pessoa, DadosFisicos, DadosJuridicos, Endereco, Documento, Contato, UnidadeAdministrativa) e suas 15 use cases.
  - Marcar artefatos com `**Status:** Vigente`.
- [ ] **IV.2 Promover artefatos do `DOM-IDN` (Identidade e Acesso)**
  - Atualizar `SIGMUN-Docs/DOM-IDN/001` a `026` com base no módulo `sigmun_idn` (Usuario, Role, Permissao, Sessao, AuditoriaLogin, fluxos JWT).
  - Marcar artefatos com `**Status:** Vigente`.
- [ ] **IV.3 Promover artefatos do `DOM-DAD` (Dados Corporativos)**
  - Atualizar `SIGMUN-Docs/DOM-DAD/001` a `026` com base nas entidades implementadas (Ativos, Catalogos, Linhagens, Politicas, Qualidade) e seus 26 use cases.
  - Marcar artefatos com `**Status:** Vigente`.
- [ ] **IV.4 Promover artefatos do `DOM-MET` (Metadados Corporativos)**
  - Atualizar `SIGMUN-Docs/DOM-MET/001` a `026` com base nas entidades implementadas (Metadados, Valores, Classificacoes, Taxonomias, Termos) e seus 22 use cases.
  - Marcar artefatos com `**Status:** Vigente`.
- [ ] **IV.5 Atualizar a Tabela do Plano de Trabalho e o README raiz**
  - Executar: `python scripts/atualizar_tabela_plano.py`.
  - Atualizar o `README.md` da raiz para listar os módulos CUM, IDN, DAD, MET e GDO na árvore de módulos e na descrição de capacidades.

---

## Fase V — Implementação dos Domínios Restantes da Onda 2 (DOM-SEG e DOM-INT)

Prioridade: **Alta** (Conclusão formal da Onda 2)

- [ ] **V.1 `DOM-SEG` — Segurança da Informação (Ordem 7)**
  - [ ] Consolidar artefatos documentais `SIGMUN-Docs/DOM-SEG/000` a `026`.
  - [ ] Criar módulo `src/modules/sigmun_seg/` seguindo o padrão Clean Architecture/DDD.
  - [ ] Modelar agregados: Controles de Segurança, Políticas de Segurança, Gestão de Incidentes, Chaves Criptográficas e Credenciais.
  - [ ] Implementar repositórios SQLAlchemy e migração Alembic para o schema `seg`.
  - [ ] Implementar APIs REST `/api/v1/seg` e integrar ao `src/main.py`.
  - [ ] Criar suíte de testes unitários (≥ 30 testes) e de integração.
- [ ] **V.2 `DOM-INT` — Integração e Interoperabilidade (Ordem 8)**
  - [ ] Consolidar artefatos documentais `SIGMUN-Docs/DOM-INT/000` a `026`.
  - [ ] Criar módulo `src/modules/sigmun_int/`.
  - [ ] Implementar barramento de eventos interno (Event Bus) consumindo o Transactional Outbox de GDO e Compras.
  - [ ] Implementar catálogo de APIs externas e webhooks com controle de retry e dead-letter queue.
  - [ ] Implementar conectores oficiais (GOV.BR, e-Social, SIAFIC, PNCP).
  - [ ] Migração Alembic para schema `integracao`.
  - [ ] Testes unitários e de integração.
- [ ] **V.3 `DOM-GOV` e `DOM-IND` (Governança e Indicadores Municipais - Ordens 9 e 10)**
  - [ ] Especificar e implementar painéis de conformidade, atos normativos e KPIs estratégicos.

---

## Fase VI — Fundação e Evolução do Frontend

Prioridade: **Média**

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

