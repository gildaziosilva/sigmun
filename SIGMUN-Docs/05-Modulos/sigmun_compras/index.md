# sigmun_compras — índice do módulo

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal
**Domínio:** Módulos de aplicação
**Versão:** 1.1
**Status:** Em elaboração
**Classificação da Informação:** Pública
**Última atualização:** 2026-09-17
**Responsável:** Equipe SIGMUN

| Campo | Conteúdo |
| --- | --- |
| Projeto | SIGMUN |
| Proprietário | Módulos de aplicação |
| Responsável | Equipe SIGMUN |
| Versão | 1.1 |
| Status | Em elaboração; validação editorial pendente |
| Classificação | Pública |
| Data de Criação | 17/09/2026 |
| Última Revisão | 17/09/2026 |
| Próxima Revisão | Ao alterar os documentos ou evidências relacionados |
| Aprovado por | Aprovação não registrada |

**Documento(s) Relacionado(s):** [Documentação geral](../../index.md) · [Catálogo de módulos](../index.md) · [Matriz DOM ↔ módulo](../../01-Arquitetura-Corporativa/031-Matriz-de-Correspondencia-DOM-MOD.md) · [Auditoria documental](../../00-Governanca/AUDITORIA-DOCUMENTAL-2026-09-17.md)

> Identidade corporativa vigente: **DOM-COM — Compras e Contratações**, conforme [ADR-0006](../../00-Governanca/ADR/ADR-0006-Compras-canonicalizacao.md). DOM-COMPRAS é identificação documental histórica; DOM-COMPRAS-001 é identificação histórica do piloto e localização física preservada por compatibilidade. A decisão não aprova códigos MOD nem certifica completude funcional.

## Identidade e estado observado

- Código-fonte: [sigmun_compras](../../../src/modules/sigmun_compras).
- Verificação estática: 17/09/2026, base `51c82dc`.
- Domínio no escopo observado: [DOM-COM](../../DOM-COMPRAS-001/index.md).
- MOD **proposto, não aprovado**: `MOD-COMPRAS`.
- Correspondência: **Confirmada no escopo observado**.
- Maturidade: **Implementação identificada**; não equivale a completude, homologação ou prontidão para produção.
- Inventário Python: 117 arquivos; 105 com instruções além de docstrings/pass. Contagem não é medida de cobertura funcional.

> Processo documental em Compras não implica cobertura integral de DOM-GDO.

## Estrutura técnica

- [domain](../../../src/modules/sigmun_compras/domain) — implementação identificada
- [application](../../../src/modules/sigmun_compras/application) — implementação identificada
- [infrastructure](../../../src/modules/sigmun_compras/infrastructure) — implementação identificada
- [presentation](../../../src/modules/sigmun_compras/presentation) — implementação identificada

## APIs e ponto de entrada

[Registro da aplicação](../../../src/main.py).

- [src/modules/sigmun_compras/presentation/api/fornecedores_router.py](../../../src/modules/sigmun_compras/presentation/api/fornecedores_router.py) — registro em `src/main.py`, linha 213 na base inspecionada.
- [src/modules/sigmun_compras/presentation/api/itens_compras_router.py](../../../src/modules/sigmun_compras/presentation/api/itens_compras_router.py) — registro em `src/main.py`, linha 214 na base inspecionada.
- [src/modules/sigmun_compras/presentation/api/compras_router.py](../../../src/modules/sigmun_compras/presentation/api/compras_router.py) — registro em `src/main.py`, linha 215 na base inspecionada.
- [src/modules/sigmun_compras/presentation/api/processo_documental_router.py](../../../src/modules/sigmun_compras/presentation/api/processo_documental_router.py) — registro em `src/main.py`, linha 216 na base inspecionada.
- [src/modules/sigmun_compras/presentation/api/contratos_router.py](../../../src/modules/sigmun_compras/presentation/api/contratos_router.py) — registro em `src/main.py`, linha 217 na base inspecionada.
- [src/modules/sigmun_compras/presentation/api/auditoria_router.py](../../../src/modules/sigmun_compras/presentation/api/auditoria_router.py) — registro em `src/main.py`, linha 218 na base inspecionada.

## Inventário de implementação

Arquivos com instruções além de docstrings/pass. A listagem aponta artefatos; não transforma cada arquivo em capacidade completa.

### domain

