# 013 – Modelo-de-Dados – Saúde Pública

#### Modelo-de-Dados – Saúde Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-SAU-013

**Domínio:** Saúde Pública

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Saude-Publica.md`
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

Este artefato detalha **o modelo de dados** do domínio Saúde Pública (`DOM-SAU`), com base na implementação material identificada em `src/modules/sigmun_saude` e no conteúdo de negócio declarado no gerador.

---

# 2. Tabelas no schema `sau`

### agendamentos (`AgendamentoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| paciente_id : TEXT <<NN>> | NOT NULL |
| especialidade : TEXT <<NN>> | NOT NULL |
| data : DATE | opcional |
| hora : TEXT | opcional |
| estabelecimento : TEXT | opcional |
| status : TEXT <<NN>> | NOT NULL |
| motivo_cancelamento : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |

### atendimentos (`AtendimentoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| paciente_id : TEXT <<NN>> | NOT NULL |
| data : DATE | opcional |
| tipo : TEXT <<NN>> | NOT NULL |
| profissional : TEXT <<NN>> | NOT NULL |
| estabelecimento : TEXT <<NN>> | NOT NULL |
| queixa : TEXT | opcional |
| conduta : TEXT | opcional |
| cid10 : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : TEXT | opcional |

### dispensacoes (`DispensacaoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| paciente_id : TEXT <<NN>> | NOT NULL |
| medicamento_id : TEXT <<NN>> | NOT NULL |
| quantidade : FLOAT <<NN>> | NOT NULL |
| data : DATE | opcional |
| receita : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : TEXT | opcional |

### medicamentos (`MedicamentoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| nome : TEXT <<NN>> | NOT NULL |
| apresentacao : TEXT | opcional |
| estoque : FLOAT <<NN>> | NOT NULL |
| estoque_minimo : FLOAT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### pacientes (`PacienteModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| nome : TEXT <<NN>> | NOT NULL |
| cns : TEXT <<UQ, NN>> | NOT NULL |
| cpf : TEXT | opcional |
| data_nascimento : TEXT | opcional |
| sexo : TEXT <<NN>> | NOT NULL |
| nome_mae : TEXT | opcional |
| telefone : TEXT | opcional |
| endereco : TEXT | opcional |
| ubs_referencia : TEXT | opcional |
| status : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### regulacoes (`RegulacaoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| paciente_id : TEXT <<NN>> | NOT NULL |
| procedimento : TEXT <<NN>> | NOT NULL |
| prioridade : TEXT <<NN>> | NOT NULL |
| solicitante : TEXT | opcional |
| data_solicitacao : DATE | opcional |
| status : TEXT <<NN>> | NOT NULL |
| justificativa : TEXT | opcional |
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

**Documento:** 013-Saude-Publica-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
