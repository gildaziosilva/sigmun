# 008 – Requisitos Funcionais – Geoinformação Municipal

#### Requisitos Funcionais – Geoinformação Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GEO-008

**Domínio:** Geoinformação Municipal

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Geoinformacao-Municipal.md`
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

Este artefato especifica os requisitos funcionais do domínio de Geoinformação Municipal,
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
| RF-GEO-001 | O sistema deve permitir cadastrar, alterar, listar, consultar, ativar, desativar e excluir camadas cartográficas. | Essencial | CAP-GEO-001 | RN-GEO-001, RN-GEO-006 | 7 |
| RF-GEO-002 | O sistema deve permitir filtrar a listagem de camadas por tipo. | Desejável | CAP-GEO-001 | RN-GEO-001 | 1 |
| RF-GEO-003 | O sistema deve permitir cadastrar, alterar, listar, consultar, publicar, arquivar e excluir mapas SIG. | Essencial | CAP-GEO-002 | RN-GEO-002, RN-GEO-004 | 7 |
| RF-GEO-004 | O sistema deve permitir compor e descompor mapas por camada, definindo ordem, opacidade, rótulo e visibilidade. | Essencial | CAP-GEO-003 | RN-GEO-004, RN-GEO-006, RN-GEO-008 | 3 |
| RF-GEO-005 | O sistema deve permitir registrar, listar, consultar e excluir elementos geoespaciais vinculados a uma camada. | Essencial | CAP-GEO-004 | RN-GEO-003, RN-GEO-008 | 4 |
| RF-GEO-006 | O sistema deve permitir listar os elementos geoespaciais de uma camada específica. | Essencial | CAP-GEO-004 | RN-GEO-008 | 1 |
| RF-GEO-007 | O sistema deve permitir cadastrar, alterar, listar, consultar, inativar e excluir serviços geoespaciais. | Essencial | CAP-GEO-005 | RN-GEO-007 | 6 |
| RF-GEO-008 | O sistema deve permitir filtrar a listagem de serviços por protocolo. | Desejável | CAP-GEO-005 | RN-GEO-007 | 1 |
| RF-GEO-009 | O sistema deve permitir filtrar a listagem de mapas por situação. | Desejável | CAP-GEO-002 | RN-GEO-004 | 1 |


---

# 4. Detalhamento

### RF-GEO-001 — O sistema deve permitir cadastrar, alterar, listar, consultar, ativar, desativar e excluir camadas cartográficas.

**Prioridade:** Essencial

**Capacidade:** CAP-GEO-001

**Regras:** RN-GEO-001, RN-GEO-006

**Operações:**

* `POST /api/v1/geo/camadas`
* `GET /api/v1/geo/camadas`
* `GET /api/v1/geo/camadas/{camada_id}`
* `PATCH /api/v1/geo/camadas/{camada_id}`
* `DELETE /api/v1/geo/camadas/{camada_id}`
* `POST /api/v1/geo/camadas/{camada_id}/ativar`
* `POST /api/v1/geo/camadas/{camada_id}/desativar`
### RF-GEO-002 — O sistema deve permitir filtrar a listagem de camadas por tipo.

**Prioridade:** Desejável

**Capacidade:** CAP-GEO-001

**Regras:** RN-GEO-001

**Operações:**

* `GET /api/v1/geo/camadas`
### RF-GEO-003 — O sistema deve permitir cadastrar, alterar, listar, consultar, publicar, arquivar e excluir mapas SIG.

**Prioridade:** Essencial

**Capacidade:** CAP-GEO-002

**Regras:** RN-GEO-002, RN-GEO-004

**Operações:**

* `POST /api/v1/geo/mapas`
* `GET /api/v1/geo/mapas`
* `GET /api/v1/geo/mapas/{mapa_id}`
* `PATCH /api/v1/geo/mapas/{mapa_id}`
* `DELETE /api/v1/geo/mapas/{mapa_id}`
* `POST /api/v1/geo/mapas/{mapa_id}/publicar`
* `POST /api/v1/geo/mapas/{mapa_id}/arquivar`
### RF-GEO-004 — O sistema deve permitir compor e descompor mapas por camada, definindo ordem, opacidade, rótulo e visibilidade.

**Prioridade:** Essencial

**Capacidade:** CAP-GEO-003

**Regras:** RN-GEO-004, RN-GEO-006, RN-GEO-008

**Operações:**

* `GET /api/v1/geo/mapas/{mapa_id}/composicao`
* `POST /api/v1/geo/mapas/{mapa_id}/composicao`
* `DELETE /api/v1/geo/mapas/{mapa_id}/composicao/{vinculo_id}`
### RF-GEO-005 — O sistema deve permitir registrar, listar, consultar e excluir elementos geoespaciais vinculados a uma camada.

**Prioridade:** Essencial

**Capacidade:** CAP-GEO-004

**Regras:** RN-GEO-003, RN-GEO-008

**Operações:**

* `POST /api/v1/geo/features`
* `GET /api/v1/geo/features`
* `GET /api/v1/geo/features/{feature_id}`
* `DELETE /api/v1/geo/features/{feature_id}`
### RF-GEO-006 — O sistema deve permitir listar os elementos geoespaciais de uma camada específica.

**Prioridade:** Essencial

**Capacidade:** CAP-GEO-004

**Regras:** RN-GEO-008

**Operações:**

* `GET /api/v1/geo/features/camada/{camada_id}`
### RF-GEO-007 — O sistema deve permitir cadastrar, alterar, listar, consultar, inativar e excluir serviços geoespaciais.

**Prioridade:** Essencial

**Capacidade:** CAP-GEO-005

**Regras:** RN-GEO-007

**Operações:**

* `POST /api/v1/geo/servicos`
* `GET /api/v1/geo/servicos`
* `GET /api/v1/geo/servicos/{servico_id}`
* `PATCH /api/v1/geo/servicos/{servico_id}`
* `DELETE /api/v1/geo/servicos/{servico_id}`
* `POST /api/v1/geo/servicos/{servico_id}/inativar`
### RF-GEO-008 — O sistema deve permitir filtrar a listagem de serviços por protocolo.

**Prioridade:** Desejável

**Capacidade:** CAP-GEO-005

**Regras:** RN-GEO-007

**Operações:**

* `GET /api/v1/geo/servicos`
### RF-GEO-009 — O sistema deve permitir filtrar a listagem de mapas por situação.

**Prioridade:** Desejável

**Capacidade:** CAP-GEO-002

**Regras:** RN-GEO-004

**Operações:**

* `GET /api/v1/geo/mapas`

# 5. Cobertura por Capacidade

| Capacidade | Requisitos |
| --- | |
| CAP-GEO-001 — Cadastro de camadas cartográficas | RF-GEO-001, RF-GEO-002 |
| CAP-GEO-002 — Gestão de mapas SIG | RF-GEO-003, RF-GEO-009 |
| CAP-GEO-003 — Composição de camadas por mapa | RF-GEO-004 |
| CAP-GEO-004 — Cadastro de elementos geoespaciais | RF-GEO-005, RF-GEO-006 |
| CAP-GEO-005 — Publicação de serviços geoespaciais | RF-GEO-007, RF-GEO-008 |
| CAP-GEO-006 — Consulta de mapas e serviços |  |


---

# 6. Observações

* Requisitos são verificados pelos casos de teste do domínio, mapeados no
  artefato de matriz de rastreabilidade.
* A contagem de operações considera apenas o prefixo `/api/v1/geo`.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 008-Requisitos-Funcionais-Geoinformacao-Municipal.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_geoinformacao`. Alterações no código devem ser
> refletidas reexecutando o gerador.
