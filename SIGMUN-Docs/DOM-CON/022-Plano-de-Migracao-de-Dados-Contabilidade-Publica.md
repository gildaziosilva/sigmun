# 022 – Plano de Migração de Dados – Contabilidade Pública

#### Plano de Migração de Dados – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-022

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

Este artefato define o plano de migração de dados do domínio de Contabilidade
Pública, abrangendo a carga inicial, a correção das divergências identificadas e a
evolução do schema `con`.

---

# 2. Inventário de Dados

| Entidade | Tabela | Registros iniciais | Origem |
| --- | --- | --- | --- |
| `ContaContabil` | `con.contas_contabeis` | Milhares | PCASP municipal |
| `Empenho` | `con.empenhos` | Zero | Operação futura |
| `Liquidacao` | `con.liquidacoes` | Zero | Operação futura |
| `Pagamento` | `con.pagamentos` | Zero | Operação futura |
| `LancamentoContabil` | `con.lancamentos` | Zero | Operação futura |
| `ConciliacaoContabil` | `con.conciliacoes` | Zero | Operação futura |

**Observação:** como o domínio nunca foi exposto, **não há histórico a migrar**. A
migração é exclusivamente de **carga inicial** e de **correção de estrutura**.

---

# 3. Carga Inicial

## 3.1 Plano de Contas

| Passo | Atividade | Volume esperado | Responsável |
| --- | --- | --- | --- |
| 1 | Exportar o PCASP oficial do município | — | Contabilidade |
| 2 | Validar estrutura de classes, grupos e naturezas | — | Contabilidade |
| 3 | Verificar unicidade de código | — | Contabilidade |
| 4 | Carregar em `con.contas_contabeis` | Milhares de linhas | Operação |
| 5 | Validar contagem e soma por classe | — | Contabilidade |

**Regras aplicadas na carga:**

* `tipo` = `analitica` quando o código tem desdobramento, `sintetica` caso contrário.
* `aceita_lancamento` = `true` apenas para contas analíticas (RN-CON-011).
* `ativa` = `true` na carga inicial.
* `conta_pai_id` resolvido a partir da hierarquia do código.

## 3.2 Dotações

As dotações **não pertencem** a este domínio. São carregadas no DOM-ORC e consumidas
por referência (`dotacao_id`).

**Risco:** se o DOM-ORC não estiver populado, o primeiro empenho falhará por dotação
inexistente.

---

# 4. Correção de Estrutura

A auditoria identificou **10 campos do domínio sem coluna** e ausência de restrições e
índices. A migration corretiva é a tarefa 1.1 do plano de trabalho.

| Coluna a criar | Tabela | Origem do valor na migração |
| --- | --- | --- |
| `favorecido_id` | `con.empenhos` | Não recuperável — registrar `NULL` |
| `data_anulacao` | `con.empenhos` | Não recuperável — registrar `NULL` |
| `descricao` | `con.liquidacoes` | Não recuperável — registrar `NULL` |
| `data_liquidacao` | `con.liquidacoes` | Derivada de `created_at` |
| `data_cancelamento` | `con.liquidacoes` | Não recuperável — registrar `NULL` |
| `descricao` | `con.pagamentos` | Não recuperável — registrar `NULL` |
| `data_programacao` | `con.pagamentos` | Derivada de `created_at` |
| `data_efetivacao` | `con.pagamentos` | Não recuperável — registrar `NULL` |
| `grupo` | `con.contas_contabeis` | Derivada da classe do PCASP |
| `data_lancamento` | `con.lancamentos` | Derivada de `created_at` |

**Advertência:** como não há dados históricos, os campos não recuperáveis serão
`NULL`. A partir da data de implantação, a informação passa a ser gravada
integralmente.

---

# 5. Restrições e Índices

| Objeto | Tipo | Efeito sobre os dados |
| --- | --- | --- |
| `UNIQUE (exercicio, numero)` | Restrição | Verificar duplicidade antes de criar |
| FK `dotacao_id → orc.dotacoes` | Integridade | Pode falhar se houver órfãos |
| FK `conta_id → contas_contabeis` | Integridade | Deve passar, pois ambos são do domínio |
| Sete índices | Desempenho | Nenhuma rejeição |

**Verificação prévia obrigatória:** antes de criar a chave estrangeira para a dotação,
consultar empenhos com `dotacao_id` inexistente na tabela `orc.dotacoes`.

```sql
SELECT e.id
  FROM con.empenhos e
  LEFT JOIN orc.dotacoes d ON d.id = e.dotacao_id
 WHERE d.id IS NULL;
```

---

# 6. Estratégia de Execução

