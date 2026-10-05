# 021 – Checklist de Prontidão para Produção – Contabilidade Pública

#### Checklist de Prontidão para Produção – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-021

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

Este artefato consolida o checklist de prontidão para produção do domínio de
Contabilidade Pública, reunindo as condições objetivas que devem ser satisfeitas
antes da entrada em operação.

---

# 2. Como usar

Cada item deve ser verificado e registrado com evidência. Item não verificado
impede a liberação. Os itens marcados como **bloqueadores** comprometem a correção do
registro contábil e, portanto, a prestação de contas.

---

# 3. Checklist

## 3.1 Persistência — Bloqueadores

| # | Item | Critério de verificação | Estado |
| --- | --- | --- | --- |
| 1.1 | Schema `con` criado | `information_schema.schemata` contém `con` | Atendido |
| 1.2 | Seis tabelas criadas | As seis tabelas constam em `con` | Atendido |
| 1.3 | Dez colunas ausentes criadas | `data_lancamento`, `data_anulacao`, `data_liquidacao`, `data_cancelamento`, `data_programacao`, `data_efetivacao`, `favorecido_id`, dois `descricao`, `grupo` | **Pendente** |
| 1.4 | `UNIQUE (exercicio, numero)` ativa | Tentativa de inserir duplicata é recusada | **Pendente** |
| 1.5 | Chave estrangeira para dotação | `con.empenhos.dotacao_id` referencia `orc.dotacoes` | **Pendente** |
| 1.6 | Chave estrangeira para conta na conciliação | `con.conciliacoes.conta_id` referencia `con.contas_contabeis` | **Pendente** |
| 1.7 | Índices criados | Sete índices presentes | **Pendente** |
| 1.8 | `ON DELETE RESTRICT` preservado | Foreign keys com `RESTRICT` | Atendido |
| 1.9 | `downgrade` testado | Reversão executada em homologação | **Pendente** |
| 1.10 | Divergência ORM × banco verificada | `Base.metadata` confere com `information_schema` | **Pendente** |

## 3.2 Exposição da API — Bloqueadores

| # | Item | Critério de verificação | Estado |
| --- | --- | --- | --- |
| 2.1 | Routers importados em `src/main.py` | `grep sigmun_con src/main.py` retorna ocorrência | **Pendente** |
| 2.2 | Routers registrados | `app.include_router` presente | **Pendente** |
| 2.3 | Sete rotas no OpenAPI | `app.openapi()['paths']` contém as sete rotas | **Pendente** |
| 2.4 | Tag declarada | `Contabilidade Pública` presente nas tags | **Pendente** |
| 2.5 | Recurso ausente responde 404 | Teste de integração | **Pendente** |
| 2.6 | Saldo insuficiente responde 422 | Teste de integração | **Pendente** |

## 3.3 Integração — Bloqueadores

| # | Item | Critério de verificação | Estado |
| --- | --- | --- | --- |
| 3.1 | Routers do DOM-ORC registrados | Dotações acessíveis | **Pendente** |
| 3.2 | Ciclo completo validado | Dotação → empenho → liquidação → pagamento | **Pendente** |
| 3.3 | Falha transacional revertida | Débito revertido quando a gravação falha | **Pendente** |
| 3.4 | Documento fiscal referenciado | Referência validada no DOM-GDO | **Pendente** |
| 3.5 | Autorização por perfil aplicada | Perfil do contador não cancela empenho | **Pendente** |

## 3.4 Qualidade

| # | Item | Critério de verificação | Estado |
| --- | --- | --- | --- |
| 4.1 | `ruff check` sem erros | Comando retorna sucesso | Atendido |
| 4.2 | `mypy` sem erros | `Found 0 errors` | **131 erros** |
| 4.3 | Cobertura de linhas ≥ 80 % | Relatório de cobertura | **Baixa** |
| 4.4 | Regras com teste | 19 de 19 | **5 de 19** |
| 4.5 | Critérios implementados com teste | 43 de 43 | **6 de 43** |
| 4.6 | Suíte de integração da API | Testes de endpoint | **Inexistente** |

## 3.5 Auditoria e Segurança — Bloqueadores

| # | Item | Critério de verificação | Estado |
| --- | --- | --- | --- |
| 5.1 | `created_by` preenchido | Registro com autor | **Pendente** |
| 5.2 | `updated_at` e `updated_by` completos | Todas as tabelas | **Pendente** |
| 5.3 | Eventos de domínio emitidos | Eventos no barramento | **Pendente** |
| 5.4 | Idempotência das escritas | Reenvio não duplica | **Pendente** |
| 5.5 | Imutabilidade do lançamento lançado | Estorno apenas por contrapartida | **Pendente** |

## 3.6 Dados

