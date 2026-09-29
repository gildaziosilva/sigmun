# sigmun_cadastro_imobiliario — índice do módulo

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

**Documento(s) Relacionado(s):** [Documentação geral](../../index.md) · [Catálogo de módulos](../index.md) · [Matriz DOM ↔ módulo](../../01-Arquitetura-Corporativa/031-Matriz-de-Correspondencia-DOM-MOD.md) · [DOM-TEL (dependência)](../../DOM-TEL/index.md)

## Identidade e estado observado

- Código-fonte: [sigmun_cadastro_imobiliario](../../../src/modules/sigmun_cadastro_imobiliario).
- Implementação verificada em 2026-09-29 (Fase IX.2 do `TODO.md`).
- Domínio: [DOM-IMO](../../DOM-IMO/index.md).
- MOD **proposto, não aprovado**: `MOD-IMO`.
- Correspondência: **Candidata; validar escopo**.
- Maturidade: **Implementada**. Entidades, regras de negócio, casos de uso, repositórios SQLAlchemy, schemas e router registrado em `src/main.py`.
- Escopo: cadastro dos lotes (inscrição imobiliária), vínculos de propriedade, características construtivas, avaliação de valor venal e geometria georreferenciada do lote.

## Estrutura técnica

- [domain](../../../src/modules/sigmun_cadastro_imobiliario/domain) — entidades e regras (RN-IMO-001 a RN-IMO-007)
- [application](../../../src/modules/sigmun_cadastro_imobiliario/application) — ports, 17 casos de uso e contrato `ConsultaPlantaValores`
- [infrastructure](../../../src/modules/sigmun_cadastro_imobiliario/infrastructure) — modelos ORM (schema `imo`), repositórios e seed DEMO
- [presentation](../../../src/modules/sigmun_cadastro_imobiliario/presentation) — schemas e endpoints

## Regras de negócio implementadas

| Regra | Descrição | Garantia no banco |
| --- | --- | --- |
| RN-IMO-001 | A inscrição imobiliária é única no município. | `imo.imoveis.inscricao_imobiliaria` UNIQUE |
| RN-IMO-002 | O imóvel exige logradouro e bairro vinculados. | — |
| RN-IMO-003 | Áreas não podem ser negativas; ano de construção deve ser coerente. | — |
| RN-IMO-004 | Situação em `ATIVO ⇄ INATIVO`, `ATIVO → EM_OBRA/DESOCUPADO`, `EM_OBRA → ATIVO/DEMOLIDO`; `DEMOLIDO` é terminal. | — |
| RN-IMO-005 | `valor_venal = área_terreno × Vt + área_construída × Vc`; `valor_lancamento = valor_venal × alíquota`. Um exercício concluído não pode ser reavaliado. | índice único `uq_imo_avaliacao_exercicio` |
| RN-IMO-006 | No máximo um proprietário **titular principal** por imóvel; a mesma pessoa não é vinculada duas vezes; documento é CPF (11) ou CNPJ (14). | índice único parcial `uq_imo_titular_principal` |
| RN-IMO-007 | A geometria do lote exige datum suportado, coordenadas no intervalo e vértices compatíveis com o tipo de geometria. | índice único `uq_imo_geometria_lote` |


## APIs e ponto de entrada

Router `sigmun_cadastro_imobiliario` registrado em [src/main.py](../../../src/main.py), prefixo `/api/v1/imo` (**18 paths**, **25 operações**):

- **Imóveis** — `POST/GET /imoveis`, `GET /imoveis/{id}`, `GET /imoveis/inscricao/{inscricao}`, `GET /imoveis/logradouro/{id}`, `GET /imoveis/bairro/{id}`, `PATCH/DELETE /imoveis/{id}`, `POST /imoveis/{id}/situacao`
- **Proprietários** — `POST/GET /proprietarios`, `GET /imoveis/{id}/proprietarios`, `DELETE /proprietarios/{id}`
- **Avaliações** — `POST/GET /avaliacoes`, `GET /avaliacoes/{id}`, `GET /avaliacoes/imovel/{id}`, `POST /avaliacoes/{id}/concluir`, `POST /avaliacoes/{id}/cancelar`
- **Características e geometria** — `POST/GET /caracteristicas`, `GET /caracteristicas/imovel/{id}`, `POST/GET /geometrias`, `GET /geometrias/imovel/{id}`

Persistência: schema `imo`, migração `alembic/versions/20260929_02_dom_imo_models.py` (cabeça única da cadeia).

## Contrato de integração (DOM-TEL)

Sem FK entre schemas (ROADMAP §2.7). A avaliação recebe os valores unitários vigentes da planta genérica de valores, resolvidos por quem consome as duas APIs:

```
GET /api/v1/tel/plantas-valores/vigente?ano={ano}&bairro_id={bairro_id}&ocupacao={ocupacao}
```

O port `ConsultaPlantaValores` (`application/interfaces.py`) isola essa dependência e admite implementação HTTP quando a integração for remota.

## Testes relacionados

- [tests/unit/test_imo_imoveis_use_cases.py](../../../tests/unit/test_imo_imoveis_use_cases.py) — 27 testes dos agregados Imóvel e Proprietário.
- [tests/unit/test_imo_avaliacao_use_cases.py](../../../tests/unit/test_imo_avaliacao_use_cases.py) — 21 testes de avaliação de valor venal.
- [tests/unit/test_imo_geometria_use_cases.py](../../../tests/unit/test_imo_geometria_use_cases.py) — 15 testes de geometria e características.
- [tests/integration/test_imo_seeds.py](../../../tests/integration/test_imo_seeds.py) — 5 testes de idempotência do seed DEMO.
- [scripts/seed_imo.py](../../../scripts/seed_imo.py) — carga DEMO (`--dry-run`, `--limpar`).

## Qualidade estática (2026-09-29)

- `ruff check src/modules/sigmun_cadastro_imobiliario/` — **All checks passed**.
- `mypy src/modules/sigmun_cadastro_imobiliario/` — **Success: no issues found in 34 source files**.

## Limites e manutenção

- O seed do DOM-IMO exige o seed do DOM-TEL aplicado (logradouros e bairros de referência).
- Revalidar este índice ao alterar código, routers ou correspondência DOM. Não promover scaffolding, propostas MOD ou relações candidatas a implementação aprovada.

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-09-29 | Criação do índice a partir da implementação do DOM-IMO (Fase IX.2) | Equipe SIGMUN |

