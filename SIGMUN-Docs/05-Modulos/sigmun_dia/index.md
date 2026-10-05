# sigmun_dia — índice do módulo

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

- Código-fonte: [sigmun_dia](../../../src/modules/sigmun_dia).
- Domínio candidato: [DOM-DIA](../../DOM-DIA/index.md). Correspondência a validar na matriz 031 (não presumir cobertura integral).
- Identidade MOD: **não definida**; não atribuir por afinidade nominal.
- Maturidade: **Implementação identificada** (28 arquivos `.py`; `router` registrado como `dia_router` em `src/main.py`).
- Registro em `src/main.py`: `app.include_router(dia_router)` presente na inspeção de 2026-10-02.

## Estrutura técnica

- [domain](../../../src/modules/sigmun_dia/domain) — ver código-fonte
- [application](../../../src/modules/sigmun_dia/application) — ver código-fonte
- [infrastructure](../../../src/modules/sigmun_dia/infrastructure) — ver código-fonte
- [presentation](../../../src/modules/sigmun_dia/presentation) — ver código-fonte

## APIs e ponto de entrada

[Registro da aplicação](../../../src/main.py) — `dia_router` registrado.

## Limites e manutenção

Revalidar este índice ao alterar código, routers ou correspondência DOM. Não promover scaffolding, propostas MOD ou relações candidatas a implementação aprovada.

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-10-02 | Criação do índice (módulo órfão sem espelho em 05-Modulos; achado F3 da auditoria documental) | Equipe SIGMUN |
