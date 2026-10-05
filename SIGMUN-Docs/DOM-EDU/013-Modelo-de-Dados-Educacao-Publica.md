# 013 – Modelo-de-Dados – Educação Pública

#### Modelo-de-Dados – Educação Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-EDU-013

**Domínio:** Educação Pública

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Educacao-Publica.md`
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

Este artefato detalha **o modelo de dados** do domínio Educação Pública (`DOM-EDU`), com base na implementação material identificada em `src/modules/sigmun_educacao` e no conteúdo de negócio declarado no gerador.

---

# 2. Tabelas no schema `edu`

### alunos (`AlunoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| nome : TEXT <<NN>> | NOT NULL |
| cpf : TEXT | opcional |
| data_nascimento : TEXT | opcional |
| sexo : TEXT <<NN>> | NOT NULL |
| nome_mae : TEXT | opcional |
| telefone : TEXT | opcional |
| endereco : TEXT | opcional |
| status : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### distribuicoes_merenda (`DistribuicaoMerendaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| matricula_id : TEXT <<NN>> | NOT NULL |
| item_id : TEXT <<NN>> | NOT NULL |
| quantidade : FLOAT <<NN>> | NOT NULL |
| data : DATE | opcional |
| refeicao : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : TEXT | opcional |

### itens_merenda (`ItemMerendaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| nome : TEXT <<NN>> | NOT NULL |
| tipo : TEXT <<NN>> | NOT NULL |
| estoque : FLOAT <<NN>> | NOT NULL |
| estoque_minimo : FLOAT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### lancamentos_diario (`LancamentoDiarioModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| matricula_id : TEXT <<NN>> | NOT NULL |
| data : DATE | opcional |
| presente : BOOLEAN <<NN>> | NOT NULL |
| nota : FLOAT | opcional |
| observacao : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : TEXT | opcional |

### matriculas (`MatriculaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| aluno_id : TEXT <<NN>> | NOT NULL |
| escola : TEXT <<NN>> | NOT NULL |
| serie : TEXT <<NN>> | NOT NULL |
| turno : TEXT <<NN>> | NOT NULL |
| ano_letivo : INTEGER <<NN>> | NOT NULL |
| data_matricula : DATE | opcional |
| status : TEXT <<NN>> | NOT NULL |
| escola_destino : TEXT | opcional |
| motivo : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |

### passagens_transporte (`PassagemTransporteModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| rota_id : TEXT <<NN>> | NOT NULL |
| matricula_id : TEXT <<NN>> | NOT NULL |
| data : DATE | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : TEXT | opcional |

### rotas_transporte (`RotaTransporteModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| identificacao : TEXT <<NN>> | NOT NULL |
| veiculo : TEXT | opcional |
| motorista : TEXT <<NN>> | NOT NULL |
| vagas : INTEGER <<NN>> | NOT NULL |
| turno : TEXT <<NN>> | NOT NULL |
| status : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 013-Educacao-Publica-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
