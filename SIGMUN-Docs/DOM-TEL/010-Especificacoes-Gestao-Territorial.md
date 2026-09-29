# 010 – Especificações – Gestão Territorial

#### Especificações – Gestão Territorial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TEL-010

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

Este artefato detalha as especificações de interface do domínio de
Gestão Territorial: contrato REST, esquema de persistência e convenções de
identificação.

---

# 2. Contrato de Interface

* **Base:** `/api/v1/tel`
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

# 4. Modelo de Persistência

| Schema | Tabela | Colunas | Chave natural / restrição |
| --- | | --- | | --- | |
| `tel` | `bairros` | 11 | codigo |
| `tel` | `logradouros` | 13 | codigo |
| `tel` | `planta_generica_valores` | 13 | — |
| `tel` | `georreferencias` | 15 | — |


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
| RN-TEL-001 | O código da divisão territorial é único no cadastro municipal; código e nome são obrigatórios. |
| RN-TEL-002 | O código do logradouro é único e todo logradouro pertence a uma divisão territorial cadastrada. |
| RN-TEL-003 | Existe no máximo uma planta vigente para cada combinação de ano, divisão e ocupação. |
| RN-TEL-004 | A planta percorre `RASCUNHO -> VIGENTE -> REVOGADA`, sem retorno a partir de `REVOGADA`; a revogação exige justificativa e somente plantas em rascunho podem ser editadas. |
| RN-TEL-005 | A georreferência exige datum suportado, está vinculada a uma divisão **ou** a um logradouro (nunca a ambos), e seus vértices são validados quanto à faixa de coordenadas e à quantidade mínima do tipo de geometria. |
| RN-TEL-006 | Uma divisão territorial com logradouros ativos não pode ser excluída. |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 010-Especificacoes-Gestao-Territorial.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_territorial`. Alterações no código devem ser
> refletidas reexecutando o gerador.
