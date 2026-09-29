# 002 – Mapa de Capacidades – Gestão Territorial

#### Mapa de Capacidades – Gestão Territorial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TEL-002

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

Este artefato consolida as capacidades de negócio oferecidas pelo domínio de
Gestão Territorial, relacionando cada capacidade aos processos que a executam e
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
| CAP-TEL-001 | Cadastro de divisões territoriais | Manter bairros, distritos, setores e zonas rurais com código único, população estimada e área. | PRO-TEL-001 | RN-TEL-001, RN-TEL-006 |
| CAP-TEL-002 | Cadastro de logradouros públicos | Manter logradouros vinculados a uma divisão territorial, com tipo, CEP e numeração. | PRO-TEL-002 | RN-TEL-002, RN-TEL-006 |
| CAP-TEL-003 | Gestão da planta genérica de valores | Elaborar, ativar e revogar os valores unitários por ano, divisão e ocupação. | PRO-TEL-003 | RN-TEL-003, RN-TEL-004 |
| CAP-TEL-004 | Consulta de valores vigentes | Disponibilizar a planta vigente por ano, divisão e ocupação, inclusive para o DOM-IMO. | PRO-TEL-004 | RN-TEL-003 |
| CAP-TEL-005 | Georreferenciamento territorial | Registrar a posição geográfica de divisões e logradouros, com datum, vértices e precisão. | PRO-TEL-005 | RN-TEL-005 |


---

# 4. Detalhamento

### CAP-TEL-001 — Cadastro de divisões territoriais

**Descrição:** Manter bairros, distritos, setores e zonas rurais com código único, população estimada e área.

**Processos:** PRO-TEL-001

**Regras aplicáveis:** RN-TEL-001, RN-TEL-006

**Atores:** AT-TEL-001

---

### CAP-TEL-002 — Cadastro de logradouros públicos

**Descrição:** Manter logradouros vinculados a uma divisão territorial, com tipo, CEP e numeração.

**Processos:** PRO-TEL-002

**Regras aplicáveis:** RN-TEL-002, RN-TEL-006

**Atores:** AT-TEL-001, AT-TEL-005

---

### CAP-TEL-003 — Gestão da planta genérica de valores

**Descrição:** Elaborar, ativar e revogar os valores unitários por ano, divisão e ocupação.

**Processos:** PRO-TEL-003

**Regras aplicáveis:** RN-TEL-003, RN-TEL-004

**Atores:** AT-TEL-002

---

### CAP-TEL-004 — Consulta de valores vigentes

**Descrição:** Disponibilizar a planta vigente por ano, divisão e ocupação, inclusive para o DOM-IMO.

**Processos:** PRO-TEL-004

**Regras aplicáveis:** RN-TEL-003

**Atores:** AT-TEL-002, AT-TEL-003

---

### CAP-TEL-005 — Georreferenciamento territorial

**Descrição:** Registrar a posição geográfica de divisões e logradouros, com datum, vértices e precisão.

**Processos:** PRO-TEL-005

**Regras aplicáveis:** RN-TEL-005

**Atores:** AT-TEL-004

---

# 5. Cobertura

| Indicador | Quantidade |
| --- | |
| Capacidades mapeadas | 5 |
| Atores exercidos | 5 |
| Processos vinculados | 5 |
| Regras aplicadas | 6 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 002-Mapa-de-Capacidades-Gestao-Territorial.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_territorial`. Alterações no código devem ser
> refletidas reexecutando o gerador.
