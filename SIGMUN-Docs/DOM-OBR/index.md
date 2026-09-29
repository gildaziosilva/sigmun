# DOM-OBR — Obras e Infraestrutura

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal
**Domínio:** DOM-OBR
**Versão:** 2.0
**Status:** Vigente
**Classificação da Informação:** Pública
**Última atualização:** 2026-09-29
**Responsável:** Equipe SIGMUN

| Campo | Conteúdo |
| --- | --- |
| Projeto | SIGMUN |
| Proprietário | DOM-OBR |
| Responsável | Equipe SIGMUN |
| Versão | 2.0 |
| Status | Vigente; artefatos `001`-`026` detalhados a partir da implementação |
| Classificação | Pública |
| Data de Criação | 17/09/2026 |
| Última Revisão | 29/09/2026 |
| Próxima Revisão | Ao alterar os documentos ou evidências relacionados |
| Aprovado por | Aprovação não registrada |

**Documento(s) Relacionado(s):** [Documentação geral](../index.md) · [Catálogo de módulos](../05-Modulos/index.md) · [Matriz DOM ↔ módulo](../01-Arquitetura-Corporativa/031-Matriz-de-Correspondencia-DOM-MOD.md) · [Auditoria documental](../00-Governanca/AUDITORIA-DOCUMENTAL-2026-09-17.md)

## Identidade e escopo

Referência de negócio: [000-Dominio-Obras-e-Infraestrutura.md](000-Dominio-Obras-e-Infraestrutura.md). Este índice organiza os documentos existentes; não declara todas as capacidades do domínio implementadas.

## Correspondência com módulos

| Domínio | Módulo de aplicação | MOD | Maturidade técnica | Correspondência |
| --- | --- | --- | --- | --- |
| [DOM-OBR](../05-Modulos/sigmun_obras/index.md) | [sigmun_obras](../../../src/modules/sigmun_obras/) | `MOD-OBR` | Implementada e validada | Confirmada (2026-09-29) |

## Correspondência confirmada

A correspondência foi registrada em 2026-09-29 com a entrega do módulo e
**promovida a confirmada** nesta data, após a conciliação dos artefatos
`001`–`026` com o escopo implementado. A evidência é verificável por
`python scripts/gerar_artefatos_territoriais.py --verificar`, que reconstrói
os artefatos dos quatro domínios territoriais a partir do OpenAPI, dos modelos
ORM, dos casos de uso e dos testes. A promoção cobre o **vínculo de ownership e
escopo documental** e não atesta prontidão para produção: permanecem as
pendências de segurança PB-01 a PB-04 do artefato 021.

## Documentos do domínio

Os status abaixo refletem o estado em 2026-09-29. Os artefatos `001`–`026` são
gerados por `scripts/gerar_artefatos_territoriais.py` a partir da implementação
verificada e podem ser reverificados com
`python scripts/gerar_artefatos_territoriais.py --verificar`.

