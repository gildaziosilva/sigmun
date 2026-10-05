# 013 – Modelo-de-Dados – Indicadores e Desempenho

#### Modelo-de-Dados – Indicadores e Desempenho

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IND-013

**Domínio:** Indicadores e Desempenho

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Indicadores-e-Desempenho.md`
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

Este artefato descreve **o modelo de dados** do domínio Indicadores e Desempenho (`DOM-IND`) em caráter **proposto**. O conteúdo técnico e de negócio deverá ser validado antes da implementação.

---

# 2. Tabelas no schema `ind`

### coletas_indicador (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| indicador_id : TEXT <<NN>> | NOT NULL |
| exercicio : INTEGER <<NN>> | NOT NULL |
| periodo : TEXT <<NN>> | NOT NULL |
| valor : FLOAT <<NN>> | NOT NULL |
| fonte : TEXT <<NN>> | NOT NULL |
| data_coleta : DATE <<NN>> | NOT NULL |
| validado : BOOLEAN <<NN>> | NOT NULL |
| observacao : TEXT | opcional |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### indicadores (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| categoria : TEXT <<NN>> | NOT NULL |
| formula : TEXT <<NN>> | NOT NULL |
| unidade : TEXT <<NN>> | NOT NULL |
| periodicidade : TEXT <<NN>> | NOT NULL |
| fonte_ref : TEXT <<NN>> | NOT NULL |
| responsavel : TEXT <<NN>> | NOT NULL |
| situacao : TEXT <<NN>> | NOT NULL |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### metas_indicador (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| indicador_id : TEXT <<NN>> | NOT NULL |
| exercicio : INTEGER <<NN>> | NOT NULL |
| valor_base : FLOAT | opcional |
| valor_alvo : FLOAT <<NN>> | NOT NULL |
| prazo : DATE <<NN>> | NOT NULL |
| responsavel : TEXT | opcional |
| situacao : TEXT <<NN>> | NOT NULL |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### paineis (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| publico : BOOLEAN <<NN>> | NOT NULL |
| periodicidade : TEXT <<NN>> | NOT NULL |
| situacao : TEXT <<NN>> | NOT NULL |
| ultimo_atualizacao : TIMESTAMPTZ | opcional |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 013-Indicadores-e-Desempenho-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
