# 013 – Modelo-de-Dados – Atendimento ao Cidadão

#### Modelo-de-Dados – Atendimento ao Cidadão

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ATE-013

**Domínio:** Atendimento ao Cidadão

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Atendimento-ao-Cidadao.md`
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

Este artefato detalha **o modelo de dados** do domínio Atendimento ao Cidadão (`DOM-ATE`), com base na implementação material identificada em `src/modules/sigmun_ate` e no conteúdo de negócio declarado no gerador.

---

# 2. Tabelas no schema `ate`

### atendimentos (`AtendimentoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| chamada_id : UUID <<NN>> | NOT NULL |
| canal_id : UUID <<NN>> | NOT NULL |
| inicio : DATETIME | opcional |
| fim : DATETIME | opcional |
| status : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : TEXT | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : TEXT | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : TEXT | opcional |

### avaliacoes_atendimento (`AvaliacaoAtendimentoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| atendimento_id : UUID <<NN>> | NOT NULL |
| nota : INTEGER <<NN>> | NOT NULL |
| comentario : TEXT | opcional |
| data_hora : DATETIME <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : TEXT | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : TEXT | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : TEXT | opcional |

### canais_atendimento (`CanalAtendimentoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| tipo : TEXT <<NN>> | NOT NULL |
| ativo : BOOLEAN <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : TEXT | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : TEXT | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : TEXT | opcional |

### chamadas (`ChamadaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| senha_id : UUID <<NN>> | NOT NULL |
| guiche_id : UUID <<NN>> | NOT NULL |
| unidade_id : UUID <<NN>> | NOT NULL |
| operador : TEXT <<NN>> | NOT NULL |
| data_hora : DATETIME <<NN>> | NOT NULL |
| ordem : INTEGER <<NN>> | NOT NULL |
| tentativa : INTEGER <<NN>> | NOT NULL |
| resultado : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : TEXT | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : TEXT | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : TEXT | opcional |

### encaminhamentos (`EncaminhamentoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| atendimento_id : UUID <<NN>> | NOT NULL |
| data_hora : DATETIME <<NN>> | NOT NULL |
| destino : TEXT <<NN>> | NOT NULL |
| motivo : TEXT <<NN>> | NOT NULL |
| status : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : TEXT | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : TEXT | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : TEXT | opcional |

### eventos_outbox (`EventoOutboxModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| topico : TEXT <<NN>> | NOT NULL |
| evento_nome : TEXT <<NN>> | NOT NULL |
| agregado_tipo : TEXT <<NN>> | NOT NULL |
| agregado_id : TEXT <<NN>> | NOT NULL |
| payload : JSON <<NN>> | NOT NULL |
| status : TEXT <<NN>> | NOT NULL |
| tentativas : INTEGER <<NN>> | NOT NULL |
| ultimo_erro : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| published_at : DATETIME | opcional |

### filas_atendimento (`FilaAtendimentoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| unidade_id : UUID <<NN>> | NOT NULL |
| servico_id : UUID <<NN>> | NOT NULL |
| data : DATETIME <<NN>> | NOT NULL |
| status : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : TEXT | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : TEXT | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : TEXT | opcional |

### guiches (`GuicheModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| unidade_id : UUID <<NN>> | NOT NULL |
| numero : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| ativo : BOOLEAN <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : TEXT | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : TEXT | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : TEXT | opcional |

### senhas (`SenhaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| fila_id : UUID <<NN>> | NOT NULL |
| servico_id : UUID <<NN>> | NOT NULL |
| triagem_id : UUID <<NN>> | NOT NULL |
| numero : TEXT <<NN>> | NOT NULL |
| data_hora_emissao : DATETIME <<NN>> | NOT NULL |
| prioridade : INTEGER <<NN>> | NOT NULL |
| status : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : TEXT | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : TEXT | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : TEXT | opcional |

### servicos_atendimento (`ServicoAtendimentoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| prioridade : INTEGER <<NN>> | NOT NULL |
| ativo : BOOLEAN <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : TEXT | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : TEXT | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : TEXT | opcional |

### triagens (`TriagemModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| servico_id : UUID <<NN>> | NOT NULL |
| data_hora : DATETIME <<NN>> | NOT NULL |
| classificacao : TEXT <<NN>> | NOT NULL |
| prioridade : INTEGER <<NN>> | NOT NULL |
| observacao : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : TEXT | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : TEXT | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : TEXT | opcional |

### unidades_atendimento (`UnidadeAtendimentoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| ativo : BOOLEAN <<NN>> | NOT NULL |
| max_rechamadas : INTEGER <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : TEXT | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : TEXT | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : TEXT | opcional |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 013-Atendimento-ao-Cidadao-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
