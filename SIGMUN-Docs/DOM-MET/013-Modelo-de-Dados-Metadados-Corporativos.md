# 013 – Modelo-de-Dados – Metadados Corporativos

#### Modelo-de-Dados – Metadados Corporativos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-MET-013

**Domínio:** Metadados Corporativos

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Metadados-Corporativos.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `030-Roadmap-de-Implementacao-dos-Dominios.md`
* `Mapa-de-Dominios.md`

---


# 1. Finalidade

Este artefato detalha **o modelo de dados** do domínio Metadados Corporativos (`DOM-MET`), com base na implementação material identificada em `src/modules/sigmun_met` e no conteúdo de negócio declarado no gerador.

---

# 2. Tabelas no schema `met`

### classificacoes (`ClassificacaoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<UQ, NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| tipo : TEXT <<NN>> | NOT NULL |
| nivel : INTEGER <<NN>> | NOT NULL |
| cor : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : UUID | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : UUID | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : UUID | opcional |

### metadados (`MetadadoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<UQ, NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| tipo_dado : TEXT <<NN>> | NOT NULL |
| obrigatorio : BOOLEAN <<NN>> | NOT NULL |
| multi_valor : BOOLEAN <<NN>> | NOT NULL |
| aplicavel_a : TEXT <<NN>> | NOT NULL |
| valor_padrao : TEXT | opcional |
| status : TEXT <<NN>> | NOT NULL |
| config : JSON | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : UUID | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : UUID | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : UUID | opcional |

### taxonomias (`TaxonomiaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<UQ, NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| termos_ids : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : UUID | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : UUID | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : UUID | opcional |

### termos_taxonomias (`TermoTaxonomiaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| taxonomia_id : UUID <<NN>> | NOT NULL |
| termo_pai_id : UUID | opcional |
| codigo : TEXT <<NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| sinonimos : TEXT <<NN>> | NOT NULL |
| ordem : INTEGER <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : UUID | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : UUID | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : UUID | opcional |

### valores_metadados (`ValorMetadadoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| metadado_id : UUID <<NN>> | NOT NULL |
| entidade_tipo : TEXT <<NN>> | NOT NULL |
| entidade_id : UUID <<NN>> | NOT NULL |
| valor : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : UUID | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : UUID | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : UUID | opcional |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 013-Metadados-Corporativos-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
