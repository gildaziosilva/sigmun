# Plano-de-Trabalho.md



**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Governança

**Versão:** 1.1

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

- 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md



---



# Plano Diretor de Execução do SIGMUN



**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal



**Município:** Prefeitura Municipal de Camacan – Bahia



**Versão:** 1.1



**Status Geral:** 🟡 Em Desenvolvimento



---



# 1. Finalidade



Este documento estabelece o Plano Diretor de Execução do SIGMUN.



Sua finalidade é organizar, acompanhar e controlar todas as fases do projeto, permitindo o gerenciamento das entregas, documentos, módulos, requisitos, riscos e evolução da plataforma.



Este documento deverá ser atualizado continuamente durante todo o ciclo de vida do projeto.



---



# 2. Objetivos



O Plano de Trabalho possui os seguintes objetivos:



- organizar o desenvolvimento do SIGMUN;

- controlar o andamento do projeto;

- acompanhar entregas;

- registrar pendências;

- controlar versões;

- acompanhar riscos;

- controlar dependências;

- apoiar a tomada de decisão;

- facilitar auditorias;

- servir como painel executivo do projeto.



---



# 2.1 Classificação das Entregas



Para evitar que a existência de documentos ou pastas seja confundida com software funcional, o acompanhamento do projeto utiliza três categorias distintas:



| Categoria | O que representa | Evidência atual | O que não representa |
|-----------|------------------|-----------------|----------------------|
| **Documentação** | Requisitos, modelos, decisões, planos, diagramas e demais artefatos Markdown que descrevem o produto e suas regras. | 1.078 arquivos Markdown; 891 artefatos documentados nos 33 domínios; 110 RF, 67 casos de uso e 67 histórias no domínio-piloto de Compras. | Não representa código executável, API operacional ou módulo pronto para uso. |
| **Scaffolding** | Estruturas iniciais de código e infraestrutura, incluindo pastas, configurações, endpoints técnicos, pipelines e manifestos. | 21 módulos backend estruturados; endpoints raiz e de saúde; Docker, Kubernetes, Terraform e CI/CD iniciados; 6 arquivos de testes. | Não representa regra de negócio implementada, banco versionado, homologação ou produção. |
| **Implementação real** | Funcionalidade executável com regras de negócio, persistência, API, segurança, auditoria, testes e operação verificadas. | Nenhum módulo de negócio implementado; 0 APIs de negócio; 0 migrações Alembic; 0 homologações. | Não deve ser inferida apenas pela existência de documentação ou scaffolding. |



**Regra de contabilização:** os percentuais de documentação, scaffolding e implementação real devem ser acompanhados separadamente. Um artefato documental concluído ou uma estrutura de código criada não transforma automaticamente a capacidade correspondente em funcionalidade implementada.



---



# 3. Situação Geral



| Item | Situação |

|-------|----------|

| Constituição do Projeto | ✅ Concluída |

| Arquitetura Corporativa | 🟡 Documentação redigida; consolidação final pendente (revisão geral, glossário, diagramas e referências) |

| Modelo de Negócio | ✅ Concluído |

| Requisitos (Framework Corporativo) | ✅ Concluído |

| Domínio-Piloto de Compras (DOM-COMPRAS-001) | 🟡 Documentação concluída (27/27 artefatos); implementação real pendente |

| Modelo de Dados (Corporativo) | 🟢 DDL físico definido e migration `20260820_01_core_compras` aplicada (9 tabelas criadas no PostgreSQL) |

| Desenvolvimento | 🟡 Iniciado (scaffolding da aplicação e dos 21 módulos; sem regras de negócio) |

| Testes | 🟡 Estrutura inicial criada (sem suíte corporativa executável) |

| Implantação | 🟡 Scaffolding iniciado (Docker, Kubernetes, Terraform e CI/CD; sem ambiente homologado) |



---



# 4. Dashboard Executivo



## Situação Geral



| Área | Status | Progresso |

|------|--------|-----------|

| Planejamento | ✅ | 100% |

| Governança | 🟡 | 95% |

| Arquitetura Corporativa | 🟡 | 90% (documentação redigida; consolidação final pendente) |

| Modelo de Negócio | ✅ | 100% |

| Requisitos (Framework Corporativo) | ✅ | 100% documental |

| Domínio-Piloto de Compras (DOM-COMPRAS-001) | 🟡 | 100% documental; 0% implementação real |

| Domínios do SIGMUN (32 domínios corporativos + 1 domínio-piloto = 33 domínios × 27 artefatos = 891 documentos) | ✅ | 100% documental (33 domínios, incl. DOM-DIA); implementação pendente |

| Modelo de Dados (Corporativo) | 🟢 | 25% documental; 100% persistência executável (migration aplicada, 9 tabelas + triggers + índices) |

| Desenvolvimento (scaffolding backend) | 🟡 | 15% scaffolding; 0% implementação real |

| Integrações | ⚪ | 0% |

| LGPD e Segurança | ⚪ | 0% |

| Migração | 🟡 | 1ª revision aplicada (20260820_01_core_compras; 9 tabelas criadas); migração de dados legados pendente |

| UX | ⚪ | 0% |

| Testes | 🟡 | 5% scaffolding; 0% cobertura de regras de negócio |

| Implantação | 🟡 | 5% scaffolding; 0% ambiente homologado |



---



# 5. Indicadores do Projeto



## Progresso Geral



██████████░░░░░░░░░░░░░



**Percentual Geral:** 44%



---



## Indicadores



| Indicador | Valor |

|------------|--------|

| Documentos Markdown inventariados | 1.078 |

| Documentos vigentes ou concluídos | 227 |

| Documentos em elaboração ou não iniciados | 833 |

| Documentos em revisão ou validação | 18 |

| Módulos modelados (domínio-piloto Compras) | 1 |

| Requisitos levantados (RF domínio-piloto Compras) | 110 |

| Casos de uso (domínio-piloto Compras) | 67 |

| Histórias de usuário (domínio-piloto Compras) | 67 |

| APIs definidas | 0 |

| Diagramas produzidos | 0 |

| Protótipos | 0 |



---



# 6. Estrutura Oficial do Projeto



```

SIGMUN/



000-CONSTITUICAO-DO-PROJETO-SIGMUN.md



Plano-de-Trabalho.md



README.md



ROADMAP.md



CHANGELOG.md



DECISOES-ARQUITETURAIS.md



00-Governanca/



01-Arquitetura-Corporativa/



02-Modelo-de-Negocio/



03-Requisitos/



04-Modelo-de-Dados/



05-Modulos/



06-Integracoes/



07-LGPD-e-Seguranca/



08-Migracao/



09-UX/



10-Testes/



11-Implantacao/



96-Sustentabilidade/



97-Estudos-e-Pesquisas/



98-Comunidade-SIGMUN/



99-Anexos/



DOM-COMPRAS-001/ (domínio-piloto)

```



