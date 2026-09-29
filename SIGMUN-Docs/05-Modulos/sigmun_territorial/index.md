# sigmun_territorial — índice do módulo

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal
**Domínio:** Módulos de aplicação
**Versão:** 1.0
**Status:** Em elaboração; implementação verificada em 2026-09-29
**Classificação da Informação:** Pública
**Última atualização:** 2026-09-29
**Responsável:** Equipe SIGMUN

| Campo | Conteúdo |
| --- | --- |
| Projeto | SIGMUN |
| Proprietário | Módulos de aplicação |
| Responsável | Equipe SIGMUN |
| Versão | 1.0 |
| Status | Em elaboração; implementação verificada na auditoria de 29/09/2026 |
| Classificação | Pública |
| Data de Criação | 29/09/2026 |
| Última Revisão | 29/09/2026 |
| Próxima Revisão | Ao alterar os documentos ou evidências relacionados |
| Aprovado por | Aprovação não registrada |

**Documento(s) Relacionado(s):** [Documentação geral](../../index.md) · [Catálogo de módulos](../index.md) · [Matriz DOM ↔ módulo](../../01-Arquitetura-Corporativa/031-Matriz-de-Correspondencia-DOM-MOD.md)

## Identidade e estado observado

- Código-fonte: [sigmun_territorial](../../../src/modules/sigmun_territorial).
- Implementação verificada em 2026-09-29 (Fase IX.2 do `TODO.md`).
- Domínio: [DOM-TEL](../../DOM-TEL/index.md).
- MOD **proposto, não aprovado**: `MOD-TEL`.
- Correspondência: **Candidata; validar escopo**.
- Maturidade: **Implementada**. Entidades, regras de negócio, casos de uso, repositórios SQLAlchemy, schemas e router registrado em `src/main.py`.
- Escopo: divisões territoriais (bairro/distrito/setor/zona rural), logradouros públicos, planta genérica de valores e georreferenciamento.

## Estrutura técnica

- [domain](../../../src/modules/sigmun_territorial/domain) — entidades e regras (RN-TEL-001 a RN-TEL-006)
- [application](../../../src/modules/sigmun_territorial/application) — ports e 17 casos de uso
- [infrastructure](../../../src/modules/sigmun_territorial/infrastructure) — modelos ORM (schema `tel`), repositórios e seed DEMO
- [presentation](../../../src/modules/sigmun_territorial/presentation) — schemas e endpoints

## Regras de negócio implementadas

| Regra | Descrição | Garantia no banco |
| --- | --- | --- |
| RN-TEL-001 | Código do bairro é único no município. | `tel.bairros.codigo` UNIQUE |
| RN-TEL-002 | Código do logradouro é único e todo logradouro pertence a um bairro cadastrado. | `tel.logradouros.codigo` UNIQUE |
| RN-TEL-003 | No máximo uma planta genérica de valores **vigente** por ano, bairro e ocupação. | índice único parcial `uq_tel_planta_vigente` |
| RN-TEL-004 | Ciclo de vida `RASCUNHO → VIGENTE → REVOGADA`, sem retorno a partir de `REVOGADA`; revogação exige justificativa. | — |
| RN-TEL-005 | Georreferência exige datum suportado, coordenadas no intervalo e vértices compatíveis com o tipo de geometria. | check `ck_tel_geo_referencia` |
| RN-TEL-006 | Bairro com logradouros ativos não pode ser excluído. | — |

## APIs e ponto de entrada

Router `sigmun_territorial` registrado em [src/main.py](../../../src/main.py), prefixo `/api/v1/tel` (**15 paths**, **25 operações**):

- **Bairros** — `POST/GET /bairros`, `GET /bairros/{id}`, `GET /bairros/codigo/{codigo}`, `GET /bairros/{id}/logradouros`, `PATCH/DELETE /bairros/{id}`
- **Logradouros** — `POST/GET /logradouros`, `GET /logradouros/{id}`, `GET /logradouros/codigo/{codigo}`, `PATCH/DELETE /logradouros/{id}`
- **Planta genérica de valores** — `POST/GET /plantas-valores`, `GET /plantas-valores/vigente?ano&bairro_id&ocupacao`, `GET/PATCH /plantas-valores/{id}`, `POST /plantas-valores/{id}/ativar`, `POST /plantas-valores/{id}/revogar`
- **Georreferenciamento** — `POST/GET /georreferencias`, `GET /georreferencias/referencia?bairro_id|logradouro_id`, `GET/DELETE /georreferencias/{id}`

Persistência: schema `tel`, migração `alembic/versions/20260929_01_dom_tel_models.py` (cabeça única da cadeia).

## Contrato de integração (DOM-IMO)

O DOM-IMO **não acessa** o schema `tel` (ROADMAP §2.7). O cálculo do valor venal recebe os valores unitários já resolvidos pelo consumidor deste endpoint:

```
GET /api/v1/tel/plantas-valores/vigente?ano={ano}&bairro_id={id}&ocupacao={ocupacao}
```

O mapeamento entre a ocupação do imóvel e a ocupação da planta está em
`application/use_cases_avaliacao.py::ocupacao_do_imovel`.

## Testes relacionados

- [tests/unit/test_tel_bairro_use_cases.py](../../../tests/unit/test_tel_bairro_use_cases.py) — 15 testes do agregado Bairro.
- [tests/unit/test_tel_logradouro_use_cases.py](../../../tests/unit/test_tel_logradouro_use_cases.py) — 12 testes do agregado Logradouro.
- [tests/unit/test_tel_planta_use_cases.py](../../../tests/unit/test_tel_planta_use_cases.py) — 19 testes da planta genérica de valores.
- [tests/unit/test_tel_geo_use_cases.py](../../../tests/unit/test_tel_geo_use_cases.py) — 16 testes de georreferenciamento.
- [tests/integration/test_tel_seeds.py](../../../tests/integration/test_tel_seeds.py) — 5 testes de idempotência do seed DEMO.
- [scripts/seed_tel.py](../../../scripts/seed_tel.py) — carga DEMO (`--dry-run`, `--limpar`).

## Qualidade estática (2026-09-29)

- `ruff check src/modules/sigmun_territorial/` — **All checks passed**.
- `mypy src/modules/sigmun_territorial/` — **Success: no issues found in 38 source files**.

## Limites e manutenção

- A referência entre o DOM-IMO e este domínio é por identificador opaco, sem FK entre schemas.
- Revalidar este índice ao alterar código, routers ou correspondência DOM. Não promover scaffolding, propostas MOD ou relações candidatas a implementação aprovada.

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-09-29 | Criação do índice a partir da implementação do DOM-TEL (Fase IX.2) | Equipe SIGMUN |
