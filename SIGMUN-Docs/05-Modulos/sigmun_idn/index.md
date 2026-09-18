# sigmun_idn — índice do módulo

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

- Código-fonte: [sigmun_idn](../../../src/modules/sigmun_idn).
- Verificação estática: 17/09/2026, base `51c82dc`.
- Domínio no escopo observado: [DOM-IDN](../../DOM-IDN/index.md).
- MOD **proposto, não aprovado**: `MOD-IDN`.
- Correspondência: **Confirmada no escopo observado**.
- Maturidade: **Implementação identificada**; não equivale a completude, homologação ou prontidão para produção.
- Inventário Python: 31 arquivos; 26 com instruções além de docstrings/pass. Contagem não é medida de cobertura funcional.

## Estrutura técnica

- [domain](../../../src/modules/sigmun_idn/domain) — implementação identificada
- [application](../../../src/modules/sigmun_idn/application) — implementação identificada
- [infrastructure](../../../src/modules/sigmun_idn/infrastructure) — implementação identificada
- [presentation](../../../src/modules/sigmun_idn/presentation) — implementação identificada

## APIs e ponto de entrada

[Registro da aplicação](../../../src/main.py).

- [src/modules/sigmun_idn/presentation/api/__init__.py](../../../src/modules/sigmun_idn/presentation/api/__init__.py) — registro em `src/main.py`, linha 221 na base inspecionada.

## Inventário de implementação

Arquivos com instruções além de docstrings/pass. A listagem aponta artefatos; não transforma cada arquivo em capacidade completa.

### domain

- [domain/__init__.py](../../../src/modules/sigmun_idn/domain/__init__.py)
- [domain/entities/__init__.py](../../../src/modules/sigmun_idn/domain/entities/__init__.py)
- [domain/entities/usuario.py](../../../src/modules/sigmun_idn/domain/entities/usuario.py)
- [domain/events/__init__.py](../../../src/modules/sigmun_idn/domain/events/__init__.py)
- [domain/events/usuario_events.py](../../../src/modules/sigmun_idn/domain/events/usuario_events.py)
- [domain/exceptions.py](../../../src/modules/sigmun_idn/domain/exceptions.py)
- [domain/services/__init__.py](../../../src/modules/sigmun_idn/domain/services/__init__.py)
- [domain/services/auth_service.py](../../../src/modules/sigmun_idn/domain/services/auth_service.py)
- [domain/value_objects/__init__.py](../../../src/modules/sigmun_idn/domain/value_objects/__init__.py)
- [domain/value_objects/email.py](../../../src/modules/sigmun_idn/domain/value_objects/email.py)
- [domain/value_objects/login.py](../../../src/modules/sigmun_idn/domain/value_objects/login.py)
- [domain/value_objects/senha.py](../../../src/modules/sigmun_idn/domain/value_objects/senha.py)

### application

- [application/interfaces/__init__.py](../../../src/modules/sigmun_idn/application/interfaces/__init__.py)
- [application/interfaces/repositories.py](../../../src/modules/sigmun_idn/application/interfaces/repositories.py)
- [application/use_cases/__init__.py](../../../src/modules/sigmun_idn/application/use_cases/__init__.py)
- [application/use_cases/usuario_use_cases.py](../../../src/modules/sigmun_idn/application/use_cases/usuario_use_cases.py)

### infrastructure

- [infrastructure/database/__init__.py](../../../src/modules/sigmun_idn/infrastructure/database/__init__.py)
- [infrastructure/database/models.py](../../../src/modules/sigmun_idn/infrastructure/database/models.py)
- [infrastructure/repositories/__init__.py](../../../src/modules/sigmun_idn/infrastructure/repositories/__init__.py)
- [infrastructure/repositories/sqlalchemy_auditoria_repository.py](../../../src/modules/sigmun_idn/infrastructure/repositories/sqlalchemy_auditoria_repository.py)
- [infrastructure/repositories/sqlalchemy_permissao_repository.py](../../../src/modules/sigmun_idn/infrastructure/repositories/sqlalchemy_permissao_repository.py)
- [infrastructure/repositories/sqlalchemy_role_repository.py](../../../src/modules/sigmun_idn/infrastructure/repositories/sqlalchemy_role_repository.py)
- [infrastructure/repositories/sqlalchemy_sessao_repository.py](../../../src/modules/sigmun_idn/infrastructure/repositories/sqlalchemy_sessao_repository.py)
- [infrastructure/repositories/sqlalchemy_usuario_repository.py](../../../src/modules/sigmun_idn/infrastructure/repositories/sqlalchemy_usuario_repository.py)

### presentation

- [presentation/api/__init__.py](../../../src/modules/sigmun_idn/presentation/api/__init__.py)
- [presentation/schemas/__init__.py](../../../src/modules/sigmun_idn/presentation/schemas/__init__.py)

## Testes relacionados

Nenhum arquivo `test_*.py` com menção explícita ao nome técnico foi encontrado. Essa busca não exclui testes indiretos ou compartilhados.

## Limites e manutenção

Revalidar este índice ao alterar código, routers ou correspondência DOM. Evidências de migração dos oito módulos com implementação identificada estão na matriz, seção 7. Não promover scaffolding, propostas MOD ou relações candidatas a implementação aprovada.

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-09-17 | Criação do inventário e navegação; aprovação não presumida | Equipe SIGMUN |
