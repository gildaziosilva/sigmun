# 005 – Casos de Uso – Geoinformação Municipal

#### Casos de Uso – Geoinformação Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GEO-005

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

Este artefato especifica os casos de uso do domínio de Geoinformação Municipal,
relacionando cada cenário à sua implementação na camada de casos de uso.

---

# 2. Convenções

* Casos de uso descrevem **cenários de negócio**; a implementação é referenciada
  pelo nome da classe de caso de uso correspondente.
* Cenários de consulta direta ao repositório são assim identificados, pois não
  exigem lógica de negócio própria.

---

# 3. Casos de Uso

### CU-GEO-001 — Cadastrar camada cartográfica

**Ator:** AT-GEO-001

**Capacidade:** CAP-GEO-001

**Pré-condições:** O servidor está autenticado e possui permissão de gestão cartográfica.

**Fluxo principal:**

1. Informar código, nome, tipo, formato, fonte, datum, SRID e faixa de zoom
2. verificar a unicidade do código (RN-GEO-001)
3. informar URL quando o formato exigir
4. gravar e registrar autoria e data.

**Pós-condições:** A camada está cadastrada em rascunho, ativa ou desativada conforme solicitado.

**Regras aplicadas:** RN-GEO-001, RN-GEO-005, RN-GEO-006

**Caso de uso implementador:** `CadastrarCamadaUseCase`
### CU-GEO-002 — Alterar camada cartográfica

**Ator:** AT-GEO-001

**Capacidade:** CAP-GEO-001

**Pré-condições:** A camada existe.

**Fluxo principal:**

1. Informar os campos a alterar
2. ao trocar o código, verificar a unicidade (RN-GEO-001)
3. gravar a alteração e registrar a data.

**Pós-condições:** A camada está atualizada.

**Regras aplicadas:** RN-GEO-001, RN-GEO-005

**Caso de uso implementador:** `AtualizarCamadaUseCase`
### CU-GEO-003 — Ativar camada cartográfica

**Ator:** AT-GEO-001

**Capacidade:** CAP-GEO-001

**Pré-condições:** A camada existe e não está desativada.

**Fluxo principal:**

1. Solicitar a ativação
2. exigir URL quando o formato for de serviço (RN-GEO-006)
3. alterar a situação para ativa.

**Pós-condições:** A camada está ativa e apta a compor mapas.

**Regras aplicadas:** RN-GEO-006

**Caso de uso implementador:** `AtivarCamadaUseCase`
### CU-GEO-004 — Desativar camada cartográfica

**Ator:** AT-GEO-001

**Capacidade:** CAP-GEO-001

**Pré-condições:** A camada existe e não está desativada.

**Fluxo principal:**

1. Solicitar a desativação
2. esconder a camada e alterar a situação para desativada (RN-GEO-006).

**Pós-condições:** A camada está desativada e indisponível para composição.

**Regras aplicadas:** RN-GEO-006

**Caso de uso implementador:** `DesativarCamadaUseCase`
### CU-GEO-005 — Excluir camada cartográfica

**Ator:** AT-GEO-001

**Capacidade:** CAP-GEO-001

**Pré-condições:** A camada existe.

**Fluxo principal:**

1. Solicitar a exclusão
2. verificar se a camada compõe mapa publicado (RN-GEO-004)
3. havendo dependência, recusar com HTTP 409
4. caso contrário, excluir logicamente.

**Pós-condições:** A camada está excluída logicamente e preserva o histórico.

**Regras aplicadas:** RN-GEO-004

**Caso de uso implementador:** `ExcluirCamadaUseCase`
### CU-GEO-006 — Cadastrar mapa SIG

**Ator:** AT-GEO-002

**Capacidade:** CAP-GEO-002

**Pré-condições:** O servidor está autenticado e possui permissão de gestão de mapas.

**Fluxo principal:**

