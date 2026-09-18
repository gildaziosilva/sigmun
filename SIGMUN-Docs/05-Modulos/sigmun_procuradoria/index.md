# sigmun_procuradoria — índice do módulo

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal
**Domínio:** Módulos de aplicação
**Versão:** 1.0
**Status:** Em elaboração
**Classificação da Informação:** Pública
**Última atualização:** 2026-09-17
**Responsável:** Equipe SIGMUN

| Campo | Conteúdo |
| --- | --- |
| Projeto | SIGMUN |
| Proprietário | Módulos de aplicação |
| Responsável | Equipe SIGMUN |
| Versão | 1.0 |
| Status | Em elaboração; validação editorial pendente |
| Classificação | Pública |
| Data de Criação | 17/09/2026 |
| Última Revisão | 17/09/2026 |
| Próxima Revisão | Ao alterar os documentos ou evidências relacionados |
| Aprovado por | Aprovação não registrada |

**Documento(s) Relacionado(s):** [Documentação geral](../../index.md) · [Catálogo de módulos](../index.md) · [Matriz DOM ↔ módulo](../../01-Arquitetura-Corporativa/031-Matriz-de-Correspondencia-DOM-MOD.md) · [Auditoria documental](../../00-Governanca/AUDITORIA-DOCUMENTAL-2026-09-17.md)

## Identidade e estado observado

- Código-fonte: [sigmun_procuradoria](../../../src/modules/sigmun_procuradoria).
- Verificação estática: 17/09/2026, base `51c82dc`.
- Domínio: **correspondência não determinada**.
- Identidade MOD: **não definida**; não atribuir por afinidade nominal.
- Maturidade: **Preparado**. Os 13 arquivos Python inspecionados contêm apenas scaffolding, sem implementação identificada além de docstrings/pass. Nenhum router deste módulo está registrado em `src/main.py`.
- Inventário Python: 13 arquivos; 0 com instruções além de docstrings/pass. Contagem não é medida de cobertura funcional.

## Estrutura técnica

- [domain](../../../src/modules/sigmun_procuradoria/domain) — estrutura preparada
- [application](../../../src/modules/sigmun_procuradoria/application) — estrutura preparada
- [infrastructure](../../../src/modules/sigmun_procuradoria/infrastructure) — estrutura preparada
- [presentation](../../../src/modules/sigmun_procuradoria/presentation) — estrutura preparada

## APIs e ponto de entrada

[Registro da aplicação](../../../src/main.py).

Sem router registrado para este módulo na inspeção.

## Testes relacionados

Nenhum arquivo `test_*.py` com menção explícita ao nome técnico foi encontrado. Essa busca não exclui testes indiretos ou compartilhados.

## Limites e manutenção

Revalidar este índice ao alterar código, routers ou correspondência DOM. Evidências de migração dos oito módulos com implementação identificada estão na matriz, seção 7. Não promover scaffolding, propostas MOD ou relações candidatas a implementação aprovada.

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-09-17 | Criação do inventário e navegação; aprovação não presumida | Equipe SIGMUN |
