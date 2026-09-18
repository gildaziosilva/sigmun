# sigmun_met — índice do módulo

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

- Código-fonte: [sigmun_met](../../../src/modules/sigmun_met).
- Verificação estática: 17/09/2026, base `51c82dc`.
- Domínio no escopo observado: [DOM-MET](../../DOM-MET/index.md).
- MOD **proposto, não aprovado**: `MOD-MET`.
- Correspondência: **Confirmada no escopo observado**.
- Maturidade: **Implementação identificada**; não equivale a completude, homologação ou prontidão para produção.
- Inventário Python: 27 arquivos; 24 com instruções além de docstrings/pass. Contagem não é medida de cobertura funcional.

## Estrutura técnica

- [domain](../../../src/modules/sigmun_met/domain) — implementação identificada
- [application](../../../src/modules/sigmun_met/application) — implementação identificada
- [infrastructure](../../../src/modules/sigmun_met/infrastructure) — implementação identificada
- [presentation](../../../src/modules/sigmun_met/presentation) — implementação identificada

## APIs e ponto de entrada

[Registro da aplicação](../../../src/main.py).

- [src/modules/sigmun_met/presentation/api/__init__.py](../../../src/modules/sigmun_met/presentation/api/__init__.py) — registro em `src/main.py`, linha 224 na base inspecionada.

## Inventário de implementação

Arquivos com instruções além de docstrings/pass. A listagem aponta artefatos; não transforma cada arquivo em capacidade completa.

### domain

- [domain/__init__.py](../../../src/modules/sigmun_met/domain/__init__.py)
- [domain/entities/__init__.py](../../../src/modules/sigmun_met/domain/entities/__init__.py)
- [domain/events/__init__.py](../../../src/modules/sigmun_met/domain/events/__init__.py)
- [domain/exceptions.py](../../../src/modules/sigmun_met/domain/exceptions.py)
- [domain/services/__init__.py](../../../src/modules/sigmun_met/domain/services/__init__.py)
- [domain/value_objects/__init__.py](../../../src/modules/sigmun_met/domain/value_objects/__init__.py)

### application

- [application/interfaces/__init__.py](../../../src/modules/sigmun_met/application/interfaces/__init__.py)
- [application/use_cases/__init__.py](../../../src/modules/sigmun_met/application/use_cases/__init__.py)
- [application/use_cases/classificacao_use_cases.py](../../../src/modules/sigmun_met/application/use_cases/classificacao_use_cases.py)
- [application/use_cases/metadado_use_cases.py](../../../src/modules/sigmun_met/application/use_cases/metadado_use_cases.py)
- [application/use_cases/taxonomia_use_cases.py](../../../src/modules/sigmun_met/application/use_cases/taxonomia_use_cases.py)
- [application/use_cases/termo_use_cases.py](../../../src/modules/sigmun_met/application/use_cases/termo_use_cases.py)
- [application/use_cases/valor_metadado_use_cases.py](../../../src/modules/sigmun_met/application/use_cases/valor_metadado_use_cases.py)

### infrastructure

- [infrastructure/database/__init__.py](../../../src/modules/sigmun_met/infrastructure/database/__init__.py)
- [infrastructure/database/models.py](../../../src/modules/sigmun_met/infrastructure/database/models.py)
- [infrastructure/repositories/__init__.py](../../../src/modules/sigmun_met/infrastructure/repositories/__init__.py)
- [infrastructure/repositories/sqlalchemy_classificacao_repository.py](../../../src/modules/sigmun_met/infrastructure/repositories/sqlalchemy_classificacao_repository.py)
- [infrastructure/repositories/sqlalchemy_metadado_repository.py](../../../src/modules/sigmun_met/infrastructure/repositories/sqlalchemy_metadado_repository.py)
- [infrastructure/repositories/sqlalchemy_taxonomia_repository.py](../../../src/modules/sigmun_met/infrastructure/repositories/sqlalchemy_taxonomia_repository.py)
- [infrastructure/repositories/sqlalchemy_termo_repository.py](../../../src/modules/sigmun_met/infrastructure/repositories/sqlalchemy_termo_repository.py)
- [infrastructure/repositories/sqlalchemy_valor_metadado_repository.py](../../../src/modules/sigmun_met/infrastructure/repositories/sqlalchemy_valor_metadado_repository.py)

### presentation

- [presentation/api/__init__.py](../../../src/modules/sigmun_met/presentation/api/__init__.py)
- [presentation/schemas/__init__.py](../../../src/modules/sigmun_met/presentation/schemas/__init__.py)

## Testes relacionados

Arquivos que mencionam explicitamente o nome técnico do módulo. Não executados nesta auditoria documental.

- [tests/unit/test_met_use_cases.py](../../../tests/unit/test_met_use_cases.py)

## Limites e manutenção

Revalidar este índice ao alterar código, routers ou correspondência DOM. Evidências de migração dos oito módulos com implementação identificada estão na matriz, seção 7. Não promover scaffolding, propostas MOD ou relações candidatas a implementação aprovada.

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-09-17 | Criação do inventário e navegação; aprovação não presumida | Equipe SIGMUN |
