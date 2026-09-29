# 002 – Mapa de Capacidades – Geoinformação Municipal

#### Mapa de Capacidades – Geoinformação Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GEO-002

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

Este artefato consolida as capacidades de negócio oferecidas pelo domínio de
Geoinformação Municipal, relacionando cada capacidade aos processos que a executam e
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
| CAP-GEO-001 | Cadastro de camadas cartográficas | Manter camadas com código único, tipo, formato, datum, faixa de zoom e URL de serviço quando aplicável. | PRO-GEO-001 | RN-GEO-001, RN-GEO-006 |
| CAP-GEO-002 | Gestão de mapas SIG | Elaborar, publicar e arquivar mapas temáticos e cadastrais do geoportal municipal. | PRO-GEO-003 | RN-GEO-002, RN-GEO-004, RN-GEO-005 |
| CAP-GEO-003 | Composição de camadas por mapa | Definir quais camadas compõem cada mapa, com ordem, opacidade, rótulo e visibilidade. | PRO-GEO-002 | RN-GEO-004, RN-GEO-008 |
| CAP-GEO-004 | Cadastro de elementos geoespaciais | Registrar pontos de interesse e demais elementos com geometria georreferenciada em uma camada. | PRO-GEO-004 | RN-GEO-003, RN-GEO-008 |
| CAP-GEO-005 | Publicação de serviços geoespaciais | Cadastrar e manter os serviços de publicação do geoportal, com protocolo, URL e camada publicada. | PRO-GEO-005 | RN-GEO-007 |
| CAP-GEO-006 | Consulta de mapas e serviços | Disponibilizar mapas publicados, elementos geoespaciais e serviços de acesso público. | PRO-GEO-006 | RN-GEO-003, RN-GEO-004 |


---

# 4. Detalhamento

### CAP-GEO-001 — Cadastro de camadas cartográficas

**Descrição:** Manter camadas com código único, tipo, formato, datum, faixa de zoom e URL de serviço quando aplicável.

**Processos:** PRO-GEO-001

**Regras aplicáveis:** RN-GEO-001, RN-GEO-006

**Atores:** AT-GEO-001

---

### CAP-GEO-002 — Gestão de mapas SIG

**Descrição:** Elaborar, publicar e arquivar mapas temáticos e cadastrais do geoportal municipal.

**Processos:** PRO-GEO-003

**Regras aplicáveis:** RN-GEO-002, RN-GEO-004, RN-GEO-005

**Atores:** AT-GEO-002

---

### CAP-GEO-003 — Composição de camadas por mapa

**Descrição:** Definir quais camadas compõem cada mapa, com ordem, opacidade, rótulo e visibilidade.

**Processos:** PRO-GEO-002

**Regras aplicáveis:** RN-GEO-004, RN-GEO-008

**Atores:** AT-GEO-002, AT-GEO-001

---

### CAP-GEO-004 — Cadastro de elementos geoespaciais

**Descrição:** Registrar pontos de interesse e demais elementos com geometria georreferenciada em uma camada.

**Processos:** PRO-GEO-004

**Regras aplicáveis:** RN-GEO-003, RN-GEO-008

**Atores:** AT-GEO-001, AT-GEO-003

---

### CAP-GEO-005 — Publicação de serviços geoespaciais

**Descrição:** Cadastrar e manter os serviços de publicação do geoportal, com protocolo, URL e camada publicada.

**Processos:** PRO-GEO-005

**Regras aplicáveis:** RN-GEO-007

**Atores:** AT-GEO-004

---

### CAP-GEO-006 — Consulta de mapas e serviços

**Descrição:** Disponibilizar mapas publicados, elementos geoespaciais e serviços de acesso público.

**Processos:** PRO-GEO-006

**Regras aplicáveis:** RN-GEO-003, RN-GEO-004

**Atores:** AT-GEO-003, AT-GEO-005

---

# 5. Cobertura

| Indicador | Quantidade |
| --- | |
| Capacidades mapeadas | 6 |
| Atores exercidos | 5 |
| Processos vinculados | 6 |
| Regras aplicadas | 8 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 002-Mapa-de-Capacidades-Geoinformacao-Municipal.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_geoinformacao`. Alterações no código devem ser
> refletidas reexecutando o gerador.
