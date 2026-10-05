# 009 – Requisitos Não Funcionais – Contabilidade Pública

#### Requisitos Não Funcionais – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-009

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

Este artefato especifica os requisitos não funcionais do domínio de Contabilidade
Pública — desempenho, segurança, confiabilidade, usabilidade, manutenibilidade,
auditabilidade, compatibilidade e conformidade legal.

---

# 2. Convenções

* Identificador `RNF-CON-<grupo><sequencial>`, sendo o grupo a dimensão avaliada.
* Requisito não funcional é verificável por medição ou por inspeção.
* A coluna **Estado** reflete a situação apurada na auditoria.

---

# 3. Requisitos Não Funcionais

| Identificador | Dimensão | Requisito | Métrica | Estado |
| --- | --- | --- | --- | --- |
| RNF-CON-001 | Desempenho | Tempo de resposta dos serviços de escrita | p95 < 500 ms | Não medido |
| RNF-CON-002 | Desempenho | Tempo de resposta das consultas de execução | p95 < 2 s | Não aplicável (RF-CON-028 inexistente) |
| RNF-CON-003 | Desempenho | Capacidade de operações simultâneas | ≥ 50 requisições/s | Não medido |
| RNF-CON-004 | Disponibilidade | Disponibilidade do serviço de contabilidade | ≥ 99,5 % mensal | Não monitorado |
| RNF-CON-005 | Confiabilidade | Integridade transacional entre empenho e dotação | 100 % ou reversão | **Não garantida** |
| RNF-CON-006 | Confiabilidade | Durabilidade de registro contábil | Sem perda de dado após confirmação | **Violada** |
| RNF-CON-007 | Segurança | Autenticação obrigatória em toda operação | 100 % das rotas | Planejada |
| RNF-CON-008 | Segurança | Segregação de funções entre emitir e pagar | Aplicada no processo | Planejada |
| RNF-CON-009 | Segurança | Imutabilidade do registro após lançamento | Estorno apenas por contrapartida | Parcial |
| RNF-CON-010 | Auditabilidade | Trilha com autor, data e valores | 100 % das operações | **Não implementada** |
| RNF-CON-011 | Usabilidade | Redução de passos no ciclo da despesa | ≤ 4 telas por etapa | Não avaliado |
| RNF-CON-012 | Manutenibilidade | Tipagem estática integral do módulo | `mypy` sem erros | **131 erros** |
| RNF-CON-013 | Manutenibilidade | Cobertura de testes | ≥ 80 % de linhas | **6 testes** |
| RNF-CON-014 | Compatibilidade | Persistência em PostgreSQL | Schema `con` | Atendida |
| RNF-CON-015 | Conformidade | Conformidade à Lei 4.320/64 | Fase da despesa implementada | Parcial |
| RNF-CON-016 | Conformidade | Conformidade ao MCASP e PCASP | Estrutura de contas | Atendida |
| RNF-CON-017 | Portabilidade | Uso de `datetime` com fuso horário | UTC em toda a persistência | **Violada** (`utcnow` deprecado) |
| RNF-CON-018 | Observabilidade | Identificador de correlação da requisição | Middleware já existente | Planejada para o domínio |

---

# 4. Requisitos em Detalhe

## RNF-CON-005 — Integridade Transacional

**Descrição:** A emissão do empenho altera duas agregações: o orçamento (no DOM-ORC) e
o registro contábil (no DOM-CON). Ambas devem ser confirmadas ou revertidas em conjunto.

**Situação atual:** os casos de uso recebem a dotação por parâmetro e a persistem
**fora** da unidade transacional do empenho. Uma falha na gravação do empenho deixa a
dotação debitada sem contrapartida (achado M-03 / etapa 3.3 do plano).

**Como medir:** injetar falha na gravação do empenho e verificar se o saldo da dotação
é restabelecido.

---

## RNF-CON-006 — Durabilidade do Registro Contábil

**Descrição:** Nenhum campo declarado pela entidade de domínio pode ser perdido na
gravação.

**Situação atual:** **violada**. A auditoria identificou 10 campos do domínio sem coluna
correspondente: `data_lancamento` (obrigatória no MCASP), `data_anulacao`,
`data_liquidacao`, `data_cancelamento`, `data_programacao`, `data_efetivacao`,
`favorecido_id`, duas `descricao` e `grupo` (achado A-01).