- [domain/entities/__init__.py](../../../src/modules/sigmun_compras/domain/entities/__init__.py)
- [domain/entities/compra.py](../../../src/modules/sigmun_compras/domain/entities/compra.py)
- [domain/entities/contrato.py](../../../src/modules/sigmun_compras/domain/entities/contrato.py)
- [domain/entities/fornecedor.py](../../../src/modules/sigmun_compras/domain/entities/fornecedor.py)
- [domain/entities/item_compra.py](../../../src/modules/sigmun_compras/domain/entities/item_compra.py)
- [domain/entities/processo_documental.py](../../../src/modules/sigmun_compras/domain/entities/processo_documental.py)
- [domain/entities/registro_auditoria.py](../../../src/modules/sigmun_compras/domain/entities/registro_auditoria.py)
- [domain/events/__init__.py](../../../src/modules/sigmun_compras/domain/events/__init__.py)
- [domain/events/compra_events.py](../../../src/modules/sigmun_compras/domain/events/compra_events.py)
- [domain/events/contrato_events.py](../../../src/modules/sigmun_compras/domain/events/contrato_events.py)
- [domain/events/fornecedor_events.py](../../../src/modules/sigmun_compras/domain/events/fornecedor_events.py)
- [domain/events/item_compra_events.py](../../../src/modules/sigmun_compras/domain/events/item_compra_events.py)
- [domain/events/processo_documental_events.py](../../../src/modules/sigmun_compras/domain/events/processo_documental_events.py)
- [domain/exceptions.py](../../../src/modules/sigmun_compras/domain/exceptions.py)
- [domain/repositories/__init__.py](../../../src/modules/sigmun_compras/domain/repositories/__init__.py)
- [domain/repositories/compra_repository.py](../../../src/modules/sigmun_compras/domain/repositories/compra_repository.py)
- [domain/repositories/contrato_repository.py](../../../src/modules/sigmun_compras/domain/repositories/contrato_repository.py)
- [domain/repositories/fornecedor_repository.py](../../../src/modules/sigmun_compras/domain/repositories/fornecedor_repository.py)
- [domain/repositories/item_compra_repository.py](../../../src/modules/sigmun_compras/domain/repositories/item_compra_repository.py)
- [domain/repositories/processo_documental_repository.py](../../../src/modules/sigmun_compras/domain/repositories/processo_documental_repository.py)
- [domain/repositories/trilha_auditoria_repository.py](../../../src/modules/sigmun_compras/domain/repositories/trilha_auditoria_repository.py)

### application

