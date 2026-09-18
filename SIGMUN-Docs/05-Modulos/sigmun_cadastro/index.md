# sigmun_cadastro — índice do módulo

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

- Código-fonte: [sigmun_cadastro](../../../src/modules/sigmun_cadastro).
- Verificação estática: 17/09/2026, base `51c82dc`.
- Domínio no escopo observado: [DOM-CUM](../../DOM-CUM/index.md).
- MOD **proposto, não aprovado**: `MOD-CUM`.
- Correspondência: **Confirmada no escopo observado**.
- Maturidade: **Implementação identificada**; não equivale a completude, homologação ou prontidão para produção.
- Inventário Python: 54 arquivos; 46 com instruções além de docstrings/pass. Contagem não é medida de cobertura funcional.

> Os routers descrevem mecanismo provisório de identificação “até DOM-IDN”. Não declarar integração de identidade concluída com base nesses comentários.

## Estrutura técnica

- [domain](../../../src/modules/sigmun_cadastro/domain) — implementação identificada
- [application](../../../src/modules/sigmun_cadastro/application) — implementação identificada
- [infrastructure](../../../src/modules/sigmun_cadastro/infrastructure) — implementação identificada
- [presentation](../../../src/modules/sigmun_cadastro/presentation) — implementação identificada

## APIs e ponto de entrada

[Registro da aplicação](../../../src/main.py).

- [src/modules/sigmun_cadastro/presentation/api/pessoas_router.py](../../../src/modules/sigmun_cadastro/presentation/api/pessoas_router.py) — registro em `src/main.py`, linha 219 na base inspecionada.
- [src/modules/sigmun_cadastro/presentation/api/unidades_router.py](../../../src/modules/sigmun_cadastro/presentation/api/unidades_router.py) — registro em `src/main.py`, linha 220 na base inspecionada.

## Inventário de implementação

Arquivos com instruções além de docstrings/pass. A listagem aponta artefatos; não transforma cada arquivo em capacidade completa.

### domain

- [domain/entities/__init__.py](../../../src/modules/sigmun_cadastro/domain/entities/__init__.py)
- [domain/entities/contato.py](../../../src/modules/sigmun_cadastro/domain/entities/contato.py)
- [domain/entities/documento.py](../../../src/modules/sigmun_cadastro/domain/entities/documento.py)
- [domain/entities/endereco.py](../../../src/modules/sigmun_cadastro/domain/entities/endereco.py)
- [domain/entities/pessoa.py](../../../src/modules/sigmun_cadastro/domain/entities/pessoa.py)
- [domain/entities/unidade_administrativa.py](../../../src/modules/sigmun_cadastro/domain/entities/unidade_administrativa.py)
- [domain/events/__init__.py](../../../src/modules/sigmun_cadastro/domain/events/__init__.py)
- [domain/events/pessoa_events.py](../../../src/modules/sigmun_cadastro/domain/events/pessoa_events.py)
- [domain/events/unidade_events.py](../../../src/modules/sigmun_cadastro/domain/events/unidade_events.py)
- [domain/exceptions.py](../../../src/modules/sigmun_cadastro/domain/exceptions.py)
- [domain/repositories/__init__.py](../../../src/modules/sigmun_cadastro/domain/repositories/__init__.py)
- [domain/repositories/pessoa_repository.py](../../../src/modules/sigmun_cadastro/domain/repositories/pessoa_repository.py)
- [domain/repositories/unidade_administrativa_repository.py](../../../src/modules/sigmun_cadastro/domain/repositories/unidade_administrativa_repository.py)
- [domain/value_objects/__init__.py](../../../src/modules/sigmun_cadastro/domain/value_objects/__init__.py)
- [domain/value_objects/cnpj.py](../../../src/modules/sigmun_cadastro/domain/value_objects/cnpj.py)
- [domain/value_objects/cpf.py](../../../src/modules/sigmun_cadastro/domain/value_objects/cpf.py)

### application

