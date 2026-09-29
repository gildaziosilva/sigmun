# 008 – Requisitos Funcionais – Obras e Infraestrutura

#### Requisitos Funcionais – Obras e Infraestrutura

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OBR-008

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

Este artefato especifica os requisitos funcionais do domínio de Obras e Infraestrutura,
declarando o comportamento esperado e sua rastreabilidade.

---

# 2. Convenções

* O padrão é `RF-<DOMÍNIO>-<sequencial>`.
* **Essencial** indica requisito sem o qual a capacidade não é entregue;
  **Importante** indica requisito cujo adiamento degrada o serviço.
* Cada requisito declara as operações REST que o implementam.

---

# 3. Requisitos Funcionais

| ID | Requisito | Prioridade | Capacidade | Regras | Operações |
| --- | | --- | | --- | | --- | | --- | |
| RF-OBR-001 | O sistema deve permitir cadastrar, alterar, listar, consultar e excluir obras públicas. | Essencial | CAP-OBR-001 | RN-OBR-001, RN-OBR-002, RN-OBR-004 | 5 |
| RF-OBR-002 | O sistema deve permitir iniciar, suspender, concluir e cancelar a obra, com justificativa quando aplicável. | Essencial | CAP-OBR-001 | RN-OBR-002, RN-OBR-003, RN-OBR-005 | 4 |
| RF-OBR-003 | O sistema deve permitir filtrar a listagem de obras por situação. | Desejável | CAP-OBR-001 | RN-OBR-002 | 1 |
| RF-OBR-004 | O sistema deve permitir registrar, aprovar, glosar e cancelar medições físico-financeiras, recompondo o avanço da obra. | Essencial | CAP-OBR-002 | RN-OBR-004, RN-OBR-005 | 4 |
| RF-OBR-005 | O sistema deve permitir registrar e excluir despesas financeiras da obra. | Essencial | CAP-OBR-003 | RN-OBR-004, RN-OBR-006 | 2 |
| RF-OBR-006 | O sistema deve permitir cadastrar etapas, atualizar o avanço realizado e concluir etapas da obra. | Essencial | CAP-OBR-004 | RN-OBR-007 | 3 |
| RF-OBR-007 | O sistema deve permitir registrar vistorias fiscalizadoras com parecer sobre o avanço verificado. | Essencial | CAP-OBR-004 | RN-OBR-008 | 1 |
| RF-OBR-008 | O sistema deve permitir consultar o acompanhamento consolidado da obra, reunindo medições, despesas, etapas e vistorias. | Essencial | CAP-OBR-005 | RN-OBR-004, RN-OBR-005, RN-OBR-006 | 1 |
| RF-OBR-009 | O sistema deve permitir consultar, separadamente, as medições, despesas, etapas e vistorias de uma obra. | Essencial | CAP-OBR-005 | RN-OBR-005, RN-OBR-006, RN-OBR-007, RN-OBR-008 | 4 |


---

# 4. Detalhamento

### RF-OBR-001 — O sistema deve permitir cadastrar, alterar, listar, consultar e excluir obras públicas.

**Prioridade:** Essencial

**Capacidade:** CAP-OBR-001

**Regras:** RN-OBR-001, RN-OBR-002, RN-OBR-004

**Operações:**

* `POST /api/v1/obr/obras`
* `GET /api/v1/obr/obras`
* `GET /api/v1/obr/obras/{obra_id}`
* `PATCH /api/v1/obr/obras/{obra_id}`
* `DELETE /api/v1/obr/obras/{obra_id}`
### RF-OBR-002 — O sistema deve permitir iniciar, suspender, concluir e cancelar a obra, com justificativa quando aplicável.

**Prioridade:** Essencial

**Capacidade:** CAP-OBR-001

**Regras:** RN-OBR-002, RN-OBR-003, RN-OBR-005

**Operações:**

* `POST /api/v1/obr/obras/{obra_id}/iniciar-execucao`
* `POST /api/v1/obr/obras/{obra_id}/suspender`
* `POST /api/v1/obr/obras/{obra_id}/concluir`
* `POST /api/v1/obr/obras/{obra_id}/cancelar`
### RF-OBR-003 — O sistema deve permitir filtrar a listagem de obras por situação.