| # | Item | Critério de verificação | Estado |
| --- | --- | --- | --- |
| 6.1 | PCASP carregado | Contas criadas conforme o plano oficial | **Pendente** |
| 6.2 | Dotações vigentes no DOM-ORC | Dotação por unidade e ação | **Pendente** |
| 6.3 | Exercício fiscal corrente configurado | Ano em uso validado | Atendido |
| 6.4 | Fontes de favorecidos integradas | `favorecido_id` referenciado | **Pendente** |

## 3.7 Documentação

| # | Item | Critério de verificação | Estado |
| --- | --- | --- | --- |
| 7.1 | Artefatos 000 a 026 com conteúdo real | Documentos sem boilerplate | Atendido |
| 7.2 | Diagramas PlantUML validados | Seis diagramas renderizam | Atendido |
| 7.3 | Matriz de rastreabilidade completa | RN ↔ RF ↔ código ↔ teste | Atendido |
| 7.4 | Conformidade legal referenciada | LC 4.320/64, MCASP, TCE | Atendido |
| 7.5 | Plano de retorno operacional | Documento publicado | Atendido |
| 7.6 | Treinamento realizado | Público capacitado | **Pendente** |

---

# 4. Resumo

| Bloco | Itens | Atendidos | Pendentes | Bloqueadores |
| --- | --- | --- | --- | --- |
| Persistência | 10 | 2 | 8 | 8 |
| Exposição da API | 6 | 0 | 6 | 6 |
| Integração | 5 | 0 | 5 | 5 |
| Qualidade | 6 | 1 | 5 | 0 |
| Auditoria e segurança | 5 | 0 | 5 | 5 |
| Dados | 4 | 1 | 3 | 0 |
| Documentação | 6 | 5 | 1 | 0 |
| **Total** | **42** | **9** | **33** | **24** |

---

# 5. Decisão

**O DOM-CON NÃO está pronto para produção.**

Dos 42 itens verificados, **9 estão atendidos** e **24 são bloqueadores**. A
implantação não deve ocorrer antes da resolução, no mínimo, dos itens bloqueadores.

O caminho crítico de liberação está descrito em
`PLANO-DE-TRABALHO-DOM-CON-2026-09-30.md`, nas ondas 0 a 3.

---

# 6. Registro de Verificação

| Data | Verificador | Resultado | Observação |
| --- | --- | --- | --- |
| 2026-09-30 | Equipe SIGMUN | **Não aprovado** | 33 pendências, sendo 24 bloqueadoras |


---

Este artefato consolida o checklist de prontidão para produção do domínio de
Contabilidade Pública, reunindo as condições objetivas que devem ser satisfeitas
antes da entrada em operação.

---

# 2. Como usar

Cada item deve ser verificado e registrado com evidência. Item não verificado
impede a liberação. Os itens marcados como **bloqueadores** comprometem a correção do
registro contábil e, portanto, a prestação de contas.

---

# 3. Checklist

## 3.1 Persistência — Bloqueadores

| # | Item | Critério de verificação | Estado |
| --- | --- | --- | --- |
| 1.1 | Schema `con` criado | `information_schema.schemata` contém `con` | Atendido |
| 1.2 | Seis tabelas criadas | As seis tabelas constam em `con` | Atendido |
| 1.3 | Dez colunas ausentes criadas | `data_lancamento`, `data_anulacao`, `data_liquidacao`, `data_cancelamento`, `data_programacao`, `data_efetivacao`, `favorecido_id`, dois `descricao`, `grupo` | **Pendente** |
| 1.4 | `UNIQUE (exercicio, numero)` ativa | Tentativa de inserir duplicata é recusada | **Pendente** |
| 1.5 | Chave estrangeira para dotação | `con.empenhos.dotacao_id` referencia `orc.dotacoes` | **Pendente** |
| 1.6 | Chave estrangeira para conta na conciliação | `con.conciliacoes.conta_id` referencia `con.contas_contabeis` | **Pendente** |
| 1.7 | Índices criados | Sete índices presentes | **Pendente** |
| 1.8 | `ON DELETE RESTRICT` preservado | Foreign keys com `RESTRICT` | Atendido |
| 1.9 | `downgrade` testado | Reversão executada em homologação | **Pendente** |
| 1.10 | Divergência ORM × banco verificada | `Base.metadata` confere com `information_schema` | **Pendente** |

## 3.2 Exposição da API — Bloqueadores

| # | Item | Critério de verificação | Estado |
| --- | --- | --- | --- |
| 2.1 | Routers importados em `src/main.py` | `grep sigmun_con src/main.py` retorna ocorrência | **Pendente** |
| 2.2 | Routers registrados | `app.include_router` presente | **Pendente** |
| 2.3 | Sete rotas no OpenAPI | `app.openapi()['paths']` contém as sete rotas | **Pendente** |
| 2.4 | Tag declarada | `Contabilidade Pública` presente nas tags | **Pendente** |
| 2.5 | Recurso ausente responde 404 | Teste de integração | **Pendente** |
| 2.6 | Saldo insuficiente responde 422 | Teste de integração | **Pendente** |

