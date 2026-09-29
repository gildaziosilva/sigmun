# 026 – Modelo de Domínio – Geoinformação Municipal

#### Modelo de Domínio – Geoinformação Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GEO-026

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

Este artefato descreve o modelo de domínio de Geoinformação Municipal: entidades,
invariantes, estados e as regras que os governam.

---

# 2. Conceitos Centrais

| Entidade | Responsabilidade |
| --- | |
| CamadaMapa | Camada cartográfica disponibilizada no geoportal. |
| MapaSig | Mapa publicado no geoportal municipal. |
| MapaCamada | Vínculo de composição entre mapa e camada. |
| FeatureGeo | Elemento geoespacial (ponto de interesse) de uma camada. |
| ServicoGeo | Serviço geoespacial publicado (WMS, WFS, WMTS, XYZ ou REST). |


---

# 3. Invariantes por Entidade

### CamadaMapa

Camada cartográfica disponibilizada no geoportal.

* **Invariantes:** Campos obrigatórios conforme o schema.
* **Estados:** —

### MapaSig

Mapa publicado no geoportal municipal.

* **Invariantes:** Campos obrigatórios conforme o schema.
* **Estados:** —

### MapaCamada

Vínculo de composição entre mapa e camada.

* **Invariantes:** Campos obrigatórios conforme o schema.
* **Estados:** —

### FeatureGeo

Elemento geoespacial (ponto de interesse) de uma camada.

* **Invariantes:** Campos obrigatórios conforme o schema.
* **Estados:** —

### ServicoGeo

Serviço geoespacial publicado (WMS, WFS, WMTS, XYZ ou REST).

* **Invariantes:** Campos obrigatórios conforme o schema.
* **Estados:** —

---

# 4. Regras e Estados

| Regra | Tipo | Entidades afetadas | Garantia técnica |
| --- | | --- | | --- | |
| RN-GEO-001 | Restrição | — | Restrição UNIQUE em `geo.camadas_mapa.codigo` e validação em `CamadaMapa.validar()`. |
| RN-GEO-002 | Restrição | — | Restrição UNIQUE em `geo.mapas_sig.codigo` e validação em `MapaSig.validar()`. |
| RN-GEO-003 | Restrição | — | Checks `ck_geo_feature_vertices` e `ck_geo_feature_coordenadas`, e validação em `FeatureGeo.validar()`. |
| RN-GEO-004 | Máquina de estados | — | Transições em `MapaSig.publicar()` e `.arquivar()`, e verificações nos casos de uso de composição e exclusão. |
| RN-GEO-005 | Restrição | — | Checks `ck_geo_mapa_zoom`, `ck_geo_mapa_extensao`, `ck_geo_camada_zoom` e `ck_geo_servico_zoom`, e validação nas entidades. |
| RN-GEO-006 | Máquina de estados | — | Check `ck_geo_camada_servico_url`, transições em `CamadaMapa.ativar()`/`.desativar()` e validação na composição. |
| RN-GEO-007 | Restrição | — | Checks `ck_geo_servico_url` e `ck_geo_servico_camada`, e validação em `ServicoGeo.validar()`. |
| RN-GEO-008 | Restrição | — | Validações em `FeatureGeo.validar()` e nos casos de uso de registro e de composição; índice único parcial `uq_geo_mapa_camada`. |


---

# 5. Modelo Conceitual

O domínio se articula em três eixos:

* **Território:** a divisão territorial organiza o território e a malha viária.
* **Valor:** a planta genérica de valores estabelece os parâmetros que sustentam
  a apuração.
* **Fundo de terra:** o cadastro imobiliário registra o lote, sua titularidade,
  sua construção e sua geometria.

---

# 6. Limites do Modelo

* As referências entre domínios são identificadores opacos, sem FK física.
* A exclusão é lógica em todos os cadastros, preservando o histórico.
* Estados terminais, como `DEMOLIDO` e `REVOGADA`, são irreversíveis por regra.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 026-Modelo-de-Dominio-Geoinformacao-Municipal.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_geoinformacao`. Alterações no código devem ser
> refletidas reexecutando o gerador.
