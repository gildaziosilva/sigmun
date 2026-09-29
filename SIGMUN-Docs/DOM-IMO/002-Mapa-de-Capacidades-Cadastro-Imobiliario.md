# 002 – Mapa de Capacidades – Cadastro Imobiliário

#### Mapa de Capacidades – Cadastro Imobiliário

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IMO-002

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

Este artefato consolida as capacidades de negócio oferecidas pelo domínio de
Cadastro Imobiliário, relacionando cada capacidade aos processos que a executam e
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
| CAP-IMO-001 | Cadastro de lotes | Manter unidades imobiliárias com inscrição única, logradouro, bairro, áreas e ano de construção. | PRO-IMO-001 | RN-IMO-001, RN-IMO-002, RN-IMO-003 |
| CAP-IMO-002 | Titularidade do imóvel | Vincular pessoas físicas e jurídicas ao imóvel, com um único titular principal. | PRO-IMO-002 | RN-IMO-006 |
| CAP-IMO-003 | Ciclo de vida do imóvel | Controlar a situação cadastral do imóvel por meio de uma máquina de estados auditável. | PRO-IMO-003 | RN-IMO-004 |
| CAP-IMO-004 | Avaliação do valor venal | Apurar o valor venal a partir dos valores unitários vigentes da planta genérica de valores. | PRO-IMO-004 | RN-IMO-005 |
| CAP-IMO-005 | Consulta e contestação cadastral | Consultar a situação do imóvel, a titularidade e o valor venal aplicado. | PRO-IMO-005 | RN-IMO-001, RN-IMO-005 |
| CAP-IMO-006 | Georreferenciamento do lote | Registrar a geometria georreferenciada de cada lote, com datum e vértices validados. | PRO-IMO-006 | RN-IMO-007 |


---

# 4. Detalhamento

### CAP-IMO-001 — Cadastro de lotes

**Descrição:** Manter unidades imobiliárias com inscrição única, logradouro, bairro, áreas e ano de construção.

**Processos:** PRO-IMO-001

**Regras aplicáveis:** RN-IMO-001, RN-IMO-002, RN-IMO-003

**Atores:** AT-IMO-001

---

### CAP-IMO-002 — Titularidade do imóvel

**Descrição:** Vincular pessoas físicas e jurídicas ao imóvel, com um único titular principal.

**Processos:** PRO-IMO-002

**Regras aplicáveis:** RN-IMO-006

**Atores:** AT-IMO-001, AT-IMO-003

---

### CAP-IMO-003 — Ciclo de vida do imóvel

**Descrição:** Controlar a situação cadastral do imóvel por meio de uma máquina de estados auditável.

**Processos:** PRO-IMO-003

**Regras aplicáveis:** RN-IMO-004

**Atores:** AT-IMO-001

---

### CAP-IMO-004 — Avaliação do valor venal

**Descrição:** Apurar o valor venal a partir dos valores unitários vigentes da planta genérica de valores.

**Processos:** PRO-IMO-004

**Regras aplicáveis:** RN-IMO-005

**Atores:** AT-IMO-002

---

### CAP-IMO-005 — Consulta e contestação cadastral

**Descrição:** Consultar a situação do imóvel, a titularidade e o valor venal aplicado.

**Processos:** PRO-IMO-005

**Regras aplicáveis:** RN-IMO-001, RN-IMO-005

**Atores:** AT-IMO-002, AT-IMO-004

---

### CAP-IMO-006 — Georreferenciamento do lote

**Descrição:** Registrar a geometria georreferenciada de cada lote, com datum e vértices validados.

**Processos:** PRO-IMO-006

**Regras aplicáveis:** RN-IMO-007

**Atores:** AT-IMO-001

---

# 5. Cobertura

| Indicador | Quantidade |
| --- | |
| Capacidades mapeadas | 6 |
| Atores exercidos | 4 |
| Processos vinculados | 6 |
| Regras aplicadas | 7 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 002-Mapa-de-Capacidades-Cadastro-Imobiliario.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_cadastro_imobiliario`. Alterações no código devem ser
> refletidas reexecutando o gerador.
