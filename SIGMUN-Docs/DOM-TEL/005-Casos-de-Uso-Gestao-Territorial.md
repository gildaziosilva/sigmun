# 005 – Casos de Uso – Gestão Territorial

#### Casos de Uso – Gestão Territorial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TEL-005

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

Este artefato especifica os casos de uso do domínio de Gestão Territorial,
relacionando cada cenário à sua implementação na camada de casos de uso.

---

# 2. Convenções

* Casos de uso descrevem **cenários de negócio**; a implementação é referenciada
  pelo nome da classe de caso de uso correspondente.
* Cenários de consulta direta ao repositório são assim identificados, pois não
  exigem lógica de negócio própria.

---

# 3. Casos de Uso

### CU-TEL-001 — Cadastrar divisão territorial

**Ator:** AT-TEL-001

**Capacidade:** CAP-TEL-001

**Pré-condições:** O servidor está autenticado e possui permissão de cadastro territorial.

**Fluxo principal:**

1. Informar código, nome, tipo, população estimada e área
2. verificar a unicidade do código (RN-TEL-001)
3. gravar e registrar autoria e data.

**Pós-condições:** A divisão territorial está cadastrada e ativa.

**Regras aplicadas:** RN-TEL-001

**Caso de uso implementador:** `CadastrarBairroUseCase`
### CU-TEL-002 — Alterar situação de divisão territorial

**Ator:** AT-TEL-001

**Capacidade:** CAP-TEL-001

**Pré-condições:** A divisão territorial existe.

**Fluxo principal:**

1. Informar a nova situação (ativo ou inativo)
2. aplicar a alteração e registrar a data da modificação.

**Pós-condições:** A divisão territorial está na situação informada.

**Regras aplicadas:** RN-TEL-001

**Caso de uso implementador:** `AtualizarBairroUseCase`
### CU-TEL-003 — Excluir divisão territorial

**Ator:** AT-TEL-001

**Capacidade:** CAP-TEL-001

**Pré-condições:** A divisão territorial existe.

**Fluxo principal:**

1. Solicitar a exclusão
2. verificar logradouros ativos vinculados (RN-TEL-006)
3. havendo dependências, recusar com HTTP 409
4. caso contrário, excluir logicamente.

**Pós-condições:** A divisão está excluída logicamente e preserva o histórico.

**Regras aplicadas:** RN-TEL-006

**Caso de uso implementador:** `ExcluirBairroUseCase`
### CU-TEL-004 — Cadastrar logradouro

**Ator:** AT-TEL-001

**Capacidade:** CAP-TEL-002

**Pré-condições:** A divisão territorial de vinculação existe.

**Fluxo principal:**

1. Selecionar a divisão e informar código, nome, tipo, CEP e numeração
2. verificar a unicidade do código (RN-TEL-002)
3. gravar o logradouro vinculado.

**Pós-condições:** O logradouro está cadastrado e vinculado à divisão territorial.

**Regras aplicadas:** RN-TEL-002

**Caso de uso implementador:** `CadastrarLogradouroUseCase`
### CU-TEL-005 — Elaborar planta genérica de valores

**Ator:** AT-TEL-002

**Capacidade:** CAP-TEL-003

**Pré-condições:** A divisão territorial de referência existe.

**Fluxo principal:**

1. Informar ano, divisão, ocupação, valores unitários, alíquota e legislação
2. gravar em rascunho
3. se solicitado, verificar a unicidade de planta vigente (RN-TEL-003) e ativar.

**Pós-condições:** A planta está cadastrada em rascunho ou vigente.

**Regras aplicadas:** RN-TEL-003, RN-TEL-004

**Caso de uso implementador:** `CadastrarPlantaValoresUseCase`
### CU-TEL-006 — Ativar planta genérica de valores

**Ator:** AT-TEL-002

**Capacidade:** CAP-TEL-003

**Pré-condições:** A planta existe e está em rascunho.

**Fluxo principal:**

1. Solicitar a ativação
2. verificar se já existe planta vigente para a mesma combinação (RN-TEL-003)
3. não havendo conflito, passar a vigente (RN-TEL-004).

**Pós-condições:** A planta está vigente e é a referência do exercício.

**Regras aplicadas:** RN-TEL-003, RN-TEL-004

**Caso de uso implementador:** `AtivarPlantaValoresUseCase`
### CU-TEL-007 — Revogar planta genérica de valores

**Ator:** AT-TEL-002

**Capacidade:** CAP-TEL-003

**Pré-condições:** A planta existe e está vigente.

**Fluxo principal:**

1. Informar a justificativa
2. o sistema exige a justificativa e altera a situação para revogada (RN-TEL-004).

**Pós-condições:** A planta está revogada e preserva o histórico.

**Regras aplicadas:** RN-TEL-004

**Caso de uso implementador:** `RevogarPlantaValoresUseCase`
### CU-TEL-008 — Consultar planta de valores vigente

**Ator:** AT-TEL-003

**Capacidade:** CAP-TEL-004

**Pré-condições:** Não há precondição.

**Fluxo principal:**

1. Informar ano, divisão e ocupação
2. retornar a planta vigente ou informar a ausência (RN-TEL-003).

**Pós-condições:** Os valores vigentes foram obtidos ou a ausência foi informada.

**Regras aplicadas:** RN-TEL-003

**Caso de uso implementador:** — (consulta ao repositório) (implementado como consulta ao repositório)
### CU-TEL-009 — Registrar georreferência

**Ator:** AT-TEL-004

**Capacidade:** CAP-TEL-005

**Pré-condições:** A divisão ou o logradouro de referência existe.

**Fluxo principal:**

1. Selecionar a referência territorial (divisão ou logradouro, nunca ambas)
2. informar geometria, vértices, datum e precisão
3. validar e gravar (RN-TEL-005).

**Pós-condições:** A georreferência está registrada e associada à referência.

**Regras aplicadas:** RN-TEL-005

**Caso de uso implementador:** `RegistrarGeorreferenciaUseCase`

# 4. Cobertura

| Indicador | Quantidade |
| --- | |
| Casos de uso especificados | 9 |
| Casos de uso com classe implementadora | 8 |
| Histórias de usuário relacionadas | 5 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 005-Casos-de-Uso-Gestao-Territorial.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_territorial`. Alterações no código devem ser
> refletidas reexecutando o gerador.