**Prioridade:** Desejável

**Capacidade:** CAP-OBR-001

**Regras:** RN-OBR-002

**Operações:**

* `GET /api/v1/obr/obras`
### RF-OBR-004 — O sistema deve permitir registrar, aprovar, glosar e cancelar medições físico-financeiras, recompondo o avanço da obra.

**Prioridade:** Essencial

**Capacidade:** CAP-OBR-002

**Regras:** RN-OBR-004, RN-OBR-005

**Operações:**

* `POST /api/v1/obr/medicoes`
* `POST /api/v1/obr/medicoes/{medicao_id}/aprovar`
* `POST /api/v1/obr/medicoes/{medicao_id}/glosar`
* `POST /api/v1/obr/medicoes/{medicao_id}/cancelar`
### RF-OBR-005 — O sistema deve permitir registrar e excluir despesas financeiras da obra.

**Prioridade:** Essencial

**Capacidade:** CAP-OBR-003

**Regras:** RN-OBR-004, RN-OBR-006

**Operações:**

* `POST /api/v1/obr/despesas`
* `DELETE /api/v1/obr/despesas/{despesa_id}`
### RF-OBR-006 — O sistema deve permitir cadastrar etapas, atualizar o avanço realizado e concluir etapas da obra.

**Prioridade:** Essencial

**Capacidade:** CAP-OBR-004

**Regras:** RN-OBR-007

**Operações:**

* `POST /api/v1/obr/etapas`
* `PATCH /api/v1/obr/etapas/{etapa_id}`
* `POST /api/v1/obr/etapas/{etapa_id}/concluir`
### RF-OBR-007 — O sistema deve permitir registrar vistorias fiscalizadoras com parecer sobre o avanço verificado.

**Prioridade:** Essencial

**Capacidade:** CAP-OBR-004

**Regras:** RN-OBR-008

**Operações:**

* `POST /api/v1/obr/vistorias`
### RF-OBR-008 — O sistema deve permitir consultar o acompanhamento consolidado da obra, reunindo medições, despesas, etapas e vistorias.

**Prioridade:** Essencial

**Capacidade:** CAP-OBR-005

**Regras:** RN-OBR-004, RN-OBR-005, RN-OBR-006

**Operações:**

* `GET /api/v1/obr/obras/{obra_id}/acompanhamento`
### RF-OBR-009 — O sistema deve permitir consultar, separadamente, as medições, despesas, etapas e vistorias de uma obra.

**Prioridade:** Essencial

**Capacidade:** CAP-OBR-005

**Regras:** RN-OBR-005, RN-OBR-006, RN-OBR-007, RN-OBR-008

**Operações:**

* `GET /api/v1/obr/obras/{obra_id}/medicoes`
* `GET /api/v1/obr/obras/{obra_id}/despesas`
* `GET /api/v1/obr/obras/{obra_id}/etapas`
* `GET /api/v1/obr/obras/{obra_id}/vistorias`

# 5. Cobertura por Capacidade

| Capacidade | Requisitos |
| --- | |
| CAP-OBR-001 — Cadastro e ciclo de vida das obras | RF-OBR-001, RF-OBR-002, RF-OBR-003 |
| CAP-OBR-002 — Medição físico-financeira | RF-OBR-004 |
| CAP-OBR-003 — Execução financeira da obra | RF-OBR-005 |
| CAP-OBR-004 — Acompanhamento de etapas e vistorias | RF-OBR-006, RF-OBR-007 |
| CAP-OBR-005 — Consulta do andamento das obras | RF-OBR-008, RF-OBR-009 |


---

# 6. Observações

* Requisitos são verificados pelos casos de teste do domínio, mapeados no
  artefato de matriz de rastreabilidade.
* A contagem de operações considera apenas o prefixo `/api/v1/obr`.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 008-Requisitos-Funcionais-Obras-e-Infraestrutura.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_obras`. Alterações no código devem ser
> refletidas reexecutando o gerador.
