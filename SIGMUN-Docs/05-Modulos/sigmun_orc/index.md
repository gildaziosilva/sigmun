# sigmun_orc — índice do módulo

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal
**Domínio:** Módulos de aplicação
**Versão:** 1.0
**Status:** Em elaboração
**Classificação da Informação:** Pública
**Última atualização:** 2026-10-02
**Responsável:** Equipe SIGMUN

| Campo | Conteúdo |
| --- | --- |
| Projeto | SIGMUN |
| Proprietário | Módulos de aplicação |
| Responsável | Equipe SIGMUN |
| Versão | 1.0 |
| Status | Em elaboração; validação editorial pendente |
| Classificação | Pública |
| Data de Criação | 2026-10-02 |
| Última Revisão | 2026-10-02 |
| Próxima Revisão | Ao alterar os documentos ou evidências relacionados |
| Aprovado por | Aprovação não registrada |

**Documento(s) Relacionado(s):** [Documentação geral](../../index.md) · [Catálogo de módulos](../index.md) · [Matriz DOM ↔ módulo](../../01-Arquitetura-Corporativa/031-Matriz-de-Correspondencia-DOM-MOD.md) · [Auditoria documental](../../00-Governanca/AUDITORIA-DOCUMENTAL-2026-09-17.md)

## Identidade e estado observado

- Código-fonte: [sigmun_orc](../../../src/modules/sigmun_orc).
- Domínio candidato: [DOM-ORC](../../DOM-ORC/index.md). Correspondência a validar na matriz 031 (não presumir cobertura integral).
- Identidade MOD: **não definida**; não atribuir por afinidade nominal.
- Maturidade: **Implementação identificada** (endpoints `dotacao_endpoints.py` e `planejamento_endpoints.py` em `presentation/api/`).
- Registro em `src/main.py`: routers registrados via coleção `orc_routers` (`for _orc_router in orc_routers: app.include_router(_orc_router)`), conforme inspeção de 2026-10-02.

## Estrutura técnica

- [domain](../../../src/modules/sigmun_orc/domain) — ver código-fonte
- [application](../../../src/modules/sigmun_orc/application) — ver código-fonte
- [infrastructure](../../../src/modules/sigmun_orc/infrastructure) — ver código-fonte
- [presentation](../../../src/modules/sigmun_orc/presentation) — ver código-fonte

## APIs e ponto de entrada

[Registro da aplicação](../../../src/main.py) — coleção `orc_routers` registrada.

## Limites e manutenção

Revalidar este índice ao alterar código, routers ou correspondência DOM. Não promover scaffolding, propostas MOD ou relações candidatas a implementação aprovada.

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-10-02 | Criação do índice (módulo órfão sem espelho em 05-Modulos; achado F3 da auditoria documental) | Equipe SIGMUN |