- [application/commands/__init__.py](../../../src/modules/sigmun_cadastro/application/commands/__init__.py)
- [application/commands/pessoa_commands.py](../../../src/modules/sigmun_cadastro/application/commands/pessoa_commands.py)
- [application/commands/unidade_commands.py](../../../src/modules/sigmun_cadastro/application/commands/unidade_commands.py)
- [application/queries/__init__.py](../../../src/modules/sigmun_cadastro/application/queries/__init__.py)
- [application/queries/pessoa_queries.py](../../../src/modules/sigmun_cadastro/application/queries/pessoa_queries.py)
- [application/queries/unidade_queries.py](../../../src/modules/sigmun_cadastro/application/queries/unidade_queries.py)
- [application/use_cases/__init__.py](../../../src/modules/sigmun_cadastro/application/use_cases/__init__.py)
- [application/use_cases/adicionar_contato.py](../../../src/modules/sigmun_cadastro/application/use_cases/adicionar_contato.py)
- [application/use_cases/adicionar_documento.py](../../../src/modules/sigmun_cadastro/application/use_cases/adicionar_documento.py)
- [application/use_cases/adicionar_endereco.py](../../../src/modules/sigmun_cadastro/application/use_cases/adicionar_endereco.py)
- [application/use_cases/atualizar_pessoa.py](../../../src/modules/sigmun_cadastro/application/use_cases/atualizar_pessoa.py)
- [application/use_cases/atualizar_unidade.py](../../../src/modules/sigmun_cadastro/application/use_cases/atualizar_unidade.py)
- [application/use_cases/consultar_pessoa.py](../../../src/modules/sigmun_cadastro/application/use_cases/consultar_pessoa.py)
- [application/use_cases/consultar_unidade.py](../../../src/modules/sigmun_cadastro/application/use_cases/consultar_unidade.py)
- [application/use_cases/excluir_pessoa.py](../../../src/modules/sigmun_cadastro/application/use_cases/excluir_pessoa.py)
- [application/use_cases/excluir_unidade.py](../../../src/modules/sigmun_cadastro/application/use_cases/excluir_unidade.py)
- [application/use_cases/listar_pessoas.py](../../../src/modules/sigmun_cadastro/application/use_cases/listar_pessoas.py)
- [application/use_cases/listar_unidades.py](../../../src/modules/sigmun_cadastro/application/use_cases/listar_unidades.py)
- [application/use_cases/registrar_pessoa.py](../../../src/modules/sigmun_cadastro/application/use_cases/registrar_pessoa.py)
- [application/use_cases/registrar_unidade.py](../../../src/modules/sigmun_cadastro/application/use_cases/registrar_unidade.py)

### infrastructure

- [infrastructure/database/__init__.py](../../../src/modules/sigmun_cadastro/infrastructure/database/__init__.py)
- [infrastructure/database/models.py](../../../src/modules/sigmun_cadastro/infrastructure/database/models.py)
- [infrastructure/repositories/__init__.py](../../../src/modules/sigmun_cadastro/infrastructure/repositories/__init__.py)
- [infrastructure/repositories/sqlalchemy_pessoa_repository.py](../../../src/modules/sigmun_cadastro/infrastructure/repositories/sqlalchemy_pessoa_repository.py)
- [infrastructure/repositories/sqlalchemy_unidade_administrativa_repository.py](../../../src/modules/sigmun_cadastro/infrastructure/repositories/sqlalchemy_unidade_administrativa_repository.py)

### presentation

- [presentation/api/pessoas_router.py](../../../src/modules/sigmun_cadastro/presentation/api/pessoas_router.py)
- [presentation/api/unidades_router.py](../../../src/modules/sigmun_cadastro/presentation/api/unidades_router.py)
- [presentation/schemas/__init__.py](../../../src/modules/sigmun_cadastro/presentation/schemas/__init__.py)
- [presentation/schemas/pessoa_schemas.py](../../../src/modules/sigmun_cadastro/presentation/schemas/pessoa_schemas.py)
- [presentation/schemas/unidade_schemas.py](../../../src/modules/sigmun_cadastro/presentation/schemas/unidade_schemas.py)

## Testes relacionados

Arquivos que mencionam explicitamente o nome técnico do módulo. Não executados nesta auditoria documental.

- [tests/integration/test_cadastro_sqlalchemy_repositories.py](../../../tests/integration/test_cadastro_sqlalchemy_repositories.py)
- [tests/unit/test_cadastro_value_objects.py](../../../tests/unit/test_cadastro_value_objects.py)
- [tests/unit/test_pessoa_entity.py](../../../tests/unit/test_pessoa_entity.py)

## Limites e manutenção

Revalidar este índice ao alterar código, routers ou correspondência DOM. Evidências de migração dos oito módulos com implementação identificada estão na matriz, seção 7. Não promover scaffolding, propostas MOD ou relações candidatas a implementação aprovada.

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-09-17 | Criação do inventário e navegação; aprovação não presumida | Equipe SIGMUN |
