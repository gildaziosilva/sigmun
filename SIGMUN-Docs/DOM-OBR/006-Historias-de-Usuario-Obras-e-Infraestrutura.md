# 006 – Histórias de Usuário – Obras e Infraestrutura

#### Histórias de Usuário – Obras e Infraestrutura

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OBR-006

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

Este artefato expressa as necessidades do domínio de Obras e Infraestrutura em histórias
de usuário, com critérios de aceitação verificáveis.

---

# 2. Convenções

* O padrão é *Como / Quero / Para*, com critérios no formato
  **Dado** / **Quando** / **Então**.
* Cada critério referencia a regra de negócio que ele exercita.

---

# 3. Histórias de Usuário

### HU-OBR-001 — Manter o cadastro das obras públicas

**Como** como gestor de obras,
**quero** cadastrar obras, convenir a contratação e manter os dados da obra,
**para** dispor de cadastro oficial para o acompanhamento e a transparência.

**Capacidade:** CAP-OBR-001

**Regras relacionadas:** RN-OBR-001, RN-OBR-002, RN-OBR-003, RN-OBR-004

**Critérios de aceitação:**

1. Dado que o número da obra é novo, quando o gestor cadastra, então a obra é criada
2. Dado que o número já existe, quando o gestor cadastra, então o sistema recusa com HTTP 409 (RN-OBR-001)
3. Dado que o valor contratado supera o orçado, quando o gestor cadastra, então o sistema recusa (RN-OBR-004)
4. Dado uma obra já concluída, quando o gestor tenta alterar o cadastro, então o sistema recusa (RN-OBR-002).
### HU-OBR-002 — Conduzir o ciclo de vida da obra

**Como** como gestor de obras,
**quero** iniciar, suspender, concluir e cancelar obras,
**para** refletir no sistema a situação real do empreendimento.

**Capacidade:** CAP-OBR-001

**Regras relacionadas:** RN-OBR-002, RN-OBR-003, RN-OBR-005

**Critérios de aceitação:**

1. Dado uma obra contratada com empresa e data prevista, quando o gestor inicia a execução, então a obra passa a em execução
2. Dado que a empresa não foi informada, quando o gestor tenta iniciar, então o sistema recusa (RN-OBR-003)
3. Dado uma obra com avanço físico parcial, quando o gestor tenta concluir, então o sistema recusa com HTTP 409 (RN-OBR-005).
### HU-OBR-003 — Medir e conferir o avanço da obra

**Como** como fiscal de obra,
**quero** conferir medições e aprovar ou glosar o avanço físico-financeiro,
**para** assegurar que o medido corresponde ao executado.

**Capacidade:** CAP-OBR-002

**Regras relacionadas:** RN-OBR-004, RN-OBR-005

**Critérios de aceitação:**

1. Dado uma medição registrada, quando o fiscal confere e aprova, então a medição passa a aprovada e o avanço da obra é recomposto
2. Dado que a medição não foi conferida, quando se tenta aprová-la, então o sistema recusa (RN-OBR-005)
3. Dado que o valor medido supera o contratado, quando o responsável registra, então o sistema recusa (RN-OBR-005)
4. Dado uma medição aprovada, quando o fiscal tenta cancelá-la, então o sistema recusa (RN-OBR-005).
### HU-OBR-004 — Registrar etapas e vistorias da obra

**Como** como fiscal de obra,
**quero** registrar etapas de execução e lavrar vistorias com parecer,
**para** documentar o avanço físico e a fiscalização de campo.

**Capacidade:** CAP-OBR-004

**Regras relacionadas:** RN-OBR-007, RN-OBR-008

**Critérios de aceitação:**

1. Dado uma etapa com responsável, quando o responsável cadastra, então a etapa é criada
2. Dado uma etapa de peso parcial totalmente executada, quando o fiscal conclui, então a etapa passa a concluída (RN-OBR-007)
3. Dado uma etapa com realizado abaixo do previsto, quando se tenta concluir, então o sistema recusa (RN-OBR-007)
4. Dado uma obra existente, quando o fiscal registra vistoria, então o parecer e o percentual verificado são gravados (RN-OBR-008).
### HU-OBR-005 — Registrar repasses e despesas da obra

**Como** como tesoureiro municipal,
**quero** registrar repasses, materiais e custos atribuíveis à obra,
**para** pagar apenas o que foi medido e acompanhar o avanço financeiro.

**Capacidade:** CAP-OBR-003

**Regras relacionadas:** RN-OBR-004, RN-OBR-006

**Critérios de aceitação:**

1. Dado que há saldo medido, quando a tesouraria registra a despesa, então o avanço financeiro é recomposto
2. Dado que a despesa supera o saldo medido a pagar, quando a tesouraria registra, então o sistema recusa com HTTP 409 (RN-OBR-006)
3. Dado que a obra está planejada, quando a tesouraria registra despesa, então o sistema recusa (RN-OBR-006).
### HU-OBR-006 — Consultar o andamento das obras

**Como** como cidadão,
**quero** consultar o percentual físico e financeiro de cada obra,
**para** acompanhar a aplicação de recursos públicos.

**Capacidade:** CAP-OBR-005

**Regras relacionadas:** RN-OBR-004, RN-OBR-005, RN-OBR-006

**Critérios de aceitação:**

1. Dado que existem obras cadastradas, quando o cidadão consulta, então a lista de obras com seus percentuais é retornada
2. Dado uma obra específica, quando o cidadão consulta o acompanhamento, então medições, despesas, etapas e vistorias são retornadas (RF-OBR-008)
3. Dado um identificador inexistente, quando o cidadão consulta, então o sistema responde HTTP 404.
### HU-OBR-007 — Fiscalizar a regularidade financeira

**Como** como auditor do controle interno,
**quero** consultar a coerência entre avanço físico, medido e pago,
**para** detectar pagamento de valor não executado.

**Capacidade:** CAP-OBR-005

**Regras relacionadas:** RN-OBR-004, RN-OBR-006

**Critérios de aceitação:**

1. Dado o conjunto de obras cadastradas, quando o auditor consulta, então nenhum caso de avanço financeiro superior ao físico é apresentado (RN-OBR-004)
2. Dado que não há saldo medido, quando o auditor verifica, então não há despesa acima do medido (RN-OBR-006).

# 4. Rastreabilidade às Capacidades

| História | Capacidade | Regras |
| --- | | --- | |
| HU-OBR-001 — Manter o cadastro das obras públicas | CAP-OBR-001 | RN-OBR-001, RN-OBR-002, RN-OBR-003, RN-OBR-004 |
| HU-OBR-002 — Conduzir o ciclo de vida da obra | CAP-OBR-001 | RN-OBR-002, RN-OBR-003, RN-OBR-005 |
| HU-OBR-003 — Medir e conferir o avanço da obra | CAP-OBR-002 | RN-OBR-004, RN-OBR-005 |
| HU-OBR-004 — Registrar etapas e vistorias da obra | CAP-OBR-004 | RN-OBR-007, RN-OBR-008 |
| HU-OBR-005 — Registrar repasses e despesas da obra | CAP-OBR-003 | RN-OBR-004, RN-OBR-006 |
| HU-OBR-006 — Consultar o andamento das obras | CAP-OBR-005 | RN-OBR-004, RN-OBR-005, RN-OBR-006 |
| HU-OBR-007 — Fiscalizar a regularidade financeira | CAP-OBR-005 | RN-OBR-004, RN-OBR-006 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 006-Historias-de-Usuario-Obras-e-Infraestrutura.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_obras`. Alterações no código devem ser
> refletidas reexecutando o gerador.