1. Informar código, nome, tipo, datum, SRID, escala, faixa de zoom e extensão
2. verificar a unicidade do código (RN-GEO-002)
3. gravar o mapa em rascunho.

**Pós-condições:** O mapa está cadastrado em rascunho.

**Regras aplicadas:** RN-GEO-002, RN-GEO-005

**Caso de uso implementador:** `CadastrarMapaUseCase`
### CU-GEO-007 — Alterar mapa SIG

**Ator:** AT-GEO-002

**Capacidade:** CAP-GEO-002

**Pré-condições:** O mapa existe.

**Fluxo principal:**

1. Informar os campos a alterar
2. em mapa publicado, o código é imutável (RN-GEO-004)
3. gravar a alteração e registrar a data.

**Pós-condições:** O mapa está atualizado.

**Regras aplicadas:** RN-GEO-004, RN-GEO-005

**Caso de uso implementador:** `AtualizarMapaUseCase`
### CU-GEO-008 — Compor mapa com camada

**Ator:** AT-GEO-002

**Capacidade:** CAP-GEO-003

**Pré-condições:** O mapa existe e está em rascunho; a camada existe e está ativa.

**Fluxo principal:**

1. Selecionar mapa e camada
2. impedir duplicidade da camada no mapa (RN-GEO-004)
3. informar ordem, opacidade e visibilidade
4. gravar o vínculo.

**Pós-condições:** O mapa possui a camada em sua composição.

**Regras aplicadas:** RN-GEO-004, RN-GEO-006, RN-GEO-008

**Caso de uso implementador:** `ComporCamadaUseCase`
### CU-GEO-009 — Remover camada da composição do mapa

**Ator:** AT-GEO-002

**Capacidade:** CAP-GEO-003

**Pré-condições:** O vínculo existe e o mapa está em rascunho.

**Fluxo principal:**

1. Selecionar o vínculo
2. remover a composição (RN-GEO-004).

**Pós-condições:** A camada foi removida da composição do mapa.

**Regras aplicadas:** RN-GEO-004

**Caso de uso implementador:** `RemoverComposicaoUseCase`
### CU-GEO-010 — Publicar mapa no geoportal

**Ator:** AT-GEO-002

**Capacidade:** CAP-GEO-002

**Pré-condições:** O mapa existe e está em rascunho.

**Fluxo principal:**

1. Solicitar a publicação
2. exigir ao menos uma camada ativa na composição (RN-GEO-004)
3. alterar a situação para publicado e registrar a data.

**Pós-condições:** O mapa está publicado e disponível ao público.

**Regras aplicadas:** RN-GEO-004

**Caso de uso implementador:** `PublicarMapaUseCase`
### CU-GEO-011 — Arquivar mapa publicado

**Ator:** AT-GEO-002

**Capacidade:** CAP-GEO-002

**Pré-condições:** O mapa existe e está publicado.

**Fluxo principal:**

1. Solicitar o arquivamento
2. alterar a situação para arquivado (RN-GEO-004).

**Pós-condições:** O mapa está arquivado e saiu do geoportal, preservando o histórico.

**Regras aplicadas:** RN-GEO-004

**Caso de uso implementador:** `ArquivarMapaUseCase`
### CU-GEO-012 — Excluir mapa SIG

**Ator:** AT-GEO-002

**Capacidade:** CAP-GEO-002

**Pré-condições:** O mapa existe e não está publicado.

**Fluxo principal:**

1. Solicitar a exclusão
2. remover os vínculos de composição
3. excluir logicamente o mapa (RN-GEO-004).

**Pós-condições:** O mapa está excluído logicamente e preserva o histórico.

**Regras aplicadas:** RN-GEO-004

**Caso de uso implementador:** `ExcluirMapaUseCase`
### CU-GEO-013 — Registrar elemento geoespacial

**Ator:** AT-GEO-001

**Capacidade:** CAP-GEO-004

**Pré-condições:** A camada de destino existe e não está desativada.

**Fluxo principal:**

