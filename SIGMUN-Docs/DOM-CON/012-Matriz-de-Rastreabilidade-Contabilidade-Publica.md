# 012 – Matriz de Rastreabilidade – Contabilidade Pública

#### Matriz de Rastreabilidade – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-012

**Domínio:** Contabilidade Pública

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Contabilidade-Publica.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000C-HIERARQUIA-DOCUMENTAL-v1.0.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `AUDITORIA-DOM-CON-2026-09-30.md`

---

# 1. Finalidade

Este artefato assegura que toda capacidade, história, requisito e regra do
domínio de Contabilidade Pública está rastreada ao código e aos testes correspondentes,
e que nenhuma peça de trabalho existe sem vínculo.

---

# 2. Princípios de Rastreabilidade

* Nenhum requisito existe sem capacidade, história e regra associadas.
* Nenhuma regra existe sem requisito que a exija.
* Nenhum serviço existe sem caso de uso que o implemente.
* Nenhuma entidade existe sem operação que a persista.
* Requisito sem teste é requisito não verificado.

---

# 3. Rastreabilidade por Capacidade

| Capacidade | Histórias | Requisitos | Regras | Casos de uso | Serviços |
| --- | --- | --- | --- | --- | --- |
| CAP-CON-001 | HU-CON-005 | RF-CON-017 a 019 | RN-CON-010, 011, 012 | CU-CON-006 | SVC-CON-005 |
| CAP-CON-002 | HU-CON-001, HU-CON-004 | RF-CON-001 a 005, 014 a 016 | RN-CON-001, 002, 003, 004 | CU-CON-001, 004, 005 | SVC-CON-001, 003 |
| CAP-CON-003 | HU-CON-002 | RF-CON-006 a 009 | RN-CON-020, 021, 022 | CU-CON-002 | SVC-CON-002 |
| CAP-CON-004 | HU-CON-003 | RF-CON-010 a 013 | RN-CON-030, 031, 032 | CU-CON-003 | SVC-CON-004 |
| CAP-CON-005 | HU-CON-006 | RF-CON-020 a 024, 031 | RN-CON-050, 051, 052 | CU-CON-007 | SVC-CON-006 |
| CAP-CON-006 | HU-CON-007 | RF-CON-025 a 027 | RN-CON-060, 061 | CU-CON-008 | SVC-CON-007 |
| CAP-CON-007 | HU-CON-008 | RF-CON-028, 029 | RN-CON-070 | — | — |
| CAP-CON-008 | HU-CON-008 | RF-CON-030 | RN-CON-070 | — | — |

---

# 4. Rastreabilidade por História

| História | Capacidade | Casos de uso | Critérios | Testes | Requisitos |
| --- | --- | --- | --- | --- | --- |
| HU-CON-001 | CAP-CON-002 | CU-CON-001 | 7 | 1 | RF-CON-001 a 005 |
| HU-CON-002 | CAP-CON-003 | CU-CON-002 | 6 | 1 | RF-CON-006 a 009 |
| HU-CON-003 | CAP-CON-004 | CU-CON-003 | 6 | 0 | RF-CON-010 a 013 |
| HU-CON-004 | CAP-CON-002 | CU-CON-004, CU-CON-005 | 7 | 0 | RF-CON-014 a 016 |
| HU-CON-005 | CAP-CON-001 | CU-CON-006 | 7 | 1 | RF-CON-017 a 019 |
| HU-CON-006 | CAP-CON-005 | CU-CON-007 | 6 | 2 | RF-CON-020 a 024 |
| HU-CON-007 | CAP-CON-006 | CU-CON-008 | 4 | 1 | RF-CON-025 a 027 |
| HU-CON-008 | CAP-CON-007, 008 | — | 3 | 0 | RF-CON-028 a 030 |

---

# 5. Rastreabilidade por Requisito Funcional

