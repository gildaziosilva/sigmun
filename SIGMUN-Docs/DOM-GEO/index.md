# DOM-GEO — Geoinformação Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal
**Domínio:** DOM-GEO
**Versão:** 2.0
**Status:** Vigente
**Classificação da Informação:** Pública
**Última atualização:** 2026-09-29
**Responsável:** Equipe SIGMUN

| Campo | Conteúdo |
| --- | --- |
| Projeto | SIGMUN |
| Proprietário | DOM-GEO |
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

Referência de negócio: [000-Dominio-Geoinformacao-Municipal.md](000-Dominio-Geoinformacao-Municipal.md). Este índice organiza os documentos existentes; não declara todas as capacidades do domínio implementadas.

## Correspondência com módulos

| Domínio | Módulo de aplicação | MOD | Maturidade técnica | Correspondência |
| --- | --- | --- | --- | --- |
| [DOM-GEO](../05-Modulos/sigmun_geoinformacao/index.md) | [sigmun_geoinformacao](../../../src/modules/sigmun_geoinformacao/) | `MOD-GEO` | Implementada e validada | Confirmada (2026-09-29) |

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
| [000-Dominio-Geoinformacao-Municipal.md](000-Dominio-Geoinformacao-Municipal.md) | Vigente |
| [001-Mapa-de-Atores-Geoinformacao-Municipal.md](001-Mapa-de-Atores-Geoinformacao-Municipal.md) | Vigente |
| [002-Mapa-de-Capacidades-Geoinformacao-Municipal.md](002-Mapa-de-Capacidades-Geoinformacao-Municipal.md) | Vigente |
| [003-Mapa-de-Processos-Geoinformacao-Municipal.md](003-Mapa-de-Processos-Geoinformacao-Municipal.md) | Vigente |
| [004-Mapa-de-Servicos-Geoinformacao-Municipal.md](004-Mapa-de-Servicos-Geoinformacao-Municipal.md) | Vigente |
| [005-Casos-de-Uso-Geoinformacao-Municipal.md](005-Casos-de-Uso-Geoinformacao-Municipal.md) | Vigente |
| [006-Historias-de-Usuario-Geoinformacao-Municipal.md](006-Historias-de-Usuario-Geoinformacao-Municipal.md) | Vigente |
| [007-Regras-de-Negocio-Geoinformacao-Municipal.md](007-Regras-de-Negocio-Geoinformacao-Municipal.md) | Vigente |
| [008-Requisitos-Funcionais-Geoinformacao-Municipal.md](008-Requisitos-Funcionais-Geoinformacao-Municipal.md) | Vigente |
| [009-Requisitos-Nao-Funcionais-Geoinformacao-Municipal.md](009-Requisitos-Nao-Funcionais-Geoinformacao-Municipal.md) | Vigente |
| [010-Especificacoes-Geoinformacao-Municipal.md](010-Especificacoes-Geoinformacao-Municipal.md) | Vigente |
| [011-Criterios-de-Aceitacao-Geoinformacao-Municipal.md](011-Criterios-de-Aceitacao-Geoinformacao-Municipal.md) | Vigente |
| [012-Matriz-de-Rastreabilidade-Geoinformacao-Municipal.md](012-Matriz-de-Rastreabilidade-Geoinformacao-Municipal.md) | Vigente |
| [013-Modelo-de-Dados-Geoinformacao-Municipal.md](013-Modelo-de-Dados-Geoinformacao-Municipal.md) | Vigente |
| [014-Modelo-de-Integracao-Geoinformacao-Municipal.md](014-Modelo-de-Integracao-Geoinformacao-Municipal.md) | Vigente |
| [015-Arquitetura-de-Servicos-Geoinformacao-Municipal.md](015-Arquitetura-de-Servicos-Geoinformacao-Municipal.md) | Vigente |
| [016-Modelo-de-Seguranca-Geoinformacao-Municipal.md](016-Modelo-de-Seguranca-Geoinformacao-Municipal.md) | Vigente |
| [017-Modelo-de-Auditoria-Geoinformacao-Municipal.md](017-Modelo-de-Auditoria-Geoinformacao-Municipal.md) | Vigente |
| [018-Plano-de-Testes-Geoinformacao-Municipal.md](018-Plano-de-Testes-Geoinformacao-Municipal.md) | Vigente |
| [019-Casos-de-Teste-Geoinformacao-Municipal.md](019-Casos-de-Teste-Geoinformacao-Municipal.md) | Vigente |
| [020-Plano-de-Implantacao-Geoinformacao-Municipal.md](020-Plano-de-Implantacao-Geoinformacao-Municipal.md) | Vigente |
| [021-Checklist-de-Prontidao-para-Producao-Geoinformacao-Municipal.md](021-Checklist-de-Prontidao-para-Producao-Geoinformacao-Municipal.md) | Vigente |
| [022-Plano-de-Migracao-de-Dados-Geoinformacao-Municipal.md](022-Plano-de-Migracao-de-Dados-Geoinformacao-Municipal.md) | Vigente |
| [023-Plano-de-Treinamento-Geoinformacao-Municipal.md](023-Plano-de-Treinamento-Geoinformacao-Municipal.md) | Vigente |
| [024-Plano-de-Suporte-e-Operacao-Geoinformacao-Municipal.md](024-Plano-de-Suporte-e-Operacao-Geoinformacao-Municipal.md) | Vigente |
| [025-Estrutura-Tecnica-Geoinformacao-Municipal.md](025-Estrutura-Tecnica-Geoinformacao-Municipal.md) | Vigente |
| [026-Modelo-de-Dominio-Geoinformacao-Municipal.md](026-Modelo-de-Dominio-Geoinformacao-Municipal.md) | Vigente |

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-09-17 | Criação do inventário e navegação; aprovação não presumida | Equipe SIGMUN |
| 2.0 | 2026-09-29 | Artefatos `001`-`026` detalhados a partir da implementação; correspondência `MOD` promovida a confirmada | Equipe SIGMUN |
