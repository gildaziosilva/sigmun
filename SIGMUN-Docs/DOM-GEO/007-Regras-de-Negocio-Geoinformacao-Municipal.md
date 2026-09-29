# 007 – Regras de Negócio – Geoinformação Municipal

#### Regras de Negócio – Geoinformação Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GEO-007

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

Este artefato consolida as regras de negócio do domínio de Geoinformação Municipal,
declarando as invariantes que a implementação deve preservar.

---

# 2. Convenção de Identificação

As regras seguem o padrão `RN-<DOMÍNIO>-<sequencial>`, onde o número é sequencial
e estável. A numeração não é reutilizada após a revogação de uma regra.

---

# 3. Classificação das Regras

| Tipo | Regras | Significado |
| --- | | --- | |
| Máquina de estados | RN-GEO-004, RN-GEO-006 | Governa as transições permitidas entre situações. |
| Restrição | RN-GEO-001, RN-GEO-002, RN-GEO-003, RN-GEO-005, RN-GEO-007, RN-GEO-008 | Limita os estados ou valores aceitos pelo domínio. |


---

# 4. Regras de Negócio

## RN-GEO-001 — Unicidade do Código da Camada

**Tipo:** Restrição

**Processo:** PRO-GEO-001

**Descrição:** O código da camada de mapa é único no geoportal municipal; código e nome são obrigatórios.

**Justificativa:** O código é a chave natural usada na composição dos mapas e nos clientes que consomem o geoportal.

**Garantia técnica:** Restrição UNIQUE em `geo.camadas_mapa.codigo` e validação em `CamadaMapa.validar()`.

---
## RN-GEO-002 — Unicidade do Código do Mapa

**Tipo:** Restrição

**Processo:** PRO-GEO-003

**Descrição:** O código do mapa SIG é único no geoportal municipal; código e nome são obrigatórios.

**Justificativa:** O código identifica o mapa publicado e é referenciado por portais e aplicações que consomem o geoportal.

**Garantia técnica:** Restrição UNIQUE em `geo.mapas_sig.codigo` e validação em `MapaSig.validar()`.

---
## RN-GEO-003 — Integridade da Geometria do Elemento

**Tipo:** Restrição

**Processo:** PRO-GEO-004

**Descrição:** O elemento geoespacial exige geometria suportada, coordenadas no intervalo do datum e quantidade de vértices compatível com o tipo de geometria (ponto 1, linha 2, polígono 3).

**Justificativa:** Geometria inválida corromperia a camada e a visualização no visor cartográfico.

**Garantia técnica:** Checks `ck_geo_feature_vertices` e `ck_geo_feature_coordenadas`, e validação em `FeatureGeo.validar()`.

---
## RN-GEO-004 — Ciclo de Vida do Mapa e Congelamento da Composição

**Tipo:** Máquina de estados

**Processo:** PRO-GEO-003

**Descrição:** O mapa percorre `RASCUNHO -> PUBLICADO -> ARQUIVADO`, sem retorno a partir de `ARQUIVADO`. Somente mapas em rascunho aceitam alteração de composição, a publicação exige ao menos uma camada ativa e mapa publicado não pode ser excluído diretamente.

**Justificativa:** A composição publicada é o produto cartográfico entregue ao cidadão e deve permanecer estável para consulta e cache.

**Garantia técnica:** Transições em `MapaSig.publicar()` e `.arquivar()`, e verificações nos casos de uso de composição e exclusão.

---
## RN-GEO-005 — Coerência Cartográfica do Mapa e do Serviço

**Tipo:** Restrição

**Processo:** PRO-GEO-003

**Descrição:** A extensão (bbox) do mapa deve ser coerente, o SRID deve estar em faixa válida e a faixa de zoom deve respeitar `zoom_minimo <= zoom_inicial <= zoom_maximo`.

**Justificativa:** Parâmetros incoerentes impedem a exibição correta do mapa no visor.

**Garantia técnica:** Checks `ck_geo_mapa_zoom`, `ck_geo_mapa_extensao`, `ck_geo_camada_zoom` e `ck_geo_servico_zoom`, e validação nas entidades.