| Requisito | História | Caso de uso | Serviço | Regra | Teste |
| --- | --- | --- | --- | --- | --- |
| RF-CON-001 | HU-CON-001 | CU-CON-001 | SVC-CON-001 | RN-CON-001 | — |
| RF-CON-002 | HU-CON-001 | CU-CON-001 | SVC-CON-001 | RN-CON-001 | — |
| RF-CON-003 | HU-CON-001 | CU-CON-001 | SVC-CON-001 | RN-CON-002 | — |
| RF-CON-004 | HU-CON-001 | CU-CON-001 | SVC-CON-001 | RN-CON-002 | — |
| RF-CON-005 | HU-CON-004 | CU-CON-004 | SVC-CON-003 | RN-CON-002 | — |
| RF-CON-006 | HU-CON-002 | CU-CON-002 | SVC-CON-002 | RN-CON-020 | — |
| RF-CON-007 | HU-CON-002 | CU-CON-002 | SVC-CON-002 | RN-CON-021 | — |
| RF-CON-008 | HU-CON-002 | CU-CON-002 | SVC-CON-002 | RN-CON-022 | — |
| RF-CON-009 | HU-CON-002 | — | — | RN-CON-022 | — |
| RF-CON-010 | HU-CON-003 | CU-CON-003 | SVC-CON-004 | RN-CON-030 | — |
| RF-CON-011 | HU-CON-003 | CU-CON-003 | SVC-CON-004 | RN-CON-031 | — |
| RF-CON-012 | HU-CON-003 | CU-CON-003 | SVC-CON-004 | RN-CON-032 | — |
| RF-CON-013 | HU-CON-003 | CU-CON-003 | SVC-CON-004 | RN-CON-032 | — |
| RF-CON-014 | HU-CON-004 | CU-CON-004 | SVC-CON-003 | RN-CON-002 | — |
| RF-CON-015 | HU-CON-004 | CU-CON-004 | SVC-CON-003 | RN-CON-002 | — |
| RF-CON-016 | HU-CON-004 | CU-CON-005 | — | RN-CON-004 | — |
| RF-CON-017 | HU-CON-005 | CU-CON-006 | SVC-CON-005 | RN-CON-010 | — |
| RF-CON-018 | HU-CON-005 | CU-CON-006 | SVC-CON-005 | RN-CON-010 | — |
| RF-CON-019 | HU-CON-005 | — | — | RN-CON-012 | — |
| RF-CON-020 | HU-CON-006 | CU-CON-007 | SVC-CON-006 | RN-CON-011, 012 | — |
| RF-CON-021 | HU-CON-006 | CU-CON-007 | SVC-CON-006 | RN-CON-050 | — |
| RF-CON-022 | HU-CON-006 | CU-CON-007 | SVC-CON-006 | RN-CON-050 | — |
| RF-CON-023 | HU-CON-006 | CU-CON-007 | SVC-CON-006 | RN-CON-050 | 2 |
| RF-CON-024 | HU-CON-006 | CU-CON-007 | SVC-CON-006 | RN-CON-052 | — |
| RF-CON-025 | HU-CON-007 | CU-CON-008 | SVC-CON-007 | RN-CON-060 | — |
| RF-CON-026 | HU-CON-007 | CU-CON-008 | SVC-CON-007 | RN-CON-060 | 1 |
| RF-CON-027 | HU-CON-007 | CU-CON-008 | SVC-CON-007 | RN-CON-061 | — |
| RF-CON-028 | HU-CON-008 | — | — | RN-CON-070 | — |
| RF-CON-029 | HU-CON-008 | — | — | RN-CON-070 | — |
| RF-CON-030 | HU-CON-008 | — | — | RN-CON-070 | — |
| RF-CON-031 | HU-CON-006 | — | — | RN-CON-052 | — |

---

# 6. Rastreabilidade por Regra

| Regra | Requisito | Entidade | Implementação | Teste |
| --- | --- | --- | --- | --- |
| RN-CON-001 | RF-CON-001, 002 | `Empenho` | `EmitirEmpenhoUseCase` | — |
| RN-CON-002 | RF-CON-003, 004, 005, 014 | `Empenho` | `Dotacao.empenhar_direto` | — |
| RN-CON-003 | RF-CON-001, 007 | `Empenho` | `saldo_a_liquidar` | — |
| RN-CON-004 | RF-CON-016 | `Empenho` | `TRANSICOES_EMPENHO` | — |
| RN-CON-010 | RF-CON-017, 018 | `ContaContabil` | `UNIQUE` + `CriarContaUseCase` | 1 |
| RN-CON-011 | RF-CON-020 | `ContaContabil` | `pode_receber_lancamento()` | — |
| RN-CON-012 | RF-CON-019, 020 | `ContaContabil` | `is_active` | — |
| RN-CON-020 | RF-CON-006 | `Liquidacao` | `Empenho.liquidar` | — |
| RN-CON-021 | RF-CON-007 | `Liquidacao` | `Empenho.liquidar` | — |
| RN-CON-022 | RF-CON-008, 009 | `Liquidacao` | `TRANSICOES_LIQUIDACAO` | — |
| RN-CON-030 | RF-CON-010 | `Pagamento` | `PagarLiquidacaoUseCase` | — |
| RN-CON-031 | RF-CON-011 | `Pagamento` | `Empenho.pagar` | — |
| RN-CON-032 | RF-CON-012, 013 | `Pagamento` | `StatusPagamento` | — |
| RN-CON-050 | RF-CON-021, 022, 023 | `LancamentoContabil` | `balanceado` / `lancar()` | 2 |
| RN-CON-051 | RF-CON-020 | `LancamentoContabil` | `LancarContabilUseCase` | — |
| RN-CON-052 | RF-CON-024, 031 | `LancamentoContabil` | campos `origem` | — |
| RN-CON-060 | RF-CON-025, 026 | `ConciliacaoContabil` | `conciliar()` | 1 |
| RN-CON-061 | RF-CON-027 | `ConciliacaoContabil` | `marcar_divergente()` | — |
| RN-CON-070 | RF-CON-028, 029, 030 | todas | não implementada | — |

