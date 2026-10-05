# 013 – Modelo-de-Dados – Cadastro Único Municipal

#### Modelo-de-Dados – Cadastro Único Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CUM-013

**Domínio:** Cadastro Único Municipal

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Cadastro-Unico-Municipal.md`
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

Este artefato detalha **o modelo de dados** do domínio Cadastro Único Municipal (`DOM-CUM`), com base na implementação material identificada em `src/modules/sigmun_cadastro` e no conteúdo de negócio declarado no gerador.

---

# 2. Tabelas no schema `core`

### contatos (`ContatoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| pessoa_id : UUID <<NN>> | NOT NULL |
| tipo : TEXT <<NN>> | NOT NULL |
| valor : TEXT <<NN>> | NOT NULL |
| principal : BOOLEAN <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : UUID | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : UUID | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : UUID | opcional |

### documentos (`DocumentoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| pessoa_id : UUID <<NN>> | NOT NULL |
| tipo : TEXT <<NN>> | NOT NULL |
| numero : TEXT <<NN>> | NOT NULL |
| orgao_emissor : TEXT | opcional |
| data_emissao : DATE | opcional |
| data_validade : DATE | opcional |
| principal : BOOLEAN <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : UUID | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : UUID | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : UUID | opcional |

### enderecos (`EnderecoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| pessoa_id : UUID <<NN>> | NOT NULL |
| tipo : TEXT <<NN>> | NOT NULL |
| logradouro : TEXT <<NN>> | NOT NULL |
| numero : TEXT <<NN>> | NOT NULL |
| complemento : TEXT | opcional |
| bairro : TEXT | opcional |
| cep : TEXT | opcional |
| cidade : TEXT | opcional |
| estado : TEXT | opcional |
| pais : TEXT | opcional |
| principal : BOOLEAN <<NN>> | NOT NULL |
| vigencia_inicio : DATETIME <<NN>> | NOT NULL |
| vigencia_fim : DATETIME | opcional |
| motivo_alteracao : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : UUID | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : UUID | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : UUID | opcional |

### pessoas (`PessoaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| tipo : TEXT <<NN>> | NOT NULL |
| categoria : TEXT <<NN>> | NOT NULL |
| unidade_id : UUID | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : UUID | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : UUID | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : UUID | opcional |

### pessoas_fisicas (`PessoaFisicaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| pessoa_id : UUID <<UQ, NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| data_nascimento : DATE | opcional |
| sexo : TEXT | opcional |
| estado_civil : TEXT | opcional |
| mae : TEXT | opcional |
| pai : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : UUID | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : UUID | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : UUID | opcional |

### pessoas_juridicas (`PessoaJuridicaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| pessoa_id : UUID <<UQ, NN>> | NOT NULL |
| razao_social : TEXT <<NN>> | NOT NULL |
| nome_fantasia : TEXT | opcional |
| cnae_principal : TEXT | opcional |
| capital : NUMERIC(15, 2) | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : UUID | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : UUID | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : UUID | opcional |

### unidades_administrativas (`UnidadeAdministrativaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| unidade_pai_id : UUID | opcional |
| codigo_ibge : TEXT | opcional |
| codigo_siafi : TEXT | opcional |
| nome : TEXT <<NN>> | NOT NULL |
| sigla : TEXT | opcional |
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

**Documento:** 013-Cadastro-Unico-Municipal-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
