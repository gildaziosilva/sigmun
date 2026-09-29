# sigmun_obras — índice do módulo

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal
**Domínio:** Módulos de aplicação
**Versão:** 1.2
**Status:** Vigente
**Classificação da Informação:** Pública
**Última atualização:** 2026-09-29
**Responsável:** Equipe SIGMUN

| Campo | Conteúdo |
| --- | --- |
| Projeto | SIGMUN |
| Proprietário | Módulos de aplicação |
| Responsável | Equipe SIGMUN |
| Versão | 1.2 |
| Status | Vigente; artefatos `001`-`026` do domínio detalhados e correspondência DOM confirmada |
| Classificação | Pública |
| Data de Criação | 17/09/2026 |
| Última Revisão | 29/09/2026 |
| Próxima Revisão | Ao alterar código, routers ou correspondência DOM |
| Aprovado por | Aprovação não registrada |

**Documento(s) Relacionado(s):** [Documentação geral](../../index.md) · [Catálogo de módulos](../index.md) · [Matriz DOM ↔ módulo](../../01-Arquitetura-Corporativa/031-Matriz-de-Correspondencia-DOM-MOD.md)

## Identidade e estado observado

- Código-fonte: [sigmun_obras](../../../src/modules/sigmun_obras).
- Domínio: [DOM-OBR](../../DOM-OBR/index.md) — Obras e Infraestrutura.
- MOD **confirmado**: `MOD-OBR` (promovido a confirmado em 2026-09-29).
- Correspondência: **Confirmada**, após conciliação dos artefatos `001`–`026` com o escopo implementado.
- Maturidade: **Implementada**. O scaffolding observado em 17/09/2026 (13 arquivos vazios, sem router) foi substituído por implementação com entidades, regras de negócio, casos de uso, repositórios SQLAlchemy, schemas e router registrado em `src/main.py`.
- Escopo: acompanhamento físico-financeiro de obras públicas — cadastro e ciclo de vida das obras, medições físico-financeiras, despesas (repasses e custos), etapas de execução e vistorias fiscalizadoras.

## Regras de negócio

| Regra | Descrição |
| --- | --- |
| RN-OBR-001 | O número da obra é único no cadastro municipal de obras públicas. |
| RN-OBR-002 | A obra obedece ao ciclo PLANEJADA → EM_LICITACAO → CONTRATADA → EM_EXECUCAO → CONCLUIDA, com SUSPENSA e CANCELADA disponíveis; obra concluída é terminal. |
| RN-OBR-003 | A contratação exige empresa, tipo de contratação e data de início prevista antes do início da execução. |
| RN-OBR-004 | Valores e percentuais de avanço são não negativos; o valor contratado não supera o orçado e o avanço financeiro não ultrapassa o físico. |
| RN-OBR-005 | A medição exige percentual físico entre 0 e 100 e obedece ao ciclo REGISTRADA → CONFERIDA → APROVADA, com GLOSADA e CANCELADA. |
| RN-OBR-006 | A despesa exige valor positivo e não pode superar o valor medido e ainda não pago. |
| RN-OBR-007 | A etapa exige responsável, percentual previsto não inferior ao realizado e obedece ao ciclo PENDENTE → EM_EXECUCAO → CONCLUIDA. |
| RN-OBR-008 | A vistoria exige fiscal e registra o parecer sobre o avanço físico verificado em campo. |

## Estrutura técnica

- [domain](../../../src/modules/sigmun_obras/domain) — entidades e regras (RN-OBR-001 a RN-OBR-008)
- [application](../../../src/modules/sigmun_obras/application) — ports e casos de uso
- [infrastructure](../../../src/modules/sigmun_obras/infrastructure) — modelos ORM (schema `obr`), repositórios e seed DEMO
- [presentation](../../../src/modules/sigmun_obras/presentation) — schemas e endpoints

## APIs e ponto de entrada

Router `sigmun_obras` registrado em [src/main.py](../../../src/main.py), prefixo `/api/v1/obr` (**21 paths**): obras (incluindo iniciar-execução, suspender, concluir e cancelar), acompanhamento consolidado, medições (aprovar/glosar/cancelar), despesas, etapas e vistorias.

Persistência: schema `obr`, migração `alembic/versions/20260929_04_dom_obr_models.py`.

## Testes relacionados

- `tests/unit/test_obr_obra_use_cases.py` — cadastro, ciclo de vida e exclusão de obras
- `tests/unit/test_obr_medicao_use_cases.py` — medições, avanço físico-financeiro e despesas
- `tests/unit/test_obr_acompanhamento_use_cases.py` — etapas e vistorias
- `tests/unit/obr_fixtures.py` — fixtures compartilhadas
- `tests/integration/test_geo_obr_openapi.py` — exposição dos domínios no OpenAPI

## Frontend

Módulo `Obras` em [frontend/admin/src/pages/obras](../../../frontend/admin/src/pages/obras), com abas de visão geral, obras, medições, despesas, etapas e vistorias. O seletor de obra habilita o acompanhamento físico-financeiro detalhado.

## Limites e manutenção

Revalidar este índice ao alterar código, routers ou correspondência DOM. Não promover scaffolding, propostas MOD ou relações candidatas a implementação aprovada.

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 17/09/2026 | Criação do índice; módulo em scaffolding (sem router) | Equipe SIGMUN |
| 1.1 | 2026-09-29 | Implementação do DOM-OBR (acompanhamento físico-financeiro de obras) | Equipe SIGMUN |
| 1.2 | 2026-09-29 | Artefatos `001`-`026` do domínio detalhados a partir da implementação; correspondência DOM promovida a confirmada | Equipe SIGMUN |
