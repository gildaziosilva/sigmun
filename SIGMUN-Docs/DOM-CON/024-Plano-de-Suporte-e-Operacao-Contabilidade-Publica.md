# 024 – Plano de Suporte e Operação – Contabilidade Pública

#### Plano de Suporte e Operação – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-024

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

Este artefato define o plano de suporte e operação do domínio de Contabilidade
Pública, abrangendo níveis de atendimento, classificação de incidentes, rotinas
operacionais e indicadores de serviço.

---

# 2. Modelo de Serviço

| Aspecto | Definição |
| --- | --- |
| Classificação | Criticidade do impacto sobre a execução da despesa |
| Horário | Segunda a sexta, das 8 h às 17 h; plantão em prazos de encerramento |
| Canais | Sistema de chamados, e-mail e telefone da equipe de TI |
| Responsável primário | Equipe SIGMUN |
| Responsável de negócio | Contabilidade municipal |

---

# 3. Níveis de Atendimento

| Nível | Descrição | Prazo de resposta | Prazo de solução |
| --- | --- | --- | --- |
| N1 — Atendimento | Dúvida de uso, orientação | 4 horas | 2 dias úteis |
| N2 — Incidente | Operação impedida | 1 hora | 1 dia útil |
| N3 — Falha crítica | Impacto financeiro ou no orçamento | 30 minutos | 4 horas |
| N4 — Emergência | Indisponibilidade em prazo de fechamento | 15 minutos | 1 hora |

---

# 4. Classificação de Incidentes

| Categoria | Exemplo | Nível | Ação |
| --- | --- | --- | --- |
| Regra de negócio | Empenho recusado por saldo insuficiente | N1 | Orientar sobre a dotação |
| Regra de negócio | Número de empenho já utilizado | N1 | Orientar sobre a numeração |
| Integração | Dotação não localizada | N3 | Verificar cadastro no DOM-ORC |
| Integração | Divergência de saldo após empenho | N3 | Estornar conforme procedimento |
| Dados | Lançamento sem data de competência | N3 | Registrar a data manualmente |
| Dados | Falha de escrita após débito na dotação | N3 | Reverter o débito no DOM-ORC |
| Aplicação | Erro 500 em serviço de contabilidade | N4 | Verificar logs e retornar versão anterior |
| Disponibilidade | API indisponível | N4 | Acionar plantão |
| Segurança | Acesso indevido | N3 | Bloquear acesso e auditar |
| Dados | Tentativa de lançamento desequilibrado | N2 | Registrar ocorrência |

---

# 5. Procedimentos Operacionais

## 5.1 Verificação Diária

| Atividade | Frequência | Responsável |
| --- | --- | --- |
| Confirmar saúde da API e do banco | Diária | Operação |
| Verificar erros no log | Diária | Operação |
| Conferir totais de empenho do dia | Diária | Contabilidade |
| Validar backups | Diária | DBA |
| Conferir fila de chamados | Diária | Suporte |

## 5.2 Rotinas Mensais

| Atividade | Frequência | Responsável |
| --- | --- | --- |
| Análise de desempenho | Mensal | Operação |
| Revisão de incidentes | Mensal | Equipe SIGMUN |
| Atualização de documentação | Mensal | Equipe SIGMUN |
| Revisão de permissões | Mensal | Segurança |

## 5.3 Rotinas Anuais

| Atividade | Frequência | Responsável |
| --- | --- | --- |
| Revisão do plano de contas | Anual | Contabilidade |
| Teste de recuperação de backup | Anual | DBA |
| Revisão de políticas de acesso | Anual | Segurança |
| Auditoria do domínio | Anual | Controle interno |

---

# 6. Reinício do Exercício Fiscal

Procedimento crítico no encerramento do exercício:

| Passo | Atividade | Responsável |
| --- | --- | --- |
| 1 | Confirmar que não há empenho pendente de pagamento | Contabilidade |
| 2 | Conciliar todas as contas bancárias do exercício | Contador da conciliação |
| 3 | Emitir as conciliações com as divergências justificadas | Contador da conciliação |
| 4 | Validar que não há lançamento em rascunho | Contabilidade |
| 5 | Fechar o exercício no sistema | Operação |
| 6 | Emitir o relatório de execução para prestação de contas | Contabilidade |
| 7 | Arquivar os documentos de comprovação no DOM-GDO | Contabilidade |