- [application/commands/__init__.py](../../../src/modules/sigmun_compras/application/commands/__init__.py)
- [application/commands/alterar_situacao_compra_command.py](../../../src/modules/sigmun_compras/application/commands/alterar_situacao_compra_command.py)
- [application/commands/alterar_situacao_contrato_command.py](../../../src/modules/sigmun_compras/application/commands/alterar_situacao_contrato_command.py)
- [application/commands/atualizar_compra_command.py](../../../src/modules/sigmun_compras/application/commands/atualizar_compra_command.py)
- [application/commands/atualizar_contrato_command.py](../../../src/modules/sigmun_compras/application/commands/atualizar_contrato_command.py)
- [application/commands/atualizar_fornecedor_command.py](../../../src/modules/sigmun_compras/application/commands/atualizar_fornecedor_command.py)
- [application/commands/atualizar_item_compra_command.py](../../../src/modules/sigmun_compras/application/commands/atualizar_item_compra_command.py)
- [application/commands/atualizar_processo_documental_command.py](../../../src/modules/sigmun_compras/application/commands/atualizar_processo_documental_command.py)
- [application/commands/criar_compra_command.py](../../../src/modules/sigmun_compras/application/commands/criar_compra_command.py)
- [application/commands/criar_contrato_command.py](../../../src/modules/sigmun_compras/application/commands/criar_contrato_command.py)
- [application/commands/criar_fornecedor_command.py](../../../src/modules/sigmun_compras/application/commands/criar_fornecedor_command.py)
- [application/commands/criar_item_compra_command.py](../../../src/modules/sigmun_compras/application/commands/criar_item_compra_command.py)
- [application/commands/criar_processo_documental_command.py](../../../src/modules/sigmun_compras/application/commands/criar_processo_documental_command.py)
- [application/commands/excluir_compra_command.py](../../../src/modules/sigmun_compras/application/commands/excluir_compra_command.py)
- [application/commands/excluir_contrato_command.py](../../../src/modules/sigmun_compras/application/commands/excluir_contrato_command.py)
- [application/commands/excluir_processo_documental_command.py](../../../src/modules/sigmun_compras/application/commands/excluir_processo_documental_command.py)
- [application/commands/formalizar_contratacao_command.py](../../../src/modules/sigmun_compras/application/commands/formalizar_contratacao_command.py)
- [application/commands/inativar_fornecedor_command.py](../../../src/modules/sigmun_compras/application/commands/inativar_fornecedor_command.py)
- [application/commands/registrar_pendencia_compra_command.py](../../../src/modules/sigmun_compras/application/commands/registrar_pendencia_compra_command.py)
- [application/commands/remover_item_compra_command.py](../../../src/modules/sigmun_compras/application/commands/remover_item_compra_command.py)
- [application/queries/__init__.py](../../../src/modules/sigmun_compras/application/queries/__init__.py)
- [application/queries/consultar_compra_query.py](../../../src/modules/sigmun_compras/application/queries/consultar_compra_query.py)
- [application/queries/consultar_contrato_query.py](../../../src/modules/sigmun_compras/application/queries/consultar_contrato_query.py)
- [application/queries/consultar_fornecedor_query.py](../../../src/modules/sigmun_compras/application/queries/consultar_fornecedor_query.py)
- [application/queries/consultar_item_compra_query.py](../../../src/modules/sigmun_compras/application/queries/consultar_item_compra_query.py)
- [application/queries/consultar_processo_documental_query.py](../../../src/modules/sigmun_compras/application/queries/consultar_processo_documental_query.py)
- [application/queries/consultar_trilha_auditoria_query.py](../../../src/modules/sigmun_compras/application/queries/consultar_trilha_auditoria_query.py)
- [application/queries/listar_compras_query.py](../../../src/modules/sigmun_compras/application/queries/listar_compras_query.py)
- [application/queries/listar_contratos_query.py](../../../src/modules/sigmun_compras/application/queries/listar_contratos_query.py)
- [application/queries/listar_fornecedores_query.py](../../../src/modules/sigmun_compras/application/queries/listar_fornecedores_query.py)
- [application/queries/listar_itens_compra_query.py](../../../src/modules/sigmun_compras/application/queries/listar_itens_compra_query.py)
- [application/queries/listar_processos_documentais_query.py](../../../src/modules/sigmun_compras/application/queries/listar_processos_documentais_query.py)
- [application/services/servico_de_auditoria.py](../../../src/modules/sigmun_compras/application/services/servico_de_auditoria.py)
- [application/use_cases/__init__.py](../../../src/modules/sigmun_compras/application/use_cases/__init__.py)
- [application/use_cases/alterar_situacao_compra.py](../../../src/modules/sigmun_compras/application/use_cases/alterar_situacao_compra.py)
- [application/use_cases/alterar_situacao_contrato.py](../../../src/modules/sigmun_compras/application/use_cases/alterar_situacao_contrato.py)
- [application/use_cases/atualizar_compra.py](../../../src/modules/sigmun_compras/application/use_cases/atualizar_compra.py)
- [application/use_cases/atualizar_contrato.py](../../../src/modules/sigmun_compras/application/use_cases/atualizar_contrato.py)
- [application/use_cases/atualizar_fornecedor.py](../../../src/modules/sigmun_compras/application/use_cases/atualizar_fornecedor.py)
- [application/use_cases/atualizar_item_compra.py](../../../src/modules/sigmun_compras/application/use_cases/atualizar_item_compra.py)
- [application/use_cases/atualizar_processo_documental.py](../../../src/modules/sigmun_compras/application/use_cases/atualizar_processo_documental.py)
- [application/use_cases/consultar_compra.py](../../../src/modules/sigmun_compras/application/use_cases/consultar_compra.py)
- [application/use_cases/consultar_contrato.py](../../../src/modules/sigmun_compras/application/use_cases/consultar_contrato.py)
- [application/use_cases/consultar_fornecedor.py](../../../src/modules/sigmun_compras/application/use_cases/consultar_fornecedor.py)
- [application/use_cases/consultar_item_compra.py](../../../src/modules/sigmun_compras/application/use_cases/consultar_item_compra.py)
- [application/use_cases/consultar_processo_documental.py](../../../src/modules/sigmun_compras/application/use_cases/consultar_processo_documental.py)
- [application/use_cases/consultar_trilha_auditoria.py](../../../src/modules/sigmun_compras/application/use_cases/consultar_trilha_auditoria.py)
- [application/use_cases/excluir_compra.py](../../../src/modules/sigmun_compras/application/use_cases/excluir_compra.py)
- [application/use_cases/excluir_contrato.py](../../../src/modules/sigmun_compras/application/use_cases/excluir_contrato.py)
- [application/use_cases/excluir_processo_documental.py](../../../src/modules/sigmun_compras/application/use_cases/excluir_processo_documental.py)
- [application/use_cases/formalizar_contratacao.py](../../../src/modules/sigmun_compras/application/use_cases/formalizar_contratacao.py)
- [application/use_cases/inativar_fornecedor.py](../../../src/modules/sigmun_compras/application/use_cases/inativar_fornecedor.py)
- [application/use_cases/listar_compras.py](../../../src/modules/sigmun_compras/application/use_cases/listar_compras.py)
- [application/use_cases/listar_contratos.py](../../../src/modules/sigmun_compras/application/use_cases/listar_contratos.py)
- [application/use_cases/listar_fornecedores.py](../../../src/modules/sigmun_compras/application/use_cases/listar_fornecedores.py)
- [application/use_cases/listar_itens_compra.py](../../../src/modules/sigmun_compras/application/use_cases/listar_itens_compra.py)
- [application/use_cases/listar_processos_documentais.py](../../../src/modules/sigmun_compras/application/use_cases/listar_processos_documentais.py)
- [application/use_cases/registrar_compra.py](../../../src/modules/sigmun_compras/application/use_cases/registrar_compra.py)
- [application/use_cases/registrar_contrato.py](../../../src/modules/sigmun_compras/application/use_cases/registrar_contrato.py)
- [application/use_cases/registrar_fornecedor.py](../../../src/modules/sigmun_compras/application/use_cases/registrar_fornecedor.py)
- [application/use_cases/registrar_item_compra.py](../../../src/modules/sigmun_compras/application/use_cases/registrar_item_compra.py)
- [application/use_cases/registrar_pendencia_compra.py](../../../src/modules/sigmun_compras/application/use_cases/registrar_pendencia_compra.py)
- [application/use_cases/registrar_processo_documental.py](../../../src/modules/sigmun_compras/application/use_cases/registrar_processo_documental.py)
- [application/use_cases/remover_item_compra.py](../../../src/modules/sigmun_compras/application/use_cases/remover_item_compra.py)

