# 013 – Modelo de Dados – Gestão Territorial

#### Modelo de Dados – Gestão Territorial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TEL-013

**Domínio:** Gestão Territorial

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-Territorial.md`
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

Este artefato descreve o modelo de dados do domínio de Gestão Territorial: entidades,
atributos, tipos, restrições e valores admissíveis.

---

# 2. Convenções

* O domínio utiliza banco relacional com schema próprio (`{'codigo': 'DOM-TEL', 'dominio': 'Gestão Territorial', 'modulo': 'sigmun_territorial', 'schema': 'tel', 'prefixo': '/api/v1/tel', 'migracao': 'alembic/versions/20260929_01_dom_tel_models.py', 'migracao_id': '20260929_01_dom_tel_models', 'rotulo': 'Gestão Territorial', 'prefixo_regra': 'TEL', 'entidades': [('Bairro', 'Divisão territorial (bairro, distrito, setor ou zona rural).'), ('Logradouro', 'Logradouro público vinculado a uma divisão territorial.'), ('PlantaGenericaValores', 'Valores unitários por ano, divisão e ocupação.'), ('Georreferencia', 'Georreferência de bairro ou logradouro.')], 'variaveis': (('Tipos de divisão', 'bairro, distrito, setor, zona_rural'), ('Tipos de logradouro', 'rua, avenida, travessa, praca, rodovia, estrada, alameda, parque, outro'), ('Situações de divisão', 'ativo, inativo'), ('Situações de logradouro', 'ativo, em_obra, inativo'), ('Ocupações', 'residencial, comercial, industrial, institucional, misto, terreno'), ('Situações da planta', 'rascunho, vigente, revogada'), ('Datuns', 'sirgas2000, sad69, wgs84'), ('Geometrias', 'ponto, linha, poligono'))}`).
* Chaves primárias são UUID v4 gerados pela aplicação.
* Campos de auditoria (`created_at`, `created_by`, `updated_at`) são comuns às
  entidades submetidas a exclusão lógica.
* **Não há chave estrangeira física entre schemas de domínios**; as referências
  entre domínios são feitas por identificador opaco, conforme o contrato de
  integração.

---

# 3. Entidades

### Bairro — Divisão territorial (bairro, distrito, setor ou zona rural).

**Tabela:** `tel.bairros`

| Coluna | Tipo | Padrão |
| --- | | --- | |
| `id` | UUID, PK | — |
| `codigo` | TEXT, NOT NULL, UNIQUE | — |
| `nome` | TEXT, NOT NULL | — |
| `tipo` | TEXT, NOT NULL | bairro |
| `populacao_estimada` | INTEGER, NOT NULL | 0 |
| `area_km2` | FLOAT, NOT NULL | 0 |
| `situacao` | TEXT, NOT NULL | ativo |
| `created_at` | DATETIME, NOT NULL | now() |
| `updated_at` | DATETIME | — |
| `created_by` | TEXT | — |
| `is_deleted` | BOOLEAN, NOT NULL | false() |


### Logradouro — Logradouro público vinculado a uma divisão territorial.

**Tabela:** `tel.logradouros`

| Coluna | Tipo | Padrão |
| --- | | --- | |
| `id` | UUID, PK | — |
| `codigo` | TEXT, NOT NULL, UNIQUE | — |
| `nome` | TEXT, NOT NULL | — |
| `tipo` | TEXT, NOT NULL | rua |
| `bairro_id` | TEXT, NOT NULL | — |
| `cep` | TEXT | — |
| `numero_inicial` | INTEGER, NOT NULL | 0 |
| `numero_final` | INTEGER, NOT NULL | 0 |
| `situacao` | TEXT, NOT NULL | ativo |
| `created_at` | DATETIME, NOT NULL | now() |
| `updated_at` | DATETIME | — |
| `created_by` | TEXT | — |
| `is_deleted` | BOOLEAN, NOT NULL | false() |


### PlantaGenericaValores — Valores unitários por ano, divisão e ocupação.

**Tabela:** `tel.planta_generica_valores`

| Coluna | Tipo | Padrão |
| --- | | --- | |
| `id` | UUID, PK | — |
| `ano` | INTEGER, NOT NULL | — |
| `bairro_id` | TEXT, NOT NULL | — |
| `ocupacao` | TEXT, NOT NULL | residencial |
| `valor_terreno_m2` | FLOAT, NOT NULL | 0 |
| `valor_construcao_m2` | FLOAT, NOT NULL | 0 |
| `aliquota_percent` | FLOAT, NOT NULL | 0 |
| `situacao` | TEXT, NOT NULL | rascunho |
| `legislacao` | TEXT | — |
| `created_at` | DATETIME, NOT NULL | now() |
| `updated_at` | DATETIME | — |
| `created_by` | TEXT | — |
| `is_deleted` | BOOLEAN, NOT NULL | false() |


### Georreferencia — Georreferência de bairro ou logradouro.

**Tabela:** `tel.georreferencias`

| Coluna | Tipo | Padrão |
| --- | | --- | |
| `id` | UUID, PK | — |
| `bairro_id` | TEXT | — |
| `logradouro_id` | TEXT | — |
| `geometria` | TEXT, NOT NULL | ponto |
| `latitude` | FLOAT, NOT NULL | 0 |
| `longitude` | FLOAT, NOT NULL | 0 |
| `altitude_m` | FLOAT | — |
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

* **Tipos de divisão:** bairro, distrito, setor, zona_rural
* **Tipos de logradouro:** rua, avenida, travessa, praca, rodovia, estrada, alameda, parque, outro
* **Situações de divisão:** ativo, inativo
* **Situações de logradouro:** ativo, em_obra, inativo
* **Ocupações:** residencial, comercial, industrial, institucional, misto, terreno
* **Situações da planta:** rascunho, vigente, revogada
* **Datuns:** sirgas2000, sad69, wgs84
* **Geometrias:** ponto, linha, poligono

---

# 5. Índices e Restrições

| Tabela | Restrição | Regra |
| --- | | --- | |
| `tel.bairros` | UNIQUE | RN-TEL-001 |
| `tel.logradouros` | UNIQUE | RN-TEL-002 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 013-Modelo-de-Dados-Gestao-Territorial.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_territorial`. Alterações no código devem ser
> refletidas reexecutando o gerador.