---



# 7. Macrocronograma



| Fase | Status |

|------|--------|

| Planejamento | ✅ |

| Arquitetura Corporativa | 🟡 (documentação redigida; consolidação final pendente) |

| Modelo de Negócio | ✅ |

| Requisitos (Framework Corporativo + Domínio-Piloto Compras) | ✅ |

| Banco de Dados | 🟢 (modelo físico definido; migration `20260820_01_core_compras` criada e aplicada ao PostgreSQL; 9 tabelas em schemas `core` e `compras`) |

| Desenvolvimento | 🟡 |

| Integrações | ⚪ |

| Segurança | ⚪ |

| Migração | ⚪ |

| UX | ⚪ |

| Testes | 🟡 (estrutura inicial) |

| Implantação | 🟡 (scaffolding) |

| Operação | ⚪ |



---



# 8. Fases do Projeto



## Fase 1 — Planejamento



### Objetivo



Definir o escopo institucional do projeto.



### Situação



✅ Concluída



### Entregáveis



- [x] Constituição do Projeto

- [x] Termo de Abertura

- [x] Visão do Projeto

- [x] Objetivos Estratégicos



---



## Fase 2 — Arquitetura Corporativa


### Objetivo


Construir toda a Arquitetura Corporativa do SIGMUN.


### Situação


🟡 Documentação redigida; consolidação final pendente


### Documentos### Documentos



- [x] 004 Princípios de Arquitetura

- [x] 005 Arquitetura de Negócio

- [x] 006 Cadastro Único Municipal

- [x] 007 Modelo de Governança

- [x] 008 Arquitetura de Software

- [x] 009 Arquitetura de Dados

- [x] 010 Arquitetura de Integração

- [x] 011 Arquitetura de Segurança

- [x] 012 Arquitetura de Implantação

- [x] 013 Experiência do Usuário

- [x] 014 Processos e Workflow

- [x] 015 Relatórios e BI

- [x] 016 Gestão Documental

- [x] 017 Gestão de Identidade

- [x] 018 Notificações

- [x] 019 Mobilidade

- [x] 020 DevSecOps

- [x] 021 Governança de Dados

- [x] 022 BI, Analytics e IA

- [x] 023 Governança Corporativa

- [x] 024 Portfólio Digital

- [x] 025 Gestão de Riscos

- [x] 026 Governança da Arquitetura

- [x] 027 Gestão de Configuração

- [x] 028 Ciclo de Vida

- [x] 029 Continuidade Tecnológica

- [x] 030 Gestão da Qualidade

- [x] 031 Inovação

- [x] 032 Gestão do Conhecimento

- [x] 033 Competências

- [x] 034 Gestão da Mudança

- [x] 035 Excelência Operacional

- [x] 036 Sustentabilidade

- [x] 037 Ética, Integridade e Compliance

- [ ] Revisão Geral

- [ ] Glossário Corporativo

- [ ] Diagramas Consolidados

- [ ] Referências Bibliográficas



---



## Fase 3 — Modelo de Negócio



Status: ✅ Concluída



Artefatos concluídos em `02-Modelo-de-Negocio/`: Cadeia de Valor, Mapa de Atores, Mapa de Capacidades, Mapa de Domínios, Mapa de Processos, Mapa de Secretarias, Mapa de Serviços, Modelo de Competências, Modelo de Governança Administrativa e Glossário de Negócio.



---



## Fase 4 — Requisitos



Status: ✅ Concluída (Framework Corporativo) / ✅ Concluída (Domínio-Piloto de Compras)



Artefatos corporativos concluídos em `03-Requisitos/`: Casos de Uso, Critérios de Aceitação, Especificações, Histórias de Usuário, Matriz de Rastreabilidade, Regras de Negócio, Requisitos Funcionais e Requisitos Não Funcionais.



Domínio-piloto `DOM-COMPRAS-001/` concluído com 27 artefatos, incluindo 110 Requisitos Funcionais (RF-COMPRAS-001 a 110), 67 Casos de Uso e 67 Histórias de Usuário, validando ponta a ponta o Framework de Rastreabilidade do SIGMUN.



---



## Fase 5 — Modelo de Dados



Status: 🟡 DDL PostgreSQL definido e primeira revision Alembic criada (`20260820_01_core_compras`); migration aplicada ao PostgreSQL com 9 tabelas criadas (schemas `core` e `compras`), mas migração de dados legados ainda pendente



Observação: o domínio-piloto de Compras já possui `013-Modelo-de-Dados-Gestao-de-Compras-e-Contratacoes.md` concluído, servindo de referência para a modelagem corporativa.



---



## Fase 6 — Desenvolvimento dos Módulos



Status: 🟡 Scaffolding iniciado; implementação real não iniciada



O código-fonte do backend (`src/`) foi estruturado segundo Clean Architecture/DDD, com `src/core` e 21 módulos de negócio (`src/modules/sigmun_*`) possuindo a estrutura de pastas padrão (`domain`, `application`, `infrastructure`, `presentation`). Nenhuma regra de negócio foi implementada ainda. A API expõe apenas os endpoints raiz e de saúde. Testes básicos, CI/CD (`.github/workflows`), Docker, Kubernetes e Terraform foram inicializados como scaffolding.



---



## Fase 7 — Integrações



Status: ⚪ Não iniciada



---



## Fase 8 — LGPD e Segurança



Status: ⚪ Não iniciada



---



## Fase 9 — Migração



Status: 🟡 Primeira revision de schema criada e aplicada no PostgreSQL (9 tabelas); migração de dados legados pendente



---



## Fase 10 — UX



Status: ⚪ Não iniciada



---



## Fase 11 — Testes



Status: 🟡 Scaffolding de testes criado; testes de regras de negócio não implementados



---



## Fase 12 — Implantação



Status: 🟡 Scaffolding de infraestrutura criado; nenhum ambiente homologado ou produtivo



---



# Fase 15 – Inteligência Institucional e Governo Orientado por Dados



Status: ⚪ Não iniciada



Objetivo:



Implantar recursos avançados de Inteligência Analítica para apoio à tomada de decisão da Administração Municipal.



# Tarefas



☐ Implantar Data Warehouse Corporativo



☐ Consolidar todos os indicadores institucionais



☐ Homologar indicadores estratégicos



☐ Implantar Sala de Situação do Prefeito



☐ Desenvolver Observatório Municipal Inteligente



☐ Implantar modelos preditivos



☐ Implantar IA Generativa para apoio à gestão



☐ Implantar monitoramento geoespacial



☐ Integrar indicadores ODS



☐ Implantar análises prescritivas



☐ Publicar Portal Executivo da Gestão Municipal



---



# 13. Controle Detalhado dos Documentos

Esta seção registra todos os documentos Markdown existentes em `SIGMUN-Docs`, com status e versão extraídos dos metadados disponíveis.

