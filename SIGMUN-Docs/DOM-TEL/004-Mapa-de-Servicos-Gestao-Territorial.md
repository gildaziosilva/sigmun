# 004 – Mapa de Serviços – Gestão Territorial

#### Mapa de Serviços – Gestão Territorial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TEL-004

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

Este artefato cataloga os serviços expostos pelo domínio de Gestão Territorial por
meio da API REST, relacionando cada operação às capacidades e requisitos que a
sustentam.

---

# 2. Convenções

* O contrato é versionado sob o prefixo `/api/v1/tel`.
* Operações de escrita devolvem `409 Conflict` quando violam regra de negócio e
  `404 Not Found` quando o recurso referenciado não existe.
* Ações de transição de estado são expostas como `POST` em sub-recursos.
* A listagem é paginada por `page` e `page_size` (1 a 100).

---

# 3. Serviços Expostos

| Método | Caminho | Operação |
| --- | | --- | |
| GET | /api/v1/tel/georreferencias | Listar ou consultar georreferencias |
| POST | /api/v1/tel/georreferencias | Registrar ação sobre georreferencias |
| GET | /api/v1/tel/georreferencias/referencia | Listar ou consultar georreferencias |
| DELETE | /api/v1/tel/georreferencias/{georreferencia_id} | Excluir georreferencias (exclusão lógica) |
| GET | /api/v1/tel/georreferencias/{georreferencia_id} | Consultar georreferencias por identificador |
| GET | /api/v1/tel/plantas-valores | Listar ou consultar plantas-valores |
| POST | /api/v1/tel/plantas-valores | Registrar ação sobre plantas-valores |
| GET | /api/v1/tel/plantas-valores/vigente | Listar ou consultar plantas-valores |
| GET | /api/v1/tel/plantas-valores/{planta_id} | Consultar plantas-valores por identificador |
| PATCH | /api/v1/tel/plantas-valores/{planta_id} | Atualizar plantas-valores |
| POST | /api/v1/tel/plantas-valores/{planta_id}/ativar | Registrar ação sobre plantas-valores |
| POST | /api/v1/tel/plantas-valores/{planta_id}/revogar | Registrar ação sobre plantas-valores |
| GET | /api/v1/tel/bairros | Listar ou consultar bairros |
| POST | /api/v1/tel/bairros | Registrar ação sobre bairros |
| GET | /api/v1/tel/bairros/codigo/{codigo} | Consultar bairros por identificador |
| DELETE | /api/v1/tel/bairros/{bairro_id} | Excluir bairros (exclusão lógica) |
| GET | /api/v1/tel/bairros/{bairro_id} | Consultar bairros por identificador |
| PATCH | /api/v1/tel/bairros/{bairro_id} | Atualizar bairros |
| GET | /api/v1/tel/bairros/{bairro_id}/logradouros | Consultar bairros por identificador |
| GET | /api/v1/tel/logradouros | Listar ou consultar logradouros |
| POST | /api/v1/tel/logradouros | Registrar ação sobre logradouros |
| GET | /api/v1/tel/logradouros/codigo/{codigo} | Consultar logradouros por identificador |
| DELETE | /api/v1/tel/logradouros/{logradouro_id} | Excluir logradouros (exclusão lógica) |
| GET | /api/v1/tel/logradouros/{logradouro_id} | Consultar logradouros por identificador |
| PATCH | /api/v1/tel/logradouros/{logradouro_id} | Atualizar logradouros |


---

# 4. Quantidades

| Indicador | Quantidade |
| --- | |
| Paths publicados | 15 |
| Operações | 25 |
| Prefixo | `/api/v1/tel` |


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

**Documento:** 004-Mapa-de-Servicos-Gestao-Territorial.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_territorial`. Alterações no código devem ser
> refletidas reexecutando o gerador.