---
## RN-GEO-006 — Ciclo de Vida da Camada e Exigência de URL de Serviço

**Tipo:** Máquina de estados

**Processo:** PRO-GEO-001

**Descrição:** A camada percorre `RASCUNHO -> ATIVA -> DESATIVADA`, sem retorno a partir de `DESATIVADA`. Camada ativa cujo formato seja de serviço (WMS, WFS, WMTS, XYZ) exige URL preenchida, e somente camada ativa compõe mapa.

**Justificativa:** Camada publicada sem endpoint válido quebraria a exibição do mapa no geoportal.

**Garantia técnica:** Check `ck_geo_camada_servico_url`, transições em `CamadaMapa.ativar()`/`.desativar()` e validação na composição.

---
## RN-GEO-007 — Validação do Serviço Geoespacial

**Tipo:** Restrição

**Processo:** PRO-GEO-005

**Descrição:** O serviço geoespacial exige código e nome únicos, URL válida iniciada por `http://` ou `https://` quando ativo e, nos protocolos WMS e WFS, o nome da camada publicada.

**Justificativa:** Serviço sem endpoint ou sem camada identificável não é consumível por terceiros.

**Garantia técnica:** Checks `ck_geo_servico_url` e `ck_geo_servico_camada`, e validação em `ServicoGeo.validar()`.

---
## RN-GEO-008 — Vinculação do Elemento Geoespacial e da Composição

**Tipo:** Restrição

**Processo:** PRO-GEO-004

**Descrição:** Todo elemento geoespacial pertence a uma camada cadastrada e não desativada; toda camada da composição de um mapa é uma camada cadastrada; a mesma camada não integra duas vezes o mesmo mapa.

**Justificativa:** Referências órfãs impediriam a consulta e a consistência da base cartográfica.

**Garantia técnica:** Validações em `FeatureGeo.validar()` e nos casos de uso de registro e de composição; índice único parcial `uq_geo_mapa_camada`.

---

---

# 5. Matriz de Decisão

| Regra | Processo | Garantia no banco | Testada por |
| --- | | --- | | --- | |
| RN-GEO-001 | PRO-GEO-001 | Restrição UNIQUE em `geo.camadas_mapa.codigo` e validação em `CamadaMapa.validar()`. | 0 teste(s) |
| RN-GEO-002 | PRO-GEO-003 | Restrição UNIQUE em `geo.mapas_sig.codigo` e validação em `MapaSig.validar()`. | 0 teste(s) |
| RN-GEO-003 | PRO-GEO-004 | Checks `ck_geo_feature_vertices` e `ck_geo_feature_coordenadas`, e validação em `FeatureGeo.validar()`. | 0 teste(s) |
| RN-GEO-004 | PRO-GEO-003 | Transições em `MapaSig.publicar()` e `.arquivar()`, e verificações nos casos de uso de composição e exclusão. | 0 teste(s) |
| RN-GEO-005 | PRO-GEO-003 | Checks `ck_geo_mapa_zoom`, `ck_geo_mapa_extensao`, `ck_geo_camada_zoom` e `ck_geo_servico_zoom`, e validação nas entidades. | 0 teste(s) |
| RN-GEO-006 | PRO-GEO-001 | Check `ck_geo_camada_servico_url`, transições em `CamadaMapa.ativar()`/`.desativar()` e validação na composição. | 0 teste(s) |
| RN-GEO-007 | PRO-GEO-005 | Checks `ck_geo_servico_url` e `ck_geo_servico_camada`, e validação em `ServicoGeo.validar()`. | 0 teste(s) |
| RN-GEO-008 | PRO-GEO-004 | Validações em `FeatureGeo.validar()` e nos casos de uso de registro e de composição; índice único parcial `uq_geo_mapa_camada`. | 0 teste(s) |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 007-Regras-de-Negocio-Geoinformacao-Municipal.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_geoinformacao`. Alterações no código devem ser
> refletidas reexecutando o gerador.
