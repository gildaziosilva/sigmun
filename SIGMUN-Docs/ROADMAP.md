# Roadmap de Implementação do SIGMUN

**Projeto:** SIGMUN - Sistema Integrado de Gestão Municipal
**Município:** Prefeitura Municipal de Camacan - Bahia
**Domínio:** Governança
**Versão:** 1.1
**Status:** Vigente
**Última atualização:** 2026-08-20
**Responsável:** Equipe SIGMUN

## 1. Situação de Partida

O SIGMUN possui a documentação corporativa, o modelo de negócio, o framework de requisitos e o domínio-piloto de Compras redigidos. A implementação técnica ainda está no estágio de fundação: o backend tem scaffolding para 21 módulos, a API possui apenas endpoints técnicos, não há migrações de banco e não há frontend efetivo.

O roadmap prioriza uma entrega vertical do `DOM-COMPRAS-001` para validar arquitetura, dados, segurança, APIs, testes e operação antes da expansão para os demais domínios.

## 1.1 Classificação de Maturidade

| Categoria | Definição | Estado atual |
|---|---|---|
| Documentação | Artefatos que especificam, modelam ou governam o produto. | 1.051 arquivos Markdown; documentação do domínio-piloto redigida. |
| Scaffolding | Estruturas iniciais que preparam o desenvolvimento ou a operação. | 21 módulos estruturados, endpoints técnicos, infraestrutura e CI/CD iniciados. |
| Implementação real | Funcionalidade executável com regra de negócio, persistência, segurança, testes e evidência de operação. | 0 módulos de negócio, 0 APIs de negócio, 0 migrações e 0 homologações. |

Documentação concluída não equivale a implementação real. Scaffolding concluído indica preparação técnica, não capacidade operacional disponível.

## 2. Princípios de Execução

1. Validar a fundação antes de expandir módulos.
2. Implementar por fatias verticais, do dado à API e ao teste.
3. Manter rastreabilidade entre requisito, caso de uso, código e teste.
4. Tratar identidade, autorização, auditoria e LGPD como capacidades estruturais.
5. Automatizar qualidade, migrações, documentação e implantação desde o primeiro domínio.
6. Promover um domínio somente quando seus critérios de saída forem comprovados.

## 3. Ondas de Implementação

### Onda 0 - Fundação técnica

**Status:** 🟡 Em andamento
**Objetivo:** tornar o framework executável e repetível.

| Entrega | Situação |
|---|---|
| Estrutura FastAPI e Clean Architecture/DDD | ✅ Scaffolding criado; implementação real ausente |
| Configuração e gestão de ambientes | 🟡 Inicial |
| PostgreSQL, SQLAlchemy e Alembic | 🟡 Dependências configuradas; 0 migrações executáveis |
| CI/CD | 🟡 Scaffolding criado |
| Docker, Kubernetes e Terraform | 🟡 Scaffolding criado |
| Logging e observabilidade | ⚪ Pendente |
| Identidade e autorização | ⚪ Pendente |
| Auditoria técnica | ⚪ Pendente |
| Testes automatizados e quality gates | 🟡 Estrutura criada; 0 testes de regras de negócio executados |

**Critério de saída:** aplicação inicial executando com banco versionado, configuração segura, pipeline de qualidade, logs estruturados e testes automatizados.

### Onda 1 - DOM-COMPRAS-001

**Status:** ⚪ A iniciar após a fundação
**Objetivo:** implementar a primeira capacidade operacional ponta a ponta.

**Sequência recomendada:**

1. Consolidar modelo físico de Compras e entidades compartilhadas.
2. Criar migrações para `core` e `compras`.
3. Implementar fornecedores, compras e itens.
4. Implementar processos documentais e contratos.
5. Expor APIs REST com OpenAPI.
6. Aplicar autorização, auditoria e validações de negócio.
7. Criar testes unitários, integração e contratos de API.
8. Executar homologação com dados de teste e checklist operacional.

**Critério de saída:** código, banco, APIs, regras de negócio, segurança, auditoria, testes, observabilidade, documentação, implantação automatizada e homologação aprovados.

### Onda 2 - Domínios mestres e transversais

**Status:** ⚪ Planejada
**Ordem:** `DOM-CUM` Cadastro Único Municipal, `DOM-IDN` Identidade e Acesso, `DOM-DAD` Governança de Dados, `DOM-GDO` Gestão Documental, `DOM-SEG` Segurança e `DOM-INT` Integrações.

**Dependência:** conclusão da Onda 1 e reutilização dos padrões validados em Compras.

### Onda 3 - Núcleo administrativo e econômico-financeiro

**Status:** ⚪ Planejada
**Domínios:** planejamento, orçamento, contabilidade, tributos, patrimônio, almoxarifado, frotas, controladoria e administração.

**Dependência:** domínios mestres, modelo físico corporativo e integrações definidas.

### Onda 4 - Domínios finalísticos e territoriais

**Status:** ⚪ Planejada
**Domínios:** saúde, educação, assistência social, obras, agricultura, meio ambiente, mobilidade, geoprocessamento e atendimento.

**Dependência:** fundação transversal, segurança, migração e padrões de integração estabilizados.

### Onda 5 - Inteligência, mobilidade e operação ampliada

**Status:** ⚪ Planejada
**Escopo:** indicadores corporativos, observatório municipal, data warehouse, portais, aplicativos móveis, análises preditivas e IA aplicada.

**Dependência:** qualidade e governança de dados comprovadas nos domínios operacionais.

## 4. Próximos Marcos

| Marco | Critério de conclusão | Status |
|---|---|---|
| Consolidação arquitetural | Revisão geral, glossário, diagramas e referências concluídos | 🟡 |
| Modelo físico corporativo | DDL revisado e decisões de índices, auditoria e LGPD registradas | ⚪ |
| Primeira migração | `alembic upgrade head` executa em ambiente limpo | ⚪ |
| Fundação executável | API, banco, testes, quality gates e observabilidade básicos | ⚪ |
| Primeira fatia de Compras | Fornecedor, compra e item disponíveis por API e testes | ⚪ |
| Homologação do piloto | Critérios de aceitação e checklist de prontidão aprovados | ⚪ |
| Expansão transversal | CUM, IDN, DAD, GDO, SEG e INT priorizados com dependências resolvidas | ⚪ |

## 5. Critérios de Priorização

Cada nova entrega será priorizada pela combinação de dependência corporativa, valor operacional, risco, disponibilidade de requisitos e capacidade de reutilização. Nenhum domínio será considerado implementado apenas por possuir documentação ou scaffolding.

## 6. Documentos de Referência

- `SIGMUN-Docs/Plano-de-Trabalho.md`
- `SIGMUN-Docs/01-Arquitetura-Corporativa/030-Roadmap-de-Implementacao-dos-Dominios.md`
- `SIGMUN-Docs/04-Modelo-de-Dados/Modelo-Conceitual.md`
- `SIGMUN-Docs/04-Modelo-de-Dados/Modelo-Logico.md`
- `SIGMUN-Docs/DOM-COMPRAS-001/`

