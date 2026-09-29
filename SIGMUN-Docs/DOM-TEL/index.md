# DOM-TEL — Gestão Territorial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal
**Domínio:** DOM-TEL
**Versão:** 2.0
**Status:** Vigente
**Classificação da Informação:** Pública
**Última atualização:** 2026-09-29
**Responsável:** Equipe SIGMUN

| Campo | Conteúdo |
| --- | --- |
| Projeto | SIGMUN |
| Proprietário | DOM-TEL |
| Responsável | Equipe SIGMUN |
| Versão | 2.0 |
| Status | Vigente; artefatos `001`-`026` detalhados a partir da implementação |
| Classificação | Pública |
| Data de Criação | 17/09/2026 |
| Última Revisão | 2026-09-29 |
| Próxima Revisão | Ao alterar os documentos ou evidências relacionados |
| Aprovado por | Aprovação não registrada |

**Documento(s) Relacionado(s):** [Documentação geral](../index.md) · [Catálogo de módulos](../05-Modulos/index.md) · [Matriz DOM ↔ módulo](../01-Arquitetura-Corporativa/031-Matriz-de-Correspondencia-DOM-MOD.md) · [Auditoria documental](../00-Governanca/AUDITORIA-DOCUMENTAL-2026-09-17.md)

## Identidade e escopo

Referência de negócio: [000-Dominio-Gestao-Territorial.md](000-Dominio-Gestao-Territorial.md). Este índice organiza os documentos existentes; não declara todas as capacidades do domínio implementadas.

## Correspondência com módulos

| Domínio | Módulo de aplicação | MOD | Maturidade técnica | Correspondência |
| --- | --- | --- | --- | --- |
| [DOM-TEL](../../05-Modulos/sigmun_territorial/index.md) | [sigmun_territorial](../../../src/modules/sigmun_territorial/) | `MOD-TEL` | Implementada e validada | Confirmada |

A correspondência foi registrada em 2026-09-29 com a entrega da Fase IX.2 do
`TODO.md` e **promovida a confirmada** em 2026-09-29, após a conciliação dos
artefatos `001`–`026` com o módulo implementado. A evidência que sustenta a
promoção é verificável por `scripts/gerar_artefatos_territoriais.py --verificar`,
que reconstrói os 52 artefatos a partir do OpenAPI, dos modelos ORM, dos casos
de uso e dos testes.

## Documentos do domínio

Os status abaixo refletem o estado em 2026-09-29. Os artefatos `001`–`026` são
gerados por `scripts/gerar_artefatos_territoriais.py` a partir da implementação
verificada (OpenAPI, modelos ORM, casos de uso e testes) e podem ser
reverificados com `python scripts/gerar_artefatos_territoriais.py --verificar`.
O alerta de numeração, blocos e status do relatório de auditoria permanece
registrado na versão 1.0.

| Documento | Status declarado / observação |
| --- | --- |
| [000-Dominio-Gestao-Territorial.md](000-Dominio-Gestao-Territorial.md) | Vigente |
| [001-Mapa-de-Atores-Gestao-Territorial.md](001-Mapa-de-Atores-Gestao-Territorial.md) | Vigente |
| [002-Mapa-de-Capacidades-Gestao-Territorial.md](002-Mapa-de-Capacidades-Gestao-Territorial.md) | Vigente |
| [003-Mapa-de-Processos-Gestao-Territorial.md](003-Mapa-de-Processos-Gestao-Territorial.md) | Vigente |
| [004-Mapa-de-Servicos-Gestao-Territorial.md](004-Mapa-de-Servicos-Gestao-Territorial.md) | Vigente |
| [005-Casos-de-Uso-Gestao-Territorial.md](005-Casos-de-Uso-Gestao-Territorial.md) | Vigente |
| [006-Historias-de-Usuario-Gestao-Territorial.md](006-Historias-de-Usuario-Gestao-Territorial.md) | Vigente |
| [007-Regras-de-Negocio-Gestao-Territorial.md](007-Regras-de-Negocio-Gestao-Territorial.md) | Vigente |
| [008-Requisitos-Funcionais-Gestao-Territorial.md](008-Requisitos-Funcionais-Gestao-Territorial.md) | Vigente |
| [009-Requisitos-Nao-Funcionais-Gestao-Territorial.md](009-Requisitos-Nao-Funcionais-Gestao-Territorial.md) | Vigente |
| [010-Especificacoes-Gestao-Territorial.md](010-Especificacoes-Gestao-Territorial.md) | Vigente |
| [011-Criterios-de-Aceitacao-Gestao-Territorial.md](011-Criterios-de-Aceitacao-Gestao-Territorial.md) | Vigente |
| [012-Matriz-de-Rastreabilidade-Gestao-Territorial.md](012-Matriz-de-Rastreabilidade-Gestao-Territorial.md) | Vigente |
| [013-Modelo-de-Dados-Gestao-Territorial.md](013-Modelo-de-Dados-Gestao-Territorial.md) | Vigente |
| [014-Modelo-de-Integracao-Gestao-Territorial.md](014-Modelo-de-Integracao-Gestao-Territorial.md) | Vigente |
| [015-Arquitetura-de-Servicos-Gestao-Territorial.md](015-Arquitetura-de-Servicos-Gestao-Territorial.md) | Vigente |
| [016-Modelo-de-Seguranca-Gestao-Territorial.md](016-Modelo-de-Seguranca-Gestao-Territorial.md) | Vigente |
| [017-Modelo-de-Auditoria-Gestao-Territorial.md](017-Modelo-de-Auditoria-Gestao-Territorial.md) | Vigente |
| [018-Plano-de-Testes-Gestao-Territorial.md](018-Plano-de-Testes-Gestao-Territorial.md) | Vigente |
| [019-Casos-de-Teste-Gestao-Territorial.md](019-Casos-de-Teste-Gestao-Territorial.md) | Vigente |
| [020-Plano-de-Implantacao-Gestao-Territorial.md](020-Plano-de-Implantacao-Gestao-Territorial.md) | Vigente |
| [021-Checklist-de-Prontidao-para-Producao-Gestao-Territorial.md](021-Checklist-de-Prontidao-para-Producao-Gestao-Territorial.md) | Vigente |
| [022-Plano-de-Migracao-de-Dados-Gestao-Territorial.md](022-Plano-de-Migracao-de-Dados-Gestao-Territorial.md) | Vigente |
| [023-Plano-de-Treinamento-Gestao-Territorial.md](023-Plano-de-Treinamento-Gestao-Territorial.md) | Vigente |
| [024-Plano-de-Suporte-e-Operacao-Gestao-Territorial.md](024-Plano-de-Suporte-e-Operacao-Gestao-Territorial.md) | Vigente |
| [025-Estrutura-Tecnica-Gestao-Territorial.md](025-Estrutura-Tecnica-Gestao-Territorial.md) | Vigente |
| [026-Modelo-de-Dominio-Gestao-Territorial.md](026-Modelo-de-Dominio-Gestao-Territorial.md) | Vigente |

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-09-17 | Criação do inventário e navegação; aprovação não presumida | Equipe SIGMUN |
