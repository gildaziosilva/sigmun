# 011 – Critérios de Aceitação – Cadastro Imobiliário

#### Critérios de Aceitação – Cadastro Imobiliário

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IMO-011

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

Este artefato consolida os critérios de aceitação das histórias de usuário do
domínio de Cadastro Imobiliário, no formato *Dado / Quando / Então*, vinculando cada
critério à regra de negócio que ele exercita.

---

# 2. Convenções

* Cada critério descreve um resultado observável, e não um passo de implementação.
* Critérios que envolvem recusa citam o código HTTP retornado.
* A coluna de regras permite medir a cobertura de verificação por regra.

---

# 3. Critérios por História

### HU-IMO-001 — Cadastrar e manter lotes

**Capacidade:** CAP-IMO-001 · **Regras:** RN-IMO-001, RN-IMO-002, RN-IMO-003

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado um logradouro existente no DOM-TEL, quando o técnico cadastra o lote, então o imóvel é criado com o bairro resolvido | RN-IMO-001, RN-IMO-002, RN-IMO-003 |
| 2 | Dado uma inscrição já cadastrada, quando o técnico tenta cadastrar, então o sistema recusa com HTTP 409 (RN-IMO-001) | RN-IMO-001, RN-IMO-002, RN-IMO-003 |
| 3 | Dado uma área negativa, quando o técnico cadastra, então o sistema recusa (RN-IMO-003). | RN-IMO-001, RN-IMO-002, RN-IMO-003 |
### HU-IMO-002 — Controlar a titularidade do imóvel

**Capacidade:** CAP-IMO-002 · **Regras:** RN-IMO-006

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado um imóvel sem titular, quando o técnico vincula um titular principal, então o vínculo é criado | RN-IMO-006 |
| 2 | Dado um imóvel que já possui titular principal, quando o técnico tenta vincular outro principal, então o sistema recusa com HTTP 409 (RN-IMO-006) | RN-IMO-006 |
| 3 | Dado um CPF ou CNPJ com comprimento inválido, quando o técnico vincula, então o sistema recusa (RN-IMO-006) | RN-IMO-006 |
| 4 | Dado a mesma pessoa já vinculada, quando o técnico vincula novamente, então o sistema recusa (RN-IMO-006). | RN-IMO-006 |
### HU-IMO-003 — Controlar o ciclo de vida do imóvel

**Capacidade:** CAP-IMO-003 · **Regras:** RN-IMO-004

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado um imóvel ativo, quando o técnico marca em obra, então a situação é alterada (RN-IMO-004) | RN-IMO-004 |
| 2 | Dado um imóvel demolido, quando o técnico tenta reativar, então o sistema recusa com HTTP 409 (RN-IMO-004) | RN-IMO-004 |
| 3 | Dado um imóvel inativo, quando o técnico marca desocupado sem reativar, então o sistema recusa (RN-IMO-004). | RN-IMO-004 |
### HU-IMO-004 — Avaliar o valor venal do imóvel

**Capacidade:** CAP-IMO-004 · **Regras:** RN-IMO-005

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado um imóvel de 200 m² de terreno e 120 m² de construção, quando a avaliação usa R$ 180/m² e R$ 950/m², então o valor venal é de R$ 150.000,00 (RN-IMO-005) | RN-IMO-005 |
| 2 | Dado um exercício já avaliado e concluído, quando o avaliador tenta reavaliar, então o sistema recusa com HTTP 409 (RN-IMO-005) | RN-IMO-005 |
| 3 | Dado um imóvel sem áreas, quando o avaliador tenta avaliar, então o sistema recusa (RN-IMO-005). | RN-IMO-005 |
### HU-IMO-005 — Georreferenciar o lote

**Capacidade:** CAP-IMO-006 · **Regras:** RN-IMO-007

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado um imóvel existente, quando o técnico registra um polígono com vértices válidos, então a geometria é gravada | RN-IMO-007 |
| 2 | Dado um polígono com menos de 3 vértices, quando o técnico registra, então o sistema recusa (RN-IMO-007) | RN-IMO-007 |
| 3 | Dado um datum não suportado, quando o técnico registra, então o sistema recusa (RN-IMO-007). | RN-IMO-007 |

# 4. Cobertura de Aceitação

| História | Critérios | Regras cobertas |
| --- | | --- | |
| HU-IMO-001 | 3 | RN-IMO-001, RN-IMO-002, RN-IMO-003 |
| HU-IMO-002 | 4 | RN-IMO-006 |
| HU-IMO-003 | 3 | RN-IMO-004 |
| HU-IMO-004 | 3 | RN-IMO-005 |
| HU-IMO-005 | 3 | RN-IMO-007 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 011-Criterios-de-Aceitacao-Cadastro-Imobiliario.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_cadastro_imobiliario`. Alterações no código devem ser
> refletidas reexecutando o gerador.
