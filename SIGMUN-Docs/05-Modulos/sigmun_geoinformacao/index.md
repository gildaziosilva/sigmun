# sigmun_geoinformacao — índice do módulo

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
| Data de Criação | 29/09/2026 |
| Última Revisão | 29/09/2026 |
| Próxima Revisão | Ao alterar código, routers ou correspondência DOM |
| Aprovado por | Aprovação não registrada |

**Documento(s) Relacionado(s):** [Documentação geral](../../index.md) · [Catálogo de módulos](../index.md) · [Matriz DOM ↔ módulo](../../01-Arquitetura-Corporativa/031-Matriz-de-Correspondencia-DOM-MOD.md)

## Identidade e estado observado

- Código-fonte: [sigmun_geoinformacao](../../../src/modules/sigmun_geoinformacao).
- Domínio: [DOM-GEO](../../DOM-GEO/index.md) — Geoinformação Municipal.
- MOD **confirmado**: `MOD-GEO` (promovido a confirmado em 2026-09-29).
- Correspondência: **Confirmada**, após conciliação dos artefatos `001`–`026` com o escopo implementado.
- Maturidade: **Implementada**. Módulo com entidades, regras de negócio, casos de uso, repositórios SQLAlchemy, schemas e router registrado em `src/main.py`.
- Escopo: mapas SIG (geoportal municipal), camadas cartográficas, composição mapa↔camada, elementos geoespaciais (pontos de interesse) e serviços geoespaciais publicados (WMS/WFS/WMTS/XYZ).

## Regras de negócio

| Regra | Descrição |
| --- | --- |
| RN-GEO-001 | O código da camada de mapa é único no geoportal municipal. |
| RN-GEO-002 | O código do mapa SIG é único no geoportal municipal. |
| RN-GEO-003 | O elemento geoespacial exige geometria suportada, coordenadas no intervalo do datum e vértices consistentes com o tipo de geometria. |
| RN-GEO-004 | O mapa obedece ao ciclo RASCUNHO → PUBLICADO → ARQUIVADO; a publicação exige ao menos uma camada ativa e mapas publicados não aceitam nova composição. |
| RN-GEO-005 | Extensão (bbox), SRID e níveis de zoom são validados no mapa, na camada e no serviço geoespacial. |
| RN-GEO-006 | A camada de mapa obedece ao ciclo RASCUNHO → ATIVA → DESATIVADA; camadas ativas exigem URL quando o formato é de serviço. |
| RN-GEO-007 | O serviço geoespacial exige URL válida e, em WMS/WFS, o nome da camada publicada. |
| RN-GEO-008 | Todo elemento geoespacial pertence a uma camada cadastrada e todo mapa publicado é composto por camadas cadastradas. |

## Estrutura técnica

- [domain](../../../src/modules/sigmun_geoinformacao/domain) — entidades e regras (RN-GEO-001 a RN-GEO-008)
- [application](../../../src/modules/sigmun_geoinformacao/application) — ports e casos de uso
- [infrastructure](../../../src/modules/sigmun_geoinformacao/infrastructure) — modelos ORM (schema `geo`), repositórios e seed DEMO
- [presentation](../../../src/modules/sigmun_geoinformacao/presentation) — schemas e endpoints

## APIs e ponto de entrada

Router `sigmun_geoinformacao` registrado em [src/main.py](../../../src/main.py), prefixo `/api/v1/geo` (**16 paths**): camadas (incluindo ativar/desativar), mapas SIG (incluindo publicar/arquivar e a composição mapa↔camada), elementos geoespaciais e serviços geoespaciais.

Persistência: schema `geo`, migração `alembic/versions/20260929_03_dom_geo_models.py`.

## Testes relacionados

- `tests/unit/test_geo_camada_use_cases.py` — cadastro, ciclo de vida e exclusão de camadas
- `tests/unit/test_geo_mapa_use_cases.py` — mapas, composição e publicação
- `tests/unit/test_geo_feature_servico_use_cases.py` — elementos geoespaciais e serviços
- `tests/unit/geo_fixtures.py` — fixtures compartilhadas
- `tests/integration/test_geo_obr_openapi.py` — exposição dos domínios no OpenAPI

## Frontend

Módulo `Geoinformação` em [frontend/admin/src/pages/geo](../../../frontend/admin/src/pages/geo), com abas de visão geral, camadas, mapas SIG, elementos e serviços.

## Limites e manutenção

Revalidar este índice ao alterar código, routers ou correspondência DOM. Não promover scaffolding, propostas MOD ou relações candidatas a implementação aprovada.

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-09-29 | Criação do índice; implementação do DOM-GEO (Mapas SIG) | Equipe SIGMUN |
| 1.2 | 2026-09-29 | Artefatos `001`-`026` do domínio detalhados a partir da implementação; correspondência DOM promovida a confirmada | Equipe SIGMUN |
