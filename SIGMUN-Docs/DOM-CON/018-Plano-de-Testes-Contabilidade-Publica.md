# 018 – Plano de Testes – Contabilidade Pública

#### Plano de Testes – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-018

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

Este artefato define o plano de testes do domínio de Contabilidade Pública,
estabelecendo estratégia, níveis, escopo, critérios de entrada e de saída, e a
situação atual da cobertura.

---

# 2. Estratégia

A estratégia é baseada em risco: os testes concentram-se nas invariantes
monetárias e nas transições de estado, onde o erro produz dano financeiro ou jurídico.

**Prioridade de teste:**

| Prioridade | Foco | Justificativa |
| --- | --- | --- |
| 1 | Invariantes de saldo | Erro gera pagamento indevido |
| 2 | Transições de estado | Erro permite burla ou saldo negativo |
| 3 | Integração com DOM-ORC | Erro compromete o orçamento |
| 4 | Regras do PCASP | Erro distorce o saldo contábil |
| 5 | Persistência | Erro perde informação |
| 6 | Formato da API | Menor impacto |

---

# 3. Níveis de Teste

| Nível | Escopo | Ferramenta | Quantidade atual |
| --- | --- | --- | --- |
| Unitário | Entidades e casos de uso, com dublês | `pytest` | 6 |
| Integração | Persistência contra PostgreSQL | `pytest` + banco | **0** |
| API | Endpoints com `TestClient` | `pytest` + FastAPI | **0** |
| Comportamento | Ciclo completo ponta a ponta | A definir | **0** |
| Não funcional | Desempenho, carga, segurança | A definir | **0** |

---

# 4. Situação Atual

## 4.1 Testes Existentes

| Arquivo | Testes | Cobre |
| --- | --- | --- |
| `tests/unit/test_con_contabil.py` | 3 | Lançamento balanceado, lançamento desequilibrado, criação de conta e conciliação |
| `tests/unit/test_con_use_cases.py` | 3 | Casos de uso de execução orçamentária |

## 4.2 Cobertura por Requisito

| Requisito | Testado | Observação |
| --- | --- | --- |
| RF-CON-017 Criar conta | Sim | `test_conta_e_conciliacao` |
| RF-CON-023 Recusar lançamento desequilibrado | Sim | `test_desequilibrado` |
| RF-CON-021 Registrar partidas dobradas | Sim | `test_lancamento_balanceado` |
| RF-CON-026 Calcular diferença | Sim | `test_conta_e_conciliacao` |
| RF-CON-001 a 005 Empenho | Parcial | Cenários negativos ausentes |
| RF-CON-006 a 009 Liquidação | Parcial | Cenários de saldo ausentes |
| RF-CON-010 a 013 Pagamento | Não | — |
| RF-CON-014 a 016 Anulação e cancelamento | Não | — |
| RF-CON-019 Desativar conta | Não | — |
| RF-CON-024 Origem do lançamento | Não | — |
| RF-CON-027 Justificativa de divergência | Não | — |

**Cobertura:** 4 de 31 requisitos funcionais (13 %).

## 4.3 Cobertura por Regra

5 de 19 regras possuem teste (26 %). As regras de máquina de estados do empenho
(RN-CON-003, RN-CON-004), de pagamento (RN-CON-030, RN-CON-031, RN-CON-032) e a de
auditoria (RN-CON-070) **não têm nenhum teste**.

---

# 5. Escopo Planejado

| Suíte | Casos | Prioridade |
| --- | --- | --- |
| Máquina de estados do empenho | 12 | Crítica |
| Invariantes de saldo | 10 | Crítica |
| Integração com DOM-ORC | 6 | Alta |
| Regras do PCASP | 8 | Alta |
| Conciliação | 5 | Média |
| Partidas dobradas | 6 | Média |
| Round-trip de persistência | 6 | Alta |
| API (7 serviços) | 14 | Alta |
| Não funcionais | 8 | Média |
| **Total** | **75** | — |

---

# 6. Estratégia de Dados de Teste

| Tipo | Fonte | Observação |
| --- | --- | --- |
| Dotação | Factory com saldo configurável | Saldo positivo, zero e insuficiente |
| Plano de contas | PCASP mínimo com 4 contas | Analítica ativa, analítica inativa, sintética |
| Favornecido | Dados fictícios | Sem dados pessoais reais — conformidade LGPD |
| Valores | Valores monetários fracionários | Exercitar arredondamento e diferença de 0,005 |
| Exercícios | Exercício corrente e anterior | Exercitar mudança de ano |

