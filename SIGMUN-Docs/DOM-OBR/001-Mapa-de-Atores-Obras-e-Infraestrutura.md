# 001 – Mapa de Atores – Obras e Infraestrutura

#### Mapa de Atores – Obras e Infraestrutura

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OBR-001

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

Este artefato identifica as pessoas, unidades organizacionais, papéis e entidades
externas que interagem com o domínio de Obras e Infraestrutura, estabelecendo quem
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
| AT-OBR-001 | Gestor de obras | Servidor municipal | Planeja, contrata e acompanha as obras públicas, respondendo pela consistência do cadastro e do ciclo de vida. | CAP-OBR-001, CAP-OBR-005 |
| AT-OBR-002 | Fiscal de obra | Servidor municipal | Confere medições no campo e lavra as vistorias fiscalizadoras do avanço físico. | CAP-OBR-002, CAP-OBR-004 |
| AT-OBR-003 | Responsável técnico da obra | Profissional contratado | Executa a obra e registra o avanço físico por etapa e por medição. | CAP-OBR-003 |
| AT-OBR-004 | Tesouraria municipal | Servidor municipal | Registra os repasses e as despesas financeiras da obra, limitados ao valor já medido. | CAP-OBR-003 |
| AT-OBR-005 | Controle interno do município | Órgão municipal de controle | Acompanha a execução financeira e a regularidade das obras públicas. | CAP-OBR-005 |
| AT-OBR-006 | Cidadão | Público externo | Consulta o andamento físico e financeiro das obras do município. | CAP-OBR-005 |


---

# 4. Detalhamento

### AT-OBR-001 — Gestor de obras

**Tipo:** Servidor municipal

**Papel:** Planeja, contrata e acompanha as obras públicas, respondendo pela consistência do cadastro e do ciclo de vida.

**Decisões que pode tomar:** Cadastra obras, altera a contratação e conduz o ciclo de vida até a conclusão ou o cancelamento.

**Sistemas utilizados:** SIGMUN — Obras e Infraestrutura

**Capacidades exercidas:** CAP-OBR-001, CAP-OBR-005

---

### AT-OBR-002 — Fiscal de obra

**Tipo:** Servidor municipal

**Papel:** Confere medições no campo e lavra as vistorias fiscalizadoras do avanço físico.

**Decisões que pode tomar:** Confere e aprova medições, glosa medições indevidas e registra vistorias com parecer.

**Sistemas utilizados:** SIGMUN — Obras e Infraestrutura

**Capacidades exercidas:** CAP-OBR-002, CAP-OBR-004

---

### AT-OBR-003 — Responsável técnico da obra

**Tipo:** Profissional contratado

**Papel:** Executa a obra e registra o avanço físico por etapa e por medição.

**Decisões que pode tomar:** Registra etapas, informa o avanço e solicita a medição; não aprova a própria medição.

**Sistemas utilizados:** SIGMUN — Obras e Infraestrutura

**Capacidades exercidas:** CAP-OBR-003

---

### AT-OBR-004 — Tesouraria municipal

**Tipo:** Servidor municipal

**Papel:** Registra os repasses e as despesas financeiras da obra, limitados ao valor já medido.

**Decisões que pode tomar:** Registra despesas e repasses; não altera medições nem avança o percentual físico.

**Sistemas utilizados:** SIGMUN — Obras e Infraestrutura; SIGMUN — Finanças

**Capacidades exercidas:** CAP-OBR-003

---

### AT-OBR-005 — Controle interno do município

**Tipo:** Órgão municipal de controle

**Papel:** Acompanha a execução financeira e a regularidade das obras públicas.

**Decisões que pode tomar:** Consulta indicadores e não altera o cadastro da obra.

**Sistemas utilizados:** SIGMUN — Obras e Infraestrutura

**Capacidades exercidas:** CAP-OBR-005

---

### AT-OBR-006 — Cidadão

**Tipo:** Público externo

**Papel:** Consulta o andamento físico e financeiro das obras do município.

**Decisões que pode tomar:** Não altera o sistema; apenas consulta.

**Sistemas utilizados:** SIGMUN — Portal do cidadão

**Capacidades exercidas:** CAP-OBR-005

---

# 5. Relação com as Capacidades

| Ator | Capacidades |
| --- | |
| AT-OBR-001 — Gestor de obras | CAP-OBR-001, CAP-OBR-005 |
| AT-OBR-002 — Fiscal de obra | CAP-OBR-002, CAP-OBR-004 |
| AT-OBR-003 — Responsável técnico da obra | CAP-OBR-003 |
| AT-OBR-004 — Tesouraria municipal | CAP-OBR-003 |
| AT-OBR-005 — Controle interno do município | CAP-OBR-005 |
| AT-OBR-006 — Cidadão | CAP-OBR-005 |


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

**Documento:** 001-Mapa-de-Atores-Obras-e-Infraestrutura.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_obras`. Alterações no código devem ser
> refletidas reexecutando o gerador.
