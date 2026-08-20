# SIGMUN Source Code

Código fonte do backend do SIGMUN, organizado segundo a **Clean Architecture** e **Domain Driven Design (DDD)**.

## Estrutura

```
src/
├── core/           # SIGMUN Core - serviços corporativos compartilhados
├── shared/         # Componentes compartilhados entre módulos
├── modules/        # Módulos de negócio (Bounded Contexts)
└── main.py         # Ponto de entrada da aplicação
```

## Convenções

Cada módulo segue a estrutura padrão da Clean Architecture:

```
modulo/
├── domain/
│   ├── entities/           # Entidades do domínio
│   ├── value_objects/      # Objetos de valor
│   ├── services/           # Serviços de domínio
│   └── events/             # Eventos de domínio
├── application/
│   ├── commands/           # Comandos (CQRS)
│   ├── queries/            # Queries (CQRS)
│   └── use_cases/          # Casos de uso
├── infrastructure/
│   ├── database/           # Modelos e migrations
│   ├── integrations/       # Integrações externas
│   └── repositories/       # Implementações de repositórios
└── presentation/
    ├── api/                # Rotas e controllers
    └── schemas/            # Schemas (DTOs)
```

## Módulos Disponíveis

| Módulo | Descrição |
|--------|-----------|
| `sigmun_rh` | Recursos Humanos |
| `sigmun_tributos` | Tributação e arrecadação |
| `sigmun_contabilidade` | Contabilidade |
| `sigmun_compras` | Compras e contratações |
| `sigmun_saude` | Saúde |
| `sigmun_educacao` | Educação |
| `sigmun_assistencia_social` | Assistência social |
| `sigmun_almoxarifado` | Almoxarifado |
| `sigmun_patrimonio` | Patrimônio |
| `sigmun_frotas` | Frota |
| `sigmun_obras` | Obras e engenharia |
| `sigmun_licitacoes` | Licitações |
| `sigmun_administracao` | Administração |
| `sigmun_agricultura` | Agricultura |
| `sigmun_controladoria` | Controladoria |
| `sigmun_gabinete` | Gabinete |
| `sigmun_ouvidoria` | Ouvidoria |
| `sigmun_planejamento` | Planejamento |
| `sigmun_procuradoria` | Procuradoria |
| `sigmun_transparencia` | Transparência |
| `sigmun_financas` | Finanças |

## Referências

- [Arquitetura de Software](SIGMUN-Docs/01-Arquitetura-Corporativa/004-Arquitetura-de-Software.md)
- [Arquitetura de Dados](SIGMUN-Docs/01-Arquitetura-Corporativa/005-Arquitetura-de-Dados.md)
- [Arquitetura de Integração](SIGMUN-Docs/01-Arquitetura-Corporativa/006-Arquitetura-de-Integracao.md)
