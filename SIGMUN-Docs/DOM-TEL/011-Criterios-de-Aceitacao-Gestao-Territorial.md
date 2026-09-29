# 011 – Critérios de Aceitação – Gestão Territorial

#### Critérios de Aceitação – Gestão Territorial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TEL-011

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

Este artefato consolida os critérios de aceitação das histórias de usuário do
domínio de Gestão Territorial, no formato *Dado / Quando / Então*, vinculando cada
critério à regra de negócio que ele exercita.

---

# 2. Convenções

* Cada critério descreve um resultado observável, e não um passo de implementação.
* Critérios que envolvem recusa citam o código HTTP retornado.
* A coluna de regras permite medir a cobertura de verificação por regra.

---

# 3. Critérios por História

### HU-TEL-001 — Manter o cadastro de divisões territoriais

**Capacidade:** CAP-TEL-001 · **Regras:** RN-TEL-001, RN-TEL-006

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado um código inexistente, quando o técnico cadastra a divisão, então a divisão é criada e fica ativa | RN-TEL-001, RN-TEL-006 |
| 2 | Dado um código já cadastrado, quando o técnico tenta cadastrar, então o sistema recusa com HTTP 409 (RN-TEL-001) | RN-TEL-001, RN-TEL-006 |
| 3 | Dado uma divisão com logradouros ativos, quando o técnico tenta excluir, então o sistema recusa com HTTP 409 (RN-TEL-006). | RN-TEL-001, RN-TEL-006 |
### HU-TEL-002 — Manter a malha de logradouros

**Capacidade:** CAP-TEL-002 · **Regras:** RN-TEL-002

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado um bairro existente, quando o técnico cadastra o logradouro, então o logradouro fica vinculado ao bairro | RN-TEL-002 |
| 2 | Dado um bairro inexistente, quando o técnico cadastra o logradouro, então o sistema recusa com HTTP 404 (RN-TEL-002) | RN-TEL-002 |
| 3 | Dado um código de logradouro já cadastrado, quando o técnico cadastra, então o sistema recusa com HTTP 409 (RN-TEL-002). | RN-TEL-002 |
### HU-TEL-003 — Elaborar e aprovar a planta de valores do exercício

**Capacidade:** CAP-TEL-003 · **Regras:** RN-TEL-003, RN-TEL-004

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado uma planta em rascunho, quando a comissão ativa e não há conflito, então a planta passa a vigente | RN-TEL-003, RN-TEL-004 |
| 2 | Dado que já existe planta vigente para a mesma combinação, quando a comissão ativa outra, então o sistema recusa com HTTP 409 (RN-TEL-003) | RN-TEL-003, RN-TEL-004 |
| 3 | Dado uma planta vigente, quando a comissão revoga com justificativa, então a planta passa a revogada (RN-TEL-004) | RN-TEL-003, RN-TEL-004 |
| 4 | Dado uma planta sem justificativa, quando a comissão tenta revogar, então o sistema recusa (RN-TEL-004) | RN-TEL-003, RN-TEL-004 |
| 5 | Dado uma planta vigente ou revogada, quando se tenta editar valores, então o sistema recusa (RN-TEL-004). | RN-TEL-003, RN-TEL-004 |
### HU-TEL-004 — Consultar a planta de valores vigente

**Capacidade:** CAP-TEL-004 · **Regras:** RN-TEL-003

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado uma planta vigente para a combinação, quando o fiscal consulta, então os valores unitários e a alíquota são retornados | RN-TEL-003 |
| 2 | Dado que não há planta vigente para a combinação, quando o fiscal consulta, então o sistema responde HTTP 404. | RN-TEL-003 |
### HU-TEL-005 — Registrar a georreferência do território

**Capacidade:** CAP-TEL-005 · **Regras:** RN-TEL-005

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado uma divisão existente, quando o técnico registra um polígono com ao menos 3 vértices válidos, então a georreferência é criada | RN-TEL-005 |
| 2 | Dado que nenhum ou ambos os vínculos são informados, quando o técnico registra, então o sistema recusa (RN-TEL-005) | RN-TEL-005 |
| 3 | Dado um polígono com menos de 3 vértices, quando o técnico registra, então o sistema recusa com HTTP 409 (RN-TEL-005) | RN-TEL-005 |
| 4 | Dado uma coordenada fora da faixa do datum, quando o técnico registra, então o sistema recusa (RN-TEL-005). | RN-TEL-005 |

# 4. Cobertura de Aceitação

| História | Critérios | Regras cobertas |
| --- | | --- | |
| HU-TEL-001 | 3 | RN-TEL-001, RN-TEL-006 |
| HU-TEL-002 | 3 | RN-TEL-002 |
| HU-TEL-003 | 5 | RN-TEL-003, RN-TEL-004 |
| HU-TEL-004 | 2 | RN-TEL-003 |
| HU-TEL-005 | 4 | RN-TEL-005 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 011-Criterios-de-Aceitacao-Gestao-Territorial.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_territorial`. Alterações no código devem ser
> refletidas reexecutando o gerador.
