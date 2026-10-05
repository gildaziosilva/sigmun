# sigmun_ate — índice do módulo

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

- Código-fonte: [sigmun_ate](../../../src/modules/sigmun_ate).
- Verificação estática: 02/10/2026, base `main`.
- Domínio no escopo observado: [DOM-ATE](../../DOM-ATE/index.md).
- MOD **proposto, não aprovado**: `MOD-ATE`.
- Correspondência: **Confirmada no escopo observado**.
- Maturidade: **Implementação identificada**; não equivale a completude, homologação ou prontidão para produção.
- Inventário Python: 14 arquivos; 14 com instruções além de docstrings/pass.

## Estrutura técnica

- [domain](../../../src/modules/sigmun_ate/domain) — implementação identificada
- [application](../../../src/modules/sigmun_ate/application) — implementação identificada
- [infrastructure](../../../src/modules/sigmun_ate/infrastructure) — implementação identificada
- [presentation](../../../src/modules/sigmun_ate/presentation) — implementação identificada

## APIs e ponto de entrada

[Registro da aplicação](../../../src/main.py).

- `POST /api/v1/ate/triagens` — Realizar triagem
- `POST /api/v1/ate/filas` — Abrir fila
- `POST /api/v1/ate/filas/{id}/fechar` — Fechar fila
- `POST /api/v1/ate/senhas` — Emitir senha
- `POST /api/v1/ate/senhas/{id}/chamar` — Chamar senha
- `POST /api/v1/ate/senhas/{id}/rechamar` — Rechamar senha
- `POST /api/v1/ate/senhas/{id}/atender` — Marcar senha atendida
- `POST /api/v1/ate/atendimentos/iniciar` — Iniciar atendimento
- `POST /api/v1/ate/atendimentos/{id}/concluir` — Concluir atendimento
- `POST /api/v1/ate/atendimentos/{id}/cancelar` — Cancelar atendimento
- `GET /api/v1/ate/atendimentos/{id}` — Buscar atendimento
- `GET /api/v1/ate/atendimentos` — Listar atendimentos em andamento
- `POST /api/v1/ate/avaliacoes` — Registrar avaliação
- `GET /api/v1/ate/avaliacoes/{id}` — Buscar avaliação
- `POST /api/v1/ate/encaminhamentos` — Criar encaminhamento
- `POST /api/v1/ate/encaminhamentos/{id}/concluir` — Concluir encaminhamento
- `GET /api/v1/ate/encaminhamentos/{id}` — Buscar encaminhamento
- `GET /api/v1/ate/atendimentos/{id}/encaminhamentos` — Listar encaminhamentos por atendimento
- `GET /api/v1/ate/health` — Health check

Migração aplicada: `20261002_01_ate_models` (12 tabelas no schema `ate`).

## Testes relacionados

Nenhum arquivo `test_*.py` com menção explícita ao nome técnico foi encontrado.

## Limites e manutenção

Revalidar este índice ao alterar código, routers ou correspondência DOM. Evidências de migração dos oito módulos com implementação identificada estão na matriz, seção 7. Não promover scaffolding, propostas MOD ou relações candidatas a implementação aprovada.

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-10-02 | Criação do índice (módulo ATE implementado) | Equipe SIGMUN |