
# Roadmap de Implementação do SIGMUN

**Projeto:** SIGMUN - Sistema Integrado de Gestão Municipal

**Município:** Prefeitura Municipal de Camacan - Bahia

**Domínio:** Governança

**Versão:** 1.2

**Status:** Vigente

**Última atualização:** 2026-08-24

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
| Implementação real | Funcionalidade executável com regra de negócio, persistência, segurança, testes e evidência de operação. | DOM-COMPRAS-001 em preparação para implementação; demais domínios ainda não implementados. |

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
| PostgreSQL | 🟢 Migration `20260820_01` aplicada (schemas `core` e `compras`) |
| SQLAlchemy | 🟡 Em preparação |
| Alembic | 🟢 Estrutura configurada; migration aplicada |
| Migrações | 🟢 Migration `20260820_01_core_compras` criada e aplicada (9 tabelas, triggers, índices) |
| CI/CD | 🟡 Scaffolding criado |
| Docker | 🟡 Scaffolding criado |
| Kubernetes | 🟡 Scaffolding/documentação |
| Terraform | 🟡 Scaffolding/documentação |
| Logging estruturado | ⚪ Pendente |
| Observabilidade | ⚪ Pendente |
| Identidade e autorização | ⚪ Pendente |
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

**Status:** 🟡 Em andamento (solicitações e processos de compras implementados; próxima etapa: processos documentais)

**Objetivo:** implementar a primeira capacidade operacional ponta a ponta do SIGMUN.

O `DOM-COMPRAS-001` será o domínio-piloto utilizado para validar o padrão de construção dos demais domínios.

## 4.1 Sequência recomendada

1. Consolidar modelo de domínio de Compras.
2. Consolidar modelo físico de Compras e entidades compartilhadas.
3. ✅ Criar migrações para `core` e `compras` (migration `20260820_01` criada e aplicada).
4. ✅ Implementar fornecedores (entidade, casos de uso, repositório SQLAlchemy, APIs REST e testes).
5. ✅ Implementar itens e produtos/serviços (entidade ItemCompra sobre `compras.itens_compras`, casos de uso, repositório SQLAlchemy e APIs REST).
6. ✅ Implementar solicitações e processos de compras (entidade Compra com máquina de estados processual sobre `compras.compras`, casos de uso, repositório SQLAlchemy e APIs REST; Requisição/Demanda – ENT-COMPRAS-001 – aguarda evolução do modelo físico).
7. ➡️ Implementar processos documentais. (PRÓXIMA TAREFA)
8. Implementar contratos.
9. Implementar integrações necessárias.
10. Expor APIs REST com OpenAPI.
11. Aplicar autorização.
12. Implementar auditoria.
13. Implementar validações de negócio.
14. Criar testes unitários.
15. Criar testes de integração.
16. Criar testes de contratos de API.
17. Executar homologação.
18. Executar checklist de prontidão.
19. Implantar em ambiente controlado.
20. Iniciar operação monitorada.

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

**Status:** ⚪ Planejada

**Objetivo:** implementar os domínios que fornecem dados, identidade, serviços e capacidades corporativas reutilizáveis.

## 5.1 Domínios

### `DOM-CUM` — Cadastro Único Municipal

Responsável pelos cadastros corporativos compartilhados.

### `DOM-IDN` — Identidade e Acesso

Responsável por:

- identidade;
- autenticação;
- autorização;
- perfis;
- papéis;
- permissões;
- acesso institucional.

### `DOM-DAD` — Dados Corporativos

Responsável por:

- governança de dados;
- qualidade;
- catálogo;
- linhagem;
- políticas;
- compartilhamento;
- gestão dos ativos de dados.

### `DOM-MET` — Metadados Corporativos

Responsável por:

- metadados;
- classificações;
- taxonomias;
- referências semânticas;
- padrões corporativos.

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
Expansão transversal	CUM, IDN, DAD, MET, GDO, SEG, INT, GOV e IND priorizados	⚪
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