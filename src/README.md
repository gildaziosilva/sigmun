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

> Lista vigente em 2026-10-02 (34 módulos). Detalhes por módulo em
> `SIGMUN-Docs/05-Modulos/index.md` e correspondência DOM ↔ módulo na matriz 031.

| Módulo | Descrição |
|--------|-----------|
| `sigmun_administracao` | Administração |
| `sigmun_agricultura` | Agricultura |
| `sigmun_almoxarifado` | Almoxarifado |
| `sigmun_assistencia_social` | Assistência social |
| `sigmun_cadastro` | Cadastro Único Municipal (DOM-CUM) |
| `sigmun_cadastro_imobiliario` | Cadastro imobiliário (DOM-IMO) |
| `sigmun_compras` | Compras e contratações (DOM-COM) |
| `sigmun_con` | Contabilidade pública — Contábil (DOM-CON) |
| `sigmun_contabilidade` | Contabilidade (scaffold; ver DOM-CON) |
| `sigmun_controladoria` | Controladoria |
| `sigmun_dad` | Dados corporativos (DOM-DAD) |
| `sigmun_dia` | Diárias, viagens e deslocamentos (DOM-DIA) |
| `sigmun_educacao` | Educação |
| `sigmun_financas` | Finanças |
| `sigmun_frotas` | Frota |
| `sigmun_gabinete` | Gabinete |
| `sigmun_gdo` | Gestão documental (DOM-GDO) |
| `sigmun_geoinformacao` | Geoinformação (DOM-GEO) |
| `sigmun_idn` | Identidade e acesso (DOM-IDN) |
| `sigmun_int` | Integração e interoperabilidade (DOM-INT) |
| `sigmun_licitacoes` | Licitações |
| `sigmun_met` | Metadados e taxonomias (DOM-MET) |
| `sigmun_obras` | Obras e engenharia |
| `sigmun_orc` | Orçamento público (DOM-ORC) |
| `sigmun_ouvidoria` | Ouvidoria |
| `sigmun_patrimonio` | Patrimônio |
| `sigmun_planejamento` | Planejamento |
| `sigmun_procuradoria` | Procuradoria |
| `sigmun_rh` | Recursos Humanos |
| `sigmun_saude` | Saúde |
| `sigmun_seg` | Segurança da informação (DOM-SEG) |
| `sigmun_territorial` | Gestão territorial |
| `sigmun_transparencia` | Transparência |
| `sigmun_tributos` | Tributação e arrecadação |

## Referências

- [Arquitetura de Software](SIGMUN-Docs/01-Arquitetura-Corporativa/004-Arquitetura-de-Software.md)
- [Arquitetura de Dados](SIGMUN-Docs/01-Arquitetura-Corporativa/005-Arquitetura-de-Dados.md)
- [Arquitetura de Integração](SIGMUN-Docs/01-Arquitetura-Corporativa/006-Arquitetura-de-Integracao.md)
