# AUDITORIA — DOM-CON (CONTABILIDADE PÚBLICA) — 2026-09-30

**Classificação da Informação:** Pública
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
**Data:** 2026-09-30
**Domínio:** DOM-CON — Contabilidade Pública
**Módulo:** `src/modules/sigmun_con` (schema `con`)
**Tipo:** Auditoria técnica de código, persistência, qualidade estática, testes e documentação
**Status da auditoria:** Concluída — achados registrados, correções não aplicadas

---

## 1. Objetivo

Auditar o domínio DOM-CON em todas as camadas verificáveis (domínio, aplicação, infraestrutura, apresentação, persistência, testes, qualidade estática, exposição na API e documentação), identificar o que está faltando para tornar o domínio utilizável e produzir plano de trabalho.

A auditoria **não alterou** código, escopo funcional, contratos ou persistência. Este documento registra achados e o plano correspondente.

---

## 2. Escopo e método

| Item | Verificação | Resultado |
| --- | --- | --- |
| Exposição na API | `app.openapi()` filtrado por `/api/v1/con` | **Falha — 0 rotas** |
| Registro de routers | `grep sigmun_con src/main.py` | **Ausente** |
| Suíte unitária do domínio | `pytest tests/unit/test_con_*.py` | 6 testes, todos passam |
| Suíte de integração do domínio | `pytest tests/integration` (rota `con`) | **Inexistente** |
| Lint | `ruff check src/modules/sigmun_con/` | Aprovado |
| Tipagem | `mypy src/modules/sigmun_con/` | **131 erros em 12 arquivos** |
| Domínio × ORM | Comparação campo a campo por AST | **10 campos sem coluna** |
| Integridade referencial | `alembic/versions/20260919_05` e `_06` | FKs incompletas |
| Índices | `create_index` nas migrations DOM-CON | **Nenhum índice** |
| Exceções | Uso das exceções declaradas | 8 sem uso |
| Documentação | Bytes e status de `DOM-CON/*.md` | 26 de 27 vazios |

**Comandos de reprodução:**

```bash
# Ausência de rotas (resultado esperado: [], 315 rotas no total)
PYTHONPATH=. python -c "from src.main import app; \
  print([p for p in app.openapi()['paths'] if p.startswith('/api/v1/con')])"

# Tipagem (resultado esperado: Found 131 errors in 12 files)
mypy src/modules/sigmun_con/

# Testes do domínio (resultado esperado: 6 passed)
pytest tests/unit/test_con_contabil.py tests/unit/test_con_use_cases.py
```

---

## 3. Diagnóstico geral

O DOM-CON está em **estado de implementação parcial não exposta**. O código de domínio é coerente e de boa qualidade relativa (lint limpo, regras de negócio implementadas com máquina de estados explícita), mas o módulo **não é alcançável por qualquer consumidor**: não há rota registrada, não há teste de integração e a documentação de domínio é um conjunto de 26 templates idênticos.

A cadeia `DOM-ORC → DOM-CON → Contabilidade Analítica` está interrompida em dois pontos: nenhum dos dois domínios registra routers na aplicação.

| Camada | Estado | Avaliação |
| --- | --- | --- |
| Domínio (entidades e regras) | Implementado | Bom — RNs explícitas, transições declaradas |
| Aplicação (casos de uso) | Implementado | 7 casos de uso |
| Infraestrutura (repositórios) | Implementado com perdas | 10 campos descartados |
| Apresentação (API) | **Não registrada** | Inacessível |
| Persistência | Parcial | Sem FKs externas, sem índices |
| Testes | Mínimo | 6 unitários, 0 de integração |
| Documentação | **Inexistente** | 26 templates de ~2,1 KB |
| Qualidade estática | Parcial | 131 erros de tipagem |

---
## 4. Achados

Classificação de severidade: **C** crítico (bloqueia o domínio) · **A** alto (correção estrutural) · **M** médio · **B** baixo.

### 4.1 Críticos

#### C-01 — Módulo inacessível: routers não registrados na aplicação

**Evidência**

```text
$ grep -n "sigmun_con" src/main.py
(nenhuma ocorrência)

$ PYTHONPATH=. python -c "... '/api/v1/con' ..."
[]
total de rotas registradas: 315
tag Contabilidade presente? False
```

