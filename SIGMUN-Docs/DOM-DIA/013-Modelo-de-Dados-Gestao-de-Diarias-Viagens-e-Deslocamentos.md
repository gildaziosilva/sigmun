# 013 – Modelo-de-Dados – Gestão de Diárias, Viagens e Deslocamentos

#### Modelo-de-Dados – Gestão de Diárias, Viagens e Deslocamentos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-DIA-013

**Domínio:** Gestão de Diárias, Viagens e Deslocamentos

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`
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

Este artefato detalha **o modelo de dados** do domínio Gestão de Diárias, Viagens e Deslocamentos (`DOM-DIA`), com base na implementação material identificada em `src/modules/sigmun_dia` e no conteúdo de negócio declarado no gerador.

---

# 2. Tabelas no schema `dia`

### diarias (`DiariaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| viagem_id : TEXT <<NN>> | NOT NULL |
| servidor_id : TEXT <<NN>> | NOT NULL |
| dota_id : TEXT <<NN>> | NOT NULL |
| categoria : TEXT <<NN>> | NOT NULL |
| descricao : TEXT <<NN>> | NOT NULL |
| data_inicio : DATETIME | opcional |
| data_fim : DATETIME | opcional |
| valor_diaria : FLOAT <<NN>> | NOT NULL |
| valor_total : FLOAT <<NN>> | NOT NULL |
| status : TEXT <<NN>> | NOT NULL |
| data_solicitacao : DATETIME <<NN>> | NOT NULL |
| data_autorizacao : DATETIME | opcional |
| data_calculo : DATETIME | opcional |
| data_concessao : DATETIME | opcional |
| data_inicio_prestacao : DATETIME | opcional |
| data_fim_prestacao : DATETIME | opcional |
| data_pagamento : DATETIME | opcional |
| data_aprovacao : DATETIME | opcional |
| data_glosa : DATETIME | opcional |
| data_restituicao : DATETIME | opcional |
| data_cancelamento : DATETIME | opcional |
| motivo_cancelamento : TEXT <<NN>> | NOT NULL |
| motivo_glosa : TEXT <<NN>> | NOT NULL |
| valor_glosado : FLOAT <<NN>> | NOT NULL |
| documento_prestacao_id : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT <<NN>> | NOT NULL |
| updated_by : TEXT <<NN>> | NOT NULL |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### eventos_diarias (`EventoDiariaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| diaria_id : TEXT <<NN>> | NOT NULL |
| status_anterior : TEXT <<NN>> | NOT NULL |
| status_posterior : TEXT <<NN>> | NOT NULL |
| usuario_id : TEXT <<NN>> | NOT NULL |
| motivo : TEXT <<NN>> | NOT NULL |
| data_evento : DATETIME <<NN>> | NOT NULL |
| detalhes : TEXT <<NN>> | NOT NULL |

### prestacoes_contas (`PrestacaoContasModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| diaria_id : TEXT <<NN>> | NOT NULL |
| servidor_id : TEXT <<NN>> | NOT NULL |
| dota_id : TEXT <<NN>> | NOT NULL |
| data_emissao : DATETIME <<NN>> | NOT NULL |
| data_vencimento : DATETIME | opcional |
| documento_id : TEXT <<NN>> | NOT NULL |
| valor_previsto : FLOAT <<NN>> | NOT NULL |
| valor_apresentado : FLOAT <<NN>> | NOT NULL |
| valor_glosado : FLOAT <<NN>> | NOT NULL |
| valor_liquido : FLOAT <<NN>> | NOT NULL |
| status : TEXT <<NN>> | NOT NULL |
| motivo_glosa : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT <<NN>> | NOT NULL |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### viagens (`ViagemModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| servidor_id : TEXT <<NN>> | NOT NULL |
| dota_id : TEXT <<NN>> | NOT NULL |
| motivo : TEXT <<NN>> | NOT NULL |
| cargo_ocupado : TEXT <<NN>> | NOT NULL |
| unidade_origem_id : TEXT <<NN>> | NOT NULL |
| unidade_destino_id : TEXT <<NN>> | NOT NULL |
| data_inicio : DATETIME | opcional |
| data_fim : DATETIME | opcional |
| destino : TEXT <<NN>> | NOT NULL |
| is_antecipacao : BOOLEAN <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT <<NN>> | NOT NULL |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 013-Gestao-de-Diarias-Viagens-e-Deslocamentos-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