### infrastructure

- [infrastructure/database/models.py](../../../src/modules/sigmun_compras/infrastructure/database/models.py)
- [infrastructure/repositories/__init__.py](../../../src/modules/sigmun_compras/infrastructure/repositories/__init__.py)
- [infrastructure/repositories/sqlalchemy_compra_repository.py](../../../src/modules/sigmun_compras/infrastructure/repositories/sqlalchemy_compra_repository.py)
- [infrastructure/repositories/sqlalchemy_contrato_repository.py](../../../src/modules/sigmun_compras/infrastructure/repositories/sqlalchemy_contrato_repository.py)
- [infrastructure/repositories/sqlalchemy_fornecedor_repository.py](../../../src/modules/sigmun_compras/infrastructure/repositories/sqlalchemy_fornecedor_repository.py)
- [infrastructure/repositories/sqlalchemy_item_compra_repository.py](../../../src/modules/sigmun_compras/infrastructure/repositories/sqlalchemy_item_compra_repository.py)
- [infrastructure/repositories/sqlalchemy_processo_documental_repository.py](../../../src/modules/sigmun_compras/infrastructure/repositories/sqlalchemy_processo_documental_repository.py)
- [infrastructure/repositories/sqlalchemy_trilha_auditoria_repository.py](../../../src/modules/sigmun_compras/infrastructure/repositories/sqlalchemy_trilha_auditoria_repository.py)

### presentation