## 3.3 Integração — Bloqueadores

| # | Item | Critério de verificação | Estado |
| --- | --- | --- | --- |
| 3.1 | Routers do DOM-ORC registrados | Dotações acessíveis | **Pendente** |
| 3.2 | Ciclo completo validado | Dotação → empenho → liquidação → pagamento | **Pendente** |
| 3.3 | Falha transacional revertida | Débito revertido quando a gravação falha | **Pendente** |
| 3.4 | Documento fiscal referenciado | Referência validada no DOM-GDO | **Pendente** |
| 3.5 | Autorização por perfil aplicada | Perfil do contador não cancela empenho | **Pendente** |

## 3.4 Qualidade

| # | Item | Critério de verificação | Estado |
| --- | --- | --- | --- |
| 4.1 | `ruff check` sem erros | Comando retorna sucesso | Atendido |
| 4.2 | `mypy` sem erros | `Found 0 errors` | **131 erros** |
| 4.3 | Cobertura de linhas ≥ 80 % | Relatório de cobertura | **Baixa** |
| 4.4 | Regras com teste | 19 de 19 | **5 de 19** |
| 4.5 | Critérios implementados com teste | 43 de 43 | **6 de 43** |
| 4.6 | Suíte de integração da API | Testes de endpoint | **Inexistente** |

## 3.5 Auditoria e Segurança — Bloqueadores

| # | Item | Critério de verificação | Estado |
| --- | --- | --- | --- |
| 5.1 | `created_by` preenchido | Registro com autor | **Pendente** |
| 5.2 | `updated_at` e `updated_by` completos | Todas as tabelas | **Pendente** |
| 5.3 | Eventos de domínio emitidos | Eventos no barramento | **Pendente** |
| 5.4 | Idempotência das escritas | Reenvio não duplica | **Pendente** |
| 5.5 | Imutabilidade do lançamento lançado | Estorno apenas por contrapartida | **Pendente** |

## 3.6 Dados

| # | Item | Critério de verificação | Estado |
| --- | --- | --- | --- |
| 6.1 | PCASP carregado | Contas criadas conforme o plano oficial | **Pendente** |
| 6.2 | Dotações vigentes no DOM-ORC | Dotação por unidade e ação | **Pendente** |
| 6.3 | Exercício fiscal corrente configurado | Ano em uso validado | Atendido |
| 6.4 | Fontes de favorecidos integradas | `favorecido_id` referenciado | **Pendente** |

## 3.7 Documentação

| # | Item | Critério de verificação | Estado |
| --- | --- | --- | --- |
| 7.1 | Artefatos 000 a 026 com conteúdo real | Documentos sem boilerplate | Atendido |
| 7.2 | Diagramas PlantUML validados | Seis diagramas renderizam | Atendido |
| 7.3 | Matriz de rastreabilidade completa | RN ↔ RF ↔ código ↔ teste | Atendido |
| 7.4 | Conformidade legal referenciada | LC 4.320/64, MCASP, TCE | Atendido |
| 7.5 | Plano de retorno operacional | Documento publicado | Atendido |
| 7.6 | Treinamento realizado | Público capacitado | **Pendente** |

---

# 4. Resumo

| Bloco | Itens | Atendidos | Pendentes | Bloqueadores |
| --- | --- | --- | --- | --- |
| Persistência | 10 | 2 | 8 | 8 |
| Exposição da API | 6 | 0 | 6 | 6 |
| Integração | 5 | 0 | 5 | 5 |
| Qualidade | 6 | 1 | 5 | 0 |
| Auditoria e segurança | 5 | 0 | 5 | 5 |
| Dados | 4 | 1 | 3 | 0 |
| Documentação | 6 | 5 | 1 | 0 |
| **Total** | **42** | **9** | **33** | **24** |

---

# 5. Decisão

**O DOM-CON NÃO está pronto para produção.**

Dos 42 itens verificados, **9 estão atendidos** e **24 são bloqueadores**. A
implantação não deve ocorrer antes da resolução, no mínimo, dos itens bloqueadores.

O caminho crítico de liberação está descrito em
`PLANO-DE-TRABALHO-DOM-CON-2026-09-30.md`, nas ondas 0 a 3.

---

# 6. Registro de Verificação

| Data | Verificador | Resultado | Observação |
| --- | --- | --- | --- |
| 2026-09-30 | Equipe SIGMUN | **Não aprovado** | 33 pendências, sendo 24 bloqueadoras |

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 021-Checklist-de-Prontidao-para-Producao-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
