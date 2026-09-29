# 003 – Mapa de Processos – Geoinformação Municipal

#### Mapa de Processos – Geoinformação Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GEO-003

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

Este artefato descreve os processos de negócio do domínio de Geoinformação Municipal,
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
| PRO-GEO-001 | Manter camada cartográfica | Aquisição de nova base geoespacial, atualização de base existente ou correção de metadado. | Manter camadas cartográficas identificáveis e tecnicamente consistentes. |
| PRO-GEO-002 | Compor mapa com camadas ativas | Elaboração de novo mapa temático ou atualização da composição de mapa em rascunho. | Compor o mapa exclusivamente com camadas aptas a publicação. |
| PRO-GEO-003 | Publicar mapa no geoportal | Mapa temático ou cadastral aprovado para disponibilização ao público. | Publicar mapa com conteúdo cartográfico verificável. |
| PRO-GEO-004 | Registrar elemento geoespacial | Levantamento de campo, cadastro de ponto de interesse ou correção de geometria. | Manter elementos georreferenciados consistentes com a camada de destino. |
| PRO-GEO-005 | Publicar serviço geoespacial | Disponibilização de novo serviço de mapa ou ajuste de endpoint existente. | Manter serviços de publicação válidos e coerentes com o protocolo declarado. |
| PRO-GEO-006 | Consultar mapa e serviço publicado | Necessidade de informação espacial por parte do público ou de servidores. | Disponibilizar a informação cartográfica publicada. |


---

# 4. Detalhamento

### PRO-GEO-001 — Manter camada cartográfica

**Gatilho:** Aquisição de nova base geoespacial, atualização de base existente ou correção de metadado.

**Objetivo:** Manter camadas cartográficas identificáveis e tecnicamente consistentes.

**Entradas:** Código; nome; tipo; formato; fonte; datum; SRID; faixa de zoom; URL de serviço

**Saídas:** Camada cadastrada, atualizada, ativada ou desativada

**Regras aplicadas:** RN-GEO-001, RN-GEO-005, RN-GEO-006

**Passos:**

1. Verificar se o código da camada já está cadastrado (RN-GEO-001).
2. Preencher os dados da camada, incluindo datum, SRID e faixa de zoom.
3. Informar a URL de serviço quando o formato exigir (RN-GEO-006).
4. Gravar a camada e registrar autoria e data.

---
### PRO-GEO-002 — Compor mapa com camadas ativas

**Gatilho:** Elaboração de novo mapa temático ou atualização da composição de mapa em rascunho.

**Objetivo:** Compor o mapa exclusivamente com camadas aptas a publicação.

**Entradas:** Mapa em rascunho; camada ativa; ordem; opacidade; rótulo

**Saídas:** Vínculo de composição criado ou removido

**Regras aplicadas:** RN-GEO-004, RN-GEO-006, RN-GEO-008

**Passos:**

1. Selecionar o mapa, que deve estar em rascunho (RN-GEO-004).
2. Selecionar a camada, que deve estar ativa (RN-GEO-006).
3. Impedir a inclusão da mesma camada duas vezes no mesmo mapa (RN-GEO-004).
4. Gravar o vínculo com ordem, opacidade e visibilidade.

---
### PRO-GEO-003 — Publicar mapa no geoportal

**Gatilho:** Mapa temático ou cadastral aprovado para disponibilização ao público.

**Objetivo:** Publicar mapa com conteúdo cartográfico verificável.

**Entradas:** Mapa em rascunho; composição de camadas

**Saídas:** Mapa publicado com data de publicação

**Regras aplicadas:** RN-GEO-004, RN-GEO-005, RN-GEO-006

**Passos:**

1. Verificar que o mapa possui ao menos uma camada na composição (RN-GEO-004).
2. Verificar que todas as camadas da composição estão ativas (RN-GEO-004, RN-GEO-006).
3. Publicar o mapa e registrar a data de publicação.

---
### PRO-GEO-004 — Registrar elemento geoespacial

**Gatilho:** Levantamento de campo, cadastro de ponto de interesse ou correção de geometria.

**Objetivo:** Manter elementos georreferenciados consistentes com a camada de destino.

**Entradas:** Código; nome; camada; geometria; vértices; datum; atributos

**Saídas:** Elemento geoespacial registrado ou excluído

**Regras aplicadas:** RN-GEO-003, RN-GEO-008

**Passos:**

1. Selecionar a camada de destino, que deve existir e não estar desativada (RN-GEO-008).
2. Verificar a unicidade do código dentro da camada.
3. Informar a geometria e os vértices, respeitando o mínimo do tipo (RN-GEO-003).
4. Gravar o elemento e registrar autoria e data.

---
### PRO-GEO-005 — Publicar serviço geoespacial

**Gatilho:** Disponibilização de novo serviço de mapa ou ajuste de endpoint existente.

**Objetivo:** Manter serviços de publicação válidos e coerentes com o protocolo declarado.

**Entradas:** Código; nome; protocolo; URL; camada publicada; datum; faixa de zoom

**Saídas:** Serviço cadastrado, atualizado ou inativado

**Regras aplicadas:** RN-GEO-005, RN-GEO-007

**Passos:**

1. Verificar se o código do serviço já está cadastrado (RN-GEO-007).
2. Informar a URL; para WMS e WFS, também a camada publicada (RN-GEO-007).
3. Gravar o serviço e registrar autoria e data.

---
### PRO-GEO-006 — Consultar mapa e serviço publicado

**Gatilho:** Necessidade de informação espacial por parte do público ou de servidores.

**Objetivo:** Disponibilizar a informação cartográfica publicada.

**Entradas:** Filtro opcional por tipo ou situação; camada de interesse

**Saídas:** Lista de mapas, elementos ou serviços

**Regras aplicadas:** RN-GEO-003, RN-GEO-004

**Passos:**

1. Informar o filtro de interesse, quando houver.
2. Retornar os registros, com paginação entre 1 e 100 itens por página.

---

# 5. Processos por Capacidade

| Processo | Capacidades | Regras |
| --- | | --- | |
| PRO-GEO-001 — Manter camada cartográfica | CAP-GEO-001 | RN-GEO-001, RN-GEO-005, RN-GEO-006 |
| PRO-GEO-002 — Compor mapa com camadas ativas | CAP-GEO-003 | RN-GEO-004, RN-GEO-006, RN-GEO-008 |
| PRO-GEO-003 — Publicar mapa no geoportal | CAP-GEO-002 | RN-GEO-004, RN-GEO-005, RN-GEO-006 |
| PRO-GEO-004 — Registrar elemento geoespacial | CAP-GEO-004 | RN-GEO-003, RN-GEO-008 |
| PRO-GEO-005 — Publicar serviço geoespacial | CAP-GEO-005 | RN-GEO-005, RN-GEO-007 |
| PRO-GEO-006 — Consultar mapa e serviço publicado | CAP-GEO-006 | RN-GEO-003, RN-GEO-004 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 003-Mapa-de-Processos-Geoinformacao-Municipal.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_geoinformacao`. Alterações no código devem ser
> refletidas reexecutando o gerador.
