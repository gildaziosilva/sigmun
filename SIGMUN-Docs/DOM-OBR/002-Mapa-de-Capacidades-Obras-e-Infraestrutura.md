# 002 – Mapa de Capacidades – Obras e Infraestrutura

#### Mapa de Capacidades – Obras e Infraestrutura

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OBR-002

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

Este artefato consolida as capacidades de negócio oferecidas pelo domínio de
Obras e Infraestrutura, relacionando cada capacidade aos processos que a executam e
às regras de negócio que a governam.

---

# 2. Princípios

* Uma capacidade descreve **o que** o domínio entrega, não **como** é implementado.
* Capacidades são independentes de tecnologia e de interface.
* Toda capacidade deve estar rastreada a processos, requisitos e regras.

---

# 3. Capacidades Identificadas

| Identificador | Capacidade | Descrição | Processos | Regras |
| --- | | --- | | --- | | --- | |
| CAP-OBR-001 | Cadastro e ciclo de vida das obras | Cadastrar obras com número único e conduzi-las pelo ciclo até a conclusão ou o cancelamento. | PRO-OBR-001 | RN-OBR-001, RN-OBR-002, RN-OBR-003, RN-OBR-004 |
| CAP-OBR-002 | Medição físico-financeira | Registrar, conferir, aprovar e glosar medições, recompondo o avanço da obra. | PRO-OBR-002 | RN-OBR-005 |
| CAP-OBR-003 | Execução financeira da obra | Registrar despesas e repasses, limitados ao valor medido e ainda não pago. | PRO-OBR-003 | RN-OBR-004, RN-OBR-006 |
| CAP-OBR-004 | Acompanhamento de etapas e vistorias | Registrar etapas de execução e vistorias fiscalizadoras com parecer sobre o avanço verificado. | PRO-OBR-004 | RN-OBR-007, RN-OBR-008 |
| CAP-OBR-005 | Consulta do andamento das obras | Consultar o avanço físico-financeiro consolidado, inclusive por terceiros. | PRO-OBR-005 | RN-OBR-004, RN-OBR-005, RN-OBR-006 |


---

# 4. Detalhamento

### CAP-OBR-001 — Cadastro e ciclo de vida das obras

**Descrição:** Cadastrar obras com número único e conduzi-las pelo ciclo até a conclusão ou o cancelamento.

**Processos:** PRO-OBR-001

**Regras aplicáveis:** RN-OBR-001, RN-OBR-002, RN-OBR-003, RN-OBR-004

**Atores:** AT-OBR-001

---

### CAP-OBR-002 — Medição físico-financeira

**Descrição:** Registrar, conferir, aprovar e glosar medições, recompondo o avanço da obra.

**Processos:** PRO-OBR-002

**Regras aplicáveis:** RN-OBR-005

**Atores:** AT-OBR-002, AT-OBR-003

---

### CAP-OBR-003 — Execução financeira da obra

**Descrição:** Registrar despesas e repasses, limitados ao valor medido e ainda não pago.

**Processos:** PRO-OBR-003

**Regras aplicáveis:** RN-OBR-004, RN-OBR-006

**Atores:** AT-OBR-004, AT-OBR-003

---

### CAP-OBR-004 — Acompanhamento de etapas e vistorias

**Descrição:** Registrar etapas de execução e vistorias fiscalizadoras com parecer sobre o avanço verificado.

**Processos:** PRO-OBR-004

**Regras aplicáveis:** RN-OBR-007, RN-OBR-008

**Atores:** AT-OBR-002, AT-OBR-003

---

### CAP-OBR-005 — Consulta do andamento das obras

**Descrição:** Consultar o avanço físico-financeiro consolidado, inclusive por terceiros.

**Processos:** PRO-OBR-005

**Regras aplicáveis:** RN-OBR-004, RN-OBR-005, RN-OBR-006

**Atores:** AT-OBR-005, AT-OBR-006, AT-OBR-001

---

# 5. Cobertura

| Indicador | Quantidade |
| --- | |
| Capacidades mapeadas | 5 |
| Atores exercidos | 6 |
| Processos vinculados | 5 |
| Regras aplicadas | 8 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 002-Mapa-de-Capacidades-Obras-e-Infraestrutura.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_obras`. Alterações no código devem ser
> refletidas reexecutando o gerador.
