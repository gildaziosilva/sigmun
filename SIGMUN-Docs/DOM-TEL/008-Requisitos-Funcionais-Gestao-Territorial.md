# 008 – Requisitos Funcionais – Gestão Territorial

#### Requisitos Funcionais – Gestão Territorial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TEL-008

**Domínio:** Gestão Territorial

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-Territorial.md`
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

Este artefato especifica os requisitos funcionais do domínio de Gestão Territorial,
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
| RF-TEL-001 | O sistema deve permitir cadastrar, alterar, listar, consultar e excluir divisões territoriais. | Essencial | CAP-TEL-001 | RN-TEL-001, RN-TEL-006 | 5 |
| RF-TEL-002 | O sistema deve permitir consultar uma divisão territorial pelo código cadastral. | Essencial | CAP-TEL-001 | RN-TEL-001 | 1 |
| RF-TEL-003 | O sistema deve permitir cadastrar, alterar, listar, consultar e excluir logradouros vinculados a uma divisão territorial. | Essencial | CAP-TEL-002 | RN-TEL-002, RN-TEL-006 | 5 |
| RF-TEL-004 | O sistema deve permitir listar os logradouros de uma divisão territorial. | Essencial | CAP-TEL-002 | RN-TEL-002 | 1 |
| RF-TEL-005 | O sistema deve permitir cadastrar a planta genérica de valores em rascunho ou já vigente. | Essencial | CAP-TEL-003 | RN-TEL-003, RN-TEL-004 | 1 |
| RF-TEL-006 | O sistema deve permitir ativar uma planta em rascunho e revogar uma planta vigente com justificativa. | Essencial | CAP-TEL-003 | RN-TEL-004 | 2 |
| RF-TEL-007 | O sistema deve permitir editar os valores de uma planta somente enquanto ela estiver em rascunho. | Essencial | CAP-TEL-003 | RN-TEL-004 | 1 |
| RF-TEL-008 | O sistema deve permitir consultar a planta vigente por ano, divisão territorial e ocupação. | Essencial | CAP-TEL-004 | RN-TEL-003 | 1 |
| RF-TEL-009 | O sistema deve permitir listar as plantas, opcionalmente filtradas por divisão territorial. | Importante | CAP-TEL-003 | — | 2 |
| RF-TEL-010 | O sistema deve permitir registrar, listar, consultar e excluir georreferências. | Essencial | CAP-TEL-005 | RN-TEL-005 | 4 |
| RF-TEL-011 | O sistema deve permitir filtrar as georreferências por divisão territorial ou por logradouro. | Importante | CAP-TEL-005 | RN-TEL-005 | 1 |


---

# 4. Detalhamento

### RF-TEL-001 — O sistema deve permitir cadastrar, alterar, listar, consultar e excluir divisões territoriais.

**Prioridade:** Essencial

**Capacidade:** CAP-TEL-001

**Regras:** RN-TEL-001, RN-TEL-006

**Operações:**

* `POST /api/v1/tel/bairros`
* `GET /api/v1/tel/bairros`
* `GET /api/v1/tel/bairros/{bairro_id}`
* `PATCH /api/v1/tel/bairros/{bairro_id}`
* `DELETE /api/v1/tel/bairros/{bairro_id}`
### RF-TEL-002 — O sistema deve permitir consultar uma divisão territorial pelo código cadastral.

**Prioridade:** Essencial

**Capacidade:** CAP-TEL-001

**Regras:** RN-TEL-001

**Operações:**

* `GET /api/v1/tel/bairros/codigo/{codigo}`
### RF-TEL-003 — O sistema deve permitir cadastrar, alterar, listar, consultar e excluir logradouros vinculados a uma divisão territorial.

**Prioridade:** Essencial

**Capacidade:** CAP-TEL-002

**Regras:** RN-TEL-002, RN-TEL-006

**Operações:**

* `POST /api/v1/tel/logradouros`
* `GET /api/v1/tel/logradouros`
* `GET /api/v1/tel/logradouros/{logradouro_id}`
* `PATCH /api/v1/tel/logradouros/{logradouro_id}`
* `DELETE /api/v1/tel/logradouros/{logradouro_id}`
### RF-TEL-004 — O sistema deve permitir listar os logradouros de uma divisão territorial.

**Prioridade:** Essencial

**Capacidade:** CAP-TEL-002

**Regras:** RN-TEL-002

**Operações:**

* `GET /api/v1/tel/bairros/{bairro_id}/logradouros`
### RF-TEL-005 — O sistema deve permitir cadastrar a planta genérica de valores em rascunho ou já vigente.

**Prioridade:** Essencial

**Capacidade:** CAP-TEL-003

**Regras:** RN-TEL-003, RN-TEL-004

**Operações:**

* `POST /api/v1/tel/plantas-valores`
### RF-TEL-006 — O sistema deve permitir ativar uma planta em rascunho e revogar uma planta vigente com justificativa.

**Prioridade:** Essencial

**Capacidade:** CAP-TEL-003

**Regras:** RN-TEL-004

**Operações:**

* `POST /api/v1/tel/plantas-valores/{planta_id}/ativar`
* `POST /api/v1/tel/plantas-valores/{planta_id}/revogar`
### RF-TEL-007 — O sistema deve permitir editar os valores de uma planta somente enquanto ela estiver em rascunho.

**Prioridade:** Essencial

**Capacidade:** CAP-TEL-003

**Regras:** RN-TEL-004

**Operações:**

* `PATCH /api/v1/tel/plantas-valores/{planta_id}`
### RF-TEL-008 — O sistema deve permitir consultar a planta vigente por ano, divisão territorial e ocupação.

**Prioridade:** Essencial

**Capacidade:** CAP-TEL-004

**Regras:** RN-TEL-003

**Operações:**

* `GET /api/v1/tel/plantas-valores/vigente`
### RF-TEL-009 — O sistema deve permitir listar as plantas, opcionalmente filtradas por divisão territorial.

**Prioridade:** Importante

**Capacidade:** CAP-TEL-003

**Regras:** —

**Operações:**

* `GET /api/v1/tel/plantas-valores`
* `GET /api/v1/tel/plantas-valores/{planta_id}`
### RF-TEL-010 — O sistema deve permitir registrar, listar, consultar e excluir georreferências.

**Prioridade:** Essencial

**Capacidade:** CAP-TEL-005

**Regras:** RN-TEL-005

**Operações:**

* `POST /api/v1/tel/georreferencias`
* `GET /api/v1/tel/georreferencias`
* `GET /api/v1/tel/georreferencias/{georreferencia_id}`
* `DELETE /api/v1/tel/georreferencias/{georreferencia_id}`
### RF-TEL-011 — O sistema deve permitir filtrar as georreferências por divisão territorial ou por logradouro.

**Prioridade:** Importante

**Capacidade:** CAP-TEL-005

**Regras:** RN-TEL-005

**Operações:**

* `GET /api/v1/tel/georreferencias/referencia`

# 5. Cobertura por Capacidade

| Capacidade | Requisitos |
| --- | |
| CAP-TEL-001 — Cadastro de divisões territoriais | RF-TEL-001, RF-TEL-002 |
| CAP-TEL-002 — Cadastro de logradouros públicos | RF-TEL-003, RF-TEL-004 |
| CAP-TEL-003 — Gestão da planta genérica de valores | RF-TEL-005, RF-TEL-006, RF-TEL-007, RF-TEL-009 |
| CAP-TEL-004 — Consulta de valores vigentes | RF-TEL-008 |
| CAP-TEL-005 — Georreferenciamento territorial | RF-TEL-010, RF-TEL-011 |


---

# 6. Observações

* Requisitos são verificados pelos casos de teste do domínio, mapeados no
  artefato de matriz de rastreabilidade.
* A contagem de operações considera apenas o prefixo `/api/v1/tel`.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 008-Requisitos-Funcionais-Gestao-Territorial.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_territorial`. Alterações no código devem ser
> refletidas reexecutando o gerador.
