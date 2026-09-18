# sigmun_dad — índice do módulo

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

- Código-fonte: [sigmun_dad](../../../src/modules/sigmun_dad).
- Verificação estática: 17/09/2026, base `51c82dc`.
- Domínio no escopo observado: [DOM-DAD](../../DOM-DAD/index.md).
- MOD **proposto, não aprovado**: `MOD-DAD`.
- Correspondência: **Confirmada no escopo observado**.
- Maturidade: **Implementação identificada**; não equivale a completude, homologação ou prontidão para produção.
- Inventário Python: 22 arquivos; 22 com instruções além de docstrings/pass. Contagem não é medida de cobertura funcional.

## Estrutura técnica

- [domain](../../../src/modules/sigmun_dad/domain) — implementação identificada
- [application](../../../src/modules/sigmun_dad/application) — implementação identificada
- [infrastructure](../../../src/modules/sigmun_dad/infrastructure) — implementação identificada
- [presentation](../../../src/modules/sigmun_dad/presentation) — implementação identificada

## APIs e ponto de entrada

[Registro da aplicação](../../../src/main.py).

- [src/modules/sigmun_dad/presentation/api/__init__.py](../../../src/modules/sigmun_dad/presentation/api/__init__.py) — registro em `src/main.py`, linha 223 na base inspecionada.

## Inventário de implementação

Arquivos com instruções além de docstrings/pass. A listagem aponta artefatos; não transforma cada arquivo em capacidade completa.

### domain

- [domain/__init__.py](../../../src/modules/sigmun_dad/domain/__init__.py)
- [domain/entities/__init__.py](../../../src/modules/sigmun_dad/domain/entities/__init__.py)
- [domain/events/__init__.py](../../../src/modules/sigmun_dad/domain/events/__init__.py)
- [domain/exceptions.py](../../../src/modules/sigmun_dad/domain/exceptions.py)
- [domain/services/__init__.py](../../../src/modules/sigmun_dad/domain/services/__init__.py)
- [domain/value_objects/__init__.py](../../../src/modules/sigmun_dad/domain/value_objects/__init__.py)

### application

- [application/interfaces/__init__.py](../../../src/modules/sigmun_dad/application/interfaces/__init__.py)
- [application/use_cases/__init__.py](../../../src/modules/sigmun_dad/application/use_cases/__init__.py)
- [application/use_cases/catalogo_use_cases.py](../../../src/modules/sigmun_dad/application/use_cases/catalogo_use_cases.py)
- [application/use_cases/linhagem_use_cases.py](../../../src/modules/sigmun_dad/application/use_cases/linhagem_use_cases.py)
- [application/use_cases/politica_use_cases.py](../../../src/modules/sigmun_dad/application/use_cases/politica_use_cases.py)
- [application/use_cases/qualidade_use_cases.py](../../../src/modules/sigmun_dad/application/use_cases/qualidade_use_cases.py)

### infrastructure

- [infrastructure/database/__init__.py](../../../src/modules/sigmun_dad/infrastructure/database/__init__.py)
- [infrastructure/database/models.py](../../../src/modules/sigmun_dad/infrastructure/database/models.py)
- [infrastructure/repositories/__init__.py](../../../src/modules/sigmun_dad/infrastructure/repositories/__init__.py)
- [infrastructure/repositories/sqlalchemy_ativo_repository.py](../../../src/modules/sigmun_dad/infrastructure/repositories/sqlalchemy_ativo_repository.py)
- [infrastructure/repositories/sqlalchemy_catalogo_repository.py](../../../src/modules/sigmun_dad/infrastructure/repositories/sqlalchemy_catalogo_repository.py)
- [infrastructure/repositories/sqlalchemy_linhagem_repository.py](../../../src/modules/sigmun_dad/infrastructure/repositories/sqlalchemy_linhagem_repository.py)
- [infrastructure/repositories/sqlalchemy_politica_repository.py](../../../src/modules/sigmun_dad/infrastructure/repositories/sqlalchemy_politica_repository.py)
- [infrastructure/repositories/sqlalchemy_qualidade_repository.py](../../../src/modules/sigmun_dad/infrastructure/repositories/sqlalchemy_qualidade_repository.py)

### presentation

- [presentation/api/__init__.py](../../../src/modules/sigmun_dad/presentation/api/__init__.py)
- [presentation/schemas/__init__.py](../../../src/modules/sigmun_dad/presentation/schemas/__init__.py)

## Testes relacionados

Arquivos que mencionam explicitamente o nome técnico do módulo. Não executados nesta auditoria documental.

- [tests/unit/test_dad_use_cases.py](../../../tests/unit/test_dad_use_cases.py)

## Limites e manutenção

Revalidar este índice ao alterar código, routers ou correspondência DOM. Evidências de migração dos oito módulos com implementação identificada estão na matriz, seção 7. Não promover scaffolding, propostas MOD ou relações candidatas a implementação aprovada.

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-09-17 | Criação do inventário e navegação; aprovação não presumida | Equipe SIGMUN |
