# 013 – Modelo de Dados – Geoinformação Municipal

#### Modelo de Dados – Geoinformação Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GEO-013

**Domínio:** Geoinformação Municipal

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Geoinformacao-Municipal.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000C-HIERARQUIA-DOCUMENTAL.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `030-Roadmap-de-Implementacao-dos-Dominios.md`
* `Mapa-de-Dominios.md`
* `Modelo-Logico.md`
* `Modelo-Fisico.md`
* `Dicionario-de-dados.md`

---

# 1. Finalidade

Este artefato descreve o modelo de dados do domínio de Geoinformação Municipal: entidades,
atributos, tipos, restrições e valores admissíveis.

---

# 2. Convenções

* O domínio utiliza banco relacional com schema próprio (`{'codigo': 'DOM-GEO', 'dominio': 'Geoinformação Municipal', 'modulo': 'sigmun_geoinformacao', 'schema': 'geo', 'prefixo': '/api/v1/geo', 'migracao': 'alembic/versions/20260929_03_dom_geo_models.py', 'migracao_id': '20260929_03_dom_geo_models', 'rotulo': 'Geoinformação Municipal', 'prefixo_regra': 'GEO', 'entidades': [('CamadaMapa', 'Camada cartográfica disponibilizada no geoportal.'), ('MapaSig', 'Mapa publicado no geoportal municipal.'), ('MapaCamada', 'Vínculo de composição entre mapa e camada.'), ('FeatureGeo', 'Elemento geoespacial (ponto de interesse) de uma camada.'), ('ServicoGeo', 'Serviço geoespacial publicado (WMS, WFS, WMTS, XYZ ou REST).')], 'variaveis': (('Tipos de camada', 'ortofoto, hipsometria, hipsografia, topografia, hidrografia, uso_solo, vegetacao, malha_urbana, infraestrutura, cadastro_territorial, outro'), ('Formatos de camada', 'geotiff, shapefile, geojson, kml, postgis, wms, wfs, wmts, xyz, vetorial'), ('Situações da camada', 'rascunho, ativa, desativada'), ('Tipos de mapa', 'tematico, cadastral, basemap, infraestrutura, ambiental, outro'), ('Situações do mapa', 'rascunho, publicado, arquivado'), ('Protocolos de serviço', 'wms, wfs, wmts, xyz, rest'), ('Situações do serviço', 'ativo, inativo, manutencao'), ('Datuns', 'sirgas2000, sad69, wgs84'), ('Geometrias', 'ponto, linha, poligono'))}`).
* Chaves primárias são UUID v4 gerados pela aplicação.
* Campos de auditoria (`created_at`, `created_by`, `updated_at`) são comuns às
  entidades submetidas a exclusão lógica.
* **Não há chave estrangeira física entre schemas de domínios**; as referências
  entre domínios são feitas por identificador opaco, conforme o contrato de
  integração.

---

# 3. Entidades

### CamadaMapa — Camada cartográfica disponibilizada no geoportal.

**Tabela:** `geo.camadas_mapa`

| Coluna | Tipo | Padrão |
| --- | | --- | |
| `id` | UUID, PK | — |
| `codigo` | TEXT, NOT NULL, UNIQUE | — |
| `nome` | TEXT, NOT NULL | — |
| `descricao` | TEXT | — |
| `tipo` | TEXT, NOT NULL | outro |
| `formato` | TEXT, NOT NULL | geojson |
| `fonte` | TEXT | — |
| `data_atualizacao` | DATE, NOT NULL | — |
| `datum` | TEXT, NOT NULL | sirgas2000 |
| `srid` | INTEGER, NOT NULL | 4326 |
| `url_servico` | TEXT | — |
| `zoom_minimo` | INTEGER, NOT NULL | 0 |
| `zoom_maximo` | INTEGER, NOT NULL | 24 |
| `visivel` | BOOLEAN, NOT NULL | true() |
| `situacao` | TEXT, NOT NULL | rascunho |
| `created_at` | DATETIME, NOT NULL | now() |
| `updated_at` | DATETIME | — |
| `created_by` | TEXT | — |
| `is_deleted` | BOOLEAN, NOT NULL | false() |


### MapaSig — Mapa publicado no geoportal municipal.

**Tabela:** `geo.mapas_sig`

