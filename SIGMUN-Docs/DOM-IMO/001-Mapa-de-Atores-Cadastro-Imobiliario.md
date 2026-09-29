# 001 – Mapa de Atores – Cadastro Imobiliário

#### Mapa de Atores – Cadastro Imobiliário

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IMO-001

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

Este artefato identifica as pessoas, unidades organizacionais, papéis e entidades
externas que interagem com o domínio de Cadastro Imobiliário, estabelecendo quem
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
| AT-IMO-001 | Técnico de cadastro imobiliário | Servidor municipal | Mantém o cadastro dos lotes, suas características e a titularidade. | CAP-IMO-001, CAP-IMO-002, CAP-IMO-003 |
| AT-IMO-002 | Avaliador fiscal | Servidor municipal | Apura o valor venal dos imóveis a partir dos valores unitários vigentes. | CAP-IMO-004 |
| AT-IMO-003 | Cartório de registro de imóveis | Entidade externa | Fornece dados registrais para conferência da titularidade e da geometria do lote. | CAP-IMO-002 |
| AT-IMO-004 | Cidadão | Externo | Consulta a situação cadastral do imóvel e a avaliação aplicada. | CAP-IMO-005 |


---

# 4. Detalhamento

### AT-IMO-001 — Técnico de cadastro imobiliário

**Tipo:** Servidor municipal

**Papel:** Mantém o cadastro dos lotes, suas características e a titularidade.

**Decisões que pode tomar:** Cadastra imóveis, altera dados cadastrais e altera a situação conforme a máquina de estados.

**Sistemas utilizados:** SIGMUN — Cadastro Imobiliário

**Capacidades exercidas:** CAP-IMO-001, CAP-IMO-002, CAP-IMO-003

---

### AT-IMO-002 — Avaliador fiscal

**Tipo:** Servidor municipal

**Papel:** Apura o valor venal dos imóveis a partir dos valores unitários vigentes.

**Decisões que pode tomar:** Registra e cancela avaliações; não altera a planta genérica de valores.

**Sistemas utilizados:** SIGMUN — Cadastro Imobiliário; SIGMUN — Gestão Territorial; SIGMUN — Tributos

**Capacidades exercidas:** CAP-IMO-004

---

### AT-IMO-003 — Cartório de registro de imóveis

**Tipo:** Entidade externa

**Papel:** Fornece dados registrais para conferência da titularidade e da geometria do lote.

**Decisões que pode tomar:** Não altera o sistema.

**Sistemas utilizados:** Cartório

**Capacidades exercidas:** CAP-IMO-002

---

### AT-IMO-004 — Cidadão

**Tipo:** Externo

**Papel:** Consulta a situação cadastral do imóvel e a avaliação aplicada.

**Decisões que pode tomar:** Não altera o sistema; pode contestar o valor venal.

**Sistemas utilizados:** SIGMUN — Cadastro Imobiliário

**Capacidades exercidas:** CAP-IMO-005

---

# 5. Relação com as Capacidades

| Ator | Capacidades |
| --- | |
| AT-IMO-001 — Técnico de cadastro imobiliário | CAP-IMO-001, CAP-IMO-002, CAP-IMO-003 |
| AT-IMO-002 — Avaliador fiscal | CAP-IMO-004 |
| AT-IMO-003 — Cartório de registro de imóveis | CAP-IMO-002 |
| AT-IMO-004 — Cidadão | CAP-IMO-005 |


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

**Documento:** 001-Mapa-de-Atores-Cadastro-Imobiliario.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_cadastro_imobiliario`. Alterações no código devem ser
> refletidas reexecutando o gerador.
