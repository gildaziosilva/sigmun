# 003 – Mapa de Processos – Gestão Territorial

#### Mapa de Processos – Gestão Territorial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TEL-003

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

Este artefato descreve os processos de negócio do domínio de Gestão Territorial,
da intenção do ator à alteração do estado, evidenciando entradas, saídas e
regras aplicadas.

---

# 2. Convenções

* **Gatilho:** evento ou condição que dispara o processo.
* **Objetivo:** resultado pretendido pelo processo.
* **Passos:** sequência lógica; as regras de negócio aplicadas aparecem entre
  parênteses na etapa correspondente.

---

# 3. Visão Geral

| ID | Processo | Gatilho | Objetivo |
| --- | | --- | | --- | |
| PRO-TEL-001 | Manter divisão territorial | Levantamento censitário, criação de nova área ou alteração de limites. | Garantir divisões territoriais codificadas e consistentes. |
| PRO-TEL-002 | Manter logradouro | Pavimentação nova, alteração de nome ou mudança de situação. | Manter a malha viária codificada e vinculada ao bairro. |
| PRO-TEL-003 | Elaborar e aprovar a planta de valores | Início do exercício fiscal ou alteração da legislação de valores. | Estabelecer os valores unitários que sustentam o valor venal. |
| PRO-TEL-004 | Consultar planta de valores vigente | Necessidade de apurar o valor unitário de um imóvel. | Recuperar de forma determinística a planta aplicável. |
| PRO-TEL-005 | Registrar georreferência | Levantamento de campo, atualização cartográfica ou georreferenciamento legal. | Associar a divisões e logradouros suas coordenadas. |


---

# 4. Detalhamento

### PRO-TEL-001 — Manter divisão territorial

**Gatilho:** Levantamento censitário, criação de nova área ou alteração de limites.

**Objetivo:** Garantir divisões territoriais codificadas e consistentes.

**Entradas:** Código; nome; tipo; população estimada; área em km²

**Saídas:** Divisão territorial cadastrada ou atualizada

**Regras aplicadas:** RN-TEL-001, RN-TEL-006

**Passos:**

1. Verificar se o código já está cadastrado (RN-TEL-001).
2. Preencher os dados da divisão territorial.
3. Gravar a divisão e registrar autoria e data.

---
### PRO-TEL-002 — Manter logradouro

**Gatilho:** Pavimentação nova, alteração de nome ou mudança de situação.

**Objetivo:** Manter a malha viária codificada e vinculada ao bairro.

**Entradas:** Código; nome; divisão territorial; tipo; CEP; numeração inicial e final

**Saídas:** Logradouro cadastrado, atualizado ou excluído

**Regras aplicadas:** RN-TEL-002, RN-TEL-006

**Passos:**

1. Selecionar a divisão territorial de vinculação (RN-TEL-002).
2. Verificar a unicidade do código do logradouro (RN-TEL-002).
3. Informar tipo, CEP e faixa de numeração.
4. Gravar o logradouro vinculado.

---
### PRO-TEL-003 — Elaborar e aprovar a planta de valores

**Gatilho:** Início do exercício fiscal ou alteração da legislação de valores.

**Objetivo:** Estabelecer os valores unitários que sustentam o valor venal.

**Entradas:** Ano; divisão; ocupação; valor do terreno; valor da construção; alíquota; legislação

**Saídas:** Planta genérica de valores vigente

**Regras aplicadas:** RN-TEL-003, RN-TEL-004

**Passos:**

1. Elaborar a planta em rascunho, conforme a legislação vigente.
2. Verificar se já existe planta vigente para o mesmo ano, divisão e ocupação (RN-TEL-003).
3. Ativar a planta, tornando-a referência do exercício (RN-TEL-004).
4. Quando superada, revogar a planta anterior com justificativa (RN-TEL-004).

---
### PRO-TEL-004 — Consultar planta de valores vigente

**Gatilho:** Necessidade de apurar o valor unitário de um imóvel.

**Objetivo:** Recuperar de forma determinística a planta aplicável.

**Entradas:** Ano; divisão territorial; ocupação

**Saídas:** Valores unitários vigentes; alíquota; legislação

**Regras aplicadas:** RN-TEL-003

**Passos:**

1. Informar ano, divisão e ocupação.
2. Localizar a planta com situação vigente (RN-TEL-003).
3. Retornar os valores; sem planta vigente, informar a ausência.

---
### PRO-TEL-005 — Registrar georreferência

**Gatilho:** Levantamento de campo, atualização cartográfica ou georreferenciamento legal.

**Objetivo:** Associar a divisões e logradouros suas coordenadas.

**Entradas:** Referência territorial; tipo de geometria; vértices; datum; precisão; data do levantamento

**Saídas:** Georreferência registrada

**Regras aplicadas:** RN-TEL-005

**Passos:**

1. Selecionar a divisão ou o logradouro de referência, nunca ambos (RN-TEL-005).
2. Informar o tipo de geometria e os vértices correspondentes (RN-TEL-005).
3. Definir o datum e a precisão do levantamento.
4. Gravar a georreferência.

---

# 5. Processos por Capacidade

| Processo | Capacidades | Regras |
| --- | | --- | |
| PRO-TEL-001 — Manter divisão territorial | CAP-TEL-001 | RN-TEL-001, RN-TEL-006 |
| PRO-TEL-002 — Manter logradouro | CAP-TEL-002 | RN-TEL-002, RN-TEL-006 |
| PRO-TEL-003 — Elaborar e aprovar a planta de valores | CAP-TEL-003 | RN-TEL-003, RN-TEL-004 |
| PRO-TEL-004 — Consultar planta de valores vigente | CAP-TEL-004 | RN-TEL-003 |
| PRO-TEL-005 — Registrar georreferência | CAP-TEL-005 | RN-TEL-005 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 003-Mapa-de-Processos-Gestao-Territorial.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_territorial`. Alterações no código devem ser
> refletidas reexecutando o gerador.
