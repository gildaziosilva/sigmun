# 013 – Modelo-de-Dados – Analytics e Inteligência

#### Modelo-de-Dados – Analytics e Inteligência

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ANA-013

**Domínio:** Analytics e Inteligência

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Analytics-e-Inteligencia.md`
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

Este artefato descreve **o modelo de dados** do domínio Analytics e Inteligência (`DOM-ANA`) em caráter **proposto**. O conteúdo técnico e de negócio deverá ser validado antes da implementação.

---

# 2. Tabelas no schema `ana`

### analises (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<NN>> | NOT NULL |
| titulo : TEXT <<NN>> | NOT NULL |
| fonte_id : TEXT <<NN>> | NOT NULL |
| modelo_id : TEXT | opcional |
| responsavel : TEXT <<NN>> | NOT NULL |
| data_execucao : DATE <<NN>> | NOT NULL |
| resultado : TEXT | opcional |
| visibilidade : TEXT <<NN>> | NOT NULL |
| situacao : TEXT <<NN>> | NOT NULL |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### fontes_analiticas (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| tipo : TEXT <<NN>> | NOT NULL |
| referencia : TEXT <<NN>> | NOT NULL |
| periodicidade : TEXT <<NN>> | NOT NULL |
| ultima_atualizacao : TIMESTAMPTZ | opcional |
| situacao : TEXT <<NN>> | NOT NULL |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### modelos_analiticos (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| tipo : TEXT <<NN>> | NOT NULL |
| tecnologia : TEXT <<NN>> | NOT NULL |
| versao : TEXT <<NN>> | NOT NULL |
| metrica : TEXT <<NN>> | NOT NULL |
| treinado_em : DATE <<NN>> | NOT NULL |
| situacao : TEXT <<NN>> | NOT NULL |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### recomendacoes (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| analise_id : TEXT <<NN>> | NOT NULL |
| destinatario : TEXT <<NN>> | NOT NULL |
| recomendacao : TEXT <<NN>> | NOT NULL |
| prioridade : TEXT <<NN>> | NOT NULL |
| data : DATE <<NN>> | NOT NULL |
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

**Documento:** 013-Analytics-e-Inteligencia-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