| Nº | Documento | Diretório | Status | Versão | Dependências |
|----|-----------|-----------|--------|---------|--------------|
| 001 | 001-Termo-de-Abertura | 00-Governanca/00.1-Estrutura-de-Governanca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 002 | 002-Visao-do-Projeto | 00-Governanca/00.1-Estrutura-de-Governanca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 003 | 003-Objetivos-Estrategicos | 00-Governanca/00.1-Estrutura-de-Governanca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 004 | 004-Modelo-de-Governanca | 00-Governanca/00.1-Estrutura-de-Governanca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 005 | 005-Governanca-Corporativa | 00-Governanca/00.1-Estrutura-de-Governanca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 007 | 007-Gestao-de-Riscos | 00-Governanca/00.1-Estrutura-de-Governanca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 008 | 008-Gestao-do-Portfolio | 00-Governanca/00.1-Estrutura-de-Governanca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 009 | 009-Governanca-da-Arquitetura | 00-Governanca/00.1-Estrutura-de-Governanca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 010 | 010-Etica-Integridade-e-Compliance | 00-Governanca/00.1-Estrutura-de-Governanca | ✅ | 1.0 | Não declaradas |
| 010 | 010-Plano-de-Comunicacao | 00-Governanca/00.2-Governanca-Organizacional | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 011 | 011-Plano-de-Gestao-das-Partes-Interessadas | 00-Governanca/00.2-Governanca-Organizacional | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 012 | 012-Plano-de-Gestao-de-Mudancas | 00-Governanca/00.2-Governanca-Organizacional | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 013 | 013-Plano-de-Governanca-de-Dados | 00-Governanca/00.3-Governanca-da-Informacao | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 014 | 014-Plano-de-Governanca-de-Indicadores | 00-Governanca/00.3-Governanca-da-Informacao | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 015 | 015-Plano-de-Auditoria | 00-Governanca/00.4-Governanca-Institucional | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 016 | 016-Plano-de-Gestao-de-Conformidade | 00-Governanca/00.4-Governanca-Institucional | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 017 | 017-Plano-de-Continuidade-de-Negocios-e-Recuperacao-de-Desastres | 00-Governanca/00.4-Governanca-Institucional | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 018 | 018-Plano-de-Gestao-de-Crises | 00-Governanca/00.4-Governanca-Institucional | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 019 | 019-Plano-de-Comunicacao-Engajamento-e-Colaboracao-da-Comunidade-SIGMUN | 00-Governanca/00.4-Governanca-Institucional | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 020 | 020-Politica-de-Classificacao-da-Informacao-e- Publicacao-de-Artefatos | 00-Governanca/00.4-Governanca-Institucional | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 019 | 019-Politica-de-Governanca-Digital | 00-Governanca/00.5-Politicas-Corporativas | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 020 | 020-Politica-de-Qualidade | 00-Governanca/00.5-Politicas-Corporativas | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 021 | 021-Politica-de-Seguranca | 00-Governanca/00.5-Politicas-Corporativas | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 022 | 022-Politica-de-Gestao-Documental | 00-Governanca/00.5-Politicas-Corporativas | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 023 | 023-Politica-de-Retencao-e-Descarte-de-Documentos | 00-Governanca/00.5-Politicas-Corporativas | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 024 | 024-Politica-de-Gestao-de-Riscos | 00-Governanca/00.5-Politicas-Corporativas | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 025 | 025-Politica-de-Protecao-de-Dados-Pessoais | 00-Governanca/00.5-Politicas-Corporativas | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 026 | 026-Manual-de-Governanca-do-SIGMUN | 00-Governanca/00.5-Politicas-Corporativas | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN | 00-Governanca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | CHANGELOG | 00-Governanca/000B-Base-de-Conhecimento | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | CONVENCOES | 00-Governanca/000B-Base-de-Conhecimento | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | INDEX | 00-Governanca/000B-Base-de-Conhecimento | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | ONTOLOGIA | 00-Governanca/000B-Base-de-Conhecimento | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | README | 00-Governanca/000B-Base-de-Conhecimento | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | SIGLAS | 00-Governanca/000B-Base-de-Conhecimento | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | TAXONOMIA | 00-Governanca/000B-Base-de-Conhecimento | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN | 00-Governanca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | 000C-HIERARQUIA-DOCUMENTAL-v1.0 | 00-Governanca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+18) |
| — | 000D-MODELO-DE-DOCUMENTO | 00-Governanca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | 000E-GUIA-DE-CONTRIBUICAO | 00-Governanca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | 000F-Registro-de-Decisoes-Arquiteturais(ADR-Arqhiteture-Decision-Records) | 00-Governanca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | 000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN | 00-Governanca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | 000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE | 00-Governanca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+23) |
| 0001 | 0001-adopt-apache-2.0-license | 00-Governanca/ADR | 🟡 | A informar | Não declaradas |
| — | ADR-0001-Arquitetura-Modular | 00-Governanca/ADR | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | ADR-0002-Offline-First | 00-Governanca/ADR | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | ADR-0003-APIs-REST | 00-Governanca/ADR | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | ADR-0004-Neutralidade-Tecnologica | 00-Governanca/ADR | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | ADR-0005-Cadastro-Unico-Municipal | 00-Governanca/ADR | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | ADR-INDEX | 00-Governanca/ADR | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | README | 00-Governanca/ADR | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | ADR-TEMPLATE | 00-Governanca/ADR/templates | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 000 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN | Raiz | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 001 | 001-Principios-de-Arquitetura | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 002 | 002-Arquitetura-de-Negocio | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 003 | 003-Cadastro-Unico-Municipal | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 004 | 004-Arquitetura-de-Software | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 005 | 005-Arquitetura-de-Dados | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 006 | 006-Arquitetura-de-Integracao | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 007 | 007-Arquitetura-de-Seguranca | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 008 | 008-Arquitetura-de-Implantacao-e-Infraestrutura | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 009 | 009-Arquitetura-de-Experiencia-do-Usuario-e-Acessibilidade | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 010 | 010-Arquitetura-de-Processos-e-Workflow | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 011 | 011-Arquitetura-de-Relatorios-Indicadores-e-BI | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 012 | 012-Arquitetura-de-Gestao-Documental-e-Arquivistica | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 013 | 013-Arquitetura-de-Identidade-e-Acessos | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 014 | 014-Arquitetura-de-Notificacoes-e-Comunicacao | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 015 | 015-Arquitetura-de-Dispositivos-Moveis-e-Servicos-de-Campo | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 016 | 016-Arquitetura-de-Observabilidade-e-Operacoes-DevSecOps | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 017 | 017-Arquitetura-de-Governaca-de-Dados | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 018 | 018-Arquitetura-de-BI-Analytcs-e-Inteligencia-Artificial | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 019 | 019-Arquitetura-de-Gestao-de-Configuracao-e-versionamento | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 020 | 020-Arquitetura-de-Gestao-do-Ciclo-de-Vida | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 021 | 021-Arquitetura-de-Continuidade-e-Evolucao-Tecnologica | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 022 | 022-Arquitetura-de-Gestao-da-Qualidade-Corporativa | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 023 | 023-Arquitetura-de-Gestao-da-Inovacao-e-Transformacao-Digital | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 024 | 024-Arquitetura-de-Gestao-do-Conhecimento-e-Aprendizagem-Organizacional | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 025 | 025-Arquitetura-de-Gestao-de-Competencias-e-Desenvolvimento-de-Pessoas | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 026 | 026-Arquitetura-de-Gestao-da-Mudanca-Organizacional | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 027 | 027-Arquitetura-de-Excelencia-Operacional-e-Melhoria-Continua | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 028 | 028-Arquitetura-de-Gestao-da-Sustentabilidade-e-Responsabilidade-Socioambiental | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 029 | 029-Arquitetura-do-Observatorio-Municipal-Inteligente | 01-Arquitetura-Corporativa | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 030 | 030-Roadmap-de-Implementacao-dos-Dominios | 01-Arquitetura-Corporativa | ✅ | 1.0 | Não declaradas |
| 000 | 000-CATALOGO-CORPORATIVO-DO-CONHECIMENTO | 01-Arquitetura-Corporativa/04-Conhecimento-Corporativo | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Cadeia-de-Valor-v1.0 | 02-Modelo-de-Negocio | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Cadeia-de-Valor-v1.1 | 02-Modelo-de-Negocio | ✅ | 1.1 – Revisada | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+31) |
| — | Glossario-de-Negocio | 02-Modelo-de-Negocio | ✅ | 1.0 | `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`; `000-CATALOGO-CORPORATIVO-DO-CONHECIMENTO.md` (+10) |
| — | Mapa-de-Atores | 02-Modelo-de-Negocio | ✅ | 1.0 | `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `Cadeia-de-Valor.md`; `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade.md` (+2) |
| — | Mapa-de-Capacidades | 02-Modelo-de-Negocio | ✅ | 1.0 | `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `Cadeia-de-Valor.md`; `Mapa-de-Atores.md` (+3) |
| — | Mapa-de-Dominios | 02-Modelo-de-Negocio | ✅ | 1.0 | `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `Cadeia-de-Valor.md`; `Mapa-de-Atores.md` (+6) |
| — | Mapa-de-Processos | 02-Modelo-de-Negocio | ✅ | 1.0 | `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `Cadeia-de-Valor.md`; `Mapa-de-Atores.md` (+6) |
| — | Mapa-de-Secretarias | 02-Modelo-de-Negocio | ✅ | 1.0 | `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `Cadeia-de-Valor.md`; `Mapa-de-Atores.md` (+6) |
| — | Mapa-de-Servicos | 02-Modelo-de-Negocio | ✅ | 1.0 | `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `Cadeia-de-Valor.md`; `Mapa-de-Atores.md` (+9) |
| — | Modelo-de-Competencias | 02-Modelo-de-Negocio | ✅ | 1.0 | `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `Cadeia-de-Valor.md`; `Mapa-de-Atores.md` (+10) |
| — | Modelo-de-Governanca-Administrativa | 02-Modelo-de-Negocio | ✅ | 1.0 | `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `Cadeia-de-Valor.md`; `Mapa-de-Atores.md` (+21) |
| — | Casos-de-Uso | 03-Requisitos | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; Cadeia-de-Valor.md; Mapa-de-Atores.md (+11) |
| — | Criterios-de-Aceitacao | 03-Requisitos | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000G-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md; Cadeia-de-Valor.md (+11) |
| — | Especificacoes-v1.0 | 03-Requisitos | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+12) |
| — | Historias-de-Usuario-v1.0 | 03-Requisitos | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+17) |
| — | Matriz-de-Rastreabilidade-v1 | 03-Requisitos | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+15) |
| — | Regras-de-Negocio-v1.0 | 03-Requisitos | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+19) |
| — | Requisitos-Funcionais-v1.0 | 03-Requisitos | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+20) |
| — | Requisitos-Nao-Funcionais-v1.0 | 03-Requisitos | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+16) |
| — | Cadastro-Unico | 04-Modelo-de-Dados | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Dicionario-de-dados | 04-Modelo-de-Dados | ✅ | 2.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 005-Arquitetura-de-Dados.md (01-Arquitetura-Corporativa); Modelo-Conceitual.md (+2) |
| — | MER | 04-Modelo-de-Dados | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Modelo-Conceitual | 04-Modelo-de-Dados | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 005-Arquitetura-de-Dados.md; 006-Cadastro-Unico-Municipal.md |
| — | Modelo-Fisico | 04-Modelo-de-Dados | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 005-Arquitetura-de-Dados.md (01-Arquitetura-Corporativa); 006-Cadastro-Unico-Municipal.md (+3) |
| — | Modelo-Logico | 04-Modelo-de-Dados | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 005-Arquitetura-de-Dados.md; 006-Cadastro-Unico-Municipal.md (+1) |
| — | Modelos-SQL | 04-Modelo-de-Dados | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Procedures | 04-Modelo-de-Dados | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Seeds | 04-Modelo-de-Dados | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Views | 04-Modelo-de-Dados | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | APIs | 05-Modulos/modelo | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Banco-de-dados | 05-Modulos/modelo | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Casos-de-Uso | 05-Modulos/modelo | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Documentacao | 05-Modulos/modelo | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Modelo-de-Negocio | 05-Modulos/modelo | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | README | 05-Modulos/modelo | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Requisitos | 05-Modulos/modelo | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Testes | 05-Modulos/modelo | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | UX | 05-Modulos/modelo | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | APIs | 06-Integracoes | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Bancos | 06-Integracoes | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Correios | 06-Integracoes | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | eSocial | 06-Integracoes | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | ESUS | 06-Integracoes | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | GovBR | 06-Integracoes | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Receita | 06-Integracoes | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | SIASUS | 06-Integracoes | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | TCM-BA | 06-Integracoes | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Auditoria | 07-LGPD-e-Seguranca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Backup | 07-LGPD-e-Seguranca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Classificacao | 07-LGPD-e-Seguranca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Continuidade | 07-LGPD-e-Seguranca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Criptografia | 07-LGPD-e-Seguranca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Incidentes | 07-LGPD-e-Seguranca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | LGPD | 07-LGPD-e-Seguranca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Logs | 07-LGPD-e-Seguranca | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | ETL | 08-Migracao | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Firebird | 08-Migracao | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Qualidade | 08-Migracao | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | SQLServer | 08-Migracao | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Validacao | 08-Migracao | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Acessibilidade | 09-UX | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Componentes | 09-UX | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | DesignSystem | 09-UX | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Prototipos | 09-UX | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Wireframes | 09-UX | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Homologacao | 10-Testes | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Integracao | 10-Testes | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Performance | 10-Testes | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Seguranca | 10-Testes | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Unitarios | 10-Testes | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Ambientes | 11-Implantacao | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | CI-CD | 11-Implantacao | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Docker | 11-Implantacao | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Kubernets | 11-Implantacao | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Operacao | 11-Implantacao | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 000 | 000-Modelo-de-Sustentabilidade-do-Ecossistema-SIGMUN | 96-Sustentabilidade | 🟡 | 1.0 | Não declaradas |
| 001 | 001-Plano-de-Captacao-de-Recursos | 96-Sustentabilidade | 🟡 | 1.0 | Não declaradas |
| 002 | 002-Programa-Nacional-de-Colaboradores | 96-Sustentabilidade | 🟡 | 1.0 | Não declaradas |
| 003 | 003-Modelo-de-Bolsas-e-Incentivos | 96-Sustentabilidade | 🟡 | 1.0 | Não declaradas |
| 004 | 004-Programa-de-Municipios-Mantenedores | 96-Sustentabilidade | 🟡 | 1.0 | Não declaradas |
| 005 | 005-Modelo-de-Certificacao-e-Servicos | 96-Sustentabilidade | 🟡 | 1.0 | Não declaradas |
| 006 | 006-Plano-de-Marketing-Institucional | 96-Sustentabilidade | 🟡 | 1.0 | Não declaradas |
| 007 | 007-Modelo-de-Governanca-do-Instituto-SIGMUN | 96-Sustentabilidade | 🟡 | 1.0 | Não declaradas |
| 001 | 001-Estudo-Nacional-da-Transformacao-Digital-dos-Municipios-Brasileiros | 97-Estudos-e-Pesquisas | ⚪ | 1.0 | Não declaradas |
| 002 | 002-Metodologia-de-Coleta-de-Dados | 97-Estudos-e-Pesquisas | ✅ | 1.0 | Não declaradas |
| 003 | 003-Dicionario-de-Dados-da-Pesquisa | 97-Estudos-e-Pesquisas | ✅ | 1.0 | Não declaradas |
| 004 | 004-Plano-de-Coleta-Nacional | 97-Estudos-e-Pesquisas | ✅ | 1.0 | Não declaradas |
| 005 | 005-Modelo-de-Questionario | 97-Estudos-e-Pesquisas | ✅ | 1.0 | Não declaradas |
| 006 | 006-Metodologia-de-Indicadores | 97-Estudos-e-Pesquisas | ✅ | 1.0 | Não declaradas |
| 007 | 007-Framework-Nacional-de-Avaliacao-da-Maturidade-Digital-Municipal | 97-Estudos-e-Pesquisas | 🟡 | 1.0 | Não declaradas |
| 008 | 008-Metodologia-do-INMDM | 97-Estudos-e-Pesquisas | 🟡 | 1.0 | Não declaradas |
| 009 | 009-Metodologia-do-IGDM | 97-Estudos-e-Pesquisas | 🟡 | 1.0 | Não declaradas |
| 010 | 010-Metodologia-do-IDDM | 97-Estudos-e-Pesquisas | 🟡 | 1.0 | Não declaradas |
| 011 | 011-Metodologia-do-ISDM | 97-Estudos-e-Pesquisas | 🟡 | 1.0 | Não declaradas |
| 012 | 012-Modelo-de-Diagnostico-e-Plano-de-Evolucao | 97-Estudos-e-Pesquisas | 🟡 | 1.0 | Não declaradas |
| 013 | 013-Modelo-de-Certificacao-da-Maturidade-Digital-Municipal | 97-Estudos-e-Pesquisas | 🟡 | 1.0 | Não declaradas |
| — | Criar-documentos-da-comunidade | 98-Comunidade-SIGMUN | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | Estrutura-da-Constituicao-SIGMUN | 99-Anexos/Estudos | 🟡 | A informar | Não declaradas |
| — | CHANGELOG | Raiz | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | DECISOES-ARQUITETURAIS | Raiz | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| 000 | 000-Dominio-Analytics-e-Inteligencia | DOM-ANA | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Analytics-e-Inteligencia | DOM-ANA | ⚪ | 1.0 | `000-Dominio-Analytics-e-Inteligencia.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Assistencia-Social | DOM-ASS | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Assistencia-Social | DOM-ASS | ⚪ | 1.0 | `000-Dominio-Assistencia-Social.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Atendimento-ao-Cidadao | DOM-ATE | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Atendimento-ao-Cidadao | DOM-ATE | ⚪ | 1.0 | `000-Dominio-Atendimento-ao-Cidadao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+20) |
| 001 | 001-Mapa-de-Atores-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-Dominio-Gestao-de-Compras-e-Contratacoes.md; 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+7) |
| 002 | 002-Mapa-de-Capacidades-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-Dominio-Gestao-de-Compras-e-Contratacoes.md; 001-Mapa-de-Atores-Gestao-de-Compras-e-Contratacoes.md; 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md (+11) |
| 003 | 003-Mapa-de-Processos-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-Dominio-Gestao-de-Compras-e-Contratacoes.md; 001-Mapa-de-Atores-Gestao-de-Compras-e-Contratacoes.md; 002-Mapa-de-Capacidades-Gestao-de-Compras-e-Contratacoes.md (+12) |
| 004 | 004-Mapa-de-Servicos-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-Dominio-Gestao-de-Compras-e-Contratacoes.md; 001-Mapa-de-Atores-Gestao-de-Compras-e-Contratacoes.md; 002-Mapa-de-Capacidades-Gestao-de-Compras-e-Contratacoes.md (+15) |
| 005 | 005-Casos-de-Uso-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-Dominio-Gestao-de-Compras-e-Contratacoes.md; 001-Mapa-de-Atores-Gestao-de-Compras-e-Contratacoes.md; 002-Mapa-de-Capacidades-Gestao-de-Compras-e-Contratacoes.md (+16) |
| 006 | 006-Historias-de-Usuario-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-Dominio-Gestao-de-Compras-e-Contratacoes.md; 001-Mapa-de-Atores-Gestao-de-Compras-e-Contratacoes.md; 002-Mapa-de-Capacidades-Gestao-de-Compras-e-Contratacoes.md (+17) |
| 007 | 007-Regras-de-Negocio-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-Dominio-Gestao-de-Compras-e-Contratacoes.md; 001-Mapa-de-Atores-Gestao-de-Compras-e-Contratacoes.md; 002-Mapa-de-Capacidades-Gestao-de-Compras-e-Contratacoes.md (+18) |
| 008 | 008-Requisitos-Funcionais-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-Dominio-Gestao-de-Compras-e-Contratacoes.md; 001-Mapa-de-Atores-Gestao-de-Compras-e-Contratacoes.md; 002-Mapa-de-Capacidades-Gestao-de-Compras-e-Contratacoes.md (+19) |
| 009 | 009-Requisitos-Nao-Funcionais-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+19) |
| 010 | 010-Especificacoes-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+21) |
| 011 | 011-Criterios-de-Aceitacao-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+22) |
| 012 | 012-Matriz-de-Rastreabilidade-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | 🟡 | A informar | Não declaradas |
| 013 | 013-Modelo-de-Dados-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+17) |
| 014 | 014-Modelo-de-Integracao-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+24) |
| 015 | 015-Arquitetura-de-Servicos-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+19) |
| 016 | 016-Modelo-de-Seguranca-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+20) |
| 017 | 017-Modelo-de-Auditoria-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+23) |
| 018 | 018-Plano-de-Testes-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+25) |
| 019 | 019-Casos-de-Teste-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000C-HIERARQUIA-DOCUMENTAL.md (+20) |
| 020 | 020-Plano-de-Implantacao-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000C-HIERARQUIA-DOCUMENTAL.md (+21) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000C-HIERARQUIA-DOCUMENTAL.md (+22) |
| 022 | 022-Plano-de-Migracao-de-Dados-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000C-HIERARQUIA-DOCUMENTAL.md (+23) |
| 023 | 023-Plano-de-Treinamento-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000C-HIERARQUIA-DOCUMENTAL.md (+24) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000C-HIERARQUIA-DOCUMENTAL.md (+25) |
| 025 | 025-Estrutura-Tecnica-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+27) |
| 026 | 026-Modelo-de-Dominio-Gestao-de-Compras-e-Contratacoes | DOM-COMPRAS-001 | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000C-HIERARQUIA-DOCUMENTAL.md; 000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md (+18) |
| 000 | 000-Dominio-Contabilidade-Publica | DOM-CON | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Contabilidade-Publica | DOM-CON | ⚪ | 1.0 | `000-Dominio-Contabilidade-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Gestao-de-Competencias | DOM-CPT | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Gestao-de-Competencias | DOM-CPT | ⚪ | 1.0 | `000-Dominio-Gestao-de-Competencias.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Cadastro-Unico-Municipal | DOM-CUM | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Cadastro-Unico-Municipal | DOM-CUM | ⚪ | 1.0 | `000-Dominio-Cadastro-Unico-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Dados-Corporativos | DOM-DAD | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Dados-Corporativos | DOM-DAD | ⚪ | 1.0 | `000-Dominio-Dados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Desenvolvimento-Economico | DOM-DEC | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Desenvolvimento-Economico | DOM-DEC | ⚪ | 1.0 | `000-Dominio-Desenvolvimento-Economico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ✅ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 001 | 001-Mapa-de-Atores-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos | DOM-DIA | ⚪ | 1.0 | `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Educacao-Publica | DOM-EDU | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Educacao-Publica | DOM-EDU | ⚪ | 1.0 | `000-Dominio-Educacao-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Gestao-de-Frota | DOM-FRO | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Gestao-de-Frota | DOM-FRO | ⚪ | 1.0 | `000-Dominio-Gestao-de-Frota.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Gestao-Documental | DOM-GDO | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Gestao-Documental | DOM-GDO | ⚪ | 1.0 | `000-Dominio-Gestao-Documental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Geoinformacao-Municipal | DOM-GEO | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Geoinformacao-Municipal | DOM-GEO | ⚪ | 1.0 | `000-Dominio-Geoinformacao-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Governanca-Municipal | DOM-GOV | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Governanca-Municipal | DOM-GOV | ⚪ | 1.0 | `000-Dominio-Governanca-Municipal.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Identidade-e-Acesso | DOM-IDN | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Identidade-e-Acesso | DOM-IDN | ⚪ | 1.0 | `000-Dominio-Identidade-e-Acesso.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Cadastro-Imobiliario | DOM-IMO | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Cadastro-Imobiliario | DOM-IMO | ⚪ | 1.0 | `000-Dominio-Cadastro-Imobiliario.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Indicadores-e-Desempenho | DOM-IND | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Indicadores-e-Desempenho | DOM-IND | ⚪ | 1.0 | `000-Dominio-Indicadores-e-Desempenho.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Infraestrutura-Tecnologica | DOM-INF | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Infraestrutura-Tecnologica | DOM-INF | ⚪ | 1.0 | `000-Dominio-Infraestrutura-Tecnologica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Integracao-e-Interoperabilidade | DOM-INT | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Integracao-e-Interoperabilidade | DOM-INT | ⚪ | 1.0 | `000-Dominio-Integracao-e-Interoperabilidade.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Meio-Ambiente | DOM-MAM | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Meio-Ambiente | DOM-MAM | ⚪ | 1.0 | `000-Dominio-Meio-Ambiente.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Metadados-Corporativos | DOM-MET | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Metadados-Corporativos | DOM-MET | ⚪ | 1.0 | `000-Dominio-Metadados-Corporativos.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Mobilidade-e-Servicos-de-Campo | DOM-MOB | ⚪ | 1.0 | `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Obras-e-Infraestrutura | DOM-OBR | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Obras-e-Infraestrutura | DOM-OBR | ⚪ | 1.0 | `000-Dominio-Obras-e-Infraestrutura.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Orcamento-Publico | DOM-ORC | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Orcamento-Publico | DOM-ORC | ⚪ | 1.0 | `000-Dominio-Orcamento-Publico.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Ouvidoria | DOM-OUV | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Ouvidoria | DOM-OUV | ⚪ | 1.0 | `000-Dominio-Ouvidoria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Gestao-Patrimonial | DOM-PAT | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Gestao-Patrimonial | DOM-PAT | ⚪ | 1.0 | `000-Dominio-Gestao-Patrimonial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Gestao-de-Pessoas | DOM-PES | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Gestao-de-Pessoas | DOM-PES | ⚪ | 1.0 | `000-Dominio-Gestao-de-Pessoas.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Planejamento-Governamental | DOM-PLA | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Planejamento-Governamental | DOM-PLA | ⚪ | 1.0 | `000-Dominio-Planejamento-Governamental.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Saude-Publica | DOM-SAU | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Saude-Publica | DOM-SAU | ⚪ | 1.0 | `000-Dominio-Saude-Publica.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Seguranca-da-Informacao | DOM-SEG | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Seguranca-da-Informacao | DOM-SEG | ⚪ | 1.0 | `000-Dominio-Seguranca-da-Informacao.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Gestao-Territorial | DOM-TEL | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Gestao-Territorial | DOM-TEL | ⚪ | 1.0 | `000-Dominio-Gestao-Territorial.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 000 | 000-Dominio-Administracao-Tributaria | DOM-TRI | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md; 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md; 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md (+11) |
| 001 | 001-Mapa-de-Atores-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 002 | 002-Mapa-de-Capacidades-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 003 | 003-Mapa-de-Processos-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 004 | 004-Mapa-de-Servicos-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 005 | 005-Casos-de-Uso-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 006 | 006-Historias-de-Usuario-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 007 | 007-Regras-de-Negocio-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 008 | 008-Requisitos-Funcionais-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 009 | 009-Requisitos-Nao-Funcionais-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 010 | 010-Especificacoes-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 011 | 011-Criterios-de-Aceitacao-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 012 | 012-Matriz-de-Rastreabilidade-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 013 | 013-Modelo-de-Dados-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 014 | 014-Modelo-de-Integracao-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 015 | 015-Arquitetura-de-Servicos-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 016 | 016-Modelo-de-Seguranca-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 017 | 017-Modelo-de-Auditoria-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 018 | 018-Plano-de-Testes-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 019 | 019-Casos-de-Teste-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 020 | 020-Plano-de-Implantacao-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 021 | 021-Checklist-de-Prontidao-para-Producao-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 022 | 022-Plano-de-Migracao-de-Dados-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 023 | 023-Plano-de-Treinamento-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 024 | 024-Plano-de-Suporte-e-Operacao-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 025 | 025-Estrutura-Tecnica-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| 026 | 026-Modelo-de-Dominio-Administracao-Tributaria | DOM-TRI | ⚪ | 1.0 | `000-Dominio-Administracao-Tributaria.md`; `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`; `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md` (+4) |
| — | Plano-de-Trabalho | Raiz | ✅ | 1.1 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | REFERENCIAS | Raiz | ✅ | 1.0 | 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md |
| — | ROADMAP | Raiz | ✅ | 1.1 | Não declaradas |

> **Observação:** documentos sem metadado explícito são marcados como `A validar` ou `Não declaradas`; a tabela deve ser regenerada após a criação ou revisão de documentos.

---

# 14. Controle de Entregáveis



| Entregável | Status | Responsável | Observações |

|-------------|--------|-------------|-------------|

| Constituição do Projeto | ✅ | Equipe SIGMUN | |

| Arquitetura Corporativa | 🟡 | Equipe SIGMUN | Documentação redigida; revisão geral, glossário, diagramas e referências pendentes |

| Modelo de Negócio | ✅ | Equipe SIGMUN | |

| Requisitos | ✅ | Equipe SIGMUN | Framework corporativo e domínio-piloto de Compras concluídos |

| Modelo de Dados | 🟡 | Equipe SIGMUN | Modelo conceitual e lógico alinhados; DDL PostgreSQL definido; migrações pendentes |

| Módulos | 🟡 | Equipe SIGMUN | Scaffolding de código-fonte iniciado (sem regras de negócio) |

| Integrações | ⚪ | | |

| Testes | 🟡 | Equipe SIGMUN | Estrutura inicializada; suíte corporativa e cobertura ainda pendentes |

| Implantação | 🟡 | Equipe SIGMUN | Docker, Kubernetes, Terraform e CI/CD inicializados como scaffolding; sem ambiente homologado |



---



# 15. Controle de Dependências



Nenhum documento ou módulo deverá ser iniciado sem que suas dependências mínimas estejam concluídas.



## Exemplo



| Documento | Depende de |

|------------|------------|

| Requisitos | Modelo de Negócio |

| Modelo de Dados | Requisitos |

| Módulos | Modelo de Dados |

| Testes | Módulos |

| Implantação | Testes |



Sempre que houver dúvida, prevalecerá a ordem definida na Constituição do Projeto.



---



# 16. Registro de Decisões Arquiteturais (ADR)



Toda decisão relevante deverá ser registrada.



| Data | ADR | Descrição | Impacto |

|------|-----|-----------|---------|

| | ADR-001 | | |

| | ADR-002 | | |

| | ADR-003 | | |



As decisões detalhadas deverão ser mantidas também no arquivo `DECISOES-ARQUITETURAIS.md`.



---



# 17. Registro de Pendências



## Prioridade Alta



- [x] Finalizar o documento 037 (Ética, Integridade e Compliance).

- [ ] Concluir a revisão geral da Arquitetura Corporativa.

- [ ] Consolidar os diagramas arquiteturais.

- [x] Iniciar o Modelo de Dados Corporativo com base no modelo do domínio-piloto de Compras.

- [ ] Revisar os documentos classificados como em elaboração ou não iniciados (833 documentos segundo o inventário do item 13), concentrados nas áreas ainda não implementadas.



## Prioridade Média



- [ ] Criar o Glossário Corporativo (consolidado).

- [ ] Consolidar referências bibliográficas (`REFERENCIAS.md`).

- [ ] Elaborar catálogo de APIs (`06-Integracoes/APIs.md`).

- [ ] Replicar o modelo do domínio-piloto de Compras (DOM-COMPRAS-001) para os demais domínios/módulos de negócio.

- [ ] Corrigir problemas de codificação (mojibake) identificados em arquivos como `REFERENCIAS.md`, `DECISOES-ARQUITETURAIS.md` e `tests/unit/test_health.py`.



## Prioridade Baixa



- [ ] Revisar nomenclaturas.

- [ ] Revisar padrões de diagramas.

- [ ] Revisar templates.



---



# 18. Registro de Riscos



| ID | Risco | Probabilidade | Impacto | Plano de Resposta | Status |

|----|--------|---------------|----------|-------------------|--------|

| R001 | Mudança de requisitos | Média | Alto | Revisão de escopo | Aberto |

| R002 | Alterações legais | Média | Alto | Atualização documental | Aberto |

| R003 | Complexidade de integrações | Alta | Médio | Planejamento incremental | Aberto |

| R004 | Crescimento do escopo | Alta | Médio | Gestão de Portfólio | Aberto |



---



# 19. Registro de Problemas



| ID | Problema | Solução | Situação |

|----|-----------|----------|----------|

| | | | |



---



# 20. Registro de Melhorias



Sempre registrar oportunidades identificadas durante o projeto.



| ID | Melhoria | Benefício | Prioridade |

|----|-----------|------------|------------|

| | | | |



---



# 21. Indicadores do Projeto



## Documentação



| Indicador | Valor |

|------------|-------|

| Documentos previstos | 1.078 arquivos Markdown existentes |

| Documentos vigentes ou concluídos | 227 |

| Documentos em elaboração ou não iniciados | 833 |

| Documentos em revisão ou validação | 18 |

| Documentos revisados | A consolidar |



---



## Desenvolvimento



| Indicador | Valor |

|------------|-------|

| Módulos previstos | 21 módulos estruturados |

| Módulos implementados | 0 (implementação real) |

| APIs desenvolvidas | 0 APIs de negócio; 2 endpoints técnicos |

| Casos de uso | 67 no domínio-piloto de Compras |

| Requisitos | 110 RF no domínio-piloto de Compras |



---



## Qualidade



| Indicador | Valor |

|------------|-------|

| Testes executados | 0 executados; 2 testes definidos para a API básica |

| Bugs encontrados | A consolidar |

| Bugs corrigidos | A consolidar |

| Cobertura de testes | A medir |



---



# 22. Controle de Versões



| Versão | Data | Alteração |

|---------|------|-----------|

| 1.0 | 2026-08-03 | Criação do documento |

| 1.1 | 2026-08-19 | Atualização geral: reflexo da conclusão do Modelo de Negócio, do Framework Corporativo de Requisitos, do domínio-piloto DOM-COMPRAS-001, do documento 037 (Ética, Integridade e Compliance) e do início do scaffolding de desenvolvimento (`src/`, testes, infraestrutura e CI/CD) |

| 1.2 | 2026-08-19 | Iniciada a Fase 5 — Modelo de Dados (Modelo Conceitual Corporativo) |
| 1.4 | 2026-08-20 | Modelo Físico PostgreSQL definido: ordem de aplicação, DDL, constraints, índices, triggers, views e tratamento LGPD |
| 1.3 | 2026-08-20 | Atualização da linha de base: consolidação arquitetural pendente, 21 módulos em scaffolding, modelo lógico em andamento e roadmap de implementação definido |



---



# 23. Histórico de Marcos do Projeto



| Marco | Data | Situação |

|--------|------|----------|

| Constituição do Projeto | 2026-08-03 | ✅ |

| Arquitetura Corporativa iniciada | 2026-08-03 | ✅ |

| Arquitetura Corporativa redigida | 2026-08-15 | ✅ |

| Arquitetura Corporativa – consolidação final | 2026-08-20 | 🟡 |

| Modelo de Negócio iniciado | 2026-08-03 | ✅ |

| Modelo de Negócio concluído | 2026-08-11 | ✅ |

| Framework Corporativo de Requisitos concluído | 2026-08-11 | ✅ |

| Domínio-Piloto de Compras (DOM-COMPRAS-001) concluído | 2026-08-15 | ✅ |

| Scaffolding do código-fonte iniciado (`src/`, testes, infraestrutura) | 2026-08-17 | ✅ |

| Primeiro módulo implementado | | ⚪ |

| Primeira versão funcional | | |

| Primeira homologação | | |

| Implantação piloto | | |

| Implantação oficial | | |



---



# 24. Critérios para Conclusão de uma Fase



Uma fase somente poderá ser considerada concluída quando:



- todos os documentos obrigatórios estiverem finalizados;

- todos os artefatos previstos estiverem revisados;

- não existirem pendências críticas;

- as dependências da fase seguinte estiverem atendidas;

- houver registro da conclusão neste Plano de Trabalho.



---



# 25. Checklist Geral do Projeto



## Governança



- [x] Constituição do Projeto

- [x] Termo de Abertura

- [x] Visão do Projeto

- [x] Objetivos Estratégicos



## Arquitetura Corporativa



- [x] Documentos 001 a 037 (incluindo Ética, Integridade e Compliance)

- [ ] Revisão Geral

- [ ] Diagramas Consolidados

- [ ] Glossário

- [ ] Referências Bibliográficas



## Modelo de Negócio



- [x] Estrutura (Mapa de Domínios e Mapa de Secretarias)

- [x] Capacidades de Negócio (Mapa de Capacidades)

- [x] Cadeia de Valor

- [x] Serviços (Mapa de Serviços)



## Requisitos



- [x] Funcionais (Framework corporativo + 110 RF do domínio-piloto Compras)

- [x] Não Funcionais (Framework corporativo + domínio-piloto Compras)

- [x] Casos de Uso (Framework corporativo + 67 UC do domínio-piloto Compras)

- [x] Histórias de Usuário (Framework corporativo + 67 HU do domínio-piloto Compras)



## Modelo de Dados



- [x] Modelo Conceitual (corporativo — `04-Modelo-de-Dados/Modelo-Conceitual.md`)

- [ ] Modelo Lógico (corporativo)

- [x] Modelo Físico (corporativo — `04-Modelo-de-Dados/Modelo-Fisico.md`)



## Desenvolvimento



- [ ] Cadastro Único

- [ ] Administração

- [ ] Tributação

- [ ] Saúde

- [ ] Educação

- [ ] Assistência Social

- [ ] Compras (requisitos e domínio concluídos; implementação de código pendente)

- [ ] Patrimônio

- [ ] Recursos Humanos

- [ ] Finanças

- [ ] Demais módulos

- [x] Scaffolding da estrutura de código (Clean Architecture/DDD) para os 21 módulos



## Testes



- [x] Estrutura inicial de testes unitários (`tests/unit/test_health.py`)

- [ ] Unitários (cobertura de regras de negócio)

- [ ] Integração

- [ ] Segurança

- [ ] Performance

- [ ] Homologação



## Implantação



- [x] Scaffolding de ambiente (Docker, Docker Compose, Kubernetes, Terraform, CI/CD)

- [ ] Ambiente (configuração completa)

- [ ] Migração

- [ ] Treinamento

- [ ] Go Live



---



# 26. Próximas Etapas



As próximas etapas deverão seguir obrigatoriamente a sequência definida na Constituição do Projeto. O Modelo de Negócio e o Levantamento de Requisitos (nível corporativo e domínio-piloto de Compras) já foram concluídos; as próximas prioridades são:



1. Conclusão da revisão geral da Arquitetura Corporativa (glossário, diagramas consolidados, referências bibliográficas).

2. Modelagem de Dados Corporativa (Conceitual, Lógico e Físico), com base no modelo já elaborado no domínio-piloto de Compras.

3. Replicação do modelo do domínio-piloto de Compras (DOM-COMPRAS-001) para os demais domínios de negócio.

4. Desenvolvimento dos Módulos (implementação das regras de negócio sobre o scaffolding já existente em `src/`), iniciando pelo módulo de Compras.

5. Integrações (APIs, bancos, GovBR, Receita, eSocial, ESUS, SIASUS, TCM-BA, Correios).

6. LGPD e Segurança.

7. Migração de dados legados (Firebird/SQL Server).

8. Testes (unitários, integração, segurança, performance, homologação).

9. Implantação (ambientes, CI/CD, Docker/Kubernetes).

10. Operação Assistida.

11. Evolução Contínua.



---



# 27. Considerações Finais



O Plano de Trabalho constitui o principal instrumento de acompanhamento da execução do SIGMUN.



Toda alteração relevante no projeto deverá refletir neste documento, garantindo rastreabilidade, transparência, governança e continuidade.



Este documento deverá ser atualizado periodicamente e permanecer alinhado à **000-CONSTITUICAO-DO-PROJETO-SIGMUN.md**, aos documentos da Arquitetura Corporativa e às decisões registradas no projeto.



---



---



**Documento:**Plano-de-Trabalho.md

**Última atualização:** 2026-08-20

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

