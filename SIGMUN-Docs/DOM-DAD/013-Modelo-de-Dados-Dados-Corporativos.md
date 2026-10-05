# 013 – Modelo-de-Dados – Dados Corporativos

#### Modelo-de-Dados – Dados Corporativos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-DAD-013

**Domínio:** Dados Corporativos

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Dados-Corporativos.md`
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

Este artefato detalha **o modelo de dados** do domínio Dados Corporativos (`DOM-DAD`), com base na implementação material identificada em `src/modules/sigmun_dad` e no conteúdo de negócio declarado no gerador.

---

# 2. Tabelas no schema `dad`

### ativos_dados (`AtivoDadoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| nome : TEXT <<UQ, NN>> | NOT NULL |
| descricao : TEXT | opcional |
| tipo : TEXT <<NN>> | NOT NULL |
| status : TEXT <<NN>> | NOT NULL |
| qualidade : TEXT <<NN>> | NOT NULL |
| dono_id : TEXT | opcional |
| steward_id : TEXT | opcional |
| schema_origem : TEXT | opcional |
| tabela_origem : TEXT | opcional |
| classificacao : TEXT | opcional |
| tags : TEXT <<NN>> | NOT NULL |
| metadata : JSON | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : UUID | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : UUID | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : UUID | opcional |

### catalogos (`CatalogoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| nome : TEXT <<UQ, NN>> | NOT NULL |
| descricao : TEXT | opcional |
| dominio : TEXT | opcional |
| ativos_ids : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : UUID | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : UUID | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : UUID | opcional |

### linhagens (`LinhagemDadoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| ativo_origem_id : UUID <<NN>> | NOT NULL |
| ativo_destino_id : UUID <<NN>> | NOT NULL |
| tipo_transformacao : TEXT | opcional |
| descricao : TEXT | opcional |
| regras : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : UUID | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : UUID | opcional |

### politicas (`PoliticaDadoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<UQ, NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| tipo : TEXT | opcional |
| regras : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : UUID | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : UUID | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : UUID | opcional |

### qualidade_dados (`QualidadeDadoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| ativo_id : UUID <<NN>> | NOT NULL |
| nivel : TEXT <<NN>> | NOT NULL |
| score : FLOAT <<NN>> | NOT NULL |
| criterios : TEXT <<NN>> | NOT NULL |
| observacao : TEXT | opcional |
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

**Documento:** 013-Dados-Corporativos-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
