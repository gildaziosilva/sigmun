# 011 – Critérios de Aceitação – Geoinformação Municipal

#### Critérios de Aceitação – Geoinformação Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GEO-011

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

Este artefato consolida os critérios de aceitação das histórias de usuário do
domínio de Geoinformação Municipal, no formato *Dado / Quando / Então*, vinculando cada
critério à regra de negócio que ele exercita.

---

# 2. Convenções

* Cada critério descreve um resultado observável, e não um passo de implementação.
* Critérios que envolvem recusa citam o código HTTP retornado.
* A coluna de regras permite medir a cobertura de verificação por regra.

---

# 3. Critérios por História

### HU-GEO-001 — Manter as camadas do geoportal

**Capacidade:** CAP-GEO-001 · **Regras:** RN-GEO-001, RN-GEO-005, RN-GEO-006

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado que o código da camada é novo, quando o técnico cadastra, então a camada é criada | RN-GEO-001, RN-GEO-005, RN-GEO-006 |
| 2 | Dado que o código já existe, quando o técnico cadastra, então o sistema recusa com HTTP 409 (RN-GEO-001) | RN-GEO-001, RN-GEO-005, RN-GEO-006 |
| 3 | Dado uma camada WMS sem URL, quando o técnico tenta ativar, então o sistema recusa (RN-GEO-006) | RN-GEO-001, RN-GEO-005, RN-GEO-006 |
| 4 | Dado uma camada desativada, quando o técnico tenta reativar, então o sistema recusa (RN-GEO-006). | RN-GEO-001, RN-GEO-005, RN-GEO-006 |
### HU-GEO-002 — Compor mapas temáticos com camadas

**Capacidade:** CAP-GEO-003 · **Regras:** RN-GEO-004, RN-GEO-006, RN-GEO-008

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado um mapa em rascunho e uma camada ativa, quando o gestor compõe, então o vínculo é criado | RN-GEO-004, RN-GEO-006, RN-GEO-008 |
| 2 | Dado que a camada já está na composição, quando o gestor tenta incluir de novo, então o sistema recusa (RN-GEO-004) | RN-GEO-004, RN-GEO-006, RN-GEO-008 |
| 3 | Dado um mapa publicado, quando o gestor tenta alterar a composição, então o sistema recusa (RN-GEO-004). | RN-GEO-004, RN-GEO-006, RN-GEO-008 |
### HU-GEO-003 — Publicar mapas no geoportal

**Capacidade:** CAP-GEO-002 · **Regras:** RN-GEO-004, RN-GEO-005, RN-GEO-006

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado um mapa com ao menos uma camada ativa, quando o gestor publica, então o mapa passa a publicado | RN-GEO-004, RN-GEO-005, RN-GEO-006 |
| 2 | Dado um mapa sem camadas, quando o gestor tenta publicar, então o sistema recusa com HTTP 409 (RN-GEO-004) | RN-GEO-004, RN-GEO-005, RN-GEO-006 |
| 3 | Dado um mapa publicado, quando o gestor arquiva, então o mapa passa a arquivado (RN-GEO-004). | RN-GEO-004, RN-GEO-005, RN-GEO-006 |
### HU-GEO-004 — Registrar pontos de interesse no mapa

**Capacidade:** CAP-GEO-004 · **Regras:** RN-GEO-003, RN-GEO-008

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado uma camada existente, quando o técnico registra um ponto com vértice válido, então o elemento é criado | RN-GEO-003, RN-GEO-008 |
| 2 | Dado um polígono com menos de 3 vértices, quando o técnico registra, então o sistema recusa com HTTP 409 (RN-GEO-003) | RN-GEO-003, RN-GEO-008 |
| 3 | Dado um elemento cuja camada foi desativada, quando o técnico registra, então o sistema recusa (RN-GEO-008). | RN-GEO-003, RN-GEO-008 |
### HU-GEO-005 — Publicar serviços de mapas para terceiros

**Capacidade:** CAP-GEO-005 · **Regras:** RN-GEO-005, RN-GEO-007

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado protocolo WMS com URL e camada publicada, quando o administrador cadastra, então o serviço é criado | RN-GEO-005, RN-GEO-007 |
| 2 | Dado um serviço ativo sem URL, quando o administrador cadastra, então o sistema recusa (RN-GEO-007) | RN-GEO-005, RN-GEO-007 |
| 3 | Dado um WFS sem nome de camada, quando o administrador cadastra, então o sistema recusa (RN-GEO-007). | RN-GEO-005, RN-GEO-007 |
### HU-GEO-006 — Consultar a cartografia municipal

**Capacidade:** CAP-GEO-006 · **Regras:** RN-GEO-003, RN-GEO-004

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
| 1 | Dado que existem mapas publicados, quando o cidadão consulta, então os mapas são retornados | RN-GEO-003, RN-GEO-004 |
| 2 | Dado que a camada é informada, quando o cidadão lista elementos, então somente os elementos da camada são retornados (RN-GEO-008) | RN-GEO-003, RN-GEO-004 |
| 3 | Dado um identificador inexistente, quando o cidadão consulta, então o sistema responde HTTP 404. | RN-GEO-003, RN-GEO-004 |

# 4. Cobertura de Aceitação

| História | Critérios | Regras cobertas |
| --- | | --- | |
| HU-GEO-001 | 4 | RN-GEO-001, RN-GEO-005, RN-GEO-006 |
| HU-GEO-002 | 3 | RN-GEO-004, RN-GEO-006, RN-GEO-008 |
| HU-GEO-003 | 3 | RN-GEO-004, RN-GEO-005, RN-GEO-006 |
| HU-GEO-004 | 3 | RN-GEO-003, RN-GEO-008 |
| HU-GEO-005 | 3 | RN-GEO-005, RN-GEO-007 |
| HU-GEO-006 | 3 | RN-GEO-003, RN-GEO-004 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 011-Criterios-de-Aceitacao-Geoinformacao-Municipal.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_geoinformacao`. Alterações no código devem ser
> refletidas reexecutando o gerador.
