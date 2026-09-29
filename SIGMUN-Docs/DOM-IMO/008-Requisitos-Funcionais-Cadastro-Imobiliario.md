# 008 – Requisitos Funcionais – Cadastro Imobiliário

#### Requisitos Funcionais – Cadastro Imobiliário

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IMO-008

**Domínio:** Cadastro Imobiliário

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Cadastro-Imobiliario.md`
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

Este artefato especifica os requisitos funcionais do domínio de Cadastro Imobiliário,
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
| RF-IMO-001 | O sistema deve permitir cadastrar, alterar, listar, consultar e excluir lotes. | Essencial | CAP-IMO-001 | RN-IMO-001, RN-IMO-002, RN-IMO-003 | 5 |
| RF-IMO-002 | O sistema deve permitir consultar o imóvel pela inscrição e listar os imóveis de um logradouro ou de um bairro. | Essencial | CAP-IMO-001 | RN-IMO-001 | 3 |
| RF-IMO-003 | O sistema deve permitir alterar a situação do imóvel conforme a máquina de estados. | Essencial | CAP-IMO-003 | RN-IMO-004 | 1 |
| RF-IMO-004 | O sistema deve permitir vincular proprietários ao imóvel, com um único titular principal. | Essencial | CAP-IMO-002 | RN-IMO-006 | 4 |
| RF-IMO-005 | O sistema deve permitir registrar a avaliação do valor venal do imóvel para um exercício. | Essencial | CAP-IMO-004 | RN-IMO-005 | 2 |
| RF-IMO-006 | O sistema deve permitir concluir e cancelar avaliações conforme o ciclo de vida da avaliação. | Essencial | CAP-IMO-004 | RN-IMO-005 | 4 |
| RF-IMO-007 | O sistema deve permitir registrar a característica construtiva do imóvel. | Importante | CAP-IMO-001 | RN-IMO-003 | 3 |
| RF-IMO-008 | O sistema deve permitir registrar a geometria georreferenciada do lote. | Essencial | CAP-IMO-006 | RN-IMO-007 | 3 |


---

# 4. Detalhamento

### RF-IMO-001 — O sistema deve permitir cadastrar, alterar, listar, consultar e excluir lotes.

**Prioridade:** Essencial

**Capacidade:** CAP-IMO-001

**Regras:** RN-IMO-001, RN-IMO-002, RN-IMO-003

**Operações:**

* `POST /api/v1/imo/imoveis`
* `GET /api/v1/imo/imoveis`
* `GET /api/v1/imo/imoveis/{imovel_id}`
* `PATCH /api/v1/imo/imoveis/{imovel_id}`
* `DELETE /api/v1/imo/imoveis/{imovel_id}`
### RF-IMO-002 — O sistema deve permitir consultar o imóvel pela inscrição e listar os imóveis de um logradouro ou de um bairro.

**Prioridade:** Essencial

**Capacidade:** CAP-IMO-001

**Regras:** RN-IMO-001

**Operações:**

* `GET /api/v1/imo/imoveis/inscricao/{inscricao}`
* `GET /api/v1/imo/imoveis/logradouro/{logradouro_id}`
* `GET /api/v1/imo/imoveis/bairro/{bairro_id}`
### RF-IMO-003 — O sistema deve permitir alterar a situação do imóvel conforme a máquina de estados.

**Prioridade:** Essencial

**Capacidade:** CAP-IMO-003

**Regras:** RN-IMO-004

**Operações:**

* `POST /api/v1/imo/imoveis/{imovel_id}/situacao`
### RF-IMO-004 — O sistema deve permitir vincular proprietários ao imóvel, com um único titular principal.

**Prioridade:** Essencial

**Capacidade:** CAP-IMO-002

**Regras:** RN-IMO-006

**Operações:**

* `POST /api/v1/imo/proprietarios`
* `GET /api/v1/imo/proprietarios`
* `GET /api/v1/imo/imoveis/{imovel_id}/proprietarios`
* `DELETE /api/v1/imo/proprietarios/{vinculo_id}`
### RF-IMO-005 — O sistema deve permitir registrar a avaliação do valor venal do imóvel para um exercício.

**Prioridade:** Essencial

**Capacidade:** CAP-IMO-004

**Regras:** RN-IMO-005

**Operações:**

* `POST /api/v1/imo/avaliacoes`
* `GET /api/v1/imo/avaliacoes`
### RF-IMO-006 — O sistema deve permitir concluir e cancelar avaliações conforme o ciclo de vida da avaliação.

**Prioridade:** Essencial

**Capacidade:** CAP-IMO-004

**Regras:** RN-IMO-005

**Operações:**

* `POST /api/v1/imo/avaliacoes/{avaliacao_id}/concluir`
* `POST /api/v1/imo/avaliacoes/{avaliacao_id}/cancelar`
* `GET /api/v1/imo/avaliacoes/{avaliacao_id}`
* `GET /api/v1/imo/avaliacoes/imovel/{imovel_id}`
### RF-IMO-007 — O sistema deve permitir registrar a característica construtiva do imóvel.

**Prioridade:** Importante

**Capacidade:** CAP-IMO-001

**Regras:** RN-IMO-003

**Operações:**

* `POST /api/v1/imo/caracteristicas`
* `GET /api/v1/imo/caracteristicas`
* `GET /api/v1/imo/caracteristicas/imovel/{imovel_id}`
### RF-IMO-008 — O sistema deve permitir registrar a geometria georreferenciada do lote.

**Prioridade:** Essencial

**Capacidade:** CAP-IMO-006

**Regras:** RN-IMO-007

**Operações:**

* `POST /api/v1/imo/geometrias`
* `GET /api/v1/imo/geometrias`
* `GET /api/v1/imo/geometrias/imovel/{imovel_id}`

# 5. Cobertura por Capacidade

| Capacidade | Requisitos |
| --- | |
| CAP-IMO-001 — Cadastro de lotes | RF-IMO-001, RF-IMO-002, RF-IMO-007 |
| CAP-IMO-002 — Titularidade do imóvel | RF-IMO-004 |
| CAP-IMO-003 — Ciclo de vida do imóvel | RF-IMO-003 |
| CAP-IMO-004 — Avaliação do valor venal | RF-IMO-005, RF-IMO-006 |
| CAP-IMO-005 — Consulta e contestação cadastral |  |
| CAP-IMO-006 — Georreferenciamento do lote | RF-IMO-008 |


---

# 6. Observações

* Requisitos são verificados pelos casos de teste do domínio, mapeados no
  artefato de matriz de rastreabilidade.
* A contagem de operações considera apenas o prefixo `/api/v1/imo`.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 008-Requisitos-Funcionais-Cadastro-Imobiliario.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_cadastro_imobiliario`. Alterações no código devem ser
> refletidas reexecutando o gerador.