**Proibição:** nenhum teste deve utilizar dados pessoais reais de cidadãos ou
servidores (Lei 13.709/2018).

---

# 7. Ambiente

| Item | Configuração |
| --- | --- |
| Banco | PostgreSQL com schema `con` criado pelas migrations |
| Isolamento | Um schema por execução de teste |
| Limpeza | Truncamento das tabelas `con` entre suítes |
| Dependências externas | DOM-ORC com dotação de teste; DOM-GDO dublê |
| Variáveis | `APP_ENV=test` |

---

# 8. Critérios de Entrada

Um caso de teste entra na suíte quando:

* o requisito ou a regra correspondente está declarado e versionado;
* o comportamento esperado está escrito em formato *Dado / Quando / Então*;
* o caso é rastreado a um identificador (CA, RF ou RN).

---

# 9. Critérios de Saída

A versão do domínio é considerada testada quando:

* [ ] Cobertura de linhas ≥ 80 % no módulo `sigmun_con`
* [ ] Todas as regras RN-CON-001 a RN-CON-070 possuem ao menos um teste
* [ ] Todos os 43 critérios de aceitação implementados possuem teste
* [ ] `mypy src/modules/sigmun_con/` não reporta erros
* [ ] `ruff check src/modules/sigmun_con/` não reporta erros
* [ ] Ciclo completo validado ponta a ponta
* [ ] Teste de falha transacional entre empenho e dotação aprovado
* [ ] Round-trip preserva os 10 campos ausentes após a Onda 1

---

# 10. Riscos de Teste

| Risco | Probabilidade | Impacto | Mitigação |
| --- | --- | --- | --- |
| Cobertura concentrada no caminho feliz | Alta | Alto | Exigir cenário negativo por regra |
| Testes dependerem do DOM-ORC real | Média | Médio | Usar dublê de repositório |
| Ausência de teste de concorrência na numeração | Alta | Alto | Teste de unicidade no banco (Onda 1) |
| Falsos positivos por arredondamento de `FLOAT` | Média | Médio | Tolerância explícita nos testes |
| Testes não refletirem a migração da Onda 1 | Média | Alto | Round-trip como critério de saída |


---

Este artefato define o plano de testes do domínio de Contabilidade Pública,
estabelecendo estratégia, níveis, escopo, critérios de entrada e de saída, e a
situação atual da cobertura.

---

# 2. Estratégia

A estratégia é baseada em risco: os testes concentram-se nas invariantes
monetárias e nas transições de estado, onde o erro produz dano financeiro ou jurídico.

**Prioridade de teste:**

| Prioridade | Foco | Justificativa |
| --- | --- | --- |
| 1 | Invariantes de saldo | Erro gera pagamento indevido |
| 2 | Transições de estado | Erro permite burla ou saldo negativo |
| 3 | Integração com DOM-ORC | Erro compromete o orçamento |
| 4 | Regras do PCASP | Erro distorce o saldo contábil |
| 5 | Persistência | Erro perde informação |
| 6 | Formato da API | Menor impacto |

---

# 3. Níveis de Teste

| Nível | Escopo | Ferramenta | Quantidade atual |
| --- | --- | --- | --- |
| Unitário | Entidades e casos de uso, com dublês | `pytest` | 6 |
| Integração | Persistência contra PostgreSQL | `pytest` + banco | **0** |
| API | Endpoints com `TestClient` | `pytest` + FastAPI | **0** |
| Comportamento | Ciclo completo ponta a ponta | A definir | **0** |
| Não funcional | Desempenho, carga, segurança | A definir | **0** |

---

# 4. Situação Atual

## 4.1 Testes Existentes

| Arquivo | Testes | Cobre |
| --- | --- | --- |
| `tests/unit/test_con_contabil.py` | 3 | Lançamento balanceado, lançamento desequilibrado, criação de conta e conciliação |
| `tests/unit/test_con_use_cases.py` | 3 | Casos de uso de execução orçamentária |

## 4.2 Cobertura por Requisito

