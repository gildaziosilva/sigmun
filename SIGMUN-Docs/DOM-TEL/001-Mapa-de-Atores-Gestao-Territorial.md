# 001 – Mapa de Atores – Gestão Territorial

#### Mapa de Atores – Gestão Territorial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TEL-001

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

Este artefato identifica as pessoas, unidades organizacionais, papéis e entidades
externas que interagem com o domínio de Gestão Territorial, estabelecendo quem
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
| AT-TEL-001 | Técnico de cadastro imobiliário | Servidor municipal | Mantém o cadastro territorial e responde pela consistência dos códigos cadastrais. | CAP-TEL-001, CAP-TEL-002 |
| AT-TEL-002 | Comissão de Valores da Planta | Colegiado municipal | Define os valores unitários de terreno e construção por divisão, ocupação e exercício. | CAP-TEL-003 |
| AT-TEL-003 | Fiscal de tributos | Servidor municipal | Consulta os valores vigentes para instruir lançamentos e contestações. | CAP-TEL-004 |
| AT-TEL-004 | Técnico de georreferenciamento | Servidor municipal | Registra a georreferência obtida em levantamento de campo ou base cartográfica. | CAP-TEL-005 |
| AT-TEL-005 | Cartório de registro de imóveis | Entidade externa | Fornece matrículas e dados de lote para conferência do cadastro municipal. | CAP-TEL-002 |


---

# 4. Detalhamento

### AT-TEL-001 — Técnico de cadastro imobiliário

**Tipo:** Servidor municipal

**Papel:** Mantém o cadastro territorial e responde pela consistência dos códigos cadastrais.

**Decisões que pode tomar:** Cadastra e altera divisões territoriais e logradouros; inativa logradouros que deixaram de existir.

**Sistemas utilizados:** SIGMUN — Gestão Territorial

**Capacidades exercidas:** CAP-TEL-001, CAP-TEL-002

---

### AT-TEL-002 — Comissão de Valores da Planta

**Tipo:** Colegiado municipal

**Papel:** Define os valores unitários de terreno e construção por divisão, ocupação e exercício.

**Decisões que pode tomar:** Elabora a planta em rascunho, aprova sua vigência e revoga plantas superadas.

**Sistemas utilizados:** SIGMUN — Gestão Territorial; legislação municipal

**Capacidades exercidas:** CAP-TEL-003

---

### AT-TEL-003 — Fiscal de tributos

**Tipo:** Servidor municipal

**Papel:** Consulta os valores vigentes para instruir lançamentos e contestações.

**Decisões que pode tomar:** Não altera a planta; apenas consulta e solicita correção.

**Sistemas utilizados:** SIGMUN — Gestão Territorial; SIGMUN — Tributos

**Capacidades exercidas:** CAP-TEL-004

---

### AT-TEL-004 — Técnico de georreferenciamento

**Tipo:** Servidor municipal

**Papel:** Registra a georreferência obtida em levantamento de campo ou base cartográfica.

**Decisões que pode tomar:** Registra e revoga georreferências, definindo datum e vértices.

**Sistemas utilizados:** SIGMUN — Gestão Territorial; SIGMUN — Geoinformação

**Capacidades exercidas:** CAP-TEL-005

---

### AT-TEL-005 — Cartório de registro de imóveis

**Tipo:** Entidade externa

**Papel:** Fornece matrículas e dados de lote para conferência do cadastro municipal.

**Decisões que pode tomar:** Não altera o sistema; participa da conferência cadastral.

**Sistemas utilizados:** Cartório

**Capacidades exercidas:** CAP-TEL-002

---

# 5. Relação com as Capacidades

| Ator | Capacidades |
| --- | |
| AT-TEL-001 — Técnico de cadastro imobiliário | CAP-TEL-001, CAP-TEL-002 |
| AT-TEL-002 — Comissão de Valores da Planta | CAP-TEL-003 |
| AT-TEL-003 — Fiscal de tributos | CAP-TEL-004 |
| AT-TEL-004 — Técnico de georreferenciamento | CAP-TEL-005 |
| AT-TEL-005 — Cartório de registro de imóveis | CAP-TEL-002 |


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

**Documento:** 001-Mapa-de-Atores-Gestao-Territorial.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_territorial`. Alterações no código devem ser
> refletidas reexecutando o gerador.
