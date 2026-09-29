# 003 – Mapa de Processos – Obras e Infraestrutura

#### Mapa de Processos – Obras e Infraestrutura

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OBR-003

**Domínio:** Obras e Infraestrutura

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Obras-e-Infraestrutura.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000C-HIERARQUIA-DOCUMENTAL.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `030-Roadmap-de-Implementacao-dos-Dominios.md`
* `Mapa-de-Dominios.md`
* `Modelo-Logico.md`
* `Modelo-Fisico.md`
* `Dicionario-de-dados.md`

---

# 1. Finalidade

Este artefato descreve os processos de negócio do domínio de Obras e Infraestrutura,
da intenção do ator à alteração do estado, evidenciando entradas, saídas e
regras aplicadas.

---

# 2. Convenções

* **Gatilho:** evento ou condição que dispara o processo.
* **Objetivo:** resultado pretendido pelo processo.
* **Passos:** sequência lógica; as regras de negócio aplicadas aparecem entre
  parênteses na etapa correspondente.

---

# 3. Visão Geral

| ID | Processo | Gatilho | Objetivo |
| --- | | --- | | --- | |
| PRO-OBR-001 | Cadastrar e conduzir a obra | Inclusão de obra no plano de metas, contratação, retomada, conclusão ou cancelamento. | Manter a obra com cadastro e situação coerentes e com o contrato vigente. |
| PRO-OBR-002 | Medir e conferir o avanço | Periodicidade de medição definida em contrato ou solicitação do responsável técnico. | Compor o avanço físico-financeiro da obra com base em medição conferida. |
| PRO-OBR-003 | Registrar a despesa da obra | Repasse, aquisição de material ou quitação de custo atribuível à obra. | Registrar o desembolso sem permitir pagamento acima do medido. |
| PRO-OBR-004 | Registrar etapas e vistorias | Planejamento de cronograma, avanço de frente de trabalho ou visita de fiscalização. | Manter o detalhamento físico da obra e o registro de fiscalização. |
| PRO-OBR-005 | Consultar o andamento físico-financeiro | Necessidade de acompanhamento por parte da gestão, do controle ou do cidadão. | Disponibilizar a situação consolidada do avanço da obra. |


---

# 4. Detalhamento

### PRO-OBR-001 — Cadastrar e conduzir a obra

**Gatilho:** Inclusão de obra no plano de metas, contratação, retomada, conclusão ou cancelamento.

**Objetivo:** Manter a obra com cadastro e situação coerentes e com o contrato vigente.

**Entradas:** Número; nome; tipo; contratação; recurso; valores orçado e contratado; prazos; empresa

**Saídas:** Obra cadastrada e situada no ciclo de vida

**Regras aplicadas:** RN-OBR-001, RN-OBR-002, RN-OBR-003, RN-OBR-004

**Passos:**

1. Verificar se o número da obra já está cadastrado (RN-OBR-001).
2. Informar valores, respeitando que o contratado não supera o orçado (RN-OBR-004).
3. Para iniciar a execução, exigir empresa, contratação e data prevista (RN-OBR-003).
4. Conduzir a obra pelo ciclo até a conclusão, que exige 100% do avanço físico (RN-OBR-005), ou o cancelamento.

---
### PRO-OBR-002 — Medir e conferir o avanço

**Gatilho:** Periodicidade de medição definida em contrato ou solicitação do responsável técnico.

**Objetivo:** Compor o avanço físico-financeiro da obra com base em medição conferida.

**Entradas:** Obra; número da medição; percentual físico; valor medido; responsável técnico

**Saídas:** Medição registrada, conferida, aprovada, glosada ou cancelada; obra recomposta

**Regras aplicadas:** RN-OBR-004, RN-OBR-005

**Passos:**

1. Verificar que a obra está em execução ou suspensa (RN-OBR-005).
2. Verificar a unicidade do número da medição dentro da obra e o teto do valor contratado.
3. Registrar a medição em situação registrada.
4. Na conferência, aprovar ou glosar; a aprovação recompõe o avanço da obra (RN-OBR-005).

---
### PRO-OBR-003 — Registrar a despesa da obra

**Gatilho:** Repasse, aquisição de material ou quitação de custo atribuível à obra.

**Objetivo:** Registrar o desembolso sem permitir pagamento acima do medido.

**Entradas:** Obra; medição vinculada; descrição; tipo; valor; credor; documento

**Saídas:** Despesa registrada e avanço financeiro da obra recomposto

**Regras aplicadas:** RN-OBR-004, RN-OBR-006

**Passos:**

1. Verificar que a obra está contratada ou em execução (RN-OBR-006).
2. Verificar que existe saldo medido e ainda não pago (RN-OBR-006).
3. Registrar a despesa e recompor o avanço financeiro, limitado ao avanço físico (RN-OBR-004).

---
### PRO-OBR-004 — Registrar etapas e vistorias

**Gatilho:** Planejamento de cronograma, avanço de frente de trabalho ou visita de fiscalização.

**Objetivo:** Manter o detalhamento físico da obra e o registro de fiscalização.

**Entradas:** Obra; etapa prevista e realizada; vistoria com parecer e percentual verificado

**Saídas:** Etapa registrada ou concluída; vistoria registrada com parecer

**Regras aplicadas:** RN-OBR-007, RN-OBR-008

**Passos:**

1. Cadastrar a etapa com responsável e percentual previsto (RN-OBR-007).
2. Atualizar o percentual realizado da etapa, na faixa de 0 a 100 (RN-OBR-007).
3. Concluir a etapa, o que exige 100% do previsto (RN-OBR-007).
4. Registrar a vistoria com fiscal, percentual verificado e parecer (RN-OBR-008).

---
### PRO-OBR-005 — Consultar o andamento físico-financeiro

**Gatilho:** Necessidade de acompanhamento por parte da gestão, do controle ou do cidadão.

**Objetivo:** Disponibilizar a situação consolidada do avanço da obra.

**Entradas:** Obra ou filtro de situação

**Saídas:** Obra com valores e percentuais, ou acompanhamento consolidado

**Regras aplicadas:** RN-OBR-004, RN-OBR-005, RN-OBR-006

**Passos:**

1. Informar a obra ou o filtro de situação, quando houver.
2. Retornar os indicadores de avanço físico e financeiro com paginação.
3. Para o acompanhamento detalhado, retornar medições, despesas, etapas e vistorias.

---

# 5. Processos por Capacidade

| Processo | Capacidades | Regras |
| --- | | --- | |
| PRO-OBR-001 — Cadastrar e conduzir a obra | CAP-OBR-001 | RN-OBR-001, RN-OBR-002, RN-OBR-003, RN-OBR-004 |
| PRO-OBR-002 — Medir e conferir o avanço | CAP-OBR-002 | RN-OBR-004, RN-OBR-005 |
| PRO-OBR-003 — Registrar a despesa da obra | CAP-OBR-003 | RN-OBR-004, RN-OBR-006 |
| PRO-OBR-004 — Registrar etapas e vistorias | CAP-OBR-004 | RN-OBR-007, RN-OBR-008 |
| PRO-OBR-005 — Consultar o andamento físico-financeiro | CAP-OBR-005 | RN-OBR-004, RN-OBR-005, RN-OBR-006 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 003-Mapa-de-Processos-Obras-e-Infraestrutura.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_obras`. Alterações no código devem ser
> refletidas reexecutando o gerador.
