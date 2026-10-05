# 013 – Modelo-de-Dados – Segurança da Informação

#### Modelo-de-Dados – Segurança da Informação

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-SEG-013

**Domínio:** Segurança da Informação

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Seguranca-da-Informacao.md`
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

Este artefato detalha **o modelo de dados** do domínio Segurança da Informação (`DOM-SEG`), com base na implementação material identificada em `src/modules/sigmun_seg` e no conteúdo de negócio declarado no gerador.

---

# 2. Tabelas no schema `seg`

### chaves_criptograficas (`ChaveCriptograficaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| nome : TEXT <<NN>> | NOT NULL |
| algoritmo : TEXT <<NN>> | NOT NULL |
| tipo : TEXT <<NN>> | NOT NULL |
| tamanho_bits : INTEGER <<NN>> | NOT NULL |
| status : TEXT <<NN>> | NOT NULL |
| data_expiracao : DATETIME | opcional |
| responsavel_id : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME <<NN>> | NOT NULL |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### controles_seguranca (`ControleSegurancaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<UQ, NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| tipo : TEXT <<NN>> | NOT NULL |
| categoria : TEXT <<NN>> | NOT NULL |
| status : TEXT <<NN>> | NOT NULL |
| nivel_risco : TEXT <<NN>> | NOT NULL |
| responsavel_id : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME <<NN>> | NOT NULL |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### credenciais (`CredencialModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| usuario_id : TEXT <<NN>> | NOT NULL |
| tipo : TEXT <<NN>> | NOT NULL |
| identificador : TEXT <<NN>> | NOT NULL |
| status : TEXT <<NN>> | NOT NULL |
| validade : DATETIME | opcional |
| ultimo_uso : DATETIME | opcional |
| tentativas_falhas : INTEGER <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME <<NN>> | NOT NULL |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### incidentes_seguranca (`IncidenteSegurancaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| titulo : TEXT <<NN>> | NOT NULL |
| descricao : TEXT <<NN>> | NOT NULL |
| severidade : TEXT <<NN>> | NOT NULL |
| impacto : TEXT | opcional |
| categoria : TEXT | opcional |
| relator_id : TEXT | opcional |
| atribuido_a : TEXT | opcional |
| status : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME <<NN>> | NOT NULL |
| data_resolucao : DATETIME | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### politicas_seguranca (`PoliticaSegurancaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<UQ, NN>> | NOT NULL |
| titulo : TEXT <<NN>> | NOT NULL |
| conteudo : TEXT <<NN>> | NOT NULL |
| versao : TEXT <<NN>> | NOT NULL |
| aprovador_id : TEXT | opcional |
| data_aprovacao : DATETIME | opcional |
| data_revisao : DATETIME | opcional |
| ativa : BOOLEAN <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME <<NN>> | NOT NULL |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 013-Seguranca-da-Informacao-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
