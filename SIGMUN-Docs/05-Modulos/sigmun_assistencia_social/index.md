# sigmun_assistencia_social — índice do módulo

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal
**Domínio:** Módulos de aplicação
**Versão:** 1.1
**Status:** Em elaboração
**Classificação da Informação:** Pública
**Última atualização:** 2026-09-29
**Responsável:** Equipe SIGMUN

| Campo | Conteúdo |
| --- | --- |
| Projeto | SIGMUN |
| Proprietário | Módulos de aplicação |
| Responsável | Equipe SIGMUN |
| Versão | 1.1 |
| Status | Em elaboração; implementação verificada na auditoria de 29/09/2026 |
| Classificação | Pública |
| Data de Criação | 17/09/2026 |
| Última Revisão | 29/09/2026 |
| Próxima Revisão | Ao alterar os documentos ou evidências relacionados |
| Aprovado por | Aprovação não registrada |

**Documento(s) Relacionado(s):** [Documentação geral](../../index.md) · [Catálogo de módulos](../index.md) · [Matriz DOM ↔ módulo](../../01-Arquitetura-Corporativa/031-Matriz-de-Correspondencia-DOM-MOD.md) · [Auditoria documental](../../00-Governanca/AUDITORIA-DOCUMENTAL-2026-09-17.md)

## Identidade e estado observado

- Código-fonte: [sigmun_assistencia_social](../../../src/modules/sigmun_assistencia_social).
- Implementação identificada em 2026-09-28 (commit `33d53da`); verificado por auditoria em 2026-09-29.
- Domínio: [DOM-ASS](../../DOM-ASS/index.md).
- MOD **proposto, não aprovado**: `MOD-ASS`.
- Correspondência: **Candidata; validar escopo**.
- Maturidade: **Implementada**. 18 arquivos Python com entidades, regras de negócio, casos de uso, repositórios SQLAlchemy, schemas e router registrado em `src/main.py`.
- Escopo: CadÚnico local (famílias e pessoas), unidades CRAS/CREAS/Centro Pop/Abrigo, benefícios eventuais e atendimentos sociais.

## Estrutura técnica

- [domain](../../../src/modules/sigmun_assistencia_social/domain) — entidades e regras (RN-ASS-001 a RN-ASS-004)
- [application](../../../src/modules/sigmun_assistencia_social/application) — ports e casos de uso
- [infrastructure](../../../src/modules/sigmun_assistencia_social/infrastructure) — modelos ORM (schema `ass`), repositórios e seed DEMO
- [presentation](../../../src/modules/sigmun_assistencia_social/presentation) — schemas e endpoints

## APIs e ponto de entrada

Router `sigmun_assistencia_social` registrado em [src/main.py](../../../src/main.py), prefixo `/api/v1/ass` (**20 paths**, **31 operações**): famílias, pessoas, unidades, benefícios (incluindo as transições aprovar/negar/entregar/cancelar) e atendimentos.

Persistência: schema `ass`, migração `alembic/versions/20260927_01_dom_ass_models.py` (head único).

## Testes relacionados

- [tests/unit/test_ass_use_cases.py](../../../tests/unit/test_ass_use_cases.py) — 49 testes dos casos de uso.
- [tests/integration/test_ass_seeds.py](../../../tests/integration/test_ass_seeds.py) — 5 testes de idempotência do seed DEMO.
- [scripts/seed_ass.py](../../../scripts/seed_ass.py) — carga DEMO (`--dry-run`, `--limpar`).

## Qualidade estática (2026-09-29)

- `ruff check src/modules/sigmun_assistencia_social/` — **All checks passed** (era 137 erros).
- `mypy src/modules/sigmun_assistencia_social/` — **Success: no issues found in 18 source files** (era 155 erros).

## Limites e manutenção

Revalidar este índice ao alterar código, routers ou correspondência DOM. Não promover scaffolding, propostas MOD ou relações candidatas a implementação aprovada.

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-09-17 | Criação do inventário e navegação; aprovação não presumida | Equipe SIGMUN |
| 1.1 | 2026-09-29 | Atualizado para a implementação entregue em `33d53da` e para o resultado da auditoria | Equipe SIGMUN |
