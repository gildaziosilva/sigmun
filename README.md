# SIGMUN — Sistema Integrado de Gestão Municipal

> Plataforma ERP Público para integração, gestão, governança e transformação digital da administração municipal da Prefeitura Municipal de Camacan-BA.

## Sobre o Projeto

O **SIGMUN** é um sistema integrado de gestão municipal desenvolvido com uma arquitetura **Modular Monolith + Clean Architecture + Domain Driven Design (DDD)**, utilizando Python e FastAPI no backend.

A plataforma visa integrar processos, dados e serviços de todas as secretarias e órgãos municipais, substituindo sistemas isolados, planilhas e controles paralelos.

## Arquitetura

A arquitetura do SIGMUN segue os princípios definidos em `SIGMUN-Docs/01-Arquitetura-Corporativa/004-Arquitetura-de-Software.md`:

- **Modular Monolith** — separação clara de domínios com evolução futura para microsserviços
- **Clean Architecture** — separação entre regras de negócio, aplicação, infraestrutura e apresentação
- **DDD** — cada módulo é um Bounded Context com suas próprias entidades, serviços e eventos

### Estrutura de Diretórios

```
sigmun-v1/
├── src/                          # Código fonte
│   ├── core/                     # SIGMUN Core (serviços compartilhados)
│   ├── shared/                   # Componentes compartilhados
│   ├── modules/                  # Módulos de negócio (Bounded Contexts)
│   │   ├── sigmun_rh/
│   │   ├── sigmun_tributos/
│   │   ├── sigmun_contabilidade/
│   │   ├── sigmun_compras/
│   │   ├── sigmun_saude/
│   │   ├── sigmun_educacao/
│   │   ├── sigmun_assistencia_social/
│   │   ├── sigmun_almoxarifado/
│   │   ├── sigmun_patrimonio/
│   │   ├── sigmun_frotas/
│   │   ├── sigmun_obras/
│   │   ├── sigmun_licitacoes/
│   │   ├── sigmun_administracao/
│   │   ├── sigmun_agricultura/
│   │   ├── sigmun_controladoria/
│   │   ├── sigmun_gabinete/
│   │   ├── sigmun_ouvidoria/
│   │   ├── sigmun_planejamento/
│   │   ├── sigmun_procuradoria/
│   │   ├── sigmun_transparencia/
│   │   └── sigmun_financas/
│   └── main.py                   # Ponto de entrada da aplicação
├── frontend/                     # Aplicações frontend
│   ├── admin/                    # Aplicação administrativa
│   ├── portal-cidadao/           # Portal do cidadão
│   └── portal-fornecedor/        # Portal do fornecedor
├── mobile/                       # Aplicativos móveis
│   ├── cidadao/
│   ├── fiscalizacao/
│   ├── saude/
│   └── equipes-externas/
├── infra/                        # Infraestrutura como código
│   ├── docker/                   # Dockerfiles e configurações
│   ├── terraform/                # Infraestrutura AWS
│   └── kubernetes/               # Manifestos Kubernetes
├── tests/                        # Testes automatizados
│   ├── unit/                     # Testes unitários
│   ├── integration/              # Testes de integração
│   └── e2e/                      # Testes end-to-end
├── .github/                      # CI/CD (GitHub Actions)
├── scripts/                      # Scripts de automação
├── docs/                         # Documentação técnica
├── SIGMUN-Docs/                  # Documentação corporativa do projeto
├── alembic/                      # Migrações de banco de dados
├── docker-compose.yml            # Orquestração local
├── pyproject.toml                # Configuração do projeto Python
├── requirements.txt              # Dependências de produção
├── requirements-dev.txt          # Dependências de desenvolvimento
├── Makefile                      # Comandos de automação
└── .env.example                  # Template de variáveis de ambiente
```

## Tecnologias

- **Backend:** Python 3.10+, FastAPI, SQLAlchemy, Pydantic, Alembic
- **Banco de Dados:** PostgreSQL
- **Cache/Filas:** Redis, Celery
- **Frontend:** React/Vue (responsivo e acessível)
- **Mobile:** React Native
- **Infraestrutura:** Docker, Docker Compose, Kubernetes, AWS
- **CI/CD:** GitHub Actions

## Como Começar

1. Clone o repositório
2. Copie `.env.example` para `.env` e ajuste as variáveis
3. Instale as dependências: `pip install -r requirements-dev.txt`
4. Inicie os containers: `docker-compose up -d`
5. Execute as migrações: `alembic upgrade head`
6. Inicie a aplicação: `make run-dev`

## Documentação

- **Documentação corporativa:** `SIGMUN-Docs/`
- **Guia de contribuição:** `SIGMUN-Docs/00-Governanca/000E-GUIA-DE-CONTRIBUICAO.md`
- **Plano de trabalho:** `SIGMUN-Docs/Plano-de-Trabalho.md`
- **Roadmap:** `SIGMUN-Docs/ROADMAP.md`

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