| Coluna | Tipo | Padrão |
| --- | | --- | |
| `id` | UUID, PK | — |
| `codigo` | TEXT, NOT NULL, UNIQUE | — |
| `nome` | TEXT, NOT NULL | — |
| `descricao` | TEXT | — |
| `tipo` | TEXT, NOT NULL | tematico |
| `situacao` | TEXT, NOT NULL | rascunho |
| `datum` | TEXT, NOT NULL | sirgas2000 |
| `srid` | INTEGER, NOT NULL | 4326 |
| `escala_denominador` | INTEGER, NOT NULL | 0 |
| `zoom_inicial` | INTEGER, NOT NULL | 13 |
| `zoom_minimo` | INTEGER, NOT NULL | 0 |
| `zoom_maximo` | INTEGER, NOT NULL | 24 |
| `lat_min` | FLOAT | — |
| `lon_min` | FLOAT | — |
| `lat_max` | FLOAT | — |
| `lon_max` | FLOAT | — |
| `publicado_em` | DATETIME | — |
| `criado_por` | TEXT | — |
| `created_at` | DATETIME, NOT NULL | now() |
| `updated_at` | DATETIME | — |
| `created_by` | TEXT | — |
| `is_deleted` | BOOLEAN, NOT NULL | false() |


### MapaCamada — Vínculo de composição entre mapa e camada.

**Tabela:** `geo.mapas_camadas`

| Coluna | Tipo | Padrão |
| --- | | --- | |
| `id` | UUID, PK | — |
| `mapa_id` | TEXT, NOT NULL | — |
| `camada_id` | TEXT, NOT NULL | — |
| `ordem` | INTEGER, NOT NULL | 0 |
| `opacidade` | FLOAT, NOT NULL | 100 |
| `visivel` | BOOLEAN, NOT NULL | true() |
| `rotulo` | TEXT | — |
| `created_at` | DATETIME, NOT NULL | now() |
| `created_by` | TEXT | — |
| `is_deleted` | BOOLEAN, NOT NULL | false() |


### FeatureGeo — Elemento geoespacial (ponto de interesse) de uma camada.

**Tabela:** `geo.features_geo`

| Coluna | Tipo | Padrão |
| --- | | --- | |
| `id` | UUID, PK | — |
| `codigo` | TEXT, NOT NULL | — |
| `nome` | TEXT, NOT NULL | — |
| `descricao` | TEXT | — |
| `camada_id` | TEXT, NOT NULL | — |
| `geometria` | TEXT, NOT NULL | ponto |
| `latitude` | FLOAT, NOT NULL | 0 |
| `longitude` | FLOAT, NOT NULL | 0 |
| `vertices` | JSON | — |
| `datum` | TEXT, NOT NULL | sirgas2000 |
| `atributos` | JSON | — |
| `criado_por` | TEXT | — |
| `created_at` | DATETIME, NOT NULL | now() |
| `updated_at` | DATETIME | — |
| `created_by` | TEXT | — |
| `is_deleted` | BOOLEAN, NOT NULL | false() |


### ServicoGeo — Serviço geoespacial publicado (WMS, WFS, WMTS, XYZ ou REST).

**Tabela:** `geo.servicos_geo`

| Coluna | Tipo | Padrão |
| --- | | --- | |
| `id` | UUID, PK | — |
| `codigo` | TEXT, NOT NULL, UNIQUE | — |
| `nome` | TEXT, NOT NULL | — |
| `descricao` | TEXT | — |
| `tipo` | TEXT, NOT NULL | wms |
| `situacao` | TEXT, NOT NULL | ativo |
| `url` | TEXT | — |
| `camada` | TEXT | — |
| `datum` | TEXT, NOT NULL | sirgas2000 |
| `srid` | INTEGER, NOT NULL | 4326 |
| `zoom_minimo` | INTEGER, NOT NULL | 0 |
| `zoom_maximo` | INTEGER, NOT NULL | 24 |
| `publico` | BOOLEAN, NOT NULL | false() |
| `created_at` | DATETIME, NOT NULL | now() |
| `updated_at` | DATETIME | — |
| `created_by` | TEXT | — |
| `is_deleted` | BOOLEAN, NOT NULL | false() |


---

# 4. Domínios de Valor

* **Tipos de camada:** ortofoto, hipsometria, hipsografia, topografia, hidrografia, uso_solo, vegetacao, malha_urbana, infraestrutura, cadastro_territorial, outro
* **Formatos de camada:** geotiff, shapefile, geojson, kml, postgis, wms, wfs, wmts, xyz, vetorial
* **Situações da camada:** rascunho, ativa, desativada
* **Tipos de mapa:** tematico, cadastral, basemap, infraestrutura, ambiental, outro
* **Situações do mapa:** rascunho, publicado, arquivado
* **Protocolos de serviço:** wms, wfs, wmts, xyz, rest
* **Situações do serviço:** ativo, inativo, manutencao
* **Datuns:** sirgas2000, sad69, wgs84
* **Geometrias:** ponto, linha, poligono

---

# 5. Índices e Restrições

| Tabela | Restrição | Regra |
| --- | | --- | |
| `geo.camadas_mapa` | UNIQUE | — |
| `geo.mapas_sig` | UNIQUE | — |
| `geo.servicos_geo` | UNIQUE | — |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 013-Modelo-de-Dados-Geoinformacao-Municipal.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_geoinformacao`. Alterações no código devem ser
> refletidas reexecutando o gerador.
