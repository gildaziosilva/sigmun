# 013 – Modelo-de-Dados – Gestão de Competências

#### Modelo-de-Dados – Gestão de Competências

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CPT-013

**Domínio:** Gestão de Competências

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-de-Competencias.md`
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

Este artefato descreve **o modelo de dados** do domínio Gestão de Competências (`DOM-CPT`) em caráter **proposto**. O conteúdo técnico e de negócio deverá ser validado antes da implementação.

---

# 2. Tabelas no schema `cpt`

### avaliacoes_competencia (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| pessoa_id : TEXT <<NN>> | NOT NULL |
| competencia_id : TEXT <<NN>> | NOT NULL |
| nivel_atual : FLOAT <<NN>> | NOT NULL |
| nivel_esperado : FLOAT <<NN>> | NOT NULL |
| avaliador : TEXT <<NN>> | NOT NULL |
| data_avaliacao : DATE <<NN>> | NOT NULL |
| observacao : TEXT | opcional |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### capacitacoes (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| modalidade : TEXT <<NN>> | NOT NULL |
| carga_horativa : INTEGER <<NN>> | NOT NULL |
| situacao : TEXT <<NN>> | NOT NULL |
| data_inicio : DATE | opcional |
| data_fim : DATE | opcional |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### competencias (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| categoria : TEXT <<NN>> | NOT NULL |
| nivel_referencia : FLOAT <<NN>> | NOT NULL |
| situacao : TEXT <<NN>> | NOT NULL |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### planos_desenvolvimento (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| pessoa_id : TEXT <<NN>> | NOT NULL |
| titulo : TEXT <<NN>> | NOT NULL |
| competencia_id : TEXT <<NN>> | NOT NULL |
| capacitacao_id : TEXT | opcional |
| acao : TEXT <<NN>> | NOT NULL |
| prazo : DATE <<NN>> | NOT NULL |
| situacao : TEXT <<NN>> | NOT NULL |
| resultado : TEXT | opcional |
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

**Documento:** 013-Gestao-de-Competencias-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
