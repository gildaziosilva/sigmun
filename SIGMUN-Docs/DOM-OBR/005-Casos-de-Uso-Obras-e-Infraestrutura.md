# 005 – Casos de Uso – Obras e Infraestrutura

#### Casos de Uso – Obras e Infraestrutura

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OBR-005

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

Este artefato especifica os casos de uso do domínio de Obras e Infraestrutura,
relacionando cada cenário à sua implementação na camada de casos de uso.

---

# 2. Convenções

* Casos de uso descrevem **cenários de negócio**; a implementação é referenciada
  pelo nome da classe de caso de uso correspondente.
* Cenários de consulta direta ao repositório são assim identificados, pois não
  exigem lógica de negócio própria.

---

# 3. Casos de Uso

### CU-OBR-001 — Cadastrar obra pública

**Ator:** AT-OBR-001

**Capacidade:** CAP-OBR-001

**Pré-condições:** O servidor está autenticado e possui permissão de gestão de obras.

**Fluxo principal:**

1. Informar número, nome, tipo, contratação, fonte de recurso e valores orçado e contratado
2. verificar a unicidade do número (RN-OBR-001) e a coerência dos valores (RN-OBR-004)
3. gravar a obra em situação planejada.

**Pós-condições:** A obra está cadastrada e planejada.

**Regras aplicadas:** RN-OBR-001, RN-OBR-004

**Caso de uso implementador:** `CadastrarObraUseCase`
### CU-OBR-002 — Alterar cadastro da obra

**Ator:** AT-OBR-001

**Capacidade:** CAP-OBR-001

**Pré-condições:** A obra existe e não está concluída.

**Fluxo principal:**

1. Informar os campos a alterar
2. gravar a alteração e registrar a data (RN-OBR-002).

**Pós-condições:** A obra está atualizada.

**Regras aplicadas:** RN-OBR-002, RN-OBR-004

**Caso de uso implementador:** `AtualizarObraUseCase`
### CU-OBR-003 — Iniciar a execução da obra

**Ator:** AT-OBR-001

**Capacidade:** CAP-OBR-001

**Pré-condições:** A obra está contratada ou suspensa, com empresa e data prevista informadas.

**Fluxo principal:**

1. Solicitar o início
2. exigir empresa contratada e data de início prevista (RN-OBR-003)
3. registrar a data de início real.

**Pós-condições:** A obra está em execução.

**Regras aplicadas:** RN-OBR-002, RN-OBR-003

**Caso de uso implementador:** `IniciarExecucaoObraUseCase`
### CU-OBR-004 — Suspender a obra

**Ator:** AT-OBR-001

**Capacidade:** CAP-OBR-001

**Pré-condições:** A obra está em execução ou contratada.

**Fluxo principal:**

1. Informar a justificativa
2. alterar a situação para suspensa (RN-OBR-002).

**Pós-condições:** A obra está suspensa com a justificativa registrada.

**Regras aplicadas:** RN-OBR-002

**Caso de uso implementador:** `SuspenderObraUseCase`
### CU-OBR-005 — Concluir a obra

**Ator:** AT-OBR-001

**Capacidade:** CAP-OBR-001

**Pré-condições:** A obra está em execução ou suspensa, com 100% do avanço físico.

**Fluxo principal:**

1. Solicitar a conclusão
2. exigir 100% do avanço físico (RN-OBR-005)
3. registrar a data de conclusão real.

**Pós-condições:** A obra está concluída com data de conclusão registrada.

**Regras aplicadas:** RN-OBR-002, RN-OBR-005

**Caso de uso implementador:** `ConcluirObraUseCase`
### CU-OBR-006 — Cancelar a obra

**Ator:** AT-OBR-001

**Capacidade:** CAP-OBR-001

**Pré-condições:** A obra não está concluída nem cancelada.

**Fluxo principal:**

1. Informar a justificativa
2. alterar a situação para cancelada (RN-OBR-002).

**Pós-condições:** A obra está cancelada com a justificativa registrada.

**Regras aplicadas:** RN-OBR-002

**Caso de uso implementador:** `CancelarObraUseCase`
### CU-OBR-007 — Excluir obra

**Ator:** AT-OBR-001

**Capacidade:** CAP-OBR-001

**Pré-condições:** A obra existe e não possui medições nem despesas.

**Fluxo principal:**

1. Solicitar a exclusão
2. havendo medições ou despesas, recusar com HTTP 409 (RN-OBR-005, RN-OBR-006)
3. caso contrário, excluir logicamente.

**Pós-condições:** A obra está excluída logicamente e preserva o histórico.

**Regras aplicadas:** RN-OBR-005, RN-OBR-006

**Caso de uso implementador:** `ExcluirObraUseCase`
### CU-OBR-008 — Registrar medição da obra

**Ator:** AT-OBR-003

**Capacidade:** CAP-OBR-002

**Pré-condições:** A obra está em execução ou suspensa.

**Fluxo principal:**

1. Informar número, tipo, percentual físico, valor medido e responsável técnico
2. verificar a unicidade do número e o teto do valor contratado (RN-OBR-005)
3. gravar a medição em situação registrada.

**Pós-condições:** A medição está registrada.

**Regras aplicadas:** RN-OBR-005

**Caso de uso implementador:** `RegistrarMedicaoUseCase`
### CU-OBR-009 — Aprovar medição

**Ator:** AT-OBR-002

**Capacidade:** CAP-OBR-002

**Pré-condições:** A medição existe e está registrada.

**Fluxo principal:**

1. Conferir a medição e aprová-la (RN-OBR-005)
2. recompor o valor medido e o avanço físico da obra a partir das medições aprovadas.