---

# 7. Rastreabilidade Entidade × Persistência

| Entidade | Tabela | Operações de escrita | Campos perdidos | Achado |
| --- | --- | --- | --- | --- |
| `Empenho` | `con.empenhos` | `save`, `get_by_id`, `get_by_numero_exercicio` | `favorecido_id`, `data_anulacao` | A-01 |
| `Liquidacao` | `con.liquidacoes` | `save`, `get_by_id` | `descricao`, `data_liquidacao`, `data_cancelamento` | A-01 |
| `Pagamento` | `con.pagamentos` | `save`, `get_by_id` | `descricao`, `data_programacao`, `data_efetivacao` | A-01 |
| `ContaContabil` | `con.contas_contabeis` | `save`, `get_by_id`, `get_by_codigo` | `grupo` | A-01 |
| `LancamentoContabil` | `con.lancamentos` | `save`, `get_by_id` | `data_lancamento` | A-01 |
| `ConciliacaoContabil` | `con.conciliacoes` | `save`, `get_by_id` | — | — |

---

# 8. Indicadores de Rastreabilidade

| Indicador | Valor |
| --- | --- |
| Capacidades | 8 |
| Histórias | 8 |
| Requisitos funcionais | 31 |
| Regras | 19 |
| Casos de uso | 8 |
| Serviços | 7 |
| Critérios de aceitação | 46 |
| Requisitos com teste automatizado | 4 de 31 (13 %) |
| Regras com teste automatizado | 5 de 19 (26 %) |
| Entidades com perda de campo | 5 de 6 (83 %) |

**Conclusão:** a rastreabilidade **declarativa** está completa e consistente, mas a
rastreabilidade **verificada** é insuficiente — menos de um terço dos requisitos possui
teste automatizado, e nenhuma capacidade é acessível ao consumidor.


---

Este artefato assegura que toda capacidade, história, requisito e regra do
domínio de Contabilidade Pública está rastreada ao código e aos testes correspondentes,
e que nenhuma peça de trabalho existe sem vínculo.

---

# 2. Princípios de Rastreabilidade

* Nenhum requisito existe sem capacidade, história e regra associadas.
* Nenhuma regra existe sem requisito que a exija.
* Nenhum serviço existe sem caso de uso que o implemente.
* Nenhuma entidade existe sem operação que a persista.
* Requisito sem teste é requisito não verificado.

---

# 3. Rastreabilidade por Capacidade

| Capacidade | Histórias | Requisitos | Regras | Casos de uso | Serviços |
| --- | --- | --- | --- | --- | --- |
| CAP-CON-001 | HU-CON-005 | RF-CON-017 a 019 | RN-CON-010, 011, 012 | CU-CON-006 | SVC-CON-005 |
| CAP-CON-002 | HU-CON-001, HU-CON-004 | RF-CON-001 a 005, 014 a 016 | RN-CON-001, 002, 003, 004 | CU-CON-001, 004, 005 | SVC-CON-001, 003 |
| CAP-CON-003 | HU-CON-002 | RF-CON-006 a 009 | RN-CON-020, 021, 022 | CU-CON-002 | SVC-CON-002 |
| CAP-CON-004 | HU-CON-003 | RF-CON-010 a 013 | RN-CON-030, 031, 032 | CU-CON-003 | SVC-CON-004 |
| CAP-CON-005 | HU-CON-006 | RF-CON-020 a 024, 031 | RN-CON-050, 051, 052 | CU-CON-007 | SVC-CON-006 |
| CAP-CON-006 | HU-CON-007 | RF-CON-025 a 027 | RN-CON-060, 061 | CU-CON-008 | SVC-CON-007 |
| CAP-CON-007 | HU-CON-008 | RF-CON-028, 029 | RN-CON-070 | — | — |
| CAP-CON-008 | HU-CON-008 | RF-CON-030 | RN-CON-070 | — | — |

---

# 4. Rastreabilidade por História

