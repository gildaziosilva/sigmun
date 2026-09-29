# 006 – Histórias de Usuário – Geoinformação Municipal

#### Histórias de Usuário – Geoinformação Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GEO-006

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

Este artefato expressa as necessidades do domínio de Geoinformação Municipal em histórias
de usuário, com critérios de aceitação verificáveis.

---

# 2. Convenções

* O padrão é *Como / Quero / Para*, com critérios no formato
  **Dado** / **Quando** / **Então**.
* Cada critério referencia a regra de negócio que ele exercita.

---

# 3. Histórias de Usuário

### HU-GEO-001 — Manter as camadas do geoportal

**Como** como técnico de geoprocessamento,
**quero** cadastrar e manter camadas cartográficas com seus metadados técnicos,
**para** dispor de bases geoespaciais identificáveis e consistentes.

**Capacidade:** CAP-GEO-001

**Regras relacionadas:** RN-GEO-001, RN-GEO-005, RN-GEO-006

**Critérios de aceitação:**

1. Dado que o código da camada é novo, quando o técnico cadastra, então a camada é criada
2. Dado que o código já existe, quando o técnico cadastra, então o sistema recusa com HTTP 409 (RN-GEO-001)
3. Dado uma camada WMS sem URL, quando o técnico tenta ativar, então o sistema recusa (RN-GEO-006)
4. Dado uma camada desativada, quando o técnico tenta reativar, então o sistema recusa (RN-GEO-006).
### HU-GEO-002 — Compor mapas temáticos com camadas

**Como** como gestor do geoportal,
**quero** definir as camadas que compõem cada mapa, com ordem e opacidade,
**para** publicar mapas consistentes e controláveis.

**Capacidade:** CAP-GEO-003

**Regras relacionadas:** RN-GEO-004, RN-GEO-006, RN-GEO-008

**Critérios de aceitação:**

1. Dado um mapa em rascunho e uma camada ativa, quando o gestor compõe, então o vínculo é criado
2. Dado que a camada já está na composição, quando o gestor tenta incluir de novo, então o sistema recusa (RN-GEO-004)
3. Dado um mapa publicado, quando o gestor tenta alterar a composição, então o sistema recusa (RN-GEO-004).
### HU-GEO-003 — Publicar mapas no geoportal

**Como** como gestor do geoportal,
**quero** publicar mapas temáticos e cadastrais para consulta pública,
**para** disponibilizar a cartografia oficial do município.

**Capacidade:** CAP-GEO-002

**Regras relacionadas:** RN-GEO-004, RN-GEO-005, RN-GEO-006

**Critérios de aceitação:**

1. Dado um mapa com ao menos uma camada ativa, quando o gestor publica, então o mapa passa a publicado
2. Dado um mapa sem camadas, quando o gestor tenta publicar, então o sistema recusa com HTTP 409 (RN-GEO-004)
3. Dado um mapa publicado, quando o gestor arquiva, então o mapa passa a arquivado (RN-GEO-004).
### HU-GEO-004 — Registrar pontos de interesse no mapa

**Como** como técnico de geoprocessamento,
**quero** registrar elementos geoespaciais com geometria validada,
**para** enriquecer a cartografia com equipamentos e referenciais.

**Capacidade:** CAP-GEO-004

**Regras relacionadas:** RN-GEO-003, RN-GEO-008

**Critérios de aceitação:**

1. Dado uma camada existente, quando o técnico registra um ponto com vértice válido, então o elemento é criado
2. Dado um polígono com menos de 3 vértices, quando o técnico registra, então o sistema recusa com HTTP 409 (RN-GEO-003)
3. Dado um elemento cuja camada foi desativada, quando o técnico registra, então o sistema recusa (RN-GEO-008).
### HU-GEO-005 — Publicar serviços de mapas para terceiros

**Como** como administrador de serviços geoespaciais,
**quero** cadastrar e manter serviços WMS, WFS, WMTS e XYZ,
**para** permitir a integração do geoportal com sistemas próprios e de terceiros.

**Capacidade:** CAP-GEO-005

**Regras relacionadas:** RN-GEO-005, RN-GEO-007

**Critérios de aceitação:**

1. Dado protocolo WMS com URL e camada publicada, quando o administrador cadastra, então o serviço é criado
2. Dado um serviço ativo sem URL, quando o administrador cadastra, então o sistema recusa (RN-GEO-007)
3. Dado um WFS sem nome de camada, quando o administrador cadastra, então o sistema recusa (RN-GEO-007).
### HU-GEO-006 — Consultar a cartografia municipal

**Como** como cidadão,
**quero** consultar mapas publicados e elementos geoespaciais,
**para** acesso à informação espacial oficial do município.

**Capacidade:** CAP-GEO-006

**Regras relacionadas:** RN-GEO-003, RN-GEO-004

**Critérios de aceitação:**

1. Dado que existem mapas publicados, quando o cidadão consulta, então os mapas são retornados
2. Dado que a camada é informada, quando o cidadão lista elementos, então somente os elementos da camada são retornados (RN-GEO-008)
3. Dado um identificador inexistente, quando o cidadão consulta, então o sistema responde HTTP 404.

# 4. Rastreabilidade às Capacidades

| História | Capacidade | Regras |
| --- | | --- | |
| HU-GEO-001 — Manter as camadas do geoportal | CAP-GEO-001 | RN-GEO-001, RN-GEO-005, RN-GEO-006 |
| HU-GEO-002 — Compor mapas temáticos com camadas | CAP-GEO-003 | RN-GEO-004, RN-GEO-006, RN-GEO-008 |
| HU-GEO-003 — Publicar mapas no geoportal | CAP-GEO-002 | RN-GEO-004, RN-GEO-005, RN-GEO-006 |
| HU-GEO-004 — Registrar pontos de interesse no mapa | CAP-GEO-004 | RN-GEO-003, RN-GEO-008 |
| HU-GEO-005 — Publicar serviços de mapas para terceiros | CAP-GEO-005 | RN-GEO-005, RN-GEO-007 |
| HU-GEO-006 — Consultar a cartografia municipal | CAP-GEO-006 | RN-GEO-003, RN-GEO-004 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 006-Historias-de-Usuario-Geoinformacao-Municipal.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_geoinformacao`. Alterações no código devem ser
> refletidas reexecutando o gerador.