**Pós-condições:** A medição está aprovada e o avanço da obra foi recomposto.

**Regras aplicadas:** RN-OBR-004, RN-OBR-005

**Caso de uso implementador:** `AprovarMedicaoUseCase`
### CU-OBR-010 — Glosar medição

**Ator:** AT-OBR-002

**Capacidade:** CAP-OBR-002

**Pré-condições:** A medição existe e está conferida.

**Fluxo principal:**

1. Informar a justificativa
2. alterar a situação para glosada (RN-OBR-005).

**Pós-condições:** A medição está glosada e não compõe o avanço.

**Regras aplicadas:** RN-OBR-005

**Caso de uso implementador:** `GlosarMedicaoUseCase`
### CU-OBR-011 — Cancelar medição

**Ator:** AT-OBR-002

**Capacidade:** CAP-OBR-002

**Pré-condições:** A medição existe e não está aprovada.

**Fluxo principal:**

1. Solicitar o cancelamento
2. alterar a situação para cancelada (RN-OBR-005).

**Pós-condições:** A medição está cancelada e não compõe o avanço.

**Regras aplicadas:** RN-OBR-005

**Caso de uso implementador:** `CancelarMedicaoUseCase`
### CU-OBR-012 — Registrar despesa da obra

**Ator:** AT-OBR-004

**Capacidade:** CAP-OBR-003

**Pré-condições:** A obra está contratada ou em execução e há saldo medido.

**Fluxo principal:**

1. Informar descrição, tipo, valor, credor e medição vinculada
2. exigir valor positivo e não superior ao saldo medido a pagar (RN-OBR-006)
3. gravar a despesa e recompor o avanço financeiro.

**Pós-condições:** A despesa está registrada e o avanço financeiro da obra foi recomposto.

**Regras aplicadas:** RN-OBR-004, RN-OBR-006

**Caso de uso implementador:** `RegistrarDespesaUseCase`
### CU-OBR-013 — Excluir despesa

**Ator:** AT-OBR-004

**Capacidade:** CAP-OBR-003

**Pré-condições:** A despesa existe.

**Fluxo principal:**

1. Solicitar a exclusão
2. excluir logicamente a despesa e recompor o avanço financeiro da obra.

**Pós-condições:** A despesa está excluída e o avanço financeiro foi recomposto.

**Regras aplicadas:** RN-OBR-006

**Caso de uso implementador:** `ExcluirDespesaUseCase`
### CU-OBR-014 — Cadastrar etapa da obra

**Ator:** AT-OBR-003

**Capacidade:** CAP-OBR-004

**Pré-condições:** A obra existe.

**Fluxo principal:**

1. Informar número, descrição, tipo, percentual previsto e responsável
2. gravar a etapa em situação pendente (RN-OBR-007).

**Pós-condições:** A etapa está cadastrada.

**Regras aplicadas:** RN-OBR-007

**Caso de uso implementador:** `CadastrarEtapaUseCase`
### CU-OBR-015 — Atualizar avanço da etapa

**Ator:** AT-OBR-003

**Capacidade:** CAP-OBR-004

**Pré-condições:** A etapa existe.

**Fluxo principal:**

1. Informar o percentual realizado e a situação
2. validar a faixa de 0 a 100 (RN-OBR-007)
3. gravar a alteração.

**Pós-condições:** O avanço da etapa está atualizado.

**Regras aplicadas:** RN-OBR-007

**Caso de uso implementador:** `AtualizarEtapaUseCase`
### CU-OBR-016 — Concluir etapa

**Ator:** AT-OBR-003

**Capacidade:** CAP-OBR-004

**Pré-condições:** A etapa existe e não está concluída nem cancelada.

**Fluxo principal:**

1. Solicitar a conclusão
2. exigir 100% do percentual previsto (RN-OBR-007)
3. registrar a data de conclusão.

**Pós-condições:** A etapa está concluída com data registrada.

**Regras aplicadas:** RN-OBR-007

**Caso de uso implementador:** `ConcluirEtapaUseCase`
### CU-OBR-017 — Registrar vistoria da obra

**Ator:** AT-OBR-002

**Capacidade:** CAP-OBR-004

**Pré-condições:** A obra existe.

**Fluxo principal:**

1. Informar tipo, parecer, percentual físico verificado e fiscal
2. validar a faixa de 0 a 100 (RN-OBR-008)
3. gravar a vistoria.

**Pós-condições:** A vistoria está registrada com o parecer do fiscal.

**Regras aplicadas:** RN-OBR-008

**Caso de uso implementador:** `RegistrarVistoriaUseCase`
### CU-OBR-018 — Consultar o andamento da obra

**Ator:** AT-OBR-005

**Capacidade:** CAP-OBR-005

**Pré-condições:** Não há precondição.

**Fluxo principal:**

1. Informar a obra ou o filtro de situação
2. retornar valores, percentuais e, quando solicitado, o acompanhamento consolidado.

**Pós-condições:** O andamento da obra foi obtido.

**Regras aplicadas:** RN-OBR-004, RN-OBR-005, RN-OBR-006

**Caso de uso implementador:** — (consulta aos repositórios) (implementado como consulta ao repositório)

# 4. Cobertura

| Indicador | Quantidade |
| --- | |
| Casos de uso especificados | 18 |
| Casos de uso com classe implementadora | 17 |
| Histórias de usuário relacionadas | 7 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 005-Casos-de-Uso-Obras-e-Infraestrutura.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_obras`. Alterações no código devem ser
> refletidas reexecutando o gerador.
