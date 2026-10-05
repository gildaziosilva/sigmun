# 013 – Modelo-de-Dados – Desenvolvimento Econômico

#### Modelo-de-Dados – Desenvolvimento Econômico

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-DEC-013

**Domínio:** Desenvolvimento Econômico

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Desenvolvimento-Economico.md`
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

Este artefato descreve **o modelo de dados** do domínio Desenvolvimento Econômico (`DOM-DEC`) em caráter **proposto**. O conteúdo técnico e de negócio deverá ser validado antes da implementação.

---

# 2. Tabelas no schema `dec`

### empreendimentos (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<NN>> | NOT NULL |
| pessoa_id : TEXT | opcional |
| nome : TEXT <<NN>> | NOT NULL |
| setor : TEXT <<NN>> | NOT NULL |
| porte : TEXT <<NN>> | NOT NULL |
| bairro_id : TEXT | opcional |
| data_abertura : DATE | opcional |
| situacao : TEXT <<NN>> | NOT NULL |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### participacoes_programa (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| programa_id : TEXT <<NN>> | NOT NULL |
| empreendimento_id : TEXT <<NN>> | NOT NULL |
| data_ingresso : DATE <<NN>> | NOT NULL |
| situacao : TEXT <<NN>> | NOT NULL |
| resultado : TEXT | opcional |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### programas_desenvolvimento (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| objetivo : TEXT <<NN>> | NOT NULL |
| publico : TEXT | opcional |
| orcamento : FLOAT <<NN>> | NOT NULL |
| situacao : TEXT <<NN>> | NOT NULL |
| data_inicio : DATE | opcional |
| data_fim : DATE | opcional |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### projetos_investimento (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<NN>> | NOT NULL |
| empreendimento_id : TEXT <<NN>> | NOT NULL |
| descricao : TEXT <<NN>> | NOT NULL |
| investimento_previsto : FLOAT <<NN>> | NOT NULL |
| empregos_previstos : INTEGER <<NN>> | NOT NULL |
| empregos_realizados : INTEGER | opcional |
| situacao : TEXT <<NN>> | NOT NULL |
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

**Documento:** 013-Desenvolvimento-Economico-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
