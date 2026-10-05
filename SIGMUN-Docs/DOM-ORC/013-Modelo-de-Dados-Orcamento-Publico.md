# 013 – Modelo-de-Dados – Orçamento Público

#### Modelo-de-Dados – Orçamento Público

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ORC-013

**Domínio:** Orçamento Público

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Orcamento-Publico.md`
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

Este artefato detalha **o modelo de dados** do domínio Orçamento Público (`DOM-ORC`), com base na implementação material identificada em `src/modules/sigmun_orc` e no conteúdo de negócio declarado no gerador.

---

# 2. Tabelas no schema `orc`

### dotacoes (`DotacaoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| loa_id : UUID <<NN>> | NOT NULL |
| exercicio : INTEGER <<NN>> | NOT NULL |
| codigo : TEXT <<NN>> | NOT NULL |
| unidade_orcamentaria : TEXT | opcional |
| natureza_despesa : TEXT | opcional |
| fonte_recursos : TEXT | opcional |
| valor_inicial : FLOAT <<NN>> | NOT NULL |
| valor_suplementado : FLOAT <<NN>> | NOT NULL |
| valor_anulado : FLOAT <<NN>> | NOT NULL |
| valor_reservado : FLOAT <<NN>> | NOT NULL |
| valor_empenhado : FLOAT <<NN>> | NOT NULL |
| status : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |
| updated_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### ldos (`LDOModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| exercicio : INTEGER <<UQ, NN>> | NOT NULL |
| ppa_id : UUID <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| status : TEXT <<NN>> | NOT NULL |
| meta_fiscal_receita : FLOAT <<NN>> | NOT NULL |
| meta_fiscal_despesa : FLOAT <<NN>> | NOT NULL |
| data_aprovacao : DATETIME | opcional |
| data_sancao : DATETIME | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |
| updated_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### loas (`LOAModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| exercicio : INTEGER <<UQ, NN>> | NOT NULL |
| ldo_id : UUID <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| status : TEXT <<NN>> | NOT NULL |
| valor_receita_prevista : FLOAT <<NN>> | NOT NULL |
| valor_despesa_fixada : FLOAT <<NN>> | NOT NULL |
| data_aprovacao : DATETIME | opcional |
| data_publicacao : DATETIME | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |
| updated_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### ppas (`PPAModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| ano_inicial : INTEGER <<NN>> | NOT NULL |
| ano_final : INTEGER <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| status : TEXT <<NN>> | NOT NULL |
| data_publicacao : DATETIME | opcional |
| data_encerramento : DATETIME | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |
| updated_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### reservas (`ReservaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| dotacao_id : UUID <<NN>> | NOT NULL |
| numero : TEXT | opcional |
| valor : FLOAT <<NN>> | NOT NULL |
| finalidade : TEXT | opcional |
| status : TEXT <<NN>> | NOT NULL |
| data_reserva : DATETIME <<NN>> | NOT NULL |
| data_conversao : DATETIME | opcional |
| data_cancelamento : DATETIME | opcional |
| motivo_cancelamento : TEXT | opcional |
| empenho_id : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |
| updated_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 013-Orcamento-Publico-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