`src/main.py` registra 26 routers (linhas 315–351). DOM-CON não consta em nenhum deles, apesar de `presentation/api/contabil_endpoints.py` e `execucao_endpoints.py` definirem 7 endpoints sob o prefixo `/api/v1/con` com a tag `Contabilidade Pública`.

**Impacto:** 100 % do módulo é código morto. Nenhum consumidor — pessoa usuária, integração ou teste — consegue alcançar empenho, liquidação, pagamento, conta, lançamento ou conciliação. O `tag` declarado nos routers também não aparece no OpenAPI, o que quebra a descoberta da capacidade na documentação da API.

#### C-02 — Domínio dependente DOM-ORC também não registrado

**Evidência:** `grep -n "sigmun_orc" src/main.py` → nenhuma ocorrência.

**Impacto:** o `EmitirEmpenhoUseCase` recebe a dotação como parâmetro injetado pelo endpoint, que a busca via `get_dotacao_repo_con`. Sem as rotas de DOM-ORC, não existe dotação a empenhar — a integração `DOM-ORC → DOM-CON` é inexistente na aplicação, ainda que o código exista.

#### C-03 — Documentação de domínio é um conjunto de templates

**Evidência**

| Documento | Bytes | Status declarado |
| --- | --- | --- |
| `000-Dominio-Contabilidade-Publica.md` | 5.866 | Vigente |
| `001` a `026` (26 documentos) | 2.104 – 2.236 | Em elaboração |

Os 26 documentos possuem tamanho praticamente idêntico e texto de boilerplate: *"Este artefato é um esboço inicial padronizado […] tem como finalidade mapear e definir […] do domínio"*. Apenas o `000` contém conteúdo real do domínio.

**Impacto:** inexistem atores, capacidades, processos, casos de uso, histórias de usuário, regras de negócio, requisitos, critérios de aceitação, matriz de rastreabilidade, modelo de dados, modelo de integração, arquitetura de serviços, segurança, auditoria, plano de testes e plano de implantação **declarados**. As regras existem apenas em docstrings de código — não há fonte documental para auditoria externa, conformidade legal (LC 4.320/64, MCASP, instrução normativa do TCE) ou treinamento.

Observação: o `index.md` do domínio registra *"Nenhuma correspondência confirmada ou candidata registrada para este domínio na matriz 031"*, ou seja, o próprio domínio admite não estar ligado ao seu módulo.

#### C-04 — Colisão de fronteira de domínio não resolvida

**Evidência**

```text
sigmun_contabilidade/  → 12 diretórios, apenas __init__.py (esqueleto vazio)
sigmun_controladoria/  → 12 diretórios, apenas __init__.py (esqueleto vazio)
```

Ambos estão no catálogo `05-Modulos/index.md` com estado "Preparado". `sigmun_con` **não consta** no catálogo.

**Impacto:** três nomes (`contabilidade`, `controladoria`, `con`) disputam a mesma fronteira. Sem decisão registrada, existe risco real de implementação duplicada e de dispersão da regra contábil. A matriz de correspondência DOM ↔ módulo não associa o domínio ao módulo que de fato o implementa.

### 4.2 Altos

#### A-01 — Dez campos do domínio são descartados silenciosamente na persistência

Comparação campo a campo entre entidades de domínio e modelos SQLAlchemy (por AST):

| Entidade | Modelo | Campos sem coluna |
| --- | --- | --- |
| `Empenho` | `EmpenhoModel` | `favorecido_id`, `data_anulacao` |
| `Liquidacao` | `LiquidacaoModel` | `descricao`, `data_liquidacao`, `data_cancelamento` |
| `Pagamento` | `PagamentoModel` | `descricao`, `data_programacao`, `data_efetivacao` |
| `ContaContabil` | `ContaContabilModel` | `grupo` |
| `LancamentoContabil` | `LancamentoModel` | `data_lancamento` |
| `ConciliacaoContabil` | `ConciliacaoModel` | — |

**Impacto — severidade contábil e legal:**

- `data_lancamento` é **obrigatória** em lançamento contábil (MCASP). Sem ela, o lançamento fica sem data de competência e não é auditável.
- As cinco datas de ciclo de vida (`data_emissao` existe, mas `data_anulacao`, `data_liquidacao`, `data_cancelamento`, `data_programacao`, `data_efetivacao` não) impedem a reconstrução da linha do tempo do processo da despesa.
- `favorecido_id` rompe o vínculo do empenho com o fornecedor, preservando apenas o nome livre — que pode divergir do cadastro oficial.
- `grupo` do PCASP é parte da hierarquia contábil oficial.

