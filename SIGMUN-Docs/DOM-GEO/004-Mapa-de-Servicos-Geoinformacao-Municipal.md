# 004 – Mapa de Serviços – Geoinformação Municipal

#### Mapa de Serviços – Geoinformação Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GEO-004

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

Este artefato cataloga os serviços expostos pelo domínio de Geoinformação Municipal por
meio da API REST, relacionando cada operação às capacidades e requisitos que a
sustentam.

---

# 2. Convenções

* O contrato é versionado sob o prefixo `/api/v1/geo`.
* Operações de escrita devolvem `409 Conflict` quando violam regra de negócio e
  `404 Not Found` quando o recurso referenciado não existe.
* Ações de transição de estado são expostas como `POST` em sub-recursos.
* A listagem é paginada por `page` e `page_size` (1 a 100).

---

# 3. Serviços Expostos

| Método | Caminho | Operação |
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

# 4. Quantidades

| Indicador | Quantidade |
| --- | |
| Paths publicados | 16 |
| Operações | 28 |
| Prefixo | `/api/v1/geo` |


---

# 5. Observações de Versionamento

* Alterações que removam campos ou mudem semântica exigem nova versão do prefixo.
* Novos campos aceitos em resposta são compatíveis com o contrato vigente.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 004-Mapa-de-Servicos-Geoinformacao-Municipal.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_geoinformacao`. Alterações no código devem ser
> refletidas reexecutando o gerador.
