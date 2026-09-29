# 010 – Especificações – Geoinformação Municipal

#### Especificações – Geoinformação Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GEO-010

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

Este artefato detalha as especificações de interface do domínio de
Geoinformação Municipal: contrato REST, esquema de persistência e convenções de
identificação.

---

# 2. Contrato de Interface

* **Base:** `/api/v1/geo`
* **Formato:** JSON sobre HTTP
* **Autenticação:** **não aplicada** — as rotas deste domínio não exigem token;
  a lacuna está registrada no artefato 016 (verifique antes de expor em produção)
* **Erros de negócio:** `409 Conflict` com mensagem descritiva
* **Recurso inexistente:** `404 Not Found`
* **Validação de entrada:** `422 Unprocessable Entity`
* **Listagem:** `page` (a partir de 1) e `page_size` (1 a 100)

---

# 3. Operações

| Método | Caminho | Finalidade |
| --- | | --- | |
| GET | /api/v1/geo/camadas | Listar ou consultar camadas |
| POST | /api/v1/geo/camadas | Registrar ação sobre camadas |
| DELETE | /api/v1/geo/camadas/{camada_id} | Excluir camadas (exclusão lógica) |
| GET | /api/v1/geo/camadas/{camada_id} | Consultar camadas por identificador |
| PATCH | /api/v1/geo/camadas/{camada_id} | Atualizar camadas |
| POST | /api/v1/geo/camadas/{camada_id}/ativar | Registrar ação sobre camadas |
| POST | /api/v1/geo/camadas/{camada_id}/desativar | Registrar ação sobre camadas |
| GET | /api/v1/geo/mapas | Listar ou consultar mapas |
| POST | /api/v1/geo/mapas | Registrar ação sobre mapas |
| DELETE | /api/v1/geo/mapas/{mapa_id} | Excluir mapas (exclusão lógica) |
| GET | /api/v1/geo/mapas/{mapa_id} | Consultar mapas por identificador |
| PATCH | /api/v1/geo/mapas/{mapa_id} | Atualizar mapas |
| POST | /api/v1/geo/mapas/{mapa_id}/publicar | Registrar ação sobre mapas |
| POST | /api/v1/geo/mapas/{mapa_id}/arquivar | Registrar ação sobre mapas |
| GET | /api/v1/geo/mapas/{mapa_id}/composicao | Consultar mapas por identificador |
| POST | /api/v1/geo/mapas/{mapa_id}/composicao | Registrar ação sobre mapas |
| DELETE | /api/v1/geo/mapas/{mapa_id}/composicao/{vinculo_id} | Excluir mapas (exclusão lógica) |
| GET | /api/v1/geo/features | Listar ou consultar features |
| POST | /api/v1/geo/features | Registrar ação sobre features |
| GET | /api/v1/geo/features/camada/{camada_id} | Consultar features por identificador |
| DELETE | /api/v1/geo/features/{feature_id} | Excluir features (exclusão lógica) |
| GET | /api/v1/geo/features/{feature_id} | Consultar features por identificador |
| GET | /api/v1/geo/servicos | Listar ou consultar servicos |
| POST | /api/v1/geo/servicos | Registrar ação sobre servicos |
| DELETE | /api/v1/geo/servicos/{servico_id} | Excluir servicos (exclusão lógica) |
| GET | /api/v1/geo/servicos/{servico_id} | Consultar servicos por identificador |
| PATCH | /api/v1/geo/servicos/{servico_id} | Atualizar servicos |
| POST | /api/v1/geo/servicos/{servico_id}/inativar | Registrar ação sobre servicos |


---

# 4. Modelo de Persistência

| Schema | Tabela | Colunas | Chave natural / restrição |
| --- | | --- | | --- | |
| `geo` | `camadas_mapa` | 19 | codigo |
| `geo` | `mapas_sig` | 22 | codigo |
| `geo` | `mapas_camadas` | 10 | — |
| `geo` | `features_geo` | 16 | — |
| `geo` | `servicos_geo` | 17 | codigo |


---

# 5. Convenções de Identificação

* **Identificador interno:** UUID v4, gerado pela aplicação.
* **Chave natural:** código cadastral, textual e estável.
* **Exclusão:** lógica, por meio do campo `is_deleted`, preservando o histórico
  fiscal e fundiário.

---

# 6. Regras Aplicadas na Interface

| Regra | Efeito observável na API |
| --- | |
| RN-GEO-001 | O código da camada de mapa é único no geoportal municipal; código e nome são obrigatórios. |
| RN-GEO-002 | O código do mapa SIG é único no geoportal municipal; código e nome são obrigatórios. |
| RN-GEO-003 | O elemento geoespacial exige geometria suportada, coordenadas no intervalo do datum e quantidade de vértices compatível com o tipo de geometria (ponto 1, linha 2, polígono 3). |
| RN-GEO-004 | O mapa percorre `RASCUNHO -> PUBLICADO -> ARQUIVADO`, sem retorno a partir de `ARQUIVADO`. Somente mapas em rascunho aceitam alteração de composição, a publicação exige ao menos uma camada ativa e mapa publicado não pode ser excluído diretamente. |
| RN-GEO-005 | A extensão (bbox) do mapa deve ser coerente, o SRID deve estar em faixa válida e a faixa de zoom deve respeitar `zoom_minimo <= zoom_inicial <= zoom_maximo`. |
| RN-GEO-006 | A camada percorre `RASCUNHO -> ATIVA -> DESATIVADA`, sem retorno a partir de `DESATIVADA`. Camada ativa cujo formato seja de serviço (WMS, WFS, WMTS, XYZ) exige URL preenchida, e somente camada ativa compõe mapa. |
| RN-GEO-007 | O serviço geoespacial exige código e nome únicos, URL válida iniciada por `http://` ou `https://` quando ativo e, nos protocolos WMS e WFS, o nome da camada publicada. |
| RN-GEO-008 | Todo elemento geoespacial pertence a uma camada cadastrada e não desativada; toda camada da composição de um mapa é uma camada cadastrada; a mesma camada não integra duas vezes o mesmo mapa. |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 010-Especificacoes-Geoinformacao-Municipal.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_geoinformacao`. Alterações no código devem ser
> refletidas reexecutando o gerador.