**Como medir:** round-trip de cada entidade verificando campo a campo.

---

## RNF-CON-010 — Auditabilidade

**Descrição:** Toda operação com efeito contábil registra autor, data e valores antes e
depois.

**Situação atual:** os campos existem, mas `created_by` nunca é preenchido e
`lancamentos` e `conciliacoes` não possuem campos de atualização (achado M-04).

---

## RNF-CON-012 — Tipagem Estática

**Descrição:** O módulo deve passar em `mypy` sem erros.

**Situação atual:** 131 erros em 12 arquivos, concentrados nos repositórios (83), por
uso de `Column` sem `Mapped[]` (achado A-05).

**Como medir:** `mypy src/modules/sigmun_con/`.

---

## RNF-CON-013 — Cobertura de Testes

**Descrição:** Cobertura de linhas ≥ 80 %.

**Situação atual:** 6 testes unitários, 0 de integração. A máquina de estados do
empenho — que concentra o risco do domínio — não possui teste (achado A-07).

---

# 5. Resumo de Situação

| Situação | Quantidade |
| --- | --- |
| Atendida | 3 |
| Parcial ou planejada | 8 |
| Não aplicável no estado atual | 1 |
| **Violada ou não garantida** | 6 |

Os seis requisitos violados são exatamente os que sustentam a conformidade contábil
do domínio: integridade transacional, durabilidade, auditabilidade, tipagem,
cobertura e fuso horário.

---

# 6. Riscos Associados

| Risco | Requisito afetado | Mitigação |
| --- | --- | --- |
| Empenho órfão por falha parcial | RNF-CON-005 | Onda 1 do plano: teste de falha transacional |
| Perda de data de competência do lançamento | RNF-CON-006 | Onda 1, tarefa 1.1: migration das 10 colunas |
| Impossibilidade de responsabilização | RNF-CON-010 | Onda 4, tarefa 4.4 |
| Defeito não detectado em revisão | RNF-CON-013 | Onda 5, tarefa 5.8 |
| Registros sem fuso horário aplicável | RNF-CON-017 | Onda 6, tarefa 6.5 |


---

Este artefato especifica os requisitos não funcionais do domínio de Contabilidade
Pública — desempenho, segurança, confiabilidade, usabilidade, manutenibilidade,
auditabilidade, compatibilidade e conformidade legal.

---

# 2. Convenções

* Identificador `RNF-CON-<grupo><sequencial>`, sendo o grupo a dimensão avaliada.
* Requisito não funcional é verificável por medição ou por inspeção.
* A coluna **Estado** reflete a situação apurada na auditoria.

---

# 3. Requisitos Não Funcionais

| Identificador | Dimensão | Requisito | Métrica | Estado |
| --- | --- | --- | --- | --- |
| RNF-CON-001 | Desempenho | Tempo de resposta dos serviços de escrita | p95 < 500 ms | Não medido |
| RNF-CON-002 | Desempenho | Tempo de resposta das consultas de execução | p95 < 2 s | Não aplicável (RF-CON-028 inexistente) |
| RNF-CON-003 | Desempenho | Capacidade de operações simultâneas | ≥ 50 requisições/s | Não medido |
| RNF-CON-004 | Disponibilidade | Disponibilidade do serviço de contabilidade | ≥ 99,5 % mensal | Não monitorado |
| RNF-CON-005 | Confiabilidade | Integridade transacional entre empenho e dotação | 100 % ou reversão | **Não garantida** |
| RNF-CON-006 | Confiabilidade | Durabilidade de registro contábil | Sem perda de dado após confirmação | **Violada** |
| RNF-CON-007 | Segurança | Autenticação obrigatória em toda operação | 100 % das rotas | Planejada |
| RNF-CON-008 | Segurança | Segregação de funções entre emitir e pagar | Aplicada no processo | Planejada |
| RNF-CON-009 | Segurança | Imutabilidade do registro após lançamento | Estorno apenas por contrapartida | Parcial |
| RNF-CON-010 | Auditabilidade | Trilha com autor, data e valores | 100 % das operações | **Não implementada** |
| RNF-CON-011 | Usabilidade | Redução de passos no ciclo da despesa | ≤ 4 telas por etapa | Não avaliado |
| RNF-CON-012 | Manutenibilidade | Tipagem estática integral do módulo | `mypy` sem erros | **131 erros** |
| RNF-CON-013 | Manutenibilidade | Cobertura de testes | ≥ 80 % de linhas | **6 testes** |
| RNF-CON-014 | Compatibilidade | Persistência em PostgreSQL | Schema `con` | Atendida |
| RNF-CON-015 | Conformidade | Conformidade à Lei 4.320/64 | Fase da despesa implementada | Parcial |
| RNF-CON-016 | Conformidade | Conformidade ao MCASP e PCASP | Estrutura de contas | Atendida |
| RNF-CON-017 | Portabilidade | Uso de `datetime` com fuso horário | UTC em toda a persistência | **Violada** (`utcnow` deprecado) |
| RNF-CON-018 | Observabilidade | Identificador de correlação da requisição | Middleware já existente | Planejada para o domínio |

