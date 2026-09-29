# DOM-IMO — Cadastro Imobiliário

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal
**Domínio:** DOM-IMO
**Versão:** 2.0
**Status:** Vigente
**Classificação da Informação:** Pública
**Última atualização:** 2026-09-29
**Responsável:** Equipe SIGMUN

| Campo | Conteúdo |
| --- | --- |
| Projeto | SIGMUN |
| Proprietário | DOM-IMO |
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

Referência de negócio: [000-Dominio-Cadastro-Imobiliario.md](000-Dominio-Cadastro-Imobiliario.md). Este índice organiza os documentos existentes; não declara todas as capacidades do domínio implementadas.

## Correspondência com módulos

| Domínio | Módulo de aplicação | MOD | Maturidade técnica | Correspondência |
| --- | --- | --- | --- | --- |
| [DOM-IMO](../../05-Modulos/sigmun_cadastro_imobiliario/index.md) | [sigmun_cadastro_imobiliario](../../../src/modules/sigmun_cadastro_imobiliario/) | `MOD-IMO` | Implementada e validada | Confirmada |

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
| [000-Dominio-Cadastro-Imobiliario.md](000-Dominio-Cadastro-Imobiliario.md) | Vigente |
| [001-Mapa-de-Atores-Cadastro-Imobiliario.md](001-Mapa-de-Atores-Cadastro-Imobiliario.md) | Vigente |
| [002-Mapa-de-Capacidades-Cadastro-Imobiliario.md](002-Mapa-de-Capacidades-Cadastro-Imobiliario.md) | Vigente |
| [003-Mapa-de-Processos-Cadastro-Imobiliario.md](003-Mapa-de-Processos-Cadastro-Imobiliario.md) | Vigente |
| [004-Mapa-de-Servicos-Cadastro-Imobiliario.md](004-Mapa-de-Servicos-Cadastro-Imobiliario.md) | Vigente |
| [005-Casos-de-Uso-Cadastro-Imobiliario.md](005-Casos-de-Uso-Cadastro-Imobiliario.md) | Vigente |
| [006-Historias-de-Usuario-Cadastro-Imobiliario.md](006-Historias-de-Usuario-Cadastro-Imobiliario.md) | Vigente |
| [007-Regras-de-Negocio-Cadastro-Imobiliario.md](007-Regras-de-Negocio-Cadastro-Imobiliario.md) | Vigente |
| [008-Requisitos-Funcionais-Cadastro-Imobiliario.md](008-Requisitos-Funcionais-Cadastro-Imobiliario.md) | Vigente |
| [009-Requisitos-Nao-Funcionais-Cadastro-Imobiliario.md](009-Requisitos-Nao-Funcionais-Cadastro-Imobiliario.md) | Vigente |
| [010-Especificacoes-Cadastro-Imobiliario.md](010-Especificacoes-Cadastro-Imobiliario.md) | Vigente |
| [011-Criterios-de-Aceitacao-Cadastro-Imobiliario.md](011-Criterios-de-Aceitacao-Cadastro-Imobiliario.md) | Vigente |
| [012-Matriz-de-Rastreabilidade-Cadastro-Imobiliario.md](012-Matriz-de-Rastreabilidade-Cadastro-Imobiliario.md) | Vigente |
| [013-Modelo-de-Dados-Cadastro-Imobiliario.md](013-Modelo-de-Dados-Cadastro-Imobiliario.md) | Vigente |
| [014-Modelo-de-Integracao-Cadastro-Imobiliario.md](014-Modelo-de-Integracao-Cadastro-Imobiliario.md) | Vigente |
| [015-Arquitetura-de-Servicos-Cadastro-Imobiliario.md](015-Arquitetura-de-Servicos-Cadastro-Imobiliario.md) | Vigente |
| [016-Modelo-de-Seguranca-Cadastro-Imobiliario.md](016-Modelo-de-Seguranca-Cadastro-Imobiliario.md) | Vigente |
| [017-Modelo-de-Auditoria-Cadastro-Imobiliario.md](017-Modelo-de-Auditoria-Cadastro-Imobiliario.md) | Vigente |
| [018-Plano-de-Testes-Cadastro-Imobiliario.md](018-Plano-de-Testes-Cadastro-Imobiliario.md) | Vigente |
| [019-Casos-de-Teste-Cadastro-Imobiliario.md](019-Casos-de-Teste-Cadastro-Imobiliario.md) | Vigente |
| [020-Plano-de-Implantacao-Cadastro-Imobiliario.md](020-Plano-de-Implantacao-Cadastro-Imobiliario.md) | Vigente |
| [021-Checklist-de-Prontidao-para-Producao-Cadastro-Imobiliario.md](021-Checklist-de-Prontidao-para-Producao-Cadastro-Imobiliario.md) | Vigente |
| [022-Plano-de-Migracao-de-Dados-Cadastro-Imobiliario.md](022-Plano-de-Migracao-de-Dados-Cadastro-Imobiliario.md) | Vigente |
| [023-Plano-de-Treinamento-Cadastro-Imobiliario.md](023-Plano-de-Treinamento-Cadastro-Imobiliario.md) | Vigente |
| [024-Plano-de-Suporte-e-Operacao-Cadastro-Imobiliario.md](024-Plano-de-Suporte-e-Operacao-Cadastro-Imobiliario.md) | Vigente |
| [025-Estrutura-Tecnica-Cadastro-Imobiliario.md](025-Estrutura-Tecnica-Cadastro-Imobiliario.md) | Vigente |
| [026-Modelo-de-Dominio-Cadastro-Imobiliario.md](026-Modelo-de-Dominio-Cadastro-Imobiliario.md) | Vigente |

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-09-17 | Criação do inventário e navegação; aprovação não presumida | Equipe SIGMUN |
