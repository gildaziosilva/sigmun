# 013 – Modelo de Dados – Cadastro Imobiliário

#### Modelo de Dados – Cadastro Imobiliário

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IMO-013

**Domínio:** Cadastro Imobiliário

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Cadastro-Imobiliario.md`
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

Este artefato descreve o modelo de dados do domínio de Cadastro Imobiliário: entidades,
atributos, tipos, restrições e valores admissíveis.

---

# 2. Convenções

* O domínio utiliza banco relacional com schema próprio (`{'codigo': 'DOM-IMO', 'dominio': 'Cadastro Imobiliário', 'modulo': 'sigmun_cadastro_imobiliario', 'schema': 'imo', 'prefixo': '/api/v1/imo', 'migracao': 'alembic/versions/20260929_02_dom_imo_models.py', 'migracao_id': '20260929_02_dom_imo_models', 'rotulo': 'Cadastro Imobiliário', 'prefixo_regra': 'IMO', 'entidades': [('Imovel', 'Unidade imobiliária (lote) com inscrição definitiva.'), ('ProprietarioImovel', 'Vínculo de titularidade entre pessoa e imóvel.'), ('AvaliacaoImovel', 'Avaliação do valor venal para um exercício.'), ('CaracteristicaImovel', 'Característica construtiva do imóvel.'), ('GeometriaImovel', 'Geometria georreferenciada do lote.')], 'variaveis': (('Tipos de imóvel', 'lote, casa, apartamento, loja, galpao, terreno, outro'), ('Situações do imóvel', 'ativo, inativo, em_obra, desocupado, demolido'), ('Tipos de propriedade', 'proprio, alugado, cedido, invencionado'), ('Vínculos', 'titular, comodato, arrendamento, usufruto, parceiro'), ('Naturezas da obra', 'residencial, comercial, industrial, institucional, mista, nao_aplicavel'), ('Situações da avaliação', 'rascunho, concluida, cancelada'), ('Datuns', 'sirgas2000, sad69, wgs84'), ('Geometrias', 'ponto, linha, poligono'))}`).
* Chaves primárias são UUID v4 gerados pela aplicação.
* Campos de auditoria (`created_at`, `created_by`, `updated_at`) são comuns às
  entidades submetidas a exclusão lógica.
* **Não há chave estrangeira física entre schemas de domínios**; as referências
  entre domínios são feitas por identificador opaco, conforme o contrato de
  integração.

---

# 3. Entidades

### Imovel — Unidade imobiliária (lote) com inscrição definitiva.

**Tabela:** `imo.imoveis`

| Coluna | Tipo | Padrão |
| --- | | --- | |
| `id` | UUID, PK | — |
| `inscricao_imobiliaria` | TEXT, NOT NULL, UNIQUE | — |
| `logradouro_id` | TEXT, NOT NULL | — |
| `bairro_id` | TEXT, NOT NULL | — |
| `numero` | TEXT | — |
| `complemento` | TEXT | — |
| `tipo` | TEXT, NOT NULL | lote |
| `situacao` | TEXT, NOT NULL | ativo |
| `tipo_propriedade` | TEXT, NOT NULL | proprio |
| `area_terreno_m2` | FLOAT, NOT NULL | 0 |
| `area_construida_m2` | FLOAT, NOT NULL | 0 |
| `ano_construcao` | INTEGER | — |
| `created_at` | DATETIME, NOT NULL | now() |
| `updated_at` | DATETIME | — |
| `created_by` | TEXT | — |
| `is_deleted` | BOOLEAN, NOT NULL | false() |


### ProprietarioImovel — Vínculo de titularidade entre pessoa e imóvel.

**Tabela:** `imo.proprietarios_imoveis`

| Coluna | Tipo | Padrão |
| --- | | --- | |
| `id` | UUID, PK | — |
| `imovel_id` | TEXT, NOT NULL | — |
| `pessoa_id` | TEXT | — |
| `nome` | TEXT, NOT NULL | — |
| `cpf` | TEXT, NOT NULL | — |
| `vinculo` | TEXT, NOT NULL | titular |
| `principal` | BOOLEAN, NOT NULL | false() |
| `created_at` | DATETIME, NOT NULL | now() |
| `updated_at` | DATETIME | — |
| `created_by` | TEXT | — |
| `is_deleted` | BOOLEAN, NOT NULL | false() |


### AvaliacaoImovel — Avaliação do valor venal para um exercício.

**Tabela:** `imo.avaliacoes_imoveis`

| Coluna | Tipo | Padrão |
| --- | | --- | |
| `id` | UUID, PK | — |
| `imovel_id` | TEXT, NOT NULL | — |
| `ano` | INTEGER, NOT NULL | — |
| `valor_terreno_m2_unitario` | FLOAT, NOT NULL | 0 |
| `valor_construcao_m2_unitario` | FLOAT, NOT NULL | 0 |
| `aliquota_percent` | FLOAT, NOT NULL | 0 |
| `area_terreno_m2` | FLOAT, NOT NULL | 0 |
| `area_construida_m2` | FLOAT, NOT NULL | 0 |
| `situacao` | TEXT, NOT NULL | rascunho |
| `data_avaliacao` | DATE, NOT NULL | — |
| `created_at` | DATETIME, NOT NULL | now() |
| `updated_at` | DATETIME | — |
| `created_by` | TEXT | — |
| `is_deleted` | BOOLEAN, NOT NULL | false() |


### CaracteristicaImovel — Característica construtiva do imóvel.

**Tabela:** `imo.caracteristicas_imoveis`

| Coluna | Tipo | Padrão |
| --- | | --- | |
| `id` | UUID, PK | — |
| `imovel_id` | TEXT, NOT NULL | — |
| `obra` | TEXT, NOT NULL | residencial |
| `numero_pavimentos` | INTEGER, NOT NULL | 1 |
| `ano_renovacao` | INTEGER | — |
| `observacao` | TEXT | — |
| `created_at` | DATETIME, NOT NULL | now() |
| `updated_at` | DATETIME | — |
| `created_by` | TEXT | — |


### GeometriaImovel — Geometria georreferenciada do lote.

**Tabela:** `imo.geometrias_imoveis`

| Coluna | Tipo | Padrão |
| --- | | --- | |
| `id` | UUID, PK | — |
| `imovel_id` | TEXT, NOT NULL | — |
| `geometria` | TEXT, NOT NULL | ponto |
| `latitude` | FLOAT, NOT NULL | 0 |
| `longitude` | FLOAT, NOT NULL | 0 |
| `vertices` | JSON | — |
| `datum` | TEXT, NOT NULL | sirgas2000 |
| `precisao_m` | FLOAT, NOT NULL | 0 |
| `data_levantamento` | DATE, NOT NULL | — |
| `created_at` | DATETIME, NOT NULL | now() |
| `updated_at` | DATETIME | — |
| `created_by` | TEXT | — |
| `is_deleted` | BOOLEAN, NOT NULL | false() |


---

# 4. Domínios de Valor

* **Tipos de imóvel:** lote, casa, apartamento, loja, galpao, terreno, outro
* **Situações do imóvel:** ativo, inativo, em_obra, desocupado, demolido
* **Tipos de propriedade:** proprio, alugado, cedido, invencionado
* **Vínculos:** titular, comodato, arrendamento, usufruto, parceiro
* **Naturezas da obra:** residencial, comercial, industrial, institucional, mista, nao_aplicavel
* **Situações da avaliação:** rascunho, concluida, cancelada
* **Datuns:** sirgas2000, sad69, wgs84
* **Geometrias:** ponto, linha, poligono

---

# 5. Índices e Restrições

| Tabela | Restrição | Regra |
| --- | | --- | |
| `imo.imoveis` | UNIQUE | RN-IMO-001 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 013-Modelo-de-Dados-Cadastro-Imobiliario.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_cadastro_imobiliario`. Alterações no código devem ser
> refletidas reexecutando o gerador.