| História | Capacidade | Casos de uso | Critérios | Testes | Requisitos |
| --- | --- | --- | --- | --- | --- |
| HU-CON-001 | CAP-CON-002 | CU-CON-001 | 7 | 1 | RF-CON-001 a 005 |
| HU-CON-002 | CAP-CON-003 | CU-CON-002 | 6 | 1 | RF-CON-006 a 009 |
| HU-CON-003 | CAP-CON-004 | CU-CON-003 | 6 | 0 | RF-CON-010 a 013 |
| HU-CON-004 | CAP-CON-002 | CU-CON-004, CU-CON-005 | 7 | 0 | RF-CON-014 a 016 |
| HU-CON-005 | CAP-CON-001 | CU-CON-006 | 7 | 1 | RF-CON-017 a 019 |
| HU-CON-006 | CAP-CON-005 | CU-CON-007 | 6 | 2 | RF-CON-020 a 024 |
| HU-CON-007 | CAP-CON-006 | CU-CON-008 | 4 | 1 | RF-CON-025 a 027 |
| HU-CON-008 | CAP-CON-007, 008 | — | 3 | 0 | RF-CON-028 a 030 |

---

# 5. Rastreabilidade por Requisito Funcional

| Requisito | História | Caso de uso | Serviço | Regra | Teste |
| --- | --- | --- | --- | --- | --- |
| RF-CON-001 | HU-CON-001 | CU-CON-001 | SVC-CON-001 | RN-CON-001 | — |
| RF-CON-002 | HU-CON-001 | CU-CON-001 | SVC-CON-001 | RN-CON-001 | — |
| RF-CON-003 | HU-CON-001 | CU-CON-001 | SVC-CON-001 | RN-CON-002 | — |
| RF-CON-004 | HU-CON-001 | CU-CON-001 | SVC-CON-001 | RN-CON-002 | — |
| RF-CON-005 | HU-CON-004 | CU-CON-004 | SVC-CON-003 | RN-CON-002 | — |
| RF-CON-006 | HU-CON-002 | CU-CON-002 | SVC-CON-002 | RN-CON-020 | — |
| RF-CON-007 | HU-CON-002 | CU-CON-002 | SVC-CON-002 | RN-CON-021 | — |
| RF-CON-008 | HU-CON-002 | CU-CON-002 | SVC-CON-002 | RN-CON-022 | — |
| RF-CON-009 | HU-CON-002 | — | — | RN-CON-022 | — |
| RF-CON-010 | HU-CON-003 | CU-CON-003 | SVC-CON-004 | RN-CON-030 | — |
| RF-CON-011 | HU-CON-003 | CU-CON-003 | SVC-CON-004 | RN-CON-031 | — |
| RF-CON-012 | HU-CON-003 | CU-CON-003 | SVC-CON-004 | RN-CON-032 | — |
| RF-CON-013 | HU-CON-003 | CU-CON-003 | SVC-CON-004 | RN-CON-032 | — |
| RF-CON-014 | HU-CON-004 | CU-CON-004 | SVC-CON-003 | RN-CON-002 | — |
| RF-CON-015 | HU-CON-004 | CU-CON-004 | SVC-CON-003 | RN-CON-002 | — |
| RF-CON-016 | HU-CON-004 | CU-CON-005 | — | RN-CON-004 | — |
| RF-CON-017 | HU-CON-005 | CU-CON-006 | SVC-CON-005 | RN-CON-010 | — |
| RF-CON-018 | HU-CON-005 | CU-CON-006 | SVC-CON-005 | RN-CON-010 | — |
| RF-CON-019 | HU-CON-005 | — | — | RN-CON-012 | — |
| RF-CON-020 | HU-CON-006 | CU-CON-007 | SVC-CON-006 | RN-CON-011, 012 | — |
| RF-CON-021 | HU-CON-006 | CU-CON-007 | SVC-CON-006 | RN-CON-050 | — |
| RF-CON-022 | HU-CON-006 | CU-CON-007 | SVC-CON-006 | RN-CON-050 | — |
| RF-CON-023 | HU-CON-006 | CU-CON-007 | SVC-CON-006 | RN-CON-050 | 2 |
| RF-CON-024 | HU-CON-006 | CU-CON-007 | SVC-CON-006 | RN-CON-052 | — |
| RF-CON-025 | HU-CON-007 | CU-CON-008 | SVC-CON-007 | RN-CON-060 | — |
| RF-CON-026 | HU-CON-007 | CU-CON-008 | SVC-CON-007 | RN-CON-060 | 1 |
| RF-CON-027 | HU-CON-007 | CU-CON-008 | SVC-CON-007 | RN-CON-061 | — |
| RF-CON-028 | HU-CON-008 | — | — | RN-CON-070 | — |
| RF-CON-029 | HU-CON-008 | — | — | RN-CON-070 | — |
| RF-CON-030 | HU-CON-008 | — | — | RN-CON-070 | — |
| RF-CON-031 | HU-CON-006 | — | — | RN-CON-052 | — |