- [presentation/api/auditoria_router.py](../../../src/modules/sigmun_compras/presentation/api/auditoria_router.py)
- [presentation/api/compras_router.py](../../../src/modules/sigmun_compras/presentation/api/compras_router.py)
- [presentation/api/contratos_router.py](../../../src/modules/sigmun_compras/presentation/api/contratos_router.py)
- [presentation/api/fornecedores_router.py](../../../src/modules/sigmun_compras/presentation/api/fornecedores_router.py)
- [presentation/api/itens_compras_router.py](../../../src/modules/sigmun_compras/presentation/api/itens_compras_router.py)
- [presentation/api/processo_documental_router.py](../../../src/modules/sigmun_compras/presentation/api/processo_documental_router.py)
- [presentation/schemas/auditoria_schemas.py](../../../src/modules/sigmun_compras/presentation/schemas/auditoria_schemas.py)
- [presentation/schemas/compra_schemas.py](../../../src/modules/sigmun_compras/presentation/schemas/compra_schemas.py)
- [presentation/schemas/contrato_schemas.py](../../../src/modules/sigmun_compras/presentation/schemas/contrato_schemas.py)
- [presentation/schemas/fornecedor_schemas.py](../../../src/modules/sigmun_compras/presentation/schemas/fornecedor_schemas.py)
- [presentation/schemas/item_compra_schemas.py](../../../src/modules/sigmun_compras/presentation/schemas/item_compra_schemas.py)
- [presentation/schemas/processo_documental_schemas.py](../../../src/modules/sigmun_compras/presentation/schemas/processo_documental_schemas.py)

## Testes relacionados

Arquivos que mencionam explicitamente o nome técnico do módulo. Não executados nesta auditoria documental.

- [tests/integration/test_auditoria_api.py](../../../tests/integration/test_auditoria_api.py)
- [tests/integration/test_auditoria_integracao_contratos.py](../../../tests/integration/test_auditoria_integracao_contratos.py)
- [tests/integration/test_compras_api.py](../../../tests/integration/test_compras_api.py)
- [tests/integration/test_contratos_api.py](../../../tests/integration/test_contratos_api.py)
- [tests/integration/test_formalizar_contratacao_api.py](../../../tests/integration/test_formalizar_contratacao_api.py)
- [tests/integration/test_fornecedores_api.py](../../../tests/integration/test_fornecedores_api.py)
- [tests/integration/test_itens_api.py](../../../tests/integration/test_itens_api.py)
- [tests/integration/test_processos_documentais_api.py](../../../tests/integration/test_processos_documentais_api.py)
- [tests/integration/test_sqlalchemy_repositories.py](../../../tests/integration/test_sqlalchemy_repositories.py)
- [tests/unit/test_compras_identidade_corporativa.py](../../../tests/unit/test_compras_identidade_corporativa.py)
- [tests/unit/test_compra_entity.py](../../../tests/unit/test_compra_entity.py)
- [tests/unit/test_compra_use_cases.py](../../../tests/unit/test_compra_use_cases.py)
- [tests/unit/test_contrato_entity.py](../../../tests/unit/test_contrato_entity.py)
- [tests/unit/test_contrato_use_cases.py](../../../tests/unit/test_contrato_use_cases.py)
- [tests/unit/test_formalizar_contratacao.py](../../../tests/unit/test_formalizar_contratacao.py)
- [tests/unit/test_fornecedor_entity.py](../../../tests/unit/test_fornecedor_entity.py)
- [tests/unit/test_fornecedor_use_cases.py](../../../tests/unit/test_fornecedor_use_cases.py)
- [tests/unit/test_item_compra_entity.py](../../../tests/unit/test_item_compra_entity.py)
- [tests/unit/test_item_compra_use_cases.py](../../../tests/unit/test_item_compra_use_cases.py)
- [tests/unit/test_processo_documental_entity.py](../../../tests/unit/test_processo_documental_entity.py)
- [tests/unit/test_processo_documental_use_cases.py](../../../tests/unit/test_processo_documental_use_cases.py)
- [tests/unit/test_registro_auditoria.py](../../../tests/unit/test_registro_auditoria.py)

## Limites e manutenção

Revalidar este índice ao alterar código, routers ou correspondência DOM. Evidências de migração dos oito módulos com implementação identificada estão na matriz, seção 7. Não promover scaffolding, propostas MOD ou relações candidatas a implementação aprovada.

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-09-17 | Criação do inventário e navegação; aprovação não presumida | Equipe SIGMUN |
| 1.1 | 2026-09-17 | Regeneração seletiva de Compras conforme ADR-0006; destinos físicos e demais qualificadores preservados | Cline, por autorização do solicitante |
