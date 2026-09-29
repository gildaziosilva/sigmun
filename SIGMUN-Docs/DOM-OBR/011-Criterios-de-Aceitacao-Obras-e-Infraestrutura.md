# 011 – Critérios de Aceitação – Obras e Infraestrutura

#### Critérios de Aceitação – Obras e Infraestrutura

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OBR-011

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

Este artefato consolida os critérios de aceitação das histórias de usuário do
domínio de Obras e Infraestrutura, no formato *Dado / Quando / Então*, vinculando cada
critério à regra de negócio que ele exercita.

---

# 2. Convenções

* Cada critério descreve um resultado observável, e não um passo de implementação.
* Critérios que envolvem recusa citam o código HTTP retornado.
* A coluna de regras permite medir a cobertura de verificação por regra.

---

# 3. Critérios por História

### HU-OBR-001 — Manter o cadastro das obras públicas

**Capacidade:** CAP-OBR-001 · **Regras:** RN-OBR-001, RN-OBR-002, RN-OBR-003, RN-OBR-004

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado que o número da obra é novo, quando o gestor cadastra, então a obra é criada | RN-OBR-001, RN-OBR-002, RN-OBR-003, RN-OBR-004 |
| 2 | Dado que o número já existe, quando o gestor cadastra, então o sistema recusa com HTTP 409 (RN-OBR-001) | RN-OBR-001, RN-OBR-002, RN-OBR-003, RN-OBR-004 |
| 3 | Dado que o valor contratado supera o orçado, quando o gestor cadastra, então o sistema recusa (RN-OBR-004) | RN-OBR-001, RN-OBR-002, RN-OBR-003, RN-OBR-004 |
| 4 | Dado uma obra já concluída, quando o gestor tenta alterar o cadastro, então o sistema recusa (RN-OBR-002). | RN-OBR-001, RN-OBR-002, RN-OBR-003, RN-OBR-004 |
### HU-OBR-002 — Conduzir o ciclo de vida da obra

**Capacidade:** CAP-OBR-001 · **Regras:** RN-OBR-002, RN-OBR-003, RN-OBR-005

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado uma obra contratada com empresa e data prevista, quando o gestor inicia a execução, então a obra passa a em execução | RN-OBR-002, RN-OBR-003, RN-OBR-005 |
| 2 | Dado que a empresa não foi informada, quando o gestor tenta iniciar, então o sistema recusa (RN-OBR-003) | RN-OBR-002, RN-OBR-003, RN-OBR-005 |
| 3 | Dado uma obra com avanço físico parcial, quando o gestor tenta concluir, então o sistema recusa com HTTP 409 (RN-OBR-005). | RN-OBR-002, RN-OBR-003, RN-OBR-005 |
### HU-OBR-003 — Medir e conferir o avanço da obra

**Capacidade:** CAP-OBR-002 · **Regras:** RN-OBR-004, RN-OBR-005

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado uma medição registrada, quando o fiscal confere e aprova, então a medição passa a aprovada e o avanço da obra é recomposto | RN-OBR-004, RN-OBR-005 |
| 2 | Dado que a medição não foi conferida, quando se tenta aprová-la, então o sistema recusa (RN-OBR-005) | RN-OBR-004, RN-OBR-005 |
| 3 | Dado que o valor medido supera o contratado, quando o responsável registra, então o sistema recusa (RN-OBR-005) | RN-OBR-004, RN-OBR-005 |
| 4 | Dado uma medição aprovada, quando o fiscal tenta cancelá-la, então o sistema recusa (RN-OBR-005). | RN-OBR-004, RN-OBR-005 |
### HU-OBR-004 — Registrar etapas e vistorias da obra

**Capacidade:** CAP-OBR-004 · **Regras:** RN-OBR-007, RN-OBR-008

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado uma etapa com responsável, quando o responsável cadastra, então a etapa é criada | RN-OBR-007, RN-OBR-008 |
| 2 | Dado uma etapa de peso parcial totalmente executada, quando o fiscal conclui, então a etapa passa a concluída (RN-OBR-007) | RN-OBR-007, RN-OBR-008 |
| 3 | Dado uma etapa com realizado abaixo do previsto, quando se tenta concluir, então o sistema recusa (RN-OBR-007) | RN-OBR-007, RN-OBR-008 |
| 4 | Dado uma obra existente, quando o fiscal registra vistoria, então o parecer e o percentual verificado são gravados (RN-OBR-008). | RN-OBR-007, RN-OBR-008 |
### HU-OBR-005 — Registrar repasses e despesas da obra

**Capacidade:** CAP-OBR-003 · **Regras:** RN-OBR-004, RN-OBR-006

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado que há saldo medido, quando a tesouraria registra a despesa, então o avanço financeiro é recomposto | RN-OBR-004, RN-OBR-006 |
| 2 | Dado que a despesa supera o saldo medido a pagar, quando a tesouraria registra, então o sistema recusa com HTTP 409 (RN-OBR-006) | RN-OBR-004, RN-OBR-006 |
| 3 | Dado que a obra está planejada, quando a tesouraria registra despesa, então o sistema recusa (RN-OBR-006). | RN-OBR-004, RN-OBR-006 |
### HU-OBR-006 — Consultar o andamento das obras

**Capacidade:** CAP-OBR-005 · **Regras:** RN-OBR-004, RN-OBR-005, RN-OBR-006

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado que existem obras cadastradas, quando o cidadão consulta, então a lista de obras com seus percentuais é retornada | RN-OBR-004, RN-OBR-005, RN-OBR-006 |
| 2 | Dado uma obra específica, quando o cidadão consulta o acompanhamento, então medições, despesas, etapas e vistorias são retornadas (RF-OBR-008) | RN-OBR-004, RN-OBR-005, RN-OBR-006 |
| 3 | Dado um identificador inexistente, quando o cidadão consulta, então o sistema responde HTTP 404. | RN-OBR-004, RN-OBR-005, RN-OBR-006 |
### HU-OBR-007 — Fiscalizar a regularidade financeira

**Capacidade:** CAP-OBR-005 · **Regras:** RN-OBR-004, RN-OBR-006

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado o conjunto de obras cadastradas, quando o auditor consulta, então nenhum caso de avanço financeiro superior ao físico é apresentado (RN-OBR-004) | RN-OBR-004, RN-OBR-006 |
| 2 | Dado que não há saldo medido, quando o auditor verifica, então não há despesa acima do medido (RN-OBR-006). | RN-OBR-004, RN-OBR-006 |

# 4. Cobertura de Aceitação

| História | Critérios | Regras cobertas |
| --- | | --- | |
| HU-OBR-001 | 4 | RN-OBR-001, RN-OBR-002, RN-OBR-003, RN-OBR-004 |
| HU-OBR-002 | 3 | RN-OBR-002, RN-OBR-003, RN-OBR-005 |
| HU-OBR-003 | 4 | RN-OBR-004, RN-OBR-005 |
| HU-OBR-004 | 4 | RN-OBR-007, RN-OBR-008 |
| HU-OBR-005 | 3 | RN-OBR-004, RN-OBR-006 |
| HU-OBR-006 | 3 | RN-OBR-004, RN-OBR-005, RN-OBR-006 |
| HU-OBR-007 | 2 | RN-OBR-004, RN-OBR-006 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 011-Criterios-de-Aceitacao-Obras-e-Infraestrutura.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_obras`. Alterações no código devem ser
> refletidas reexecutando o gerador.