---

# 6. Rastreabilidade por Regra

| Regra | Requisito | Entidade | Implementação | Teste |
| --- | --- | --- | --- | --- |
| RN-CON-001 | RF-CON-001, 002 | `Empenho` | `EmitirEmpenhoUseCase` | — |
| RN-CON-002 | RF-CON-003, 004, 005, 014 | `Empenho` | `Dotacao.empenhar_direto` | — |
| RN-CON-003 | RF-CON-001, 007 | `Empenho` | `saldo_a_liquidar` | — |
| RN-CON-004 | RF-CON-016 | `Empenho` | `TRANSICOES_EMPENHO` | — |
| RN-CON-010 | RF-CON-017, 018 | `ContaContabil` | `UNIQUE` + `CriarContaUseCase` | 1 |
| RN-CON-011 | RF-CON-020 | `ContaContabil` | `pode_receber_lancamento()` | — |
| RN-CON-012 | RF-CON-019, 020 | `ContaContabil` | `is_active` | — |
| RN-CON-020 | RF-CON-006 | `Liquidacao` | `Empenho.liquidar` | — |
| RN-CON-021 | RF-CON-007 | `Liquidacao` | `Empenho.liquidar` | — |
| RN-CON-022 | RF-CON-008, 009 | `Liquidacao` | `TRANSICOES_LIQUIDACAO` | — |
| RN-CON-030 | RF-CON-010 | `Pagamento` | `PagarLiquidacaoUseCase` | — |
| RN-CON-031 | RF-CON-011 | `Pagamento` | `Empenho.pagar` | — |
| RN-CON-032 | RF-CON-012, 013 | `Pagamento` | `StatusPagamento` | — |
| RN-CON-050 | RF-CON-021, 022, 023 | `LancamentoContabil` | `balanceado` / `lancar()` | 2 |
| RN-CON-051 | RF-CON-020 | `LancamentoContabil` | `LancarContabilUseCase` | — |
| RN-CON-052 | RF-CON-024, 031 | `LancamentoContabil` | campos `origem` | — |
| RN-CON-060 | RF-CON-025, 026 | `ConciliacaoContabil` | `conciliar()` | 1 |
| RN-CON-061 | RF-CON-027 | `ConciliacaoContabil` | `marcar_divergente()` | — |
| RN-CON-070 | RF-CON-028, 029, 030 | todas | não implementada | — |

---

# 7. Rastreabilidade Entidade × Persistência

| Entidade | Tabela | Operações de escrita | Campos perdidos | Achado |
| --- | --- | --- | --- | --- |
| `Empenho` | `con.empenhos` | `save`, `get_by_id`, `get_by_numero_exercicio` | `favorecido_id`, `data_anulacao` | A-01 |
| `Liquidacao` | `con.liquidacoes` | `save`, `get_by_id` | `descricao`, `data_liquidacao`, `data_cancelamento` | A-01 |
| `Pagamento` | `con.pagamentos` | `save`, `get_by_id` | `descricao`, `data_programacao`, `data_efetivacao` | A-01 |
| `ContaContabil` | `con.contas_contabeis` | `save`, `get_by_id`, `get_by_codigo` | `grupo` | A-01 |
| `LancamentoContabil` | `con.lancamentos` | `save`, `get_by_id` | `data_lancamento` | A-01 |
| `ConciliacaoContabil` | `con.conciliacoes` | `save`, `get_by_id` | — | — |

---

# 8. Indicadores de Rastreabilidade

| Indicador | Valor |
| --- | --- |
| Capacidades | 8 |
| Histórias | 8 |
| Requisitos funcionais | 31 |
| Regras | 19 |
| Casos de uso | 8 |
| Serviços | 7 |
| Critérios de aceitação | 46 |
| Requisitos com teste automatizado | 4 de 31 (13 %) |
| Regras com teste automatizado | 5 de 19 (26 %) |
| Entidades com perda de campo | 5 de 6 (83 %) |

**Conclusão:** a rastreabilidade **declarativa** está completa e consistente, mas a
rastreabilidade **verificada** é insuficiente — menos de um terço dos requisitos possui
teste automatizado, e nenhuma capacidade é acessível ao consumidor.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 012-Matriz-de-Rastreabilidade-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
