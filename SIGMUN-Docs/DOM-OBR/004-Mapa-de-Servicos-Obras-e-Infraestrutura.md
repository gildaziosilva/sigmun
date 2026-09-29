# 004 – Mapa de Serviços – Obras e Infraestrutura

#### Mapa de Serviços – Obras e Infraestrutura

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OBR-004

**Domínio:** Obras e Infraestrutura

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Obras-e-Infraestrutura.md`
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

Este artefato cataloga os serviços expostos pelo domínio de Obras e Infraestrutura por
meio da API REST, relacionando cada operação às capacidades e requisitos que a
sustentam.

---

# 2. Convenções

* O contrato é versionado sob o prefixo `/api/v1/obr`.
* Operações de escrita devolvem `409 Conflict` quando violam regra de negócio e
  `404 Not Found` quando o recurso referenciado não existe.
* Ações de transição de estado são expostas como `POST` em sub-recursos.
* A listagem é paginada por `page` e `page_size` (1 a 100).

---

# 3. Serviços Expostos

| Método | Caminho | Operação |
| --- | | --- | |
| GET | /api/v1/obr/obras/{obra_id}/acompanhamento | Consultar obras por identificador |
| POST | /api/v1/obr/medicoes | Registrar ação sobre medicoes |
| GET | /api/v1/obr/obras/{obra_id}/medicoes | Consultar obras por identificador |
| POST | /api/v1/obr/medicoes/{medicao_id}/aprovar | Registrar ação sobre medicoes |
| POST | /api/v1/obr/medicoes/{medicao_id}/glosar | Registrar ação sobre medicoes |
| POST | /api/v1/obr/medicoes/{medicao_id}/cancelar | Registrar ação sobre medicoes |
| POST | /api/v1/obr/despesas | Registrar ação sobre despesas |
| GET | /api/v1/obr/obras/{obra_id}/despesas | Consultar obras por identificador |
| DELETE | /api/v1/obr/despesas/{despesa_id} | Excluir despesas (exclusão lógica) |
| POST | /api/v1/obr/etapas | Registrar ação sobre etapas |
| GET | /api/v1/obr/obras/{obra_id}/etapas | Consultar obras por identificador |
| PATCH | /api/v1/obr/etapas/{etapa_id} | Atualizar etapas |
| POST | /api/v1/obr/etapas/{etapa_id}/concluir | Registrar ação sobre etapas |
| POST | /api/v1/obr/vistorias | Registrar ação sobre vistorias |
| GET | /api/v1/obr/obras/{obra_id}/vistorias | Consultar obras por identificador |
| GET | /api/v1/obr/obras | Listar ou consultar obras |
| POST | /api/v1/obr/obras | Registrar ação sobre obras |
| DELETE | /api/v1/obr/obras/{obra_id} | Excluir obras (exclusão lógica) |
| GET | /api/v1/obr/obras/{obra_id} | Consultar obras por identificador |
| PATCH | /api/v1/obr/obras/{obra_id} | Atualizar obras |
| POST | /api/v1/obr/obras/{obra_id}/iniciar-execucao | Registrar ação sobre obras |
| POST | /api/v1/obr/obras/{obra_id}/suspender | Registrar ação sobre obras |
| POST | /api/v1/obr/obras/{obra_id}/concluir | Registrar ação sobre obras |
| POST | /api/v1/obr/obras/{obra_id}/cancelar | Registrar ação sobre obras |


---

# 4. Quantidades

| Indicador | Quantidade |
| --- | |
| Paths publicados | 21 |
| Operações | 24 |
| Prefixo | `/api/v1/obr` |


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

**Documento:** 004-Mapa-de-Servicos-Obras-e-Infraestrutura.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_obras`. Alterações no código devem ser
> refletidas reexecutando o gerador.