---

# 7. Indicadores de Serviço

| Indicador | Meta | Medição |
| --- | --- | --- |
| Disponibilidade | ≥ 99,5 % mensal | Sondas de saúde |
| Tempo médio de resposta | ≤ 1 hora (N2 e N3) | Sistema de chamados |
| Taxa de resolução no prazo | ≥ 95 % | Sistema de chamados |
| Incidentes de integridade de dados | Zero | Revisão de auditoria |
| Falhas de transação entre domínios | Zero | Testes de falha transacional |
| Chamados de primeiro contato resolvidos | ≥ 60 % | Sistema de chamados |

---

# 8. Comunicação com Usuários

| Situação | Ação |
| --- | --- |
| Falha programada | Comunicar com 24 h de antecedência |
| Falha não programada | Comunicar em até 15 minutos |
| Resolução | Comunicar junto com a análise de causa |
| Mudança de escopo | Comunicar com 5 dias de antecedência |
| Manutenção de rotina | Janela mensal de baixa duração |

---

# 9. Ferramentas

| Ferramenta | Uso |
| --- | --- |
| Logs da aplicação | Diagnóstico de falhas |
| `information_schema` | Verificação de estrutura |
| Health-check da API | Monitoramento de disponibilidade |
| Sistema de chamados | Registro e acompanhamento |
| Testes automatizados | Verificação após correção |

---

# 10. Riscos Operacionais

| Risco | Probabilidade | Impacto | Mitigação |
| --- | --- | --- | --- |
| Falha na gravação após débito na dotação | Média | **Alto** | Teste de falha transacional (Onda 3) |
| Perda de dados pela falta de índice em consulta | Média | Médio | Criar índices (Onda 1) |
| Indisponibilidade em prazo de fechamento | Baixa | **Alto** | Plantão e procedimento de retorno |
| Acesso indevido a dados do favorecido | Baixa | **Alto** | Autorização por perfil (Onda 3) |
| Divergência entre ORM e banco | Alta | Alto | Validação de metadados (Onda 1) |


---

Este artefato define o plano de suporte e operação do domínio de Contabilidade
Pública, abrangendo níveis de atendimento, classificação de incidentes, rotinas
operacionais e indicadores de serviço.

---

# 2. Modelo de Serviço

| Aspecto | Definição |
| --- | --- |
| Classificação | Criticidade do impacto sobre a execução da despesa |
| Horário | Segunda a sexta, das 8 h às 17 h; plantão em prazos de encerramento |
| Canais | Sistema de chamados, e-mail e telefone da equipe de TI |
| Responsável primário | Equipe SIGMUN |
| Responsável de negócio | Contabilidade municipal |

---

# 3. Níveis de Atendimento

| Nível | Descrição | Prazo de resposta | Prazo de solução |
| --- | --- | --- | --- |
| N1 — Atendimento | Dúvida de uso, orientação | 4 horas | 2 dias úteis |
| N2 — Incidente | Operação impedida | 1 hora | 1 dia útil |
| N3 — Falha crítica | Impacto financeiro ou no orçamento | 30 minutos | 4 horas |
| N4 — Emergência | Indisponibilidade em prazo de fechamento | 15 minutos | 1 hora |

---

# 4. Classificação de Incidentes

| Categoria | Exemplo | Nível | Ação |
| --- | --- | --- | --- |
| Regra de negócio | Empenho recusado por saldo insuficiente | N1 | Orientar sobre a dotação |
| Regra de negócio | Número de empenho já utilizado | N1 | Orientar sobre a numeração |
| Integração | Dotação não localizada | N3 | Verificar cadastro no DOM-ORC |
| Integração | Divergência de saldo após empenho | N3 | Estornar conforme procedimento |
| Dados | Lançamento sem data de competência | N3 | Registrar a data manualmente |
| Dados | Falha de escrita após débito na dotação | N3 | Reverter o débito no DOM-ORC |
| Aplicação | Erro 500 em serviço de contabilidade | N4 | Verificar logs e retornar versão anterior |
| Disponibilidade | API indisponível | N4 | Acionar plantão |
| Segurança | Acesso indevido | N3 | Bloquear acesso e auditar |
| Dados | Tentativa de lançamento desequilibrado | N2 | Registrar ocorrência |

