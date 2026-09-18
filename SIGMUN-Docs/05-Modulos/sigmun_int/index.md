# sigmun_int — índice do módulo

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

- Código-fonte: [sigmun_int](../../../src/modules/sigmun_int).
- Verificação estática: 17/09/2026, base `51c82dc`.
- Domínio no escopo observado: [DOM-INT](../../DOM-INT/index.md).
- MOD **proposto, não aprovado**: `MOD-INT`.
- Correspondência: **Confirmada no escopo observado**.
- Maturidade: **Implementação identificada**; não equivale a completude, homologação ou prontidão para produção.
- Inventário Python: 36 arquivos; 31 com instruções além de docstrings/pass. Contagem não é medida de cobertura funcional.

> Referências a DOM-SEG nos modelos/repositórios descrevem adoção de padrão, não dependência direta comprovada. Consulte a matriz, seção 8.1.

## Estrutura técnica

- [domain](../../../src/modules/sigmun_int/domain) — implementação identificada
- [application](../../../src/modules/sigmun_int/application) — implementação identificada
- [infrastructure](../../../src/modules/sigmun_int/infrastructure) — implementação identificada
- [presentation](../../../src/modules/sigmun_int/presentation) — implementação identificada

## APIs e ponto de entrada

[Registro da aplicação](../../../src/main.py).

- [src/modules/sigmun_int/presentation/api/__init__.py](../../../src/modules/sigmun_int/presentation/api/__init__.py) — registro em `src/main.py`, linha 226 na base inspecionada.

## Inventário de implementação

Arquivos com instruções além de docstrings/pass. A listagem aponta artefatos; não transforma cada arquivo em capacidade completa.

### domain

- [domain/entities/__init__.py](../../../src/modules/sigmun_int/domain/entities/__init__.py)
- [domain/events/__init__.py](../../../src/modules/sigmun_int/domain/events/__init__.py)
- [domain/exceptions.py](../../../src/modules/sigmun_int/domain/exceptions.py)
- [domain/value_objects/__init__.py](../../../src/modules/sigmun_int/domain/value_objects/__init__.py)

### application

- [application/interfaces/__init__.py](../../../src/modules/sigmun_int/application/interfaces/__init__.py)
- [application/use_cases/__init__.py](../../../src/modules/sigmun_int/application/use_cases/__init__.py)
- [application/use_cases/api_use_cases.py](../../../src/modules/sigmun_int/application/use_cases/api_use_cases.py)
- [application/use_cases/bus_use_cases.py](../../../src/modules/sigmun_int/application/use_cases/bus_use_cases.py)
- [application/use_cases/conector_use_cases.py](../../../src/modules/sigmun_int/application/use_cases/conector_use_cases.py)
- [application/use_cases/contrato_use_cases.py](../../../src/modules/sigmun_int/application/use_cases/contrato_use_cases.py)
- [application/use_cases/entrega_use_cases.py](../../../src/modules/sigmun_int/application/use_cases/entrega_use_cases.py)
- [application/use_cases/webhook_use_cases.py](../../../src/modules/sigmun_int/application/use_cases/webhook_use_cases.py)

### infrastructure

- [infrastructure/database/models.py](../../../src/modules/sigmun_int/infrastructure/database/models.py)
- [infrastructure/database/seeds.py](../../../src/modules/sigmun_int/infrastructure/database/seeds.py)
- [infrastructure/messaging/__init__.py](../../../src/modules/sigmun_int/infrastructure/messaging/__init__.py)
- [infrastructure/messaging/despachador_webhooks.py](../../../src/modules/sigmun_int/infrastructure/messaging/despachador_webhooks.py)
- [infrastructure/messaging/outbox_source.py](../../../src/modules/sigmun_int/infrastructure/messaging/outbox_source.py)
- [infrastructure/repositories/__init__.py](../../../src/modules/sigmun_int/infrastructure/repositories/__init__.py)
- [infrastructure/repositories/sqlalchemy_api_externa_repository.py](../../../src/modules/sigmun_int/infrastructure/repositories/sqlalchemy_api_externa_repository.py)
- [infrastructure/repositories/sqlalchemy_conector_repository.py](../../../src/modules/sigmun_int/infrastructure/repositories/sqlalchemy_conector_repository.py)
- [infrastructure/repositories/sqlalchemy_contrato_repository.py](../../../src/modules/sigmun_int/infrastructure/repositories/sqlalchemy_contrato_repository.py)
- [infrastructure/repositories/sqlalchemy_entrega_repository.py](../../../src/modules/sigmun_int/infrastructure/repositories/sqlalchemy_entrega_repository.py)
- [infrastructure/repositories/sqlalchemy_evento_processado_repository.py](../../../src/modules/sigmun_int/infrastructure/repositories/sqlalchemy_evento_processado_repository.py)
- [infrastructure/repositories/sqlalchemy_webhook_repository.py](../../../src/modules/sigmun_int/infrastructure/repositories/sqlalchemy_webhook_repository.py)

### presentation

- [presentation/api/__init__.py](../../../src/modules/sigmun_int/presentation/api/__init__.py)
- [presentation/schemas/__init__.py](../../../src/modules/sigmun_int/presentation/schemas/__init__.py)
- [presentation/schemas/api_schemas.py](../../../src/modules/sigmun_int/presentation/schemas/api_schemas.py)
- [presentation/schemas/conector_schemas.py](../../../src/modules/sigmun_int/presentation/schemas/conector_schemas.py)
- [presentation/schemas/contrato_schemas.py](../../../src/modules/sigmun_int/presentation/schemas/contrato_schemas.py)
- [presentation/schemas/entrega_schemas.py](../../../src/modules/sigmun_int/presentation/schemas/entrega_schemas.py)
- [presentation/schemas/webhook_schemas.py](../../../src/modules/sigmun_int/presentation/schemas/webhook_schemas.py)

## Testes relacionados

Arquivos que mencionam explicitamente o nome técnico do módulo. Não executados nesta auditoria documental.

- [tests/integration/test_dom_int_sqlalchemy_repositories.py](../../../tests/integration/test_dom_int_sqlalchemy_repositories.py)
- [tests/unit/test_dom_int_use_cases.py](../../../tests/unit/test_dom_int_use_cases.py)

## Limites e manutenção

Revalidar este índice ao alterar código, routers ou correspondência DOM. Evidências de migração dos oito módulos com implementação identificada estão na matriz, seção 7. Não promover scaffolding, propostas MOD ou relações candidatas a implementação aprovada.

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-09-17 | Criação do inventário e navegação; aprovação não presumida | Equipe SIGMUN |
