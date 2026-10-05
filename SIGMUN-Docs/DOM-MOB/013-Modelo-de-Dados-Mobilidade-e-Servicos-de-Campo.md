# 013 – Modelo-de-Dados – Mobilidade e Serviços de Campo

#### Modelo-de-Dados – Mobilidade e Serviços de Campo

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-MOB-013

**Domínio:** Mobilidade e Serviços de Campo

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`
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

Este artefato descreve **o modelo de dados** do domínio Mobilidade e Serviços de Campo (`DOM-MOB`) em caráter **proposto**. O conteúdo técnico e de negócio deverá ser validado antes da implementação.

---

# 2. Tabelas no schema `mob`

### dispositivos_moveis (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<NN>> | NOT NULL |
| identificador : TEXT <<NN>> | NOT NULL |
| modelo : TEXT | opcional |
| pessoa_id : TEXT | opcional |
| versao_app : TEXT | opcional |
| ultimo_acesso : TIMESTAMPTZ | opcional |
| sincronizado_em : TIMESTAMPTZ | opcional |
| situacao : TEXT <<NN>> | NOT NULL |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### evidencias_campo (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| ordem_id : TEXT <<NN>> | NOT NULL |
| tipo : TEXT <<NN>> | NOT NULL |
| arquivo_ref : TEXT | opcional |
| latitude : FLOAT <<NN>> | NOT NULL |
| longitude : FLOAT <<NN>> | NOT NULL |
| data_captura : TIMESTAMPTZ <<NN>> | NOT NULL |
| hash : TEXT | opcional |
| sincronizada : BOOLEAN <<NN>> | NOT NULL |
| observacao : TEXT | opcional |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### ordens_campo (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| numero : TEXT <<NN>> | NOT NULL |
| titulo : TEXT <<NN>> | NOT NULL |
| tipo : TEXT <<NN>> | NOT NULL |
| dispositivo_id : TEXT | opcional |
| responsavel_id : TEXT | opcional |
| bairro_id : TEXT | opcional |
| prioridade : INTEGER <<NN>> | NOT NULL |
| situacao : TEXT <<NN>> | NOT NULL |
| data_abertura : DATE <<NN>> | NOT NULL |
| data_conclusao : DATE | opcional |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### sincronizacoes (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| dispositivo_id : TEXT <<NN>> | NOT NULL |
| data_inicio : TIMESTAMPTZ <<NN>> | NOT NULL |
| data_fim : TIMESTAMPTZ | opcional |
| registros_enviados : INTEGER <<NN>> | NOT NULL |
| registros_recebidos : INTEGER | opcional |
| conflitos : INTEGER <<NN>> | NOT NULL |
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

**Documento:** 013-Mobilidade-e-Servicos-de-Campo-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