| Requisito | Testado | Observação |
| --- | --- | --- |
| RF-CON-017 Criar conta | Sim | `test_conta_e_conciliacao` |
| RF-CON-023 Recusar lançamento desequilibrado | Sim | `test_desequilibrado` |
| RF-CON-021 Registrar partidas dobradas | Sim | `test_lancamento_balanceado` |
| RF-CON-026 Calcular diferença | Sim | `test_conta_e_conciliacao` |
| RF-CON-001 a 005 Empenho | Parcial | Cenários negativos ausentes |
| RF-CON-006 a 009 Liquidação | Parcial | Cenários de saldo ausentes |
| RF-CON-010 a 013 Pagamento | Não | — |
| RF-CON-014 a 016 Anulação e cancelamento | Não | — |
| RF-CON-019 Desativar conta | Não | — |
| RF-CON-024 Origem do lançamento | Não | — |
| RF-CON-027 Justificativa de divergência | Não | — |

**Cobertura:** 4 de 31 requisitos funcionais (13 %).

## 4.3 Cobertura por Regra

5 de 19 regras possuem teste (26 %). As regras de máquina de estados do empenho
(RN-CON-003, RN-CON-004), de pagamento (RN-CON-030, RN-CON-031, RN-CON-032) e a de
auditoria (RN-CON-070) **não têm nenhum teste**.

---

# 5. Escopo Planejado

| Suíte | Casos | Prioridade |
| --- | --- | --- |
| Máquina de estados do empenho | 12 | Crítica |
| Invariantes de saldo | 10 | Crítica |
| Integração com DOM-ORC | 6 | Alta |
| Regras do PCASP | 8 | Alta |
| Conciliação | 5 | Média |
| Partidas dobradas | 6 | Média |
| Round-trip de persistência | 6 | Alta |
| API (7 serviços) | 14 | Alta |
| Não funcionais | 8 | Média |
| **Total** | **75** | — |

---

# 6. Estratégia de Dados de Teste

| Tipo | Fonte | Observação |
| --- | --- | --- |
| Dotação | Factory com saldo configurável | Saldo positivo, zero e insuficiente |
| Plano de contas | PCASP mínimo com 4 contas | Analítica ativa, analítica inativa, sintética |
| Favornecido | Dados fictícios | Sem dados pessoais reais — conformidade LGPD |
| Valores | Valores monetários fracionários | Exercitar arredondamento e diferença de 0,005 |
| Exercícios | Exercício corrente e anterior | Exercitar mudança de ano |

**Proibição:** nenhum teste deve utilizar dados pessoais reais de cidadãos ou
servidores (Lei 13.709/2018).

---

# 7. Ambiente

| Item | Configuração |
| --- | --- |
| Banco | PostgreSQL com schema `con` criado pelas migrations |
| Isolamento | Um schema por execução de teste |
| Limpeza | Truncamento das tabelas `con` entre suítes |
| Dependências externas | DOM-ORC com dotação de teste; DOM-GDO dublê |
| Variáveis | `APP_ENV=test` |

---

# 8. Critérios de Entrada

Um caso de teste entra na suíte quando:

* o requisito ou a regra correspondente está declarado e versionado;
* o comportamento esperado está escrito em formato *Dado / Quando / Então*;
* o caso é rastreado a um identificador (CA, RF ou RN).

---

# 9. Critérios de Saída

A versão do domínio é considerada testada quando:

* [ ] Cobertura de linhas ≥ 80 % no módulo `sigmun_con`
* [ ] Todas as regras RN-CON-001 a RN-CON-070 possuem ao menos um teste
* [ ] Todos os 43 critérios de aceitação implementados possuem teste
* [ ] `mypy src/modules/sigmun_con/` não reporta erros
* [ ] `ruff check src/modules/sigmun_con/` não reporta erros
* [ ] Ciclo completo validado ponta a ponta
* [ ] Teste de falha transacional entre empenho e dotação aprovado
* [ ] Round-trip preserva os 10 campos ausentes após a Onda 1

---

# 10. Riscos de Teste

| Risco | Probabilidade | Impacto | Mitigação |
| --- | --- | --- | --- |
| Cobertura concentrada no caminho feliz | Alta | Alto | Exigir cenário negativo por regra |
| Testes dependerem do DOM-ORC real | Média | Médio | Usar dublê de repositório |
| Ausência de teste de concorrência na numeração | Alta | Alto | Teste de unicidade no banco (Onda 1) |
| Falsos positivos por arredondamento de `FLOAT` | Média | Médio | Tolerância explícita nos testes |
| Testes não refletirem a migração da Onda 1 | Média | Alto | Round-trip como critério de saída |

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 018-Plano-de-Testes-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