---

# 4. Requisitos em Detalhe

## RNF-CON-005 — Integridade Transacional

**Descrição:** A emissão do empenho altera duas agregações: o orçamento (no DOM-ORC) e
o registro contábil (no DOM-CON). Ambas devem ser confirmadas ou revertidas em conjunto.

**Situação atual:** os casos de uso recebem a dotação por parâmetro e a persistem
**fora** da unidade transacional do empenho. Uma falha na gravação do empenho deixa a
dotação debitada sem contrapartida (achado M-03 / etapa 3.3 do plano).

**Como medir:** injetar falha na gravação do empenho e verificar se o saldo da dotação
é restabelecido.

---

## RNF-CON-006 — Durabilidade do Registro Contábil

**Descrição:** Nenhum campo declarado pela entidade de domínio pode ser perdido na
gravação.

**Situação atual:** **violada**. A auditoria identificou 10 campos do domínio sem coluna
correspondente: `data_lancamento` (obrigatória no MCASP), `data_anulacao`,
`data_liquidacao`, `data_cancelamento`, `data_programacao`, `data_efetivacao`,
`favorecido_id`, duas `descricao` e `grupo` (achado A-01).

**Como medir:** round-trip de cada entidade verificando campo a campo.

---

## RNF-CON-010 — Auditabilidade

**Descrição:** Toda operação com efeito contábil registra autor, data e valores antes e
depois.

**Situação atual:** os campos existem, mas `created_by` nunca é preenchido e
`lancamentos` e `conciliacoes` não possuem campos de atualização (achado M-04).

---

## RNF-CON-012 — Tipagem Estática

**Descrição:** O módulo deve passar em `mypy` sem erros.

**Situação atual:** 131 erros em 12 arquivos, concentrados nos repositórios (83), por
uso de `Column` sem `Mapped[]` (achado A-05).

**Como medir:** `mypy src/modules/sigmun_con/`.

---

## RNF-CON-013 — Cobertura de Testes

**Descrição:** Cobertura de linhas ≥ 80 %.

**Situação atual:** 6 testes unitários, 0 de integração. A máquina de estados do
empenho — que concentra o risco do domínio — não possui teste (achado A-07).

---

# 5. Resumo de Situação

| Situação | Quantidade |
| --- | --- |
| Atendida | 3 |
| Parcial ou planejada | 8 |
| Não aplicável no estado atual | 1 |
| **Violada ou não garantida** | 6 |

Os seis requisitos violados são exatamente os que sustentam a conformidade contábil
do domínio: integridade transacional, durabilidade, auditabilidade, tipagem,
cobertura e fuso horário.

---

# 6. Riscos Associados

| Risco | Requisito afetado | Mitigação |
| --- | --- | --- |
| Empenho órfão por falha parcial | RNF-CON-005 | Onda 1 do plano: teste de falha transacional |
| Perda de data de competência do lançamento | RNF-CON-006 | Onda 1, tarefa 1.1: migration das 10 colunas |
| Impossibilidade de responsabilização | RNF-CON-010 | Onda 4, tarefa 4.4 |
| Defeito não detectado em revisão | RNF-CON-013 | Onda 5, tarefa 5.8 |
| Registros sem fuso horário aplicável | RNF-CON-017 | Onda 6, tarefa 6.5 |

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 009-Requisitos-Nao-Funcionais-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
