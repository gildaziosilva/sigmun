# 013 – Modelo-de-Dados – Gestão de Pessoas

#### Modelo-de-Dados – Gestão de Pessoas

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-PES-013

**Domínio:** Gestão de Pessoas

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-de-Pessoas.md`
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

Este artefato detalha **o modelo de dados** do domínio Gestão de Pessoas (`DOM-PES`), com base na implementação material identificada em `src/modules/sigmun_rh` e no conteúdo de negócio declarado no gerador.

---

# 2. Tabelas no schema `rh`

### cargos (`CargoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<UQ, NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| nivel : TEXT <<NN>> | NOT NULL |
| salario_base : FLOAT <<NN>> | NOT NULL |
| carga_horaria_semanal : INTEGER <<NN>> | NOT NULL |
| ativo : BOOLEAN <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### ferias (`FeriasModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| servidor_id : TEXT <<NN>> | NOT NULL |
| periodo_aquisitivo_inicio : DATE | opcional |
| periodo_aquisitivo_fim : DATE | opcional |
| data_inicio_gozo : DATE | opcional |
| data_fim_gozo : DATE | opcional |
| dias : INTEGER <<NN>> | NOT NULL |
| parcela : INTEGER <<NN>> | NOT NULL |
| status : TEXT <<NN>> | NOT NULL |
| data_aprovacao : DATETIME | opcional |
| data_cancelamento : DATETIME | opcional |
| motivo_cancelamento : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### folhas_pagamento (`FolhaPagamentoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| competencia_ano : INTEGER <<NN>> | NOT NULL |
| competencia_mes : INTEGER <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| status : TEXT <<NN>> | NOT NULL |
| total_proventos : FLOAT <<NN>> | NOT NULL |
| total_descontos : FLOAT <<NN>> | NOT NULL |
| total_liquido : FLOAT <<NN>> | NOT NULL |
| quantidade_servidores : INTEGER <<NN>> | NOT NULL |
| data_fechamento : DATETIME | opcional |
| data_homologacao : DATETIME | opcional |
| data_pagamento : DATETIME | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |
| updated_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### frequencias (`FrequenciaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| servidor_id : VARCHAR(36) <<NN>> | NOT NULL |
| data : DATE <<NN>> | NOT NULL |
| tipo : TEXT <<NN>> | NOT NULL |
| hora_entrada : TIME | opcional |
| hora_saida : TIME | opcional |
| minutos_atraso : INTEGER <<NN>> | NOT NULL |
| justificativa : TEXT | opcional |
| desconto_folha : BOOLEAN <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### lotacoes (`LotacaoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| servidor_id : TEXT <<NN>> | NOT NULL |
| unidade_id : TEXT <<NN>> | NOT NULL |
| cargo_id : TEXT | opcional |
| data_inicio : DATE | opcional |
| data_fim : DATE | opcional |
| vigente : BOOLEAN <<NN>> | NOT NULL |
| motivo : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### servidores (`ServidorModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| matricula : TEXT <<UQ, NN>> | NOT NULL |
| cpf : VARCHAR(11) <<UQ, NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| cargo_id : TEXT <<NN>> | NOT NULL |
| tipo_vinculo : TEXT <<NN>> | NOT NULL |
| status : TEXT <<NN>> | NOT NULL |
| data_admissao : DATE | opcional |
| data_desligamento : DATE | opcional |
| salario : FLOAT <<NN>> | NOT NULL |
| email : TEXT | opcional |
| telefone : TEXT | opcional |
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

**Documento:** 013-Gestao-de-Pessoas-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