| Documento | Status declarado / observação |
| --- | --- |
| [000-Dominio-Obras-e-Infraestrutura.md](000-Dominio-Obras-e-Infraestrutura.md) | Vigente |
| [001-Mapa-de-Atores-Obras-e-Infraestrutura.md](001-Mapa-de-Atores-Obras-e-Infraestrutura.md) | Vigente |
| [002-Mapa-de-Capacidades-Obras-e-Infraestrutura.md](002-Mapa-de-Capacidades-Obras-e-Infraestrutura.md) | Vigente |
| [003-Mapa-de-Processos-Obras-e-Infraestrutura.md](003-Mapa-de-Processos-Obras-e-Infraestrutura.md) | Vigente |
| [004-Mapa-de-Servicos-Obras-e-Infraestrutura.md](004-Mapa-de-Servicos-Obras-e-Infraestrutura.md) | Vigente |
| [005-Casos-de-Uso-Obras-e-Infraestrutura.md](005-Casos-de-Uso-Obras-e-Infraestrutura.md) | Vigente |
| [006-Historias-de-Usuario-Obras-e-Infraestrutura.md](006-Historias-de-Usuario-Obras-e-Infraestrutura.md) | Vigente |
| [007-Regras-de-Negocio-Obras-e-Infraestrutura.md](007-Regras-de-Negocio-Obras-e-Infraestrutura.md) | Vigente |
| [008-Requisitos-Funcionais-Obras-e-Infraestrutura.md](008-Requisitos-Funcionais-Obras-e-Infraestrutura.md) | Vigente |
| [009-Requisitos-Nao-Funcionais-Obras-e-Infraestrutura.md](009-Requisitos-Nao-Funcionais-Obras-e-Infraestrutura.md) | Vigente |
| [010-Especificacoes-Obras-e-Infraestrutura.md](010-Especificacoes-Obras-e-Infraestrutura.md) | Vigente |
| [011-Criterios-de-Aceitacao-Obras-e-Infraestrutura.md](011-Criterios-de-Aceitacao-Obras-e-Infraestrutura.md) | Vigente |
| [012-Matriz-de-Rastreabilidade-Obras-e-Infraestrutura.md](012-Matriz-de-Rastreabilidade-Obras-e-Infraestrutura.md) | Vigente |
| [013-Modelo-de-Dados-Obras-e-Infraestrutura.md](013-Modelo-de-Dados-Obras-e-Infraestrutura.md) | Vigente |
| [014-Modelo-de-Integracao-Obras-e-Infraestrutura.md](014-Modelo-de-Integracao-Obras-e-Infraestrutura.md) | Vigente |
| [015-Arquitetura-de-Servicos-Obras-e-Infraestrutura.md](015-Arquitetura-de-Servicos-Obras-e-Infraestrutura.md) | Vigente |
| [016-Modelo-de-Seguranca-Obras-e-Infraestrutura.md](016-Modelo-de-Seguranca-Obras-e-Infraestrutura.md) | Vigente |
| [017-Modelo-de-Auditoria-Obras-e-Infraestrutura.md](017-Modelo-de-Auditoria-Obras-e-Infraestrutura.md) | Vigente |
| [018-Plano-de-Testes-Obras-e-Infraestrutura.md](018-Plano-de-Testes-Obras-e-Infraestrutura.md) | Vigente |
| [019-Casos-de-Teste-Obras-e-Infraestrutura.md](019-Casos-de-Teste-Obras-e-Infraestrutura.md) | Vigente |
| [020-Plano-de-Implantacao-Obras-e-Infraestrutura.md](020-Plano-de-Implantacao-Obras-e-Infraestrutura.md) | Vigente |
| [021-Checklist-de-Prontidao-para-Producao-Obras-e-Infraestrutura.md](021-Checklist-de-Prontidao-para-Producao-Obras-e-Infraestrutura.md) | Vigente |
| [022-Plano-de-Migracao-de-Dados-Obras-e-Infraestrutura.md](022-Plano-de-Migracao-de-Dados-Obras-e-Infraestrutura.md) | Vigente |
| [023-Plano-de-Treinamento-Obras-e-Infraestrutura.md](023-Plano-de-Treinamento-Obras-e-Infraestrutura.md) | Vigente |
| [024-Plano-de-Suporte-e-Operacao-Obras-e-Infraestrutura.md](024-Plano-de-Suporte-e-Operacao-Obras-e-Infraestrutura.md) | Vigente |
| [025-Estrutura-Tecnica-Obras-e-Infraestrutura.md](025-Estrutura-Tecnica-Obras-e-Infraestrutura.md) | Vigente |
| [026-Modelo-de-Dominio-Obras-e-Infraestrutura.md](026-Modelo-de-Dominio-Obras-e-Infraestrutura.md) | Vigente |

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-09-17 | Criação do inventário e navegação; aprovação não presumida | Equipe SIGMUN |
| 2.0 | 2026-09-29 | Artefatos `001`-`026` detalhados a partir da implementação; correspondência `MOD` promovida a confirmada | Equipe SIGMUN |