| Etapa | Atividade | Ambiente |
| --- | --- | --- |
| 1 | Backup completo do banco | Produção |
| 2 | Aplicar migrations de criação do schema `con` | Já feito |
| 3 | Verificar órfãos de dotação e de conta | Produção (leitura) |
| 4 | Aplicar migration das colunas ausentes | Homologação |
| 5 | Aplicar restrições e índices | Homologação |
| 6 | Testar `downgrade` | Homologação |
| 7 | Repetir etapas 4 a 6 em produção | Produção |
| 8 | Validar `information_schema` contra `Base.metadata` | Produção |
| 9 | Carregar o PCASP | Produção |
| 10 | Validar a carga | Produção |

---

# 7. Validação

| Verificação | Resultado esperado |
| --- | --- |
| Colunas existem | Dez colunas presentes em `information_schema` |
| Restrição ativa | Inserção de empenho duplicado é recusada |
| Índices presentes | Sete índices em `pg_indexes` |
| ORM e banco alinhados | `Base.metadata` confere com `information_schema` |
| Round-trip | As dez colunas sobrevivem à gravação e releitura |
| PCASP carregado | Contagem de contas confere com o plano oficial |

---

# 8. Plano de Reversão

| Etapa | Reversão |
| --- | --- |
| Colunas ausentes | `alembic downgrade` remove as colunas; os dados não são recuperáveis |
| Restrições | `alembic downgrade` remove as constraints |
| Índices | `alembic downgrade` remove os índices |
| Carga do PCASP | `DELETE FROM con.contas_contabeis` |
| Aplicação | Remover os routers registrados em `src/main.py` |

**Backup:** deve ser realizado imediatamente antes da Etapa 7 e mantido por, no
mínimo, 90 dias.

---

# 9. Riscos

| Risco | Probabilidade | Impacto | Mitigação |
| --- | --- | --- | --- |
| Carga do PCASP com código duplicado | Média | Médio | Validar unicidade antes da carga |
| FK para dotação rejeitada por órfãos | Baixa | Alto | Consulta prévia da seção 5 |
| Perda de dados na reversão de coluna | Baixa | Alto | Backup obrigatório |
| Carga com naturzas de saldo incorretas | Média | **Alto** | Validação contábil antes de liberar |
| Divergência entre ORM e banco | Alta | Alto | Validar metadados na Etapa 8 |

---

# 10. Idempotência

| Operação | Idempotente |
| --- | --- |
| Criação de schema e tabelas | Sim (`IF NOT EXISTS`) |
| Criação de colunas | Não — falha se já existirem |
| Criação de índices | Sim (`IF NOT EXISTS`) |
| Carga do PCASP | Não — `UNIQUE` em `codigo` impede duplicidade |
| Aplicação de restrição `UNIQUE` | Não — falha se houver duplicatas |


---

Este artefato define o plano de migração de dados do domínio de Contabilidade
Pública, abrangendo a carga inicial, a correção das divergências identificadas e a
evolução do schema `con`.

---

# 2. Inventário de Dados

| Entidade | Tabela | Registros iniciais | Origem |
| --- | --- | --- | --- |
| `ContaContabil` | `con.contas_contabeis` | Milhares | PCASP municipal |
| `Empenho` | `con.empenhos` | Zero | Operação futura |
| `Liquidacao` | `con.liquidacoes` | Zero | Operação futura |
| `Pagamento` | `con.pagamentos` | Zero | Operação futura |
| `LancamentoContabil` | `con.lancamentos` | Zero | Operação futura |
| `ConciliacaoContabil` | `con.conciliacoes` | Zero | Operação futura |

**Observação:** como o domínio nunca foi exposto, **não há histórico a migrar**. A
migração é exclusivamente de **carga inicial** e de **correção de estrutura**.

---

# 3. Carga Inicial

## 3.1 Plano de Contas

| Passo | Atividade | Volume esperado | Responsável |
| --- | --- | --- | --- |
| 1 | Exportar o PCASP oficial do município | — | Contabilidade |
| 2 | Validar estrutura de classes, grupos e naturezas | — | Contabilidade |
| 3 | Verificar unicidade de código | — | Contabilidade |
| 4 | Carregar em `con.contas_contabeis` | Milhares de linhas | Operação |
| 5 | Validar contagem e soma por classe | — | Contabilidade |

**Regras aplicadas na carga:**

* `tipo` = `analitica` quando o código tem desdobramento, `sintetica` caso contrário.
* `aceita_lancamento` = `true` apenas para contas analíticas (RN-CON-011).
* `ativa` = `true` na carga inicial.
* `conta_pai_id` resolvido a partir da hierarquia do código.

## 3.2 Dotações

As dotações **não pertencem** a este domínio. São carregadas no DOM-ORC e consumidas
por referência (`dotacao_id`).

**Risco:** se o DOM-ORC não estiver populado, o primeiro empenho falhará por dotação
inexistente.

---

# 4. Correção de Estrutura

A auditoria identificou **10 campos do domínio sem coluna** e ausência de restrições e
índices. A migration corretiva é a tarefa 1.1 do plano de trabalho.

