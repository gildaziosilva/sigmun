# sigmun_con — índice do módulo

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

- Código-fonte: [sigmun_con](../../../src/modules/sigmun_con).
- Domínio candidato: [DOM-CON — Contabilidade Pública](../../DOM-CON/index.md). Correspondência a validar na matriz 031 (não presumir cobertura integral).
- Identidade MOD: **não definida**; não atribuir por afinidade nominal.
- Maturidade: **Implementação identificada** (endpoints `contabil_endpoints.py` e `execucao_endpoints.py` em `presentation/api/`). Não equivale a completude, homologação ou prontidão para produção.
- Registro em `src/main.py`: **não há `include_router` direto deste módulo** na inspeção atual — verificar se os endpoints são expostos via outro router ou se o registro está pendente.

## Estrutura técnica

- [domain](../../../src/modules/sigmun_con/domain) — ver código-fonte
- [application](../../../src/modules/sigmun_con/application) — ver código-fonte
- [infrastructure](../../../src/modules/sigmun_con/infrastructure) — ver código-fonte
- [presentation](../../../src/modules/sigmun_con/presentation) — ver código-fonte

## APIs e ponto de entrada

[Registro da aplicação](../../../src/main.py).

Verificar o registro dos routers deste módulo em `src/main.py` (inspeção de 2026-10-02 não localizou `include_router` dedicado).

## Limites e manutenção

Revalidar este índice ao alterar código, routers ou correspondência DOM. Não promover scaffolding, propostas MOD ou relações candidatas a implementação aprovada.

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-10-02 | Criação do índice (módulo órfão sem espelho em 05-Modulos; achado F3 da auditoria documental) | Equipe SIGMUN |