A perda é silenciosa: o repositório grava a entidade, descarta o campo e, na releitura, o valor retorna como vazio. Nenhum erro, nenhum log.

#### A-02 — RN-CON-001 não garantida pelo banco

`get_by_numero_exercicio` faz a verificação de unicidade em Python, mas **não existe** `UNIQUE (exercicio, numero)` em `con.empenhos`.

**Impacto:** condição de corrida. Duas requisições simultâneas com o mesmo número e exercício passam ambas pela verificação e criam empenhos duplicados. A numeração de empenho é requisito de ordenação legal da despesa.

#### A-03 — Ausência de chaves estrangeiras

```text
con.empenhos.dotacao_id  → TEXT, sem FK  (deveria referenciar orc.dotacoes.id)
con.empenhos.reserva_id  → TEXT, sem FK  (deveria referenciar orc.reservas.id)
con.conciliacoes.conta_id → TEXT, sem FK (deveria referenciar con.contas_contabeis.id)
con.contas_contabeis.conta_pai_id → TEXT, sem FK (auto-referência)
```

A dependência `DOM-ORC → DOM-CON` é real e já registrada em `divergencias.txt` como pendência. Sem FK, o banco não impede empenho órfão: um `dotacao_id` inexistente é aceito.

#### A-04 — Nenhum índice no schema `con`

As migrations `20260919_05_dom_con_models` e `20260919_06_dom_con_contabil` não criam **nenhum** índice.

**Impacto:** consultas degradam para varredura sequencial à medida que a base cresce. Os caminhos mais prováveis — empenhos por dotação, por status, por exercício; lançamentos por origem; conciliações por conta e competência — atingem todas as tabelas.

#### A-05 — 131 erros de tipagem

```text
Found 131 errors in 12 files (checked 21 source files)
```

Concentração: repositórios (83 erros), endpoints sem anotação de retorno (7), modelos (9), casos de uso (7).

O padrão dominante — `Argument "classe" to "ContaContabil" has incompatible type "Column[str] | str"` — indica anotação frouxa nos modelos (`Column` sem `Mapped[]`), fazendo o ORM parecer não tipado. `ruff` passa, o que confirma que a lacuna é de tipagem, não de estilo.

#### A-06 — Oito exceções de domínio declaradas e nunca utilizadas

| Exceção | Usos |
| --- | --- |
| `EmpenhoJaExistenteError` | 0 |
| `EmpenhoEmEstadoInvalidoError` | 0 |
| `PagamentoNaoEncontradoError` | 0 |
| `ContaContabilNaoEncontradaError` | 0 |
| `ContaContabilJaExistenteError` | 0 |
| `LancamentoNaoEncontradoError` | 0 |
| `ConciliacaoNaoEncontradaError` | 0 |
| `TransicaoInvalidaError` | 0 |

**Impacto:** o contrato de erro da API está incorreto. Os endpoints capturam `DomConDomainError` e devolvem **409** para tudo, inclusive para recurso não encontrado, que deveria ser **404**. Um cliente não consegue distinguir "conta inexistente" de "conta duplicada" — o que impede tratamento correto de erro.

#### A-07 — Cobertura de testes insuficiente

6 testes unitários no total (3 em `test_con_contabil.py`, 3 em `test_con_use_cases.py`). Não há nenhum teste de integração para `/api/v1/con`, porque a rota não existe.

Cobertura ausente de maior risco: máquina de estados do empenho (`liquidar`, `estornar_liquidacao`, `pagar`, `anular`, `cancelar`), estorno de pagamento, round-trip dos repositórios e conciliação com divergência.

---

### 4.3 Médios

#### M-01 — Camadas ausentes no módulo de domínio

`sigmun_con` não possui `domain/events`, `domain/value_objects` nem `domain/services`. É um dos **dois únicos** módulos do sistema nessa situação — o outro é `sigmun_orc`. Os demais 30 módulos têm as três camadas.

Consequência: não há eventos de domínio, o que impede a integração assíncrona e a projeção de auditoria; e não há objetos de valor para `Exercicio`, `ValorMonetario` ou `Competencia`, cujo reuso hoje se limita a validações inline.

#### M-02 — Partidas dobradas sem integridade referencial

