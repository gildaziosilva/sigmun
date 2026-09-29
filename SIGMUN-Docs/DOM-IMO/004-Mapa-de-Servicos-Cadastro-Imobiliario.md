# 004 – Mapa de Serviços – Cadastro Imobiliário

#### Mapa de Serviços – Cadastro Imobiliário

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IMO-004

**Domínio:** Cadastro Imobiliário

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Cadastro-Imobiliario.md`
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

Este artefato cataloga os serviços expostos pelo domínio de Cadastro Imobiliário por
meio da API REST, relacionando cada operação às capacidades e requisitos que a
sustentam.

---

# 2. Convenções

* O contrato é versionado sob o prefixo `/api/v1/imo`.
* Operações de escrita devolvem `409 Conflict` quando violam regra de negócio e
  `404 Not Found` quando o recurso referenciado não existe.
* Ações de transição de estado são expostas como `POST` em sub-recursos.
* A listagem é paginada por `page` e `page_size` (1 a 100).

---

# 3. Serviços Expostos

| Método | Caminho | Operação |
| --- | | --- | |
| GET | /api/v1/imo/avaliacoes | Listar ou consultar avaliacoes |
| POST | /api/v1/imo/avaliacoes | Registrar ação sobre avaliacoes |
| GET | /api/v1/imo/avaliacoes/imovel/{imovel_id} | Consultar avaliacoes por identificador |
| GET | /api/v1/imo/avaliacoes/{avaliacao_id} | Consultar avaliacoes por identificador |
| POST | /api/v1/imo/avaliacoes/{avaliacao_id}/concluir | Registrar ação sobre avaliacoes |
| POST | /api/v1/imo/avaliacoes/{avaliacao_id}/cancelar | Registrar ação sobre avaliacoes |
| GET | /api/v1/imo/caracteristicas | Listar ou consultar caracteristicas |
| POST | /api/v1/imo/caracteristicas | Registrar ação sobre caracteristicas |
| GET | /api/v1/imo/caracteristicas/imovel/{imovel_id} | Consultar caracteristicas por identificador |
| GET | /api/v1/imo/geometrias | Listar ou consultar geometrias |
| POST | /api/v1/imo/geometrias | Registrar ação sobre geometrias |
| GET | /api/v1/imo/geometrias/imovel/{imovel_id} | Consultar geometrias por identificador |
| GET | /api/v1/imo/imoveis | Listar ou consultar imoveis |
| POST | /api/v1/imo/imoveis | Registrar ação sobre imoveis |
| GET | /api/v1/imo/imoveis/inscricao/{inscricao} | Consultar imoveis por identificador |
| GET | /api/v1/imo/imoveis/logradouro/{logradouro_id} | Consultar imoveis por identificador |
| GET | /api/v1/imo/imoveis/bairro/{bairro_id} | Consultar imoveis por identificador |
| DELETE | /api/v1/imo/imoveis/{imovel_id} | Excluir imoveis (exclusão lógica) |
| GET | /api/v1/imo/imoveis/{imovel_id} | Consultar imoveis por identificador |
| PATCH | /api/v1/imo/imoveis/{imovel_id} | Atualizar imoveis |
| POST | /api/v1/imo/imoveis/{imovel_id}/situacao | Registrar ação sobre imoveis |
| GET | /api/v1/imo/imoveis/{imovel_id}/proprietarios | Consultar imoveis por identificador |
| GET | /api/v1/imo/proprietarios | Listar ou consultar proprietarios |
| POST | /api/v1/imo/proprietarios | Registrar ação sobre proprietarios |
| DELETE | /api/v1/imo/proprietarios/{vinculo_id} | Excluir proprietarios (exclusão lógica) |


---

# 4. Quantidades

| Indicador | Quantidade |
| --- | |
| Paths publicados | 18 |
| Operações | 25 |
| Prefixo | `/api/v1/imo` |


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

**Documento:** 004-Mapa-de-Servicos-Cadastro-Imobiliario.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_cadastro_imobiliario`. Alterações no código devem ser
> refletidas reexecutando o gerador.
