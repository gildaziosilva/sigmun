# 001 – Mapa de Atores – Geoinformação Municipal

#### Mapa de Atores – Geoinformação Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GEO-001

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

Este artefato identifica as pessoas, unidades organizacionais, papéis e entidades
externas que interagem com o domínio de Geoinformação Municipal, estabelecendo quem
participa, com que responsabilidade e em qual capacidade.

---

# 2. Princípios

* Atores representam papéis, e não pessoas específicas.
* A mesma pessoa pode exercer mais de um papel.
* Responsabilidade de negócio não se confunde com permissão de sistema.
* Atores externos são identificados quando influenciam os processos.

---

# 3. Atores Identificados

| Identificador | Ator | Tipo | Papel no domínio | Capacidades |
| --- | | --- | | --- | | --- | |
| AT-GEO-001 | Técnico de geoprocessamento | Servidor municipal | Mantém as camadas cartográficas do geoportal e responde pela consistência técnica das base geoespaciais. | CAP-GEO-001, CAP-GEO-003 |
| AT-GEO-002 | Gestor do geoportal | Servidor municipal | Decide o conteúdo e a publicação dos mapas temáticos e cadastrais do município. | CAP-GEO-002 |
| AT-GEO-003 | Fiscal de urbanismo | Servidor municipal | Consulta mapas e elementos geoespaciais para instruir processos de licenciamento e fiscalização. | CAP-GEO-004 |
| AT-GEO-004 | Administrador de serviços geoespaciais | Servidor municipal | Cadastra e mantém os serviços de publicação (WMS, WFS, WMTS, XYZ) consumidos por terceiros. | CAP-GEO-005 |
| AT-GEO-005 | Cidadão | Público externo | Consulta os mapas publicados e os serviços geoespaciais de acesso público. | CAP-GEO-006 |


---

# 4. Detalhamento

### AT-GEO-001 — Técnico de geoprocessamento

**Tipo:** Servidor municipal

**Papel:** Mantém as camadas cartográficas do geoportal e responde pela consistência técnica das base geoespaciais.

**Decisões que pode tomar:** Cadastra e altera camadas; ativa e desativa camadas; publica mapas no geoportal.

**Sistemas utilizados:** SIGMUN — Geoinformação Municipal

**Capacidades exercidas:** CAP-GEO-001, CAP-GEO-003

---

### AT-GEO-002 — Gestor do geoportal

**Tipo:** Servidor municipal

**Papel:** Decide o conteúdo e a publicação dos mapas temáticos e cadastrais do município.

**Decisões que pode tomar:** Compõe mapas a partir das camadas ativas; publica, arquiva e exclui mapas.

**Sistemas utilizados:** SIGMUN — Geoinformação Municipal

**Capacidades exercidas:** CAP-GEO-002

---

### AT-GEO-003 — Fiscal de urbanismo

**Tipo:** Servidor municipal

**Papel:** Consulta mapas e elementos geoespaciais para instruir processos de licenciamento e fiscalização.

**Decisões que pode tomar:** Não altera a cartografia; consulta e solicita correção.

**Sistemas utilizados:** SIGMUN — Geoinformação Municipal

**Capacidades exercidas:** CAP-GEO-004

---

### AT-GEO-004 — Administrador de serviços geoespaciais

**Tipo:** Servidor municipal

**Papel:** Cadastra e mantém os serviços de publicação (WMS, WFS, WMTS, XYZ) consumidos por terceiros.

**Decisões que pode tomar:** Cadastra, altera e inativa serviços geoespaciais.

**Sistemas utilizados:** SIGMUN — Geoinformação Municipal

**Capacidades exercidas:** CAP-GEO-005

---

### AT-GEO-005 — Cidadão

**Tipo:** Público externo

**Papel:** Consulta os mapas publicados e os serviços geoespaciais de acesso público.

**Decisões que pode tomar:** Não altera o sistema; apenas consulta.

**Sistemas utilizados:** Geoportal municipal

**Capacidades exercidas:** CAP-GEO-006

---

# 5. Relação com as Capacidades

| Ator | Capacidades |
| --- | |
| AT-GEO-001 — Técnico de geoprocessamento | CAP-GEO-001, CAP-GEO-003 |
| AT-GEO-002 — Gestor do geoportal | CAP-GEO-002 |
| AT-GEO-003 — Fiscal de urbanismo | CAP-GEO-004 |
| AT-GEO-004 — Administrador de serviços geoespaciais | CAP-GEO-005 |
| AT-GEO-005 — Cidadão | CAP-GEO-006 |


---

# 6. Observações

* A autorização de acesso é derivada das responsabilidades descritas acima e
  tratada no artefato de modelo de segurança.
* Atores externos participam por troca de informações; não alteram o sistema.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 001-Mapa-de-Atores-Geoinformacao-Municipal.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_geoinformacao`. Alterações no código devem ser
> refletidas reexecutando o gerador.
