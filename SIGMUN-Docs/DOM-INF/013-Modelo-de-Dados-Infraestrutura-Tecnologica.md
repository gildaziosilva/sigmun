# 013 – Modelo-de-Dados – Infraestrutura Tecnológica

#### Modelo-de-Dados – Infraestrutura Tecnológica

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-INF-013

**Domínio:** Infraestrutura Tecnológica

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Infraestrutura-Tecnologica.md`
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

Este artefato descreve **o modelo de dados** do domínio Infraestrutura Tecnológica (`DOM-INF`) em caráter **proposto**. O conteúdo técnico e de negócio deverá ser validado antes da implementação.

---

# 2. Tabelas no schema `inf`

### ambientes_infraestrutura (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| tipo : TEXT <<NN>> | NOT NULL |
| responsavel : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| situacao : TEXT <<NN>> | NOT NULL |
| ultimo_check : TIMESTAMPTZ | opcional |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### incidentes_infraestrutura (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| numero : TEXT <<NN>> | NOT NULL |
| titulo : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| recurso_id : TEXT | opcional |
| severidade : TEXT <<NN>> | NOT NULL |
| aberto_em : TIMESTAMPTZ <<NN>> | NOT NULL |
| fechado_em : TIMESTAMPTZ | opcional |
| responsavel : TEXT <<NN>> | NOT NULL |
| situacao : TEXT <<NN>> | NOT NULL |
| causa : TEXT | opcional |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### monitoramentos_infraestrutura (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| recurso_id : TEXT <<NN>> | NOT NULL |
| metrica : TEXT <<NN>> | NOT NULL |
| valor : FLOAT <<NN>> | NOT NULL |
| unidade : TEXT <<NN>> | NOT NULL |
| limite : FLOAT | opcional |
| status : TEXT <<NN>> | NOT NULL |
| coletado_em : TIMESTAMPTZ <<NN>> | NOT NULL |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### recursos_infraestrutura (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| tipo : TEXT <<NN>> | NOT NULL |
| ambiente_id : TEXT <<NN>> | NOT NULL |
| capacidade : TEXT | opcional |
| provedor : TEXT | opcional |
| identificador_externo : TEXT | opcional |
| situacao : TEXT <<NN>> | NOT NULL |
| data_aquisicao : DATE | opcional |
| garantia_ate : DATE | opcional |
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

**Documento:** 013-Infraestrutura-Tecnologica-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
