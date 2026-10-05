# 013 – Modelo-de-Dados – Assistência Social

#### Modelo-de-Dados – Assistência Social

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ASS-013

**Domínio:** Assistência Social

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Assistencia-Social.md`
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

Este artefato detalha **o modelo de dados** do domínio Assistência Social (`DOM-ASS`), com base na implementação material identificada em `src/modules/sigmun_assistencia_social` e no conteúdo de negócio declarado no gerador.

---

# 2. Tabelas no schema `ass`

### atendimentos_sociais (`AtendimentoSocialModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| pessoa_id : TEXT <<NN>> | NOT NULL |
| unidade_id : TEXT <<NN>> | NOT NULL |
| tipo : TEXT <<NN>> | NOT NULL |
| data : DATE | opcional |
| descricao : TEXT | opcional |
| encaminhamento : TEXT | opcional |
| profissional : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : TEXT | opcional |

### beneficios_eventuais (`BeneficioEventualModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| familia_id : TEXT <<NN>> | NOT NULL |
| tipo : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| valor : FLOAT <<NN>> | NOT NULL |
| quantidade : INTEGER <<NN>> | NOT NULL |
| data_solicitacao : DATETIME <<NN>> | NOT NULL |
| data_aprovacao : DATETIME | opcional |
| data_entrega : DATETIME | opcional |
| status : TEXT <<NN>> | NOT NULL |
| unidade_id : TEXT | opcional |
| observacao : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |

### familias_cadunico (`FamiliaCadUnicoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| nis : TEXT <<UQ, NN>> | NOT NULL |
| responsavel_nome : TEXT <<NN>> | NOT NULL |
| responsavel_cpf : TEXT | opcional |
| endereco : TEXT | opcional |
| telefone : TEXT | opcional |
| renda_per_capita : FLOAT <<NN>> | NOT NULL |
| quantidade_pessoas : INTEGER <<NN>> | NOT NULL |
| status : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### pessoas_cadunico (`PessoaCadUnicoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| familia_id : TEXT <<NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| cpf : TEXT <<UQ, NN>> | NOT NULL |
| data_nascimento : TEXT | opcional |
| sexo : TEXT <<NN>> | NOT NULL |
| nome_mae : TEXT | opcional |
| parentesco : TEXT | opcional |
| escolaridade : TEXT | opcional |
| ocupacao : TEXT | opcional |
| renda : FLOAT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### unidades_assistencia (`UnidadeAssistenciaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<UQ, NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| tipo : TEXT <<NN>> | NOT NULL |
| endereco : TEXT | opcional |
| telefone : TEXT | opcional |
| email : TEXT | opcional |
| responsavel : TEXT | opcional |
| status : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
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

**Documento:** 013-Assistencia-Social-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