1. Selecionar a camada
2. informar geometria, vértices, datum e atributos
3. verificar o mínimo de vértices e a faixa de coordenadas (RN-GEO-003)
4. gravar o elemento.

**Pós-condições:** O elemento está registrado e vinculado à camada.

**Regras aplicadas:** RN-GEO-003, RN-GEO-008

**Caso de uso implementador:** `RegistrarFeatureUseCase`
### CU-GEO-014 — Excluir elemento geoespacial

**Ator:** AT-GEO-001

**Capacidade:** CAP-GEO-004

**Pré-condições:** O elemento existe.

**Fluxo principal:**

1. Solicitar a exclusão
2. excluir logicamente o elemento.

**Pós-condições:** O elemento está excluído logicamente.

**Regras aplicadas:** RN-GEO-003

**Caso de uso implementador:** `ExcluirFeatureUseCase`
### CU-GEO-015 — Cadastrar serviço geoespacial

**Ator:** AT-GEO-004

**Capacidade:** CAP-GEO-005

**Pré-condições:** O servidor está autenticado e possui permissão de gestão de serviços.

**Fluxo principal:**

1. Informar código, nome, protocolo, URL e camada publicada
2. verificar a unicidade do código e a coerência do serviço (RN-GEO-007)
3. gravar o serviço.

**Pós-condições:** O serviço geoespacial está cadastrado e ativo.

**Regras aplicadas:** RN-GEO-007

**Caso de uso implementador:** `CadastrarServicoUseCase`
### CU-GEO-016 — Alterar serviço geoespacial

**Ator:** AT-GEO-004

**Capacidade:** CAP-GEO-005

**Pré-condições:** O serviço existe.

**Fluxo principal:**

1. Informar os campos a alterar
2. ao trocar o código, verificar a unicidade (RN-GEO-007)
3. validar e gravar a alteração.

**Pós-condições:** O serviço está atualizado.

**Regras aplicadas:** RN-GEO-007

**Caso de uso implementador:** `AtualizarServicoUseCase`
### CU-GEO-017 — Inativar serviço geoespacial

**Ator:** AT-GEO-004

**Capacidade:** CAP-GEO-005

**Pré-condições:** O serviço existe e está ativo.

**Fluxo principal:**

1. Solicitar a inativação
2. alterar a situação para inativo (RN-GEO-007).

**Pós-condições:** O serviço está inativo e indisponível para consumo.

**Regras aplicadas:** RN-GEO-007

**Caso de uso implementador:** `InativarServicoUseCase`
### CU-GEO-018 — Excluir serviço geoespacial

**Ator:** AT-GEO-004

**Capacidade:** CAP-GEO-005

**Pré-condições:** O serviço existe.

**Fluxo principal:**

1. Solicitar a exclusão
2. excluir logicamente o serviço.

**Pós-condições:** O serviço está excluído logicamente.

**Regras aplicadas:** RN-GEO-007

**Caso de uso implementador:** `ExcluirServicoUseCase`
### CU-GEO-019 — Consultar mapas, elementos e serviços

**Ator:** AT-GEO-003

**Capacidade:** CAP-GEO-006

**Pré-condições:** Não há precondição.

**Fluxo principal:**

1. Informar o filtro de interesse, quando houver
2. retornar os registros com paginação (RF-GEO-002, RF-GEO-008, RF-GEO-009).

**Pós-condições:** Os registros foram obtidos ou a lista vazia foi informada.

**Regras aplicadas:** RN-GEO-004

**Caso de uso implementador:** — (consulta aos repositórios) (implementado como consulta ao repositório)

# 4. Cobertura

| Indicador | Quantidade |
| --- | |
| Casos de uso especificados | 19 |
| Casos de uso com classe implementadora | 18 |
| Histórias de usuário relacionadas | 6 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 005-Casos-de-Uso-Geoinformacao-Municipal.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_geoinformacao`. Alterações no código devem ser
> refletidas reexecutando o gerador.
