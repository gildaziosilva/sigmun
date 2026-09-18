# sigmun_gdo — índice do módulo

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

- Código-fonte: [sigmun_gdo](../../../src/modules/sigmun_gdo).
- Verificação estática: 17/09/2026, base `51c82dc`.
- Domínio no escopo observado: [DOM-GDO](../../DOM-GDO/index.md).
- MOD **proposto, não aprovado**: `MOD-GDO`.
- Correspondência: **Confirmada no escopo observado**.
- Maturidade: **Implementação identificada**; não equivale a completude, homologação ou prontidão para produção.
- Inventário Python: 38 arquivos; 33 com instruções além de docstrings/pass. Contagem não é medida de cobertura funcional.

## Estrutura técnica

- [domain](../../../src/modules/sigmun_gdo/domain) — implementação identificada
- [application](../../../src/modules/sigmun_gdo/application) — implementação identificada
- [infrastructure](../../../src/modules/sigmun_gdo/infrastructure) — implementação identificada
- [presentation](../../../src/modules/sigmun_gdo/presentation) — implementação identificada

## APIs e ponto de entrada

[Registro da aplicação](../../../src/main.py).

- [src/modules/sigmun_gdo/presentation/api/__init__.py](../../../src/modules/sigmun_gdo/presentation/api/__init__.py) — registro em `src/main.py`, linha 225 na base inspecionada.

## Inventário de implementação

Arquivos com instruções além de docstrings/pass. A listagem aponta artefatos; não transforma cada arquivo em capacidade completa.

### domain

- [domain/entities/__init__.py](../../../src/modules/sigmun_gdo/domain/entities/__init__.py)
- [domain/events/__init__.py](../../../src/modules/sigmun_gdo/domain/events/__init__.py)
- [domain/exceptions.py](../../../src/modules/sigmun_gdo/domain/exceptions.py)
- [domain/services/__init__.py](../../../src/modules/sigmun_gdo/domain/services/__init__.py)
- [domain/value_objects/__init__.py](../../../src/modules/sigmun_gdo/domain/value_objects/__init__.py)

### application

- [application/interfaces/__init__.py](../../../src/modules/sigmun_gdo/application/interfaces/__init__.py)
- [application/use_cases/__init__.py](../../../src/modules/sigmun_gdo/application/use_cases/__init__.py)
- [application/use_cases/arquivar_documento_use_case.py](../../../src/modules/sigmun_gdo/application/use_cases/arquivar_documento_use_case.py)
- [application/use_cases/assinar_documento_use_case.py](../../../src/modules/sigmun_gdo/application/use_cases/assinar_documento_use_case.py)
- [application/use_cases/avaliar_destinacao_use_case.py](../../../src/modules/sigmun_gdo/application/use_cases/avaliar_destinacao_use_case.py)
- [application/use_cases/classificar_documento_use_case.py](../../../src/modules/sigmun_gdo/application/use_cases/classificar_documento_use_case.py)
- [application/use_cases/criar_documento_use_case.py](../../../src/modules/sigmun_gdo/application/use_cases/criar_documento_use_case.py)
- [application/use_cases/criar_versao_documento_use_case.py](../../../src/modules/sigmun_gdo/application/use_cases/criar_versao_documento_use_case.py)
- [application/use_cases/tipo_documento_use_cases.py](../../../src/modules/sigmun_gdo/application/use_cases/tipo_documento_use_cases.py)
- [application/use_cases/tramitar_documento_use_case.py](../../../src/modules/sigmun_gdo/application/use_cases/tramitar_documento_use_case.py)

### infrastructure

- [infrastructure/database/models.py](../../../src/modules/sigmun_gdo/infrastructure/database/models.py)
- [infrastructure/database/seeds.py](../../../src/modules/sigmun_gdo/infrastructure/database/seeds.py)
- [infrastructure/messaging/__init__.py](../../../src/modules/sigmun_gdo/infrastructure/messaging/__init__.py)
- [infrastructure/messaging/dispatcher.py](../../../src/modules/sigmun_gdo/infrastructure/messaging/dispatcher.py)
- [infrastructure/messaging/outbox.py](../../../src/modules/sigmun_gdo/infrastructure/messaging/outbox.py)
- [infrastructure/repositories/__init__.py](../../../src/modules/sigmun_gdo/infrastructure/repositories/__init__.py)
- [infrastructure/repositories/sqlalchemy_arquivamento_repository.py](../../../src/modules/sigmun_gdo/infrastructure/repositories/sqlalchemy_arquivamento_repository.py)
- [infrastructure/repositories/sqlalchemy_assinatura_repository.py](../../../src/modules/sigmun_gdo/infrastructure/repositories/sqlalchemy_assinatura_repository.py)
- [infrastructure/repositories/sqlalchemy_classificacao_documental_repository.py](../../../src/modules/sigmun_gdo/infrastructure/repositories/sqlalchemy_classificacao_documental_repository.py)
- [infrastructure/repositories/sqlalchemy_documento_repository.py](../../../src/modules/sigmun_gdo/infrastructure/repositories/sqlalchemy_documento_repository.py)
- [infrastructure/repositories/sqlalchemy_processo_documento_repository.py](../../../src/modules/sigmun_gdo/infrastructure/repositories/sqlalchemy_processo_documento_repository.py)
- [infrastructure/repositories/sqlalchemy_tabela_temporalidade_repository.py](../../../src/modules/sigmun_gdo/infrastructure/repositories/sqlalchemy_tabela_temporalidade_repository.py)
- [infrastructure/repositories/sqlalchemy_tipo_documental_repository.py](../../../src/modules/sigmun_gdo/infrastructure/repositories/sqlalchemy_tipo_documental_repository.py)
- [infrastructure/repositories/sqlalchemy_tramitacao_repository.py](../../../src/modules/sigmun_gdo/infrastructure/repositories/sqlalchemy_tramitacao_repository.py)
- [infrastructure/repositories/sqlalchemy_versao_documento_repository.py](../../../src/modules/sigmun_gdo/infrastructure/repositories/sqlalchemy_versao_documento_repository.py)

### presentation

- [presentation/api/__init__.py](../../../src/modules/sigmun_gdo/presentation/api/__init__.py)
- [presentation/schemas/__init__.py](../../../src/modules/sigmun_gdo/presentation/schemas/__init__.py)

## Testes relacionados

Arquivos que mencionam explicitamente o nome técnico do módulo. Não executados nesta auditoria documental.

- [tests/integration/test_gdo_api.py](../../../tests/integration/test_gdo_api.py)
- [tests/integration/test_gdo_eventos.py](../../../tests/integration/test_gdo_eventos.py)
- [tests/integration/test_gdo_seeds.py](../../../tests/integration/test_gdo_seeds.py)
- [tests/unit/test_gdo_use_cases.py](../../../tests/unit/test_gdo_use_cases.py)

## Limites e manutenção

Revalidar este índice ao alterar código, routers ou correspondência DOM. Evidências de migração dos oito módulos com implementação identificada estão na matriz, seção 7. Não promover scaffolding, propostas MOD ou relações candidatas a implementação aprovada.

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-09-17 | Criação do inventário e navegação; aprovação não presumida | Equipe SIGMUN |
