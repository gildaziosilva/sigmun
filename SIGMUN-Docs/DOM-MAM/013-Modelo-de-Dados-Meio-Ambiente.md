# 013 – Modelo-de-Dados – Meio Ambiente

#### Modelo-de-Dados – Meio Ambiente

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-MAM-013

**Domínio:** Meio Ambiente

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Meio-Ambiente.md`
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

Este artefato descreve **o modelo de dados** do domínio Meio Ambiente (`DOM-MAM`) em caráter **proposto**. O conteúdo técnico e de negócio deverá ser validado antes da implementação.

---

# 2. Tabelas no schema `mam`

### areas_protegidas (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| categoria : TEXT <<NN>> | NOT NULL |
| area_km2 : FLOAT <<NN>> | NOT NULL |
| nivel_protecao : TEXT <<NN>> | NOT NULL |
| bairro_id : TEXT | opcional |
| situacao : TEXT <<NN>> | NOT NULL |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### fiscalizacoes_ambientais (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| numero : TEXT <<NN>> | NOT NULL |
| licenca_id : TEXT | opcional |
| data : DATE <<NN>> | NOT NULL |
| agente : TEXT <<NN>> | NOT NULL |
| objeto : TEXT <<NN>> | NOT NULL |
| resultado : TEXT <<NN>> | NOT NULL |
| prazo_adequacao : DATE | opcional |
| situacao : TEXT <<NN>> | NOT NULL |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### licencimentos_ambientais (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| numero : TEXT <<NN>> | NOT NULL |
| empreendimento : TEXT <<NN>> | NOT NULL |
| tipo : TEXT <<NN>> | NOT NULL |
| atividade : TEXT <<NN>> | NOT NULL |
| situacao : TEXT <<NN>> | NOT NULL |
| data_emissao : DATE | opcional |
| validade_ate : DATE | opcional |
| condicoes : TEXT | opcional |
| created_at : TIMESTAMPTZ <<NN>> | NOT NULL |
| updated_at : TIMESTAMPTZ | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### monitoramentos_ambientais (``)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| licenca_id : TEXT | opcional |
| parametro : TEXT <<NN>> | NOT NULL |
| data : DATE <<NN>> | NOT NULL |
| valor : FLOAT <<NN>> | NOT NULL |
| unidade : TEXT <<NN>> | NOT NULL |
| limite_legal : FLOAT | opcional |
| conformidade : TEXT <<NN>> | NOT NULL |
| observacao : TEXT | opcional |
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

**Documento:** 013-Meio-Ambiente-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