`con.lancamentos.partidas` é `TEXT` com JSON. Não há tabela filha, não há FK para `con.contas_contabeis`, e não há índice.

**Impacto:** o balanço (RN-CON-040) é validado apenas na aplicação. Um lançamento persistido diretamente no banco pode referenciar conta inexistente ou ficar desequilibrado.

#### M-03 — Sem geração automática de lançamento contábil

`LancamentoContabil` possui os campos `origem` e `origem_id`, e `LancarContabilUseCase` existe, mas **nenhum** caso de uso do ciclo do empenho o invoca. O lançamento contábil depende de POST manual em `/api/v1/con/lancamentos`.

**Impacto:** o reflexo contábil da operação orçamentária não é garantido. Um empenho liquidado pode não gerar lançamento, quebrando a conciliabilidade e o fechamento do exercício.

#### M-04 — Trilha de auditoria incompleta em lançamentos e conciliações

`lancamentos` e `conciliacoes` possuem apenas `created_at` e `created_by`; não possuem `updated_at` nem `updated_by` — ao contrário de `empenhos`, `liquidacoes` e `pagamentos`, que têm os quatro. Além disso, `created_by` existe mas **não é preenchido** por nenhum caminho de escrita (os repositórios nunca o gravam na inserção).

**Impacto:** não é possível saber quem lançou nem quem conciliou.

---

### 4.4 Baixos

| ID | Achado | Evidência |
| --- | --- | --- |
| B-01 | `sigmun_con` ausente do catálogo de módulos | `05-Modulos/index.md` lista `contabilidade` e `controladoria`, não `con` |
| B-02 | Ausência de `README.md` no diretório `puml/` | Existe em `00-Governanca/puml/README.md`, não em `DOM-CON/puml/` |
| B-03 | Uso de `datetime.utcnow()`, depreciado no Python 3.12 | Todas as entidades e modelos |
| B-04 | Nenhum evento de auditoria emitido pelos repositórios | Repositórios gravam, mas não publicam evento |
| B-05 | Sem paginação, ordenação ou filtro nos endpoints | 7 endpoints de coleção sem `limit`/`offset` |

---

## 5. Achados positivos

Registrado para devolutiva ao que já está bem resolvido:

- **Regras de negócio explícitas e verificáveis.** As RNs estão codificadas em docstrings e em estruturas de dados (`TRANSICOES_EMPENHO`, `ESTADOS_TERMINAIS_EMPENHO`), e a máquina de estados é consistente com as transições implementadas.
- **Invariantes de saldo corretamente derivadas.** `valor_liquido`, `saldo_a_liquidar` e `saldo_a_pagar` são propriedades calculadas, sem estado redundante.
- **Proteção contra saldo negativo.** `liquidar`, `pagar` e `anular` validam saldo antes de aplicar.
- **Separação de responsabilidades clara.** `dotacao.empenhar_direto` e `dotacao.anular_empenho` mantêm o saldo no DOM-ORC, respeitando a fronteira.
- **Lint limpo.** `ruff check` sem apontamentos.
- **Impedição deleteiva correta.** FKs internas com `ON DELETE RESTRICT` preservam a trilha contábil.
- **PCASP modelado com a regra certa.** `pode_receber_lancamento()` combina analiticidade, atividade e permissão — evitando lançamento em conta sintética ou inativa.

---

## 6. Conclusão

O DOM-CON **não está pronto para uso**. O critério decisivo é o achado **C-01**: existem 7 endpoints, 7 casos de uso, 6 entidades e 6 tabelas — porém **nenhuma delas é alcançável**, porque o módulo não é registrado na aplicação. Todo o restante da auditoria descreve o que precisará ser resolvido **depois** que a exposição for feita.

A ordem importa: registrar as rotas sem antes sanar **A-01** (perda silenciosa de dados contábeis) e **A-03**/**A-04** (ausência de integridade e índices) tornaria o domínio publicamente acessível com defeitos de conformidade contábil.

**Prioridade de entrada:** C-01 → A-01 → A-02 → A-03 → A-06 → A-07 → C-02 → demais.

O plano de trabalho correspondente está em
[`PLANO-DE-TRABALHO-DOM-CON-2026-09-30.md`](PLANO-DE-TRABALHO-DOM-CON-2026-09-30.md).

---

**Documento:** AUDITORIA-DOM-CON-2026-09-30.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente

