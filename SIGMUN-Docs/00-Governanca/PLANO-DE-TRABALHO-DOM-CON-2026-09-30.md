# PLANO DE TRABALHO — DOM-CON (CONTABILIDADE PÚBLICA) — 2026-09-30

**Classificação da Informação:** Pública
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
**Data:** 2026-09-30
**Domínio:** DOM-CON — Contabilidade Pública
**Módulo:** `src/modules/sigmun_con` (schema `con`)
**Origem:** [`AUDITORIA-DOM-CON-2026-09-30.md`](AUDITORIA-DOM-CON-2026-09-30.md)
**Tipo:** Plano de implementação por ondas
**Estimativa total:** 15 sprints (2 semanas cada)

---

## 1. Objetivo

Tornar o DOM-CON funcional, íntegro, exposto, testado e documentado, resolvendo os 20 achados da auditoria em ondas ordenadas por dependência e risco.

---

## 2. Princípios de ordenação

A ordem das ondas **não é por severidade isolada**, e sim por dependência técnica e risco contábil:

1. **Correção antes da exposição.** Nenhuma rota é publicada antes de sanar a perda de dados (A-01), a corrida de numeração (A-02) e a ausência de integridade (A-03).
2. **Persistência antes de integração.** Índices e restrições precisam existir antes de o DOM-ORC conversar com o DOM-CON.
3. **Exposição antes de funcionalidade.** Sem rota, nenhum teste de integração e nenhuma validação de usuário são possíveis.
4. **Documentação ao final.** Documentar antes de estabilizar o código gera retrabalho.

---

## 3. Visão geral das ondas

| Onda | Objetivo | Achados | Saída |
| --- | --- | --- | --- |
| **0** | Decisão de fronteira | C-04, B-01 | ADR + catálogo corrigido |
| **1** | Integridade de persistência | A-01, A-02, A-03, A-04 | Migration + ORM alinhados |
| **2** | Exposição na API | C-01, A-06, B-05 | 7 rotas publicadas |
| **3** | Integração com DOM-ORC | C-02, M-03 | Ciclo da despesa completo |
| **4** | Eventos e valores | M-01, M-04, B-04 | Camadas de domínio |
| **5** | Testes | A-07 | Cobertura do ciclo e round-trip |
| **6** | Qualidade estática | A-05, B-03 | mypy limpo |
| **7** | Documentação | C-03, B-02 | 27 documentos reais |
| **8** | Funcionalidade residual | M-02 | Partidas normalizadas |
| **9** | Fechamento | — | Auditoria de revalidação |

---

## 4. Detalhamento das ondas

### Onda 0 — Decisão de fronteira de domínio

**Objetivo:** eliminar a colisão entre `sigmun_con`, `sigmun_contabilidade` e `sigmun_controladoria`.

| # | Tarefa | Entregável |
| --- | --- | --- |
| 0.1 | Decidir se `sigmun_con` absorve contabilidade pública **e** analítica, ou os módulos se separam | ADR em `00-Governanca/000F` |
| 0.2 | Corrigir `05-Modulos/index.md` para listar `sigmun_con` | Catálogo atualizado |
| 0.3 | Associar DOM-CON ao módulo na matriz `031-Matriz-de-Correspondencia-DOM-MOD.md` | Correspondência registrada |
| 0.4 | Remover ou arquivar os esqueletos `sigmun_contabilidade` e `sigmun_controladoria` | Módulos extintos ou documentados |
| 0.5 | Atualizar `DOM-CON/index.md`, que hoje declara "nenhuma correspondência registrada" | Índice coerente |

**Critério de pronto:** existe ADR, o catálogo aponta um único módulo para o domínio e nenhum esqueleto vazio permanece disputando a fronteira.

**Estimativa:** 1 sprint.

---

### Onda 1 — Integridade de persistência

**Objetivo:** eliminar a perda silenciosa de dados contábeis e garantir as invariantes no banco. **Esta onda bloqueia a Onda 2.**

| # | Tarefa | Detalhe | Achado |
| --- | --- | --- | --- |
| 1.1 | Migration `add_con_data_operacional` | Criar as 10 colunas ausentes listadas em A-01 | A-01 |
| 1.2 | Alinhar modelos ORM | Adicionar as 10 colunas com `Mapped[]` tipado | A-01 |
| 1.3 | Corrigir mapeamento dos repositórios | Gravar e ler os 10 campos; preencher `created_by` na inserção | A-01, M-04 |
| 1.4 | `UNIQUE (exercicio, numero)` | Constraint em `con.empenhos` + tratamento de violação como conflito | A-02 |
| 1.5 | FK `empenhos.dotacao_id → orc.dotacoes.id` | Avaliar FK entre schemas; se inviável, justificar em ADR | A-03 |
| 1.6 | FK `empenhos.reserva_id → orc.reservas.id` | Idem 1.5 | A-03 |
| 1.7 | FK `conciliacoes.conta_id → con.contas_contabeis.id` | Constraint interna, sem risco de schema cruzado | A-03 |
| 1.8 | FK `contas_contabeis.conta_pai_id` (auto-referência) | Hierarquia do PCASP | A-03 |
| 1.9 | Índices | `empenhos(dotacao_id)`, `empenhos(status)`, `empenhos(exercicio)`, `pagamentos(liquidacao_id)`, `conciliacoes(conta_id, ano, mes)`, `lancamentos(origem, origem_id)` | A-04 |
| 1.10 | Teste de round-trip | Gravar e reler cada entidade, verificando os 10 campos | A-01 |

**Critério de pronto:** comparação campo a campo entre entidade e modelo reporta zero perdas; round-trip preserva datas e identificadores; `UNIQUE` recusa duplicidade no banco.

**Riscos:** a FK entre schemas (1.5, 1.6) pode esbarrar em isolamento de dados; se assim for, registrar decisão e manter validação em aplicação.

**Estimativa:** 2 sprints.
---

### Onda 2 — Exposição na API

**Objetivo:** tornar o DOM-CON alcançável. **Não iniciar sem a Onda 1 concluída.**

| # | Tarefa | Detalhe | Achado |
| --- | --- | --- | --- |
| 2.1 | Importar routers | `from src.modules.sigmun_con.presentation.api import routers` | C-01 |
| 2.2 | Registrar routers | `app.include_router` para os dois routers do domínio | C-01 |
| 2.3 | Declarar tag no OpenAPI | `Contabilidade Pública` na lista `openapi_tags` | C-01 |
| 2.4 | Mapear exceções por tipo | Não encontrado → **404**; regra/duplicidade → **409**; saldo → **422** | A-06 |
| 2.5 | Adotar as 8 exceções órfãs | Substituir `RegraNegocioError` genérico pelas exceções específicas | A-06 |
| 2.6 | Paginação e filtro | `limit`/`offset` e ordenação nos endpoints de coleção | B-05 |
| 2.7 | Teste de exposição | Estender `test_openapi.py` com as 7 rotas e a tag | C-01, A-07 |

**Critério de pronto:** `app.openapi()` lista as 7 rotas sob `/api/v1/con`; a tag consta na documentação; erros de recurso ausente respondem 404.

**Estimativa:** 1 sprint.

---

### Onda 3 — Integração com DOM-ORC

**Objetivo:** fechar a cadeia `DOM-ORC → DOM-CON` e garantir o reflexo contábil.

| # | Tarefa | Detalhe | Achado |
| --- | --- | --- | --- |
| 3.1 | Registrar routers de DOM-ORC | Sem dotação não há empenho | C-02 |
| 3.2 | Teste E2E do ciclo completo | Dotação → empenho → liquidação → pagamento, verificando saldo da dotação | C-02 |
| 3.3 | Teste de falha transacional | Falha na gravação do empenho deve reverter o débito da dotação | C-02 |
| 3.4 | Lançamento automático | Gerar lançamento a partir de liquidação e pagamento, preenchendo `origem` e `origem_id` | M-03 |
| 3.5 | Mapear contas do PCASP | Tabela de equivalência despesa → conta contábil | M-03 |
| 3.6 | Idempotência | Reenvio não pode duplicar lançamento nem pagamento | M-03 |

**Critério de pronto:** o ciclo completo roda ponta a ponta com saldo de dotação consistente e lançamento contábil automático balanceado.

**Estimativa:** 2 sprints.

---

### Onda 4 — Eventos de domínio e objetos de valor

**Objetivo:** alinhar o módulo ao padrão dos outros 30 módulos e habilitar integração assíncrona.

| # | Tarefa | Detalhe | Achado |
| --- | --- | --- | --- |
| 4.1 | `domain/events/` | `EmpenhoEmitido`, `EmpenhoLiquidado`, `EmpenhoPago`, `EmpenhoAnulado`, `EmpenhoCancelado`, `LancamentoRegistrado`, `ConciliacaoDivergente` | M-01 |
| 4.2 | `domain/value_objects/` | `Exercicio`, `ValorMonetario`, `Competencia` | M-01 |
| 4.3 | `domain/services/` | `ServicoPartidasDobradas` (RN-CON-040), `ServicoSaldosEmpenho` | M-01 |
| 4.4 | Completar trilha de auditoria | `updated_at`/`updated_by` em `lancamentos` e `conciliacoes` | M-04 |
| 4.5 | Publicar eventos | Emissão via barramento do SIGMUN, com destino à auditoria | M-01, B-04 |

**Critério de pronto:** estrutura idêntica à dos demais módulos; eventos consumíveis; trilha de auditoria completa em todas as tabelas.

**Estimativa:** 2 sprints.

---

### Onda 5 — Testes

**Objetivo:** cobrir o ciclo da despesa e a persistência.

| # | Tarefa | Cobertura | Achado |
| --- | --- | --- | --- |
| 5.1 | Máquina de estados do empenho | `liquidar`, `estornar_liquidacao`, `pagar`, `anular`, `cancelar` | A-07 |
| 5.2 | Transições inválidas | Empenho pago não pode ser cancelado; estorno que comprometeria valor pago | A-07 |
| 5.3 | Invariantes de saldo | Saldo a liquidar e a pagar em sequências parciais | A-07 |
| 5.4 | PCASP | Lançamento em conta sintética, inativa ou não analítica é recusado | A-07 |
| 5.5 | Conciliação com divergência | Justificativa obrigatória; diferença zerada → conciliada | A-07 |
| 5.6 | Round-trip de repositórios | Os 10 campos da Onda 1 sobrevivem à gravação | A-07 |
| 5.7 | Testes de integração da API | 7 endpoints, incluindo 404 e 409 | A-07 |
| 5.8 | Meta mínima | Cobertura de linhas ≥ 80 % no módulo | A-07 |

**Critério de pronto:** meta de cobertura atingida e ciclo completo coberto por testes automatizados.

**Estimativa:** 1 sprint.

---

### Onda 6 — Qualidade estática

| # | Tarefa | Detalhe | Achado |
| --- | --- | --- | --- |
| 6.1 | Tipar modelos com `Mapped[]` | Eliminar a maior parte dos 131 erros | A-05 |
| 6.2 | Tipar repositórios | Eliminar os 83 erros de `arg-type` | A-05 |
| 6.3 | Anotar retorno dos endpoints | 7 funções sem anotação | A-05 |
| 6.4 | Tipar casos de uso | 7 erros restantes | A-05 |
| 6.5 | Migrar `utcnow()` | `datetime.now(UTC)` — depreciação do Python 3.12 | B-03 |
| 6.6 | Congelar em CI | `mypy src/modules/sigmun_con/` sem erros | A-05 |

**Critério de pronto:** `mypy` reporta zero erros no módulo; `ruff` continua limpo.
---

### Onda 7 — Documentação

**Objetivo:** substituir os 26 templates por artefatos reais, com rastreabilidade ao código.

| # | Tarefa | Documentos | Achado |
| --- | --- | --- | --- |
| 7.1 | Extrair do código | `007-Regras-de-Negocio` (as RN-CON já existem em docstrings), `013-Modelo-de-Dados`, `025-Estrutura-Tecnica`, `026-Modelo-de-Dominio` | C-03 |
| 7.2 | Mapear execução | `001-Atores`, `002-Capacidades`, `003-Processos`, `004-Servicos`, `005-Casos-de-Uso` | C-03 |
| 7.3 | Especificar requisitos | `006-Historias`, `008-Requisitos-Funcionais`, `009-Nao-Funcionais`, `010-Especificacoes`, `011-Criterios-de-Aceitacao` | C-03 |
| 7.4 | Fechar rastreabilidade | `012-Matriz-de-Rastreabilidade` vinculando RN ↔ código ↔ teste | C-03 |
| 7.5 | Arquitetura | `014-Modelo-de-Integracao`, `015-Arquitetura-de-Servicos`, `016-Seguranca`, `017-Auditoria` | C-03 |
| 7.6 | Operação | `018` a `024` (testes, implantação, checklist, migração, treinamento, suporte) | C-03 |
| 7.7 | `README.md` em `puml/` | Seguir o padrão de `00-Governanca/puml/README.md` | B-02 |
| 7.8 | Validar conformidade | Referenciar LC 4.320/64, MCASP e instrução normativa do TCE | C-03 |

**Critério de pronto:** os 27 documentos têm conteúdo específico do domínio, sem boilerplate; a matriz de rastreabilidade liga cada regra ao seu teste.

**Estimativa:** 2 sprints.

---

### Onda 8 — Funcionalidade residual

| # | Tarefa | Detalhe | Achado |
| --- | --- | --- | --- |
| 8.1 | Normalizar partidas dobradas | Tabela `con.lancamento_partidas` com FK para `contas_contabeis`, CHECK de sinal e trigger de balanço | M-02 |
| 8.2 | CHECK de saldo | Impedir `valor_pago > valor_liquidado` no banco | A-02 |
| 8.3 | CHECK de competência | `competencia_mes` entre 1 e 12 | M-04 |
| 8.4 | Relatórios | Execução orçamentária, saldo por dotação e por conta | C-03 |
| 8.5 | Fechamento de exercício | Bloqueio de lançamentos em exercício encerrado | M-03 |

**Critério de pronto:** invariantes garantidas pelo banco; relatórios de execução e fechamento disponíveis.

**Estimativa:** 2 sprints.

---

### Onda 9 — Revalidação

| # | Tarefa |
| --- | --- |
| 9.1 | Reexecutar a auditoria com o mesmo método |
| 9.2 | Confirmar zero achados críticos e altos abertos |
| 9.3 | Atualizar `DOM-CON/index.md` com o status real |
| 9.4 | Atualizar `ROADMAP.md` e a matriz `031` |
| 9.5 | Publicar o resultado em `00-Governanca/` |

---

## 5. Sequenciamento e dependências

```text
Onda 0 (fronteira)
   │
   ▼
Onda 1 (persistência) ── bloqueia ──▶ Onda 2 (exposição)
   │                                        │
   │                                        ▼
   └──▶ Onda 4 (eventos) ──────────────▶ Onda 3 (integração DOM-ORC)
                                                │
                                                ▼
                                           Onda 5 (testes)
                                                │
                                                ▼
                                           Onda 6 (qualidade)
                                                │
                                                ▼
                                           Onda 7 (documentação)
                                                │
                                                ▼
                                           Onda 8 (residual)
                                                │
                                                ▼
                                           Onda 9 (revalidação)
```

**Caminho crítico:** Onda 0 → 1 → 2 → 3 → 5. As ondas 4 e 6 avançam em paralelo a partir da 1; a 7 depende de todas.

---

## 6. Definição de pronto do domínio

O DOM-CON será considerado pronto quando, simultaneamente:

- [ ] As 7 rotas `/api/v1/con` respondem e constam do OpenAPI.
- [ ] Nenhum campo do domínio é perdido na persistência (round-trip comprovado).
- [ ] `UNIQUE (exercicio, numero)` impede empenho duplicado.
- [ ] Integridade referencial garantida para dotação, reserva e conta.
- [ ] Índices criados nos caminhos de consulta principais.
- [ ] Ciclo `dotação → empenho → liquidação → pagamento` validado ponta a ponta.
- [ ] Lançamento contábil gerado automaticamente e balanceado.
- [ ] Cobertura de linhas ≥ 80 % e `mypy` sem erros.
- [ ] Os 27 documentos têm conteúdo real e rastreabilidade ao código.
- [ ] Fronteira de domínio decidida e catálogo de módulos coerente.

---

## 7. Riscos

| Risco | Probabilidade | Impacto | Mitigação |
| --- | --- | --- | --- |
| FK entre schemas inviável por isolamento de dados | Média | Médio | Validar na Onda 1.5; se inviável, registrar ADR e manter validação em aplicação com teste periódico de integridade |
| Migration corretiva em base com dados | Alta | Alto | Backfill explícito e `downgrade` testado; executar em homologação antes de produção |
| Escopo da documentação (27 docs) consumir o roadmap | Alta | Médio | Priorizar 7.1 e 7.4; o restante segue incrementalmente sem bloquear a operação |
| Colisão `contabilidade`/`controladoria` gerar retrabalho | Média | Alto | Resolver na Onda 0, antes de qualquer código novo |
| Tabelas sem índice degradarem em produção | Média | Alto | Executar `EXPLAIN ANALYZE` após a Onda 1.9 com dados representativos |

---

## 8. Esforço estimado

| Onda | Sprints | Dias-pessoa (equipe de 2) |
| --- | --- | --- |
| 0 — Fronteira | 1 | 10 |
| 1 — Persistência | 2 | 20 |
| 2 — Exposição | 1 | 10 |
| 3 — Integração DOM-ORC | 2 | 20 |
| 4 — Eventos e valores | 2 | 20 |
| 5 — Testes | 1 | 10 |
| 6 — Qualidade estática | 1 | 10 |
| 7 — Documentação | 2 | 20 |
| 8 — Funcionalidade residual | 2 | 20 |
| 9 — Revalidação | 1 | 10 |
| **Total** | **15** | **150** |

Estimativa em dias-pessoa, calibrada no tamanho dos domínios já implementados no SIGMUN. As ondas 4 e 6 são paralelizáveis entre si, o que reduz o caminho crítico para **8 sprints**.

---

**Critério de pronto:** auditoria de revalidação publicada, com os achados encerrados.

**Estimativa:** 1 sprint.

**Documento:** PLANO-DE-TRABALHO-DOM-CON-2026-09-30.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
