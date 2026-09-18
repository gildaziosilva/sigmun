# sigmun_seg — índice do módulo

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

- Código-fonte: [sigmun_seg](../../../src/modules/sigmun_seg).
- Verificação estática: 17/09/2026, base `51c82dc`.
- Domínio no escopo observado: [DOM-SEG](../../DOM-SEG/index.md).
- MOD **proposto, não aprovado**: `MOD-SEG`.
- Correspondência: **Confirmada no escopo observado**.
- Maturidade: **Implementação identificada**; não equivale a completude, homologação ou prontidão para produção.
- Inventário Python: 32 arquivos; 24 com instruções além de docstrings/pass. Contagem não é medida de cobertura funcional.

## Estrutura técnica

- [domain](../../../src/modules/sigmun_seg/domain) — implementação identificada
- [application](../../../src/modules/sigmun_seg/application) — implementação identificada
- [infrastructure](../../../src/modules/sigmun_seg/infrastructure) — implementação identificada
- [presentation](../../../src/modules/sigmun_seg/presentation) — implementação identificada

## APIs e ponto de entrada

[Registro da aplicação](../../../src/main.py).

- [src/modules/sigmun_seg/presentation/api/__init__.py](../../../src/modules/sigmun_seg/presentation/api/__init__.py) — registro em `src/main.py`, linha 222 na base inspecionada.

## Inventário de implementação

Arquivos com instruções além de docstrings/pass. A listagem aponta artefatos; não transforma cada arquivo em capacidade completa.

### domain

- [domain/entities/__init__.py](../../../src/modules/sigmun_seg/domain/entities/__init__.py)
- [domain/events/__init__.py](../../../src/modules/sigmun_seg/domain/events/__init__.py)
- [domain/exceptions.py](../../../src/modules/sigmun_seg/domain/exceptions.py)
- [domain/services/__init__.py](../../../src/modules/sigmun_seg/domain/services/__init__.py)
- [domain/value_objects/__init__.py](../../../src/modules/sigmun_seg/domain/value_objects/__init__.py)

### application

- [application/interfaces/__init__.py](../../../src/modules/sigmun_seg/application/interfaces/__init__.py)
- [application/use_cases/chave_use_cases.py](../../../src/modules/sigmun_seg/application/use_cases/chave_use_cases.py)
- [application/use_cases/controle_use_cases.py](../../../src/modules/sigmun_seg/application/use_cases/controle_use_cases.py)
- [application/use_cases/credencial_use_cases.py](../../../src/modules/sigmun_seg/application/use_cases/credencial_use_cases.py)
- [application/use_cases/incidente_use_cases.py](../../../src/modules/sigmun_seg/application/use_cases/incidente_use_cases.py)
- [application/use_cases/politica_use_cases.py](../../../src/modules/sigmun_seg/application/use_cases/politica_use_cases.py)

### infrastructure

- [infrastructure/database/models.py](../../../src/modules/sigmun_seg/infrastructure/database/models.py)
- [infrastructure/repositories/__init__.py](../../../src/modules/sigmun_seg/infrastructure/repositories/__init__.py)
- [infrastructure/repositories/sqlalchemy_chave_repository.py](../../../src/modules/sigmun_seg/infrastructure/repositories/sqlalchemy_chave_repository.py)
- [infrastructure/repositories/sqlalchemy_controle_repository.py](../../../src/modules/sigmun_seg/infrastructure/repositories/sqlalchemy_controle_repository.py)
- [infrastructure/repositories/sqlalchemy_credencial_repository.py](../../../src/modules/sigmun_seg/infrastructure/repositories/sqlalchemy_credencial_repository.py)
- [infrastructure/repositories/sqlalchemy_incidente_repository.py](../../../src/modules/sigmun_seg/infrastructure/repositories/sqlalchemy_incidente_repository.py)
- [infrastructure/repositories/sqlalchemy_politica_repository.py](../../../src/modules/sigmun_seg/infrastructure/repositories/sqlalchemy_politica_repository.py)

### presentation

- [presentation/api/__init__.py](../../../src/modules/sigmun_seg/presentation/api/__init__.py)
- [presentation/schemas/chave_schemas.py](../../../src/modules/sigmun_seg/presentation/schemas/chave_schemas.py)
- [presentation/schemas/controle_schemas.py](../../../src/modules/sigmun_seg/presentation/schemas/controle_schemas.py)
- [presentation/schemas/credencial_schemas.py](../../../src/modules/sigmun_seg/presentation/schemas/credencial_schemas.py)
- [presentation/schemas/incidente_schemas.py](../../../src/modules/sigmun_seg/presentation/schemas/incidente_schemas.py)
- [presentation/schemas/politica_schemas.py](../../../src/modules/sigmun_seg/presentation/schemas/politica_schemas.py)

## Testes relacionados

Arquivos que mencionam explicitamente o nome técnico do módulo. Não executados nesta auditoria documental.

- [tests/unit/test_dom_seg_chave_credencial_use_cases.py](../../../tests/unit/test_dom_seg_chave_credencial_use_cases.py)
- [tests/unit/test_dom_seg_use_cases.py](../../../tests/unit/test_dom_seg_use_cases.py)

## Limites e manutenção

Revalidar este índice ao alterar código, routers ou correspondência DOM. Evidências de migração dos oito módulos com implementação identificada estão na matriz, seção 7. Não promover scaffolding, propostas MOD ou relações candidatas a implementação aprovada.

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-09-17 | Criação do inventário e navegação; aprovação não presumida | Equipe SIGMUN |