---

# 5. Procedimentos Operacionais

## 5.1 Verificação Diária

| Atividade | Frequência | Responsável |
| --- | --- | --- |
| Confirmar saúde da API e do banco | Diária | Operação |
| Verificar erros no log | Diária | Operação |
| Conferir totais de empenho do dia | Diária | Contabilidade |
| Validar backups | Diária | DBA |
| Conferir fila de chamados | Diária | Suporte |

## 5.2 Rotinas Mensais

| Atividade | Frequência | Responsável |
| --- | --- | --- |
| Análise de desempenho | Mensal | Operação |
| Revisão de incidentes | Mensal | Equipe SIGMUN |
| Atualização de documentação | Mensal | Equipe SIGMUN |
| Revisão de permissões | Mensal | Segurança |

## 5.3 Rotinas Anuais

| Atividade | Frequência | Responsável |
| --- | --- | --- |
| Revisão do plano de contas | Anual | Contabilidade |
| Teste de recuperação de backup | Anual | DBA |
| Revisão de políticas de acesso | Anual | Segurança |
| Auditoria do domínio | Anual | Controle interno |

---

# 6. Reinício do Exercício Fiscal

Procedimento crítico no encerramento do exercício:

| Passo | Atividade | Responsável |
| --- | --- | --- |
| 1 | Confirmar que não há empenho pendente de pagamento | Contabilidade |
| 2 | Conciliar todas as contas bancárias do exercício | Contador da conciliação |
| 3 | Emitir as conciliações com as divergências justificadas | Contador da conciliação |
| 4 | Validar que não há lançamento em rascunho | Contabilidade |
| 5 | Fechar o exercício no sistema | Operação |
| 6 | Emitir o relatório de execução para prestação de contas | Contabilidade |
| 7 | Arquivar os documentos de comprovação no DOM-GDO | Contabilidade |

---

# 7. Indicadores de Serviço

| Indicador | Meta | Medição |
| --- | --- | --- |
| Disponibilidade | ≥ 99,5 % mensal | Sondas de saúde |
| Tempo médio de resposta | ≤ 1 hora (N2 e N3) | Sistema de chamados |
| Taxa de resolução no prazo | ≥ 95 % | Sistema de chamados |
| Incidentes de integridade de dados | Zero | Revisão de auditoria |
| Falhas de transação entre domínios | Zero | Testes de falha transacional |
| Chamados de primeiro contato resolvidos | ≥ 60 % | Sistema de chamados |

---

# 8. Comunicação com Usuários

| Situação | Ação |
| --- | --- |
| Falha programada | Comunicar com 24 h de antecedência |
| Falha não programada | Comunicar em até 15 minutos |
| Resolução | Comunicar junto com a análise de causa |
| Mudança de escopo | Comunicar com 5 dias de antecedência |
| Manutenção de rotina | Janela mensal de baixa duração |

---

# 9. Ferramentas

| Ferramenta | Uso |
| --- | --- |
| Logs da aplicação | Diagnóstico de falhas |
| `information_schema` | Verificação de estrutura |
| Health-check da API | Monitoramento de disponibilidade |
| Sistema de chamados | Registro e acompanhamento |
| Testes automatizados | Verificação após correção |

---

# 10. Riscos Operacionais

| Risco | Probabilidade | Impacto | Mitigação |
| --- | --- | --- | --- |
| Falha na gravação após débito na dotação | Média | **Alto** | Teste de falha transacional (Onda 3) |
| Perda de dados pela falta de índice em consulta | Média | Médio | Criar índices (Onda 1) |
| Indisponibilidade em prazo de fechamento | Baixa | **Alto** | Plantão e procedimento de retorno |
| Acesso indevido a dados do favorecido | Baixa | **Alto** | Autorização por perfil (Onda 3) |
| Divergência entre ORM e banco | Alta | Alto | Validação de metadados (Onda 1) |

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 024-Plano-de-Suporte-e-Operacao-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