| Coluna a criar | Tabela | Origem do valor na migração |
| --- | --- | --- |
| `favorecido_id` | `con.empenhos` | Não recuperável — registrar `NULL` |
| `data_anulacao` | `con.empenhos` | Não recuperável — registrar `NULL` |
| `descricao` | `con.liquidacoes` | Não recuperável — registrar `NULL` |
| `data_liquidacao` | `con.liquidacoes` | Derivada de `created_at` |
| `data_cancelamento` | `con.liquidacoes` | Não recuperável — registrar `NULL` |
| `descricao` | `con.pagamentos` | Não recuperável — registrar `NULL` |
| `data_programacao` | `con.pagamentos` | Derivada de `created_at` |
| `data_efetivacao` | `con.pagamentos` | Não recuperável — registrar `NULL` |
| `grupo` | `con.contas_contabeis` | Derivada da classe do PCASP |
| `data_lancamento` | `con.lancamentos` | Derivada de `created_at` |

**Advertência:** como não há dados históricos, os campos não recuperáveis serão
`NULL`. A partir da data de implantação, a informação passa a ser gravada
integralmente.

---

# 5. Restrições e Índices

| Objeto | Tipo | Efeito sobre os dados |
| --- | --- | --- |
| `UNIQUE (exercicio, numero)` | Restrição | Verificar duplicidade antes de criar |
| FK `dotacao_id → orc.dotacoes` | Integridade | Pode falhar se houver órfãos |
| FK `conta_id → contas_contabeis` | Integridade | Deve passar, pois ambos são do domínio |
| Sete índices | Desempenho | Nenhuma rejeição |

**Verificação prévia obrigatória:** antes de criar a chave estrangeira para a dotação,
consultar empenhos com `dotacao_id` inexistente na tabela `orc.dotacoes`.

```sql
SELECT e.id
  FROM con.empenhos e
  LEFT JOIN orc.dotacoes d ON d.id = e.dotacao_id
 WHERE d.id IS NULL;
```

---

# 6. Estratégia de Execução

| Etapa | Atividade | Ambiente |
| --- | --- | --- |
| 1 | Backup completo do banco | Produção |
| 2 | Aplicar migrations de criação do schema `con` | Já feito |
| 3 | Verificar órfãos de dotação e de conta | Produção (leitura) |
| 4 | Aplicar migration das colunas ausentes | Homologação |
| 5 | Aplicar restrições e índices | Homologação |
| 6 | Testar `downgrade` | Homologação |
| 7 | Repetir etapas 4 a 6 em produção | Produção |
| 8 | Validar `information_schema` contra `Base.metadata` | Produção |
| 9 | Carregar o PCASP | Produção |
| 10 | Validar a carga | Produção |

---

# 7. Validação

| Verificação | Resultado esperado |
| --- | --- |
| Colunas existem | Dez colunas presentes em `information_schema` |
| Restrição ativa | Inserção de empenho duplicado é recusada |
| Índices presentes | Sete índices em `pg_indexes` |
| ORM e banco alinhados | `Base.metadata` confere com `information_schema` |
| Round-trip | As dez colunas sobrevivem à gravação e releitura |
| PCASP carregado | Contagem de contas confere com o plano oficial |

---

# 8. Plano de Reversão

| Etapa | Reversão |
| --- | --- |
| Colunas ausentes | `alembic downgrade` remove as colunas; os dados não são recuperáveis |
| Restrições | `alembic downgrade` remove as constraints |
| Índices | `alembic downgrade` remove os índices |
| Carga do PCASP | `DELETE FROM con.contas_contabeis` |
| Aplicação | Remover os routers registrados em `src/main.py` |

**Backup:** deve ser realizado imediatamente antes da Etapa 7 e mantido por, no
mínimo, 90 dias.

---

# 9. Riscos

| Risco | Probabilidade | Impacto | Mitigação |
| --- | --- | --- | --- |
| Carga do PCASP com código duplicado | Média | Médio | Validar unicidade antes da carga |
| FK para dotação rejeitada por órfãos | Baixa | Alto | Consulta prévia da seção 5 |
| Perda de dados na reversão de coluna | Baixa | Alto | Backup obrigatório |
| Carga com naturzas de saldo incorretas | Média | **Alto** | Validação contábil antes de liberar |
| Divergência entre ORM e banco | Alta | Alto | Validar metadados na Etapa 8 |

---

# 10. Idempotência

| Operação | Idempotente |
| --- | --- |
| Criação de schema e tabelas | Sim (`IF NOT EXISTS`) |
| Criação de colunas | Não — falha se já existirem |
| Criação de índices | Sim (`IF NOT EXISTS`) |
| Carga do PCASP | Não — `UNIQUE` em `codigo` impede duplicidade |
| Aplicação de restrição `UNIQUE` | Não — falha se houver duplicatas |

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 022-Plano-de-Migracao-de-Dados-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
